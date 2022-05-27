# human readable
# requests not request
import requests
from pprint import pprint

url= "http://10.8.26.87:2224/jsondata"

# need to do the request.get first, so you can have that object to loop through
yugiohcard= requests.get(url).json()

for x in yugiohcard:
    pprint(f"The card info is name: {x['monster name']} level: {x['level']} type: {x['type']} attribute: {x['attribute']} attack points: {x['atk']} defense points: {x['def']}")

