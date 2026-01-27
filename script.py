# sample_list = [1, "another", "list", "a", [3,4]]
# print(sample_list[0]) # 1
# print(sample_list[1]) # "another",
# print(sample_list[-1]) # [3,4]]
# print(sample_list[1:4])# ["another", "list", "a"]
# print(sample_list[:4])# [1, "another", "list", "a"]
# print(sample_list[3:])# ["a",[3,4]]]

# sample_dict = {"Key1": "Value1", 2: 3, "Age": 23}
# print(sample_dict["Age"]) # 23
# print(sample_dict[2]) # 3

# sample_tuple = (1,"2","brij")
# print(sample_tuple [0]) # 1

# sample_set = {5,9}
# sample_set.add(4)
# print(sample_set) # {5,9,4}
# sample_set.remove(9)
# print(sample_set) # {5, 4}

# num = 0
# # Try below two as well:
# # num = 7
# # num = 6
# if num == 0:
#     print("This is a Zero")
# elif num%3 == 0:
#     print("Number is divisible by 3")
# else:
#     print("Number is not divisible by 3")

# # Program to return a list of even number from a given list
# # Given list
# numbers = [7,4,3,5,8,9,8,6,14]
# # Declare an empty list
# even_numbers = []# iterate over the list
# for num in numbers:
# #Add the even numbers to even_numbers list
#     if num%2 == 0:
#         even_numbers.append(num)

# print("The Even number list is ",even_numbers)

# count = 0
# while (count < 11):
#     print ('The current number is :', count)
#     count = count + 1
 
# print('While loop terminates here.')

# def div_of_numbers(num1, num2):
#     """This function returns the division of num1 by num2"""
#     if num2 == 0:
#         return "num 2 is zero"
#     else:
#         return num1/num2

# print(div_of_numbers(6,3))

# parent class
# class DataPipelineBook:
#     def __init__(self):
#         print("This book is very hot in market")
#         self.pages =300
#     def what_is_this(self):
#         print("Book")
#     def pages(self):
#         return self.pages
    
# # child class
# class PythonDataPipelineBook(DataPipelineBook):
#     def __init__(self):
#         # call super() function
#         super().__init__()
#         print("Create Data Pipeline with Python")
#     def what_technology_is_used(self):
#         return "Python"

# pipeline = PythonDataPipelineBook()
# pipeline.what_is_this()
# pipeline.what_technology_is_used()

# with open("video.txt", "a") as f:
#     f.write("\nI'm doing so good!")

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     'A': [1, 2, np.nan, 4],
#     'B': [5, np.nan, np.nan, 8],
#     'C': [9, 10, 11, 12],
#     'D': [40, 10, np.nan, np.nan]
# })

# df.fillna(df.mean(), inplace=True)
# print(df)

# # Suppose 'A' is the column we want to normalize (make the values lie between 0 & 1)
# df['A'] = (df['A'] - df['A'].min()) / (df['A'].max() - df['A'].min())
# print(df)
# df['D'] = (df['D'] - df['D'].min()) / (df['D'].max() - df['D'].min())
# print(df)

