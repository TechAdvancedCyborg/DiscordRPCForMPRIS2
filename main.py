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
        uri = next(get_players_uri())
        player = Player(dbus_interface_info={'dbus_uri': uri})
        oldtrackid = "Null"
        endtime=0
        while 1:
             metadata = player.Metadata
             print(metadata)
             try:
                 if metadata['mpris:trackid'] != oldtrackid:
                     endtime = time.time()+metadata['mpris:length']/1000000
                     oldtrackid = metadata['mpris:trackid']
             except:
                 endtime=1000
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
             print(origin,originicons[currentoriginicon])
             RPC.update(state=artist, details=title+album,start=time.time(),large_image=albumcovers[currentalbumcover],end=endtime,large_text=largetext,small_image=originicons[currentoriginicon],small_text=origin)
             time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(5)
