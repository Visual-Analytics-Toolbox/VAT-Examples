"""
Fetches links to images
"""

import os
from vaapi.client import Vaapi

client = Vaapi(
    base_url=os.environ.get("VAT_API_URL"),
    api_key=os.environ.get("VAT_API_TOKEN"),
)
my_list = client.image.list(log=282)

for image in my_list:
    print(image)