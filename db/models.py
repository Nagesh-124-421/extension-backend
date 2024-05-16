from sqlalchemy import Column, Integer, String, Text
from .database import Base

class HtmlContent(Base):
    __tablename__ = "html_contents"

    id = Column(Integer, primary_key=True, index=True)
    urlname = Column(String, unique=True, index=True)  # Ensures urlname is unique
    htmlcontent = Column(Text)  # Suitable for storing large HTML content
