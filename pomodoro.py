#!/home/samhattangady/anaconda3/bin/python
import time
import sys
import pygame
import argparse
import datetime


# Function to print current time
def print_time():
    print('{0:02d}:{1:02d}'.format(datetime.datetime.now().hour, datetime.datetime.now().minute), end='\t')

# Function is used to return the cursor to
# overwrite the old messages
def erase_line(chars):
    print('\b' * chars, end=' ')
    sys.stdout.flush()


# Function to print number of minutes remaining
# Currently uses sleep. To add further functionality, we will
# have to change that, and use multithreading to listen for keypresses
def countdown(minutes):
    while minutes > 0:
        message = '\bTime remaining: {0} minutes'.format(minutes)
        print(message, end=' ')
        sys.stdout.flush()
        time.sleep(60)
        minutes -= 1
        erase_line(len(message))
    print(' ' * (len(message) + 2), end=' ')
    erase_line(len(message) + 2)
    return


# Function for the working cycles
def start_pomodoro(cycle, work_length):
    minutes = work_length
    print_time()
    print('Pomodoro number {0}:    '.format(cycle), end=' ')
    countdown(minutes)
    play_sound(1)
    print('Completed')
    return


# Function for the break cycles
def start_break(minutes):
    print_time()
    print('Break! Relax... ', end=' ')
    countdown(minutes)
    play_sound(3)
    print('Okay. Back to work')
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
    parser = argparse.ArgumentParser(description='A pomodoro timer in your terminal')
    parser.add_argument('-w', '--work_length', help='Length of working session in minutes. Default is 25')
    parser.add_argument('-b', '--break_length', help='Length of break in minutes. Default is 5 mins')
    parser.add_argument('-n', '--number_of_cycles', help='Number of cycles. Default is 4')
    args = parser.parse_args()

    work_length = int(args.work_length) if args.work_length else 25
    break_length = int(args.break_length) if args.break_length else 5
    number_of_cycles = int(args.number_of_cycles) if args.number_of_cycles else 4
    for cycle in range(number_of_cycles):
        input("Press enter to begin working...")
        start_pomodoro(cycle+1, work_length)
        if cycle+1 < number_of_cycles:
            input("Press enter to begin break...")
            start_break(break_length)
    print('Good job!')

if __name__ == '__main__':
    main()
