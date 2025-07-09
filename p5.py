import random
import statistics
random_num=[random.randint(1,10) for j in range(25)]
print("Mean:")
print(statistics.mean(random_num))
print("\n")
print("Median:")
print(statistics.median(random_num))
print("\n")
print("Mode:")
print(statistics.mode(random_num))
print("\n")
