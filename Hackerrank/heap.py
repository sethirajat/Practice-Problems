'''
This question is designed to help you get a better understanding of basic heap operations.
You will be given queries of  types:

" " - Add an element  to the heap.
" " - Delete the element  from the heap.
"" - Print the minimum of all the elements in the heap.
NOTE: It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only distinct elements will be in the heap.

Input Format

The first line contains the number of queries, .
Each of the next  lines contains a single query of any one of the  above mentioned types.

Constraints

Output Format

For each query of type , print the minimum value on a single line.

Sample Input

5
1 4
1 9
3
2 4
3
Sample Output

4
9
Explanation

After the first  queries, the heap contains {}. Printing the minimum gives  as the output.
 Then, the  query deletes  from the heap, and the  query gives  as the output.
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT

class heap(object):
    def __init__(self):
        self.elements = []

    def insert(self, val):
        self.elements.append(val)
        if len(self.elements) == 1:
            return
        self.heapify()

    def heapify(self):
        child = len(self.elements) - 1
        parent = int((child - 1) / 2)
        while parent >= 0:
            if self.elements[child] < self.elements[parent]:
                self.elements[child], self.elements[parent] = self.elements[parent], self.elements[child]
                child = parent
                parent = int((child - 1) / 2)
            else:
                break

    def heapify_top(self, x=0):
        parent = x
        left = parent * 2 + 1
        right = parent * 2 + 2

        while left < len(self.elements):
            smaller = left
            if right < len(self.elements) and self.elements[right] < self.elements[left]:
                smaller = right

            if self.elements[smaller] < self.elements[parent]:
                self.elements[smaller], self.elements[parent] = self.elements[parent], self.elements[smaller]
                parent = smaller
                left = parent * 2 + 1
                right = parent * 2 + 2
            else:
                break

    def remove(self, val):
        if len(self.elements) == 0:
            return None
        for x in range(len(self.elements)):
            if self.elements[x] == val:
                break

        self.elements[x], self.elements[-1] = self.elements[-1], self.elements[x]
        res = self.elements.pop()
        self.heapify_top(x)
        return res

    def peek(self):
        if len(self.elements) == 0:
            return None
        return self.elements[0]


heap1 = heap()
querynum = int(raw_input())
for x in range(querynum):
    nwlist = [int(x) for x in raw_input().split()]
    query = nwlist[0]
    if len(nwlist) > 1:
        val = nwlist[1]
    if query == 1:
        heap1.insert(val)

    elif query == 2:
        heap1.remove(val)

    elif query == 3:
        print heap1.peek()
    else:
        print "wrong input"