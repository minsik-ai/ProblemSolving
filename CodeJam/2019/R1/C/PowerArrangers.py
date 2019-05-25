import itertools
import sys
import logging

# logging.basicConfig(filename='app.log', filemode='w', level='DEBUG')


class Solution:

    def __init__(self):
        self.currentF = 0
        self.currentSetIndex = 0
        self.currentSet = ''
        self.remainingSets = set([''.join(p) for p in itertools.permutations('ABCDE')])

    def solve(self):
        setIndex = self.currentF // 4

        if setIndex != self.currentSetIndex:
            missing_letters = list(filter(lambda x: x not in self.currentSet, 'ABCDE'))
            self.currentSet += missing_letters[0]

            self.remainingSets.remove(self.currentSet)
            self.currentSet = ''
            self.currentSetIndex = setIndex

        if setIndex > 117:
            # Find Last Sets
            remainings = list(self.remainingSets)
            # logging.debug('Remaining Set : {}'.format(remainings))
            remaining0 = remainings[0]
            remaining1 = remainings[1]
            for i in range(5):
                if remaining0[i] != remaining1[i]:
                    diff_ind = i
                    break

            last_index = setIndex * 5 + diff_ind + 1
            print(last_index)
            # logging.debug('Index : {}'.format(last_index))
            sys.stdout.flush()

            letter = input()
            # logging.debug('Letter : {}'.format(letter))
            if remaining0[diff_ind] == letter:
                print(remaining1)
                # logging.debug(remaining1)
            else:
                print(remaining0)
                # logging.debug(remaining0)

            sys.stdout.flush()

            result = input()
            # logging.debug(result)

            return

        nextNumber = setIndex * 5 + self.currentF % 4 + 1
        print(nextNumber)
        # logging.debug('F : {}'.format(self.currentF))
        # logging.debug('Index : {}'.format(nextNumber))
        sys.stdout.flush()

        letter = input()
        # logging.debug('Letter : {}'.format(letter))
        self.currentSet += letter

        self.currentF += 1
        self.solve()


# logging.debug("Start")
t, f = map(int, input().split())

for _ in range(t):
    Solution().solve()
