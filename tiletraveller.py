#Algoritm:
# Player starts in tile [1,1] from this tile the user can only go north. From [1,2] he can go all directions except 
# west. [1,1], [2,1] and [3,1] are the same because they can only go one north. [2,2] and [3,3] are the same because 
# they can go south and west.[1,3] can go south and east. [2,3] can go west and east. 
# We need to take in each tile starting from [1,1] and we inform the user which directions are possible and then he 
# can choose which direction he will go to. If he chooses an invalid direction we will inform him about that.




def directions(x):
    if x==1.1 or 2.1 or 3.1:
        print('You can travel (N)orth')
    elif x==2.2 or 3.3:
        print('You can travel (S)outh or (W)est')
    elif x==1.2:
        print('You can travel (N)orth, (E)ast or (S)outh')
    elif x==3.2:
        print('You can travel (N)orth or (S)outh')
    elif x==1.3:
        print('You can travel (E)ast or (S)outh')
    elif x==2.3:
        print('You can travel (E)ast or (S)outh')


def valid_direction(x,direction):
    if x==1.1 or 2.1 or 3.1:
        if direction!="N":
            return False
        else:
            return True
    elif x==2.2 or 3.3:
        if direction!="S" or "W":
            return False
        else: 
            return True
    elif x==1.2:
        if direction!="N" or "E" or "S":
            return False
        else:
            return True
    elif x==3.2:
        if direction!="N" or "S":
            return False
        else:
            return True
    elif x==1.3:
        if direction!="E" or "S":
            return False
        else:
            return True
    elif x==2.3:
        if direction!="E" or "S":
            return False
        else:
            return True

def move(x,direction):
    if direction=="N":
        x+=0.1
    elif direction=="E":
        x+=1
    elif direction=="S":
        x-=0.1
    elif direction=="W":
        x-=1
    return round(x,2)

x=1.1
while True:
    directions(x)
    direction=(raw_input('Direction: ')).upper()
    if x==3.1:
        print('Victory!')
        break
    else:
        if valid_direction(x,direction):
            x=move(x,direction)
        else:
            print('Not a valid direction!')



        


