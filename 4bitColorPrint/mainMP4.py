import imageprint,PIL.Image,cv2,time,vlc
file =r"\video.mp4"


player = vlc.MediaPlayer(vlc.Instance())
player.set_mrl(file, ":no-video")



video = cv2.VideoCapture(file)
start = time.time()
player.play()

while(True):
    frame = int((time.time()-start)*30)
    video.set(cv2.CAP_PROP_POS_FRAMES, frame-1)
    ret,img = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)
    if ret:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(img)   
        imageprint.printImg(img)
    else:
        break
end = time.time()
print(end-start)