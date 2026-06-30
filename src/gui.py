import customtkinter as ctk
from src.clicker import Clicker
from src.hotkeys import HotkeyManager

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AutoClickerApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.clicker = Clicker()
        self.hotkeys = HotkeyManager(self.clicker)

        self.title("🚂 AutoClick Pro")
        self.geometry("420x360")
        self.resizable(False, False)

        # =========================
        # STATUS
        # =========================
        self.status = ctk.CTkLabel(
            self,
            text="Estado: Detenido",
            font=("Arial", 18)
        )
        self.status.pack(pady=15)

        # =========================
        # BOTONES
        # =========================
        self.start_button = ctk.CTkButton(
            self,
            text="Iniciar",
            command=self.start_clicking
        )
        self.start_button.pack(pady=5)

        self.stop_button = ctk.CTkButton(
            self,
            text="Detener",
            command=self.stop_clicking
        )
        self.stop_button.pack(pady=5)

        # =========================
        # INTERVALO (VELOCIDAD)
        # =========================
        self.interval_label = ctk.CTkLabel(self, text="Intervalo (ms)")
        self.interval_label.pack(pady=(15, 5))

        self.interval_entry = ctk.CTkEntry(self)
        self.interval_entry.insert(0, "50")  # default
        self.interval_entry.pack()

        self.apply_button = ctk.CTkButton(
            self,
            text="Aplicar velocidad",
            command=self.apply_interval
        )
        self.apply_button.pack(pady=10)

        # iniciar loop UI
        self.update_ui()

    # =========================
    # CONTROL CLICKER
    # =========================
    def start_clicking(self):
        self.clicker.start()

    def stop_clicking(self):
        self.clicker.stop()

    def apply_interval(self):
        try:
            value = int(self.interval_entry.get())
            self.clicker.set_interval(value)
            self.status.configure(text=f"⚙️ Intervalo: {value} ms")
        except ValueError:
            self.status.configure(text="❌ Valor inválido")

    # =========================
    # UI LOOP
    # =========================
    def update_ui(self):

        if self.clicker.running:
            self.status.configure(
                text=f"🟢 Activo | Clicks: {self.clicker.click_count}"
            )
        else:
            self.status.configure(
                text=f"🔴 Detenido | Clicks: {self.clicker.click_count}"
            )

        self.after(100, self.update_ui)