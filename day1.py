# # #py = '''What is Python It is a high level language which is trending in this 
# # #i dont know what is python brother!!!'''
# # #sl = py[0:15]
# # #y = py[0:20]
# # #print(sl + y)

# # # Add 2 roll no's
# # # roll1 = 12
# # # roll2 = 25

# # # print(roll2)
# # # print(type(roll1))

# # # roll1_str = str(roll1)
# # # roll2_str = str(roll2)
# # # print(roll2)
# # # print(type(roll2))

# # # name = input("What is Your Name: ")
# # # print(name)

# # # marks1 = input("What is your marks 1? ")
# # # marks2 = input("What is your marks 2?")

# # # if marks1 > marks2:
# # #     print("Marks1 is greater: ")
# # # else:
# # #     print("marks2 is greater")


# # # idk = [1,2,3,"i dont know"]
# # # idk.append(222)
# # # print(idk)
# # # idk.pop(2)
# # # print(idk)
# # # idk.remove(2)
# # # print(idk[::2])


# # idk_2 = [1,2,4,3,5,1,4,6]
# # # idk_2.append(2)
# # # idk_2.remove(2)
# # # del idk_2[1]
# # # idk_2.sort(reverse=True)
# # # idk_2.count(1)
# # # print(idk_2)

# # Myself =  {"Name": 'dhara', "Rollno": 25 , "age": 18}
# # print(Myself["age"])
 
# # def greet(name):
# #     print("What is your name?: ")

# # greet("dhara")

# def switch_case(value):
#     if value == 'a':
#         return "Option A"
    
#     elif value == 'b':
#         return "Option B"
    
#     elif value == 'c':
#         return "Option C"
    
#     else:
#         return "Invalid option"
    
# print(switch_case('b'))

# import random

# secret_number = random.randint(1, 100)
# max_attempts = 5

# while max_attempts > 0:
#     try:
#         guess = int(input(f"Attempts left ({max_attempts}): Enter your guess: "))
#         if guess == secret_number:
#             print("Congratulations! You guessed it right!")
#             break
#         elif guess < secret_number:
#             print("Too low!")
#         else:
#             print("Too high!")
#         max_attempts -= 1
#     except ValueError:
#         print("Invalid input. Please enter a number.")