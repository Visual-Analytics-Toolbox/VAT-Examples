from vaapi.client import Vaapi
from vaapi.types.image import Image
import os

def get_and_update_img():
    imgs = client.image.list(log=282)
    imgs_to_update = []
    for img in imgs:
        #construct image with id and the fields that you want to update
        imgs_to_update.append(Image(id=img.id,frame=img.frame.id))
        if len(imgs_to_update) == 10:
            break
    print(imgs_to_update)

    client.image.bulk_update(data=imgs_to_update)

if __name__ == "__main__":
    client = Vaapi(
        base_url=os.environ.get("VAT_API_URL"),
        api_key=os.environ.get("VAT_API_TOKEN"),
    )
    get_and_update_img()