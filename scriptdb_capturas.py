# David Carrascal(davidcawork@gmail.com) UAH Department of Automatics  Scholarship assistant (Github: @davidcawork)
# Python 3.6.5

import random
import time
import datetime




def genfichero():
    return open("data-CaptureValue.txt",'w')
  
def terminar(aux):
    
    aux.close()
    return

def escribir(fichero,id,rtt):
    coin = flipflop()
    fecha = (datetime.datetime.now()+datetime.timedelta(seconds=(5+rtt))).strftime("%Y-%m-%d %H:%M:%S")  #Necesitamos formato unix para la fecha
    if coin == 0:
        fichero.write('{},{},1,"{}",1\n'.format(id,random.randint(-10,55),fecha))#Cº
    elif coin == 1:
        fichero.write('{},{},2,"{}",2\n'.format(id,random.randint(1,280),fecha)) #Candela unidad de intensidad luminos
    else:
        fichero.write('{},{},3,"{}",3\n'.format(id,random.randint(0,1),fecha))    #true o false de mov 
    
    return

def flipflop():
    return random.randint(0,2)

if __name__ =='__main__':
    fichero = genfichero()
    rtt=1 #Para variar de una forma más visible la fecha
    for i in range(0,20000):
        escribir(fichero, i,rtt)
        rtt+=2
    terminar(fichero)
    
