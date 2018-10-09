def get_prime(x):
    def is_prime(y):
        for j in range(2,y):
            if y%j == 0:
                return False
        return True
    master_list = []
    for i in range(2,x+1):
        if is_prime(i):
            master_list.append(i)
        else:
            continue
    return master_list

def index(master_list):
    for i,j in enumerate(master_list):
        print(i+1,j)
while True:
    prime_list = input('How far do you want?\n(or type \'break\' to stop) ')
    if str(prime_list) == 'break':
        break
    else:
        index(get_prime(int(prime_list)))