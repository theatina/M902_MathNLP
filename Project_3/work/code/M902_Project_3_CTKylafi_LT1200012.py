# -*- coding: utf-8 -*-
#coding=utf-8
import argparse
from collections import Counter
import numpy as np
from numpy.linalg import norm

def matrix_cofactor(matrix):
    return np.linalg.inv(matrix).T * np.linalg.det(matrix)

#Exercises
class Exercises:
    
    def ex_3_1(self, A=[[2,-3,5],[1,-2,7],[3,8,4]]):
        #Εύρεση υποοριζουσών
        for i in range(len(A)):
            for j in range(len(A[0])):
                print(f"\na_{i+1}{j+1}: {A[i][j]}")
        
    
        return 9

    def ex_3_2(self):
        pass 

    def ex_3_3(self):
        pass

    def ex_3_4(self):
        pass

    def ex_3_5(self):
        pass

    def ex_3_6(self):
        pass

    def ex_3_7(self):
        pass

    def ex_3_8(self):
        pass

    def ex_3_9(self):
        pass

    def ex_3_10(self, d0=[8,6,0], d1=[0,6,8], d2=[6,0,8], d3=[2,3,0], d4=[9,6,0]):
        
        d_vectors = [d0,d1,d2,d3,d4]
        d_vectors_normalised = []
        # print(d_vectors)
        for vect in d_vectors:
            print(norm(vect))
            vect /= norm(vect)
            d_vectors_normalised.append(vect)

        d_vectors_normalised = np.array(d_vectors_normalised)
        d_vectors_normalised_T = d_vectors_normalised.T
        print(d_vectors_normalised)

        similarity_array = d_vectors_normalised @ d_vectors_normalised_T
        print(similarity_array)
        
        corrcoef_vectors = np.corrcoef(d_vectors)
        print("\n%s\n"%(corrcoef_vectors))

        high_threshold = 0.9
        for j in range(similarity_array.shape[1]):
            for i in range(j+1,similarity_array.shape[0]):
                if similarity_array[i,j] >= high_threshold:
                    print("\nDot product d%d • d%d: %.4f (Correlation: %.4f)  ->  Documents %d and %d are similar ! ! \n"%(j+1, i+1, similarity_array[i,j],corrcoef_vectors[i,j], j+1, i+1 ))
                else:
                    print("\nDot product d%d • d%d: %.4f (Correlation: %.4f)\n"%(j+1, i+1, similarity_array[i,j], corrcoef_vectors[i,j]))
        


        return 9


#main
parser = argparse.ArgumentParser()
parser.add_argument("-ex", type=int, help="number of exercise to solve", default=1)
args = parser.parse_args()

if (args.ex > 10) or (args.ex < 1):
    print("\nExercise number must be between 1 - 10 ! !\n")
    exit()

line = ["_" for i in range(100)]
line = "".join(line)

function_to_call_name = "ex_3_" + str(args.ex)
fun_to_call = getattr(Exercises, function_to_call_name)

print("\n--> %s:"%(fun_to_call.__name__))
print(""+str(line)+"\n")
fun_to_call(Exercises)
print(str(line)+"\n")