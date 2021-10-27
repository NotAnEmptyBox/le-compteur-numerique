input.onButtonPressed(Button.A, function () {
    peopleNb += 1
})
input.onButtonPressed(Button.AB, function () {
    peopleNb = 0
})
input.onButtonPressed(Button.B, function () {
    peopleNb += -1
})
let peopleNb = 0
peopleNb = 0
basic.forever(function () {
    basic.clearScreen()
    peopleNb = Math.max(peopleNb, 0)
    if (peopleNb < 20) {
        basic.showNumber(peopleNb)
    } else {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . # . .
            . . # . .
            . . # . .
            . . . . .
            . . # . .
            `)
    }
})
