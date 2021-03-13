text = input()
str_len = len(text)

string = text[ : str_len // 2].lower() + text[str_len // 2: ].upper()
print(string)