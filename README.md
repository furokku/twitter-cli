# wtf
terrible twitter cli client that took too long<br>
syntax is available by running client.py with no arguments or right here<br>
`./client.py -status="your tweet content here" [ -fp="/path/to/media" -reply="tweet_id" ]`<br>
[] represents optional arguments<br>

# how tf
put your access token, access token secret, consumer key, consumer key secret in a .env like so<br>
```CONSUMER_KEY = "your_consumer_key"
CONSUMER_KEY_SECRET = "your_consumer_key_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"
```<br>
i might make it better in the future but for now i don't really care

# requirements
tweepy<br>
python3<br>
dotenv<br>


i spent way too much of my life on this