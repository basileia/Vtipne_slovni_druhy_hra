import json
from collections import defaultdict
from random import choice


def ask_questions(repetition):
    """Ptá se na otázky tolikrát, kolikrát chce uživatel. Ukládá k nim
    odpovědi. Vrací slovník, kde klíčem jsou indexy otázek a hodnotami
    listy odpovědí."""
    questions = ["Kdo? ", "S kým? ", "Co dělali? ", "Kde? ", "Kdy? ", "Proč? "]
    count = 0
    answers = defaultdict(list)
    while count < repetition:
        for question in questions:
            answer = input(question)
            if questions.index(question) == 0:
                answer = answer[0].upper() + answer[1::]
            answers[str(questions.index(question))].append(answer)
        count += 1
    return dict(answers)


def create_sentence(extended_dict):
    """Vybere náhodně odpovědi ze slovníku na sadu otázek a složí z
    nich větu, tu vrátí."""
    new_sentence = []
    for i in range(len(extended_dict)):
        new_sentence.append(choice(extended_dict[str(i)]))
    return " ".join(new_sentence)


def mergeDict(answers, data):
    """Metoda spojí dva slovníky - nové odpovědi od uživatele a odpovědi již
    uložené z jsonu"""
    a, b = answers, data
    merged_dict = defaultdict(list, a)
    for i, j in b.items():
        merged_dict[i].extend(j)
    return dict(merged_dict)


print("Vítej ve hře!")
with open("dataInJson.txt", encoding="utf-8") as fileToRead:
    json_data = json.load(fileToRead)
while True:
    repeat = input("Kolikrát chceš odpovídat na sadu otázek? ")
    try:
        repetition = int(repeat)
        break
    except ValueError:
        print("To nebylo číslo. Zkus to znovu.")
userAnswers = ask_questions(repetition)
extended_dict = mergeDict(userAnswers, json_data)
print("Výsledná věta zní:")
print(create_sentence(extended_dict), ".", sep="")
with open("dataInJson.txt", "w", encoding="utf-8") as file:
    file.write(json.dumps(extended_dict, ensure_ascii=False, indent=2))
