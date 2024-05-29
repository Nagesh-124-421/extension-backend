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


sample1="""
Build your product View Product The ultimate game-changer in e-commerce management The Orderhive ecommerce automation platform, now owned by Cin7 , enables wholesalers and retailers manage inventory, orders, product listings, shipping, warehouses, returns, and more. 3.2K+ Active Customers 450+ Integrations 1M+ Transactions Processed Daily Build your Product Read Case Study Revolutionary AI-powered job-matching platform for recruiters and job seekers Through JobTatkal, recruiters can post their requirements, and Artificial Intelligence will parse through millions of CVs uploaded by job seekers to find the best match. 10x faster profile setup with AI parsing of CVs 91% less hiring time with AI candidate search 7x faster job posting with AI-driven job descriptions Build your Product Read Case Study Software Solutions for SMEs and Enterprises Our impressive results across a variety of industries: Healthcare E-commerce BFSI Education Logistic Energy & Utility Sports View All Healthcare IIAM - The Next-gen Patient Management Mobile Application Created for doctors from John Hopkins Research Institute, IIAM is a patient management platform that sorts the patient’s information and stores it locally on their mobiles Explore AWS IONIC Native Android NodeJS E-commerce Orderhive - A SaaS-based Ecommerce Automation Software Cin7 Orderhive is SaaS product developed for buyers and vendors that helps them manage and update inventory, orders, shipping details, warehouse etc. seamlessly Explore AWS Java MySQL NodeJS BFSI Power Traveller - An App for Power Credit Cardholders Power Traveller is a reward planning application, developed for Ajman Bank to increase user engagement. The application was built to help power card holders avail multiple benefits Explore AWS Java NodeJS Swift Education TracPrac - Competency and LMS Platform For Nursing Students TracPrac is a clinical application built for nursing students to track their attendance and evaluate their performance via reports that can be accessed through the application. Explore Java MySQL NodeJS ReactJS Logistic Mover Storage - A Warehouse Storage Management App Mover Storage is a mobile application for storage management of warehouses built by OpenXcell. The app helps users allocate units for storage and tracks status of deliveries Explore iOS NodeJS Energy & Utility Step-Up - A Waste Management App for the Citizens Step Up is a waste management application used in Singapore to manage recyclable waste. It is a user reward system which credits its users C02 points against carbon emission Explore iOS Kotlin ReactJS Swift Sports AthletesGoLive - A Platform For Sports Enthusiasts AthletesGoLive is a creative application for aspiring athletes and sports followers that allows recording of performances along with live streaming capabilities Explore AWS Mongo DB We Love Happy Clients! Client satisfaction is our ultimate goal. Here are some testimonials from our clients expressing their satisfaction with our software development solutions Eliza Greene Director, GRNSTR I will rate OpenXcell 5 on 5 for their exceptional work! × Lisa Bailey Founder, DockHere I couldn’t thank OpenXcell more in terms of giving valuable suggestions. They were always available to discuss the design and feasibility of the project. The core strengths of OpenXcell are their expertise, patience, etc. × Franz A. Wakefield CEO And Founder , CoolTVNetwork OpenXcell Team was highly professional, detail-oriented & committed to giving the highest quality product. × Bryan Rivers CEO, Malibbo It's been great to work with the team, this is my second project. I truly appreciate each and every one of your efforts. We are almost there, a couple of more weeks and I think we will be able to take this leap. × Christina Delord Founder, TracPrac They understood our idea, had realistic timelines, and offered innovative suggestions for our software. You can depend on their creativity, expertise, and reliable service to complete your project, big or small. × SEE ALL TESTIMONIALS What Makes Us The Ideal Bespoke Software Development Company Some of the reasons why clients choose and recommend our software development services company 1000+ Happy Customers A wide client base across various industries 
        """
        
