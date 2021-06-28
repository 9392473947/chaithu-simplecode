# chaithu-simplecode
this repository is used to send unlimited whatapp messages using pyautogui library 
program:
import pyautogui
import time
import webbrowser as wb
wb.open("www.web.whatapp.com")
my_msg=input("enter the msg:")
time.sleep(30)      #take 30 sec to open webwhatapp
for i in range(100):
      pyautogui.typewrite(my_msg)
      pyautogui.press("enter")
      print("success")
