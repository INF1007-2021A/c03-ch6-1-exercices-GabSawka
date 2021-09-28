#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = []
        i = input(
            "valeur a mettre dans la liste a ordonnée (ENTER pour finir la liste) ")
        while i != "":
            values.append(i)
            i = input(
                "valeur a mettre dans la liste a ordonnée (ENTER pour finir la liste) ")
            print(values)
    values.sort()
    return values
    
def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les valeurs ici
        word1 = input("mot 1: ")
        word2 = input("mot 2: ")
        words =[word1,word2]
    return sorted(words[0])==sorted(words[1])



def contains_doubles(items: list) -> bool:
    return len(items) != len(set(items)) 

def average(grades: list)-> float:
    return sum(grades)/len(grades)

def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_average=0
    name=""
    for student in student_grades:
        moy=average(student_grades[student])
        if  moy > best_average:
            best_average = moy
            name=student
    return {name:best_average}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    sentence_order=sorted(sentence)
    letters=set(sentence_order)
    freq={}
    for letter in letters:
        nb=sentence_order.count(letter)
        if nb>5:
            freq[f"{letter}"] = nb
    return dict(sorted(freq.items(), key=lambda item:item[1],reverse=True))
#  https://thispointer.com/sort-a-dictionary-by-value-in-python-in-descending-ascending-order/

def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    recette= input("nom de recette: ")
    ingredient= input("nom de ingredient separer par espace: ")
    return {recette, ingredient.split()}


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    recette = input("nom de recette: ")
    if recette in ingredients:
        print(recette)


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    print(frequence(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
