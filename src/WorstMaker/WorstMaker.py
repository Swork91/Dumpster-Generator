'''
Created on May 7, 2018

@author: Sam
'''
import random
determiner = ("a", "the", "my", "your", 'his', "her", "its", "our", "their", "whose", "this", "that", "these", "those", "which")
noun = ("area","book","business","case","child","company","country","day","eye","fact","family","government","group","hand","home", "job", "life", "lot", "man", "money", "month", "mother", "Mr", "night", "number", "part", "people", "place", "point", "problem", "program", "question", "right", "room", "school", "state", "story", "student", "study", "system", "thing", "time", "water", "way", "week", "woman", "word", "work", "world", "year")
adjective = ("able", "bad", "best", "better", "big", "black", "certain", "clear", "different", "early", "easy", "economic", "federal", "free", "full", "good", "great", "hard", "high", "human", "important", "international", "large", "late", "little", "local", "long", "low", "major", "military", "national", "new", "old", "only", "other", "political", "possible", "public", "real", "recent", "right", "small", "social", "special", "strong", "sure", "true", "white", "whole", "young")
print(random.choice(determiner) + " " + random.choice(adjective) + " " + random.choice(noun))