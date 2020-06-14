from mpris2 import get_players_uri, Player
import time
from pypresence import Presence
import time

client_id = '717362726028050533'

image = '81596775_p0'

largetext = ".　　　　　　　*　˚ 　 ˚.　 　✦　.　　　　*　　˚ 　　　.　　　　˚.　 　　.　　　　　　　*　　　　　.　✦　˚ .　　　　˚.　 　　.　　　　　　　*　˚ 　 ˚.　 　✦　.　　　　*　　˚"
RPC = Presence(client_id)
RPC.connect()


albumcovers = {"A Brief Inquiry Into Online Relationships":"abriefinquiry1","Good Faith":"good_faith","After Hours":"after_hours","Get Your Wish":"get_your_wish","Worlds":"worlds","":image}
originicons = {"MellowPlayer":"mellowplayer","":"play-button"}


while 1:
    try:
        print("----------------------------------------")
        print(round(time.time()*100)/100,"Initialising DBUS Interface...")
        uri = next(get_players_uri())
        player = Player(dbus_interface_info={'dbus_uri': uri})
        oldtrackid = "Null"
        endtime=0
        while 1:
             print("----------------------------------------")
             print(round(time.time()*100)/100,"Getting from DBUS...")
             metadata = player.Metadata
             position = player.Position
             status = player.PlaybackStatus
             print(round(time.time()*100)/100,"Done...")
             print(round(time.time()*100)/100,"Processing...")
             try:
                 if metadata['mpris:trackid'] != oldtrackid:
                     oldtrackid = metadata['mpris:trackid']
             except:
                 pass
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
             try:
                 if status == "Paused":
                     currentoriginicon = "pause-button"
             except:
                 pass
             try:
                 if str(metadata['xesam:artist'][0]) == "":
                     artist = "  "
                 else:
                     artist = metadata['xesam:artist'][0]
             except:
                 artist = "  "
             try:
                 album = " • "+metadata['xesam:album']
             except:
                 album = "  "
             try:
                 title = metadata['xesam:title']
             except:
                 title = "  "
             try:
                 origin = metadata['origin']
             except:
                 origin = "  "
             dynamicendtime = time.time()+metadata['mpris:length']/1000000-position/1000000
             print(round(time.time()*100)/100,"Done...")
             print(round(time.time()*100)/100,"Updating RPC...")
             RPC.update(state=artist, details=title+album,start=time.time(),large_image=albumcovers[currentalbumcover],end=dynamicendtime,large_text=largetext,small_image=originicons[currentoriginicon],small_text=origin)
             print(round(time.time()*100)/100,"Done...")
             print(round(time.time()*100)/100,"Waiting 1s...")
             time.sleep(1)
             print(round(time.time()*100)/100,"Done...")
    except Exception as e:
        print(round(time.time()*100)/100,e)
        print(round(time.time()*100)/100,"Waiting 5s...")
        time.sleep(5)
        print(round(time.time()*100)/100,"Done...")
