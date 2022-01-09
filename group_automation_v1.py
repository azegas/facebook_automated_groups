# source env/bin/activate
# pip install pyautogui
# NOTE: You must install tkinter on Linux to use MouseInfo. Run the following: sudo apt-get install python3-tk python3-dev
# sudo apt install both of those
# sudo apt install xdotool - for mouse location
# into terminal for mouse coordinates = watch -t -n 0.0001 xdotool getmouselocation
# sudo apt-get install xsel - for pyperclip to work.
# sudo apt isntall scrot - for screenshots to work


# sadly you are unable to use your pc while the script is runnig, since it needs your keyboard and mouse.

# butu nice:
# paimti is excelio failo grupes
# jei cant open page - (popup confirmation window) - open new tab and continue

import pyautogui
import time
import pyperclip

# Global variables 
# better to read from excel than type on by one... maybe one day
groups = ['1467560530167742', 'Jurbarko.ir.rajono.Turgelis', '549191192845130', '152671655435790', 'tiandelietuva1', '892970181113610', 'sveikuoliuturgelis', '355205269060292', '3000680066687339', '749997648386908', 'bucobu.perkuparduodukeiciudovanoju', '618509231575741', '830370327028272', '476145985851899', '958130160929894', '447610092267140', 'alytaus']

# pridek sita - '1411568779062260'
# mokymu id - '1531444367245555'

# time to prepare and open a browser and leave mouse untouched
time.sleep(10)

# Set up a 2.5 second pause after each PyAutoGUI call:
pyautogui.PAUSE = 2.5

# opens new tab in chrome
pyautogui.keyDown('ctrl')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('ctrl')

# Lithuanian content attempt

content = 'Glotnučiai kupini naudos Jūsų sveikatai! 💪'

# start for loop, post to all the groups above
for i in range(len(groups)):
    link = 'https://facebook.com/groups/'+groups[i]
    pyautogui.typewrite(link)
    pyautogui.typewrite('\n')
    print("atsidariau", link) # print out url opening confirmation

    # Open "Create Post window"
    pyautogui.hotkey('ctrl','f')
    pyautogui.typewrite('Write something')
    pyautogui.press('enter')
    pyautogui.press('escape')
    pyautogui.press('enter')
    
    pyautogui.typewrite("https://www.facebook.com/107538098417353/photos/a.107837208387442/127916193046210/")
    time.sleep(10)
    # link not necessary anymore, delete
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('backspace')
    time.sleep(2)
    
    # Writing Post
    # pyautogui.typewrite("Susipilk -> Paplak -> Megaukis!")
    # time.sleep(3)
    
    pyperclip.copy(content)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
        
    # newline
    pyautogui.press('enter')
    time.sleep(1)
    
    # more text
    pyautogui.typewrite("Apsilankyk www.smutifruti.lt ir paragauk!")
    time.sleep(3)
    
    # turn off url link
    pyautogui.click(1666, 515)  # choose pixel location according to your screen(xdotool on linux)
    time.sleep(3)
    
    # click Post
    pyautogui.click(1453, 947)  # choose pixel location according to your screen(xdotool on linux)
    print("Done", link)        # print out posting confirmation
    time.sleep(5)
    
    # mark search field, prepare for new link input
    pyautogui.write(['f6'])
    time.sleep(1)
