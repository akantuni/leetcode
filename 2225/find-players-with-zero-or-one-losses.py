class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = [arr[0] for arr in matches]
        losers = [arr[1] for arr in matches]

        losses = {}

        for player in losers:
            lossCount = losses.get(player)
            if lossCount is None:
                losses.update({player: 1})
            else:
                losses.update({player: lossCount + 1})

        lostNone = sorted(list(set(winners) - set(losers)))
        lostOne = sorted([player for player, ls in losses.items() if ls == 1])

        return [lostNone, lostOne]
