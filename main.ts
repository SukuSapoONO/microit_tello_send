input.onGesture(Gesture.TiltRight, function () {
    if (flying == 1) {
        radio.sendString("right=" + ("" + right))
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            `)
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.A, function () {
    if (flying == 1) {
        radio.sendString("ccw=" + ("" + degrees))
        flying = 1
        basic.showLeds(`
            . . # # #
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            `)
        basic.clearScreen()
    }
})
input.onGesture(Gesture.TiltLeft, function () {
    if (flying == 1) {
        radio.sendString("left=" + ("" + left))
        basic.showLeds(`
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            `)
        basic.clearScreen()
    }
})
input.onGesture(Gesture.LogoUp, function () {
    if (flying == 1) {
        radio.sendString("Back=" + ("" + back))
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            `)
        basic.clearScreen()
    }
})
input.onGesture(Gesture.Shake, function () {
    radio.sendString("takeoff")
    flying = 1
    basic.showLeds(`
        . . # . .
        . # # # .
        # . # . #
        . . # . .
        # # # # #
        `)
    basic.clearScreen()
})
input.onGesture(Gesture.LogoDown, function () {
    if (flying == 1) {
        radio.sendString("forward=" + ("" + forward))
        basic.showLeds(`
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            `)
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.AB, function () {
    radio.sendString("land")
    flying = 0
    basic.showLeds(`
        # # # # #
        . . # . .
        # . # . #
        . # # # .
        . . # . .
        `)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    if (flying == 1) {
        radio.sendString("cw=" + ("" + degrees))
        flying = 1
        basic.showLeds(`
            # # # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            `)
        basic.clearScreen()
    }
})
let back = 0
let forward = 0
let right = 0
let left = 0
let degrees = 0
let flying = 0
radio.setGroup(1)
flying = 0
degrees = 90
left = 100
right = 100
forward = 100
back = 100
