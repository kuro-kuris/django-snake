# -*- coding: utf-8 -*
from requests_oauthlib import OAuth1Session
import pprint
import json
import urllib.request
import os
import datetime

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


'''
Calculate current date, and date one week ago
'''
current_date = datetime.datetime.today()
current_date_str = (str(current_date)).partition(" ")[0]
real_current_date = datetime.datetime.strptime(current_date_str, "%Y-%m-%d")




#get the bank accounts of the user
our_bank = 'rbs-rbs-c'
print("Available accounts")
r = openbank.get(u"{}/obp/v1.4.0/banks/{}/accounts/private".format(base_url, our_bank))


acc_infos = []
accounts = r.json()['accounts']
'''
for a in accounts:
    parsed_acc_details = {}
    #print(a['id'])
    #print(a["label"])
    parsed_acc_details["id"] = a["id"]
    parsed_acc_details["label"] = a["label"]
    acc_infos.append(parsed_acc_details)
for elem in acc_infos:
    print(elem)
'''
for a in accounts:
    acc_infos.append(a["id"])
    acc_infos.append(a["label"])


our_account = accounts[0]['id']



r = openbank.get(u"{}/obp/v1.4.0/banks/{}/accounts/{}/owner/transactions".format(base_url, 
    our_bank,
    our_account), headers= {'obp_limit' : '25'})
transactions = r.json()['transactions']

transactions = r.json()
#parsed_json = json.loads(r.json())
trans_infos = []
for trans in transactions["transactions"]:
    parsed_data = {}
    parsed_data["this_acc_id"] = trans["this_account"]["id"]
    for i in range(len(trans["this_account"]["holders"])):
        parsed_data["this_acc_holder_name_" + str(i)] = trans["this_account"]["holders"][i]["name"]
    parsed_data["other_acc_id"] = trans["other_account"]["id"]
    parsed_data["other_acc_holder_name"] = trans["other_account"]["holder"]["name"]
    parsed_data["transaction_type"] = trans["details"]["type"]
    parsed_data["transaction_posted"] = datetime.datetime.strptime(((trans["details"]["posted"]).partition("T")[0]), "%Y-%m-%d")
    parsed_data["transaction_completed"] = trans["details"]["completed"]
    parsed_data["transaction_value"] = trans["details"]["value"]["amount"]
    trans_infos.append(parsed_data)

'''
Find the transactions from the past 7 days
Calculate the overall budget for Direct Debit transactions in this interval
'''
#week_spending = []
week_budget = 0
for elem in trans_infos:
    is_from_last_7_days = elem["transaction_posted"] > (real_current_date - datetime.timedelta(days = 7))
    #print(elem["transaction_posted"] > (real_current_date - datetime.timedelta(days = 7)))
    if (is_from_last_7_days):
        #week_spending.append(float(elem["transaction_value"]))
        if (elem["transaction_type"] == "Direct Debit"):
            week_budget = week_budget + float(elem["transaction_value"])
        elif (elem["other_acc_id"] in acc_infos):
            if("savings" in (acc_infos[acc_infos.index(elem["other_acc_id"]) + 1]).lower()):
                print("lofaszgeci")

#for num in week_spending:
#    print(num)
print(week_budget)

