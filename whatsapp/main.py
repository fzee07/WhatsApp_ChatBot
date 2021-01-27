import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(1)

position1 = pt.locateOnScreen("whatsapp/smiley.png", confidence=.6)
x = position1[0]
y = position1[1]

#gets message
def get_message():
    global x, y

    position = pt.locateOnScreen("whatsapp/smiley.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y, duration=.5)
    pt.moveTo(x + 100, y - 60, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(20,-250)
    sleep(0.5)
    pt.click()
    whatsapp_message = pyperclip.paste()
    # pt.click()
    print("Message received: " + whatsapp_message)

    return whatsapp_message

#post
def post_response(message):
    globals(x,y)

    position = pt.locateOnScreen("whatsapp/smiley.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 200, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)

#processe response
def proces_response(message):
    random_no = random.random(3)
    if "?" in str(message).lower():
        return "DOn;t ask me any question!"
    else:
        if random_no == 0:
            return "That's cool!"
        elif random_no == 1:
            return "Hey there"
        else:
            return "Hello, How are you?"

#check for new message
def check_new_message():
    pt.moveTo(x+50,y-70, duration=.5)

    while True:
        #continously checking for green dot and new message
        try:
            position = pt.locateOnScreen("whatsapp/green_colour.png", condfidence=.7)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(.5)
        except(Exception):
            print("No new message")

        if pt.pixelMatchesColor(int(x+50), int(y-70), (255,255,255), tolerance=10):
            print("is white")
            processed_message = proces_response(get_message())
            post_response(processed_message)
        else:
            print("No new message")
        sleep(5);

check_new_message()
