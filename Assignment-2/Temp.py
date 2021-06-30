# def is_palindrome(x,y):
#     # add your code here
    # print(x)
    
def count_char(x):
    count = 0
    dict1 = {}
    for i in x:
        if i in dict1:
            count = dict1[i]
            count = count + 1
            dict1[i] = count
        else:
            dict1[i] = 1
    return dict1

print(count_char("anagram"))



    
    # print(tempArr)


# print(is_palindrome(121))