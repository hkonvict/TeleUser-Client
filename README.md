# TeleUser-Client
Telegram Client that helps you to reply for Personal Messages using your own account when you are Offline.

## Introduction

Using [Telegram API and TDLib](https://core.telegram.org/#tdlib-build-your-own-telegram) a client is made that reply for Personal Messages.

This API allows you to build your own customized Telegram clients.

Also it make use of a Python Library [Telethon](https://pypi.org/project/Telethon/).
Telethon is an [asyncio](https://docs.python.org/3/library/asyncio.html) Python 3 [MTProto](https://core.telegram.org/mtproto) library to interact with [Telegram](https://telegram.org/)’s API as a user or through a bot account (bot API alternative).


## Installation

You can install `Telethon` library using:
```
pip install Telethon
```



## Creating a client
This syntax is just to provide some basics and not to be used in the main `TeleUser.py`.

Make sure that you have your own `api_id` and `api_hash` by clicking [here](https://my.telegram.org).

```python
from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'

client = TelegramClient('session_name', api_id, api_hash)
client.start()
```
In place of `session_name` give any string keyword, like may be your name. It basically creates a authentication key with that name so you don't have to login again.

## Running 
Let's run the main `TeleUser.py` file now. 

Before Running it make sure that you have replaced the `api_id`, `api_hash` and `session_name` variables with your own by manually opening and editing it.

Now go the directory where you have downloaded the files using `cd` for windows.
And then run the `TeleUser.py` as:
```bash
python TeleUser.py
```

## Working

So when `TeleUser.py` is running in the terminal, all the private messages that you are receiving will be replied automatically and also their messages will be collected in text file in the same directory.

## Basic Commands
`STOP`
- When you are online again, you can stop the Client without closing it by terminal. Just go to the Saved Messages dialogue and send `STOP`.

`START`
- When you are going offline again, you can start the Client again without restarting it by terminal. Just go to the Saved Messages dialogue and send `START`

**Note:-**
-  You can use these `START` `STOP` commands in any Chat.

- You can use these `START` `STOP` commands in any number of times continuosly.

## Contributing
Contributions of all sizes are welcome. 

## Note
Before running the `TeleUser.py` in the terminal you must:

- Assign the `api_id` and `api_hash` editing the `TeleUser.py`.
- Assign the `session_name` editing the `TeleUser.py`. It may be your name.

You are good to go now.
All the Best.

## Contact
For any queries you can send your messages by clicking [here](http://telegram.me/hkonvict).

## License
[MIT](https://choosealicense.com/licenses/mit/)
