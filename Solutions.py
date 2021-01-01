import json
import time
import threading
from threading import *
dic = {} # We are taking input from JSON file but shall do the operation using this dictionary
#dic1 = {} # temp dictionary for conversion
#key = ""
#out_file = open("output_data.json","w")
def create(json_file_name, timeout=0):
    """
    out_file = open("output_data.json","w")
    with open('output_data.json') as json_file:
        dic = json.load(json_file)
    """
    with open(json_file_name) as json_file:
        dic1 = json.load(json_file)
    for k in dic1.keys():
        key = k
    value = dic1[key]
    if key in dic:
        print("error: this key already exists")
        return 0
    else:
        if(key.isalpha()):
            if type(value) == int:
                if len(dic)<(1024*1020*1024) and value<=(16*1024):
                    if timeout==0:
                        l=[value,timeout]
                    else:
                        l=[value,time.time()+timeout]
                    if len(key)<=32:
                        dic[key] = l
                    return 1
                else:
                    print("error: Memory limit exceeded !!!")
                    return 0
            elif isinstance(value,dict):
                if len(dic)<(1024*1020*1024) and len(value) <= (16*1024):
                    if timeout==0:
                        l=[value,timeout]
                    else:
                        l=[value,time.time()+timeout]
                    if len(key)<=32:
                        dic[key] = l
                    #json.dump(dic, out_file)
                    return 1
                else:
                    print("error: Memory limit exceeded !!!")
                    return 0
        else:
            print("error: Invalid key_name !!! key_name must contain only alphabets and no special characters or numbers")
            return 0
    #json.dump(dic, out_file)
            
def read(key):
    if key not in dic:
        print("error: given key does not exist in data-store. Please enter a valid key")
        return 0
    else:
        dummy=dic[key]
        if dummy[1]!=0:
            if time.time()<dummy[1]:
                s = '{"' + str(key)+'" :' + str(dummy[0]) + "}"
                print(s)
                return 1
            else:
                print("error: time-to-live of",key,"has expired")
                return 0
        else:
            s = '{"' + str(key)+'" :' + str(dummy[0]) + "}"
            print(s)
            return 1
def delete(key):
    """
    out_file = open("output_data.json","w")
    with open('output_data.json') as json_file:
        dic = json.load(json_file)
    """
    if key not in dic:
        print("error: given key does not exist in data-store. Please enter a valid key") 
    else:
        dummy=dic[key]
        if dummy[1]!=0:
            if time.time()<dummy[1]:
                del dic[key]
                print("key is successfully deleted")
                #json.dump(dic, out_file, indent=2)
                return 1
            else:
                print("error: time-to-live of",key,"has expired")
                return 0
        else:
            del dic[key]
            print("key is successfully deleted")
            #json.dump(dic, out_file, indent=2)
            return 1
