#---importing useful libraries
import wget
import pandas as pd
import json
from bs4 import BeautifulSoup
from pandas.io.json import json_normalize

#--function used to download the data from the given link
def download_data(url):
    wget.download(url,"api.json")
    print("\n successfully downloaded...")

def get_details(path):
    #extract the json from the file
    with open(path,'r',encoding='UTF-8') as f:
        data=json.load(f)

    # Extracting episode data
    episodes_data = data['_embedded']['episodes']
    # Iterate over each episode and extract the given output attributes
    dict = {}
    for episode in episodes_data:
        id = episode['id']
        url = episode['url']
        name = episode['name']
        season = episode['season']
        number = episode['number']
        type = episode['type']
        airdate = episode['airdate']
        airtime = episode['airtime']
        runtime = episode['runtime']
        average_rating = episode['rating']['average']
        summary = BeautifulSoup(episode['summary'], "html.parser").get_text()
        medium_image = episode['image']['medium']
        original_image = episode['image']['original']
        # Print the extracted attributes
        print("Episode ID:", id)
        print("URL:", url)
        print("Name:", name)
        print("Season:", season)
        print("Number:", number)
        print("Type:", type)
        print("Airdate:", airdate)
        print("Airtime:", airtime)
        print("Runtime:", runtime)
        print("Average Rating:", average_rating)
        print("Summary:", summary)
        print("Medium Image Link:", medium_image)
        print("Original Image Link:", original_image)
        print(100*"=")
    print("\n Data Extracted Successfully...")

         
    


#--- main function to execute both the function together
if __name__ == "__main__":
    #---calling function to download the data file
    download_data("http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes")
    #---calling function to convert the data file into excel format
    get_details("api.json")
    



    
