from mpris2 import get_players_uri, Player
import time
from pypresence import Presence
from termcolor import colored, cprint

client_id = '717362726028050533'

image = '81596775_p0'

largetext = ".　　　　　　　*　˚ 　 ˚.　 　✦　.　　　　*　　˚ 　　　.　　　　˚.　 　　.　　　　　　　*　　　　　.　✦　˚ .　　　　˚.　 　　.　　　　　　　*　˚ 　 ˚.　 　✦　.　　　　*　　˚"


albumcovers = {"A Brief Inquiry Into Online Relationships":"abriefinquiry1","Good Faith":"good_faith","After Hours":"after_hours","Get Your Wish":"get_your_wish","Worlds":"worlds","Illusions of the Heart":"illusions-of-the-heart","":image}
originicons = {"MellowPlayer":"mellowplayer","":"play-button","pause-button":"pause-button"}

def log(log_time,log_type,log_message):
    log_message_to_print=str(round(time.time()*100)/100)
    if log_type == "Log":
        log_message_to_print = log_message_to_print+" [Log]: "+log_message
    elif log_type == "Warning":
        log_message_to_print = colored(log_message_to_print+" [Warning]: "+log_message, 'yellow')
    elif log_type == "Error":
        log_message_to_print = colored(log_message_to_print+" [Error]: "+log_message, 'red', attrs=['reverse'])
    elif log_type == "Separator":
        log_message_to_print="----------------------------------------\n"
    elif log_type == "Validation":
        log_message_to_print = colored(log_message,"green")
    print(log_message_to_print, end = '')
RPC = Presence(client_id)
def connecttorpc():
    try:
        RPC.connect()
    except:
        log(time.time(),"Log","Waiting 45s...")
        time.sleep(45)
        log(time.time(),"Validation","✓\n")
        connecttorpc()


connecttorpc()
while 1:
    try:
        log(time.time(),"Separator","")
        log(time.time(),"Log","Initialising DBUS Interface\n")
        uri = next(get_players_uri())
        player = Player(dbus_interface_info={'dbus_uri': uri})
        oldtrackid = "Null"
        endtime=0
        log(time.time(),"Validation","✓\n")
        while 1:
             log(time.time(),"Separator","")
             log(time.time(),"Log","Getting from DBUS...")
             log(time.time(),"Validation","✓\n")
             metadata = player.Metadata
             position = player.Position
             status = player.PlaybackStatus
             log(time.time(),"Log","Processing...")
             log(time.time(),"Validation","✓\n")
             try:
                 if metadata['mpris:trackid'] != oldtrackid:
                     oldtrackid = metadata['mpris:trackid']
             except:
                 log(time.time(),"Warning","No Track ID...\n")
             try:
                 currentalbumcover = ""
                 tempvar = albumcovers[str(metadata['xesam:album'])]
                 currentalbumcover = str(metadata['xesam:album'])
             except:
                 pass
             try:
                 currentoriginicon = ""
                 tempvar = originicons[str(metadata['origin'])]
                 currentoriginicon = str(metadata['origin'])
             except:
                 pass
             if status == "Paused":
                 currentoriginicon = "pause-button"
             try:
                 if str(metadata['xesam:artist'][0]) == "":
                     artist = "  "
                     log(time.time(),"Warning","No Artist...\n")
                 else:
                     artist = metadata['xesam:artist'][0]
             except:
                 artist = "  "
                 log(time.time(),"Warning","No Artist...\n")
             try:
                 album = " • "+metadata['xesam:album']
             except:
                 album = "  "
                 log(time.time(),"Warning","No Album...\n")
             try:
                 title = metadata['xesam:title']
             except:
                 title = "  "
                 log(time.time(),"Warning","No Title...\n")
             try:
                 origin = metadata['origin']
             except:
                 origin = "  "
                 log(time.time(),"Warning","No Origin...\n")
             try:
                 dynamicendtime = time.time()+metadata['mpris:length']/1000000-position/1000000
             except:
                 log(time.time(),"Warning","No Length...\n")
                 dynamicendtime = 100
             log(time.time(),"Log","Updating RPC...")
             log(time.time(),"Validation","✓\n")
             RPC.update(state=artist, details=title+album,start=time.time(),large_image=albumcovers[currentalbumcover],end=dynamicendtime,large_text=largetext,small_image=originicons[currentoriginicon],small_text=origin)
             log(time.time(),"Log","Waiting 1s...")
             time.sleep(1)
             log(time.time(),"Validation","✓\n")
    except Exception as e:
        log(time.time(),"Error",str(e)+"\n")
        log(time.time(),"Log","Waiting 5s...")
        time.sleep(5)
        log(time.time(),"Validation","✓\n")
        if str(e) == "Client ID is Invalid":
            log(time.time(),"Log","Waiting 25s...")
            time.sleep(25)
            log(time.time(),"Validation","✓\n")
            connecttorpc()
