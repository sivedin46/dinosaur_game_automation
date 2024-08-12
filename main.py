import pyautogui
import webbrowser
from PIL import ImageChops
import keyboard
import time

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
url = "https://elgoog.im/dinosaur-game/"

webbrowser.get(chrome_path).open(url)
time.sleep(3)
pyautogui.press("space")
go_on = True
while go_on:
    background_down = pyautogui.screenshot(region=(160, 100, 300, 1)).convert("1")
    background_up = pyautogui.screenshot(region=(160, 100, 280, 1)).convert("1")
    down = pyautogui.screenshot(region=(200, 592, 300, 1)).convert("1")
    up = pyautogui.screenshot(region=(200, 496, 280, 1)).convert("1")
    if ImageChops.difference(background_down, down).getbbox():
        pyautogui.press("space")
    elif ImageChops.difference(background_up, up).getbbox():
        pyautogui.keyDown("down")
        time.sleep(0.25 )
        pyautogui.keyUp("down")
    if keyboard.is_pressed('q'):
        go_on = False   # quit game



