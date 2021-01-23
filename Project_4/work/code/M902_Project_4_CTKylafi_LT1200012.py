# -*- coding: utf-8 -*-
#coding=utf-8

'''

Christina-Theano (Theatina) Kylafi
M902 - Project 4
LT1200012

'''

import argparse
from collections import Counter
import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy

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
    

    def ex_4_1(self):
        pass

    def ex_4_2(self):
        pass 

    def ex_4_3(self):
        pass


    def initial_state(self):
        self.training = open("./data/training_sentences.txt","r").read().split("\n")
        self.test = open("./data/test_sentences.txt","r").read().split("\n")

        training_sentences = [ i.split(",") for i in self.training  ]
        self.test_sentences = self.test

        self.negative_class_docs = [ i[0].split(" ") for i in training_sentences if i[1]=="-"]
        self.negative_class_words = [ element for i in self.negative_class_docs for element in i ]
        self.positive_class_docs = [ i[0].split(" ") for i in training_sentences if i[1]=="+"]
        self.positive_class_words = [ element for i in self.positive_class_docs for element in i ]
        
        self.unique_overall_words = set(self.negative_class_words).union(set(self.positive_class_words))


        # print(self.positive_class_words,self.negative_class_words,self.unique_overall_words)


    def prior(self,class_type):
        if class_type=="-":
            return len(self.negative_class_docs)/len(self.training)
        elif class_type=="+":
            return len(self.positive_class_docs)/len(self.training)

    def likelihood(self,word,class_type):
        if class_type =="-":
            class_type_words = self.negative_class_words
        elif class_type =="+":
            class_type_words = self.positive_class_words

        occs_of_word_in_class = class_type_words.count(word)
        # print(f"\nOccurrencies: {occs_of_word_in_class}")

        return (occs_of_word_in_class+1)/ ( len(class_type_words)+len(self.unique_overall_words))

    def test_sentence_cleaning(self):
        self.test = [ [ y for y in i.split(" ") if y in self.unique_overall_words ] for i in self.test ]
        return 


    def ex_4_4(self):
    
        self.initial_state(self)
        self.test_sentence_cleaning(self)

        # negative_class_words,positive_class_words,unique_overall_words = self.load_data()
       
        print(f"Unique words: {len(self.unique_overall_words)}\nNegative class words: {len(self.negative_class_words)}\nPositive class words: {len(self.positive_class_words)}")
        
        # likelihood("μη",negative_class_words,len(unique_overall_words))
        print(f"\nP(-): {self.prior(self,'-')}\nP(+): {self.prior(self,'+')}\n")

        counter = 0
        for test_sentence in self.test:
            print(f"-----> SENTENCE #{counter+1} <-----")
            for class_type in ["-","+"]:
                score  = self.prior(self,class_type)
               
                for word in test_sentence:#.split(" "):
                    
                    word_score = self.likelihood(self,word,class_type)
                    score*= word_score
    
                    print(word, word_score)

                print(f"\nConditional probability P( {class_type} | {self.test_sentences[counter]} ): {score}\n\n")

            counter+=1
        
        return 9    

    def ex_4_5(self):
        pass

    def ex_4_6(self):
        pass

    def ex_4_7(self):
        pass

    def ex_4_8(self):
        pass

    
    def fill_area(pt1,pt2,colour,mean,std):

        plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean, std)], color='black')

        plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean, std)], color='black')

        ptx = np.linspace(pt1, pt2, 10)
        pty = scipy.stats.norm.pdf(ptx,mean,std)

        plt.fill_between(ptx, pty, color=colour, alpha=1.0)


    def ex_4_9(self):
    # pdf for a normal distribution

        x_min = 20.0
        x_max = 90.0

        mean = 50.0
        std = 3.0

        x = np.linspace(x_min, x_max, 10000)

        y = scipy.stats.norm.pdf(x,mean,std)

        plt.plot(x,y, color='black')

        pt1 = [ mean+i*std for i in [1.0,1.0,-1.0,2.0,-2.0,3.0,-3.0] ] 
        pt2 = [ mean+i*std for i in [-1.0,+2.0,-2.0,3.0,-3.0,10.0,-10.0] ] 
        colours = [ '#0b559f', '#2b7bba', '#2b7bba', '#539ecd', '#539ecd', '#89bedc', '#89bedc' ]

        print(pt1,pt2)

        for p1,p2,colour in zip(pt1,pt2,colours):
            self.fill_area(p1,p2,colour,mean,std)


        plt.grid()

        plt.xlim(x_min,x_max)
        plt.ylim(0,0.25)

        # plt.title('How to plot a normal distribution in python with matplotlib',fontsize=10)
        plt.title(f"Probability density of normal distribution N ({ int(mean) }, {int(std)}$^2$)")

        plt.xlabel('x')
        plt.ylabel('Normal Distribution (PDF)')
        ticks = pt1.copy()
        ticks.extend(pt2)
        ticks.append(mean)
        print(ticks)
        plt.xticks( ticks )

        plt.savefig("./normal_distribution.png")
        plt.show()



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