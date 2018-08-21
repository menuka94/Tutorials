class MusicalInstrument:
    no_of_major_keys = 12


class StringInstrument(MusicalInstrument):
    type_of_wood = "Tonewood"


class Guitar(StringInstrument):
    def __init__(self):
        self.no_of_strings = 6
        print("This guitar consists of {} strings. It is made of {} and it can play {} keys.".format(
            self.no_of_major_keys, self.type_of_wood, self.no_of_major_keys))


guitar = Guitar()
