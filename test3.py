# human readable

import request
from pprint import pprint

url= "https://0.0.0.0:2224/jsondata"

for x in yugiohcard:
    pprint(f"The card info is name: {x['monster name']} level: {x['level']} type: {x['type']} attribute: {x['attribute']} attack points: {x['atk']} defense points: {x['def']}")

