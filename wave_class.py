import wave
import struct
import math
from even_or_odd import *
import pygame
from pygame.locals import *

"""
THIS CLASS IS IN PROGRESS. FEEL FREE TO IGNORE.
"""


class WaveClass:
    id = 0

    def __init__(self, output_filename, length_of_file, channels, sample_width, sample_rate, volume, frequency):
        self.output_filename = output_filename
        self.length_of_file = length_of_file
        self.channels = channels
        self.sample_width = sample_width
        self.sample_rate = sample_rate
        self.sample_length = sample_rate / length_of_file
        self.volume = volume
        self.frequency = frequency
        self.id = WaveClass.id
        WaveClass.id += 1

    def open_file(self, output_filename):
        """
        This opens a new file with a the desired file name to be worked on

        :param output_filename:     The name of the file
        :return:                    The new file to be written to
        """
        file_to_write = wave.open(output_filename, "w")
        return file_to_write

    def close_file(self, file_to_close):
        """
        This closes the desired file

        :param file_to_close:       The file to be closed
        :return:                    Nothing
        """
        file_to_close.close()

    def sine_wave(self, frequency, index_position, sample_rate, volume):
        """
        Creates a sine wave

        :param frequency:       The frequency of the wave (how close together the waves are)
        :param index_position:  The current position in the index
        :param sample_rate:     The rate at which the wave is sampled (typically 44100)
        :param volume:          The amplitude of the wave (how high it goes)
        :return:                The current sample of the wave
        """
        new_wave = 0
        new_wave += (math.sin(2.0 * math.pi * frequency * (index_position / sample_rate)) / math.pi) * volume
        packed_value = struct.pack('h', int(new_wave))
        return packed_value

    def square_wave(self, frequency, index_position, sample_rate):
        """
        Creates a square wave

        :param frequency:       Frequency of the wave
        :param index_position:  Current position in the index
        :param sample_rate:     Rate at which the wave is sampled
        :return:                1 or -1
        """
        # Creates a square wave
        value = 0
        if (math.sin(2.0 * math.pi * frequency * (index_position / sample_rate)) * self.volume) > 0:
            value += self.volume
        else:
            value += -self.volume
        packed_values = struct.pack('h', value)
        return packed_values

    def saw_wave(self, frequency, index_position, sample_rate, volume, max_range):
        """
        Creates a saw wave
        :param frequency:       The frequency of the wave
        :param index_position:  The index position
        :param sample_rate:     The rate at which the wave is sampled
        :param volume:          The amplitude of the wave
        :param max_range:       The maximum range of the wave
        :return:                The current sample of the wave
        """
        new_wave = 0
        for multiplier in range(1, max_range):
            if is_odd(multiplier):
                multiplier = -multiplier
            print(multiplier)
            new_wave += (math.sin(multiplier * 2.0 * math.pi * frequency * (index_position / sample_rate)) / (multiplier * math.pi))* volume
        packed_values = struct.pack('h', int(new_wave))
        return packed_values

    def combine_waves(self):
        pass
