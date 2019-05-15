from collections import Collection


class Ship(Collection):
    NotfoundStat = 0
    WondStat = 1
    killStat = 2
    def __init__(self, *cells):
        self.decks = cells
        self.__status = Ship.NotfoundStat

    @property
    def status(self):
        return self.__status


    def check_status(self):
        return self.decks

    def __repr__(self):
        return str(self.decks)

    def __getitem__(self, item):
         return self.decks[item]

    def __len__(self):
        return len(self.decks)

    def __iter__(self):
        return iter(self.decks)

    def __contains__(self, value):
        return value in self.decks