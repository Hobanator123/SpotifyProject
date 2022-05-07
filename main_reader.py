#!/usr/bin/env python
# from mfrc522 import SimpleMFRC522
# import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

DEVICE_ID = "4cc9d5ed502d3c91e94d8df94a49faa901db3a36"
CLIENT_ID = "5a20366b92274044beebc4c0bb8829d2"
CLIENT_SECRET = "feac3b2b22bf4ff885e84c94eaed063a"

ADD_TO_QUEUE_ID = 'abc'
listening_to_queue = False

pause_play_count = 0
pause = pause_play_count % 2 == 0

shuffle_count = 0
is_shuffle = shuffle_count % 2 == 0


# Define all the functions

def add_to_queue(song_to_add_id):
    sp.add_to_queue(f'spotify:track:{song_to_add_id}', device_id=DEVICE_ID)

def start_album(albumid):
    sp.start_playback(device_id=DEVICE_ID, context_uri=f'spotify:album:{albumid}')


def start_track(trackid):
    sp.start_playback(device_id=DEVICE_ID, uris=[f'spotify:track:{trackid}'])


def start_playlist(playlistid):
    sp.start_playback(device_id=DEVICE_ID, context_uri=f'spotify:playlist:{playlistid}')


def pause_play_song():
    global pause_play_count
    global pause
    pause = pause_play_count % 2 == 0
    pause_play_count += 1
    if pause:
        sp.pause_playback(device_id=DEVICE_ID)
    else:
        sp.start_playback(device_id=DEVICE_ID)


def next_song():
    sp.next_track(device_id=DEVICE_ID)


def previous_song():
    sp.previous_track(device_id=DEVICE_ID)


def toggle_shuffle():
    global shuffle_count
    global is_shuffle
    is_shuffle = shuffle_count % 2 == 0
    shuffle_count += 1
    sp.shuffle(is_shuffle, device_id=DEVICE_ID)


rfid_playlist_Id = {
    'RFID-CARDVALUE-1': '37i9dQZF1EVHGWrwldPRtj',  # Chill Mix
    'RFID-CARDVALUE-1': '37i9dQZF1EQqedj0y9Uwvu',  # 2010 Mix
    'RFID-CARDVALUE-1': '37i9dQZF1EQn4jwNIohw50'   # 2000 Mix
}

rfid_album_Id = {
    'RFID-CARDVALUE-1': '2cWBwpqMsDJC1ZUwz813lo',  # Eminem Show
    'RFID-CARDVALUE-1': '6t7956yu5zYf5A829XRiHC',  # The Marshal Mathers LP
    'RFID-CARDVALUE-1': '5qENHeCSlwWpEzb25peRmQ',  # Curtain Call
    'RFID-CARDVALUE-1': '7tsXPtLqhab1zWeubbf6JH',  # Encore
    'RFID-CARDVALUE-1': '7MZzYkbHL9Tk3O6WeD4Z0Z',  # Relapse Refill
    'RFID-CARDVALUE-1': '4Uv86qWpGTxf7fU7lG5X6F',  # College Dropout
    'RFID-CARDVALUE-1': '7gsWAHLeT0w7es6FofOXk1',  # The Life of Pablo
    'album3': '0Y7qkJVZ06tS2GUCDptzyW',  # Straight Outta Compton
    'album2': '7q2B4M5EiBkqrlsNW8lB7N',  # 2001
    'album1': '6tE9Dnp2zInFij4jKssysL'   # I NEVER LIKED YOU
}

