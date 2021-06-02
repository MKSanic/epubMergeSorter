#Location of buttons
tosbx = 639 #top of scroll bar   import pyautogui as pyag;import time;time.sleep(10);pyag.position()
tosby = 301
bosb = 639,456
delay = 1

#imports
import pyautogui as pyag
import pyperclip
import time
import os
from pathlib import Path

#setting working directory
os.chdir(Path(__file__).parent)
#defining functions
def pause():
    input("pause")

    
def switch(bef,aft):
    save = position[str(aft)]
    position[str(aft)] = position[str(bef)]
    position[str(bef)] = save


def fChap():
    pos = str(pyag.locateOnScreen("title.png"))
    x = 20 + int(pos[pos.find("=")+1:pos.find(",")])
    y = 30 + int(pos[pos.find("p=")+2:pos.find(", w")])
    return  x,y


def db():
    pos = str(pyag.locateOnScreen("downbutton.png"))
    x = 6 + int(pos[pos.find("=")+1:pos.find(",")])
    y = 8 + int(pos[pos.find("p=")+2:pos.find(", w")])
    return  x,y


def ub():
    pos = str(pyag.locateOnScreen("upbutton.png"))
    x = 5 + int(pos[pos.find("=")+1:pos.find(",")])
    y = 8 + int(pos[pos.find("p=")+2:pos.find(", w")])
    return  x,y



#asking for number of chapters
while(True):
    no = int(input("Number of chapters: "))
    try:
        if(no > 0):
            break
        else:
            print("Negative number?? u got a problem with ur head?")
    except:
        print(str(no) + " is not an integer, u fool")


for i in range(3,0,-1):
    print(str(i))
    time.sleep(1)


#adding all chapters to dictionary
position = {}
pyag.hotkey("alt","tab")
time.sleep(1)
pyag.click(fChap())
for i in range(1,no + 1,1):
    print("adding " + str(i))
    pyag.hotkey("ctrl","c")
    time.sleep(delay)
    position[str(i)] = int(pyperclip.paste()[8:])
    pyag.press("down")
print(position)


#finding all buttons
firstChap = fChap()
upButton = ub()

#selecting top chapter
pyag.moveTo(bosb)
pyag.dragTo(tosbx,tosby,1)
pyag.click(firstChap)

#ordering
currentChap = 1
currentlySel = 1
while(currentChap <= no):   #each loop moves a chapter to its correct position, starting from chap 1
    #selecting chapter to move
    print(currentChap)
    print(position)
    posk = list(position.keys())
    posv = list(position.values())
    moveThis = int(posv.index(currentChap)) + 1
    diff = moveThis - currentChap
    if(diff == 0):
        print("hands up no moving")
    else:
        for i in range(1,diff+1,1): #selecting to chap to move
            pyag.press("down")
            currentlySel += 1
            time.sleep(0.2)
        for i in range(1,diff+1,1):#moving chapter to correct position
            pyag.click(upButton)
            switch(currentlySel - 1,currentlySel)
            currentlySel -= 1
            time.sleep(0.2)
    pyag.press("down")
    currentlySel += 1
    currentChap += 1
    time.sleep(0.2)
pause()