sample2="""

Build your Product. Read Case Study
### The fastest way to make Bitcoin payments globally
Make lightning-fast payments with your Bitcoin. Speed Wallet- the Bitcoin li- **50K+ Downloads**
- **35K+ Active users**
- **21+ Countries Served**
Build your product. View Product
### The ultimate game-changer in e-commerce management
The Orderhive ecommerce automation platform, now owned by Cin7 , enables who- **3.2K+ Active Customers**
- **450+ Integrations**
- **1M+ Transactions Processed Daily**
Build your Product. Read Case Study
### Revolutionary AI-powered job-matching platform for recruiters and job seThrough JobTatkal, recruiters can post their requirements, and Artificial In- **10x faster profile setup with AI parsing of CVs**
- **91% less hiring time with AI candidate search**
- **7x faster job posting with AI-driven job descriptions**
Build your Product. Read Case Study
---
## Software Solutions for SMEs and Enterprises
Our impressive results across a variety of industries:
- **Healthcare**
- **E-commerce**
- **BFSI**
- **Education**
- **Logistic**
- **Energy & Utility**
- **Sports**
---
## Healthcare
### IIAM - The Next-gen Patient Management Mobile Application
Created for doctors from John Hopkins Research Institute, IIAM is a patient - **Technology Stack:** AWS, IONIC, Native Android, NodeJS
---
## E-commerce
### Orderhive - A SaaS-based Ecommerce Automation Software
Cin7 Orderhive is SaaS product developed for buyers and vendors that helps t- **Technology Stack:** AWS, Java, MySQL, NodeJS
---
## BFSI
### Power Traveller - An App for Power Credit Cardholders
Power Traveller is a reward planning application, developed for Ajman Bank t- **Technology Stack:** AWS, Java, NodeJS, Swift
---
## Education
### TracPrac - Competency and LMS Platform For Nursing Students
TracPrac is a clinical application built for nursing students to track their- **Technology Stack:** Java, MySQL, NodeJS, ReactJS
---
## Logistic
### Mover Storage - A Warehouse Storage Management App
Mover Storage is a mobile application for storage management of warehouses b- **Technology Stack:** iOS, NodeJS
---
## Energy & Utility
### Step-Up - A Waste Management App for the Citizens
Step Up is a waste management application used in Singapore to manage recycl- **Technology Stack:** iOS, Kotlin, ReactJS, Swift
---
## Sports
### AthletesGoLive - A Platform For Sports Enthusiasts
AthletesGoLive is a creative application for aspiring athletes and sports fo- **Technology Stack:** AWS, Mongo DB
---
## We Love Happy Clients!
Client satisfaction is our ultimate goal. Here are some testimonials from ou**Eliza Greene**
*Director, GRNSTR*
I will rate OpenXcell 5 on 5 for their exceptional work!
**Lisa Bailey**
*Founder, DockHere*
I couldn’t thank OpenXcell more in terms of giving valuable suggestions. The**Franz A. Wakefield**
*CEO And Founder, CoolTVNetwork*
OpenXcell Team was highly professional, detail-oriented & committed to givin**Bryan Rivers** 
*CEO, Malibbo*
It's been great to work with the team, this is my second project. I truly ap**Christina Delord**
*Founder, TracPrac*
They understood our idea, had realistic timelines, and offered innovative su---
## What Makes Us The Ideal Bespoke Software Development Company
Some of the reasons why clients choose and recommend our software developmen- **1000+ Happy Customers:** A wide client base across various industrie

"""



