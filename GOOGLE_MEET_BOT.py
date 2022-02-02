# works in both windows and Mac
from time import sleep
import pyautogui as aseem
import schedule
import webbrowser
import subprocess
# the link of the class
link = "meet.google.com/[meet-code]"
# the timing of the class
time = "11:11"
subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")
def join():
    webbrowser.open_new_tab('https://'+ link)
    sleep(10)
    aseem.hotkey('Ctrl','d') #FIXED
    aseem.hotkey('Ctrl','e') #FIXED
    aseem.click(1413,576)
schedule.every().day.at(time).do(join)
while True:
    schedule.run_pending()
    sleep(1)

