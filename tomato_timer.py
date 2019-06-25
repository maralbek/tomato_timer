
import time
import webbrowser
import datetime
import vlc

study_time = 1500
break_time = 300
blink_time = 310
print("Study time started")
while study_time > 0:
    time_minutes = str(datetime.timedelta(seconds=study_time))
    print(time_minutes, end='\n')
    time.sleep(1)
    study_time = study_time - 1
    blink_time = blink_time - 1
    if blink_time == 10:
        print("Eyes relax time started")
        p = vlc.MediaPlayer("C:/relax_sound.mp3")
        p.play()
    elif blink_time == 0:
        print("Eyes relax time ended")
        p.stop()
        blink_time = 310

url = 'put your URL' %This url opens when it is time to have a break  
webbrowser.open_new_tab(url)

print("Break time started")
while break_time > 0:
    time_minutes = str(datetime.timedelta(seconds=break_time))
    print(time_minutes, end='\n')
    time.sleep(1)
    break_time = break_time - 1
url = 'put another URL' %this URL opens when it is time to get to work 
webbrowser.open_new_tab(url)
