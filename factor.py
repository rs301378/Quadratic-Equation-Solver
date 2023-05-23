#QUADRATIC SOLVER TEST
import math
import sys
import sympy
from sympy import *

a = int(input('Enter a coefficient->'))
b = int(input('Enter b coefficient->'))
c = int(input('Enter c coefficient->'))

if a==0:
    sys.exit('Error wrong equation')

def factor(p):
    if p<0:
        p = -p;
    f=[1]
    while p > 1:
        for i in range(2, p+1):
            if p%i == 0:
                f.append(i)
                p //= i
                break
    return f
    

def sp_chk(s,p,f1,f2):
    if s == (f1+f2) and p == f1*f2:
        return f1,f2
    elif s == (-f1+f2) and p == (-f1)*f2:
        return -f1,f2
    elif s == (-f1-f2) and p == (-f1)*(-f2):
        return -f1,-f2
    elif s == (f1-f2) and p == f1*(-f2):
        return f1,-f2
    else:
        return 0,0

def middle_term(a,b,c,r1,r2):
    sum_q = b
    prod_q = a*c
    fs = factor(prod_q)
    print(" ")
    print("Quadratic Equation is: {}x^2 + {}x + {} = 0".format(a, b, c))
    print(" ")

    fs_len = len(fs)
    for i in range(fs_len):
        f1 = fs[i]
        j =0 
        while(j<len(fs)):
            if i!=j:
                f1 = fs[j]*f1
            j = j+1
            f2 = prod_q/f1
            m1,m2 = sp_chk(sum_q,prod_q,f1,f2)
            if m1!=0 and m2!=0:
                print('Step 1: ')
                v = symbols(str(a)+'x^2')
                s = symbols(str(a)+'x')
                v1 = symbols(str(m1)+'x')
                v2 = symbols(str(m2)+'x')
                v3 = symbols(str(c))
                x = symbols("x")
                y = symbols("1")
                eq1 = Eq(v + v1 + v2 + v3, 0)
                pprint(eq1)
                print("(Split the middle term)")
                
                print(' ')
                print('Step 2: ')
                eq2 = Eq(s*(x + 1) + v3*(x + 1), 0)
                pprint(eq2)

                print(' ')
                print('Step 3: ')
                eq3 = Eq((x + 1) * (s + v3), 0)
                pprint(eq3)
                print(' ')
                print("We can now equate each factor to zero and obtain")
                print(' ')
                eq4 = Eq((x + 1),0) 
                eq5 = Eq((s + v3), 0)
                pprint(eq4)
                print('Or')
                pprint(eq5)

                print(' ')
                # eq6 = Eq((x), -(y)) 
                # eq7 = Eq((x), 0)
                # solution_1 = y
                # solution_2 = Rational(-(v3), a)
                # print(f"x = {solution_1}")
                # print(f"x = {solution_2}")
                # pprint(eq6)
                # print('Or')
                # pprint(eq7)
                return
    print('Middle term NOT possible')
    x = sympy.symbols('x')
    discr = b**2 - 4*a*c

    print("Quadratic Equation is: {}x^2 + {}x + {} = 0".format(a, b, c))
    print("Step 1: To calculate the discriminant")
    print("   Discriminant = b^2 - 4ac = {}^2 - 4*{}*{} = {}".format(b, a, c, discr))

    if discr < 0:
        print("   There are no real solutions!")
        return []
    elif discr == 0:
        x_solution = -b / (2*a)
        print("   There is one real solution!: x =", x_solution)
        return [x_solution]
    else:
        print("   Step 2: Calculate the two solutions using the quadratic formula: ")
        print("   x1 = (-b + sqrt(disc)) / (2a)")
        print("   x2 = (-b - sqrt(disc)) / (2a)")
        x1 = (-b + sympy.sqrt(discr)) / (2*a)
        x2 = (-b - sympy.sqrt(discr)) / (2*a)
        print("   x1 =", x1)
        print("   x2 =", x2)
        print("   There are two real solutions!")
        return [x1, x2]
    return

def compute_D(a,b,c):
    d = (b*b) - (4*a*c)
    if d > 0:
        root = 'real and distinct'
    elif d==0:
        root = 'real and equal'
    elif d<0:
        root = 'complex'
    
    return root,d

def solve(a,b,c,d):
    i = -b/(2*a)
    j = (math.sqrt(d))/(2*a)
    r1 = i + j
    r2 = i - j
    return r1,r2


rt,D = compute_D(a,b,c)
# print('Roots are ',rt)
# print('Discriminant =',D)

if D >=0:
    r1,r2 = solve(a,b,c,D)
    # print('Roots=',r1)
    # print('Roots=',r2)

else:
    print('Out of scope')

middle_term(a,b,c,r1,r2)
sys.exit()

########MIDDLE TERM

##if r1.is_integer() and r2.is_integer():
##    print('Middle term possible')
##    middle_term(a,b,c,r1,r2)
##else:
##    print('Middle term NOT possible')



