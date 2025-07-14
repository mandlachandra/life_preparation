#1.How to swap 2 numbers Approch1
# num1 = 10
# num2 = 20
# num1 = input("enter the num1 value:")
# num2 = input("enter the num2 value:")
#
# print("value of num1 before swaping:", num1)
# print("value of num2 before swaping:",num2)
#
# #approch1
# # temp = num1
# # num1 = num2
# # num2 = temp
#
# #approch 2
# num1,num2 = num2,num1
# print("value of num1 after swaping:",num1)
# print("value of num2 after swaping:", num2)

#............................
#2.How to check number is prime or not

# num =5
# count = 0
# if num>1:
#     for i in range(1, num+1):
#         if (num%i)==0:
#             count = count+1
#     if count == 2:
#         print("it is prime")
#     else:
#         print("it is not prime")

#3.write a program to find out common letters b/w 2 strings
# def common_letters():
#
#     str1 = input("enter first string:")
#     str2 = input("enter second string:")
#     s1 = set(str1)
#     s2 = set(str2)
#     lst = s1 & s2 # by using & we can extract common letter
#     print(lst)
# common_letters()

#4.Frequency of words in a string
def freq_words():
    str = input("enter the string:")
    li = str.split()
    d = {}

    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i] = d[i]+1
    print(d)

freq_words()

#find missing number in an array

