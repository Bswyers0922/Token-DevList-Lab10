import requests
import json
from pprint import pprint
from requests.auth import HTTPBasicAuth
from getpass import getpass
import urllib3


urllib3.disable_warnings()
username = input("Please enter your username: ")
password = getpass("Please enter your password: ")

baseURL = "https://sandboxdnac.cisco.com"
authAPI = "/dna/system/api/v1/auth/token"
devListAPI = "/dna/intent/api/v1/network-device"

payload = {}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

getToken = baseURL + authAPI

response = requests.post(getToken, auth=HTTPBasicAuth(username, password), headers=headers, data=payload, verify=False)

token = response.json()['Token']

#print('Your token is: ' + '"' + token + '"')

getDeviceList = baseURL + devListAPI

devPayload = {}
devHeaders = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-Auth-Token': token
}

devListresponse = requests.request("GET", getDeviceList, headers=devHeaders, data=devPayload, verify=False)

devList = devListresponse.json()

pprint(devList)
