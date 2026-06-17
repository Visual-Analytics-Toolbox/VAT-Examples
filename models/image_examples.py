from vaapi.client import Vaapi
from vaapi.types.image import Image
from vaapi.types.cognition_frame import CognitionFrame
import os
import requests
import cv2
import matplotlib.pyplot as plt
import numpy as np
from cognition_frame_examples import bulk_create_cognitionframe

def get_images():
    response = client.image.list(log=171)
    i = 0
    for img in response:
        print(img)
        i+=1
        if i == 20:
            break

def filter_images():
    """brightness_value and blurredness_value support gt,lt,gte and lte"""
    response = client.image.list(log=171,blurredness_value__lt=45)
    i = 0
    for img in response:
        print(img)
        i+=1
        if i == 20:
            break

def count_images():
    response = client.image.get_image_count(log=171,camera="TOP")
    print(f"There are {response["count"]} images matching the filter criterias")

def bulk_update_img():
    imgs = client.image.list(log=282)
    imgs_to_update = []
    for img in imgs:
        #construct image with id and the fields that you want to update
        imgs_to_update.append({"id":img.id,"frame":img.frame.id})
        if len(imgs_to_update) == 10:
            break
    print(imgs_to_update)

    client.image.bulk_update(data=imgs_to_update)

def get_image(id):
    response = client.image.get(id=id)
    print(response)

def create_image():
    # image can't exist without cognitionframe
    resp = client.cognitionframe.create(log=171,frame_number=300000,frame_time=30)
    response = client.image.create(camera="TOP",type="JPEG",log=171,frame=resp.id)
    return response

def bulk_create_cognitionframe(log_id):
    cognition_frames = []
    for x in range(2,20):
        cognition_frames.append(CognitionFrame(log=log_id,frame_number=x,frame_time=x))

    client.cognitionframe.bulk_create(frame_list=cognition_frames)

def bulk_create_images(log_id):
    cognitionframes = client.cognitionframe.list(log=log_id)
    imgs = []
    for frame in cognitionframes:
        #none of these fields can be omitted when using bulk create
        imgs.append(Image(log=log_id,frame=frame.id,camera="TOP",type="JPEG",image_url="test",blurredness_value=None,brightness_value=None))
    
    client.image.bulk_create(data_list=imgs)

def update_image(id):
    response = client.image.update(id=id,blurredness_value=100)
    print(response)

def delete_image(id):
    client.image.delete(id=id)

def download_image():
    response = client.image.list(
        log=155,
        camera="TOP",
    )
    for img in response:
        url = "https://logs.berlin-united.com/" +img.image_url
        response = requests.get(url)
        response.raise_for_status() 
        image = np.asarray(bytearray(response.content), dtype="uint8")
        image_cv = cv2.imdecode(image, cv2.IMREAD_COLOR)
        cv2.imwrite("test.png", image_cv)
        return

def brightness_histogram():
   
    response = client.image.list(
        log=712,
        camera="BOTTOM",
        limit=1000
    )
    brightness_values = [val.brightness_value for val in response]
    blurredness_values = [val.blurredness_value for val in response]

    fig, (ax1, ax2) = plt.subplots(2)
    
    ax1.set_title("brightness_values")
    ax1.hist(brightness_values)
    
    ax2.set_title("blurredness_values")
    ax2.hist(blurredness_values)
    plt.show()

if __name__ == "__main__":
    client = Vaapi(
        base_url=os.environ.get("VAT_API_URL"),
        api_key=os.environ.get("VAT_API_TOKEN"),
    )
    # get_images()
    # filter_images()
    # image = create_image()
    # get_image(image.id)
    # update_image(image.id)
    # delete_image(image.id)
    # download_image()
    # count_images()
    # bulk_update_img()
    brightness_histogram()

    # log = client.logs.create(game=441,robot=6,player_number=5)
    # cognitionframes = bulk_create_cognitionframe(log.id)
    # bulk_create_images(log.id)

    #cleanup created data
    #client.logs.delete(log.id)
