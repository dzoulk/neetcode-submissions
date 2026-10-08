import heapq
class Twitter:

    def __init__(self):
        self.count = 0
        self.mapping = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.mapping[userId].append([self.count, tweetId])
        self.count -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            if followeeId in self.mapping:
                index = len(self.mapping[followeeId]) -1
                count, tweetId = self.mapping[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.mapping[followeeId][index]   
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)