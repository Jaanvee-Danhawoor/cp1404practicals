"""CP1404/CP5632 Practical - ProgrammingLanguage class."""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, field="", typing="", reflection=False, year=0):
        """Initialise a ProgrammingLanguage instance."""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage object."""
        return (f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, "
                f"First appeared in {self.year}")

    def is_dynamic(self):
        """Determine if a ProgrammingLanguage is dynamically typed."""
        return self.typing == "Dynamic"
