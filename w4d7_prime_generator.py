import math

# Generate a List of Prime Numbers Up to N
# Prime numbers are natural numbers that are 
# divisble by only 1 and the number itself.

def prime_generator(num_inp):
    """Generate a list of prime numbers upto N"""
    
    prime_lst = []
       
    if num_inp < 2:
        return prime_lst
    
    for num_inp in range(2, num_inp+1):
        is_prime = True 
        for i in range(2, int(math.sqrt(num_inp))+1):
            if num_inp % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_lst.append(num_inp)
            
    return prime_lst


def main():
    """Main interface for prime generator"""

    welcome_msg = "Prime number list generator upto N"
    print(welcome_msg)
    print('-' * len(welcome_msg))
    
    while True:
        inp = input("Enter a number or 'q' to quit: ").strip().lower()
        if inp == 'q':
            print('Bye!')
            break
        try:
            inp_num = int(inp)
            if inp_num <= 0:
                print('Enter an integer number greater than zero.')
        except ValueError:
            print('Invalid input! Enter a number.') 
        
        primes = prime_generator(inp_num)
        print(f"Prime numbers upto {inp_num}: {primes}")
          
if __name__ == "__main__":
    main()