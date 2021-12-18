input.onButtonPressed(Button.A, function () {
    svemirski_brod.move(-1)
})
input.onButtonPressed(Button.B, function () {
    svemirski_brod.move(1)
})
input.onButtonPressed(Button.AB, function () {
    udarac = game.createSprite(svemirski_brod.get(LedSpriteProperty.X), svemirski_brod.get(LedSpriteProperty.Y))
    udarac.change(LedSpriteProperty.Brightness, 80)
    for (let index = 0; index < 4; index++) {
        udarac.change(LedSpriteProperty.Y, -1)
        basic.pause(150)
        if (udarac.isTouching(neprijatelj)) {
            game.addScore(1)
            neprijatelj.delete()
            udarac.delete()
        }
    }
    if (udarac.get(LedSpriteProperty.Y) <= 0) {
        udarac.delete()
    }
})
let neprijatelj: game.LedSprite = null
let udarac: game.LedSprite = null
let svemirski_brod: game.LedSprite = null
svemirski_brod = game.createSprite(2, 4)
game.setScore(0)
basic.forever(function () {
    neprijatelj = game.createSprite(randint(0, 4), 0)
    neprijatelj.set(LedSpriteProperty.Brightness, 150)
    basic.pause(100)
    neprijatelj.turn(Direction.Right, 90)
    for (let index = 0; index < 4; index++) {
        neprijatelj.move(1)
        basic.pause(500)
        if (neprijatelj.isTouching(svemirski_brod)) {
            basic.showString("" + game.score())
            game.gameOver()
        }
    }
    if (neprijatelj.isTouchingEdge()) {
        neprijatelj.delete()
    }
})
