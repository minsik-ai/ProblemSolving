import itertools
import sys
import logging

# logging.basicConfig(filename='app.log', filemode='w', level='DEBUG')


class Solution:

    def __init__(self):
        self.letterOffset = 1
        self.positions = {ch: [] for ch in 'ABCDE'}
        self.searchPositions = [x for x in range(119)]
        self.result = ''

    def solve(self):
        position = self.searchPositions.pop()

        index = position * 5 + self.letterOffset
        print(index)
        sys.stdout.flush()

        # logging.debug('Index : {}'.format(index))

        letter = input()
        self.positions[letter].append(position)

        # logging.debug('Letter : {}'.format(letter))

        if not self.searchPositions:
            result_letter = min(self.positions.items(), key=lambda x: len(x[1]))[0]
            self.searchPositions = self.positions[result_letter]
            # logging.debug('Search Positions : {}'.format(self.searchPositions))
            self.result += result_letter
            self.letterOffset += 1
            # logging.debug('Iterated Result : {}'.format(self.result))

            del self.positions[result_letter]
            for key in self.positions:
                self.positions[key] = []

            if self.letterOffset == 5:
                last_letter = list(filter(lambda x: x not in self.result, 'ABCDE'))[0]
                self.result += last_letter
                # logging.debug('Last Letter : {}'.format(last_letter))

                print(self.result)
                sys.stdout.flush()

                result = input()
                # logging.debug('Result : {}'.format(result))
                return

        self.solve()


# logging.debug("Start")
t, f = map(int, input().split())

for _ in range(t):
    Solution().solve()
