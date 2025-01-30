
class Jar:
    def __init__(self, capacity=12, size=0):
        if capacity < 0:
            raise ValueError("Capacity cant be nagative")
        self._capacity = capacity
        self._size = size

    def __str__(self):
        cookie_output = "🍪" * self._size
        return f"{cookie_output}"
    
    def deposit(self, n):
        if n > 12:
            raise ValueError("Exceeded capacity")
        elif n < 0:
            raise ValueError("Can't deposit a negative amount")
        self._size = self._size + n
        

    def withdraw(self, n):
        if self._size == 0:
            raise ValueError("Not enough cookies to remove")
        elif n > self._size:
            raise ValueError("Can't subtract more than size")
        self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self._size
        
    
def main():
    cookie_jar = Jar(12, 0)
    cookie_jar.deposit(8)
    cookie_jar.withdraw(0)
    print(cookie_jar)





if __name__ == "__main__":
    main()

    