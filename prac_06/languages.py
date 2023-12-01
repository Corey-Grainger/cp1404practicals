"""CP1404 Week 06 Practicals
Programming Languages Program

Estimate: 25 minutes
Commenced: 2:27pm
Completed: 2:43pm """

from programming_language import ProgrammingLanguage


python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programming_languages = [ProgrammingLanguage("Python", "Dynamic", True, 1991), ProgrammingLanguage("Ruby", "Dynamic", True, 1995), ProgrammingLanguage("Visual Basic", "Static", False, 1991)]
print("The dynamically typed languages are: ")
for language in programming_languages:
    if language.is_dynamic():
        print(language.name)
