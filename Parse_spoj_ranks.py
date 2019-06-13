# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:48:32 2019

@author: Jędrzej Błaszczak
"""

import sys
import re

sys.stdin.reconfigure(encoding='utf-8')

args = len(sys.argv);
nicknames =[]

if args>1:
    handler = open(sys.argv[1])
    for line in handler:
        pattern = "\"(.*)\""
        result = re.search(pattern, line)
        nicknames.append(result[1])
    handler.close();
 
resultFile = 'wyniki.csv';
handler2 = open(resultFile, "w+");
check = 0;

for line in sys.stdin:
    line.rstrip();
    pattern = "<tr class=\"problemrow\""
    result = re.search(pattern, line)
    if result:
        split_line = re.findall(r'<tr class=\"problemrow\">(.*?)<\/tr>', line)
        split_length = len(split_line);
        for i in range(0, split_length):
            split_record = re.findall(r'<td class=\"mini\">(.*?)<\/td>', split_line[i]);
            record_length = len(split_record);
            for j in range(0, record_length):
                pattern = "users\/(.*)\">(.*)<\/a>"
                result = re.search(pattern, split_record[j])
                if result:
                    if args>1 :
                        nicknames_length = len(nicknames);
                        for k in range(0, nicknames_length):
                            if(nicknames[k] == result[1]):
                                check = 1;
                            
                        if check == 0:
                            break;  
                                      
                    print ("\n%s; " % (result[1]), end='');
                    print ("%s; " % (result[2]), end='');
                    handler2.write("\n%s; " % (result[1]));
                    handler2.write("%s; " % (result[2]));
                
                pattern = "submissions\">(.*)<\/font>"
                result = re.search(pattern, split_record[j])
                if result:
                    pattern = "(\d+).(\d+)";
                    result = re.search(pattern, result[1]);
                    if result:
                        print("%s,%s; " % (result[1], result[2]), end='');
                        handler2.write("%s,%s; " % (result[1], result[2]))                          
                
                pattern = "-"
                result = re.search(pattern, split_record[j])
                if result:
                    print(" 0,0; ", end='');
                    handler2.write(" 0,0; ");
                
                pattern = "mini\">(\d+).(\d+)<\/td>"
                result = re.search(pattern, split_record[j])
                if result:
                    print("$s; " % (result[1]), end='');
                    handler2.write("$s; " % (result[1]))          
                
                if split_record[j] == split_record[record_length-1] :
                    pattern = "(\d+).(\d+)"
                    result = re.search(pattern, split_record[j])
                    if result:
                        print("%s,%s; " % (result[1], result[2]), end='');
                        handler2.write("%s,%s; " % (result[1], result[2]))
                    
                check=0;
          
print("\n\n            Saved\n");
handler2.close();
