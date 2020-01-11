from copy import deepcopy
'''
backtracking??algorithm which give me all the possible ways to have [1, 0 ,0..] with a given number of ones
used for coset
'''
class Backtracking(object):
    def __init__(self, number, ones):
        self.number = number
        self.ones = ones
        self.data = [0] * self.number
        self.last_list = []

    def ok(self):
        one = 0
        for i in range(self.number):
            if self.data[i] == 1:
                one += 1
        if one == self.ones:
            return 1
        return 0

    def sol(self, k):
        return k == self.number

    def backtracking(self, k):
        if k == self.number:
            return 0
        for i in [1, 0]:
            self.data[k] = i
            if self.ok():
                found = False
                for i in self.last_list:
                    if i == self.data:
                        found = True
                if found == False:
                    self.last_list.append(deepcopy(self.data))
                self.data[k] = 0
                self.backtracking(k+1)
            else:
                self.backtracking(k+1)

    def __str__(self):
        return str(self.last_list)

b = Backtracking(6, 1)
b.backtracking(0)
