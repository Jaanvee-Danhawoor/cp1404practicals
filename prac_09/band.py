"""Band class for CP1404"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def __repr__(self):
        """Return a string representation of a Band."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Iterate through each musician in the band and return a string showing the instrument they are playing
        if any."""
        if not self.musicians:
            return f"{self.name} has no musicians."
        return '\n'.join(musician.play() for musician in self.musicians)
