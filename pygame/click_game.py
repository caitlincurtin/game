character=Actor('character')
character.toptright=0,10

WIDTH=500
HEIGHT=character.height+20

def draw():
    screen.fill((128, 50, 250))
    character.draw()

def update():
    character.left=character.left+2
    if character.left > WIDTH:
        character.right = 0

def on_mouse_down(pos):
    if character.collidepoint(pos):
        print("good vibes")
        set_character_clicked()
    else:
        print("the vibes")

def set_character_clicked():
    character.image='character_clicked'
    sounds.guitar_sound.play()
    print("good vibes")
    clock.schedule_unique(set_character_normal, 1.0)

def set_character_normal():
    character.image='character'
