#1

# a=[1, 1, 3, 4, 4, 5, 6, 7]
# b=[0, 1, 2, 3, 4, 4, 5, 7, 8]
# c=a+b
# sum_=sum(c)
# len_=len(c)
# avg=sum_/len_
# print(avg)

#2

# a=[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# count=0
# for i in a:
#     if type(i)==int:
#         count+=1
# print(count)

#3
# a=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# c=[]
# for i in a:
#     if len(i)==0:
#         pass
#         # print(i)
#     else:
#         c.append(i)
# print(c)

#4
# txt = "Hello, welcome to my world."
# b=input("Belgini kiriting: ")
# c=[]
# for i in range(len(txt)):
#
#     if txt[i]==b:
#         c.append(i)
# print(c[-1])

#5
# from math import sqrt
# def function(a,b):
#     l=[]
#     if a<b:
#         for i in range(a,b+1):
#             if sqrt(i)==int(sqrt(i)):
#                 l.append(i)
#
#
#         return l
#     else:
#         return "a dan katta qiymat kiriting"
# print(function(15,40))


#6

# with open("test.txt", 'a') as f:
#     f.write("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna")

# with open("test.txt", 'r') as f:
#     read=f.read().split()
#     long_word=max(read, key=len)
#     print(long_word)

#7
# with open("test.txt", 'r') as f:
#     read=f.readlines()
#     l_count=len(read)
#     print(l_count)

#8
# num=input("Enter a number: ")
def is_antiqa(num):
    flip_map = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
    num_str = str(num)
    flipped_str = ''.join(flip_map.get(c, '') for c in reversed(num_str))
    return flipped_str == num_str
n = input("=> ")
print(f"{n} - {'Antiqa son' if is_antiqa(n) else 'Antiqa son emas'}")

