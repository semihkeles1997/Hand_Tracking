import cv2
from cvzone.HandTrackingModule import HandDetector
import imutils
from time import sleep
import time
import numpy as np
from pynput.keyboard import Key, Controller
import subprocess

cap = cv2.VideoCapture(1)
cap.set(3, 1920)
cap.set(4, 1080)

detector = HandDetector(detectionCon=0.8)

keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "-"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", "+", ";"],
        ["_", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "  "]]

lowerKeys = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "-"],
             ["a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "+"],
             ["^", "z", "x", "c", "v", "b", "n", "m", ",", ".", "  "]]

finalText = ""

keyboard = Controller()
"""
def drawAllWithoutAlphaValue(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4,
                    (255, 255, 255), 4)
    return img
"""

topButtons = []


def drawTopList(img, topButtons):
    cv2.putText(img, "Applications", (450, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_4, 0)
    cv2.rectangle(img, (100, 50), (820, 100), (0, 0, 0), cv2.FILE_NODE_REAL)

    cv2.rectangle(img, (100, 50), (250, 100), (12, 45, 78), cv2.FILLED)
    cv2.putText(img, "Google", (120, 85), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    topButtons.append(Button([100, 50], "Google", [250, 100], (12, 45, 78), (255, 255, 255)))

    #cv2.rectangle(img, (100, 200), (300, 270), (0, 0, 0), 4)
    #cv2.putText(img, "Keyboard", (120, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    #topButtons.append(Button([120, 250], "Keyboard", [250, 300], (12, 45, 78), (255, 255, 255)))

    cv2.rectangle(img, (250, 50), (450, 100), (12, 45, 78), cv2.FILLED)
    cv2.putText(img, "Facebook", (280, 85), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    topButtons.append(Button([250, 50], "Facebook", [450, 100], (12, 45, 78), (255, 255, 255)))

    cv2.rectangle(img, (450, 50), (660, 100), (12, 45, 78), cv2.FILLED)
    cv2.putText(img, "Instagram", (480, 85), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    topButtons.append(Button([450, 50], "Instagram", [660, 100], (12, 45, 78), (255, 255, 255)))

    cv2.rectangle(img, (660, 50), (820, 100), (12, 45, 78), cv2.FILLED)
    cv2.putText(img, "Twitter", (700, 85), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    topButtons.append(Button([660, 50], "Twitter", [820, 100], (12, 45, 78), (255, 255, 255)))

    cv2.ellipse(img, (1125, 75), (25, 25), 0, 0, 360, (0, 0, 255), cv2.FILLED)
    cv2.putText(img, "X", (1110, 90), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 4)
    topButtons.append(Button([110, 90], cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 4))


def drawAll(img, buttonList):
    imgNew = np.zeros_like(img, np.uint8)
    for button in buttonList:
        x, y = button.pos
        # cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1]+500, button.size[0], button.size[1]), 20, rt=0)
        cv2.rectangle(imgNew, [button.pos[0], button.pos[1]], (x + button.size[0], y + button.size[1]), button.bgcolor,
                      cv2.FILLED)
        cv2.putText(imgNew, button.text, (x + 20, y + 65), button.font, 2, button.textColor, 3)
    out = img.copy()
    alpha = 0.2
    mask = imgNew.astype(bool)
    # print(mask.shape)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
    return out


class Button():
    def __init__(self, pos, text, size=[85, 85], bgcolor=(12, 12, 255), textColor=(255, 255, 255),
                 font=cv2.FONT_HERSHEY_SIMPLEX):
        self.pos = pos
        self.size = size
        self.text = text
        self.bgcolor = bgcolor
        self.textColor = textColor
        self.font = font


buttonList = []


def keyList(btnKeys):
    for i in range(len(btnKeys)):
        for j, key in enumerate(btnKeys[i]):
            buttonList.append(Button([100 * j + 50, 100 * i + 500], key))


def textArea():
    cv2.rectangle(img, (50, 375), (1000, 450), (0, 0, 0))
    cv2.putText(img, finalText, (60, 425), cv2.FONT_HERSHEY_PLAIN, 4,
                (255, 255, 255), 5)


def Write(string):
    for i in range(len(string)):
        keyboard.press(string[i])
    keyboard.press(Key.enter)


def functionButtons():
    func = ['+', '-', '^', '_', '  ', '||', 'X', "Zengin", "Google", "Keyboard", "Facebook"]
    return func


keyList(lowerKeys)
# buttonList.append(Button([50,50], "Zengin",[400,120],(255,255,255),(0,0,0)))

"""
topButtons = ["Google", "Facebook","Twitter","Instagram"]
tbS = 1
for tb in topButtons:
    tbS = tbS+1
    topButtons.append(Button([100 * tbS + 50, 100 * tbS + 20],tb))

"""

# topButtons.append(Button([50,50], "Google", [250,100], (0,0,0),(255,255,255),cv2.FONT_HERSHEY_COMPLEX_SMALL))

cTime = 0
pTime = 0  # bitiş zamanı


def ex(cButton, f, big=True):
    if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
        if big == True:
            cv2.rectangle(img, cButton.pos, (x + w, y + h), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, cButton.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

        else:
            cv2.rectangle(img, cButton.pos, cButton.size, (220, 220, 220), cv2.FILLED)
            cv2.putText(img, cButton.text, (cButton.pos[0] + 25, cButton.pos[1] + 35), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 0), 4)
            print(cButton.text)

            # print("Girdi..."+cButton.text+" "+str(cButton.size))

        l, _, _ = detector.findDistance(8, 4, img, draw=False)
        # print(l)
        if l < 25:
            if big == True:
                cv2.rectangle(img, cButton.pos, (x + w, y + h), (144, 258, 144), cv2.FILLED)
                cv2.putText(img, cButton.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4,
                            (255, 255, 255), 4)
            else:
                cv2.rectangle(img, cButton.pos, cButton.size, (0, 255, 0), cv2.FILLED)
                cv2.putText(img, cButton.text, (cButton.pos[0] + 20, 85), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 4)

            allFunc = functionButtons()
            control = False
            for c in allFunc:
                if c == button.text:
                    control = True
                    break

            if control == False:
                keyboard.press(cButton.text)
                f += button.text
                sleep(.30)

            else:
                if cButton.text == "  ":
                    keyboard.press(Key.space)

                if cButton.text == "^":
                    buttonList.clear()
                    keyList(keys)
                    # print("Girdi")

                if cButton.text == "_":
                    buttonList.clear()
                    keyList(lowerKeys)

                if cButton.text == "+":
                    keyboard.press(Key.enter)

                if cButton.text == "||":
                    keyboard.press(Key.space)

                if cButton.text == "-" and len(finalText) != 0:
                    keyboard.press(Key.backspace)
                    f = f.rstrip(f[-1])

                if cButton.text != "_" and cButton.text != "^":
                    f += button.text

                if cButton.text == "Zengin":
                    Write("Lütfen bana zengin ve Avrupalı (mümkünse İngilere'de yaşayan) bir kadın ayarlar mısın artııııık")

                if cButton.text == "Google":
                    Write("Google__")
                    f += cButton.text
                    subprocess.call(['C:/Users/semih/AppData/Local/Programs/Opera/launcher.exe'])

                sleep(0.30)

                control = True

    return f


while True:
    success, img = cap.read()
    img = imutils.resize(img, width=1200, height=720)
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    img = drawAll(img, buttonList)
    drawTopList(img, topButtons)

    # FPS Hesaplama
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

    #textArea()

    if lmList:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size
            finalText = ex(button, finalText, True)

        for topBtn in topButtons:
            x, y = topBtn.pos
            w, h = topBtn.size
            finalText = ex(topBtn, finalText, False)
            break

            """
                 # when clicked
                if l<25:

                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4,
                                (255, 255, 255), 4)

                    allFunc = functionButtons()
                    control = False
                    for c in allFunc:
                        if c == button.text:
                            control = True
                            break

                    if control == False:
                        keyboard.press(button.text)
                        finalText += button.text

                    else:

                        if button.text == "  ":
                            keyboard.press(Key.space)

                        if button.text == "^":
                                buttonList.clear()
                                keyList(keys)
                                # print("Girdi")

                        if button.text == "_":
                            buttonList.clear()
                            keyList(lowerKeys)

                        if button.text == "+":
                            keyboard.press(Key.enter)

                        if button.text == "||":
                            keyboard.press(Key.space)

                        if button.text == "-" and len(finalText) != 0:
                            keyboard.press(Key.backspace)
                            finalText = finalText.rstrip(finalText[-1])

                        if button.text != "_" and button.text != "^":
                            finalText += button.text

                        if button.text == "Zengin":
                            Write("Lütfen bana zengin ve Avrupalı (mümkünse İngilere'de yaşayan) bir kadın ayarlar mısın artııııık")

                    control = True





                  
                    if button.text != "  " and button.text != "^" and button.text != "_" and button.text != "+" and button.text != "||" and button.text != "-" and button.text != "_" and button.text != "Zengin":
                        keyboard.press(button.text)
                  

















                    sleep(.15)
                """

    """
    cv2.rectangle(img, (50,350), (700,450), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finalText, (60, 425), cv2.FONT_HERSHEY_PLAIN, 4,
                (255, 255, 255), 5)
    """

    """
     recXPos, recYPos, recW, recH = 50, 20, 150, 50
    rec = cv2.rectangle(img, (recXPos, recYPos), (recW, recH), (0, 0, 0), cv2.FILLED)
    anaSayfa = cv2.putText(rec, "Ana Sayfa", (recXPos + 10, recYPos + 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255))

    """

    # print(img[0].__len__(), img[1].__len__())
    cv2.imshow("Image", img)
    cv2.waitKey(1)
