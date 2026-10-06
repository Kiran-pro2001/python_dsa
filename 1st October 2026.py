
# Step - - - >
# question (self input/ output/ wording/ get depeer into it)
# input
# output 
# test cases & contraints  (think about the edge cases)
# process - near to ouput (concepts)  - - - build the logic in roughwork - - take 1 demo case (input, output), then type it. 
# when you get the output, think about optimization

# (default)
# in between, use chatgpt/google/yt - - to understand the underline concept (make notes)




my_list = [30,20,10,40,50]

# first maximium 


# method -1 : using sort method 

my_list.sort()  # ascending order - - [10,20,30,40,50]
print(my_list[-2])  # 40 

# time complexity - -  n log n



# method - 2 : max, remove, max 

first_max = max(my_list) # 50 - - O(n)
my_list.remove(first_max) # [30,20,10,40] - - O(n)
second_max = max(my_list) # 40 - - O(n)
print(second_max)


# O(n)


# method - 3: Pass by method - - one time loop, two variable 


my_list = [30,20,10,40,50]
first_max = float('-inf')
second_max = float('-inf')

for element in my_list:
  if element > first_max:
    second_max = first_max
    first_max = element 
  elif element < first_max and element > second_max:     # remove this condition -  element < first_max
    second_max = element 

print("Second Max:",second_max)

# time complexity - ?
# 0(n)











my_list = [5,10,15,20,18]  # second largest 
first_max = float('-inf')  
second_max = float('-inf')

for element in my_list: # element = 5, 10, 15, 20
  if element > first_max: # first_max = 5, 10,15   20 > 15
    second_max = first_max # second_max = 5,10, 15
    first_max = element   # first_max = 10, 15, 20
    
  elif element < first_max and element > second_max: 
    second_max = element 

print(second_max)
    



# 10 to 2 - Placement? (Group Discussion)





# input 
# output 
# test cases 


  # first_max = 5 
  # second_max = -infinity







# HW - - Function, Recursion (10 minutes - - read, what, syntax), class & object -- what, syntax
# doubt - 



# list of string 



nums = ["kiran", "amulya"]

k = integer value 

# no leading zeroes -- before it, no zeros 
# eg - 007 - - no 
# 7 is yes 

nums = ["1", "2", "5", "10"]

# output  - - return - - kth largest integer - - index ka element ko return karo 

# duplicate ko bhi count karna hai 

















nums = ["3","6","7","10"]
nums = ["k", "a", "b"]
k = 4

# output - "3"

nums.sort()  ["10","3","6","7"]
                    



# It will simply give the lexicographic/string order
# 
# 




# factorial 
'''

5! 
5 * 4 * 3 * 2 * 1 = 120

'''



num =int(input("Enter a number : ")) # 5 
# proces - 5 * 4 * 3 * 2 * 1
fact = 1
for value in range(1,num+1): # 1 2 3 4 5
  fact = fact * value 
print(fact) 




# palindrome - - array, string - - don't use function 



# Palindrome for string 

str1 = "madam"
str2 = "madam"

# using slicing 


# without slicing 
# two pointers  
str1 = "mad1am"
#     !
# m a d a m 
#     !
n = len(str1) # 5
left = 0
right = n-1 # 4

while left < right: 
  if str1[left] != str1[right]:
    print("Not Palindrome")
    break
  left = left + 1
  right = right -1 
else:
  print("Palindrome")





for num in range(5,1,-1):
  print(num)


# concept of range 


# range() - function in python -- use to give range of values  

range(start, end, step)


case - 1
range(5)

start = 0 (by default value)
end = 5 (excluded)
step = 1  (go forward by 1 step )

0 to 5 => take 1 step at a time 
0 
1 
2 
3 
4 


print(range(5)) # range(0,5)

for num in range(5):
  print(num)

output - 
0 
1
2
3
4


case - 2
range(1,5)

start = 1
end = 5 (excluded)
step = 1 (by default value)

1 to 4 => by 1 step at  a time 

