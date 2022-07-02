"""
get tweet content with API call:

curl -o tweets.txt -H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAACQidQEAAAAAJCdB%2FDdIhfce8G9wUsHPgKLNYKA%3DC9pRAClQhw0i3eeOl690RgUNcHOj3T4dGOJQrL8TB2yzJNDJOC" "https://api.twitter.com/2/users/888790426995621888/tweets?max_results=100"

"""
import json

with open('tweets.json') as json_file:
    data = json.load(json_file)


# sample a tweet
print(data['data'][0]['text'])


#write the text to a new file
with open('rawtext.txt', 'a') as f:
    for i in range(len(data['data'])):
        f.write(str(data['data'][i]['text']).replace('\n'," ").strip())
        # f.write(str(data['data'][i]['text']))
        f.write('.\n')