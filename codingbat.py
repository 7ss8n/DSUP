def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

##weekday = False
##vacation = False
##print sleep_in(weekday, vacation)
##
##weekday = True
##vacation = False
##print sleep_in(weekday, vacation)
##
##weekday = False
##vacation = True
##print sleep_in(weekday, vacation)


def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile :
        return True
    elif not a_smile and not b_smile :
        return True
    else:
        return False

def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile :
        return True
    else:
        return False

def sum_double(a, b):
    if a == b:
        return 2*(a + b)
    else:
        return a + b

def diff21(n):
    if n > 21:
        return 2 * (n - 21)
    else:
        return 21 - n

##print diff21(19)
##print diff21(10)
##print diff21(21)
##print diff21(22)


def parrot_trouble(talking, hour):
    if talking and (hour <7 or hour >20):
        return True
    else:
        return False

##print parrot_trouble(True, 6)
##print parrot_trouble(True, 7)
##print parrot_trouble(False, 6)


def makes10(a, b):
    if (a == 10) or (b == 10) or (a + b == 10):
        return True
    else:
        return False

##print makes10(9, 10)
##print makes10(9, 9)
##print makes10(1, 9)


def near_hundred(n):
    if abs(n-100) <= 10 or abs(n-200) <= 10:
        return True
    else:
        return False

##print near_hundred(93)
##print near_hundred(90)
##print near_hundred(89)


def pos_neg(a, b, negative):
    if (a*b < 0) and (not negative):
        return True
    elif a<0 and b<0 and negative:
        return True
    else:
        return False

##print pos_neg(1,-1,False)
##print pos_neg(-1,1,False)
##print pos_neg(-1,-1,True)
##print pos_neg(-1,-1,False)

def not_string(str):
    if str[0:3] == 'not':
        return str
    else:
        return 'not '+str

##print not_string('candy')
##print not_string('x')
##print not_string('not bad')



def missing_char(str, n):
    new = ''
    i = 0
    while i< len(str):
        if i != n:
            new += str[i]
        i += 1
    return new

##print missing_char('kitten', 1)
##print missing_char('kitten', 0)
##print missing_char('kitten', 4)


def front_back(str):
    if len(str) <= 1:
        return str
    else:
        new = str[-1] + str[1:len(str)-1]+str[0]
        return new

##print front_back('code')
##print front_back('a')
##print front_back('ab')

def front3(str):
    if len(str) < 3:
        return 3*str
    else:
        return 3*str[0:3]

##print front3('Java')
##print front3('Chocolate')
##print front3('abc')
##        


def string_times(str, n):
    return n*str

##print string_times('Hi', 2)
##print string_times('Hi', 3)
##print string_times('Hi', 1)


def front_times(str, n):
    if len(str) < 3:
        return n*str
    else:
        return n*str[0:3]
    
##print front_times('Chocolate', 2)
##print front_times('Chocolate', 3)
##print front_times('Abc', 3)


def string_bits(str):
    return str[::2]

##print string_bits('Hello')
##print string_bits('Hi')
##print string_bits('Heeololeo')


def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result += str[:i+1]
    return result
        
##print string_splosion('Code') 
##print string_splosion('abc')
##print string_splosion('ab')


def last2(str):
    count = 0
    last = str[len(str)-2:len(str)]
    for i in range(len(str)-2):
        if str[i:i+2] == last:
            count += 1
    return count

##print last2('hixxhi')
##print last2('xaxxaxaxx')
##print last2('axxxaaxx')
##print last2('xx')


def array_count9(nums):
    count = 0
    for elem in nums:
        if elem == 9:
            count += 1
    return count
        
##print array_count9([1, 2, 9])
##print array_count9([1, 9, 9])
##print array_count9([1, 9, 9, 3, 9])


def array_front9(nums):
    if len(nums)<4:
        front = nums
    else:
        front = nums[:4]

    for elem in front:
        if elem == 9:
            return True
    return False

