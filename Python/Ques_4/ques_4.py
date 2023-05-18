#---importing useful libraries
import wget
import pandas as pd
import json
from pandas.io.json import json_normalize

#--function used to download the data from the given link
def download_data(url):
    wget.download(url,"meteorite.json")
    print("\n successfully downloaded...")

#---function used to convert data into csv format
def convert_to_csv(path):
    #load the json data
    with open(path,'r',encoding='UTF-8') as f:
        data = json.loads(f.read())
    #convert the json data in dataframe
    df = pd.json_normalize(data) 

    #drop unrequired columns
    df.drop([":@computed_region_cbhk_fwbd",":@computed_region_nnqa_25f4"],axis=1,inplace=True)
    #rename columns for better connectivity
    df.rename(columns={'geolocation.type':'geolocation_type','geolocation.coordinates':'geolocation_coordinates'},inplace=True)
    df.to_csv("meteorite.csv")
    print('\n Successfully converted')


#--- main function to execute both the function together
if __name__ == "__main__":
    #---calling function to download the data file
    download_data("https://data.nasa.gov/resource/y77d-th95.json")
    #---calling function to convert the data file into excel format
    convert_to_csv("meteorite.json")