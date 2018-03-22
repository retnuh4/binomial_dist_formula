from math import *


class bi_dist:

    def fact_form(self):
        n_fact = int(input("Enter the 'n' value: "))
        x_fact = int(input("Enter the 'x' value: "))

        self.com = (factorial(n_fact))/(factorial(x_fact)*(factorial(n_fact - x_fact)))
        print("Answer for n!/(x!(n-x)!) is : ")
        print(self.com)
        print("")

    def p_form(self):
        p = float(input("Enter the 'p' value: "))
        x = int(input("Enter the 'x' value: "))
        n = int(input("Enter the 'n' value: "))
        CONST = 1

        self.val = (p**x) * (CONST - p)**(n-x)
        print("Answer for P^x(1-P)^(n-x) is: ")
        print(self.val)
        print("")

    def final_form(self):
        ans = self.com * self.val
        print("Final answer: ")
        print(ans)
        print("")


a = bi_dist()
print(a.fact_form())
print(a.p_form())
print(a.final_form())
