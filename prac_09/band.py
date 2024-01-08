class Band:

    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def __str__(self):
        musicians_str = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_str})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician in the band playing their instrument."""
        return '\n'.join(musician.play() for musician in self.musicians)

