"""
This program generates passages that are generated in mad-lib format
Author: Katherin 
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %s were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %s very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %s ruled the world."
print "Mad Libs has Started"
name = raw_input("Enter a name:")
ad1 = raw_input("Enter adjective 1:")
ad2 = raw_input("Enter adjective 2:")
ad3 = raw_input("Enter adjective 3:")
verb =raw_input("Enter any verb:")
print "Enter two nouns"
noun1 = raw_input("noun1:")
noun2 = raw_input("noun2:")
print "Enter any from below"
animal = raw_input("Enter a Animal")
food = raw_input("Enter a food")
fruit = raw_input("Enter a fruit")
superhero = raw_input("Enter a superhero")
country = raw_input("Enter a country")
dessert = raw_input("Enter a dessert")
year = raw_input("Enter a year")
print STORY %(name,ad1,ad2,animal,food,verb,noun1,fruit,ad3,name,superhero,name,country,name,dessert,name,year,noun2)
