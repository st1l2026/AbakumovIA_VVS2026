import os
import sys
from datetime import*
from PyQt6.QtCore import*
from PyQt6.QtGui import*
from PyQt6.QtWidgets import*


class PaymentApp(QMainWindow):
    LOG_FILE = "transactions.txt"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Форма оплаты и авторизации")
        self.setMinimumSize(500, 400)
        self.resize(520, 420)
        self.build_ui()

    def build_ui(self):
        menu_bar = self.menuBar()
        help_menu = menu_bar.addMenu("Помощь")

        privacy_action = QAction("Политика безопасности", self)
        privacy_action.triggered.connect(self.show_privacy)
        help_menu.addAction(privacy_action)

        help_menu.addSeparator()

        exit_action = QAction("Выход", self)
        exit_action.triggered.connect(self.close)
        help_menu.addAction(exit_action)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(15)

        form_layout = QFormLayout()
        form_layout.setSpacing(12)

        self.entry_card = QLineEdit()
        self.entry_card.setPlaceholderText("0000 0000 0000 0000")
        self.entry_card.setStyleSheet("font-size: 14px; padding: 4px;")
        self.entry_card.textChanged.connect(self.format_card_input)
        form_layout.addRow("Номер карты (16 цифр):", self.entry_card)

        self.entry_password = QLineEdit()
        self.entry_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.entry_password.setStyleSheet("font-size: 14px; padding: 4px;")
        form_layout.addRow("Пароль приложения:", self.entry_password)

        self.combo_system = QComboBox()
        self.combo_system.addItems(["MIR", "VISA", "Mastercard"])
        self.combo_system.setStyleSheet("font-size: 13px; padding: 4px;")
        form_layout.addRow("Платежная система:", self.combo_system)

        main_layout.addLayout(form_layout)

        self.privacy_check = QCheckBox("Я принимаю настройки конфиденциальности")
        main_layout.addWidget(self.privacy_check)

        self.submit_btn = QPushButton("Подтвердить операцию")
        self.submit_btn.setStyleSheet(
            "background-color: #27ae60; color: white; font-weight: bold; font-size: 13px; padding: 8px;"
        )
        self.submit_btn.clicked.connect(self.submit_form)
        main_layout.addWidget(self.submit_btn)

        status_box = QGroupBox("Статус транзакции")
        status_layout = QVBoxLayout(status_box)

        self.lbl_status = QLabel("Ожидание ввода данных...")
        self.lbl_status.setStyleSheet("color: gray; font-size: 13px;")
        self.lbl_status.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        status_layout.addWidget(self.lbl_status)

        main_layout.addWidget(status_box)
        main_layout.addStretch()

    def format_card_input(self, text):
        digits = "".join(c for c in text if c.isdigit())[:16]
        formatted = " ".join(digits[i:i + 4] for i in range(0, len(digits), 4))
        if formatted != text:
            self.entry_card.blockSignals(True)
            self.entry_card.setText(formatted)
            self.entry_card.setCursorPosition(len(formatted))
            self.entry_card.blockSignals(False)

    def get_card_digits(self):
        return "".join(c for c in self.entry_card.text() if c.isdigit())

    def save_to_txt(self, system, masked_card):
        try:
            is_new = not os.path.exists(self.LOG_FILE)
            with open(self.LOG_FILE, "a", encoding="utf-8") as f:
                if is_new:
                    f.write("Журнал транзакций\n")
                    f.write(f"{'Дата и время':<22} | {'Система':<16} | {'Карта':<22} | Статус\n")
                    f.write("-" * 78 + "\n")

                now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                f.write(f"{now:<22} | {system:<16} | {masked_card:<22} | Успешно\n")
            return True
        except Exception:
            return False

    def submit_form(self):
        card_num = self.get_card_digits()
        password = self.entry_password.text().strip()

        if not self.privacy_check.isChecked():
            QMessageBox.warning(self, "Внимание", "Вы должны принять условия конфиденциальности для продолжения!")
            return

        if len(card_num) != 16:
            QMessageBox.critical(self, "Ошибка ввода", "Некорректный номер карты! Он должен состоять строго из 16 цифр.")
            return

        if len(password) < 4:
            QMessageBox.critical(self, "Ошибка ввода", "Пароль слишком короткий! Введите не менее 4 символов.")
            return

        system = self.combo_system.currentText()
        masked = f"XXXX-XXXX-XXXX-{card_num[-4:]}"

        self.lbl_status.setText(f"Данные успешно приняты!\nСистема: {system} | Карта: {masked}")
        self.lbl_status.setStyleSheet("color: green; font-weight: bold; font-size: 13px;")

        if self.save_to_txt(system, masked):
            QMessageBox.information(
                self, "Успех", f"Операция успешно обработана!\nЗапись добавлена в файл «{self.LOG_FILE}»."
            )
        else:
            QMessageBox.information(
                self,
                "Успех",
                f"Операция успешно обработана!\nНо журнал «{self.LOG_FILE}» обновить не удалось (нет прав на запись или файл занят).",
            )

    def show_privacy(self):
        QMessageBox.information(
            self,
            "Политика конфиденциальности",
            "Ваши персональные данные шифруются и не передаются третьим лицам согласно стандарту PCI DSS.",
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PaymentApp()
    window.show()
    sys.exit(app.exec())
