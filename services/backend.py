import requests

def vectorize_text(text_value: str, chat_room_id: str):
    url = "https://ai-vector.onrender.com/vectorizeText"
    data = {
        "textValue": text_value,
        "chatRoomID": chat_room_id
    }
    
    try:
        response = requests.post(url, json=data)
        
        if response.status_code == 200 and response.json():
            response_data = response.json()
            print("Success:", response_data.get("response"))
            return True
        else:
            response_data = response.json()
            print("Error:", response_data.get("response"))
            return False

    except requests.RequestException as error:
        print("Error:", error)
        return False


def get_matched_content(user_query,chatRoomURL):
    matched_content = "no information found"
    url = "https://ai-vector.onrender.com/query"
    data={
        'query':user_query,
        'chatRoomID':chatRoomURL
        
    }
    
    try:
        response = requests.post(url, json=data)
        
        if response.status_code == 200 and response.json():
            response_data = response.json()
            print("Success:", response_data.get("response"))
            
            if response_data.get("response") and len(response_data["response"]) > 0:
                matched_content = response_data["response"]
            return  matched_content
        else:
            response_data = response.json()
            print("Error:", response_data.get("response"))
            return matched_content

    except requests.RequestException as error:
        print("Error:", error)
        return matched_content



import tldextract

def is_google_url(url):
    extracted = tldextract.extract(url)
    domain = extracted.domain
    suffix = extracted.suffix

    # Check if the domain is "google"
    if domain == "google":
        return True

    # Check for subdomains like google.com, google.co.in, google.com.au, etc.
    if domain.endswith("google") and suffix in ["com", "co.in", "com.au", "co.uk", "de", "fr", "jp", "it", "es", "br", "ca", "ru", "com.tr"]:
        return True

    return False

