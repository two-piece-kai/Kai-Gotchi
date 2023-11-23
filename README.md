# Kai-Gotchi

## Description

I created Kai-Gotchi as an extremely small-scale project for fun once I started applying to internships.
I wanted "proof" that I was capable not only of ~ programming ~ in Python (something that I'm entirely
self-instructed in), but that I am able to read and adapt existing documentation with some success.

In this particular case, I used this frog tamagotchi game to gain an initial understanding of the tkinter
and pillow libraries. That being said, it's clear that tkinter and Python are not well-suited to anything
more than a low-quality, cute tamagotchi game.

## Installation

I've used pyinstaller to create a zipped executable file to easily run the game. However, I know very well
that an unknown and undocumented executable file will cause every computer and browser to insist this is
a virus and refuse download.

If downloading is an issue (either due to trusting some girl on the internet or your browser being a pain),
you may run the source code to play the game as long as main.py is contained in the same folder/directory
as the folder labeled "graphics", as this has... well, the graphics. Make sure to have pillow and tkinter
libraries installed <3

## Gameplay

Kai-Gotchi consists of a single animated frog and two bars labelled "Hunger" and "Clean".

The frog has three moods: happy, a little sad, and very angry.

Over 100 seconds, the frog will cycle through every mood. To return the frog back to his happier states,
one may click on the "Hunger" and "Clean" bars respectively to reduce the frog's stress. Due to my error
and laziness, a full "Hunger" bar indicates the frog is full and happy, while an empty "Clean" bar indicates
that he is clean and stress-free.

![Angry-Stage Frog]((https://github.com/two-piece-kai/Kai-Gotchi/blob/0d8a9b3302babcbb74b29239ecbd2994d93a18ca/docs/assets/angy.png))

## Credit

All art created by me. The code is entirely from scratch as well, which if read through, will be alarmingly obvious.

## License

MIT License (in other words, you may do as you please with any part of this)
