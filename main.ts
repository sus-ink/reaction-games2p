input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (Running) {
        Running = false
        End = input.runningTime()
        basic.showLeds(`
            # # . . .
                        # # . . .
                        # # . . .
                        # # . . .
                        # # . . .
        `)
        basic.pause(1000)
        basic.showNumber(End - Recorder)
    } else {
        False_Start = true
        basic.showLeds(`
            # . . . .
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . .
        `)
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    x = randint(0, 4)
    y = randint(0, 4)
    basic.showNumber(3)
    basic.showNumber(2)
    basic.showNumber(1)
    basic.clearScreen()
    Running = false
    False_Start = false
    basic.pause(1000 + randint(100, 1000))
    if (!False_Start) {
        Recorder = input.runningTime()
        Running = true
        led.stopAnimation()
        basic.clearScreen()
        music.playMelody("C5 - - - - - - - ", 120)
        led.plot(x, y)
        basic.clearScreen()
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (Running) {
        Running = false
        End = input.runningTime()
        basic.showLeds(`
            . . . # #
                        . . . # #
                        . . . # #
                        . . . # #
                        . . . # #
        `)
        basic.pause(1000)
        basic.showNumber(End - Recorder)
    } else {
        False_Start = true
        basic.showLeds(`
            . . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        . . . . #
        `)
    }
    
})
let y = 0
let x = 0
let Recorder = 0
let End = 0
let False_Start = false
let Running = false
Running = false
False_Start = false
End = 0
Recorder = 0
