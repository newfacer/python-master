import random
import numpy as np
def generate_rand(n, sum_v):
    Vector = [random.random() for i in range(n)]
    Vector = [ int(i / sum(Vector) * sum_v) for i in Vector]
    if sum(Vector) < sum_v:
        Vector[0] += sum_v-sum(Vector)
    return Vector

print(generate_rand(10,100))

# Vector =[]
# for i in range(10):
#      Vector.append(random.random())

# Tector = []
# for i in range(10):
#     Tector.append(int(i/sum(Vector)* 10.00))

# if sum(Tector) < 100:
#    Tector[0] += 100-sum(Tector)

# print(Tector)


# list1 = [random.randint(0, 50) for i in range(9)]
# list1.sort()
# list2 = []
# list2.append(list1[0])
# for i in range(8):
#     list2.append(list1[i + 1] - list1[i])
# list2.append(50 - list1[8])
# sum(list2)
