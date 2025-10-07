import os

class Util:
    def clear_screen():
        # ANSI escape code: clear screen and move cursor to top-left
        print("\033[2J\033[H", end="")

    def print_bar():
        print("\n" + "─" * os.get_terminal_size().columns, end="")

    def color_substring(string, substring):
        if (len(substring) == 0):
            return string

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
        return string.replace("(", "\033[35m").replace(")", "\033[39m")