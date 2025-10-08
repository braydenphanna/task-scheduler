from scripts.search import Search as S
from pynput import keyboard
import pywinctl
from ui.util import Util
import os
import math

# https://www.reddit.com/r/learnpython/comments/aqjfsh/taking_live_keyboard_input_in_python_idle_without/
# https://jakob-bagterp.github.io/colorist-for-python/ansi-escape-codes/

class Search:
    tasks = []
    results = []
    query = ""
    windowTitle = ""
    selected = 1
    page = 1
    tasks_per_page = math.floor((os.get_terminal_size().lines - 4) / 2)

    def start(t):
        Search.windowTitle = pywinctl.getActiveWindowTitle()
        Util.clear_screen()
        print("search: ", end="", flush=True)
        Util.print_bar()
        Search.tasks = t
        Search.__print_results()
        with keyboard.Listener(on_press=Search.__on_press) as listener:
            listener.join()

    def __on_press(key):
        if Search.windowTitle == pywinctl.getActiveWindowTitle():
            Util.clear_screen()
            Search.tasks_per_page = math.floor((os.get_terminal_size().lines - 4) / 2)

            try:
                # any letter key: adds letter to query
                Search.query += key.char
                Search.selected=1
                Search.page=1

            except AttributeError:
                # esc: exit the search menu
                if key == keyboard.Key.esc:
                    # Stop listener
                    return False
                
                # enter: marks selected task as complete or incomplete
                elif key == keyboard.Key.enter:
                    Search.results[Search.selected-1].completed = not Search.results[Search.selected-1].completed

                # backspace: delete the last typed character in query
                elif key == keyboard.Key.backspace and len(Search.query) > 0:
                    Search.query = Search.query[:-1]
                    Search.selected=(Search.page*Search.tasks_per_page)-Search.tasks_per_page+1
                
                # space: adds an empty character to query (can't type space first)
                elif key == keyboard.Key.space and len(Search.query)>0:
                    Search.query+=" "
                    Search.selected=(Search.page*Search.tasks_per_page)-Search.tasks_per_page+1

                # up arrow: moves task selector up one position (if possible)
                elif key == keyboard.Key.up:
                    if Search.selected>(Search.page*Search.tasks_per_page)-Search.tasks_per_page+1: 
                        Search.selected-=1
                    elif Search.selected==(Search.page*Search.tasks_per_page)-Search.tasks_per_page+1 and Search.page>1: 
                        Search.page-=1
                        Search.selected-=1

                # down arrow: moves task selector down one position (if possible)
                elif key == keyboard.Key.down:
                    if Search.selected < Search.page*Search.tasks_per_page and Search.selected<len(Search.results): 
                        Search.selected+=1
                    elif Search.selected==Search.page*Search.tasks_per_page and Search.page<len(Search.results)/Search.tasks_per_page: 
                        Search.page+=1
                        Search.selected+=1

                # right arrow: jumps forward one page (if possible)
                elif key == keyboard.Key.right and Search.page<len(Search.results)/Search.tasks_per_page:
                    Search.page+=1
                    # Cursor resets to the first of each page on page switch
                    #Search.selected=(Search.page*Search.tasks_per_page)-Search.tasks_per_page+1

                    # Cursor stays in the same spot on page switch
                    Search.selected+=Search.tasks_per_page
                    if Search.selected >len(Search.results): 
                        Search.selected = len(Search.results)

                # left arrow: jumps back one page (if possible)
                elif key == keyboard.Key.left and Search.page>1:
                    Search.page-=1
                    
                    # Cursor goes to the first of each page on page switch
                    #Search.selected=(Search.page*Search.tasks_per_page)-Search.tasks_per_page+1

                    # Cursor stays in the same spot on page switch
                    Search.selected-=Search.tasks_per_page

            print("search: " + Search.query, end="", flush=True)
            Util.print_bar()
            Search.__print_results()
       
    def __print_results():
        print("")
        i = 1
        Search.results = S.linear(Search.tasks, Search.query)
        for task in Search.results:
            if i < Search.page*Search.tasks_per_page-Search.tasks_per_page+1:
                i+=1
                continue
            elif i > Search.page*Search.tasks_per_page:
                print(f"◄  {int(Search.page)}  ►".center(os.get_terminal_size().columns))
                break

            temp = task.clone()

            temp.description = Util.color_substring(temp.description, Search.query)
            temp.name = Util.color_substring(temp.name, Search.query)
            
            if Search.selected == i:
                spacing = len(task.name)+len(task.description)+2-len(task.due_date.strftime("%#m/%#d/%y, %#I:%M %p"))
                print(temp.invert(spacing))
            else:
                print(temp)  
            
            if i == len(Search.results): 
                print(f"◄  {int(Search.page)}  ►".center(os.get_terminal_size().columns))

            i+=1
            
        # Returns the cursor to the next character position in the search bar
        # 9 is the length of "search: " + the length of " " (current character space)
        print(f"\033[0;{9+len(Search.query)}H", end="", flush=True)
    