from cProfile import run
import pyautogui, sys
import time
# import mouse
# import keyboard
# import win32api
import threading
from pynput import mouse, keyboard
# import asyncio

# while True:
#     mouse_events = []
#     mouse.hook(mouse_events.append)
#     keyboard.start_recording()
#     keyboard.wait('esc')

#     mouse.unhook(mouse_events.append)
#     keyboard_events = keyboard.stop_recording()

#     print(mouse_events)
#     print(keyboard_events)

# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

# username: X:265, 365
# password: X:265, 430
# login: X:400, 790

# time.sleep(3)

# pyautogui.click(x = 265, y = 365)
# pyautogui.typewrite('DUCKH3RO', interval = 0.20)

# pyautogui.click(x = 265, y = 430)
# pyautogui.typewrite('Catclaw0415', interval = 0.20)

# pyautogui.click(x = 400, y = 790)
# time.sleep(0.2)
# scr1 = pyautogui.screenshot()
# scr1.save('screenshot1.png')
# i=0

# c

#     # start_time = time.time()
#     # print(start_time)
#     time.sleep(0.2)
#     timestamp = time.time() 
#     print( timestamp )
#     i+=1
#     mouse_position = pyautogui.position()
#     print(mouse_position)

    # check if the mouse clicked or not

    

#take screenshot

i = 0


while True:
    time.sleep(1)
    timestamp = time.time() 
    filename = str(timestamp) + ".png"
    src1 = pyautogui.screenshot(region=(768, 336, 1024, 768))
    src1.save(filename)
    i += 1

# get mouse state
# while True:
#     # time.sleep(0.1)
#     # print("1234")
#     if keyboard.read_key('c'):
#         print("1 is pressed")




# start_key = win32api.GetKeyState()

# get keyboard state




# 事件驱动
# 是否自动施法? 非自动施法就会有左键点击的操作
# 不使用A键和S键盘，只用规定的键

# Get screenshot while mouse clicked
# Record Timestamp, mouse_locaton, mouse_isclicked_left, mouse_isclicked_right
# Save screenshot with name as timestamp.png 

# Get screenshot while keyboard pressed
# Record Timestamp, Q, W, E, R
# Save screenshot with name as timestamp.png


# VALID_KEYBOARD_INPUTS = ['q', 'w', 'e', 'r']
# VALID_MOUSE_INPUTS = ['LD', 'LU', 'RD', 'RU']

# keyboard_input_sequence = []
# mouse_input_sequence = []

# def on_press(key):
#     if key == keyboard.Key.esc:
#         return False
#     try:
#         k = key.char
#     except:
#         k = key.name
#     if k in VALID_KEYBOARD_INPUTS:
#         keyboard_input_sequence.append(k)
#         print(k + ' key is pressed at ' + str(time.time()) + '.')

# def on_click(x, y, button, pressed):
#     if button == mouse.Button.left:
#         if pressed:
#             m = 'LD'
#         else:
#             m = 'LU'
#         mouse_input_sequence.append(m)

#         print('{0} at {1}'.format(
#             'Left Pressed' if pressed else 'Left Released',
#             (x, y)))
#     if button == mouse.Button.right:
#         if pressed:
#             m = 'RD'
#         else:
#             m = 'RU'
#         mouse_input_sequence.append(m)

#         print('{0} at {1}'.format(
#             'Right Pressed' if pressed else 'Right Released',
#             (x, y)))

# with (
#     keyboard.Listener(on_press=on_press) as keyboard_listener, 
#     mouse.Listener(on_click=on_click) as mouse_listener
#     ):
#     keyboard_listener.join()
#     mouse_listener.join()

