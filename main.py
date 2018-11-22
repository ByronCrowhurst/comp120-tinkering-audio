import wave
import struct
import math
import pygame
from pygame.locals import *
import sys

OUTPUT_FILENAME = "noise.wav"
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
wave_intensity = {"none": 0, "low": 1, "medium": 2, "high": 3}


def sound_gen():
    noise_out = wave.open(OUTPUT_FILENAME, "w")
    noise_out.setparams((CHANNEL_COUNT, SAMPLE_WIDTH, SAMPLE_RATE, SAMPLE_LENGTH, COMPRESSION_TYPE, COMPRESSION_NAME))

    values = []
    for i in range(0, SAMPLE_LENGTH):
        packed_value = wave_gen(wave_types[1], wave_intensity["high"], i)

        for j in range(0, CHANNEL_COUNT):
            values.append(packed_value)
    noise_out.writeframes(b''.join(values)) # writing the array in the file
    noise_out.close()


def wave_gen(wave_type, intensity, i):
    value_list = []
    if wave_type == "sine":
        if intensity <= 0:
            value = (math.sin(2.0 * math.pi * FREQUENCY * (i / SAMPLE_RATE)) / math.pi) * MAX_VOLUME
            value_list.append(value)
    elif wave_type == "square":
        if intensity >= 0:
            value = (math.sin(2.0 * math.pi * FREQUENCY * (i / SAMPLE_RATE)) / math.pi) * MAX_VOLUME
            value_list.append(value)
        if intensity >= 1:
            value_two = (math.sin(3 * (2.0 * math.pi * FREQUENCY * (i / SAMPLE_RATE))) / (3 * math.pi)) * MAX_VOLUME
            value_list.append(value_two)
        if intensity >= 2:
            value_three = (math.sin(5 * (2.0 * math.pi * FREQUENCY * (i / SAMPLE_RATE))) / (5 * math.pi)) * MAX_VOLUME
            value_list.append(value_three)
        if intensity >= 3:
            value_four = (math.sin(7 * (2.0 * math.pi * FREQUENCY * (i / SAMPLE_RATE))) / (7 * math.pi)) * MAX_VOLUME
            value_list.append(value_four)
    elif wave_type == "saw":
        if intensity >= 0:
            value = (math.sin(2.0 * math.pi * FREQUENCY * (i / SAMPLE_RATE)) / -math.pi) * MAX_VOLUME
            value_list.append(value)
        if intensity >= 1:
            value_two = (math.sin(2 * (2.0 * math.pi * FREQUENCY * (i / SAMPLE_RATE))) / (2 * math.pi)) * MAX_VOLUME
            value_list.append(value_two)
        if intensity >= 2:
            value_three = (math.sin(-3 * (2.0 * math.pi * FREQUENCY * (i / SAMPLE_RATE))) / (-3 * math.pi)) * MAX_VOLUME
            value_list.append(value_three)
        if intensity >= 3:
            value_four = (math.sin(4 * (2.0 * math.pi * FREQUENCY * (i / SAMPLE_RATE))) / (4 * math.pi)) * MAX_VOLUME
            value_list.append(value_four)
    value_sum = int(sum(value_list))
    packed_values = struct.pack('h', value_sum)
    return packed_values


def main():
    sound_gen()
    pygame.init()
    pygame.display.set_mode((250, 250), 0, 32)
    sound = pygame.mixer.Sound('noise.wav')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_p:
                    sound.play()


main()
