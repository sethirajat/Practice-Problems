'''
Write a function Brackets(int n) that prints all combinations of well-formed brackets.
For Brackets(3) the output would be ((())) (()()) (())() ()(()) ()()()
'''
import math

finals = set()
call_count = 0
def brackets(num, s = "", open = 0, closed = 0):
    global finals, call_count
    call_count += 1
    if open - closed < 0 or open > num or closed > num:
        return
    #call_count += 1
    if open == num and closed == num:
        finals.add(s)
        return
    if open < num and open - closed >= 0:
        brackets(num,s[:]+ "(", open+1,closed)

    if closed < num and open - closed > 0:
        brackets(num,s[:] + ")", open, closed +1)

def brackets_iter(num):
    open = 0
    closed = 0

    count = 0
    max_count = math.factorial(2*num)/(math.factorial(num+1)* math.factorial(num))

    while count < max_count:
        

brackets(3)
print "finals is: ", finals
print "total call count is: ", call_count




