import math
import re


def count_vowels(s):
    vowels = 'aeiou'
    count = 0
    for letter in s.lower():
        if letter in vowels:
            count += 1
    return count


def generate_array(length, start):
    arr = []
    for i in range(length):
        arr.append(start)
        start += 1
    return arr


def sort_array():
    arr = []

    for i in range(5):
        arr[i] = int(input("Enter element {}: ".format(i + 1)))

    arr_desc = sorted(arr, reverse=True)
    arr_asc = sorted(arr)

    print("Original array: ", arr)
    print("Array in descending order: ", arr_desc)
    print("Array in ascending order: ", arr_asc)


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


def reverse_string(s):
    return s[::-1]


def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    print(f"The area of the circle is {area:.2f}")
    print(f"The circumference of the circle is {circumference:.2f}")


def user_confirm():
    while True:
        name = input("Enter your name: ")
        if name.strip() != '':
            break
        print("Name cannot be empty.")

    while True:
        email = input("Enter your email: ")
        if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            break
        print("Invalid email address.")

    print(f"Name: {name}")
    print(f"Email: {email}")


def iti_count(text):
    count = text.lower().count("iti")
    print(f"The string 'iti' appears {count} times in the input string.")


def longest_substring_alphabetical_order(string):
    current = string[0]
    longest = string[0]
    for char in string[1:]:
        if char >= current[-1]:
            current += char
            if len(current) > len(longest):
                longest = current
        else:
            current = char
    print(f"Longest substring in alphabetical order is: {longest}")


if __name__ == '__main__':
    print(count_vowels("ahmedelshaar"))
    print(generate_array(5, 10))
    sort_array()
    fizzbuzz(15)
    reverse_string("ahmedelshaar")
    circle(5.5)
    user_confirm()
    iti_count("ITI Mans OS. it is very easy")
    longest_substring_alphabetical_order("abdulrahman")
