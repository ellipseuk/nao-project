from src.nao_controller import NaoController
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    # Fetch robot IP and port from environment variables
    robot_ip = os.getenv("ROBOT_IP")
    robot_port = int(os.getenv("ROBOT_PORT", 9559))

    # Create NAO controller object
    nao = NaoController(robot_ip, robot_port)

    # Example action: Make NAO say "Hello World"
    nao.say("Hello world!")

if __name__ == "__main__":
    main()