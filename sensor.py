import speech_recognition as sr
import pyttsx3

# Initialize speech recognition and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to listen to user's speech
def listen_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        # Convert speech to text
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")

# Function to speak a response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to read sensor input
def read_sensor(sensor):
    # Read sensor value
    value = sensor.read()

    # Process the sensor value
    # ...

    # Return the processed value
    return value

# Main program loop
while True:
    # Listen to user's speech
    user_input = listen_speech()

    # Process user's speech and generate response
    if user_input:
        if user_input.lower() == "hello":
            speak("Hello! How can I assist you?")
        elif user_input.lower() == "how are you":
            speak("I'm an AI, so I don't have feelings, but thank you for asking.")
        elif user_input.lower() == "read sensor":
            # Assuming you have a sensor object initialized
            sensor_value = read_sensor(sensor)
            speak(f"The sensor value is {sensor_value}.")
        elif user_input.lower() == "exit":
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I don't have the information you requested.")