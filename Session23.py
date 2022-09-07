import json
import requests

api_key = "31c21508fad64116acd229c10ac11e84"
url = "https://newsapi.org/v2/top-headlines?country=in&apiKey={}".format(api_key)

response = requests.get(url)
print(response)
text_response = response.text
print(text_response)
print(type(text_response))

dictionary_response = json.loads(text_response)
print(dictionary_response)
print(type(dictionary_response))

articles = dictionary_response['articles']
for article in articles:
    # print(article)
    print(article['title'])
    print(article['author'])
    print(article['urlToImage'])
    print("``````````````````````````")