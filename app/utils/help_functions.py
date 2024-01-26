import tempfile
import os
import whisper
import moviepy as mp

class HelpFunctions():

    @staticmethod  
    def irroita_aani(video):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmpfile:
            tmpfile.write(video)
            tmp_filename = tmpfile.name

        try:
            videoclip = mp.VideoFileClip(tmp_filename)
            audioclip = videoclip.audio
            audioclip_filename = tmp_filename + ".mp3"
            audioclip.write_audiofile(audioclip_filename)
        finally:
            audioclip.close()
            videoclip.close()
            os.remove(tmp_filename) 
        return audioclip_filename
    
    @staticmethod
    def whisper_f(audioclip):
        model = whisper.load_model("base")
        result = model.transcribe(audioclip)
        return result["text"]
    
    @staticmethod
    def testi():
        return "KAKKA"