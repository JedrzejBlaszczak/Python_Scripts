# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 14:26:39 2019

@author: Jędrzej Błaszczak
"""

import random as random

def zaklam(sig):
    i = random.randrange(0, 6, 1)
    if(sig[i] == 1):
        sig[i] = 0
    else:
        sig[i] = 1
    
    return sig, i


def nadajnik(sig):
    hamKod = []
    
    x1 = (sig[3] + sig[2] + sig[0]) % 2
    x2 = (sig[3] + sig[1] + sig[0]) % 2
    x4 = (sig[2] + sig[1] + sig[0]) % 2
    
    hamKod.append(x1)
    hamKod.append(x2)
    hamKod.append(sig[3])
    hamKod.append(x4)
    hamKod.append(sig[2])
    hamKod.append(sig[1])
    hamKod.append(sig[0])
    
    hamKod.reverse()
    
    return hamKod

def odbiornik(sig):
    sig.reverse()
    flaga = 0
    dekod = []
    
    x1 = sig[0]
    x2 = sig[1]
    x4 = sig[3]
    
    x11 = (sig[2] + sig[4] + sig[6]) % 2
    x22 = (sig[2] + sig[5] + sig[6]) % 2
    x44 = (sig[4] + sig[5] + sig[6]) % 2
    
    x111 = (x1 + x11) % 2
    x222 = (x2 + x22) % 2
    x444 = (x4 + x44) % 2

    S = x111 *(2>>1) + x222 * 2 + x444 * (2<<1)
    
    print("")
    print("x1: ", x1)
    print("x2: ", x2)
    print("x4: ", x4)
    print("x1': ", x11)
    print("x2': ", x22)
    print("x4': ", x44)
    print("x1^: ", x111)
    print("x2^: ", x222)
    print("x4^: ", x444)
    print("S:", S)
    print("")
    
    if(S!=0):
        flaga =1
        
        if(sig[S-1] == 1):
            sig[S-1] = 0
        else:
            sig[S-1] = 1
        
        x1 = sig[0]
        x2 = sig[1]
        x4 = sig[3]
    
        x11 = (sig[2] + sig[4] + sig[6]) % 2
        x22 = (sig[2] + sig[5] + sig[6]) % 2
        x44 = (sig[4] + sig[5] + sig[6]) % 2

        x111 = (x1 + x11) % 2
        x222 = (x2 + x22) % 2
        x444 = (x4 + x44) % 2

        S = x111 *(2>>1) + x222 * 2 + x444 * (2<<1)
        
        print("x1: ", x1)
        print("x2: ", x2)
        print("x4: ", x4)
        print("x1': ", x11)
        print("x2': ", x22)
        print("x4': ", x44)
        print("x1^: ", x111)
        print("x2^: ", x222)
        print("x4^: ", x444)
        print("S:", S)
        print("")
        if(S!=0):
            flaga = 2
    
    dekod.append(sig[6])
    dekod.append(sig[5])
    dekod.append(sig[4])
    dekod.append(sig[2])
    
    return dekod, flaga

m = [1, 1, 0, 0]
print("Oryginalny sygnal: ",m)
    
hamKod = nadajnik(m)
print ("Kod Hamminga: ", hamKod)

hamKod, bit=zaklam(hamKod)
print("Zaklamano ",bit,". bit", sep='')

dekod, flaga = odbiornik(hamKod)
print ("Sygnal odebrany: ",dekod)

if(flaga!=0):
    print("")
    print("Dokonano przestawienia bitu")