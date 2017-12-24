####________ Question NO. !_________ ####

def alphabets(string):
    vowels = 'aeiou'
    lst = []
    for i in vowels:
        count = 0
        for j in string:
            if i == j:
                count += 1
        lst.append(str(i) + ' = ' +str(count))
    return tuple(lst)

a  = raw_input('''Please write a sentence: ''')
alphabets(a)

####______ Alternative of Q.1______####
def alphabets(string):
    vowels = 'aeiou'
    lst = []
    for i in vowels:
        count = 0
        for j in string:
            if i == j:
                count += 1
        print i,'=',count

a  = raw_input('''Please write a sentence: ''')
alphabets(a)


####________ Question No.2________####


cost = float(input('''fitness centre fee: '''))
a  = 'a = For senior citizen , 30% discount'
b  = 'b = if you are member since 12 months or more, 15% discount'
c = "c = if you buy more than 5 personal training sessons, 20% discount on each session"
d = "d = None of above"
print a
print b
print c
print d

def membership_fee(t):
    if choice == 'a':
        total_cost = str(cost - (cost * .3))
        return 'Rs.'+total_cost+'/-'
    if choice == 'b':
        total_cost = str(cost - (cost * .15))
        return 'Rs.'+total_cost+'/-'
    if choice == 'c':
        v  = int(input('''How many session will you want to buy?  '''))
        if v >5:
            total_cost = str(v*(cost - (cost * .2)))
            return'Rs.'+total_cost+'/-'
        if v<=5:
            w = int(input('''You can buy more than 5 session not less: '''))
            total_cost = str(w*(cost - (cost * .2)))
            return'Rs.'+total_cost+'/-'
    else:
        cst = str(cost)
        return'Rs.'+cst+'/-'

choice = raw_input('''choose one of above option: ''')
membership_fee(choice)


####________ Question No.3________####

def time_conversion(time):
    a = time.split(time[:-2])
    b = time.split(':')
    if a[1] in ['am','AM','pm','PM'] and int(b[0])< 12:
        t = convert_to_24(time)
    else:
        t = convert_to_12(time)

def convert_to_12(time):  # 24 hours
    a = time.split(':')  #[ 00 , 00 ]
    if a[0] == '00' and int(a[1]) in range(60) and len(a[1]) == 2:
        print '12' + ':' +a[1] + 'AM'
    elif int(a[0]) in range(1,13) and int(a[1]) in range(60) and len(a[1]) == 2:
        print time + 'AM'
    elif int(a[0]) in range(13,24) and int(a[1]) in range(60) and len(a[1]) ==2:
        sub = int(a[0]) - 12 +':' +a[1] + 'AM'
    else:
        t = raw_input('''Please input correct format e.g hh:mm: ''')
        time_conversion(t)
def convert_to_24(time):
    f = time.split(time[:-2])
    x = time.split(time[-2:])
    a  = x[0].split(':')
    if 'pm' in f or 'PM' in f :
        if a[0] == '12' and int(a[1]) in range(60) and len(a[1]) == 2:
            print x[0]+' hrs'
        if int(a[0])<12 and int(a[1]) in range(60) and len(a[1]) == 2:
            y = x[0].split(":")
            z = str(int(y[0]) + 12)
            time1 = z + ":" +y[1]+" hrs"
            print time1
        else:
            t = raw_input('''Please input correct format e.g 12:01pm/PM: ''')
            convert_to_24(t)

    if 'AM'in f or 'am' in f:
        if a[0] == '12' and int(a[1]) in range(60) and len(a[1]) == 2:
            print '00'+ ":" +a[1] + ' hrs'
        if int(a[0])in range(1,12) and int(a[1]) in range(60) and len(a[1]) == 2:
            print x[0] + ' hrs'
        else:
            t = raw_input('''Please input correct format e.g 12:01am/AM: ''')
            convert_to_24(t)



t  = raw_input('''Time: ''')
time_conversion(t)


####_______END_______####
