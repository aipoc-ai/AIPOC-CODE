import requests
#for geting answer
def get_ans(query):
    url = "https://flaskapp955.herokuapp.com/ans/"+str(query)

    response = requests.get(url)

    data = response.json()

    return data['answer']+"."

