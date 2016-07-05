#!/usr/bin/python
import time
import sys
import pygame


# Function is used to return the cursor to
# overwrite the old messages
def erase_line(chars):
    print '\b' * chars,
    sys.stdout.flush()


# Function to print number of minutes remaining
# Currently uses sleep. To add further functionality, we will
# have to change that, and use multithreading to listen for keypresses
def countdown(minutes):
    while minutes > 0:
        message = '\bTime remaining: {0} minutes'.format(minutes)
        print message,
        sys.stdout.flush()
        time.sleep(60)
        minutes -= 1
        erase_line(len(message))
    print ' ' * (len(message) + 2),
    erase_line(len(message) + 2)
    return


# Function for the working cycles
def start_pomodoro(cycle, work_length):
    minutes = work_length
    print 'Pomodoro number {0}:    '.format(cycle),
    countdown(minutes)
    play_sound(1)
    print 'Completed'
    return


# Function for the break cycles
def start_break(minutes):
    print 'Break! Relax... ',
    countdown(minutes)
    play_sound(3)
    print 'Okay. Back to work'
    return


# Function to play sound
def play_sound(n):
    while n > 0:
        pygame.mixer.music.play()
        time.sleep(0.2)
        n -= 1
    return


def main():
    pygame.init()
    pygame.mixer.music.load("sound.wav")
    cycles = 0
    time_worked = 0
    time_rested = 0
    work_length = 25
    break_length = 5
    raw_input("Press enter to begin...")
    while cycles < 4:
        cycles += 1
        start_pomodoro(cycles, work_length)
        start_break(break_length)
    print 'Good job!'

if __name__ == '__main__':
    main()

