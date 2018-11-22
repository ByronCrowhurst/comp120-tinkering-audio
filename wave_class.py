import wave
import struct
import math
import pygame
from pygame.locals import *
class WaveClass:

    def __init__(self, output_filename, length_of_file, channels, sample_width, sample_rate, volume, frequency):
        self.output_filename = output_filename
        self.length_of_file = length_of_file
        self.channel = channels
        self.sample_width = sample_width
        self.sample_rate = sample_rate
        self.sample_length = sample_rate / length_of_file
        self.volume = volume
        self.frequency = frequency

    def open_file(self, output_filename):
        file_to_write = wave.open(output_filename, "w")
        return file_to_write

    def close_file(self, file_to_close):
        file_to_close.close()

    def pack_wave(self, wave_type):
        # Will pack the values into a struct and return the struct.
        value_list = []


    def sine_wave(self, frequency, index_position, sample_rate, volume):
        # Creates a sine wave
        new_wave = (math.sin(2.0 * math.pi * frequency * (index_position / sample_rate)) / math.pi) * volume
        return new_wave

    def square_wave(self, frequency, index_position, sample_rate):
        # Creates a square wave
        if math.sin(2.0 * math.pi * (index_position / sample_rate)) > 0:
            return 1
        else:
            return -1