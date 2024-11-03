def on_received_number(receivedNumber):
    music.play(music.tone_playable(262, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    if receivedNumber == 0:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . # # # .
            . . . . .
            . . . . .
            """)
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    basic.clear_screen()
radio.on_received_number(on_received_number)

def on_logo_long_pressed():
    radio.send_number(1)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_logo_pressed():
    radio.send_number(0)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    pass
basic.forever(on_forever)
