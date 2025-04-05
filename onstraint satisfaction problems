VARIABLES=['csc','maths','phy','che','tam','eng','bio']
DOMAIN=['Monday','Tuesday','Wednesday']
def is_consistent(var,value,assignment):
    return True
def backtrack(assignment):
    if len(assignment)==len(VARIABLES):
        assigned_days=set(assignment.values())
        if all(day in assigned_days for day in DOMAIN):
            return assignment
        else:
            return None
    for var in VARIABLES:
        if var not in assignment:
            for value in DOMAIN:
                if is_consistent(var,value,assignment):
                    assignment[var]=value
                    result=backtrack(assignment)
                    if result:
                        return result
                    del assignment[var]
            return None
    return None
solution=backtrack({})
print("RESULT:")
print(solution)
