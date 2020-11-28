import os
import speech_recognition as s
addlist = ['ADD', '+', 'SUM', 'PLUS']
sublist = ['SUBTRACT', 'DIFFERENCE', '-', 'MINUS']
mullist = ['MULTIPLY', 'PRODUCT', 'X', 'x', '*']
divlist = ['DIVISON', 'DIV', '/']
hcflist=['GCD','HCF','GREATEST COMMMON DIVISIOR','HIGHEST COMMON FACTOR']
lcmlist=['LCM','LEAST COMMON MULTIPLE']
factoriallist=['FACTORIAL']
otherlist = ['Sorry,I am not capable of it !', 'Thank you', 'My Name is BraveStone', 'I was developed by Yash Dabhade']
def helpfunction():
    print("You can use the following keyword and sentences::")
    print("\nFor performing additon use keywords and say numbers:")
    for i in addlist:
        print(i,end=' ')
    print("\n\n")
    print("\nFor performing subtraction use keywords and say numbers:")
    for i in sublist:
        print(i,end=' ')
    print("\n\n")
    print("\nFor division use keywords and say numbers:: ")
    for i in divlist:
        print(i,end=' ')
    print("\n\n")
    print("\nFor multiplication use keywords and say number::")
    for i in mullist:
        print(i,end=' ')
    print("\n\n")
    print("\nFor hcf and lcm use keywords and say any two numbers::")
    for i in lcmlist:
        print(i,end=" ")
    print("\n\n")
    for i in hcflist:
        print(i,end=" ")
    print("\n\n")
    print("\nFor factorial say keyword and any one number::")
    print("FACTORIAL")
    print("\n\n")
    print("\nFor exit say exit and for help say help")
    print("\n\nPress Enter to continue >>>>")
    input()
def num_from_text(string1):
    res = [int(e) for e in string1.split(' ') if e.isdigit()]
    return res
def hcf(command):
    l=num_from_text(command)
    x=l[0]
    y=l[1]
    # choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    print('HCF is :: ',hcf)
def lcm(command):
    l=num_from_text(command)
    x=l[0]
    y=l[1]
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    print("LCM is ::",lcm)

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
def factorial(command):
    l = num_from_text(command)
    x = l[0]
    ans=fact(x)
    print("Factorial of ",x," is :: ",ans)
def add(command):
    l=num_from_text(command)
    sum=0
    for i in l:
        sum+=i
    print(sum)
def sub(command):
    l = num_from_text(command)
    sum = 0
    for i in l:
      sum=i-sum
    print(-sum)
def mul(command):
    l = num_from_text(command)
    sum = 1
    for i in l:
        sum *= i
    print(sum)
def div(command):
    l = num_from_text(command)
    sum=l[0]
    i=1
    while(i<len(l)):
        sum=sum/l[i]
        i+=1
    print(sum)
otherstring='WHAT IS YOUR NAME GOOD EXCELLENT VERY NICE FABULOUS MADE DEVELOPED OWNER WRONG INCORRECT BAD NOT BORING'
def other(commandList):
    for i in commandList:
        if i.upper() in 'NAME':
            print(otherlist[2])
            break
        elif i.upper() in 'GOOD EXCELLENT VERY NICE FABULOUS':
            print(otherlist[1])
            break
        elif i.upper() in 'MADE DEVELOPED  OWNER':
            print(otherlist[3])
            break
        elif i.upper() in 'WRONG INCORRECT BAD BORING':
            print(otherlist[0])
            break

    # raise StopIteration
if __name__ == '__main__':
   try:
     print("Welcome to the smart Bravestone calculator (Say help for help) and (Say exit to quit)")
     while True:
       print("\n^^^^ Say Command ^^^^ ")
       r = s.Recognizer()
       print("I am Listening >>>>..........")
       with s.Microphone() as source:
           r.adjust_for_ambient_noise(source)
           # read the audio data from the default microphone
           audio_data = r.record(source,5)
           print("Recognizing...\n")
           # convert speech to text
           text = r.recognize_google(audio_data, language='en-us')


       commandList=[str(e) for e in text.split(' ')]
       command=str(text)

       # numlist=[num_from_text(command)]
       for c in commandList:
           if c.upper() in mullist:
               mul(command)
               break
           elif c.upper() in divlist:
               div(command)
               break
           elif c.upper() in sublist:
               sub(command)
               break
           elif c.upper() in addlist:
               add(command)
               break
           elif c.upper() in otherstring:
               other(commandList)
               break
           elif c.upper() in hcflist:
               hcf(command)
           elif c.upper() in lcmlist:
               lcm(command)
           elif c.upper() in factoriallist:
               factorial(command)
           elif c.upper() in "EXIT QUIT":
               print("Exiting Program !")
               raise StopIteration
           elif c.upper() in "HELP":
               helpfunction()
           else:
             pass
   except NameError:
       print("Some exception came , Please try again.")
   except ValueError:
       print("Some exception came , Please try again.")
   except ArithmeticError:
       print("Some error occured , Please restart the program !")
   except StopIteration:
       print("Good bye")
   finally:
     print("Sorry If i Not heard it please restart the program !!!")
     print("Thank You for using our services:")
     input()




