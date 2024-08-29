import json, time, os
import requests
from database import get_db_general_rtb
from utils import get_restarted
from pyrogram import Client, enums
super_sudoers = [7031471363, 7031471363]


####################################################################################

# start
wr = get_restarted()
if wr is None:
    if os.path.exists('info.json'):
        fileSize = os.path.getsize("info.json")
        if fileSize == 0:
            print("Please Input Your Token:\n")
            tokenBot = input()
            print("Please Input id sudo:\n")
            idSudo = input()

            aDict = {"Token": tokenBot, "idSudo": int(idSudo)}
            jsonString = json.dumps(aDict)
            jsonFile = open("info.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
    else:
        print("Please Input Your Token:\n")
        tokenBot = input()
        print("Please Input id sudo:\n")
        idSudo = input()

        aDict = {"Token": tokenBot, "idSudo": int(idSudo)}
        jsonString = json.dumps(aDict)
        jsonFile = open("info.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()


####################################################################################

# Token bot
f = open('info.json', )
data = json.load(f)
TOKEN = data['Token']

# Your API ID and Hash from https://my.telegram.org/apps
API_ID = 24417943
API_HASH = "8f8023dbe6965da5ffe851c5f69b2bf5"

# Chat used for logs
log_chat = 7031471363
# Sudoers and super sudoers
sudoers = [data['idSudo']]
sudoers += super_sudoers
developer = []
developer += sudoers
bot_start_time = time.time()

####################################################################################
def dev():
    lang = get_db_general_rtb("developer")
    lang2 = get_db_general_rtb("secdeveloper")
    if lang is None:
        print("No Developer")
    else:
        for row in lang:
            t = row[0]
            developer.append(t)
    if lang2 is None:
        print("No Second Devoloper")
    else:
        for row in lang2:
            t = row[0]
            developer.append(t)
    print(developer)


def get_bot_information():
    bot_inf = requests.get(
        "https://api.telegram.org/bot" + TOKEN + "/getme")
    bot_info = bot_inf.json()
    result = bot_info["result"]
    bot_id = result["id"]
    bot_username = result["username"]
    bot_name = result["first_name"]
    return bot_id, bot_username, bot_name

app = Client(
    "Dream",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    parse_mode=enums.ParseMode.HTML,
    plugins=dict(root="plugins"),
    in_memory=True, 
)

#####################################################################################


# Prefixes for commands, e.g: /command and !command
prefix = ["/", "!", "."]

# List of disabled plugins
disabled_plugins = []

# API keys
TENOR_API_KEY = "2MAL8NKBOO01"

# Bot version, do not touch this
with open("version.txt") as f:
    version = f.read().strip()
