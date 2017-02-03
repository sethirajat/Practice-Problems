'''
Leetcode-29

'''

import sys


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return sys.maxint

        if dividend == 0:
            return 0
        numer = abs(dividend)
        denomin = abs(divisor)
        if numer < denomin:
            return 0

        ispositive = True
        if dividend < 0:
            ispositive = not (ispositive)
        if divisor < 0:
            ispositive = not (ispositive)
        denom = denomin
        result = 1
        while denom < numer:
            denom = denom << 1
            result = result << 1
        if denom == numer:
            pass
        else:
            denom >>= 1
            result >>= 1
            answer = 0
            while (result != 0):
                if ( numer >= denom):
                    numer -= denom;
                    answer |= result;
                result >>= 1;
                denom >>= 1;
            result = answer

        '''
        while denom > numer:
            denom -= denomin
            result -= 1
        '''


        if not ispositive:
            result = -result

        #result = min(sys.maxint, result)
        return result

sol1 = Solution()
print "sys maxint is: ", sys.maxint
num, den = map(int,raw_input("enter the divident and divisor separated by space\n").strip().split(' '))
print "dividend is: ", num
print "divisor is: ", den
print "result is: ", sol1.divide(num,den)