# A = open('log.txt').read().split()
keys = list("@234567890]^1,.-;lrdyp[aoeiugntskf:xcvwqjhmbz/")
keyId = {}
for i in range(len(keys)):
    keyId[keys[i]] = i
hinndo = [0]*49
# for a in A:
#     try:
#         hinndo[keyId[a]] += 1
#     except:
#         pass

data = {"<Return>": 809,
"a": 805,
"<Backspace>": 730,
"i": 609,
"o": 604,
"n": 565,
"<Space>": 547,
"t": 506,
"u": 476,
"e": 428,
"k": 383,
"<ShiftLeft>": 368,
"<F>": 323,
"<H>": 321,
"r": 316,
"s": 306}
for a in data:
    try:
        hinndo[keyId[a]] = data[a]
    except:
        pass

use = set()
rank = []
for k in keys:
    use.add(k)
for i in range(49):
    Max = 0
    key = ""
    for a in use:
        if Max <= hinndo[keyId[a]]:
            key = a
    use.discard(key)
    rank.append(key)
keyboard = [
    [[],[],4],
    [[],[],4],
    [[],[],4],
    [[],[],8],
    [[],[],8],
    [[],[],4],
    [[],[],4],
    [[],[],12]
    ]
count = 0
for a in rank:
    m = 10**100
    index = -1
    for i in range(8):
        if sum(keyboard[i][0]) < m and len(keyboard[i][0])<keyboard[i][2]:
            index = i
            m = sum(keyboard[i][0])
    try:
        keyboard[index][0].append(hinndo[keyId[a]])
        keyboard[index][1].append(a)
    except:
        pass
for k in keyboard:
    print(k[1])
