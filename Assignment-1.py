# Question 1: Print
#   1.Define a string variable, and print it.

string_variable = "Hello Python";
print(string_variable);

#   2.Define a string (I’m a student), print it

string_variable_1 = "I’m a student";
print(string_variable_1);

#   3. Defind a string: (4pts) (How do you think of this course?
#                                Describe your feeling of this course)
#   print it in multiple line.

string_variable_2 = "How do you think of this course? \nDescribe your feeling of this course";
print(string_variable_2);

# Question 2: Operator
# Define a = 100, b = 9, calculate following problems
# declared the variable a and b
a = 100
b = 9

#   1. c = a + b, print c out.

c = a + b;
print(c); 

#   2. print the quotient of a/b.

print(a/b)

#   3.print the integer part of a/b.

print(a//b)

#   4.print the remainder part of a/b.

print(a%b)

#   5.print the result of ’a’ to the power of b.

print(a**b)

#   6.Using logic operator to return a Boolean value for a unequal to b.

print(a!=b)

#   7.Using logic operator to return a Boolean value for a greater than b.

print(a>b)


# Question 3: List Practice
#   1.Define a list Name it List_A), whose items should include integer, float, and
# string. Please notice the length of the list should be greater than 5.
List_A = [1,2,3,1.1,2.2,"integer"]
print(len(List_A))

#   2.Using extend and append to add another list(Name it List_B) to List_A.
List_B = [4,5,3.3,"string"]
List_A.extend(List_B)
print(List_A)
List_A.append(List_B)
print(List_A)

#   3.Insert a string (’FE520’) to the second place of List A, and delete it after that.
List_A.insert(1,'FE520');
print(List_A)
List_A.remove('FE520');
# List_A.pop(1) Even pop can be used because we know the location of the List
print(List_A)

#   4.Return and delete the last element in the List A, and print the new list.
print(List_A.pop())
print(List_A)

#   5.Return a new list (Name is List_C), slicing the List_A from 3rd to the end.
List_C = List_A[2:]
print(List_C)

#   6.Double size your List_C.
List_C.extend(List_C)
print(List_C)

#   7.Reverse your sequence of List C.
List_C.reverse()
print(List_C)


#4 Questions 4: Practice Dictionary

#   1.Define a list A = [1, 2, 3, 2, 1, 7].

A = [1, 2, 3, 2, 1, 7]

#   2.Write a loop to count the number of each unique digit into dictionary, where your
#   keys are digit in the list A, and value is the count corresponding to each digit.
#   Your result should look like :
#   {1: 2, 2: 2, 3: 1, 7: 1}

count_dict = {}

for x in A:
    if(count_dict.get(x) == None):
        count_dict.update({x:1})
    else:
        count = count_dict.get(x);
        count=count+1;
        count_dict.update({x:count})

print(count_dict)
    
#5 Question 5 : Loop Practice: Sum
#   Write a loop for calculate the average of a list.
#   For example: if you have a list A = [1, 2, 3, 4, 5, 6], after your loop calculation,
#   you need to get a total num equals to 3.5.

A = [1, 2, 3, 4, 5, 6]
Sum = 0
for x in A:
    Sum = Sum + x;

print(Sum/len(A))


#6 Question 6: Loop Practice Gradient Decent
#   1.Set initial variable. m=0 and c=0, Learning rate L=0.001, number of iterations

m=0
c=0
L=0.001

#   2.Write a for loop, in this loop, go over all pair (xi, yi):
#       a.calculate ypredi= xi ∗ m + b
#       b.calculate xi(ypredi− yi), and store it in list Dm
#       c.calculate (ypredi− yi), and store it in list Dc
#    3. calculate the average for list Dm and Dc equal to dm and dc
#   4. update m by: m = m − L × dm
#   5. update c by: c = c − L × dc

# Test Data

x = [[0.18], [1.0], [0.92], [0.07], [0.85], [0.99], [0.87]]

y = [[109.85], [155.72], [137.66], [76.17], [139.75], [162.6], [151.77]]


Dm=[]
Dc=[]
for i in range(len(x)):
    ypredi = (x[i][0] *m) + c
    Dm.append(x[i][0]*(ypredi-y[i][0]))
    Dc.append(ypredi-y[i][0])
dm = sum(Dm)/len(Dm)
dc = sum(Dc)/len(Dc)
m = m - L * dm
c = c - L * dc

print(m,c)


#   6(Bonus 5 pts) What you have done above are one iteration of gradient descent,
    # once you repeat from step 2 to 5 again and again, the m and c will be converged
    # to the true value. Can you wrap them in big loop for 200 iteration?
m=0
c=0
L=0.001

x = [[0.18], [1.0], [0.92], [0.07], [0.85], [0.99], [0.87]]

y = [[109.85], [155.72], [137.66], [76.17], [139.75], [162.6], [151.77]]

for a in range(200):
    Dm=[]
    Dc=[]
    for i in range(len(x)):
        ypredi = (x[i][0] *m) + c
        Dm.append(x[i][0]*(ypredi-y[i][0]))
        Dc.append(ypredi-y[i][0])
    dm = sum(Dm)/len(Dm)
    dc = sum(Dc)/len(Dc)
    m = m - L * dm
    c = c - L * dc

print(m,c)