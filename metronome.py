from time import sleep
from thread import start_new_thread

from playsound import playsound as play


def get_tempo(seconds_per_minute, tone_length):
    while True:
        try:
            tempo = float(raw_input('Enter tempo in beats per minute: '))

            # Each beat plays for a non-zero amount of time, so there is an
            # upper limit on the number of beats per minute.
            if tempo > seconds_per_minute / tone_length:
                print "Tempo must be less than " \
                     + str(seconds_per_minute / tone_length) \
                     + " beats per minute."
                continue
        except ValueError:
            print "Enter a number."
        else:
            return tempo

            
def listener(flag):
    raw_input()
    flag.append(None)
    return

    
def metronome(tone, pause):
    # If the user happens to terminate the metronome while a tone is
    # playing, they might get some nasty errors back from their sound
    # driver (at least I did). It's better to open up a thread which
    # takes the 'terminate' command but waits until the tone stops playing
    # before executing it.
    break_flag = []
    start_new_thread(listener, (break_flag,))

    while True:
        if break_flag: 
            break
        play(tone)
        sleep(pause)

    return


def main():
    sound_file = 'kick.wav'    # metronome 'tick' to play
    tone_length = 0.25         # in seconds
    seconds_per_minute = 60.0
    
    # time to wait in between ticks
    tempo = get_tempo(seconds_per_minute, tone_length)
    print str(tempo)
    time_to_wait = seconds_per_minute / tempo - tone_length
    
    metronome(sound_file, time_to_wait)

if __name__ == '__main__':
    main()
