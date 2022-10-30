import logger as log

def calc_comp(z1,z2,z3):
    if z3 == '+':
        result = complex(z1) + complex(z2)
    elif z3 == '-':
        result = complex(z1) - complex(z2)
    elif z3 == '*':
        result = complex(z1) * complex(z2)       
    elif z3 == '/':
        result = complex(z1) / complex(z2)
    log.result_logger(result)   
    print (result)
