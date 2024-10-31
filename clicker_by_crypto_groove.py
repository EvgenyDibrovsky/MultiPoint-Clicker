import tkinter as tk
from pynput import mouse
import threading
import time
import keyboard
import win32api, win32con
import ctypes


class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.click_points = [None] * 8  # Список для хранения координат кликов
        self.running = False
        self.click_delay = 0.001  # Задержка между кликами по умолчанию (1 миллисекунда)
        self.setup_ui()
        self.setup_hotkeys()
        self.set_high_dpi_awareness()

    def setup_ui(self):
        self.root.title("MultiPoint Clicker")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        # Заголовок
        self.title_label = tk.Label(self.root, text="MultiPoint Clicker", font=("Helvetica", 16, "bold"), bg="black", fg="white")
        self.title_label.pack(pady=(20, 10))

        # Общий стиль для кнопок
        button_style = {
            "font": ("Helvetica", 12),
            "fg": "black",
            "activebackground": "#a3d432",  
            "relief": "raised",
            "bd": 2,
            "highlightthickness": 2,
            "highlightbackground": "#000000",
            "highlightcolor": "#3e8e41",
            "width": 10,
            "height": 2
        }
        
        # Кнопки для установки каждой из восьми точек клика (синие)
        self.set_buttons = []
        button_frame = tk.Frame(self.root, bg="black")
        button_frame.pack(pady=10)
        for i in range(8):
            button = tk.Button(button_frame, text=f"Click {i+1}", command=lambda i=i: threading.Thread(target=self.set_click_point, args=(i,)).start(), **button_style, bg="#007bff")
            button.grid(row=i // 4, column=i % 4, padx=10, pady=10)
            self.set_buttons.append(button)

        # Ползунок для регулировки скорости клика от 1 до 10000 миллисекунд
        self.speed_slider = tk.Scale(self.root, from_=1, to=10000, resolution=1, orient='horizontal', label="Click Speed (milliseconds)", length=460)
        self.speed_slider.set(self.click_delay * 1000)
        self.speed_slider.pack(pady=10)

        # Кнопки "Старт", "Стоп" и "Сброс" в ряд (зеленые и оранжевая)
        control_frame = tk.Frame(self.root, bg="black")
        control_frame.pack(pady=10)

        self.start_button = tk.Button(control_frame, text="Start clicker", command=self.start_clicker, **button_style, bg="#28a745")
        self.start_button.grid(row=0, column=0, padx=5)

        self.stop_button = tk.Button(control_frame, text="Stop clicker", command=self.stop_clicker, state=tk.DISABLED, **button_style, bg="#28a745")
        self.stop_button.grid(row=0, column=1, padx=5)
        
        self.reset_button = tk.Button(control_frame, text="Reset", command=self.reset_click_points, **button_style, bg="#ff8c00")
        self.reset_button.grid(row=0, column=2, padx=5)

        # Кредит
        self.credit_label = tk.Label(self.root, text="Developed by @edwebdev", font=("Helvetica", 10, "italic"), bg="black", fg="gray")
        self.credit_label.pack(pady=10)

    def setup_hotkeys(self):
        keyboard.add_hotkey('ctrl+alt+s', self.toggle_clicker)

    def toggle_clicker(self):
        if self.running:
            self.stop_clicker()
        else:
            self.start_clicker()

    def set_click_point(self, index):
        """Установить координаты точки клика, нажатие левой кнопки мыши сохраняет координаты"""
        def on_click(x, y, button, pressed):
            if pressed:
                scale_factor = self.get_display_scale()
                self.click_points[index] = (int(x * scale_factor), int(y * scale_factor))
                self.set_buttons[index].config(bg="red")  # Меняем цвет кнопки на красный, если координаты заданы
                print(f"Click {index + 1} set to: {self.click_points[index]}")
                listener.stop()
                return False

        listener = mouse.Listener(on_click=on_click)
        listener.start()
        listener.join()

    def reset_click_points(self):
        """Сброс всех заданных координат клика"""
        self.click_points = [None] * 8
        for button in self.set_buttons:
            button.config(bg="#007bff")  # Возвращаем кнопкам исходный цвет
        print("All click points reset")

    def start_clicker(self):
        """Запуск автокликера с заданными точками и скоростью"""
        self.running = True
        self.click_delay = self.speed_slider.get() / 1000  # Получение значения скорости клика в секундах
        threading.Thread(target=self.run_clicker, daemon=True).start()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_clicker(self):
        """Остановка автокликера"""
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def run_clicker(self):
        """Основной цикл для выполнения кликов по заданным точкам"""
        while self.running:
            for point in self.click_points:
                if point:  # Если точка задана, выполнить клик
                    self.click_mouse(*point)
                    time.sleep(self.click_delay)

    def click_mouse(self, x, y):
        """Функция для выполнения клика по координатам (x, y) с учетом масштабирования"""
        x, y = self.adjust_for_scaling(x, y)
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    def adjust_for_scaling(self, x, y):
        """Корректирует координаты с учетом масштабирования экрана"""
        scale_factor = self.get_display_scale()
        return int(x / scale_factor), int(y / scale_factor)

    def get_display_scale(self):
        """Возвращает коэффициент масштабирования дисплея для корректного определения координат"""
        user32 = ctypes.windll.user32
        hdc = user32.GetDC(0)
        dpi = ctypes.windll.gdi32.GetDeviceCaps(hdc, 88)  # LOGPIXELSX для ширины
        user32.ReleaseDC(0, hdc)
        return dpi / 96.0

    def set_high_dpi_awareness(self):
        """Устанавливает поддержку высокого DPI для Windows"""
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(2)  # Устанавливает DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2
        except Exception as e:
            print(f"Ошибка установки DPI: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClickerApp(root)
    root.mainloop()
