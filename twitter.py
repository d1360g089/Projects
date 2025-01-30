def main():
    while True:
        try:
            wrd = input("Input: ")
            wd = shorten(wrd)
            print(wd)
        except ValueError:
            pass

def shorten(word):
    vowels = "aeiouAEIOU" 
    result = ''
    for c in word:
        if c not in vowels:
            result = result + c
    return f"Output: {result}"

if __name__ == "__main__":
    main()