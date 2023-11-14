"""CP1404 Week 09 Prac
Band Class
Estimated: 20 minutes
Commenced 1:34pm
Completed 2:03pm"""

class Band():

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        musician_strings = []
        for musician in self.musicians:
            musician_strings.append(str(musician))
        return f"{self.name} ({','.join(musician_strings)})"

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        play_strings = []
        for musician in self.musicians:
            play_strings.append(musician.play())
        return ",".join(play_strings)
