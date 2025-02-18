import os
import requests
from dotenv import load_dotenv
import json
load_dotenv()
api_key = os.getenv("SCRAPING_API_KEY")

def scrape_linkedin(profile_url:str, mock:bool=False):
    if mock:
        profile_url  = "https://gist.githubusercontent.com/Suhas-199915/bd8653878027b60920d5e01c3a723218/raw/73f88c1fb4dc0fd5a49a7f799538a4d2411be2dc/suhas-scraping.json"
        response = requests.get(profile_url, timeout=10)
    else :
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        headers = {'Authorization': 'Bearer ' + api_key}
        params = {
            'linkedin_profile_url': profile_url
        }
        response = requests.get(api_endpoint,params=params,headers=headers)


        return response.json()
        

if __name__ == "__main__":
    data = scrape_linkedin("www.linkedin.com/in/suhas-kulkarni-aa5627221", mock=True)
    
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)