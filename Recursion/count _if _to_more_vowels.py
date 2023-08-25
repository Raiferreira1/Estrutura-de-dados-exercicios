import unicodedata


def remove_accent(str: str):
    nfkd_form = unicodedata.normalize("NFKD", str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])


def count_if_to_more_vowels(string: str, count_vowel=0, count_consuant=0, vowels: str = "aeiou"):
    if not string:
        return count_vowel > count_consuant
    else:
        if string[0].lower() in vowels:
            return count_if_to_more_vowels(string[1:], count_vowel + 1, count_consuant)
        elif string[0].isalpha():
            return count_if_to_more_vowels(string[1:], count_vowel, count_consuant + 1)
        else:
            return count_if_to_more_vowels(string[1:], count_vowel, count_consuant)


print(count_if_to_more_vowels(remove_accent("Não")))


# def hasMoreVowels(text, vowels, counter=0, index=0):
#     if index == len(text):
#         return counter > index / 2
#     if text[index] in vowels:
#         return hasMoreVowels(text, vowels, counter + 1, index + 1)
#     return hasMoreVowels(text, vowels, counter, index + 1)


# vowels = "aeiouAEIOUáéíóúÁÉÍÓÚãõÃÕàèìòùÀÈÌÒÙäëïöüÄËÏÖÜ"
# text = str(input(">>> Informe um texto qualquer: "))
# print(
#     f'O texto "{text}"{"" if hasMoreVowels(text, vowels) else " não"} tem mais vogais que consoantes.'
# )
