def on_button_pressed_a():
    global Running, End, False_Start
    if Running:
        Running = False
        End = input.running_time()
        basic.show_leds("""
            # # . . .
                        # # . . .
                        # # . . .
                        # # . . .
                        # # . . .
        """)
        basic.pause(1000)
        basic.show_number(End - Recorder)
    else:
        False_Start = True
        basic.show_leds("""
            # . . . .
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global x, y, Running, False_Start, Recorder
    x = randint(0, 4)
    y = randint(0, 4)
    basic.show_number(3)
    basic.show_number(2)
    basic.show_number(1)
    basic.clear_screen()
    Running = False
    False_Start = False
    basic.pause(1000 + randint(100, 1000))
    if not (False_Start):
        Recorder = input.running_time()
        Running = True
        led.stop_animation()
        basic.clear_screen()
        music.play_melody("C5 - - - - - - - ", 120)
        led.plot(x, y)
        basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Running, End, False_Start
    if Running:
        Running = False
        End = input.running_time()
        basic.show_leds("""
            . . . # #
                        . . . # #
                        . . . # #
                        . . . # #
                        . . . # #
        """)
        basic.pause(1000)
        basic.show_number(End - Recorder)
    else:
        False_Start = True
        basic.show_leds("""
            . . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        . . . . #
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

y = 0
x = 0
Recorder = 0
End = 0
False_Start = False
Running = False
Running = False
False_Start = False
End = 0
Recorder = 0