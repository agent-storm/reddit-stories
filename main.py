from edge_tts_lib import TextToSpeech

class StoryVideoCreator():
    def __init__(self) -> None:
        pass
    def generateVoice(self):
        tts = TextToSpeech(voice="en-US-AvaNeural")
        text = open("text_input.txt", "r", encoding="utf-8").read()
        output_file = f"assets/outputs/voice.mp3"
        tts.convert_text(text,output_file)
        print(f"Voice file created with name:{output_file}")

obj = StoryVideoCreator()
obj.generateVoice()