class OpenAI:
    def __init__(self, html_data, user_query,model='gpt-3.5-turbo-0125'):
        self.html_data = html_data
        self.user_query = user_query
        self.responses = []
        self.model=model
        
        
        self.chunkSIZE=15000
        if self.model in ['gpt-4-turbo','gpt-4o']:
            self.chunkSIZE=120000

    def chunk_data(self,data,chunk_size_provided=None):
        chunk_size=self.chunkSIZE
        if chunk_size_provided:
            chunk_size=chunk_size_provided
        chunks = []
        num_chunks = math.ceil(len(data) / chunk_size)
        for i in range(num_chunks):
            start = i * chunk_size
            end = min((i + 1) * chunk_size, len(data))
            chunks.append(data[start:end])
        return chunks

    async def gpt(self, chunk_data_user_query):
        chunk_data, user_query = chunk_data_user_query
        instruction='Note :If your answer has code added in then please provide thripple comma langige name , code and then close with thripple comma'
        instruction2='Note : i am using 700px by 540px screen so , your markdown respose should add new line accordingly'
        instruction3=',Give me your answer in resposive markdown language format'
        instruction4="Find relavent information from Context Section for Question Asked in Question Section, Note : If Context section is ; no information found ,response As No Information Found as well in return... "
        
        final_instruction=instruction4+'1)'+instruction+'2)'+instruction2 +'3)'+instruction3
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                # {"role": "system", "content": f"Your job is to answer the user query using only this information: {chunk_data}, \
                #     you can't use outside information. If you can't find anything, just respond with 'I AM SORRY!'."},
                {"role":"system","content":final_instruction},
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
        messages=[
            {"role": "user", "content": userQuery}
            ],
        stream=True
        )

        return stream
    
    def ask_gpt_for_markdown(self,raw_text):
        try:
            userQuery="convert this to markdown fromat for attached Raw Text, dont explain , dont say anything , just return with converted markdown"
            chunks=self.chunk_data(raw_text,10000)
            markdown_code=''
            for chunk in chunks:
                content =f"""
                        {userQuery}....
                        Raw Text: 
                        {chunk} 
                        """
        
                response = client.chat.completions.create(
                    model=self.model,
                    messages=[
                        # {"role": "user", "content": userQuery+'Raw Text:'+sample1},
                        # {"role": "assistant", "content": sample2},
                        
                        
                        
                        
                        
                        
                        {"role": "user", "content": content},
                    ]
                )
            
                markdown_code+=response.choices[0].message.content
                print('---------------------',len(response.choices[0].message.content))
            
            return markdown_code
        except Exception as e:
            print(f"Error While ask_gpt_for_markdown ",e)
            return ''






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




# html_content="""

