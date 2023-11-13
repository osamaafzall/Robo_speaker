import os

if __name__ == '__main__':
    print("welcome to RoboSpeaker 1.1. Created by osama")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q":
            break
        command = f'''"PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');"'''
        os.system(command)

