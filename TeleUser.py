from telethon import TelegramClient, events
import datetime
api_id = <YOUR API ID>  #type Integer
api_hash = '<YOUR API HASH>' # type String
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
client = TelegramClient('<YOUR SESSION NAME>', api_id, api_hash)  #type String
user_dict = {}
@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()
    me = await client.get_me()
    if sender.id ==me.id:
      if event.raw_text.upper() == "START":
        await event.reply('Great Starting the Bot Again. 👍 Relax')
        user_dict.clear()
      if event.raw_text.upper() == "STOP":
        await event.reply('Okay, Happy Chatting 🤓')
        user_dict["StopCommand"] =0
    if event.is_private and sender.id != me.id and "StopCommand" not in user_dict.keys():
      currentDT = datetime.datetime.now()
      data = event.raw_text
      name = str(sender.first_name) + " " + str(sender.last_name)
      dump = str(currentDT) + "===>>" + name +"::" + data
      print(dump)
      my_name = me.first_name
      f = open(my_name + "DataBase.txt","a")
      f.write(dump + "\n")
      f.close()
      if sender.id not in user_dict.keys():
        user_dict[sender.id] = 1
        await event.reply('Hello there, the Human Server is off now, Get back to you Soon.\nTake Care')
      else:
        user_dict[sender.id] = user_dict[sender.id] + 1
        if user_dict[sender.id] == 5 :
          await event.reply('Hope you are not Spamming!!\nI am aborting now from here.')
client.start()
client.run_until_disconnected()