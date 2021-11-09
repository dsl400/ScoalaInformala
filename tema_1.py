
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
list_copy = my_list.copy()
list_copy.sort()
print(my_list,'<<<< lista initala')
print(list_copy,'<<<< copie sortata ascendent')

print()
list_copy.reverse()
print(my_list,'<<<< lista initala')
print(list_copy,'<<<< copie sortata descendent')

print()
list_copy.reverse()
print(list_copy[1::2],'<<< numere pare')

print()
print(list_copy[0::2],'<<< numere impare')

print()
print(list_copy[2::3],'<<< numere ce se impart la 3')