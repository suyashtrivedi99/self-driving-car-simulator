import keyboard as kbd
import pyautogui as pg

while(True):
    if kbd.is_pressed('esc'):
        print('ESC')
        pg.keyUp('up')
        break
    else:
        pg.keyDown('up')