class Apple:
    manufacturer = "Apple Inc."
    contact_website = "https://www.apple.com/contact"

    def contact_details(self):
        print("To contact us, log on to", self.contact_website)


class MacBook(Apple):
    def __init__(self):
        self.year_of_manufacture = 2017

    def manufacture_details(self):
        print("Manufactured in {} by {}".format(self.year_of_manufacture, self.manufacturer))


macBook = MacBook()
macBook.manufacture_details()
macBook.contact_details()
