def on_gesture_tilt_right():
    if flying == 1:
        radio.send_string("right=" + str(right))
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
        basic.clear_screen()
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_button_pressed_a():
    global flying
    if flying == 1:
        radio.send_string("ccw=" + str(degrees))
        flying = 1
        basic.show_leds("""
            . . # # #
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        """)
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    if flying == 1:
        radio.send_string("left=" + str(left))
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
        basic.clear_screen()
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_logo_up():
    if flying == 1:
        radio.send_string("Back=" + str(back))
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        """)
        basic.clear_screen()
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_shake():
    global flying
    radio.send_string("takeoff")
    flying = 1
    basic.show_leds("""
        . . # . .
                . # # # .
                # . # . #
                . . # . .
                # # # # #
    """)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_logo_down():
    if flying == 1:
        radio.send_string("forward=" + str(forward))
        basic.show_leds("""
            . . # . .
                        . # # # .
                        # . # . #
                        . . # . .
                        . . # . .
        """)
        basic.clear_screen()
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_button_pressed_ab():
    global flying
    radio.send_string("land")
    flying = 0
    basic.show_leds("""
        # # # # #
                . . # . .
                # . # . #
                . # # # .
                . . # . .
    """)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global flying
    if flying == 1:
        radio.send_string("cw=" + str(degrees))
        flying = 1
        basic.show_leds("""
            # # # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        """)
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

back = 0
forward = 0
right = 0
left = 0
degrees = 0
flying = 0
radio.set_group(1)
flying = 0
degrees = 90
left = 100
right = 100
forward = 100
back = 100