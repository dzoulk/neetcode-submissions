class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for card in hand:
            if card not in count:
                count[card] = 1
            else:
                count[card] +=1

        for x in sorted(count):
            while count[x] > 0:
                for v in range(x, x + groupSize):
                    if count.get(v, 0) == 0:
                        return False
                    count[v] -= 1
        return True