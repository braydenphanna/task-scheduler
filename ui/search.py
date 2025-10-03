from scripts.search import Search as S
from pynput import keyboard

# https://www.reddit.com/r/learnpython/comments/aqjfsh/taking_live_keyboard_input_in_python_idle_without/

class Search:
    tasks = []
    query = ""

    def start(t):
        print("search: ", end="", flush=True)
        Search.tasks = t
        with keyboard.Listener(on_press=Search.on_press) as listener:
            listener.join()

    def on_press(key):
        
        Search.__clear_screen()
        try:
            Search.query += key.char
            print("\rsearch: " + Search.query, end="", flush=True)
            
        except AttributeError:
            if key == keyboard.Key.backspace:
                Search.query = Search.query[:-1]
                print("\rsearch: " + Search.query, end="", flush=True)
            elif key == keyboard.Key.space:
                Search.query+=" "
                print("\rsearch: " + Search.query, end="", flush=True)
            elif key == keyboard.Key.esc or key == keyboard.Key.enter:
                # Stop listener
                return False

        print("")
        for task in S.linear(Search.tasks, Search.query):
            if(task.contains(Search.query)): 
                temp = task.clone()

                temp.description = Search.__replaceIgnorecase(temp.description, Search.query)
                temp.name = Search.__replaceIgnorecase(temp.name, Search.query)

                print(temp)

    def __clear_screen():
        # ANSI escape code: clear screen and move cursor to top-left
        print("\033[2J\033[H", end="")

    def __replaceIgnorecase(string, query):
        if len(query)<=0: return string
        
        lowerString = string.lower()
        lowerQuery = query.lower()
        i = lowerString.find(lowerQuery)
        while i != -1:
            string = string[:i]+"\033[35m"+string[i:i+len(query)]+"\033[0m"+string[i+len(query):]
            lowerString =lowerString[:i]+(" " * (len(query)+9))+lowerString[i+len(query):]
            i = lowerString.find(lowerQuery)

        return string

