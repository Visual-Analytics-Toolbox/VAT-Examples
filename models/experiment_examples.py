from vaapi.client import Vaapi
import os

def get_experiments():
    response = client.experiment.list()
    for experiment in response:
        print(experiment)

def get_experiment(id):
    response = client.experiment.get(id=id)
    print(response)

def filter_experiments(event=None):
    response = client.experiment.list(event=event,experiment_folder="None")
    for experiment in response:
        print(experiment)

def create_experiment():
    response = client.experiment.create(event=10,type="Gamelog")
    return response

def update_experiment(id):
    response = client.experiment.update(id=id,comment="everything was fine :)")
    print(response)

def delete_experiment(id):
    client.experiment.delete(id=id)


if __name__ == "__main__":
    client = Vaapi(
        base_url=os.environ.get("VAT_API_URL"),
        api_key=os.environ.get("VAT_API_TOKEN"),
    )

    get_experiments()
    filter_experiments(10)
    experiment = create_experiment()
    get_experiment(experiment.id)
    update_experiment(experiment.id)
    delete_experiment(experiment.id)
