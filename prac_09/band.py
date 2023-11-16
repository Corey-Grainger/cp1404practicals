"""CP1404 Week 09 Prac
Band Class
Estimated: 20 minutes
Commenced 1:34pm
Completed 2:03pm"""

class Band():

    def __init__(self, name):
        """Initialise a band."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return the string version of a band."""
        musician_strings = []
        for musician in self.musicians:
            musician_strings.append(str(musician))
        return f"{self.name} ({','.join(musician_strings)})"

    def add(self, musician):
        """Add a Musician to a bands list of musicians."""
        self.musicians.append(musician)

    def play(self):
        """Return each bands members play() contribution."""
        play_strings = []
        for musician in self.musicians:
            play_strings.append(musician.play())
        return ",".join(play_strings)
