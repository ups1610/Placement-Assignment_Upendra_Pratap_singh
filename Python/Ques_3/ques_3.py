#---importing useful libraries
import wget
import pandas as pd
import json
from pandas.io.json import json_normalize

#--function used to download the data from the given link
def download_data(url):
    wget.download(url,"pokemon.json")
    print("\n successfully downloaded...")

#---function used to convert data into excel format
def convet_to_excel(file):
     #first convert the json data in dataframe using json_normalize() function
     f = open(file)
     dict = json.load(f)     
     df = pd.json_normalize(dict['pokemon']) 
     
     #now dataframe can be converted into excel format using pandas libraries
     excel_file = "pokemon.xlsx"
     df.to_excel(excel_file)
     print("\n successfully converted...")


#--- main function to execute both the function together
if __name__ == "__main__":
    #---calling function to download the data file
    download_data("https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json")
    #---calling function to convert the data file into excel format
    convet_to_excel("pokemon.json")
    
