import os,urllib,random,pydub,speech_recognition,time
from DrissionPage.common import Keys
from DrissionPage import ChromiumPage 

class OFD:
    def __init__(self, dr:ChromiumPage):
        self.dr = dr
    
    def solveCaptcha(self):
        iframe_inner = self.dr"@title=reCAPTCHA")
        time.sleep(0.1)
        iframe_inner('.rc-anchor-content',timeout=1).click()
        self.dr.wait.ele_displayed("xpath://iframe[contains(@title, 'recaptcha')]",timeout=3)

        if self.isSolved():
            return
        iframe = self.dr("xpath://iframe[contains(@title, 'recaptcha')]")
        iframe('#recaptcha-audio-button',timeout=1).click()
        time.sleep(.3)
        src = iframe('#audio-source').attrs['src']
        path_to_mp3 = os.path.normpath(os.path.join((os.getenv("TEMP") if os.name=="nt" else "/tmp/")+ str(random.randrange(1,1000))+".mp3"))
        path_to_wav = os.path.normpath(os.path.join((os.getenv("TEMP") if os.name=="nt" else "/tmp/")+ str(random.randrange(1,1000))+".wav"))
        urllib.request.urlretrieve(src, path_to_mp3)
        sound = pydub.AudioSegment.from_mp3(path_to_mp3)
        sound.export(path_to_wav, format="wav")
        sample_audio = speech_recognition.AudioFile(path_to_wav)
        r = speech_recognition.Recognizer()
        
        with sample_audio as source:
            audio = r.record(source)
        key = r.recognize_google(audio)
        iframe('#audio-response').input(key.lower())
        time.sleep(0.1)
        iframe('#audio-response').input(Keys.ENTER)
        time.sleep(.4)
        if self.isSolved():
            return
        else:
            raise Exception()

    def isSolved(self):
        try:
            return "style" in self.dr.ele(".recaptcha-checkbox-checkmark",timeout=1).attrs
        except:
            return False
