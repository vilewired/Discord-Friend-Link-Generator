import requests

token = "TOKEN_HERE"

link = 'https://discord.com/api/v9/users/@me/invites'
request_header = {
    "Authorization": token,
    "Content-Type": "application/json"
}

payload = { # setting these is useless they will be set automatically
"max_age":0, # max age will be 604800(seconds) (1 week) automatically 
"max_uses":0, # max uses will be 5 automatically so only 5 people can use it
"temporary":False
}

code = requests.post(url=link, headers=request_header, json=payload).json()['code']
print('discord.gg/' + code)