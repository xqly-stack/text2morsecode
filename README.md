# Text-to-Morse Audio Converter
The Text-to-Morse Audio Converter is a Python function that converts a text message into a Morse code audio signal. The function takes a string of text as input and outputs an audio file containing the corresponding Morse code signal.

## Requirements
This function requires the following packages to be installed:

- pydub==0.25.1
- numpy==1.21.0
- scipy==1.7.0

## Installation
To install the required packages, run the following command:
````bash
pip install -r requirements.txt
````
Install ffmpeg aswell
````bash
apt install ffmpeg -y
````

## Usage
To use the Text-to-Morse Audio Converter, run the text_to_morse_audio.py script and provide the input text and output file name as command line arguments.
````bash
usage: text_to_morse_audio.py [-h] input_text output_file 

Converts a string of text to Morse code audio.

positional arguments:
  input_text            The text to be converted to Morse code.
  output_file
                        The name of the output audio file

optional arguments:
  -h, --help            show this help message and exit
````

For example, to convert the text "Hello, world!" to Morse code and save the output as "my_morse_code.wav", run the following command:

````bash
python text_to_morse_audio.py "Hello, world!" my_morse_code.wav
````

## Examples
Here are some example inputs and their corresponding Morse code signals:

Input: "Hello, world!"
Morse Code: .... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--

Input: "SOS"
Morse Code: ... --- ...

## Limitations
The Text-to-Morse Audio Converter only supports the 26 letters of the English alphabet, as well as the numbers 0-9 and some common punctuation marks. Any other characters in the input text will be ignored.
The output audio file may be quite large, depending on the length of the input text and the duration of the Morse code signal.
