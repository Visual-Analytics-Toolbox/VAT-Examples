from vaapi.client import Vaapi
import os


def get_logs():
    response = client.logs.list()
    for log in response:
        print(f"{log.game} - Player: {log.player_number}")

    # you can print all fields of a log with:
    # response[0].dict()

def filter_logs():
    response = client.logs.list(event=10,head_number=35,game=441)
    for log in response:
        print(f"{log.game} - Player: {log.player_number}")

def get_log(id):
    response = client.logs.get(id=id)
    print(response)

def create_log():
    response = client.logs.create(game=441,robot=6,player_number=5)
    return response

def update_log(id):
    response = client.logs.update(id=id,comment="everything was fine :)")
    print(response)

def delete_log(id):
    client.logs.delete(id=id)

if __name__ == "__main__":
    client = Vaapi(
        base_url=os.environ.get("VAT_API_URL"),
        api_key=os.environ.get("VAT_API_TOKEN"),
    )
    get_logs()
    filter_logs()
    log = create_log()
    get_log(log.id)
    update_log(log.id)
    delete_log(log.id)


