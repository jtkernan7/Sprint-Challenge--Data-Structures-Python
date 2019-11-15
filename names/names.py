import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


#runtime was O(n^2)
#checked each value of list 1 against list 2 then checked each value of list 2 against 1
#bad approx 10.1 seconds
'''
duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''


#new runtime O(n) i think. maybe less
#approx 0.004 seconds
#best by far

#duplicates = frozenset(names_1).intersection(names_2)


#same runtime no intersection code

#this is most intuitive make list of one, run through list 1 get values, check all values as running through list 2
#approx 1.6 seconds

duplicates = []
for name_1 in names_1:
    if name_1 in names_2:
        duplicates.append(name_1)



print(f"{len(duplicates)} duplicates:\n\n{duplicates}")
end_time = time.time()
#print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

