# Conditions statements if elif else
def standarConditions():
    if(x > y):
        print("x its greater than y")
    elif(x < y):
        print("x its lower than y")
    else:
        print("x and y have the same value")

# Condition switch statement (with dictionary)
def switchStatement():
    switcher = {
        0: "This is Case Zero",
        1: "This is Case One",
        2: "This is Case Two",
    }
    return print(switcher.get(cases, "Non Existent Case"))

# Row Condition
def rowCondition():
    row_condition = "X and Y have the same value" if x == y else "X and Y have diferent values"
    print(row_condition)

# Match condition
def matchStatement():
    match cases:
        case 0:
            print("Case 0 with match")
        case 1:
            print("Case 1 with match")
        case 2:
            print("Case 2 with match")
        case other:
            print('No match found')

# Switch statement
if(__name__ == "__main__"):
    x = int(input("x: "))
    y = int(input("y: "))
    cases = int(input("switch case: "))

    # Exec and output
    standarConditions()
    switchStatement()
    rowCondition()
    matchStatement()
