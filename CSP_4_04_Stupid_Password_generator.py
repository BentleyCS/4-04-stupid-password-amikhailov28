"""
Problem: Stupid Password Generator
Write a program that enters two integers n and l and generates, in alphabetical order, all possible "stupid passwords" that consist of the following 5 characters:

Character 1: a digit from 1 to n.
Character 2: a digit from 1 to n.
Character 3: a small letter from the first l letters of the Latin alphabet.
Character 4: a small letter from the first l letters of the Latin alphabet.
Character 5: a digit from 1 to n, greater than the first 2 digits.
Input Data
The input is read as arguments and consists of two integers: n and l within the range [1 … 9].Screenshot 2025-10-07 at 10.53.33 AM.png

Output Data
Return a list of all "stupid" passwords in alphabetical order.
"""

def stupidPassword(n: int, l: int):
    passwordList = []
    x = 2
    for i in range (1, n):
        c1 = i
        for i in range (1, n):
            c2 = i
            for i in range(97, 97+l):
                c3 = chr(i)
                for i in range(97, 97+l):
                    c4 = chr(i)
                    while x <= c1 or x <= c2:
                        x += 1
                    for i in range (x, n+1):
                        c5 = i
                        password = f"{c1}{c2}{c3}{c4}{c5}"
                        passwordList.append(password)
    return passwordList

print(stupidPassword(2, 4))
