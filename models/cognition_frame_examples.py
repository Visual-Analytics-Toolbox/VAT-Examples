from vaapi.client import Vaapi
from vaapi.types.cognition_frame import CognitionFrame
import os

def get_cognition_frames():
    response = client.cognitionframe.list(log=171)
    i = 0
    for cognitionframe in response:
        print(cognitionframe)
        i+=1
        if i == 20:
            break

def count_cognitionframe():
    response = client.cognitionframe.get_frame_count(log=171)
    print(f"There are {response["count"]} cognitionframes matching the filter criterias")

def get_and_update_cognitionframe():
    cognitionframes = client.cognitionframe.list(log=282)
    cognitionframes_to_update = []
    for cognitionframe in cognitionframes:
        #construct cognition frame with id and the fields that you want to update
        cognitionframes_to_update.append({"id":cognitionframe.id,"closest_motion_frame":cognitionframe.closest_motion_frame})
        if len(cognitionframes_to_update) == 10:
            break
    print(cognitionframes_to_update)

    client.cognitionframe.bulk_update(data=cognitionframes_to_update)

def get_cognitionframes(id):
    response = client.cognitionframe.get(id=id)
    print(response)

def create_cognitionframe(log_id):
  
    resp = client.cognitionframe.create(log=log_id,frame_number=1,frame_time=5)
    return resp

def bulk_create_cognitionframe(log_id):
    cognition_frames = []
    for x in range(2,20):
        cognition_frames.append(CognitionFrame(log=log_id,frame_number=x,frame_time=x))

    client.cognitionframe.bulk_create(frame_list=cognition_frames)

def update_cognitionframe(id):
    response = client.cognitionframe.update(id=id,frame_time=7)
    print(response)

def delete_cognitionframe(id):
    client.cognitionframe.delete(id=id)

if __name__ == "__main__":
    client = Vaapi(
        base_url=os.environ.get("VAT_API_URL"),
        api_key=os.environ.get("VAT_API_TOKEN"),
    )
    get_cognition_frames()
    count_cognitionframe()
    get_and_update_cognitionframe()
    # log = client.logs.create(game=441,robot=6,player_number=5)
    # cognitionframe = create_cognitionframe(log.id)
    # update_cognitionframe(cognitionframe.id)
    # delete_cognitionframe(cognitionframe.id)

    # bulk_create_cognitionframe(log.id)
    
    #cleanup created data
    # client.logs.delete(log.id)
