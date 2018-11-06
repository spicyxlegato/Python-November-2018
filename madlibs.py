"""
This program generates passages that are generated in mad-lib format
Author: Robert
"""

# The template for the story

story = "Late in the evening, %s woke up feeling %s. 'It is going to be a %s night...' " \
        "Outside, a bunch of %ss were protesting to keep %ss in stores. They began to %s to the " \
        "rhythm of the %s, which made all the %ss incredibly %s. Rightly concerned, %s sent a raven to %s, " \
        "who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a time " \
        "when %ss ruled the world."

print("Mad libs has started!")

name = input("Enter a name: ")
ad1 = input("Give me one adjective: ")
ad2 = input("Give me another one: ")
ad3 = input("Give me one more: ")
verb = input("How about a verb?: ")
noun1 = input("Now give me a noun: ")
noun2 = input("One more noun: ")
animal = input("Enter a random animal: ")
food = input("Enter a random food: ")
fruit = input("Enter a random fruit: ")
superhero = input("Enter a random superhero: ")
country = input("Enter a random country: ")
dessert = input("Enter a random dessert: ")
year = input("Enter a random year: ")

print(story % (name, ad1, ad2, animal, food, verb, noun1, fruit, ad3, name,
               superhero, name, country, name, dessert, name, year, noun2))