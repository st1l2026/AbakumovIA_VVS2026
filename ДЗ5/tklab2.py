import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk


class PaymentApp:
    CARD_TEMPLATE = "0000 0000 0000 0000"
    LOG_FILE = "transactions.txt"

    def __init__(self, root):
        self.root = root
        self.root.title("Форма оплаты и авторизации")
        self.root.geometry("520x420")
        self.root.minsize(500, 400)

        self.privacy_var = tk.BooleanVar()
        self.build_ui()

    def build_ui(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Политика безопасности", command=self.show_privacy)
        help_menu.add_separator()
        help_menu.add_command(label="Выход", command=self.root.quit)
        menu_bar.add_cascade(label="Помощь", menu=help_menu)

        frame = tk.Frame(self.root, padx=25, pady=25)
        frame.pack(fill="both", expand=True)
        frame.columnconfigure(1, weight=1)

        tk.Label(frame, text="Номер карты (16 цифр):", anchor="w").grid(row=0, column=0, sticky="we", pady=8)
        self.entry_card = tk.Entry(frame, font=("Arial", 11), fg="gray")
        self.entry_card.grid(row=0, column=1, sticky="we", pady=8, padx=(10, 0))
        self.entry_card.insert(0, self.CARD_TEMPLATE)
        self.entry_card.bind("<FocusIn>", self.on_card_focus_in)
        self.entry_card.bind("<FocusOut>", self.on_card_focus_out)
        self.entry_card.bind("<KeyPress>", self.on_card_key_press)
        self.entry_card.bind("<KeyRelease>", self.on_card_key_release)

        tk.Label(frame, text="Пароль приложения:", anchor="w").grid(row=1, column=0, sticky="we", pady=8)
        self.entry_password = tk.Entry(frame, font=("Arial", 11), show="*")
        self.entry_password.grid(row=1, column=1, sticky="we", pady=8, padx=(10, 0))

        tk.Label(frame, text="Платежная система:", anchor="w").grid(row=2, column=0, sticky="we", pady=8)
        self.combo_system = ttk.Combobox(
            frame,
            values=["MIR", "VISA", "Mastercard"],
            state="readonly",
            font=("Arial", 10),
        )
        self.combo_system.current(0)
        self.combo_system.grid(row=2, column=1, sticky="we", pady=8, padx=(10, 0))

        tk.Checkbutton(
            frame,
            text="Я принимаю настройки конфиденциальности",
            variable=self.privacy_var,
            anchor="w",
        ).grid(row=3, column=0, columnspan=2, sticky="we", pady=10)

        tk.Button(
            frame,
            text="Подтвердить операцию",
            bg="#27ae60",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.submit_form,
        ).grid(row=4, column=0, columnspan=2, sticky="we", pady=15)

        status_box = tk.LabelFrame(frame, text=" Статус транзакции ", padx=10, pady=10)
        status_box.grid(row=5, column=0, columnspan=2, sticky="we", pady=5)

        self.lbl_status = tk.Label(status_box, text="Ожидание ввода данных...", fg="gray", font=("Arial", 10))
        self.lbl_status.pack(anchor="w")

    def on_card_focus_in(self, event):
        if self.entry_card.get() == self.CARD_TEMPLATE:
            self.entry_card.delete(0, "end")
            self.entry_card.config(fg="black")

    def on_card_focus_out(self, event):
        if not self.entry_card.get().strip():
            self.entry_card.insert(0, self.CARD_TEMPLATE)
            self.entry_card.config(fg="gray")

    def on_card_key_press(self, event):
        if event.state & 0x4:
            return
        if event.char and not event.char.isdigit():
            return "break"

    def on_card_key_release(self, event):
        val = self.entry_card.get()
        if val == self.CARD_TEMPLATE:
            return
        digits = "".join(c for c in val if c.isdigit())[:16]
        formatted = " ".join(digits[i:i + 4] for i in range(0, len(digits), 4))
        if formatted != val:
            self.entry_card.delete(0, "end")
            self.entry_card.insert(0, formatted)
            self.entry_card.config(fg="black")
            self.entry_card.icursor(len(formatted))

    def get_card_digits(self):
        val = self.entry_card.get()
        if val == self.CARD_TEMPLATE:
            return ""
        return "".join(c for c in val if c.isdigit())

    def save_to_txt(self, system, masked_card):
        try:
            is_new = not os.path.exists(self.LOG_FILE)
            with open(self.LOG_FILE, "a", encoding="utf-8") as f:
                if is_new:
                    f.write("=" * 78 + "\n")
                    f.write("ЖУРНАЛ ТРАНЗАКЦИЙ\n")
                    f.write("Файл создаётся автоматически при подтверждении операции.\n")
                    f.write("=" * 78 + "\n")
                    f.write(f"{'Дата и время':<22} | {'Система':<16} | {'Карта':<22} | Статус\n")
                    f.write("-" * 78 + "\n")

                now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                f.write(f"{now:<22} | {system:<16} | {masked_card:<22} | Успешно\n")
            return True
        except Exception:
            return False

    def submit_form(self):
        card_num = self.get_card_digits()
        password = self.entry_password.get().strip()

        if not self.privacy_var.get():
            messagebox.showwarning("Внимание", "Вы должны принять условия конфиденциальности для продолжения!")
            return

        if len(card_num) != 16:
            messagebox.showerror("Ошибка ввода", "Некорректный номер карты! Он должен состоять строго из 16 цифр.")
            return

        if len(password) < 4:
            messagebox.showerror("Ошибка ввода", "Пароль слишком короткий! Введите не менее 4 символов.")
            return

        system = self.combo_system.get()
        masked = f"XXXX-XXXX-XXXX-{card_num[-4:]}"

        self.lbl_status.config(
            text=f"Данные успешно приняты!\nСистема: {system} | Карта: {masked}",
            fg="green",
            font=("Arial", 10, "bold"),
        )

        if self.save_to_txt(system, masked):
            messagebox.showinfo("Успех", f"Операция успешно обработана!\nЗапись добавлена в файл «{self.LOG_FILE}».")
        else:
            messagebox.showinfo(
                "Успех",
                f"Операция успешно обработана!\nНо журнал «{self.LOG_FILE}» обновить не удалось (нет прав на запись или файл занят)."
            )

    def show_privacy(self):
        messagebox.showinfo(
            "Политика конфиденциальности",
            "Ваши персональные данные шифруются и не передаются третьим лицам согласно стандарту PCI DSS."
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentApp(root)
    root.mainloop()
