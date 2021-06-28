import pyautogui
import time
import webbrowser as wb
my_msg=input("enter the msg:")   #after you  need to go web.whatapp
wb.open("www.web.whatapp.com")
time.sleep(10)  #creat time to open browser in time
for i in range(10):
    pyautogui.typewrite(my_msg)
    pyautogui.press("enter")