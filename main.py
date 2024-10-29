# Code take from: https://rosettacode.org/wiki/Markov_chain_text_generator#Procedural
# text taken from Gutenburg
# No Author listed
# License: GNU Free document License 1.3
# Acessed on: 10/24/2024
# CHANGELOG:
#    - While loop given
#    - Inputs asked
#    - texts from Gutenburg added
import random, sys
from collections import Counter
import math

def makerule(data, context):
    '''Make a rule dict for given data.'''
    rule = {}
    words = data.split(' ')
    index = context
    
    for word in words[index:]:
        key = ' '.join(words[index-context:index])
        if key in rule:
            rule[key].append(word)
        else:
            rule[key] = [word]
        index += 1

    return rule


def makestring(rule, length, temp):    
    '''Use a given rule to make a string.'''
    oldwords = random.choice(list(rule.keys())).split(' ') #random starting words
    string = ' '.join(oldwords) + ' '
    
    for i in range(length):
        try:
            key = ' '.join(oldwords)
            #newword = random.choice(rule[key])
            newword = highest_choice(rule[key], temp)
            string += newword + ' '

            #for word in range(len(oldwords)):
            #    oldwords[word] = oldwords[(word + 1) % len(oldwords)]
            #oldwords[-1] = newword
            oldwords = oldwords[1:] + [newword]
        except KeyError:
            return string
    return string

def countrules(rules_dict):
    stats = {}
    for key in rules_dict.keys():
        stats[key] = Counter(rules_dict[key])
    return stats

def highest_choice(counter,temp):
    opt = counter.most_common()
    #print(opt)
    return opt[math.floor((len(opt)-1)*temp)][0]


def main():
    while True:
        text_list = ["A room with a view.txt", "alice.txt", "Frankenstein.txt", "great gatsby.txt", "the blue castle.txt"]
        num_text = int(input("How many text would you like to combine? (max of 5)"))
        window = int(input("What size window would you like?"))
        temp = float(input("What temperature would you like?"))
        generated = int(input("How many words would you like to generate?"))
        texts = random.sample(text_list, num_text)
        data = ""
        for text in texts:
            with open(text, encoding='utf8') as f:
                data += f.read()        
        rule = makerule(data, window)
        stats = countrules(rule)
        string = makestring(stats, generated, temp)
        print(string)

if __name__ == "__main__":
    main()