# Python-Assignment-5-Submission

Task 9: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

Code:
#Task 9 " Creates a dictionary where student names are keys and their marks are values"

dictionary={'Sai':'85','Teja':'75','Sriman':'65','Praveen':'95'}
a=(input("Enter the Student's Name:"))
if a in dictionary:
    print(f"{a}'s Marks: {dictionary[a]}")
else:
    print("Student not found")

Excepted Output:

Enter the Student's Name:Sai
Sai's Marks: 85

#Task10 Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

Source Code:

#Demostrate list slicing

a= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:",a)
sliced_list = a[0:5]
print("Extracted first five elements:", a[0:5])  
reversed_list = sliced_list[::-1]
print("Reversed Extracted elements:", reversed_list)

Excpected Output:
Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed Extracted elements: [5, 4, 3, 2, 1]
