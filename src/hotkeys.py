from pynput import keyboard


class HotkeyManager:

    def __init__(self, clicker):
        self.clicker = clicker

        self.listener = keyboard.Listener(
            on_press=self.on_press
        )

        self.listener.daemon = True
        self.listener.start()

    def on_press(self, key):

        try:

            if key == keyboard.Key.f6:
                self.clicker.toggle()

            elif key == keyboard.Key.esc:
                self.clicker.stop()

        except Exception:
            pass