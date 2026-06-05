from vaapi.client import Vaapi
import os
from datetime import datetime

def get_games():
    response = client.games.list()
    for game in response:
        print(game)

def get_game(id):
    response = client.games.get(id=id)
    print(response)

# game_folder="None" filters for games where this field is null
def filter_games(event=None,is_testgame=None):
    response = client.games.list(event=event,is_testgame=is_testgame,game_folder="None",half="half1")
    for game in response:
        print(game)

def create_game():
    response = client.games.create(event=10,team1=4,team2=5,half="half1",start_time=datetime.today().strftime('%Y-%m-%d_%h-%m-%s'))
    return response

def update_game(id):
    response = client.games.update(id=id,comment="everything was fine :)")
    print(response)

def delete_game(id):
    client.game.delete(id=id)


if __name__ == "__main__":
    client = Vaapi(
        base_url=os.environ.get("VAT_API_URL"),
        api_key=os.environ.get("VAT_API_TOKEN"),
    )

    get_games()
    filter_games(10,False)
    game = create_game()
    get_game(game.id)
    update_game(game.id)
    delete_game(game.id)
