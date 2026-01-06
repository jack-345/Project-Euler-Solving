# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. 
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

# solving function for below 10
# def multiples_of_3_or_5():
#     # count below 10 so decrement to 9
#     n = 10
#     n -= 1
#     sum = 0
#     elements = 0
#     if (n >= 3):
#         elements = n//3
#         sum += (elements * (3 + elements*3))//2
#     if (n >= 5):
#         elements = n//5
#         sum += (elements * (5 + elements*5))//2
#     print(sum)

# solving function for below 1000
def multiples_of_3_or_5():
    n = 1000
    n -= 1
    sum = 0
    elements = 0
    if (n >= 3):
        elements = n//3
        sum += (elements * (3 + elements*3))//2
    if (n >= 5):
        elements = n//5
        sum += (elements * (5 + elements*5))//2
    if (n >= 15):
        elements = n//15
        sum -= (elements * (15 + elements*15))//2
    print(sum)

multiples_of_3_or_5()