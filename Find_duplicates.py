# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:02:18 2019

@author: Jędrzej Błaszczak
"""

import sys
import os
import filecmp

args = len(sys.argv);

listOfFiles =[]
while(args>1):
    args-=1
    for path, dnames, fnames in os.walk(sys.argv[args]):
        listOfFiles.extend([os.path.join(path, x) for x in fnames])
    
filesCount = len(listOfFiles)

print("\n# findduplicates ", end='')
for i in range(1, len(sys.argv)):
    print(sys.argv[i] + " ", end='')
print("\n")
found=0;
for i in range(0, filesCount):
    for j in range(i, filesCount):
        if(i!=j):
            if(filecmp.cmp(listOfFiles[i], listOfFiles[j], shallow=False)):
                if(found==0):
                    print("duplicate found | size of file: ", end ='')
                    print(os.path.getsize(listOfFiles[i]), end='')
                    print("B")
                    print(listOfFiles[i])
                    found=1;
                if(found==1):
                    print(listOfFiles[j])
    if(found==1):
        print("")
        found=0;
        
            
print("Done")

