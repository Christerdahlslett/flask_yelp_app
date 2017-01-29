# Importing libaries required. 

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


# Function that gets Authentication to use the Yelp API, then it defines parameters to be used to search for the best 
# resutrants. The limit is set to three resutrants, and its beeing sorted by the most recommended resturants. 
# By calling the variable "response" we run the search through the database with the parameters. 
# We create a list of businesses, and in the for loop we add the businesses we found in the search to the list created
# above. In the end we return the list containing the three most recommended resturants. 

def get_businesses(location):

    auth = Oauth1Authenticator(
        consumer_key=os.environ["CONSUMER_KEY"],
        consumer_secret=os.environ["CONSUMER_SECRET"],
        token=os.environ["TOKEN"],
        token_secret=os.environ["TOKEN_SECRET"]
        )

    client = Client(auth)

    params = {
        'lang': 'en',
        'limit' : 3,
        'sort' : 2
        }

    response = client.search(location, **params)

    businesses_list = []

    for business in response.businesses:
        business_names = businesses_list.append(business.name)


    return businesses_list