output -
1 
2
3
4

for num in range(1,5):
  print(num)




case - 3:
range(5,1,-1)

start = 5
end = 1 (excluded)
step = -1 (from backward go one step a time) - reveerse gear 

5 to 1 (excluded) - 1 step go backward direction

for num in range(5,1,-1):
  print(num)


5
4
3
2




# reverse a string 


# method - 1 - string slicing

str = "kiranamulya"
str2 = str[0, len(str)-1]
print(str2)



#indexing in string 
str1 = "kiran"
      #  01234
print(str1[4], type(str[4]))  # 4  str()


# multiple characters 
# slicing 

str1 = "kiranaffanamulya"
# string slicing 

# str1[start_index: end_index: step_value]

# start_index = 0 (default value) -- from the very start 
# end_index = till end of the string (till length) = excluded
# step_value = 1 (go step by step in forward direction)

print(str1[5: :])
print(str1[5:10:1])

print(str1[::]) # complete string 
print(str1[::-1]) # reverse string 
print(str1[1:5]) # from 1st index to 4th index, and move forward by 1 step



## need to focus on this behaviour 
str1 = "kirankumar"
print(str1[:5:-1]) # go backward - - from start to 4th value 
# ramu 



"""

Reverse a String
- Input: "hello"
- Output: "olleh"
- Focus: strings, loops

"""



str1 = "kiran"  # reverse - start = end. and end = start 
output -narik



# string slicing 
str1[::-1]  # go backward, from start to end 

# Method -1 : Using slicing (with function)

str1 = "kiran"
reverse = str1[::-1]
print(reverse)


# TC - 0(n)
# SC - 0(n)



# Method - 2: Using Loops + range function  (without function)

# str1 = "kirankumar"
#         012345678910

# # 9876543210

# for index in range(0, len(str1)-1, -1)  # 0 to 


for num in range(5):
  print(num)

# 0 1 2 3 4 
start = 0 (default value)
end = 5 
step value = 1 (default value)



for num in range(1,5):
  print(num)

# 1 2 3 4 
start = 1
end = 5 excluded 
step = 1 


for num in range(5,1,-1):
  print(num)

# 5 4 3 2 
start = 5 
end = 1 excluded 
step = -1 (one step backward)

#         12345
# str1 = "kiran"
# 54321 

for num in range(5,0,-1):
  print(num)



str1 = "kiran"
str2 = ""
for index in range(len(str1)-1,-1,-1):  #  4 3 2 1 0    -1
  str2 = str2 + str1[index]  # append    # "narik"
print(str2)




str1[::-1]


str1 = "kiran"
new= ""
for index in range(len(str1)-1, -1, -1):
  new = new + str1[index]

print(new)



"""

Check Palindrome
- Input: "madam"
- Output: true
- Focus: two pointers / string manipulation

"""


# slicing  - with method 

str1 = "madam"
reverse = str1[::-1]
if str1 == reverse:
  print("palindrome")
# tc - O(n)
# sc - O(n)

# for loop +  range  - without method 
str1 = "madam"
str2 = ""
for index in range(len(str1)-1, -1, -1):
  str2 = str2 + str1[index]
if str1 == str2:
  print("palindrome")

# tc - O(n)
# sc - O(n)


# two pointer  - more optimal approach 
str1 = "madam"

left = 0
right = len(str1)-1

while left < right:
  if str1[left] != str1[right]:
    print("Not a Palindrome")
    break
  left = left + 1
  right = right - 1
print("Palindrome")

# tc - 0(n)
# sc - O(1)




"""

Find the Second Largest Element
- Input: [10, 5, 20, 8, 20]
- Output: 10
- Focus: arrays, tracking maximums

"""


# method 1 : bruteforce 
arr1 = [1,2,3,4,5]
max_num = max(arr1) #5
arr1.remove(max_num)
print(max(arr1))

# tc - o(n)
# sc - o(n)


# method 2 : 
arr1 = [1,2,3,4,5]

# assume 
first_max = 