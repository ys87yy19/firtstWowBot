import win32gui
from time import sleep
import pyautogui
import random


class MyGame:
    def __init__(self, title):
        hwnd = win32gui.FindWindow(None, title)
        win32gui.SetForegroundWindow(hwnd)

    def speak(self, text):
        pyautogui.press('enter')
        pyautogui.write(text)
        pyautogui.press('enter')

    def hit(self, path, confi, hit_time):
        """在屏幕上查找图片，如果找到则返回左上角和右下角的坐标位置。
        默认情况下，查找精确度为1.0"""
        p1 = pyautogui.locateCenterOnScreen(path, confidence=confi)
        sleep(1)
        # 鼠标移动到坐标
        pyautogui.click(p1.x, p1.y)
        print("找到假人了,等待攻击")
        sleep(1)
        #pyautogui.mouseDown(buttom='right')
        #pyautogui.mouseUp(buttom='right')
        pyautogui.press('1')
        sleep(hit_time)

    def mouse_move(self, x, y):
        pyautogui.moveTo(x, y)
        pyautogui.rightClick()
        pyautogui.rightClick()


while True:
    try:
        my = MyGame('魔兽世界')
        my.hit('C:\\Users\\ZeroAgain\\Desktop\\learm-code\\wow\\yuren1.png', 0.9, 1)
    except AttributeError as e:
        if str(e) == "'NoneType' object has no attribute 'x'":
            ran_x = random.randint(200, 1000)
            ran_y = random.randint(200, 700)
            my.mouse_move(ran_x, ran_y)
            print(ran_x, ran_y)
            sleep(2)
