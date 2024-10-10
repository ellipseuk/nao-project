from naoqi import ALProxy

class NaoController:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.tts = ALProxy("ALTextToSpeech", self.ip, self.port)
        self.tts.setLanguage("English")
    
    def say(self, message):
        """Make NAO say a message."""
        self.tts.say(message)