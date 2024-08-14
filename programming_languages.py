# Dictionary of programming languages and their release years
lang_dict = {"Python": 1991,
             "Ruby": 1995,
             "Java": 1995,
             "C#": 2001,
             "Kotlin": 2011,
             "C++": 1980,
}

# Prompt the user for input
lang1 = input("Enter your language: ")
lang2 = input("Enter your language: ")

 # Calculate the max length of both the languages
max_length = max(len(lang1), len(lang2))

# Print if language found in the dictionary
if lang1 in lang_dict:
    print(f'{lang1:{max_length}} : {lang_dict[lang1]}')

# Print a message if the language is not found
else:
    print(f'{lang1:{max_length}} : Sorry, the language is not in the dictionary.')

# Print if language found in the dictionary
if lang2 in lang_dict:
    print(f'{lang2:{max_length}} : {lang_dict[lang2]}')

# Print a message if the language is not found
else:
    print(f'{lang2:{max_length}} : Sorry, the language is not in the dictionary.')