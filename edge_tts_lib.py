import edge_tts
import asyncio

class TextToSpeech:
    def __init__(self, voice='en-US-AriaNeural', rate='+0%', pitch='+0Hz', volume='+0%'):
        """
        Initializes the TextToSpeech class with default or user-specified voice, rate, pitch, and volume.
        
        :param voice: The name of the voice to use (default: 'en-US-AriaNeural').
        :param rate: The speaking rate (default: '1.0').
        :param pitch: The pitch adjustment (default: '0.0').
        :param volume: The volume adjustment (default: '+0dB').
        """
        self.voice = voice
        self.rate = rate
        self.pitch = pitch
        self.volume = volume

    async def text_to_speech(self, text, output_file):
        """
        Converts text to speech using the specified voice, rate, pitch, and volume, 
        and saves the output to a file.
        
        :param text: The text to be spoken.
        :param output_file: The output file path where the speech will be saved.
        """
        communicate = edge_tts.Communicate(text, self.voice, rate=self.rate, pitch=self.pitch, volume=self.volume)
        await communicate.save(output_file)

    def convert_text(self, text, output_file):
        """
        Public method to handle the asynchronous text-to-speech conversion.
        
        :param text: The text to be spoken.
        :param output_file: The output file path where the speech will be saved.
        """
        asyncio.run(self.text_to_speech(text, output_file))
