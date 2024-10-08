from fastapi import FastAPI,WebSocket, WebSocketDisconnect,Depends,UploadFile , File,Request
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from manageSocket.manager import ConnectionManager
from services.openAI import OpenAI
import asyncio
from fastapi.responses import FileResponse

from services.scrap import Amazon,Beautiful_Soup,WebScrapper,Google
import json
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from db.database import SessionLocal,engine

from db.schemas import HtmlContentRequest
from db import models
from services.backend import vectorize_text,get_matched_content,is_google_url
from services.generate_markdown import generate_markdown_pdf
import os
import shutil
from services.ocr import process_pdf_and_send_ocr





# Initialize database models
models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



from pydantic import BaseModel
class UrlData(BaseModel):
    url: str
    
class UserQueryData(BaseModel):
    userQuery: str
    html_data:str



app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Adjust this in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

manager=ConnectionManager()




@app.get("/")
async def get():
    return 'test'

@app.get('/my-endpoint')
async def my_endpoint(request: Request):
    forwarded_for = request.headers.get('X-Forwarded-For')
    if forwarded_for:
        # Get the first IP in the X-Forwarded-For list, which is the client's IP
        ip = forwarded_for.split(',')[0]
    else:
        # Fallback to the request's client IP (likely to be the proxy's IP)
        ip = request.client.host

    print(ip)
    return {'status': 1, 'message': 'ok'}
    
@app.post("/")
async def post_url(data: UrlData,db: Session = Depends(get_db)):
    if 'amazon' in data.url:
        response=Amazon(url=data.url).scrap()
    else:
        response=WebScrapper(url=data.url).scrap()
    response=response.json()
    html_content=response['results'][0]['content']
    text_only=Beautiful_Soup().get_only_text(html=html_content)
    
    db_item = models.HtmlContent(urlname=data.url, htmlcontent=text_only)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    
   
    
    return db_item

    return {'data':text_only}

@app.get("/get_scrapped_content")
async def get_scrapped_content(url: str, db: Session = Depends(get_db)):
    try:
        db_item = db.query(models.HtmlContent).filter(models.HtmlContent.urlname == url).first()
        if not db_item:
            if 'amazon' in url:
                response=Amazon(url=url).scrap()
            elif is_google_url(url):
                response=Google(url=url).scrap
            else:
                response=WebScrapper(url=url).scrap()
            response=response.json()
            print(response)
            print('------------------------')
            html_content=response['results'][0]['content']
            text_only=Beautiful_Soup().get_only_text(html=html_content)
            
            db_item = models.HtmlContent(urlname=url, htmlcontent=text_only)
            db.add(db_item)
            db.commit()
            db.refresh(db_item)
            
            # Supabase
            vectorize_text(text_only,url)
    
            return db_item.htmlcontent
    
        return db_item.htmlcontent
    except Exception as e:
        print(e)
        return ''
    

@app.post("/ask_gpt")
async def ask_gpt(data:UserQueryData,db: Session = Depends(get_db)):
    try:
        userQuery,html_data=data.userQuery,data.html_data
        
        openAI=OpenAI(html_data,userQuery,'gpt-4-turbo')
        await openAI.process_chunks()

        final_output = openAI.format_responses()
    
        return {'data':final_output}
    except Exception as e:
        print(e)
        return ''

    
@app.websocket("/communicate")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            data=data.split('????')
            userQuery,current_url,selectedModel=data[0],data[1],data[2]
            
            # Find Relavent text
            matched_content=get_matched_content(userQuery,current_url)
            
            
            
            openAI=OpenAI(matched_content,userQuery,selectedModel)
            chunks=openAI.chunk_data(matched_content)
            
            content =f"""
                        Context Section: 
                        {matched_content} 
                    
                        Question Section: 
                        {userQuery} """

            
            streams=[]
            for chunk in chunks:
                stream=openAI.askGPT(content)
                streams.append(stream)
                
            for stream in streams:
                for chunk in stream:
                    chunk_response=chunk.choices[0].delta.content
                    if chunk_response is not None:
                        chunkData=chunk.choices[0].delta.content
                        await manager.send_personal_message(chunkData, websocket)
                        await asyncio.sleep(0.1)
            
            answer_finished="🚀"
            await manager.send_personal_message(answer_finished, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client  left the chat")


@app.get("/get_markdown_pdf")
async def get_markdown_pdf(url: str, db: Session = Depends(get_db)):
    try:
        # Scrap exist in db or not
        db_item = db.query(models.HtmlContent).filter(models.HtmlContent.urlname == url).first()
        if not db_item:
            # Oxylabs Get scrap
            if 'amazon' in url:
                response=Amazon(url=url).scrap()
            elif is_google_url(url):
                response=Google(url=url).scrap
            else:
                response=WebScrapper(url=url).scrap()
            response=response.json()
            html_content=response['results'][0]['content']
            print(response)
            print('--------OXY LABS RESPONSE----------------')
            
            # Beautiful soup
            text_only=Beautiful_Soup().get_only_text(html=html_content)
            # Add In DB 
            db_item = models.HtmlContent(urlname=url, htmlcontent=text_only)
            db.add(db_item)
            db.commit()
            db.refresh(db_item)
        
        text_only=db_item.htmlcontent
        # Ask Gpt For Markdown
        openAI=OpenAI(html_data="", user_query="",model='gpt-4o')
        markdown_code=openAI.ask_gpt_for_markdown(text_only)
        print(markdown_code)
                
        # Convert Markdown Into PDF
        file_path='temp/markdown.pdf'
        pdf_markdown_instance=generate_markdown_pdf(markdown_code)
        pdf_markdown_instance.save(file_path)
        
        response = FileResponse(file_path, media_type="application/pdf")
            
        return response
            
        
    except Exception as e:
        print(e)
        return FileResponse('temp/something_went_wrong.pdf',media_type="application/pdf")



@app.post("/ocr-pdf")
async def ocr_pdf(file: UploadFile = File(...)):
    try:
        if file.content_type != "application/pdf":
            return {"error": "File must be a PDF"}

        file_location = 'temp'+'/'+file.filename
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        ocr_text=process_pdf_and_send_ocr(file.filename)
        
        # Remove file
        os.remove(file_location)
    except Exception as e:
        print(e)
        return {'data':'something went wrong'}
    
    return {'data':ocr_text}
