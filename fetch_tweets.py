import tweepy

# API and Access Tokens

access_token  = 'TWITTER ACCESS TOKEN'
access_token_secret  = 'TWITTER SECRET'
api_key = 'TWITTER KEY'
api_secret = 'TWITTER API SECRET'

bearer_token = 'TWITTER BEARER'

# OAuth 1.0a authentication
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

# API client using tweepy
api = tweepy.API(auth)


def get_user_ids(screen_names):
    # Get user id (numeric) from user names
    user_ids = []
    for screen_name in screen_names:
        try:
            user = api.get_user(screen_name=screen_name)
            user_ids.append(str(user.id))
            print(f"User {screen_name} has ID: {user.id}")
        except Exception as e:
            print(f"Error fetching user ID for {screen_name}: {str(e)}")
    return user_ids

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        # Print the tweet text
        print(f"\nNew tweet from {tweet.author_id}:\n {tweet.text}\n")

    def on_error(self, status_code):
        print(f"Encountered streaming error (status code: {status_code})")
        if status_code == 420: # In case of rate limit
            return False # Returning False disconnects the stream

# List of user names to monitor
screen_names = ['TWITTER USERNAME'] 

user_ids = get_user_ids(screen_names)

# Stream
stream = MyStream(bearer_token=bearer_token)

# Start the stream with these user IDs
stream.filter(follow=user_ids)
