import random
import threading
import time
import pyautogui


class Clicker:
    def __init__(self):

        self.running = False
        self.thread = None

        self._interval_ms = 50
        self.random_percent = 10

        self.click_count = 0

    def set_interval(self, ms: int):
        try:
            ms = int(ms)
        except Exception:
            ms = 50

        if ms < 1:
            ms = 1
        elif ms > 60000:
            ms = 60000

        self._interval_ms = ms

    def get_interval(self):
        return self._interval_ms

    def start(self):
        if self.running:
            return

        self.running = True
        self.thread = threading.Thread(target=self._loop, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False

    def toggle(self):
        if self.running:
            self.stop()
        else:
            self.start()

    def _loop(self):
        while self.running:

            # intervalo base fijo
            base = self._interval_ms / 1000

            # variación controlada (NO exagerada)
            variation = base * (self.random_percent / 100)

            wait = random.uniform(
                max(0.05, base - variation),
                base + variation
            )

            # 🔥 IMPORTANTE: click primero o después no cambia estabilidad si el loop es consistente
            pyautogui.click()
            self.click_count += 1

            time.sleep(wait)