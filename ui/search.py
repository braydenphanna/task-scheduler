from scripts.search import Search as S
from pynput import keyboard

# https://www.reddit.com/r/learnpython/comments/aqjfsh/taking_live_keyboard_input_in_python_idle_without/

# https://jakob-bagterp.github.io/colorist-for-python/ansi-escape-codes/
class Search:
    tasks = []
    results = []
    query = ""
    selected = 0

    def start(t):
        print("search: ", end="", flush=True)
        Search.tasks = t
        with keyboard.Listener(on_press=Search.on_press) as listener:
            listener.join()

    def on_press(key):
        Search.__clear_screen()

        try:
            Search.query += key.char
            Search.selected=0
            print("\rsearch: " + Search.query, end="", flush=True)
            
        except AttributeError:
            if key == keyboard.Key.esc:
                # Stop listener
                return False
            elif key == keyboard.Key.backspace:
                Search.query = Search.query[:-1]
                Search.selected=0
            elif key == keyboard.Key.space:
                # using if statement because space as the first character doesn't work for some reason
                if len(Search.query)>0: Search.query+=" "
                Search.selected=0
            elif key == keyboard.Key.up:
                if Search.selected>0: Search.selected-=1
            elif key == keyboard.Key.down:
                Search.selected+=1
            elif key == keyboard.Key.enter:
                Search.results[Search.selected].completed = not Search.results[Search.selected].completed

            print("\rsearch: " + Search.query, end="", flush=True)

        print("")
        i = 0
        Search.results = S.linear(Search.tasks, Search.query)
        for task in Search.results:
            temp = task.clone()

            temp.description = Search.__replaceIgnorecase(temp.description, Search.query)
            temp.name = Search.__replaceIgnorecase(temp.name, Search.query)
            
            if Search.selected == i:
                print(temp.invert())
            else:
                print(temp)  
            
            i+=1

        # Returns the cursor to the next character position in the search bar
        # 9 is the length of "search: " + the length of " " (current character space)
        print(f"\033[0;{9+len(Search.query)}H", end="", flush=True)

    def __clear_screen():
        # ANSI escape code: clear screen and move cursor to top-left
        print("\033[2J\033[H", end="")

    def __replaceIgnorecase(string, query):
        if len(query)<=0: return string
        
        lowerString = string.lower()
        lowerQuery = query.lower()
        i = lowerString.find(lowerQuery)
        while i != -1:
            string = string[:i]+"\033[35m"+string[i:i+len(query)]+"\x1b[37m"+string[i+len(query):]
            lowerString =lowerString[:i]+(" " * (len(query)+10))+lowerString[i+len(query):]
            i = lowerString.find(lowerQuery)

        return string