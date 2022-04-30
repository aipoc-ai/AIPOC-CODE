import requests
#get weather api
def get_weather(query):
    url = "https://flaskapp955.herokuapp.com/"+str(query)

    response = requests.get(url)

    data = response.json()

    return data['temperature'],list(data["time"].split("\n"))
