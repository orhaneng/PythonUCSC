'''
Modified version of problem #414 from project Euler 
(https://projecteuler.net/problem=414)


6174 is a remarkable number; if we sort its digits in increasing order
and subtract that number from the number you get when you sort the digits
in decreasing order, we get 7641-1467=6174. Even more remarkable is that 
if we start from any 4 digit number and repeat this process of sorting and
subtracting, we'll eventually end up with 6174 or immediately with 0 if 
all digits are equal. This also works with numbers that have less than 4 
digits if we pad the number with leading zeroes until we have 4 digits.
E.g. let's start with the number 0837:
8730-0378=8352
8532-2358=6174

6174 is called the Kaprekar constant. The process of sorting and 
subtracting and repeating this until either 0 or the Kaprekar constant 
is reached is called the Kaprekar routine.

Write a Python program to calculate the number of steps to reach the 
Kaprekar constant for values 8730 and 9730. 
'''
mynum = 9730
count = 0
while True:
    mynum_list = list(str(mynum))
    mynum_list.sort()
    mynum_forward = ''.join(mynum_list)
    
    mynum_list.sort(reverse = True)
    mynum_backward = ''.join(mynum_list)
    mynum_forward_int =  int(mynum_forward)
    mynum_backward_int =  int(mynum_backward)
    if mynum_backward_int > mynum_forward_int:
        mynum = mynum_backward_int - mynum_forward_int
    else:
        mynum = mynum_forward_int - mynum_backward_int
    count = count+1
    if mynum == 6174 or mynum == 0:
        break

print('The number of steps to reach Kaprekar constant is ',count)

'''
https://en.wikipedia.org/wiki/Run-length_encoding

Implement an encoding scheme.

The string 
WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW 
has 67 characters. Write a Python program 
to convert this string to 
12W1B12W3B24W1B14W. The new string is created
by calculating the number of times a characters appears consecutively and
placing the character next to it. The new string only needs 18 character,
thus compressing the original string by 73%.
'''


orig_string = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
firstitem = orig_string[0]
count = 0
finalstring = []
for i in range(len(orig_string)-1):
	if orig_string[i] == firstitem:
		count = count+1 
	else:
		newstring = '%d%s'%(count,firstitem)
		finalstring.append(newstring)
		firstitem = orig_string[i]
		count = 1
    
count = count+1 
newstring = '%d%s'%(count,firstitem)
finalstring.append(newstring)
print(''.join(finalstring))


