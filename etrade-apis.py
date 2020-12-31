#
# e*Trade api
#
# install rauth:
#   pip install rauth
# 
from rauth import OAuth1Service
import webbrowser
from bs4 import BeautifulSoup

#
# I use Google Colaboratory for my development
#  https://research.google.com/colaboratory/faq.html
# It is being run in the cloud, so this is a way to open a new tab on my local browser from the cloud
#
from IPython.display import Javascript
def open_web(url):
    display(Javascript('window.open("{url}");'.format(url=url)))



service = OAuth1Service(
          name = 'etrade',
          consumer_key = 'Your_key_here',
          consumer_secret = 'Your_secret_here',
          request_token_url = 'https://apisb.etrade.com/oauth/request_token',
          access_token_url = 'https://apisb.etrade.com/oauth/access_token',
          authorize_url = 'https://us.etrade.com/e/t/etws/authorize?key={}&token={}',
          base_url = 'https://apisb.etrade.com')

oauth_token, oauth_token_secret = service.get_request_token(params =
       {'oauth_callback': 'oob', 
        'format': 'json'})

auth_url = service.authorize_url.format('Your_key_here', oauth_token)

#
# if you run locally, you can run the browser directly, just uncomment the line.
# webbrowser.open(auth_url)
open_web(auth_url)

verifier = input('Please input the verifier: ')
session = service.get_auth_session(oauth_token, oauth_token_secret, params = {'oauth_verifier': verifier})

url = 'https://apisb.etrade.com/v1/accounts/list'
resp = session.get(url)

print(BeautifulSoup(resp.content, "xml").prettify())

url = 'https://apisb.etrade.com/v1/market/quote/AAPL'
resp = session.get(url)

print(BeautifulSoup(resp.content, "xml").prettify())