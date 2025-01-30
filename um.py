import re

def  main():
    sentence = input("TEXT: ")
    print(count(sentence))


def count(s):
    pattern = r"\bum\b"
    um_pattern = re.findall(pattern, s, flags=re.IGNORECASE)
    
    if um_pattern:
        count = 0
        for i in um_pattern:
            count = count + 1
        return count
    else:
        return 0

if __name__ == "__main__":
    main()


