import requests
from datetime import datetime
USERNAME = "krishana" ## from parameter I created
TOKEN = "jfjefnslfsejfnslfsfsei98" # from parameter I created
GRAPH_ID = "graph1"
pixela_endpoints = "https://pixe.la/v1/users"

"""Sitting up the user account on pixela"""

user_paramas = {
    "token": TOKEN,   #this is API key which we created for authentication by myself
    "username":USERNAME,  #this is username which we created to access this pixela account in future
    "agreeTermsofService":"yes",
    "notMinor":"yes"
}

# response = requests.post(pixela_endpoints,json=user_paramas)
# print(response.text)
"""create a graph on pixela for than user name"""


#first we are going to update our endpoint
graph_endpoint = f"{pixela_endpoints}/{USERNAME}/graphs"  # this is our graph end point crated from above username and key

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit" : "hr",
    "type" : "float",
    "color": "ajisai"
}

headers = {                  # this is parameter to store our Token(key) we created in header
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

"""Now we are going to posting in pixel(It records the quantity of the specified date as a "Pixel")."""


#first we are going to update our endpoint
pixel_creation_endpoints = f"{pixela_endpoints}/{USERNAME}/graphs/{GRAPH_ID}"
Coding_date = datetime.now()
#to convert this date into formant we required we use strftime() method
pixel_data ={
    "date":Coding_date.strftime("%Y%m%d"),  #here we write date in YYYYMMDD format envery where
    "quantity": input("How many hours do u code today?: ")

}

response= requests.post(url= pixel_creation_endpoints, json=pixel_data, headers=headers)
print(response.text)
"""here we r going to update our data on any data which we want"""

pixel_update_endpoint = f"{pixela_endpoints}/{USERNAME}/graphs/{GRAPH_ID}/20250305"  #here we write date in YYYYMMDD format envery where

modify_data = {
    "quantity":"1.5",

}
# response = requests.put(url=pixel_update_endpoint,json=modify_data,headers=headers)
# print(response.text)

"""here we are going to delete any pixels which we want on any specific date"""
delete_pixel_endpoint = f"{pixela_endpoints}/{USERNAME}/graphs/{GRAPH_ID}/20250305"  #here we write date in YYYYMMDD format envery where

# response=requests.delete(url=delete_pixel_endpoint,headers=headers)
# print(response.text)


"""*******this is the our final graph link (https://pixe.la/v1/users/krishana/graphs/graph1.html)  you can check on chrome********"""


