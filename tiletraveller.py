#Algoritm:
# Player starts in tile [1,1] from this tile the user can only go north. From [1,2] he can go all directions except 
# west. [1,1], [2,1] and [3,1] are the same because they can only go one north. [2,2] and [3,3] are the same because 
# they can go south and west.[1,3] can go south and east. [2,3] can go west and east. 
# We need to take in each tile starting from [1,1] and we inform the user which directions are possible and then he 
# can choose which direction he will go to. If he chooses an invalid direction we will inform him about that.




def directions(x):
    if x==1.1 or x==2.1:
        print('You can travel: (N)orth.')
    elif x==3.1:
        print('Victory!')
    elif x==2.2 or x== 3.3:
        print('You can travel: (S)outh or (W)est.')
    elif x==1.2:
        print('You can travel: (N)orth or (E)ast or (S)outh.')
    elif x==3.2:
        print('You can travel: (N)orth or (S)outh.')
    elif x==1.3:
        print('You can travel: (E)ast or (S)outh.')
    elif x==2.3:
        print('You can travel: (E)ast or (W)est.')


def valid_direction(x,direction):
    if x==1.1 or x==2.1 or x==3.1:
        if direction!="N":
            return False
        else:
            return True
    elif x==2.2 or x==3.3:
        if direction=="S" or direction=="W":
            return True
        else: 
            return False
    elif x==1.2:
        if direction=="N" or direction=="E" or direction=="S":
            return True
        else:
            return False
    elif x==3.2:
        if direction=="N" or direction=="S":
            return True
        else:
            return False
    elif x==1.3:
        if direction=="E" or direction=="S":
            return True
        else:
            return False
    elif x==2.3:
        if direction=="E" or direction=="S":
            return True
        else:
            return False

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
    if x==3.1:
        print('Victory!')
        break
    else:
        directions(x)
        direction=(input('Direction: ')).upper()
        if valid_direction(x,direction):
            x=move(x,direction)
        else:
            print('Not a valid direction!')
            
            
            



        


