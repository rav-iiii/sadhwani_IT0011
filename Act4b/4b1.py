A = {'a', 'g', 'c', 'd', 'f', 'b'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'h', 'k', 'd', 'f', 'j', 'i'}

print(f"a. Number of elements in A: {len(A)}, Number of elements in B: {len(B)}")
print(f"b. Elements in B not in A or C: {len(B - A - C)}")  
print(f"\nc. Show the following using set operations:")
print(f"i. [h, i, j, k]: {(C - A - B) | {'h'}}")
print(f"ii. [c, d, f]: {A & C}")
print(f"iii. [b, c, h]: {(B & C) | {'b'}}")
print(f"iv. [d, f]: {(A & C) - {'c'}}")
print(f"v. [c]: {A & B & C}")
print(f"vi. [l, m, o]: {B - A - C}")