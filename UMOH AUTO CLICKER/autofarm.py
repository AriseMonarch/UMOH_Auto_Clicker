import keyboard
import pydirectinput
import time

time.sleep(5)


while keyboard.is_pressed('q') == False:
    pydirectinput.keyDown('8')
    pydirectinput.keyDown('f')
    pydirectinput.keyDown('1')
    pydirectinput.keyDown('z')
    pydirectinput.keyDown('x')
    pydirectinput.keyDown('v')
    pydirectinput.click
    
    time.sleep(0.01)

    pydirectinput.keyUp('8')
    pydirectinput.keyUp('f')    
    pydirectinput.keyUp('1')
    pydirectinput.keyUp('z')
    pydirectinput.keyUp('x')
    pydirectinput.keyUp('v')
    time.sleep(0.01)

    #autoclicker