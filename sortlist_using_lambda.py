#Write a Python program to sort a list of tuples using Lambda Expression.
marks = [('Analysis of Algo', 94), ('DBMS', 86), ('Operating System', 99), ('Networking', 92)]
print("Initial list of tuples:")
print(marks)
marks.sort(key = lambda x: x[1])
print("\nNow We are Sorting the List of Tuples:")
print(marks)
