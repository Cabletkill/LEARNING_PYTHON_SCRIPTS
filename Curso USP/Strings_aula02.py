def fazAlgo(string):
    pos = 0
    string1 = string.capitalize()
    while pos < len(string):
        if string[pos] == " ":
            string1 = string1 + string[pos]
        pos = pos + 1
    print(string1)
def main():
    string=("É UM TESTE")
    fazAlgo(string)
main()

