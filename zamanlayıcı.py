import tkinter as tk
from tkinter import messagebox
import winsound

class StudyTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ders Çalışma Zamanlayıcı")
        self.root.configure(bg="black")

        self.timer_label = tk.Label(root, text="00:00", font=("Helvetica", 72), fg="white", bg="black")
        self.timer_label.pack(expand=True)

        self.duration_label = tk.Label(root, text="Süre:", font=("Helvetica", 18), fg="white", bg="black")
        self.duration_label.pack(expand=True)

        self.duration_entry = tk.Entry(root, font=("Helvetica", 18), bg="white")
        self.duration_entry.pack(expand=True, fill=tk.BOTH)

        self.start_button = tk.Button(root, text="Başlat", command=self.start_timer, font=("Helvetica", 18), bg="white", fg="black")
        self.start_button.pack(expand=True, fill=tk.BOTH)

        self.stop_button = tk.Button(root, text="Durdur", command=self.stop_timer, font=("Helvetica", 18), bg="white", fg="black")
        self.stop_button.pack(expand=True, fill=tk.BOTH)

        self.resume_button = tk.Button(root, text="Devam Et", command=self.resume_timer, font=("Helvetica", 18), bg="white", fg="black", state=tk.DISABLED)
        self.resume_button.pack(expand=True, fill=tk.BOTH)

        self.reset_button = tk.Button(root, text="Sıfırla", command=self.reset_timer, font=("Helvetica", 18), bg="white", fg="black")
        self.reset_button.pack(expand=True, fill=tk.BOTH)

        self.time_left = 0
        self.paused_time = 0
        self.timer_running = False

    def start_timer(self):
        if not self.timer_running:
            try:
                self.time_left = int(self.duration_entry.get()) * 60
                self.timer_running = True
                self.update_timer()
                self.start_button.config(state=tk.DISABLED)
                self.stop_button.config(state=tk.NORMAL)
            except ValueError:
                messagebox.showerror("Hata", "Geçerli bir dakika sayısı girin.")

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.paused_time = self.time_left
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.resume_button.config(state=tk.NORMAL)

    def resume_timer(self):
        if not self.timer_running:
            self.time_left = self.paused_time
            self.timer_running = True
            self.update_timer()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.resume_button.config(state=tk.DISABLED)

    def reset_timer(self):
        self.timer_running = False
        self.time_left = 0
        self.paused_time = 0
        self.timer_label.config(text="00:00")
        self.duration_entry.delete(0, tk.END)
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.resume_button.config(state=tk.DISABLED)

    def update_timer(self):
        if self.timer_running:
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            time_string = f"{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=time_string)

            if self.time_left > 0:
                self.time_left -= 1
                self.root.after(1000, self.update_timer)  # Her 1 saniyede bir güncelle
            else:
                self.timer_running = False
                messagebox.showinfo("Zamanlayıcı", "Süre doldu!")
                self.start_button.config(state=tk.NORMAL)
                self.stop_button.config(state=tk.DISABLED)
                self.resume_button.config(state=tk.DISABLED)
                winsound.Beep(1000, 500)  # Zil sesi

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="black")
    root.geometry("400x400")
    app = StudyTimerApp(root)
    root.mainloop()
