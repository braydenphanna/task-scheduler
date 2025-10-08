from pynput import keyboard
from ui.util import Util

class DateSelector:
    date = []
    i = 0

    def start():
        DateSelector.date = list("00/00/00 12:00 PM")
        i = 0
        print(DateSelector.date)
        print("".join(DateSelector.date), end=f"\r{"".join(DateSelector.date[:DateSelector.i])}", flush=True)
        with keyboard.Listener(on_press=DateSelector.__on_press) as listener:
            listener.join()
    
    def __on_press(key):
        # if Search.windowTitle == pywinctl.getActiveWindowTitle():
        #     Util.clear_screen()
        Util.clear_screen()

        try:
            if (DateSelector.date[DateSelector.i] != "/"):
                DateSelector.date[DateSelector.i] = key.char
                DateSelector.i += 1
                if (DateSelector.date[DateSelector.i] == "/" or DateSelector.date[DateSelector.i] == " "):
                    DateSelector.i += 1

        except AttributeError:
            # esc: exit the search menu
            if key == keyboard.Key.esc:
                # Stop listener
                return False
            
            # enter
            elif key == keyboard.Key.enter:
                pass

            # backspace
            elif key == keyboard.Key.backspace:
                pass
            
            # space
            elif key == keyboard.Key.space:
                pass

            # right arrow
            elif key == keyboard.Key.right:
                pass

            # left arrow
            elif key == keyboard.Key.left and Search.page>1:
                pass

        print("".join(DateSelector.date), end=f"\r{"".join(DateSelector.date[:DateSelector.i])}", flush=True)