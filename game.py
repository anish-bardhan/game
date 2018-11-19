time = 20
cal = 200
distance = 3
result = False

print("you are at a restaurant 3 blocks away from school")
print("you have 20 minutes and 200 calories")
print("get back to school without running out of time or calories")

def route(time, cal, distance):
    if time > 0 and cal > 0:
        ans = int(input("1. walk one block towards school, 2. run one block towards school, 3. stop by another restaurant"))
        if ans == 1:
            print("you walk one block towards school")
            time -= 2
            cal -= 5
            distance -= 1
            if distance > 0:
                route(time, cal, distance)
            else:
                school(time, cal)
        elif ans == 2:
            print("you run one block towards school")
            time -= 1
            cal -= 10
            distance -= 1
            if distance > 0:
                route(time, cal, distance)
            else:
                school(time, cal)
        elif ans == 3:
            print("you stop by another restaurant")
            time -= 2
            cal -= 2
            store(time, cal)
        else:
            result = False
            return result
    else:
        result = False
        return result

def school(time, cal):
    if time > 0 and cal > 0:
        ans = int(input("1. go to the classroom, 2. use the restroom, 3. fake a sickness"))
        if ans == 1:
            print("you are standing outside the classroom. What now?")
            time -= 1
            cal -= 5
            classroom(time, cal)
        elif ans == 2:
            print("you walk to the restroom")
            time -= 1
            cal -= 5
            restroom(time, cal)
        elif ans == 3:
            print("you went to the nurses's office")
        else:
            result = False
            return result
    else:
        result = False
        return result

def restroom(time, cal):
    if time > 0 and cal > 0:
        ans = int(input("1. hide in bathroom, 2. hide in bathroom with mark, 3. go to classroom"))
        if ans == 1:
            print("you hide in the bathroom. your dean finds you in there and you get a saturday detention")
        elif ans == 2:
            print("you hide in the bathroom with mark. luckily you weren't caught")
            time -= 1
            cal -= 5
            classroom(time, cal)
        elif ans == 3:
            print("you go to class")
            time -= 1
            cal -= 5
            classroom(time, cal)
        else:
            result = False
            return result
    else:
        result = False
        return result

def classroom(time, cal):
    if time > 0 and cal > 0:
        ans = int(input("1. skip class, 2. use restroom, 3. start class"))
        if ans == 1:
            print("you skip class")
        elif ans == 2:
            time -= 1
            cal -= 5
            print("you go to the restroom")
            restroom(time, cal)
        elif ans == 3:
            print("class starts")
            result = True
            return result
        else:
            result = False
            return result
    else:
        result = False
        return result

def ddash(time, cal):
    if time > 0 and cal > 0:
        ans = int(input("1. run for it, 2. hide, 3. go back and pay?"))
        if ans == 1:
            time -= 1
            cal -= 20
            print("you ran like forrest")
            route(time, cal, distance)
        elif ans == 2:
            time -= 5
            cal -= 10
            print("you hid well")
            route(time, cal, distance)
        elif ans == 3:
            time -= 5
            cal += 20
            print("you went back to pay")
            store(time, cal)
        else:
            result = False
            return result
    else:
        result = False
        return result

def order_more(time, cal):
    if time > 0 and cal > 0:
        ans = int(input("1. change your mind, 2. order a drink to go, 3. order another meal?"))
        if ans == 1:
            time -= 1
            cal -= 5
            print("you changed your mind")
            store(time, cal)
        elif ans == 2:
            time -= 1
            cal += 50
            print("you got your drink in a to go cup")
            store(time, cal)
        elif ans == 3:
            time -= 1
            cal += 200
            print("you got a second helping of your meal")
            store(time, cal)
        else:
            result = False
            return result
    else:
        result = False
        return result

def store(time, cal):
    if time > 0 and cal > 0:
        ans = int(input("1. ask for check, 2. order more, 3. dine and dash?"))
        if ans == 1:
            time -= 1
            cal -= 5
            print("the waitress is bringing the check")
            route(time, cal, distance)
        elif ans == 2:
            time -= 1
            cal -= 5
            print("the waitress is bringing the menu")
            order_more(time, cal)
        elif ans == 3:
            time -= 1
            cal -= 15
            print("just after finishing, you dash out the door of the restaurant!")
            ddash(time, cal)
        else:
            result = False
            return result
    else:
        result = False
        return result

def check(time, cal):
    if time > 0 and cal > 0:
        ans = int(input("1. pay by card, 2. pay by cash, 3. dine and dash? "))
        if ans == 1:
            time -= 2
            cal -= 5
            print("you paid $9 by card")
            route(time, cal)
        elif ans == 2:
            time -= 1
            cal -= 5
            print("you paid $9 by cash")
            route(time, cal)
        elif ans == 3:
            time -= 1
            cal -= 15
            print("just after finishing, you dash out the door of the restaurant!")
            ddash(time, cal)
        else:
            result = False
            return result
    else:
        result = False
        return result

store(time, cal)

if result == True:
    print("you made it back to class on time")
else:
    print("you failed to make it back")
