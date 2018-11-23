# Contract 1 \- Sound Effect Generation
* _Byron Crowhurst_
* _github ID: ByronCrowhurst_

## How to use the program:
Running the program will display a blank screen.
* Controls:
* w \- Generates and writes to file a sine wave
* a \- Generates and writes to file a square wave
* d \- Generates and writes to file a saw wave
* p \- Plays the latest file to be generated

1. main\(\)
The main function groups the programs functionality, creates the display and checks for user input
2. new_sound_gen\(\)
Takes the wave class and type of wave to be generated, creates a new file and writes the generated wave data into it.
3. open_file\(\)
Opens a new file to be written into
4. close_file\(\)
Closes the file once written into.
5. sine_wave\(\)
Generates a sine wave
6. square_wave\(\)
Generates a square wave
7. saw_wave\(\)
Generates a saw wave
8. is_odd\(\)
Checks a number to see if it even or odd.