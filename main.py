import sys
from sympy import *

class QuadraticSolver:
    def __init__(self):
        self.show_welcome_screen()

    def show_welcome_screen(self):
        print("-------------*--------------")
        print("Welcome to Quadratic Solver!")
        print("-------------*--------------")
        print("A quadratic is an expression of the form ax2 + bx + c, where a, b and c are given numbers and a ≠ 0.")
        
        print("Type one of the following commands:")
        print("-------------------------------------")
        print("  help  - Display the help menu")
        print("  learn - Learn about quadratic equations")
        print("  solve - Solve a quadratic equation")
        print("  main  - Return to the main menu")
        print("  quit  - Exit the program")
        print("------------------------------------")
        print(" ")
        print("Note: -")
        print("It cannot solve complex roots.")


    def run(self):
        while True:
            command = input("\nEnter a command: ")

            if command == "help":
                self.show_help_menu()

            elif command == "learn":
                self.learn_quadratic_equations()

            elif command == "solve":
                self.solve_quadratic_equation()

            elif command == "main":
                self.show_welcome_screen()

            elif command == "quit":
                print("Goodbye...!")
                sys.exit()

            else:
                print("Invalid command. Type 'help' to see available commands.")

    def show_help_menu(self):
        '''
        This function explains about help menu how to use all the commands.
        '''
        print("Help menu:")
        print("  ")
        print("  --learn     to understand how quadratic equations work.")
        print("  --solve     to solve a quadratic equation.")
        print("  --main      will return you to the main menu.")
        print("  --quit      will exit the program.")

    def learn_quadratic_equations(self):
        '''
        This function describes about quadratic equation how to solve the quadratic equations.
        '''
        print(" ")
        print("Section 1")

        print("• Quadratic equation : A quadratic equation in the variable x is of the form ax2 + bx + c = 0, where a, b, c are real numbers and a ≠ 0.")
        print("• Roots of a quadratic equation : A real number α is said to be a root of the quadratic equation ax2 + bx + c = 0, if aα2 + bα + c = 0.") 
        print("• The roots of the quadratic equation ax2 + bx + c = 0 are the same as the zeroes of the quadratic polynomial ax2 + bx + c.")
        
        print(" ")
        print("Section 2")
        print("• The expression b2 – 4ac is called the discriminant of the quadratic equation.") 
        print("• Existence of roots of a quadratic equation: A quadratic equation ax2 +bx+c=0 has QUADRATIC EQUATIONS CHAPTER 4 03/05/18 36 EXEMPLAR PROBLEMS")
        print("         (i) two distinct real roots if b2 – 4ac > 0") 
        print("         (ii) two equal real roots if b2 – 4ac = 0") 
        print("         (iii) no real roots if b2 – 4ac < 0.")

        print(" ")
        print("Section 3")
        print("The method of solving quadratic equations by factoring rests on the simple fact.  if we obtain zero as the product of two numbers then at least one of the numbers must be zero.") 
        print("In the module, Factorisation, we first saw how to factor monic quadratics, then we learnt how to factorise non-monic quadratics.") 
        print("To factor ax 2 + bx + c we try to find two numbers whose sum is b and whose product is ac. We now apply this idea to solving quadratic equations.")
        y = symbols('2x^2')
        y1 = symbols('5x')
        y2 = symbols('3')
        y3 = symbols('2x')
        y4 = symbols('3x')
        y5 = symbols('2a')
        y6 = symbols('x')
        print(" ")
        print("EXAMPLE:") 
        print("Solve the equation: ") 
        eq1 = Eq(y + y1 + y2, 0)
        pprint(eq1)
        print(" ")
        print("SOLUTION: -") 
        print("Using the factoring method from the module Factorisation, we multiply 2 and 3 to give 6 and find two numbers that multiply to give 6 and add to give 5.") 
        print("The desired numbers are 2 and 3. We use these numbers to split the middle term and factor in pairs.")
        print(" ") 
        eq1 = Eq(y + y1 + y2, 0)
        pprint(eq1)
        print(" ") 
        eq2 = Eq(y + y3 + y4 + y2, 0)
        pprint(eq2)
        print("(Split the middle term)")
        print(" ") 
        eq3 = Eq(y3*(y6 + 1) + y2*(y6 + 1), 0)
        pprint(eq3)
        print(" ") 
        eq4 = Eq((y6 + 1) * (y3 + y2), 0)
        pprint(eq4)
        print(" ")
        print("We can now equate each factor to zero and obtain")
        print(" ")
        eq5 = Eq((y6 + 1), 0)
        eq6 = Eq((y3 + y2), 0)
        pprint(eq5)
        print('or')
        pprint(eq6)
        print("x = –1, or x = –3/2.")  

        print(" ")
        print("Section 4")
        print("QUADRATIC FORMULA")
        print("Any quadratic equation of the form ax^2+bx+c=0, where a ≠ 0 can be solved for both real and imaginary solutions using the quadratic formula:") 
        
        x1 = symbols('x_1')
        x2 = symbols('x_2')
        up1 = symbols('-b')
        up2 = symbols('b^2')
        up4 = symbols('4ac')
        lw1 = symbols('2a')
        eq1 = Eq(x1, (up1 + sqrt(up2 - up4)) / lw1)
        eq2 = Eq(x2, (up1 - sqrt(up2 - up4)) / lw1)
        pprint(eq1)
        print("Example:") 
        xp = symbols('x^2')
        yp = symbols('6x')
        eq2 = Eq(xp+yp-11,0)
        pprint(eq2)
        print("(a = 1, b = 6, c = -11)")   
        print("Substitute values into the quadratic formula:")
        a = symbols('-6')
        up21 = symbols('6^2')
        x21 = symbols('x_1')
        x22 = symbols('x_2')
        x31 = symbols('4(1)')
        x32 = symbols('(11)')
        y11 = symbols('2(1)')
        eq3 = Eq(x21, (a + sqrt(up21 - (x31) - (x32))) / y11)
        eq4 = Eq(x22, (a - sqrt(up21 - (x31) - (x32))) / y11)
        pprint(eq3)
        pprint(eq4)
        print("----->") 
        up31 = symbols('36')
        up32 = symbols('44')
        x31 = symbols('x_1')
        x32 = symbols('x_2')
        y21 = symbols('2')
        eq5 = Eq(x31, (a + sqrt(up31 + up32)) / y21)
        eq6 = Eq(x32, (a - sqrt(up31 + up32)) / y21)
        pprint(eq5)
        pprint(eq6)
        print("----->") 
        up41 = symbols('80')
        x41 = symbols('x_1')
        x42 = symbols('x_2')
        eq7 = Eq(x41, (a + sqrt(up41)) / y21)
        eq8 = Eq(x42, (a - sqrt(up41)) / y21)
        pprint(eq7)
        pprint(eq8)
        print("simplify the radical")
        print("----->")
        eq9 = Eq(x1,  (a + root(5,4)) / y21)
        eq10 = Eq(x2, (a - root(5,4)) / y21)
        pprint(eq9)
        pprint(eq10)
        print("----->") 
        a1 = symbols('3')
        eq11 = Eq(x1,  (a1 + root(5,2)) / y21)
        eq12 = Eq(x2,  (a1 - root(5,2)) / y21)
        pprint(eq11)
        pprint(eq12)
        print("This is the final simplified EXACT answer")
        print("Answer: x= 1.472")

    def solve_quadratic_equation(self):
        '''
        This function is used to solve the quadratic equations by calling factor.py file.
        ''' 
        import factor
        
        #input parameters for solving the quadratic equations
        a = int(input('Enter a coefficient -> '))
        b = int(input('Enter b coefficient -> '))
        c = int(input('Enter c coefficient -> '))
        
        print('Middle term possible.')
        factor.middle_term(a, b, c) #call middle term function from factor.py file 
    
#main function call
if __name__ == '__main__':
    solver = QuadraticSolver()
    solver.run()
