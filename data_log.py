import pyautogui, sys
import time
import mouse
import keyboard

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

    

# take screenshot'

i = 0
print(type(pyautogui.screenshot()))

while True:
    time.sleep(1)
    filename = str(i) + '.png'
    src1 = pyautogui.screenshot()
    src1.save(filename)
    i += 1

# get mouse state


# get keyboard state
