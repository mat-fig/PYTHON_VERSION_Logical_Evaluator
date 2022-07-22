# Helper functions "LISP terminology"
def is_null (x): return not (x)
def is_pair (x): return len(x) > 1
def is_atom (x):
    return not(is_null(x)) and not(is_pair(x))

# Constructors 
def make_not (p): return list(('-', p))
def make_and (p1, p2): return list((p1, '^', p2))
def make_or (p1, p2): return list((p1, 'v', p2))
def make_implies (p1, p2): return list((p1, '=>', p2))

# Selectors 
'''extract opertor from the propositional statement'''
def operator (p): 
    if (p[0] == '-'):
        return '-'
    else:
        return p[1]

'''extract first operand from the propositional statement'''
def first_operand (p):
    if (p[0] == '-'):
        return p[1]
    else:
        return p[0]

'''extract second operand from the propositional statement'''
def second_operand (p): return p[2]

# Classifiers
def is_not (p):
    if (is_atom(p)):
        return False
    else:
        return (operator(p) == '-')

def is_and (p):
    if (is_atom(p)):
        return False
    else:
        return (operator(p) == '^')


def is_or (p):
    if (is_atom(p)):
        return False
    else:
        return (operator(p) == 'v')

def is_implies (p):
    if (is_atom(p)):
        return False
    else:
        return (operator(p) == '=>')
    

def simplify (p):
    if (is_atom(p)): 
        return p
    if (is_not(p)): 
        return make_not (simplify(first_operand(p)))
    if (is_and(p)): 
        return (
            make_and (
                simplify(first_operand(p)), simplify(second_operand(p))))
    if (is_or(p)): 
        return (
            simplify (
                make_not (
                    make_and (
                        make_not(first_operand(p)), make_not(second_operand(p))))))
    if (is_implies(p)): 
        return (
            simplify (
                make_not(
                    make_and (
                        make_not(make_not(first_operand(p))), make_not(second_operand(p))))))


# Function to evaluate propositional statement
def eval_prop (p):
    if (is_not(p)): return (lambda x: (list ((not x))))(first_operand(p))
    if (is_and(p)): return (lambda x, y: (list ((x and y))))((first_operand(p)), (second_operand(p)))


if __name__ == '__main__':
    prop = ['-', True]
    print([1])
