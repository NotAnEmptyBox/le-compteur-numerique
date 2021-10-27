def on_button_pressed_a():
    global peopleNb
    peopleNb += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global peopleNb
    peopleNb = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global peopleNb
    peopleNb += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

peopleNb = 0
peopleNb = 0

def on_forever():
    global peopleNb
    basic.clear_screen()
    peopleNb = max(peopleNb, 0)
    if peopleNb < 20:
        basic.show_number(peopleNb)
    else:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . # . .
                        . . # . .
                        . . # . .
                        . . . . .
                        . . # . .
        """)
basic.forever(on_forever)
