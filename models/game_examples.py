from vaapi.client import Vaapi
import os


def get_games():
    response = client.games.list()
    for game in response:
        print(game)

if __name__ == "__main__":
    client = Vaapi(
        base_url=os.environ.get("VAT_API_URL"),
        api_key=os.environ.get("VAT_API_TOKEN"),
    )

    get_games()