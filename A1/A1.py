#### Question no.1#####
A = [] ## divisible by 7 and Multiple of 5

for i in range(1501,2700):
    if i%7 == 0 and i%5 ==0:
        A.append(i)        
print A

#### END ####
#### Question no.2#####


def Temperature(x ,y):
    if not type(x) == int or type(x) == float:
        print 'Invalid magnitude'
        return a
        
    if y == 'C':
        
        F =(9/5.0)*x +32.0
        print 'Temperature =',F,'Fahrenheit '
        
    if  y == 'F':
        
        C = (5.0/9)*(x - 32.0)
        print 'Temperture =',C,'degree'
    if y != 'F' or y != 'C':
        c = raw_input('''for calculate celsius, input F othrwise C): ''')
        Temperature(x ,c)
a = input('''please_input_magnitude:  ''')
b = raw_input('''please_input_unit: ''')
Temperature(a ,b)



#### END ####
#### Question no.3 #####

from random import randint
def guess(x):
    
    secret_number = randint(0,9)
    if x == secret_number:
        print 'Well guessed!'
        
    else:
        x = input('''try agaim: ''')
        return guess(x)
        
    
x = input('''give guess in range from 0 to 9: ''')
guess(x)


#### END ####
#### Question no.4 #####

n = 0
r = 1
while n<5:
    print '* ' * r
    r += 1
    n += 1
    if n ==5:
        m = n-1
        r = r-2
        while m<5:
            if m <=0:
                break
            else:
                print '* ' * r
                m -= 1
                r -= 1

#### END #####
#### Question no.5 ####

for i  in range(1 ,51):
    i = int(i)
    if i % 3 == 0:
        print 'Fizz'
    if i % 5 == 0:
        print 'Buzz'
    if i%3 == 0 and i%5 ==0:
        print 'FizzBuzz'
    else:
        print i
        
#### END #####
#### Question no.6#####

def sequence(x): 
    for i in x:
        if i%5 == 0:
            print i
        
a = [1100,1101,1010,1111]
sequence(a)
#### Question no.7 ####
   ##==>For 'A' Pattern<==##
  

t = 7
s = 0
x = 9
while t>1:
   
        
    print x*' '+'a'*1+s*'  '+'a'*1
    
    t-=1
    s+=1
    x -=1
    if t == 3:
        x = x-1
        print x*' '+' a '*4
        s+=1
        continue
 
   #==>For 'D' Pattern<==
   
n = 4
while n>1:
    if n == 4:
        print 'D '*3
    print 'D '*1 + 3*' '+'D'*1
    n -= 1
    if n == 1:
        print 'D '*3
        
        
   #==>For '6' Pattern<==
   
for n in range(1 ,8):
    if n == 7 or n == 4 or n == 1:
        print '6 '*4
        continue
    if n == 6 or n == 5:
        print '6 '*1 + 3*' ' + ' 6'*1
        
    if n == 3 or n ==2:
        print '6' *1
        
     
   #==>For 'X' Pattern<==
   
s = 3
r = 7
e = 0
while r>4:
    print e *' ' + 'x' + s*'  ' + 'x'
    e+=1
    r-=1
    s-=1
if r == 4:
    print e *' '+'x'
    r-=1
    e-=1
    s+=1
if r<4:
    while r>0:
        print e *' ' + 'x' + s*'  ' + 'x'
        e-=1
        s+=1
        r-=1
        
    
#### END ####
#### Question no.9####

pA = input('''population of A:''') 
pB = input('''population of B:''')
gA= input('''growth rate of A(input only number  e.g 1 ,3.4...):''')
gB =input('''growth rate of B(input only number  e.g 1 ,3.4...):''')

def calculation(pA,pB,gA,gB):
    if type(pA) == str or type(pB)==str or type(gA)==str or type(gB)==str:
        print 'Please! input integers or float values'
    if pA == pB or gA==gB:
        print 'invalid commands'
    if pA>pB or gA<gB:
        print 'invalid commands'
    Years = 0
    if pA<pB and gA>gB:
        while pA<pB:
            growthA = (pA/100)*gA
            pA = pA + growthA
            growthB = (pB/100)*gB
            pB = pB + growthB
            Years +=1
            
    print 'After',Years,',Population of B = ',pB
    print 'After',Years,',Population of A = ',pA
        
calculation(pA,pB,gA,gB)

#### END #####