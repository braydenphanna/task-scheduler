from pynput import keyboard
from ui.util import Util
import pywinctl

class DateSelector:
    date = []
    i = 0
    windowTitle = ""

    def start():
        DateSelector.windowTitle = pywinctl.getActiveWindowTitle()
        DateSelector.date = list("00/00/00 00:00 PM ")
        i = 0
        DateSelector.__print_date()
        with keyboard.Listener(on_press=DateSelector.__on_press) as listener:
            listener.join()

    def __print_date():
        print("".join(DateSelector.date[DateSelector.i:]), end=f"\r{"".join(DateSelector.date[:DateSelector.i])}")
    
    def __on_press(key):
        if DateSelector.windowTitle == pywinctl.getActiveWindowTitle():
            try:
                if (DateSelector.i < 15 and DateSelector.date[DateSelector.i] not in [" ", "/", ":"] and key.char.isdigit()):
                    DateSelector.date[DateSelector.i] = key.char
                    DateSelector.i += 1
                    if (DateSelector.date[DateSelector.i] in [" ", "/", ":"]):
                        DateSelector.i += 1
                        print(DateSelector.date[DateSelector.i], end="", flush=True)
                elif (DateSelector.i == 15 and key.char in ["a", "A", "p", "P"]):
                    DateSelector.date[DateSelector.i] = key.char.upper()
                    DateSelector.i += 1 # skips past M in AM and PM
                
                if (DateSelector.i > len(DateSelector.date)):
                    return False


            except AttributeError:
                if key == keyboard.Key.esc:
                    return False
                elif key == keyboard.Key.enter:
                    return False
                elif key == keyboard.Key.backspace:
                    if (DateSelector.i < 15):
                        DateSelector.date[DateSelector.i] = "0"
                        DateSelector.i -= 1
                    else:
                        DateSelector.i -= 1
                    if (DateSelector.date[DateSelector.i] in [" ", "/", ":"]):
                        DateSelector.i -= 1
                    DateSelector.__print_date() # I can not figure out why this is required
            DateSelector.__print_date()