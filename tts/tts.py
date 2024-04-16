import vlc,time

voice = r'https://api.streamelements.com/kappa/v2/speech?voice=Ivy&text='
instance = vlc.Instance()
player = instance.media_player_new()

def get_device():
    mods = player.audio_output_device_enum()
    if mods:
        mod = mods
        while mod:
            mod = mod.contents
            # If VB-Cable is found, return it's module and device id
            if b'CABLE Input (VB-Audio Virtual Cable)' == mod.description:
                device = mod.device
                module = mod.description
                return device,module
            mod = mod.next

device,module = get_device()
player.audio_output_device_set(None, device)
def playTTS(text):
    media = instance.media_new(voice+text)
    player.set_media(media)
    player.play()
    while not player.is_playing():
        pass
    
def ifplaying():
    return player.is_playing()
    
    
if __name__ == '__main__': 
    while True:
        print('> ',end='')
        text = input()
        playTTS(text)
