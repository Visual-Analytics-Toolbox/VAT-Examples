from vaapi.client import Vaapi
import os


def get_events():
    response = client.events.list()
    for event in response:
        print(event)


if __name__ == "__main__":
    client = Vaapi(
        base_url=os.environ.get("VAT_API_URL"),
        api_key=os.environ.get("VAT_API_TOKEN"),
    )

    get_events()
