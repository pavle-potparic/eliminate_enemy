def on_button_pressed_a():
    svemirski_brod.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    svemirski_brod.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    global udarac
    udarac = game.create_sprite(svemirski_brod.get(LedSpriteProperty.X),
        svemirski_brod.get(LedSpriteProperty.Y))
    udarac.change(LedSpriteProperty.BRIGHTNESS, 80)
    for index in range(4):
        udarac.change(LedSpriteProperty.Y, -1)
        basic.pause(150)
        if udarac.is_touching(neprijatelj):
            game.add_score(1)
            neprijatelj.delete()
            udarac.delete()
    if udarac.get(LedSpriteProperty.Y) <= 0:
        udarac.delete()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

neprijatelj: game.LedSprite = None
udarac: game.LedSprite = None
svemirski_brod: game.LedSprite = None
svemirski_brod = game.create_sprite(2, 4)
game.set_score(0)

def on_forever():
    global neprijatelj
    neprijatelj = game.create_sprite(randint(0, 4), 0)
    neprijatelj.set(LedSpriteProperty.BRIGHTNESS, 150)
    basic.pause(100)
    neprijatelj.turn(Direction.RIGHT, 90)
    for index2 in range(4):
        neprijatelj.move(1)
        basic.pause(500)
        if neprijatelj.is_touching(svemirski_brod):
            basic.show_string("" + str((game.score())))
            game.game_over()
    if neprijatelj.is_touching_edge():
        neprijatelj.delete()
basic.forever(on_forever)
