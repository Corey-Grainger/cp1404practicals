""" CP1404 Week 06 Practicals
ProgrammingLanguage Class"""

class ProgrammingLanguage:
    """Represent a programming language object."""
    def __init__(self, name="", typing="Static", has_reflection=False, year=1900):
        """Construct a Programming language object."""
        self.name = name
        self.typing = typing
        self.has_reflection = has_reflection
        self.year = year

    def __str__(self):
        """Returns the string version of a programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.has_reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if programming language is dynamic."""
        return self.typing == "Dynamic"

