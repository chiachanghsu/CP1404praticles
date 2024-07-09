from prac_06.programming_language import ProgrammingLanguage

languages = [ProgrammingLanguage("Python", "Dynamic", True, 1991),
             ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
             ProgrammingLanguage("Visual Basic", "Static", False, 1991)]
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
for language in languages:
    print(language)
print("The dynamically typed languages are:")
for language in languages:
    if ProgrammingLanguage.is_dynamic(language):
        print(language.name)
