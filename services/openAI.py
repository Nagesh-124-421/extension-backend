from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime


load_dotenv()  # take environment variables from .env.

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


# stream = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Full hitler bioagraphy in 2000 character"}],
#     stream=True,
# )


# def askGPT(userQuery):
#     stream = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{
#         "role": "user", 
#         "content": userQuery}],
#     stream=True
#     )
#     for chunk in stream:
#         if chunk.choices[0].delta.content is not None:
#             print(chunk.choices[0].delta.content, end="")

#     return stream



import math
import asyncio



class OpenAI:
    def __init__(self, html_data, user_query,model='gpt-3.5-turbo-0125'):
        self.html_data = html_data
        self.user_query = user_query
        self.responses = []
        self.model=model
        
        
        self.chunkSIZE=15000
        if self.model in ['gpt-4-turbo','gpt-4o']:
            self.chunkSIZE=120000

    @staticmethod
    def chunk_data(data, chunk_size=15000):
        chunks = []
        num_chunks = math.ceil(len(data) / chunk_size)
        for i in range(num_chunks):
            start = i * chunk_size
            end = min((i + 1) * chunk_size, len(data))
            chunks.append(data[start:end])
        return chunks

    async def gpt(self, chunk_data_user_query):
        chunk_data, user_query = chunk_data_user_query
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                # {"role": "system", "content": f"Your job is to answer the user query using only this information: {chunk_data}, \
                #     you can't use outside information. If you can't find anything, just respond with 'I AM SORRY!'."},
                {"role": "user", "content": user_query+chunk_data},
            ]
        )
        
        self.responses.append(response.choices[0].message.content)

    async def process_chunks(self):
        chunk_size = self.chunkSIZE
        chunks = self.chunk_data(self.html_data, chunk_size)
        chunk_data_user_query = [(chunk, self.user_query) for chunk in chunks]
        
        tasks = [self.gpt(chunk_user_query) for chunk_user_query in chunk_data_user_query]
        await asyncio.gather(*tasks)
        
        
    def format_responses(self):
            # Filter out "I AM SORRY!" responses
            filtered_responses = [response for response in self.responses if "I AM SORRY!".lower() not in response.lower()]
            # Join and format remaining responses
            final_response = "...".join(filtered_responses)
            return final_response

    def askGPT(self,userQuery):
        stream = client.chat.completions.create(
        model=self.model,
        messages=[{
            "role": "user", 
            "content": userQuery}],
        stream=True
        )

        return stream





# # Define the location of the file to read
# file_location = "response_1715765359834.json"
# import json
# # Read the JSON data from the file
# with open(file_location, "r") as file_object:  # Open the file in read mode
#     html_data= json.load(file_object)  # Load JSON data from the file

# print(len(html_data))
# user_query = 'what is element_text function,give me response in responsive markdown languge'

# openAI=OpenAI(html_data,user_query,'gpt-4-turbo')
# asyncio.run(openAI.process_chunks())

# final_output = openAI.format_responses()
# print('------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..')
# print(final_output)




