from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

last = 0
locked = 0
muted = 0
kb = Controller()


def current_milli_time():
    return round(time.time() * 1000)


def mute():
    global muted
    muted = 1
    print("Mute\n")
    with kb.pressed(Key.alt_r):
        kb.press('m')
        kb.release('m')


def unmute():
    global muted
    muted = 0
    print("Unmute")
    with kb.pressed(Key.alt_r):
        kb.press('m')
        kb.release('m')


def on_press(key):

    global last, locked, muted

    if key == Key.alt_l:
        if (muted == 0) & (locked == 1):
            locked = 0
        elif muted == 1:
            if current_milli_time() - last < 300:
                print("2 presses")
                locked = 1
                unmute()
            elif locked == 0:
                unmute()
    last = current_milli_time()



def on_release(key):
    global last, locked
    if key == keyboard.Key.alt_l:
        if locked != 1:
            mute()



if __name__ == '__main__':
    mute()
    last = current_milli_time()
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

