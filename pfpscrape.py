  
import discord
from discord.ext import commands  
from colorama import Fore as C
from discord_webhook import DiscordWebhook
import time
import os
###################################################
os.system(f'cls & title 07tacey pfp scraper')
intents = discord.Intents.all()
client = discord.Client()
client = commands.Bot(command_prefix="$", self_bot=True, help_command=None, intents=intents)
token = input("ENTER TOKEN: ")
image_types = ["png", "jpeg", "gif", "jpg"]
#####################################################
async def scrape():
  chan = input(f"\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mENTER CHANNEL ID:{C.RESET} ")
  channel = await client.fetch_channel(chan)
  messages = await channel.history(limit=500).flatten()
  try:
      os.remove("images.txt")
  except:
      pass
  for x in messages:
    if x.attachments:
      attachment = x.attachments[0] 
      f = open("images.txt", "a")
      f.write(attachment.url + '\n')
      f.close()
      print(C.MAGENTA + "["+ C.RESET + "~" + C.MAGENTA + "]" + C.RESET + attachment.url)
    else:
      print(f"{C.MAGENTA}[{C.RESET}~{C.MAGENTA}]MESSAGE NOT A IMAGE | SKIPPING {C.RESET}")
      pass   
###################################################
async def paste():
  send = input(f"\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mENTER CHANNEL ID: {C.RESET}")
  channel = await client.fetch_channel(send)
  f = open("images.txt", "r")
  for line in f:
    print(C.MAGENTA + "["+ C.RESET + "~" + C.MAGENTA + "]" + C.RESET + line + C.RESET)
    await channel.send(line)
    pass
##################################################
async def websend():
  url = input(f"\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mENTER WEBHOOK URL: {C.RESET}")
  f = open("images.txt", "r")
  for line in f:
    print(C.MAGENTA + "["+ C.RESET + "~" + C.MAGENTA + "]" + C.RESET + line + C.RED)
    webhook = DiscordWebhook(url=url, content=line, rate_limit_retry=True)
    response = webhook.execute()
###################################################
os.system('cls')

async def menu():
  with open('images.txt') as f:
      L = len(f.readlines())
  os.system('cls')
  print(f'''\x1b[38;5;199m

                     ╔╦╗╔═╗╔═╗╔═╗╦ ╦
                      ║ ╠═╣║  ║╣ ╚╦╝
                      ╩ ╩ ╩╚═╝╚═╝ ╩ 

\x1b[38;5;199m       ╔═════════════════════════════════════════╗
       ║\x1b[38;5;199m[{C.RESET}1\x1b[38;5;199m] {C.RESET}SCRAPE PFPS/GIFS\x1b[38;5;199m                     ║
\x1b[38;5;199m       ║\x1b[38;5;199m[{C.RESET}2\x1b[38;5;199m] {C.RESET}SEND TO SERVER\x1b[38;5;199m                       ║
       ║\x1b[38;5;199m[{C.RESET}3\x1b[38;5;199m] {C.RESET}SEND TO WEBHOOK (RATELIMITS ALOT)\x1b[38;5;199m    ║
       ║\x1b[38;5;199m[{C.RESET}4\x1b[38;5;199m] {C.RESET}CREDITS\x1b[38;5;199m                              ║
       ║\x1b[38;5;199m[{C.RESET}5\x1b[38;5;199m] {C.RESET}EXIT\x1b[38;5;199m                                 ║
\x1b[38;5;199m       ╚═════════════════════════════════════════╝
  {C.RESET}''')
  while True:
    choice = input(f"\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mCHOICE\x1b[38;5;199m: \x1b[0m")
    if choice == "1":
      await scrape()
      print("\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mSCRAPED ICONS")
      time.sleep(1)
      await menu()
    elif choice == "2":
      await paste()
      print("\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mFINISHED SENDING SCRAPED ICONS")
      time.sleep(3)
      await menu()
    elif choice == "3":
      await websend()
      print("\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mFINISHED SENDING SCRAPED ICONS")
      time.sleep(3)
      await menu()
    elif choice == "4":
      os.system('cls')
      print('''
      Credits:\x1b[38;5;199m
╔══════════════════════╗
║\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0m07TACEY              \x1b[38;5;199m║
\x1b[38;5;199m║\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0m07TACEY               \x1b[38;5;199m║
\x1b[38;5;199m╚══════════════════════╝
''')
      time.sleep(3)
      await menu()
    elif choice == "5":
      print("\x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mCLOSING...")
      time.sleep(2)
      os._exit(0)
    else:
      print(f"{C.RED}THATS NOT A OPTION!{C.RESET}")
      time.sleep(1)
      await menu()

#####################################################

@client.event
async def on_connect():
	await menu()

client.run(token, bot=False) 
