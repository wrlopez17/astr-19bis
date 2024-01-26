# Python program to define a function and use it in the main part of the program

def f(x):
    return x**3 + 8

def main():
    result = f(9)
    print("Result:", result)
    
    if result > 27:
        print("YAY!")

# Call the main function
main()
