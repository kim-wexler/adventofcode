import sys, re, math

f = open(sys.argv[1]).read().strip()
cards = [re.findall("\\d+", line) for line in f.strip().splitlines()]

ans = 0
card_dupes = [1] * len(cards)
for i, card in enumerate(cards):
    _, *nums = card
    winning_nums, my_nums = nums[:10], nums[10:]
    wins = len(set(my_nums) & set(winning_nums))
    ans += math.floor(2**(wins-1))
    for j in range(i+1, i+wins+1):
        card_dupes[j] += card_dupes[i]

print(ans, sum(card_dupes))
