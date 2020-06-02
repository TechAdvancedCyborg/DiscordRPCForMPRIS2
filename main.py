from mpris2 import get_players_uri, Player
import time
from pypresence import Presence
import time

client_id = '717362726028050533'
image = '81596775_p0'
RPC = Presence(client_id)
RPC.connect()

uri = next(get_players_uri())
player = Player(dbus_interface_info={'dbus_uri': uri})
oldtrackid = "Null"
endtime=0
while 1:
     metadata = player.Metadata
     print(metadata)
     if metadata['mpris:trackid'] != oldtrackid:
         endtime = time.time()+metadata['mpris:length']/1000000
         oldtrackid = metadata['mpris:trackid']
     try:
     	 RPC.update(state=metadata['xesam:artist'][0], details=metadata['xesam:title'],start=time.time(),large_image=image,end=endtime)
     except:
         RPC.update(details=metadata['xesam:title'],start=time.time(),large_image=image,end=endtime)
     time.sleep(1)
