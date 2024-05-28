import requests
from pprint import pprint
from dotenv import load_dotenv
import os
import json
from bs4 import BeautifulSoup



load_dotenv()  # take environment variables from .env.




# pprint(json.dumps(response.json(), indent=4))

# pprint(response.json())



class Amazon():
    def __init__(self,url):
        self.payload = {
            'source': 'amazon',
            'url':url,
            "render" : "html",
            'user_agent_type':'desktop_chrome',
            # "parse" : True
        }


        self.OXYLABS_ECOMMERCE_USERNAME=os.environ.get("OXYLABS_ECOMMERCE_USERNAME")
        self.OXYLABS_ECOMMERCE_PASSWORD=os.environ.get("OXYLABS_ECOMMERCE_PASSWORD")



    def scrap(self):
        # Get response.
        response = requests.request(
            'POST',
            'https://realtime.oxylabs.io/v1/queries',
            auth=(self.OXYLABS_ECOMMERCE_USERNAME, self.OXYLABS_ECOMMERCE_PASSWORD),
            json=self.payload,
        )
        
        return response



class File():
    def __init__(self,response):
        self.response=response
    
    def write_json_file(self,file_location): #"temp/testuk_3.json"
        try:
            # Define the location where the file will be saved
            os.makedirs(os.path.dirname(file_location), exist_ok=True)

            # Write the JSON data to the file
            with open(file_location, "w") as file_object:  # Open the file in text mode for writing JSON
                json.dump(self.response.json(), file_object, indent=4)
        except Exception as e:
            print(e)



class WebScrapper():
    def __init__(self,url):
        self.payload={
            'source': 'universal',
            'url':url,
            'render' : 'html',
            # 'user_agent_type':'desktop_chrome',
            # 'parse':True
            
        }
        self.OXYLABS_WEB_SCRAPPER_USERNAME=os.environ.get("OXYLABS_WEB_SCRAPPER_USERNAME")
        self.OXYLABS_WEB_SCRAPPER_PASSWORD=os.environ.get("OXYLABS_WEB_SCRAPPER_PASSWORD")



    def scrap(self):
        print(self.OXYLABS_WEB_SCRAPPER_USERNAME,self.OXYLABS_WEB_SCRAPPER_PASSWORD)
        # Get response.
        response = requests.request(
            'POST',
            'https://realtime.oxylabs.io/v1/queries',
            auth=(self.OXYLABS_WEB_SCRAPPER_USERNAME, self.OXYLABS_WEB_SCRAPPER_PASSWORD),
            json=self.payload,
        )
        
        return response




class Beautiful_Soup():
    def __init__(self):
        pass
    
    
    def  get_only_text(self,html):
        soup = BeautifulSoup(html, 'lxml')
        # Extract all text from the parsed HTML
        text_only = soup.get_text(separator=' ', strip=True)
        
        return text_only


