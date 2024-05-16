from pydantic import BaseModel

class HtmlContentRequest(BaseModel):
    urlname: str
    htmlcontent: str