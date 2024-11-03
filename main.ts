radio.onReceivedNumber(function (receivedNumber) {
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    if (receivedNumber == 0) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
    } else {
        basic.showLeds(`
            . . . . .
            . . . . .
            . # # # .
            . . . . .
            . . . . .
            `)
    }
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    basic.clearScreen()
})
input.onLogoEvent(TouchButtonEvent.LongPressed, function () {
    radio.sendNumber(1)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    radio.sendNumber(0)
})
basic.forever(function () {
	
})
