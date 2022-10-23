#!/usr/bin/python3
#port-knocking.py
#Pronic numbers  between 4000 and 4999

import socket
import time

def isPronicNumber(num):
    flag = False;
    for j in range(1, num+1):
        #Checks for pronic number by multiplying consecutive numbers    
        if((j*(j+1)) == num):    
            flag = True;    
            break;    
    return flag;   

startTime = time.time()

target = input('Please specify the host that you want to scan: ')
target_IP = target

print ('Initiating Scan for host: ', target_IP)

for i in range(4000,4999):
    if(isPronicNumber(i)):
        print(i)
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = scanner.connect_ex((target_IP, i))  
        scanner.close()

endTime = time.time()
totalTime = endTime - startTime
print('Total Time: %s' %(totalTime))
