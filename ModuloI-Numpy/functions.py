
import numpy as np
import pandas as pd

#Average withouth arguments
def media():
    x=2
    y=4
    avg = (x+y)/2
    return avg

print("Function 1")
print(media())


#Average with arguments
def media2(x,y):

    media = (x+y)/2
    return media

print("Function 2")
print(media2(2,5))

def media3(list):
    somaDaLista=0
    mediaFinal = 0

    for i in range(0,len(list)-1):
        somaDaLista = somaDaLista + list[i]

    mediaFinal = somaDaLista/len(list)
    return mediaFinal

print("Function 1")
print(media3([1,2,3,4]))