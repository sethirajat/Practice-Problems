'''
Given 3 coins of different values, print all the sums of the coins up to 1000. Must be printed in order.

ex: coins(10, 15, 55)
10
15
20
25
30
.
.
.
1000
'''
sums = set()
def coin_sums(coins, idx,csum,S):
    if csum >= S or idx >= len(coins):
        return
    global sums
    curr_sum = csum
    mul = 0
    while curr_sum < S:
        curr_sum = csum + coins[idx]* mul
        sums.add(curr_sum)
        coin_sums(coins,idx+1,curr_sum,S)
        mul += 1

cn = [10,15,25]
id = 0
csm = 0
S = 1000
coin_sums(cn,id,csm,S)
print "the result is: "

print sorted(list(sums))




