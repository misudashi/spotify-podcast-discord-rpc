from SwSpotify import spotify
from pypresence import Presence
import time
import random
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

CLIENT_ID = '1254832151648800928'
RPC = Presence(CLIENT_ID)

DESC = "Listening to a podcast"

spotify_logo = "custom_logo"
misudashi_logo = "misudashi"

def update(title, artist):
    RPC.update(
        large_image=spotify_logo,
        large_text=DESC,
        small_image=misudashi_logo,
        small_text="Script by Misudashi",
        details=title
    )


def stopped():
    RPC.update()


RPC.connect()
while True:
    time.sleep(0.1)
    try:
        title, artist = spotify.current()
        print(title, artist)
        update(title, artist)
        time.sleep(5)
        print('start')
    except:
        print('stop')
        stopped()
        time.sleep(5)
        continue
