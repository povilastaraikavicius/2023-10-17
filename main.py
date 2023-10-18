# squares = {i: i * i for i in range(10)}
# print(squares)

# squares = [number * number for number in range(10) if number != 5]
# print(squares)

# squares = {i: i * i for i in range(10) if i  % 3 !=0 }
# print(squares)



# values = ["a", "b", "c"]
# index = 0

# for value in values:
#     print(index, value)
#     index += 1

# values = ["a", "b", "c"]
# for count, value in enumerate(values):
#     print(count, value)

# values = ["a", "b", "c"]
# for count, value in enumerate(values, start=1):
#     print(count, value)


# def even_items(numbers: list):
#     return [v for i, v in enumerate(numbers, start=1) if not i % 2]

# seq = list(range(1, 11))

# print(even_items(seq))
# import secrets


# def event_items(number: list):
#     numbers = [] 
#     for i , v in enumerate(numbers, start=1 ):
#       if not i % 2:
#         numbers.append(v)
#     return numbers
    # seq - list(range(10,31))
# print(event_items(secrets))
#         print(numbers)

# Given string: text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
# calculate how many words have letter 'e' in it.

# text = "In this lecture we will review some additional functionalities of python built-in data structures."
# # new_tex = text.split()
# # print ([words for words in new_tex if  "e" in words])
        
# # #  tą patį stringą, kaip ir ankstesniame pratime: apskaičiuokite raidžių, kurios turi daugiau nei 5 simbolius, skaičių.

# word_with_e  = [words for words in text.split() if len(words) > 5]
# print(len(word_with_e))






# # Given the same string calculate the occurrence of each letter in the string. (HINT: store everything in dictionary)

# char_dict = {}
# text = "In this lecture we will review some additional functionalities of python built-in data structures."
# new_tex = text.split()

# for word in new_tex:
#     for char in word:
#         if char.isalpha():
#             if char in char_dict:
#                 char_dict [char] +=1
#             else:
#                 char_dict[char] = 1
            
            
# print(char_dict)
# print(type(new_tex))


# Write a program that checks if given number is a perfect square.


# import math
# num_check = float (input("enter number:"))

# if num_check % math.sqrt(num_check) == 0:
#     print("number is perfect square")
# else:
#     print ("number is not perfect square")

# user_name_list = []
# user_password_list = []

# print("Enter five different username and password")

# for _ in range(5):
#     username = input("Add username: ")
#     password = input("Add password: ")
#     user_name_list.append(f"username='{username}'")
#     user_password_list.append(f"password='{password}'")
# print(user_name_list,user_password_list)
# while True:
#     username_input = input("Enter username: ")
#     password_input = input("Enter password: ")

#     if f"username='{username_input}'" in user_name_list and f"password='{password_input}'" in user_password_list:
#         print("Welcome")
#         break
#     else:
#         print("Wrong password. Please try again.")

user_name_and_pasword = []
print("Enter five different username and password")
name_and_pasword = input("write five username and password in a format 'username1=': 'password1'")
user_name_and_pasword.append(f"user='{name_and_pasword}'")
print(user_name_and_pasword)

while True:
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")
    if f"username='{username_input}'" in user_name_and_pasword and f"password='{password_input}'" in user_name_and_pasword:
        print("Welcome")
        break
    else:
        print("Wrong password. Please try again.")

# login_atempts = 0
# name_and_pasword = input("write five username and password in a format: username1=, password1=; username2=, password2=;")
# name_list = name_and_pasword.split("; ")
# name_and_pasword_dic = {}
# for combination in name_list:
#     splited_combination = combination.split(";")
#     username = splited_combination[0].strip("username=")
#     pasword = splited_combination[1].strip("pasword=")

#     name_and_pasword_dic[username] = pasword
# print(name_and_pasword_dic)
# full_dic = {key.replace('"', ''): val.replace('"', '') for key, val in name_and_pasword_dic.items()}


# while True:
#     user_input = input("enter your name ant pasword: ")
#     user_pasword_list = user_input.split(" ")
#     user_entered =user_pasword_list[0]






# user_name_list = []
# user_password_list = []

# print("Enter five different username and password")

# for _ in range(5):
#     username = input("Add username: ")
#     password = input("Add password: ")
#     user_name_list.append(f"username='{username}'")
#     user_password_list.append(f"password='{password}'")

# while True:
#     username_input = input("Enter username: ")
#     password_input = input("Enter password: ")

#     if f"username='{username_input}'" in user_name_list and f"password='{password_input}'" in user_password_list:
#         print("Welcome")
#         break
#     else:
#         print("Wrong password. Please try again.")