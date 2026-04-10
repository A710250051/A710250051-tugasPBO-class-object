class RemoteTv():

    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0

    def turnOn(self):
        self.switchIsOn = True

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness += 1

    def show(self):
        print("Switch:", self.switchIsOn)
        print("Brightness:", self.brightness)


# membuat 2 instance
remoteA = RemoteTv()
remoteB = RemoteTv()

remoteA.turnOn()
remoteB.turnOn()

# brightness remoteA dinaikkan 3 kali
remoteA.raiseLevel()
remoteA.raiseLevel()
remoteA.raiseLevel()

# brightness remoteB dinaikkan 1 kali
remoteB.raiseLevel()

print("State Remote A")
remoteA.show()

print("State Remote B")
remoteB.show() 