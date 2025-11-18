code = input()

source = ""

for first_letter_number in range(len(code)):
    if code[first_letter_number].isupper():
        for second_letter_number in range(first_letter_number + 1, len(code)):
            if code[second_letter_number].isnumeric():
                for letter_number in range(
                    first_letter_number,
                    len(code),
                    second_letter_number - first_letter_number + 1,
                ):
                    source += code[letter_number]
                    if code[letter_number] == ".":
                        break
                break
        break

print(source)
