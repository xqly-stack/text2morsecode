import argparse
from pydub import AudioSegment
from pydub.generators import Sine

# Define the Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

# Define the duration of each dot and dash (in milliseconds)
DOT_DURATION = 100
DASH_DURATION = 3 * DOT_DURATION


def text_to_morse_audio(text):
    """Converts text to Morse code and generates an audio signal that encodes
    the Morse code representation of the text.

    Args:
        text (str): The input text to convert to Morse code.

    Returns:
        AudioSegment: An audio signal that encodes the Morse code representation
        of the input text.
    """
    morse_code = ''
    for char in text:
        morse_char = MORSE_CODE_DICT.get(char.upper())
        if morse_char:
            morse_code += morse_char + ' '
        else:
            morse_code += ' '

    # Generate the audio signal
    audio_signal = AudioSegment.silent(duration=DOT_DURATION)
    for element in morse_code:
        if element == '.':
            beep = Sine(440).to_audio_segment(duration=DOT_DURATION)
        elif element == '-':
            beep = Sine(440).to_audio_segment(duration=DASH_DURATION)
        else:  # Pause between elements
            beep = AudioSegment.silent(duration=DOT_DURATION)
        audio_signal += beep + AudioSegment.silent(duration=DOT_DURATION)

    return audio_signal


if __name__ == '__main__':
    # Define command-line arguments
    parser = argparse.ArgumentParser(description='Convert text to Morse code and generate an audio signal.')
    parser.add_argument('text', type=str, help='The text to convert to Morse code.')
    parser.add_argument('output_file', type=str, help='The output file to save the audio signal to.')
    args = parser.parse_args()

    # Convert text to Morse code and generate the audio signal
    audio_signal = text_to_morse_audio(args.text)

    # Save the audio signal to a file
    audio_signal.export(args.output_file, format='wav')
