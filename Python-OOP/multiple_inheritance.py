class OperatingSystem:
    multitasking = True
    name = "MacOS"

class Apple:
    name = "Apple"
    website = "https://www.apple.com"


class MacBook(Apple, OperatingSystem):
    def __init__(self):
        if self.multitasking:
            print("This is a multitasking enabled system. Visit {} for more details.".format(self.website))
            print("Name:", self.name)


macBook = MacBook()
