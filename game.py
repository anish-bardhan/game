time = 20
cal = 200
cash = 20
distance = 6

def route():
    ans = int(input("1. walk one block towards school, 2. run one block towards school, 3. stop by another restaurant"))
    if ans == 1:
        print("you walk one block towards school")
        time =- 2
        cal =- 5
        distance =- 1
        route()
    elif ans == 2:
        print("you run one block towards school")
        time =- 1
        cal =- 10
        distance =- 1
        route()
    elif ans == 3:
        print("you stop by another restaurant")
        time =- 2
        cal =- 2
        store()
    else:
        print("u lose!")

def school():
    ans = int(input("1. go to the classroom, 2. use the restroom, 3. fake a sickness"))
    if ans == 1:
        print("you are standing outside the classroom. What now?")
        #add recursion and subtractions
    elif ans == 2:
        print("you walk to the restroom")
        restroom()
    elif ans == 3:
        print("you went to the nurses's office")
        #add recursion and subtractions
    else:
        print("u lose!")

def restroom():
    
def ddash():
    ans = int(input("1. run for it, 2. hide, 3. go back and pay?"))
    if ans == 1:
        time -= 1
        cal -= 20
        cash -= 0
        print("you ran like forrest")
        store()
    elif ans == 2:
        time -= 5
        cal -= 10
        cash -= 2
        print("you got your drink in a to go cup")
        store()
    elif ans == 3:
        time -= 5
        cal += 20
        cash -= 9
        print("you went back to pay")
        store()
    else:
        print("u lose!")
    return time, cal, cash

def order_more():
    ans = int(input("1. change your mind, 2. order a drink to go, 3. order another meal?"))
    if ans == 1:
        time -= 1
        cal -= 5
        cash -= 0
        print("you changed your mind")
        store()
    elif ans == 2:
        time -= 1
        cal += 50
        cash -= 2
        print("you got your drink in a to go cup and only paid for the drink")
        store()
    elif ans == 3:
        time -= 1
        cal += 200
        cash -= 9
        print("you got a second helping of your meal and only paid for this dish")
        store()
    else:
        print("u lose!")
    return time, cal, cash

def store():
    ans = int(input("1. ask for check, 2. order more, 3. dine and dash?"))
    if ans == 1:
        time -= 1
        cal -= 5
        cash -= 0
        print("the waitress is bringing the check")
        route()
    elif ans == 2:
        time -= 1
        cal -= 5
        cash -= 0
        print("the waitress is bringing the menu")
        route()
    elif ans == 3:
        time -= 1
        cal -= 15
        cash -= 0
        print("just after finishing, you dash out the door of the restaurant!")
        ddash()
    else:
        print("u lose!")
    return time, cal, cash

def check():
    ans = int(input("1. pay by card, 2. pay by cash, 3. dine and dash? "))
    if ans == 1:
        time -= 2
        cal -= 5
        cash -= 9
        print("you paid $9 by card")
        route()
    elif ans == 2:
        time -= 1
        cal -= 5
        cash -= 9
        print("you paid $9 by cash")
        route()
    elif ans == 3:
        time -= 1
        cal -= 15
        cash -= 0
        print("just after finishing, you dash out the door of the restaurant!")
        ddash()
    else:
        print("u lose!")
    return time, cal, cash
