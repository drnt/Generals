import itertools as it
"""
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
"""
states={0,1,2}
a = set(it.product(states, states))
b = list(it.product(states, states))
print(a)

c = [x for x in b if sum(x)<2]


S = [x for x in range(5) if x ** 2 > .3]


for i in a:
    print(i[0])

# lambda: anonymous function
f = lambda x, y : x + y
f(1,1)


# from the net
b1 = [1,2,3,4,5,9,11,15]
b2 = [4,5,6,7,8]
b3 = [val for val in b1 if val in b2]


c1 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
c2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]
c3 = [[13, 32], [7, 13, 28], [1,6]]
c3 = [filter(lambda x: x in c1, sublist) for sublist in c2]