rfid_track_Id = {
    'RFID-CARDVALUE-1': '0gHcxtyWQT0HrlGxaxP1KT',  # Hit
    'RFID-CARDVALUE-1': '44GokgCa37BTZP2NU2zkoJ',  # Shutdown
    'RFID-CARDVALUE-1': '7GX5flRQZVHRAGd6B4TmDO',  # XO Tour Llif3
    'RFID-CARDVALUE-1': '5Qy6a5KzM4XlRxsNcGYhgH',  # 6 Foot 7 Foot
    'RFID-CARDVALUE-1': '3uqinR4FCjLv28bkrTdNX5',  # A  Milli
    'RFID-CARDVALUE-1': '51EC3I1nQXpec4gDk0mQyP',  # 90210
    'RFID-CARDVALUE-1': '7Bpx2vsWfQFBACRz4h3IqH',  # family ties
    'RFID-CARDVALUE-1': '05nbZ1xxVNwUTcGwLbp7CN',  # Myself
    'RFID-CARDVALUE-1': '01Lr5YepbgjXAWR9iOEyH1',  # Love Sosa
    'RFID-CARDVALUE-1': '7KXjTSCq5nL1LoYtL7XAwS',  # HUMBLE
    'RFID-CARDVALUE-1': '14PlDNjNh3pXyHXzkhX8n5',  # KEKE
    'RFID-CARDVALUE-1': '2EEeOnHehOozLq4aS0n6SL',  # iSpy
    'RFID-CARDVALUE-1': '1fCeXjoRExPP2qwSBh2aST',  # Black & White
    'RFID-CARDVALUE-1': '2BJSMvOGABRxokHKB0OI8i',  # Shoota
    'RFID-CARDVALUE-1': '0tYHqwTW4s6VuPWDSD7n7K',  # KOODA
    'RFID-CARDVALUE-1': '2bsy1j0guuVP0I3xoTRCvn',  # Skepta and JME Freestyle
    'RFID-CARDVALUE-1': '0WbHgG6Em5sbiTXw7Ani1e',  # Who Am I
    'RFID-CARDVALUE-1': '722tgOgdIbNe3BEyLnejw4',  # Black Skinhead
    'RFID-CARDVALUE-1': '0VgkVdmE4gld66l8iyGjgx',  # Mask Off
    'RFID-CARDVALUE-1': '2igwFfvr1OAGX9SK DCPBwO',  # Empire State of mMind
    'RFID-CARDVALUE-1': '5ljCWsDlSyJ41kwqym2ORw',  # 03 Bonnie and Clyde
    'RFID-CARDVALUE-1': '2gZUPNdnz5Y45eiGxpHGSc',  # Power
    'RFID-CARDVALUE-1': '5eJpwQyirY5EEdNadHKRAM',  # Mannequin
    'RFID-CARDVALUE-1': '0ESJlaM8CE1jRWaNtwSNj8',  # beibs in the trap
    'RFID-CARDVALUE-1': '5274I4mUMnYczyeXkGDWZN',  # Fine China
    'track5': '35VUTs0LoeWGp69L0jyHOZ',  # Nuthin But A  G Thang
    'track4': '6Tsu3OsuMz4KEGKbOYd6A0',  # Hypnotize
    'track3': '5mCPDVBb16L4XQwDdbRUpz',  # Passionfruit
    'track2': '2oUwMN5VfdGX10XeQJLBBi',  # Clash
    'track1': '7EiZI6JVHllARrX9PUvAdX'  # Low Life
    }

functional_rfids = {
    'pauseplay': pause_play_song,
    'next': next_song,
    'prev': previous_song,
    'shuffle': toggle_shuffle
}


while True:
    try:
        # reader = SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))
        
        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Waiting for record scan...")
            rf_id = input('ID: ')
            print("Card Value is:", rf_id)
            sp.transfer_playback(device_id=DEVICE_ID, force_play=True)
            

            if rf_id == ADD_TO_QUEUE_ID:
                queue_list = []
                listening_to_queue = True
                time.sleep(2)

            elif rf_id in rfid_track_Id.keys() and listening_to_queue:
                # add_songs_to_queue
                queue_list.append(rf_id)
                while listening_to_queue:
                    start = time.perf_counter()
                    # queue_reader = SimpleMFRC522()
                    rf_id = input('ID: ')
                    end = time.perf_counter()
                    time_delta  = end - start
                    if time_delta > 5:
                        listening_to_queue = False
                        
                    elif rf_id in rfid_track_Id.keys():
                        queue_list.append(rf_id)

                
                for song_rf_id in queue_list:
                    add_to_queue(rfid_track_Id[song_rf_id])
                    



            elif rf_id in rfid_album_Id.keys():
                # playing an album
                start_album(rfid_album_Id[rf_id])
                time.sleep(2)

            elif rf_id in rfid_track_Id.keys() and not listening_to_queue:
                # playing a track
                start_track(rfid_track_Id[rf_id])
                time.sleep(2)

            elif rf_id in rfid_playlist_Id.keys():
                # playing a playlist
                start_playlist(rfid_playlist_Id[rf_id])
                time.sleep(2)

            elif rf_id in functional_rfids.keys():
                # performing functionality
                functional_rfids[rf_id]()  # Calls function in dictionary
                time.sleep(2)

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc.)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        # GPIO.cleanup()