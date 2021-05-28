

def is_string(func):
    def wrapper(num):
        if type(num) == str:
            if num.isdigit():
                num = int(num)
            else:
                return '{} is not a number'.format(num)
        return func(num)
        
    return wrapper





@is_string
def expanded_form(num):
    '''This function returns the expanded form of a number'''
    n = str(num)
    b = len(n)
    r = []
    for nu in n:
        if len(n) > 1:   
            r.append(nu + '0'*(b-1))
            b -= 1
            continue
        r.append(nu)
    
    c = [n for n in r if int(n) > 0]
   
    return ' + '.join(c)
    

if __name__ == '__main__':
    num = input('[+] Enter number: ')
    print(expanded_form(num))
            
