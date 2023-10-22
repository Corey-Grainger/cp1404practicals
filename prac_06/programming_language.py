""" CP1404 Week 06 Practicals
ProgrammingLanguage Class"""

class ProgrammingLanguage:
    def __init__(self, name="", typing="Static", has_reflection=False, year=1900):
        """Programming language class"""
        self.name = name
        self.typing = typing
        self.has_reflection = has_reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.has_reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"

