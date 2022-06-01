from cProfile import run
import pyautogui, sys
import time
import os
from playsound import playsound
# import mouse
# import keyboard
# import win32api
import threading
from pynput import mouse, keyboard
# import asyncio

# while True:qwer
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

# i = 0


# while True:
#     time.sleep(1)
#     timestamp = time.time() 
#     filename = str(timestamp) + ".png"
#     src1 = pyautogui.screenshot()
#     src1.save(filename)
#     i += 1

# get mouse state
# while True:
#     # time.sleep(0.1)
#     # print("1234")
#     if keyboard.read_key('c'):
#         print("1 is pressed")




# start_key = win32api.GetKeyState()

# get keyboard state




# 事件驱动
# 是否自动施法? 自动施法就会有左键点击的操作
# 不使用A键和S键盘，只用规定的键

# Get screenshot while mouse clicked
# Record Timestamp, mouse_locaton, mouse_isclicked_left, mouse_isclicked_right
# Save screenshot with name as timestamp.png 



# Get screenshot while keyboard pressed
# Record Timestamp, A, S, Q, W, E, R
# Save screenshot with name as timestamp.png


VALID_INPUTS = ['a', 's', 'q', 'w', 'e', 'r']


class Screenshotter:
    def __init__(self):
        self.dirname = os.path.dirname(__file__)
        self.start_time = time.time()
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press)
        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.mouse_controller = mouse.Controller()
        self.start_listener()
        # with self.keyboard_listener, self.mouse_listener:
        #     self.keyboard_listener.join()
        #     self.mouse_listener.join()

    def on_press(self, key):
        if key == keyboard.Key.f8:
            print('Monitoring is stopped')
            # return False
            self.stop_listener()
        try:
            k = key.char
            pos = self.mouse_controller.position
        except:
            k = key
            pos = self.mouse_controller.position
        if k in VALID_INPUTS:
            event = k + '_' + str(pos)
            self.take_screenshot(event)
            print(k + ' pressed at ' + str(pos) + ', time: ' + str(self.timestamp()) + '.')

    def on_click(self, x, y, button, pressed):
        if button == mouse.Button.middle:
            print('Mouse monitoring is stopped ')
            return False
        if pressed:
            event = f'mr_({x},{y})' if button == mouse.Button.right else f'ml_({x},{y})'
            self.take_screenshot(event)
            print('{0} at {1}, time:{2}'.format(
                'Right clicked' if button == mouse.Button.right else 'Left clicked',
                # 'Right clicked',
                (x, y), self.timestamp()))

    def start_listener(self):
        with self.keyboard_listener, self.mouse_listener:
            filename = 'recording_start.wav'
            path = os.path.join(self.dirname, r'Recording', filename)
            playsound(path)
            self.keyboard_listener.join()
            self.mouse_listener.join()
            

    def stop_listener(self):
        self.keyboard_listener.stop()
        self.mouse_listener.stop()
        filename = 'recording_end.wav'
        path = os.path.join(self.dirname, r'Recording', filename)
        playsound(path)
        
    def timestamp(self):
        return time.time() - self.start_time

    def take_screenshot(self, event):
        filename = str(self.timestamp()) + '_' +str(event) + ".jpg"
        path = os.path.join(self.dirname, r'Screenshots', filename)
        try:
            img = pyautogui.screenshot()
            img.save(path)
        except Exception as e:
            print(e+ '\n' + 'At path: ' + path)


def main():
    def on_f7_press(key):
        if keyboard.Key.f7 == key:
            screenshotter = Screenshotter()

        if keyboard.Key.f8 == key:
            playsound(os.getcwd() + '\\' + r'Recording\recording_end.wav')
            listener.stop()


    # Collect events until released
    with keyboard.Listener(
            on_press=on_f7_press) as listener:
        listener.join()
    # screenshotter = Screenshotter()

if __name__ == '__main__':
    main()


