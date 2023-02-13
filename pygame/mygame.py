# Write your code here :-WIDTH=400
from random import randint
WIDTH=400
HEIGHT=400
score=0
game_over=False
bunny=Actor("bunny")
bunny.pos=100,100

carrot=Actor("carrot")
carrot.pos=200,200

def draw():
    screen.fill("light green")
    bunny.draw()
    carrot.draw()
    screen.draw.text("Score:"+str(score),color="dark green",topleft=(10,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score:" +str(score),center=(200,50), fontsize=60)

def place_carrot():
    carrot.x=randint(20, (WIDTH-20))
    carrot.y=randint(20,(HEIGHT-20))

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

clock.schedule(time_up,15.0)
place_carrot()
