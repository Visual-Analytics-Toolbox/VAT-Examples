from vaapi.client import Vaapi
import os

def filter_image():
    response = client.image.list(log=282,blurredness_value__lt=45,limit=20)
    i = 0
    for img in response:
        i +=1 
        print(img.blurredness_value)
        if i == 20:
            break

if __name__ == "__main__":
    client = Vaapi(
        base_url=os.environ.get("VAT_API_URL"),
        api_key=os.environ.get("VAT_API_TOKEN"),
    )
    filter_image()