##print array_front9([1, 2, 9, 3, 4])
##print array_front9([1, 2, 3, 4, 9]) 
##print array_front9([1, 2, 3, 4, 5])


def array123(nums):
    for i in range(len(nums)-2):
        if nums[i:i+3] == [1,2,3]:
            return True
    return False

##print array123([1, 1, 2, 3, 1])
##print array123([1, 1, 2, 4, 1])
##print array123([1, 1, 2, 1, 2, 3])
    

def string_match(a, b):
    lena = len(a)
    lenb = len(b)
    length = min(lena,lenb)
    count = 0
    for i in range(length-1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count

##print string_match('xxcaazz', 'xxbaaz')
##print string_match('abc', 'abc')
##print string_match('abc', 'axc')

##----------------------------------------------
##string-1
def hello_name(name):
    return 'hello '+name+'!'

##print hello_name('Bob')
##print hello_name('Alice')
##print hello_name('X')

def make_abba(a, b):
    return a + 2*b + a
  
##print make_abba('Hi', 'Bye')
##print make_abba('Yo', 'Alice')
##print make_abba('What', 'Up')


def make_tags(tag, word):
    first = '<'+tag+'>'
    last = '</'+tag+'>'
    return first + word + last

##print make_tags('i', 'Yay') 
##print make_tags('i', 'Hello') 
##print make_tags('cite', 'Yay')


def make_out_word(out, word):
    return out[:2] + word + out[2:]

##print make_out_word('<<>>', 'Yay')
##print make_out_word('<<>>', 'WooHoo')
##print make_out_word('[[]]', 'word')


def extra_end(str):
    return 3*str[len(str)-2:]
##print extra_end('Hello')
##print extra_end('ab')
##print extra_end('Hi')


def first_two(str):
    if len(str)<2:
        return str
    else:
        return str[:2]

##print first_two('Hello')
##print first_two('abcdefg')
##print first_two('ab')


def first_half(str):
    #Given a string of even length, return the first half.
    #So the string "WooHoo" yields "Woo".
    return str[:len(str)/2]

##print first_half('WooHoo') 
##print first_half('HelloThere') 
##print first_half('abcdef')

def without_end(str):
    return str[1:len(str)-1]

##print without_end('Hello')
##print without_end('java')
##print without_end('coding')


def combo_string(a, b):
    short = a
    longer = b
    if len(a)>len(b):
        short = b
        longer = a
    return short + longer + short

##print combo_string('Hello', 'hi')
##print combo_string('hi', 'Hello')
##print combo_string('aaa', 'b')

def non_start(a, b):
    return a[1:] + b[1:]

##print non_start('Hello', 'There')
##print non_start('java', 'code')
##print non_start('shotl', 'java')

def left2(str):
  return str[2:]+str[:2]

##print left2('Hello')
##print left2('java')
##print left2('Hi')
##----------------------------------------------
##List-1

def first_last6(nums):
    if nums[0] == 6 or nums[-1] == 6:
        return True
    return False

##print first_last6([1, 2, 6])
##print first_last6([6, 1, 2, 3])
##print first_last6([13, 6, 1, 2, 3])


def same_first_last(nums):
    return len(nums)>=1 and nums[0] == nums[-1]

##print same_first_last([1, 2, 3]) 
##print same_first_last([1, 2, 3, 1])
##print same_first_last([1, 2, 1])

def make_pi():
    return [3,1,4]
        
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
    sum = 0
    for elem in nums:
        sum += elem
    return sum
##print sum3([1, 2, 3])
##print sum3([5, 11, 2])
##print sum3([7, 0, 0])


def rotate_left3(nums):
    return nums[1:]+nums[0:1]

##print rotate_left3([1, 2, 3])
##print rotate_left3([5, 11, 9])
##print rotate_left3([7, 0, 0])

def reverse3(nums):
    return [nums[-1]]+nums[1:2]+nums[0:1]
##print reverse3([1, 2, 3])
##print reverse3([5, 11, 9]) 
##print reverse3([7, 0, 0])

def max_end3(nums):
    value = max(nums[0],nums[-1])
    for i in range(len(nums)):
        nums[i] = value
    return nums

##print max_end3([1, 2, 3])
##print max_end3([11, 5, 9]) 
##print max_end3([2, 11, 3])

def sum2(nums):
    sum = 0
    if len(nums) == 1:
        sum += nums[0]
    elif len(nums) > 1:
        sum = nums[0] + nums[1]
    return sum
        
##print sum2([1, 2, 3]) 
##print sum2([1, 1])
##print sum2([1, 1, 1, 1]) 
##print sum2([])

def middle_way(a, b):
    return [a[1]] + [b[1]]

##print middle_way([1, 2, 3], [4, 5, 6])
##print middle_way([7, 7, 7], [3, 8, 0]) 
##print middle_way([5, 2, 9], [1, 4, 5])

def make_ends(nums):
    return [nums[0]] + [nums[-1]]
##print make_ends([1, 2, 3])
##print make_ends([1, 2, 3, 4]) 
##print make_ends([7, 4, 6, 2]) 
##print make_ends([7])


def has23(nums):
    for elem in nums:
        if elem == 2 or elem == 3:
            return True
    return False

##----------------------------------------------
##Logic-1
def cigar_party(cigars, is_weekend):
    if not is_weekend and (cigars <= 60 and cigars >= 40):
        return True
    elif is_weekend and  cigars >= 40:
        return True
    else:
        return False

##print cigar_party(30, False)
##print cigar_party(50, False) 
##print cigar_party(70, True)


def date_fashion(you, date):
    if you >=8:
       if date<=2:
           return 0
       else:
           return 2
    elif date >= 8:
       if you <= 2:
           return 0
       else:
           return 2        
    elif you <=2 or date<=2:
        return 0
    else:
        return 1

def squirrel_play(temp, is_summer):
    if is_summer:
        return temp>=60 and temp <= 90
    else:
        return temp>=60 and temp <= 100


def caught_speeding(speed, is_birthday):
    if is_birthday:
        if speed <=(60+5):
            return 0
        elif speed >=(61+5) and speed <=(80+5):
            return 1
        elif speed >=(81+5):
            return 2
    else:
        if speed <=60:
            return 0
        elif speed >=61 and speed <=80:
            return 1
        elif speed >=81:
            return 2        

##print caught_speeding(60, False)
##print caught_speeding(65, False) 
##print caught_speeding(65, True) 

def sorta_sum(a, b):
    if a+b <=19 and a+b>=10:
        return 20
    else:
        return a+b


def alarm_clock(day, vacation):
    if vacation:
        if day >=1 and day <=5:
            return "10:00"
        else:
            return "off"
    else:
        if day >=1 and day <=5:
            return "7:00"
        else:
            return "10:00"

##print alarm_clock(1, False) 
##print alarm_clock(5, False) 
##print alarm_clock(0, False) 
      
def love6(a, b):
    if a == 6 or b == 6:
        return True
    elif a+b == 6:
        return True
    elif abs(a-b) == 6:
        return True
    else:
        return False

##print love6(6, 4)
##print love6(4, 5) 
##print love6(1, 5)


def in1to10(n, outside_mode):
    if outside_mode:
        return n<=1 or n>=10
    else:
        return n>=1 and n<=10
    
##print in1to10(5, False)
##print in1to10(11, False)
##print in1to10(11, True) 


def near_ten(num):
    if num%10 <=2 or 10 -num%10 <=2 :
        return True
    return False
##print near_ten(12)
##print near_ten(17) 
##print near_ten(19) 


##----------------------------------------------
##Logic-2
def make_bricks(small, big, goal):
    if big >0:
        if 5*big <=goal:
            goal =goal - 5*big
            big = 0            
        else:
            goal = goal%5
            big = 0
##        print 'small =',small
##        print 'big =',big
##        print 'goal =' ,goal
        return make_bricks(small, big, goal)
    elif big == 0:
##        print 'small =',small
##        print 'big =',big
##        print 'goal =' ,goal
        return small >= goal

##print make_bricks(3, 1, 8)
##print make_bricks(3, 1, 9)
##print make_bricks(3, 2, 10)
##print make_bricks(10, 0, 10)
##print make_bricks(3, 2, 9)
##
##print make_bricks(1, 4, 12)
##print make_bricks(2, 1000000, 1000003)

def make_chocolate(small, big, goal):
    if big >0:
        if 5*big <=goal:
            goal =goal - 5*big
            big = 0            
        else:
            goal = goal%5
            big = 0
        return make_chocolate(small, big, goal)
    else:
        if small >= goal:
            return goal
        else:
            return -1
    
print make_chocolate(4, 1, 9)
print make_chocolate(4, 1, 10) 
print make_chocolate(4, 1, 7)

def lone_sum(a, b, c):
    if a ==b and a== c:
        sum = 0
    elif a== b :
        sum = c
    elif a == c:
        sum = b
    elif b == c:
        sum = a
    else:
        sum = a + b + c
    return sum
##print lone_sum(1, 2, 3) 
##print lone_sum(3, 2, 3)
##print lone_sum(3, 3, 3)   
        
def lucky_sum(a, b, c):
    sum = 0
    if a!=13:
        sum += a
        if b!=13:
            sum += b
            if c!= 13:
                sum += c
    return sum
##print lucky_sum(1, 2, 3) 
##print lucky_sum(1, 2, 13) 
##print lucky_sum(1, 13, 3)     


def no_teen_sum(a, b, c):
    sum = 0
    sum = fix_teen(a)+fix_teen(b)+fix_teen(c)
    return sum

def fix_teen(n):
    if n>=13 and n <=19 and n !=15 and n!=16:
        return 0
    else:
        return n

##print no_teen_sum(1, 2, 3)
##print no_teen_sum(2, 13, 1) 
##print no_teen_sum(2, 1, 14) 

def round_sum(a, b, c):
    return  round10(a) +round10(b) +round10(c)
def round10(num):
    if num%10 >=5:
        return (num/10+1)*10
    else:
        return (num/10)*10

##print round_sum(16, 17, 18)
##print round_sum(12, 13, 14)
##print round_sum(6, 4, 4)



def close_far(a, b, c):
    if isclose(b,a) and isfar(c,a,b):
        return True
    elif isclose(c,a) and isfar(b,a,c):
        return True
    else:
        return False
def isclose(n,m):
    return abs(n-m)<=1
def isfar(a,b,c):
    return abs(a-b)>=2 and abs(a-c)>=2

##print close_far(1, 2, 10) 
##print close_far(1, 2, 3) 
##print close_far(4, 1, 3)

def double_char(str):
    new = ''
    for i in range(len(str)):
        new += str[i]*2
    return new
        
##print double_char('The') 
##print double_char('AAbb') 
##print double_char('Hi-There') 


def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        if str[i:i+2] == 'hi':
            count += 1
    return count

##print count_hi('abc hi ho') 
##print count_hi('ABChi hi') 
##print count_hi('hihi')


def cat_dog(str,substr):
    count_cat = 0
    count_dog = 0    
    for i in range(len(str)-2):
        if str[i:i+3] == 'cat':
            count_cat += 1
        elif str[i:i+3] == 'dog':
            count_dog += 1
    return count_cat == count_dog


def count_code(str):
    count = 0
    for i in range(len(str)-3):
        if str[i:i+2] == 'co' and str[i+3:i+4] == 'e':
            count += 1
    return count

##print count_code('aaacodebbb')
##print count_code('codexxcode')
##print count_code('cozexxcope')


def end_other(a, b):
    if (len(a) < len(b)):
        result = end_other_1(a,b)
    else:
        result = end_other_1(b,a)
    return result

def end_other_1(short,longer):
    n  = len(short)
    s_new = short.lower()
    l_new = longer.lower()
    if l_new[-n:] == s_new:
        return True
    else:
        return False

##print end_other('Hiabc', 'abc')
##print end_other('AbC', 'HiaBc') 
##print end_other('abc', 'abXabc') 


def xyz_there(str):
    for i in range(len(str)-2):
        #print "i = ",i
        if str[i:i+3] == 'xyz' and i==0:
            return True
        elif str[i:i+3] == 'xyz' and str[i-1] != '.':
            return True
    return False
    
##print xyz_there('abcxyz') 
##print xyz_there('abc.xyz') 
##print xyz_there('xyz.abc')

##----------------------------------------------
##List-2
def count_evens(nums):
    count = 0
    for elem in nums:
        if elem %2 == 0:
            count += 1
    return count

##print count_evens([2, 1, 2, 3, 4])
##print count_evens([2, 2, 0])
##print count_evens([1, 3, 5])


def big_diff(nums):
    min = nums[0]
    max = nums[0]
    for elem in nums:
        if elem >max:
            max = elem
        if elem <min:
            min = elem
    return max - min

##print big_diff([10, 3, 5, 6]) 
##print big_diff([7, 2, 10, 9]) 
##print big_diff([2, 10, 7, 2]) 


def centered_average(nums):
    min = nums[0]
    max = nums[0]
    sum = 0
    for elem in nums:
        if elem >max:
            max = elem
        if elem <min:
            min = elem
        sum += elem
    return (sum - max - min) /(len(nums)-2)

##print centered_average([1, 2, 3, 4, 100])
##print centered_average([1, 1, 5, 5, 10, 8, 7])
##print centered_average([-10, -4, -2, -4, -2, 0])


def sum13(nums):
    i = 0
    sum = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            sum += nums[i]
            i += 1
    return sum


##print sum13([1, 2, 2, 1]) 
##print sum13([1, 1]) 
##print sum13([1, 2, 2, 1, 13]) 
##print sum13([1, 13, 2, 1, 13])


def sum67(nums):
    i = 0
    sum = 0
    while i < len(nums):
        if nums[i] == 6:
            i += 1
            while(i<len(nums)):
                if nums[i] == 7:
                    i += 1
                    break
                i += 1
        else:
            sum += nums[i]
            i += 1
    return sum    

##print sum67([1, 2, 2])
##print sum67([1, 2, 2, 6, 99, 99, 7])
##print sum67([1, 1, 6, 7, 2])

def has22(nums):
    for i in range(len(nums)-1):
        if nums[i:i+2]== [2,2]:
            return True
    return False

##print has22([1, 2, 2])
##print has22([1, 2, 1, 2]) 
##print has22([2, 1, 2])



def matrixDimensions(m): 
    rows = len(m)
    cols = len(m[0])
    for elem in m:
        if len(elem) != cols:
            return 'This is not a valid matrix.'
    a = 'This is a {}x{} matrix.'.format(rows,cols)
    return a



def addNumbersInList(numbers):
    min= 0
    for elem in numbers:
        sum += elem
    return sum


def addOddNumbers(numbers):
    new =[]
    for elem in numbers:
        if elem%2 == 0:
            new.append(elem)
    return new

def getMaxNumber(numbers):
    if len(numbers) == 0:
        return 'N.A'
    max= numbers[0]
    for elem in numbers:
        if elem>max:
            max = elem
    return max    


def countA(word):
    count = 0
    for elem in word:
        if elem == 'a':
            count += 1
    return count

def removeLetter(word, letter):
    new= ''
    for elem in word:
        if elem not in letter:
            new += elem
    return new
        
