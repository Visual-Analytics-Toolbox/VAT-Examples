from vaapi.client import Vaapi
import os


##### setup



def create_log():
    log = client.logs.create(game=441,robot=6,player_number=5)
    return log.id

def create_cognitionframe(log_id,frame_number=1,frame_time=5):
    resp = client.cognitionframe.create(log=log_id,frame_number=frame_number,frame_time=frame_time)
    frame_number = frame_number + 1
    frame_time = frame_time + 10
    return resp.id

def delete_log(id):
    client.logs.delete(id=id)

#####

def get_logsfirstframe():
    response = client.log_first_frame.list()
    for log in response:
        print(log)

def get_logfirstframe(id):
    response = client.log_first_frame.get(id=id)
    print(response)

def create_logfirstframe(log_id):
    response = client.log_first_frame.create(log=log_id,first_standby_frame=create_cognitionframe(log_id,frame_number=2,frame_time=5),
                                             first_set_frame=create_cognitionframe(log_id,frame_number=3,frame_time=10),
                                             first_ready_frame=create_cognitionframe(log_id,frame_number=4,frame_time=20))
    return response

def update_logfirstframe(id):
    response = client.log_first_frame.update(log=id,first_ready_frame=create_cognitionframe(id,frame_number=10,frame_time=30))
    print(response)

def delete_log(id):
    client.log_first_frame.delete(id=id)

if __name__ == "__main__":
    client = Vaapi(
        base_url=os.environ.get("VAT_API_URL"),
        api_key=os.environ.get("VAT_API_TOKEN"),
    )
    get_logsfirstframe()
    log = create_log()
    create_logfirstframe(log)
    get_logfirstframe(log)
    update_logfirstframe(log)
    delete_log(log)


