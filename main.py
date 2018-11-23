import pygame
from pygame.locals import *
import sys
import wave_class
import os.path

"""
Main file for wave generation code
"""
OUTPUT_FILENAME = "new-sound"
LENGTH_OF_FILE_IN_SECONDS = 5
CHANNEL_COUNT = 1
SAMPLE_WIDTH = 2
SAMPLE_RATE = 44100  # How many time we sample per second
SAMPLE_LENGTH = SAMPLE_RATE * LENGTH_OF_FILE_IN_SECONDS
COMPRESSION_TYPE = 'NONE'
COMPRESSION_NAME = 'not compressed'
MAX_VOLUME = 32767  # How high/low the crest/trough will be. How loud the sound will be AMPLITUDE
FREQUENCY = 261  # Hz How tightly packed each wave is.
wave_types = {0: "sine", 1: "square", 2: "saw"}


def new_sound_gen(sound_class, wave_type):
    """
    Function for generating a new sound from the class.

    :param sound_class:         Class for generating waves
    :param wave_type:           Type of wave to be generated
    :return:                    Latest file generated
    """
    output_file_name = str(sound_class.output_filename + str(sound_class.id) + ".wav")
    # New file name generated so many files can be created
    created_sound = sound_class.open_file(output_file_name)
    created_sound.setparams((CHANNEL_COUNT, SAMPLE_WIDTH, SAMPLE_RATE,
                             SAMPLE_LENGTH, COMPRESSION_TYPE, COMPRESSION_NAME))
    values = []
    for i in range(0, int(sound_class.sample_length)):
        if wave_type == "sine":
            created_wave = sound_class.sine_wave(sound_class.frequency, i, sound_class.sample_rate, sound_class.volume)
        elif wave_type == "square":
            created_wave = sound_class.square_wave(sound_class.frequency, i, sound_class.sample_rate)
        elif wave_type == "saw":
            created_wave = sound_class.saw_wave(sound_class.frequency, i, sound_class.sample_rate, sound_class.volume, 6
                                                )
        # Allows program to generate different types of waves
        for j in range(0, sound_class.channels):
            values.append(created_wave)
    created_sound.writeframes(b''.join(values))
    sound_class.close_file(created_sound)
    return output_file_name


def main():
    """
    Main function for the program to run.

    :return:            Nothing
    """
    pygame.init()
    pygame.display.set_mode((250, 250), 0, 32)
    current_file_to_play = ""

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_p:
                    if os.path.isfile(current_file_to_play):
                        current_sound = pygame.mixer.Sound(current_file_to_play)
                        current_sound.play()
                if event.key == K_w:
                    current_file_to_play = new_sound_gen(
                        wave_class.WaveClass("new-sound", LENGTH_OF_FILE_IN_SECONDS, CHANNEL_COUNT, SAMPLE_WIDTH,
                                             SAMPLE_RATE, MAX_VOLUME, FREQUENCY), wave_types[0])
                    print(current_file_to_play)
                if event.key == K_a:
                    current_file_to_play = new_sound_gen(
                        wave_class.WaveClass("new-sound", LENGTH_OF_FILE_IN_SECONDS, CHANNEL_COUNT, SAMPLE_WIDTH,
                                             SAMPLE_RATE, MAX_VOLUME, FREQUENCY), wave_types[1])
                if event.key == K_d:
                    current_file_to_play = new_sound_gen(
                        wave_class.WaveClass("new-sound", LENGTH_OF_FILE_IN_SECONDS, CHANNEL_COUNT, SAMPLE_WIDTH,
                                             SAMPLE_RATE, MAX_VOLUME, FREQUENCY), wave_types[2])


if __name__ == "__main__":
    main()
