from fastapi import FastAPI,WebSocket, WebSocketDisconnect,Depends
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from manageSocket.manager import ConnectionManager
from services.openAI import OpenAI
import asyncio

from services.scrap import Amazon,Beautiful_Soup,WebScrapper
import json
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from db.database import SessionLocal,engine

from db.schemas import HtmlContentRequest
from db import models
from services.backend import vectorize_text,get_matched_content

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


from pprint import pprint



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
            else:
                response=WebScrapper(url=url).scrap()
            response=response.json()
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

    


    



# @app.websocket("/communicate")
# async def websocket_endpoint(websocket: WebSocket):
#     await manager.connect(websocket)
#     try:
#         while True:
#             data = await websocket.receive_text()
#             data=data.split('????')
#             userQuery,html_data,selectedModel=data[0],data[1],data[2]
#             openAI=OpenAI(html_data,userQuery,selectedModel)
#             chunks=openAI.chunk_data(html_data)
            
#             streams=[]
#             for chunk in chunks:
#                 stream=openAI.askGPT('MyQuestion : '+userQuery+'.Here I am Providing detials , you can only use this detials to answer my question. Details Provided: '+chunk+'Note: If you dont find provided Details not related to my question just answer with I DONT KNOW')
#                 streams.append(stream)
                
#             for stream in streams:
#                 for chunk in stream:
#                     chunk_response=chunk.choices[0].delta.content
#                     if chunk_response is not None:
#                         chunkData=chunk.choices[0].delta.content
#                         await manager.send_personal_message(chunkData, websocket)
#                         await asyncio.sleep(0.1)
           
#     except WebSocketDisconnect:
#         manager.disconnect(websocket)
#         await manager.broadcast(f"Client  left the chat")




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
            
            content =f"""Find relavent information from Context Section for Question Asked in Question Section, 
                        Note : If Context section is ; no information found , then response As No Information Found as well in return... 
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
           
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client  left the chat")

