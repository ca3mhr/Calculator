'''
    A Calculator Program Written In Python
'''

'''
    This program is divided into 3 sections:
        Section 1: The imports used in the program
        Section 2: The functions used in the program
        Section 3: The start of the program
'''

'''
    Section 1: The imports
'''
import os

'''
    Section 2: The functions
'''

'''
    Function list:
        1.clear_screen()
        2.cal()
        3.main()
'''
def clear_screen():
    '''
        Clear the terminal when called
    '''
    if os.name=="posix":
        os.system("clear")
    else:
        os.system("cls")

def cal():
    '''
        The calculator logic
    '''
    clear_screen()
    print("Welcome To The Calculator!")
    print("Press 1 to exit")
    print("Press 2 for addition")
    print("Press 3 for subtraction")
    print("Press 4 for multipication")
    print("Press 5 for divition")

    main_input=input(">")

    try:
        con_input=int(main_input)

        check_num=False

        for i in range(1,6):
            if con_input==i:
                check_num=True

        if check_num:
            if con_input==1:
                return -1
            else:
                print("Enter first number:")
                raw_fno=input(">")
                print("Enter second number:")
                raw_sno=input(">")
                
                try:
                    fno=int(raw_fno)
                    sno=int(raw_sno)

                    if con_input==2:
                        ans=fno+sno
                    elif con_input==3:
                        ans=fno-sno
                    elif con_input==4:
                        ans=fno*sno
                    elif con_input==5:
                        ans=fno/sno
                    else:
                        ans=0

                    print("The answer is",int(ans))
                    input(">")
                except:
                    print("Error: The input must be a number")
                    print("Please try again")
        else:
            print("Error: The input must be a number between 1 and 6")
            print("Please try again")
            input(">")
    except:
        print("Error: The input must be a number")
        print("Please try again")
        input(">")

def main():
    '''
        The main loop of the function
    '''
    while True:
        exit_com=cal()
        if exit_com==-1:
            print("Bye!")
            break

'''
    Section 3: The start of the program
'''
main()


