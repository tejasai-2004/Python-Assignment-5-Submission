#Task 9 " Creates a dictionary where student names are keys and their marks are values"

dictionary={'Sai':'85','Teja':'75','Sriman':'65','Praveen':'95'}
a=(input("Enter the Student's Name:"))
if a in dictionary:
    print(f"{a}'s Marks: {dictionary[a]}")
else:
    print("Student not found")