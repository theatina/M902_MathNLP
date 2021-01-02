# -*- coding: utf-8 -*-
#coding=utf-8

import argparse
from collections import Counter
import numpy as np
from numpy.linalg import norm

# def load_data():
#     training = open("./data/training_sentences.txt","r").read().split("\n")
#     test = open("./data/test_sentences.txt","r").read().split("\n")

#     training_sentences = [ i.split(",") for i in training  ]

#     negative_class_words = [ i[0].split(" ") for i in training_sentences if i[1]=="-"]
#     negative_class_words = [ element for i in negative_class_words for element in i ]
#     positive_class_words = [ i[0].split(" ") for i in training_sentences if i[1]=="+"]
#     positive_class_words = [ element for i in positive_class_words for element in i ]
    
#     unique_overall_words = set(negative_class_words).union(set(positive_class_words))

#     return negative_class_words,positive_class_words,unique_overall_words


#Exercises
class Exercises:
    
    def initial_state(self):
        self.training = open("./data/training_sentences.txt","r").read().split("\n")
        self.test = open("./data/test_sentences.txt","r").read().split("\n")

        training_sentences = [ i.split(",") for i in self.training  ]

        self.negative_class_docs = [ i[0].split(" ") for i in training_sentences if i[1]=="-"]
        self.negative_class_words = [ element for i in self.negative_class_docs for element in i ]
        self.positive_class_docs = [ i[0].split(" ") for i in training_sentences if i[1]=="+"]
        self.positive_class_words = [ element for i in self.positive_class_docs for element in i ]
        
        self.unique_overall_words = set(self.negative_class_words).union(set(self.positive_class_words))

    def prior(self,class_type):
        if class_type=="-":
            return len(self.negative_class_docs)/len(self.training)
        else:
            return len(self.positive_class_docs)/len(self.training)

    def likelihood(self,word,class_type):
        if class_type =="-":
            class_type_words = self.negative_class_words
        else:
            class_type_words = self.positive_class_words

        occs_of_word_in_class = class_type_words.count(word)
        # print(occs_of_word_in_class)

        return (occs_of_word_in_class+1)/ ( len(class_type_words)+len(self.unique_overall_words))


    def ex_4_1(self):
        pass

    def ex_4_2(self):
        pass 

    def ex_4_3(self):
        pass

    def ex_4_4(self):
    
        self.initial_state(self)
        # negative_class_words,positive_class_words,unique_overall_words = self.load_data()
       
        print(f"Unique words: {len(self.unique_overall_words)}\nNegative class words: {len(self.negative_class_words)}\nPositive class words: {len(self.positive_class_words)}")
        
        # likelihood("μη",negative_class_words,len(unique_overall_words))
        print(self.prior(self,"-"))

        for test_sentence in self.test:
            # print(test_sentence)
            for class_type in ["-","+"]:
                score  = self.prior(self,class_type)
                for word in test_sentence.split(" "):
                    # print(word)
                    if word in self.unique_overall_words:
                        score*= self.likelihood(self,word,class_type)
                
                print(f"\nConditional probability P( {class_type} | {test_sentence} ): {score}")

        
        return 9    

    def ex_4_5(self):
        pass

    def ex_4_6(self):
        pass

    def ex_4_7(self):
        pass

    def ex_4_8(self):
        pass

    def ex_4_9(self):
        pass

    def ex_4_10(self):
        pass


#main
parser = argparse.ArgumentParser()
parser.add_argument("-ex", type=int, help="number of exercise to solve", default=1)
args = parser.parse_args()

if (args.ex > 10) or (args.ex < 1):
    print("\nExercise number must be between 1 - 10 ! !\n")
    exit()

line = ["_" for i in range(100)]
line = "".join(line)

function_to_call_name = "ex_4_" + str(args.ex)
fun_to_call = getattr(Exercises, function_to_call_name)

print("\n--> %s:"%(fun_to_call.__name__))
print(""+str(line)+"\n")
fun_to_call(Exercises)
print(str(line)+"\n")