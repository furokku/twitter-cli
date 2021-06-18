#!/usr/bin/python

import os
import sys
import tweepy
from dotenv import load_dotenv

load_dotenv()
keys = [
    os.getenv("CONSUMER_KEY"),
    os.getenv("CONSUMER_KEY_SECRET"),
    os.getenv("ACCESS_TOKEN"),
    os.getenv("ACCESS_TOKEN_SECRET")
]

def main():
    """main function"""

    args = [ arg for arg in sys.argv[1:] ]
    try:
        if 2 > len(sys.argv):
            raise SystemExit

        for arg in args:
            if arg.startswith("-reply"):  replyid = arg.split('=')[1]
            if arg.startswith("-status"): status  = arg.split('=')[1]
            if arg.startswith("-fp"):
                fp = arg.split('=')[1]
                if not os.path.exists(fp): raise FileNotFoundError
    except FileNotFoundError:
        raise SystemExit(f"{sys.argv[0]}: {fp}: file not found")
    except:
        raise SystemExit(f"usage: {sys.argv[0]} -status=\"whatever you want to tweet\" [-reply=\"tweet id\"] [-fp=\"/path/to/media\"]")

##  print(f"{status}, {fp}, {reply}")

    auth = tweepy.OAuthHandler(keys[0], keys[1])
    auth.set_access_token(keys[2], keys[3])
    api = tweepy.API(auth)
    keys.clear()

    kwargDict = {}
    if 'fp' in locals():
        kwargDict['filename'] = fp
    if 'replyid' in locals():
        kwargDict['in_reply_to_status'] = replyid
    if 'status' in locals():
        kwargDict['status'] = status

    print(f"{kwargDict}")


#   shittiest code ever conceived but if it works it works.
    if 'filename' in kwargDict.keys():
        api.update_with_media(
            status=kwargDict['status'],
            filename=kwargDict['filename']
            )

    elif 'in_reply_to_status' in kwargDict.keys():
        api.update_status(
            in_reply_to_status_id=kwargDict['in_reply_to_status'],
            status=kwargDict['status'],
            auto_populate_reply_metadata=True
            )

    elif 'in_reply_to_status' and 'filename' in kwargDict.keys():
        api.update_with_media(
            status=kwargDict['status'],
            filename=kwargDict['filename'],
            in_reply_to_status_id=kwargDict['in_reply_to_status'],
            auto_populate_reply_metadata=True
            )
        
    else:
        api.update_status(
            status=kwargDict['status']
            )

main()