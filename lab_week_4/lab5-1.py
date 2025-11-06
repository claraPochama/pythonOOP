
def main():
    print("Prime Number Checker \n")
    while True:
        num = int(input("Please enter an integer between 1 and 5000:"))
        if num == 0 or num == 1:
            print(num, "is not a prime number")
        elif num > 1 and num < 5000:
            # check for factors
            factors = [1]  # start with 1 always
            for i in range(2, num):
                if num % i == 0:
                    factors.append(i)
            factors.append(num)  # include the number itself

            if len(factors) == 2:
                print(num, "is a prime number.")
            else:
                print(num, "is NOT a prime number.")
                print("The factors of", num, "are:", factors)

        else:
            print(num,"please input a valid number.")
        again = input("Continue? (y/n): ")
        print()
        if again.lower() != "y":
            break
   
    
if __name__ == "__main__":
    main()