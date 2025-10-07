from scripts.search import Search as S
from pynput import keyboard

# https://www.reddit.com/r/learnpython/comments/aqjfsh/taking_live_keyboard_input_in_python_idle_without/
# https://jakob-bagterp.github.io/colorist-for-python/ansi-escape-codes/

class Search:
    tasks = []
    results = []
    query = ""
    selected = 1

    page_length = 8
    page = 1

    def start(t):
        Search.__clear_screen()
        print("search: ", end="", flush=True)
        Search.tasks = t
        Search.__print_results()
        with keyboard.Listener(on_press=Search.__on_press) as listener:
            listener.join()

    def __on_press(key):
        Search.__clear_screen()

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
            elif key == keyboard.Key.backspace:
                Search.query = Search.query[:-1]
                Search.selected=(Search.page*Search.page_length)-Search.page_length+1
            
            # space: adds an empty character to query (can't type space first)
            elif key == keyboard.Key.space and len(Search.query)>0:
                Search.query+=" "
                Search.selected=(Search.page*Search.page_length)-Search.page_length+1

            # up arrow: moves task selector up one position (if possible)
            elif key == keyboard.Key.up:
                if Search.selected>(Search.page*Search.page_length)-Search.page_length+1: Search.selected-=1
                elif Search.selected==(Search.page*Search.page_length)-Search.page_length+1 and Search.page>1: 
                    Search.page-=1
                    Search.selected-=1

            # down arrow: moves task selector down one position (if possible)
            elif key == keyboard.Key.down:
                if Search.selected<= Search.page*Search.page_length and Search.selected<len(Search.results): Search.selected+=1
                elif Search.selected==Search.page*Search.page_length and Search.page<len(Search.results)/Search.page_length: 
                    Search.page+=1
                    Search.selected+=1

            # right arrow: jumps forward one page (if possible)
            elif key == keyboard.Key.right and Search.page<len(Search.results)/Search.page_length:
                Search.page+=1
                # Cursor resets to the first of each page on page switch
                #Search.selected=(Search.page*Search.page_length)-Search.page_length+1

                # Cursor stays in the same spot on page switch
                Search.selected+=Search.page_length
                if Search.selected >len(Search.results): Search.selected = len(Search.results)

            # left arrow: jumps back one page (if possible)
            elif key == keyboard.Key.left and Search.page>1:
                Search.page-=1
                
                # Cursor goes to the first of each page on page switch
                #Search.selected=(Search.page*Search.page_length)-Search.page_length+1

                # Cursor stays in the same spot on page switch
                Search.selected-=Search.page_length

        print("\rsearch: " + Search.query, end="", flush=True)
        Search.__print_results()
       
    def __print_results():
        print("")
        i = 1
        Search.results = S.linear(Search.tasks, Search.query)
        for task in Search.results:
            if i < Search.page*Search.page_length-Search.page_length+1:
                i+=1
                continue
            elif i > Search.page*Search.page_length:
                print(f"◄  {int(Search.page)}  ►".center(60))
                break

            temp = task.clone()

            temp.description = Search.__colorSubstring(temp.description, Search.query)
            temp.name = Search.__colorSubstring(temp.name, Search.query)
            
            if Search.selected == i:
                spacing = len(task.name)+len(task.description)+2-len(task.due_date.strftime("%#m/%#d/%y, %#I:%M %p"))
                print(temp.invert(spacing))
            else:
                print(temp)  
            
            if i == len(Search.results): 
                print(f"◄  {int(Search.page)}  ►".center(60))

            i+=1
            
        # Returns the cursor to the next character position in the search bar
        # 9 is the length of "search: " + the length of " " (current character space)
        print(f"\033[0;{9+len(Search.query)}H", end="", flush=True)

    def __clear_screen():
        # ANSI escape code: clear screen and move cursor to top-left
        print("\033[2J\033[H", end="")

    def __colorSubstring(string, substring):
        # 1. get indexes of all occurrences of substring in string
        #    goes backwards for step 2
        occurrences = []
        for i in range(len(string) - len(substring) + 1, -1, -1):
            if (string[i:i + len(substring)].lower() == substring.lower()):
                occurrences.append(i)

        # 2. add parentheses around occurrence
        letters = list(string)
        for occurrence in occurrences:
            letters.insert(occurrence, "(")
            letters.insert(occurrence + len(substring) + 1, ")")
        string = ''.join(letters)
        
        # 3. remove redundant parentheses
        #    goes backwards for step 4
        redundancies = []
        i = 0
        for j in range(len(string) - 1, -1, -1):
            if (string[j] == "("):
                i -= 1
            if ((string[j] == "(" or string[j] == ")") and i > 0):
                redundancies.append(j)
            if (string[j] == ")"):
                i += 1

        for j in redundancies:
            string = string[:j] + string[j + 1:]

        # 4. replace parentheses with color escape codes
        return string.replace("(", "\033[35m").replace(")", "\033[37m")
    