# Amazon.in - Deals Skip to main content .in Delivering to Rajkot 360004 Update location Deals Select the department you want to search in Deals All Categories Alexa Skills Amazon Devices Amazon Fashion Amazon Pharmacy Appliances Apps & Games Audible Audiobooks Baby Beauty Books Car & Motorbike Clothing & Accessories Collectibles Computers & Accessories Electronics Furniture Garden & Outdoors Gift Cards Grocery & Gourmet Foods Health & Personal Care Home & Kitchen Industrial & Scientific Jewellery Kindle Store Luggage & Bags Luxury Beauty Movies & TV Shows MP3 Music Music Musical Instruments Office Products Pet Supplies Prime Video Shoes & Handbags Software Sports, Fitness & Outdoors Subscribe & Save Tools & Home Improvement Toys & Games Under ₹500 Video Games Watches Search Amazon.in EN Hello, sign in Account & Lists Returns & Orders 0 Cart All Amazon miniTV Sell Best Sellers Today's Deals Mobiles Electronics Prime Customer Service Home & Kitchen Fashion New Releases Amazon Pay Computers Gift Ideas Books Car & Motorbike Home Improvement Toys & Games Coupons Beauty & Personal Care Sports, Fitness & Outdoors Grocery & Gourmet Foods Gift Cards Health, Household & Personal Care Baby Video Games Custom Products Pet Supplies AmazonBasics Audible Subscribe & Save Kindle eBooks Today's Deals All Deals Watched Deals Subscribe & Save Coupons Clearance Refurbished & Open Box Today's Deals Previous Deal of the Day Lightning Deals Mobiles Electronics Mobiles & computer accessories Large Appliances Home & Kitchen Furniture Grooming & Wellness Health & Household Clothing Footwear Beauty & Makeup Jewellery, Luggage, Watches Kids & Baby Amazon Brands & more Grocery Sports & Fitness Books & Stationery Car & motorbike accessories Pet Supplies Video games & Software Musical Instruments Amazon Business Next Discount grid Department All Amazon Devices & Accessories Appliances Apps for Android Baby See more filter options See more Customer Reviews All and up and up and up and up Price All Under ₹500 ₹500 to ₹1,000 ₹1,000 to ₹2,000 ₹2,000 to ₹5,000 ₹5,000 and Above Discount All 10% off or more 25% off or more 50% off or more 70% off or more Prime Programmes Prime Exclusive Prime Early Access 25% off Limited time deal Redmi 13C 5G (Startrail Silver, 4GB RAM, 128GB Storage) | MediaTek Dimensity 6100+ 5G | 90Hz Display Redmi 13C 5G (Startrail Silver, 4GB RAM, 128GB St… Save ₹1,000.00 with coupon 20% off Limited time deal iQOO Z9 5G (Brushed Green, 8GB RAM, 128GB Storage) | Dimensity 7200 5G Processor | Sony IMX882 OIS Camera | 120Hz AMOLED with 1800 nits Local Peak Brightness | 44W Charger in The Box iQOO Z9 5G (Brushed Green, 8GB RAM, 128GB Storage)… 31% off Limited time deal Redmi 12 5G Jade Black 6GB RAM 128GB ROM Redmi 12 5G Jade Black 6GB RAM 128GB ROM Save ₹1,000.00 with coupon 49% off Limited time deal Voltas 1.5 ton 3 Star, Inverter Split AC (Copper, 4-in-1 Adjustable Mode, Anti-dust Filter, 2024 Model, 183V Vectra CAW, White) Voltas 1.5 ton 3 Star, Inverter Split AC (Copper, 4-in-1 Adj… 44% off Limited time deal Lloyd 1.5 Ton 3 Star Inverter Split AC (5 in 1 Convertible, Copper, Anti-Viral + PM 2.5 Filter, 2023 Model, White with Chrome Deco Strip, GLS18I3FWAGC) Lloyd 1.5 Ton 3 Star Inverter Split AC (5 in 1 Convertible,… 19% off Limited time deal Redmi Note 13 5G (Arctic White, 6GB RAM, 128GB Storage) | 5G Ready | 120Hz Bezel-Less AMOLED | 7.mm Slimmest Note Ever | 108MP Pro-Grade Camera Redmi Note 13 5G (Arctic White, 6GB RAM, 128GB St… +2 colours/patterns 37% off Limited time deal Daikin 1.5 Ton 3 Star Inverter Split AC (Copper, PM 2.5 Filter, Triple Display, Dew Clean Technology, Coanda Airflow, 2023 Model, MTKL50U, White) Daikin 1.5 Ton 3 Star Inverter Split AC (Copper, PM 2.5 Fil… 22% off Limited time deal realme NARZO 70 Pro 5G (Glass Green, 8GB RAM,256GB Storage) Dimensity 7050 5G Chipset | Horizon Glass Design | Segment 1st Flagship Sony IMX890 OIS Camera realme NARZO 70 Pro 5G (Glass Green, 8GB RAM,25… 40% off Limited time deal Lloyd 1.5 Ton 5 Star Inverter Split AC (5 in 1 Convertible, Anti Corrosion Coating, Copper, PM 2.5 Filter, 2024 Model, White with Chrome Deco Strip, GLS18I5FWBEW) Lloyd 1.5 Ton 5 Star Inverter Split AC (5 in 1 Convertible,… 36% off Limited time deal Redmi 13C (Starshine Green, 4GB RAM, 128GB Storage) | Powered by 4G MediaTek Helio G85 | 90Hz Display | 50MP AI Triple Camera Redmi 13C (Starshine Green, 4GB RAM, 128GB Storage)… 29% off Limited time deal Samsung 653 L, 3 Star, Frost Free, Double Door, Convertible 5-in-1 Digital Inverter, Side By Side AI Enabled Smart Refrigerator with WiFi (RS76CG8003S9HL, Silver, Refined Inox, 2024 Model) Samsung 653 L, 3 Star, Frost Free, Double Door, Converti… Save ₹3,000.00 with coupon 33% off Limited time deal Panasonic 1.5 Ton 3 Star Wi-Fi Inverter Smart Split AC (Copper Condenser, 7 in 1 Convertible with True AI Mode, PM 0.1 Air Purification Filter, CS/CU-SU18ZKYWT, 2024 Model, White) Panasonic 1.5 Ton 3 Star Wi-Fi Inverter Smart Split AC (… Limited time deal Oneplus Nord CE4 (Dark Chrome, 8GB RAM, 128GB Storage) Oneplus Nord CE4 (Dark Chrome, 8GB RAM, 128GB… 50% off Limited time deal Voltas 1.4 ton 5 Star, Inverter Split AC (Copper, 4-in-1 Adjustable Mode, Anti-dust Filter, 2024 Model, 175V Vectra CAR, White) Voltas 1.4 ton 5 Star, Inverter Split AC (Copper, 4-in-1 Adj… 35% off Limited time deal Lava Agni 2 5G (Glass Viridian, 8GB RAM, 256GB Storage) | India's First Dimensity 7050 Processor | 120 Hz Curved Amoled Display | 13 5G Bands | Superfast 66W Charging | Clean Android Lava Agni 2 5G (Glass Viridian, 8GB RAM, 256GB… 44% off Limited time deal Sony Bravia 139 cm (55 inches) 4K Ultra HD Smart LED Google TV KD-55X74L (Black) Sony Bravia 139 cm (55 inches) 4K Ultra HD Smart… 50% off Limited time deal MI 80 cm (32 inches) A Series HD Ready Smart Google TV L32M8-5AIN (Black) MI 80 cm (32 inches) A Series HD Ready Smart Google T… 14% off Limited time deal Redmi Note 13 Pro (Coral Purple, 8GB RAM, 128GB Storage) | 1.5K AMOLED | 200MP Hi-Res Camera | Flagship 4nm SD 7s Gen 2 | 67W TurboCharge Redmi Note 13 Pro (Coral Purple, 8GB RAM, 128GB S… Javascript Required We're sorry, but this widget requires JavaScript. Please enable JavaScript to interact with it! Selecting deals from preset: All Deals Shop collections Previous page All Deals Deal of the Day Lightning Deals Mobiles Electronics Mobiles & computer accessories Beauty & Makeup Clothing Footwear Jewellery, Luggage, Watches Amazon Brands & more Health & Household Home & Kitchen Grocery Books & Stationery Grooming & Wellness Kids & Baby Sports & Fitness Car & motorbike accessories Musical Instruments Pet Supplies Video games & Software Large Appliances Furniture Gift cards Amazon Business Next page Sort deals by Sort by: Featured Sort by: Discount - Low to High Sort by: Discount - High to Low Sort by: Price - Low to High Sort by: Price - High to Low Deals filters All deals Available Upcoming Watchlist Price All Under ₹500 ₹500 to ₹1,000 ₹1,000 to ₹2,000 ₹2,000 to ₹5,000 ₹5,000 and Above Discount All deals 10% off or more 25% off or more 50% off or more 70% off or more Average Customer Review and up and up and up and up Deal type All deals Deal of the day Lightning deal Best deal Prime Programmes Prime eligible Prime Early Access deals Prime Exclusive deals Loaded new deals Deals grid Up to 25% off Limited time deal Up to 25% off Limited time deal Redmi 13C 5G (Starting from 9499/- inclduing additional offers) Up to 20% off Limited time deal Up to 20% off Limited time deal iQOO Z9 5G | Starting @17999 Including add. Offers Up to 31% off Limited time deal Up to 31% off Limited time deal Redmi 12 5g (Starting from 9999/- inclduing additional offers) Up to 90% off Limited time deal Up to 90% off Limited time deal Fireboltt Asphalt New Launch Smartwatch Limited time deal Limited time deal OnePlus Nord CE4 (Starting from 22999/- including additional offers) Up to 80% off Ends in 05:22:50 Up to 80% off Ends in 05:22:50 Summer Sale from Ptron- Music Fest 39% off Limited time deal 39% off Limited time deal Redmi 13c (Starting from 7699/- inclduing additional offers) Up to 76% off Limited time deal Up to 76% off Limited time deal Branded Suitcase, Backpacks and Duffles - American Tourister, Safari, Skybags, etc. Up to 81% off Limited time deal Up to 81% off Limited time deal All Clothing: Levi's, BIBA, U.S.POLO ASSN. and more Up to 19% off Limited time deal Up to 19% off Limited time deal Redmi note 13 5g (Starting from 15499/- inclduing additional offers) Up to 4% off Limited time deal Up to 4% off Limited time deal Deals on Samsung Fold and Flip Limited time deal Limited time deal OnePlus 12R (Starting from 37999/- including additional offers) Up to 14% off Limited time deal Up to 14% off Limited time deal Redmi note 13 pro (Starting from 21999/- inclduing additional offers) Up to 24% off Limited time deal Up to 24% off Limited time deal Starting from 19999 including additional offers Up to 53% off Limited time deal Up to 53% off Limited time deal Mega Discounts on Mivi Earbuds Up to 31% off Limited time deal Up to 31% off Limited time deal Laptops Starting INR 19990; Upto 6 months NCE Up to 30% off Limited time deal Up to 30% off Limited time deal Best Selling Printer starting at Rs 3249 – HP, Canon and Epson 40% off Limited time deal 40% off Limited time deal iQOO Z6 Lite | Starting @10999 Including add. Offers Up to 48% off Limited time deal Up to 48% off Limited time deal Deal of the Day on Grocery Up to 87% off Limited time deal Up to 87% off Limited time deal Made for Amazon - Clothing Bestsellers Up to 73% off Limited time deal Up to 73% off Limited time deal Top Home Picks Up to 73% off Limited time deal Up to 73% off Limited time deal Deal of the day Up to 9% off Limited time deal Up to 9% off Limited time deal Redmi note 13 pro + (Starting from 27999/- inclduing additional offers) Up to 76% off Limited time deal Up to 76% off Limited time deal Deal Of The Day Up to 82% off Ends in 05:22:50 Up to 82% off Ends in 05:22:50 Curated Deals on Mobile Accessories -  Buy or Loose Up to 47% off Limited time deal Up to 47% off Limited time deal Deal of the day 35% off Limited time deal 35% off Limited time deal Lava Agni 2 Available at Rs. 16,999 Up to 75% off Limited time deal Up to 75% off Limited time deal Robotic, Handheld Vacuum cleaners & accessories 38% off Limited time deal 38% off Limited time deal Starting from 6199 including additional offers Up to 86% off Limited time deal Up to 86% off Limited time deal Unbeatable price on boAt smartwatches starting 899 Restrictions apply ← Previous 1 2 3 ... 294 Next → Javascript Required We're sorry, but this widget requires JavaScript. Please enable JavaScript to interact with it! Your recently viewed items and featured recommendations › View or edit your browsing history After viewing product detail pages, look here to find an easy way to navigate back to pages you are interested in. Your recently viewed items and featured recommendations › View or edit your browsing history After viewing product detail pages, look here to find an easy way to navigate back to pages you are interested in. Back to top Get to Know Us About Us Careers Press Releases Amazon Science Connect with Us Facebook Twitter Instagram Make Money with Us Sell on Amazon Sell under Amazon Accelerator Protect and Build Your Brand Amazon Global Selling Become an Affiliate Fulfilment by Amazon Advertise Your Products Amazon Pay on Merchants Let Us Help You COVID-19 and Amazon Your Account Returns Centre 100% Purchase Protection Amazon App Download Help English India AbeBooks Books, art & collectibles Amazon Web Services Scalable Cloud Computing Services Audible Download Audio Books IMDb Movies, TV & Celebrities Shopbop Designer Fashion Brands Amazon Business Everything For Your Business Prime Now 2-Hour Delivery on Everyday Items Amazon Prime Music 100 million songs, ad-free Over 15 million podcast episodes Conditions of Use & Sale Privacy Notice Interest-Based Ads © 1996-2024, Amazon.com, Inc. or its affiliates
# """
# userQuery,html_data="Give me all mobile phones details?",html_content
# openAI=OpenAI(html_data,userQuery,'gpt-4o')
# chunks=openAI.chunk_data(html_data)

# streams=[]
# for chunk in chunks:
#     stream=openAI.askGPT('MyQuestion : '+userQuery+'.Here I am Providing detials , you can only use this detials to answer my question. Details Provided: '+chunk+'Note: If you dont find provided Details not related to my question just answer with I DONT KNOW')
#     streams.append(stream)


# response=[]
# for stream in streams:
#     for chunk in stream:
#         if chunk.choices[0].delta.content is not None:
#             chunkData=chunk.choices[0].delta.content
#             #print(chunkData)
#             response.append(chunkData)
#     response.append('---------------------------------')


# def save_in_text_file(file_name,chunk_data_list):
#     # Open the file in write mode and store the chunk data
#     with open(file_name, 'w') as file:
#         for chunk_data in chunk_data_list:
#             file.write(chunk_data + "\n")  # Write each chunk data followed by a newline character

# save_in_text_file('hitler_ww2.txt',response)
