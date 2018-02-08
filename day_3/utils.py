'''
Created on 06/02/2018

@author: Carolina
'''
#Param: any value
#Return: int value
def is_number(value):
    try:
        return int(value)
    except:
        return None
#Param: any value
#Return: real/float value
def is_float(value):
    try:
        return float(value)
    except:
        return None
    
    