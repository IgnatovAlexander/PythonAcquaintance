import view
import calc_racional as rac
import calc_complex as comp

def check():
    a = view.user_input()
    if a == 1:
        pattern = "0,1,2,3,4,5,6,7,8,9,+,-,*,/"
        formula = view.input_data(a)
        for i in formula:
            if i not in pattern:
                view.iferror()
                return view.user_input()
        return rac.calc_rat(formula)
    elif a == 2:
        x,y,z = view.input_data(a)
        pattern = "+,-,*,/"
        if complex(x) and complex(y) and z in pattern:
            return comp.calc_comp(x, y, z)
        else:
            view.iferror()
            return view.user_input()
