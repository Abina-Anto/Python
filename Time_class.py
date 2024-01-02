class Time:
    def __init__(self, hours, mins, sec):
        self.hours = hours
        self.mins = mins
        self.sec = sec

    def __add__(self, other):
        t3 = Time(0, 0, 0)
        if self.mins + other.mins > 60:
            t3.hours = (self.mins + other.mins) // 60
        t3.hours = t3.hours + self.hours + other.hours
        t3.mins = (self.mins + other.mins) % 60
        t3.sec = self.sec + other.sec
        return t3

    def displayTime(self):
        print("Time is", self.hours, "hours", self.mins, "minutes", "and", self.sec, "seconds")

    def displayMinute(self):
        print("Minutes:", self.hours * 60 + self.mins)

    def displaysecond(self):
        print("Second:", self.hours * 60 * 60 + self.mins * 60 + self.sec)

h1 = int(input("Enter time 1 in hours: "))
m1 = int(input("Enter time 1 in minutes: "))
s1 = int(input("Enter time 1 in seconds: "))
h2 = int(input("Enter time 2 in hours: "))
m2 = int(input("Enter time 2 in minutes: "))
s2 = int(input("Enter time 2 in seconds: "))

a = Time(h1, m1, s1)
b = Time(h2, m2, s2)
c = a + b

c.displayTime()
c.displayMinute()
c.displaysecond()
