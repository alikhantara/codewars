#this is for fun =)

from art import *                         #comment this for using in codewars

def count_bits(n: int):
    pr_name=text2art("super bit counter") #comment this for using in codewars
    print(pr_name)                        #comment this for using in codewars
    if type(n) != int:
        print("!!! Only Integers as Input !!!")
    formatted = ("{0:b}".format(n))
    bitcount = formatted.count("1")
    print("Your Value is:", bitcount)
    return(bitcount)

count_bits('qweqwe')
