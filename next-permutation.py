'''
Can you implement a class that returns the "next" permutation (in no particular order) of representatives chosen from a list of lists.
Also implement a method that determines whether there are any new permutations to return.
I.e., when given [ [1 2] [b] [3 4] ] the permutations are: [1 b 3], [1 b 4], [2 b 3], [2 b 4].

'''

class NextPerm(object):

    def __init__(self):
        self.elements = []
        self.next_perm = []

    def insert(self, arr):
        self.elements.append(arr)
        self.next_perm.append(0)

    def new_perms_possible(self):
        if self.next_perm[0] == -1:
            return False
        else:
            return True

    def get_next_perm(self):
        if not self.new_perms_possible():
            return None
        res = []
        for idx,num in enumerate(self.next_perm):
            res.append(self.elements[idx][num])

        self.setnextperm()
        return res

    def setnextperm(self):
        idx_changed = -1

        elem_len = len(self.next_perm)

        for x in range(elem_len-1,-1,-1):
            if self.next_perm[x] < len(self.elements[x])- 1:
                idx_changed = x
                self.next_perm[x] += 1
                break

        if idx_changed == -1:
            self.next_perm[0] = -1
            return

        for y in range(idx_changed+1,len(self.next_perm)):
            self.next_perm[y] = 0


nextperm1 = NextPerm()
nextperm1.insert([1,2])
nextperm1.insert(['b'])
nextperm1.insert([3,4])
while nextperm1.new_perms_possible():
    print nextperm1.get_next_perm()