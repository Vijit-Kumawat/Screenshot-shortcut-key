import keyboard
import pyautogui
import os
from playsound import playsound

while True:
    try:
        keyboard.wait('alt+m')    
        screenshot_count=0
        while True:      
            screenshot_count += 1
            query = screenshot_count
            a = os.path.exists('D:\\screenshot\\' + str(query) + '.png')
            if a == False:
                pyautogui.screenshot('D:\\screenshot\\' + str(query) + '.png')
                break
            else:
                print("The file already exists")
        print("taken!")
        playsound('shutter.MP3')
    except Exception as e:
        print(e)
