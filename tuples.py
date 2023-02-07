t1 = 10,2,3
t2 = 4,5

print(t1==t2)
print(t1<t2)
t4=('3',)*3

a,b,c = t4

print(t4)
print(a,b,c)

print(t1.index(3))

for x,y in zip(t1, t2):
    print(x,y)

# print(list(zip(t1,t2)))
# print(help(zip))


today_responses = [200, 300, 404, 500]
match today_responses:
     case [a]:
             print(f"One response today: {a}")
     case [a, b]:
             print(f"Two responses today: {a} and {b}")
     case [a, b, *rest]:
             print(f"All responses: {a}, {b}, {rest}")

import sys

while True:
     feedback = input('Type exit to exit: ')
     if feedback == 'exit':
         print(f'You typed {feedback}.')
         sys.exit()



