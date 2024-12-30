class Time:
    def __init__(self, h, m, s):
        self._hour = h
        self._min = m
        self._sec = s

    def __add__(self, a):
        c = Time(0, 0, 0)
        c._hour = self._hour + a._hour
        c._min = self._min + a._min
        c._sec = self._sec + a._sec
        
        if c._sec >= 60:
            c._sec -= 60
            c._min += 1
        
        if c._min >= 60:
            c._min -= 60
            c._hour += 1
        
        return c

    def display(self):
        print(f"Time: {self._hour:02}:{self._min:02}:{self._sec:02}")

x, y, z = map(int, input("Enter Time 1 in (hh:mm:ss): ").split(":"))
a = Time(x, y, z)

x, y, z = map(int, input("Enter Time 2 in (hh:mm:ss): ").split(":"))
b = Time(x, y, z)

result = a + b
print("Time 1 + Time 2:")
result.display()
