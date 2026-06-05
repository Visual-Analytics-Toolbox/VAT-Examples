from vaapi.client import Vaapi
import os
from datetime import datetime,timedelta

def get_events():
    response = client.events.list()
    for event in response:
        print(event)

def get_event(id):
    response = client.events.get(id=id)
    print(response)

def create_event():
    response = client.events.create(name="GO_27",is_testevent=False,start_day=datetime.today().strftime('%Y-%m-%d'),end_day=(datetime.today() + timedelta(days=4)).strftime('%Y-%m-%d'))
    return response

def update_event(id):
    response = client.events.update(id=id,comment="everything was fine :)")
    print(response)

def delete_event(id):
    client.events.delete(id=id)

if __name__ == "__main__":
    client = Vaapi(
        base_url=os.environ.get("VAT_API_URL"),
        api_key=os.environ.get("VAT_API_TOKEN"),
    )

    get_events()
    event = create_event()
    get_event(event.id)
    update_event(event.id)
    delete_event(event.id)
    
