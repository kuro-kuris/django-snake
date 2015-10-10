# -*- coding: utf-8 -*
from requests_oauthlib import OAuth1Session
import pprint
import json
import urllib.request
import os

RBS_OBP_CLIENT_KEY = os.environ.get('RBS_OBP_CLIENT_KEY')
RBS_OBP_CLIENT_SECRET = os.environ.get('RBS_OBP_CLIENT_SECRET')


# initialise parameters
# client key and secret are tied into which base url
# you are using in the examples we are using the base_url for rbs
client_key = RBS_OBP_CLIENT_KEY
client_secret = RBS_OBP_CLIENT_SECRET
base_url = "https://rbs.openbankproject.com"
request_token_url = base_url + "/oauth/initiate"
authorization_base_url = base_url + "/oauth/authorize"
access_token_url = base_url + "/oauth/token"

# oauth handshake initial part takes absolutely ages
openbank = OAuth1Session(client_key, client_secret=client_secret, callback_uri='http://127.0.0.1/cb')
openbank.fetch_request_token(request_token_url)
authorization_url = openbank.authorization_url(authorization_base_url)
print('Going here to authorize:', authorization_url)

# handshake 2nd part where we gain access to the clients' data
r = urllib.request.urlopen(authorization_url)
redirect_url = urllib.response.addinfourl.geturl(r)

#redirect_response = urllib.request.urlopen(redirect_url)
redirect_response = input('Paste the full redirect URL here:')

openbank.parse_authorization_response(redirect_response)
openbank.fetch_access_token(access_token_url)

our_bank = 'rbs-rbs-c'


r = openbank.get(u"{}/obp/v1.4.0/banks/{}/accounts/private".format(base_url, our_bank))
accounts = r.json()['accounts']
transactions = r.json()['transactions']


print(r)
print(accounts)
print(transactions)
