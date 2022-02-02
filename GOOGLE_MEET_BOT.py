# works in both windows and Mac
from time import sleep
import pyautogui as chirag
import schedule
import webbrowser
import subprocess
# the link of the class
link = "meet.google.com/yrf-feui-ykz"
# the timing of the class
time = "19:27"
subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")
def join():
    webbrowser.open_new_tab('https://'+ link)
    sleep(10)
    chirag.hotkey('Ctrl','d') #FIXED
    chirag.hotkey('Ctrl','e') #FIXED
    chirag.click(1413,576)
schedule.every().day.at(time).do(join)
while True:
    schedule.run_pending()
    sleep(1)

