from naoqi import ALProxy
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    # Coonect to the robot
    robot_ip = os.getenv("ROBOT_IP")
    robot_port = int(os.getenv("ROBOT_PORT", 9559))

    # Create a proxy to ALTextToSpeech
    tts = ALProxy("ALTextToSpeech", robot_ip, robot_port)

    # Say a test message
    tts.say("Hello world!")

if __name__ == "__main__":
    main()