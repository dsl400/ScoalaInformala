
def sum_args(*args,**kwargs):
    result = 0
    args += tuple(kwargs.values())
    for arg in args:
        arg_type = type(arg)
        if arg_type is not int and arg_type is not float:
            continue
        result += arg
    return result

def sum_recursive(n):

    sum_n = 0
    sum_odd = 0
    sum_even = 0

    if n == 0:
        #daca n este zero functia returneaza zero
        return sum_n, sum_odd, sum_even

    sum_n += n #adaugam n la suma

    if n % 2:
        #adaugam numere pare
        sum_even += n
    else:
        #adaugam numere impare
        sum_odd += n 

    #urmatorul n devine n-1 daca n este pozitiv
    next_n = n-1 
    
    if n < 0:
        #urmatorul n devine n+1 daca n este negativ
        next_n = n+1
    
    if next_n == 0:
        #daca n este diferit de zero functia returneaza sumele curente
        return sum_n, sum_odd, sum_even 

    #daca n nu este diferit de zero calculam sumele pentru next_n
    _sum_n, _sum_odd, _sum_even = sum_recursive(next_n) 

    return sum_n + _sum_n, sum_odd + _sum_odd, sum_even + _sum_even


def print_input():
    in_value = input('introduceti un numar: ')
    try:
        in_value = int(in_value)
    except:
        in_value = 0
    print(f'numarul introduse este: {in_value}')


print(sum_args(1,1.1,'a',someval=2))
print(sum_recursive(-3))
print_input()
