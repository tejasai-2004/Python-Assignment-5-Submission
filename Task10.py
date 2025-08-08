#Demostrate list slicing

a= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:",a)
sliced_list = a[0:5]
print("Extracted first five elements:", a[0:5])  
reversed_list = sliced_list[::-1]
print("Reversed List:", reversed_list)
