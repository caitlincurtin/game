# Write your code here :-WIDTH=400
from random import randint
WIDTH=450
HEIGHT=450
score=0
game_over=False
bunny=Actor("bunny")
bunny.pos=100,100

carrot=Actor("carrot")
carrot.pos=200,200

rock=Actor("rock")
rock.pos=300,300

def draw():
    screen.fill("light green")
    bunny.draw()
    carrot.draw()
    rock.draw()
    screen.draw.text("Score:"+str(score),color="dark green",topleft=(10,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score:" +str(score),center=(200,50), fontsize=60)

def place_carrot():
    carrot.x=randint(20, (WIDTH-20))
    carrot.y=randint(20,(HEIGHT-20))

def place_rock():
    rock.x=randint(50, (WIDTH-50))
    rock.y=randint(50, (HEIGHT-50))

def time_up():
    global game_over
    game_over=True

def update():
    global score

    if keyboard.left:
        bunny.x=bunny.x-2
    elif keyboard.right:
        bunny.x=bunny.x+2
    elif keyboard.up:
        bunny.y=bunny.y-2
    elif keyboard.down:
        bunny.y=bunny.y+2

    carrot_collected=bunny.colliderect(carrot)

    if carrot_collected:
        score=score+1
        place_carrot()
        place_rock()

    rock_collected=bunny.colliderect(rock)

    if rock_collected:
        score=score-1
        place_rock()

clock.schedule(time_up,20.0)
place_carrot()
