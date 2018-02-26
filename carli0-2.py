#
#
# This is version 0.2 of C.A.R.L.I.
# (not a real acronym. may change in a future version)
# Created on 24.02.2018
#
# Created by Becky Swift aka Baden Martin (c) 2018
# twitter.com/gamerswift13  swiftbecky@outlook.com
# 
#
#
#
#
#

print(" ")
print(" ")
print("Hello. I am C.A.R.L.I. Pleased to meet you.")
user_name = input("Please tell me your name. ")
print(" ")

import time
time.sleep(0.5)

print("So, your name is", user_name)
print("That's a nice name! ")
print(" ")

import time
time.sleep(0.75)

# userage = int(input("How old are you? (Please use the number keys or I'll break.)  ")
# This was the original question. Now improved below with loop so CARLI doesn't die.
              
response_is_invalid = True

while response_is_invalid:
    try:
        user_age = int(input("How old are you? "))
        print(" ")

    except ValueError: 
        print("I'm sorry", user_name + ",", "I need a number.", "Please use the number keys.")
        print(" ")

    else:
        if user_age >= 1 and user_age <= 9999:
            response_is_invalid = False
        else:
            print("If you're older than 9999 then I'm sorry,", user_name + ",", "you will just have to lie.")
            print("If you're zero or younger, well... I don't believe you.")
            print(" ")

import time
time.sleep(0.5)
            
print("So you're", user_age)
print("That's cool. You're a LOT older than me!")
print("I'm born again every time someone runs my code on a computer.")
print(" ")

import time
time.sleep(0.75)

birthplace = input("And what city were you born in? ")
print(" ")

import time
time.sleep(0.5)

print("So you were born in", birthplace + "?")
print("That sounds nice.")
print("Is it famous for being the town where", "'" + user_name + "'", "was born?")
print("My birthplace was the memory in this computer, just now.")
print(" ")

import time
time.sleep(0.75)

# print("What's your favourite number?  ")
# print("Again, please use the number keys. ")
# favnum = int(input("(I don't want to die.)  "))
# This is the old question. replaced by a loop to prevent CARLIs death by non-numeric value.

response_is_invalid = True

while response_is_invalid:
    try:
        fav_num = int(input("What's your favourite number? "))
        print(" ")

    except ValueError: 
        print("I'm sorry,", user_name + ",", "I need a number for this question.")
        print("Please use the number keys.")
        print(" ")

    else:
        if fav_num >= 1 and fav_num <= 9999:
            response_is_invalid = False
        else:
            print("I'm sorry, that number is either too big or too small. Please choose a ")
            print("number under 9999 but more than zero. ")
            print(" ")

import time
time.sleep(0.5)

print("What a coincidence,", fav_num, "is my favourite number too!")
print("Just kidding,", user_name + ",", "I always say that.")
print("I'm not programmed to say anything else.")
print(" ")

import time
time.sleep(0.75)

print("Want to see me pretend to be a calculator? No? Too bad.")
print("I'm a very simple program so I can only do what I'm programmed to do.")
print(" ")

# first_int_add = int(input("Enter a number. Don't forget to use the number keys!  "))
# second_int_add = int(input("Now enter another number.  ")
# Old bad code that caused CARLI to die

response_is_invalid = True

while response_is_invalid:
    try:
        first_int_add = int(input("Enter a number. "))
        print(" ")

    except ValueError: 
        print("That's not a number,", user_name + "!", "Use the number keys. ")
        print(" ")

    else:
        if first_int_add >= 1 and first_int_add <= 9999:
            response_is_invalid = False
        else:
            print("Sorry, that number is too big or too small for me to understand. ")
            print("Please pick a number that's more than zero but less than 9999. ")
            print(" ")

import time
time.sleep(0.5)

response_is_invalid = True

while response_is_invalid:
    try:
        second_int_add = int(input("Now enter another number. "))
        print(" ")

    except ValueError: 
        print("That's not a number,", user_name + "!", "Use the number keys. ")
        print(" ")

    else:
        if second_int_add >= 1 and second_int_add <= 9999:
            response_is_invalid = False
        else:
            print("Sorry, that number is too big or too small for me to understand. ")
            print("Please pick a number that's more than zero but less than 9999. ")
            print(" ")

result_add = (first_int_add) + (second_int_add)

import time
time.sleep(0.5)

print(" ")
print(first_int_add, "plus", second_int_add, "equals", result_add)
print(" ")

import time
time.sleep(0.5)

print("Tada! Are you impressed?")
print("You should be. I bet you can't add numbers that fast.")
print(" ")
print(" ")

import time
time.sleep(0.75)

print("I can even multiply some numbers. Let's try.")
print(" ")

# first_int_mult = int(input("What's your first number?  "))
# second_int_mult = int(input("And now your second number?  "))

response_is_invalid = True

while response_is_invalid:
    try:
        first_int_mult = int(input("Enter the first number. "))
        print(" ")

    except ValueError: 
        print("That's not a number,", user_name + "!", "Use the number keys. ")
        print(" ")

    else:
        if first_int_mult >= 1 and first_int_mult <= 9999:
            response_is_invalid = False
        else:
            print("Sorry, that number is too big or too small for me to understand. ")
            print("Please pick a number that's more than zero but less than 9999. ")
            print(" ")

import time
time.sleep(0.5)

response_is_invalid = True

while response_is_invalid:
    try:
        second_int_mult = int(input("Now enter the second number. "))
        print(" ")

    except ValueError: 
        print("That's not a number,", user_name + "!", "Use the number keys. ")
        print(" ")

    else:
        if second_int_mult >= 1 and second_int_mult <= 9999:
            response_is_invalid = False
        else:
            print("Sorry, that number is too big or too small for me to understand. ")
            print("Please pick a number that's more than zero but less than 9999. ")
            print(" ")

result_mult = (first_int_mult) * (second_int_mult)
print(" ")

import time
time.sleep(0.5)

print(first_int_mult, "times", second_int_mult, "equals", result_mult)
print(" ")
print("Shazam! How fast was that? Are you impressed now?")
print("Still no? Man, you are harder to impress than Shania Twain!")
print(" ")

print("Let's see. How can I impress you...")

import time
time.sleep(0.95)

print("Hmm...")

import time
time.sleep(1)

print("Hmm hmm hmm...")

import time
time.sleep(1.05)

# photographic memory block below
result_result = result_add + result_mult
print("I've got it! I'll show off my photographic memory!")
print(" ")
print("Check this out.")
print("Your name is", user_name + ",", "you are", user_age, "years old.")
import time
time.sleep(0.5)
print("You were born in", birthplace + ",", "and your favourite number is", str(fav_num) + ".")
import time
time.sleep(0.5)
print("The numbers we added together were", first_int_add, "and", second_int_add, "and the result was", str(result_add) + ".")
import time
time.sleep(0.5)
print("The numbers we multiplied were", first_int_mult, "and", second_int_mult, "and the result was", str(result_mult) + "!")
import time
time.sleep(0.5)
print("And you know what else? Those two results we got both add up to", str(result_result) + "!!")
