# Title: 99 bottles
# Author: Twazanga Mugala
# Purpose: Create a program that prints out every line to the song "99 bottles of beer on the wall."

# Requirements: Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
#   Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
#   Remember, when you reach 1 bottle left, the word "bottles" becomes singular.


bottles = 99


def count_down(n):
    num = n
    while type(num) == int:
        verse1 = "of beer on the wall"
        verse2 = "of beer, take one down, pass it around"
        verse3 = "bottles of beer on the wall"
        obj = "bottles"
        one_less = str(num-1)
        if num == 2:
            verse3 = "more bottle of beer on the wall"
        elif num == 1:
            obj = "bottle"
            one_less = "no more"
        elif num == 0:
            num = "No more"
            obj = "bottles"
            one_less = str(99)
            verse2 = "bottles of beer, go to the store and buy some more,"

        if n <= 99 or n >0:
            print(num, obj, verse1, num, obj, verse2, one_less, verse3)
        else:
            print("Error: Something went wrong with the beer!")
        if type(num) == int:
            num -= 1


count_down(bottles)
