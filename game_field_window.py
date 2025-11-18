from PyQt5 import QtWidgets, QtGui, QtCore


class GameWindow(QtWidgets.QMainWindow):
    def __init__(self, main_window=None):
        super().__init__()

        self.main_window = main_window

        self.setWindowTitle("Checkers – Game ❄️")
        self.resize(700, 800)

        # ===== СТИЛИ ОКНА =====
        self.setStyleSheet("""
            QWidget {
                background-color: #e6f7ff; /* снежный фон */
            }

            QPushButton {
                background-color: #d32f2f;
                color: white;
                font-size: 22px;
                border-radius: 12px;
                padding: 10px;
                border: 2px solid #fff;
            }

            QPushButton:hover {
                background-color: #f44336;
            }

            QPushButton:pressed {
                background-color: #b71c1c;
            }

            QLabel {
                font-size: 26px;
                font-weight: bold;
                color: #003366;
            }
        """)

        # === Основной виджет ===
        central = QtWidgets.QWidget()
        self.setCentralWidget(central)

        main_layout = QtWidgets.QVBoxLayout(central)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # ==============================
        #     ТАЙМЕРЫ ИНФОРМАЦИЯ
        # ==============================
        timers_layout = QtWidgets.QHBoxLayout()

        self.white_timer_label = QtWidgets.QLabel("⏱ Ақ: 05:00")
        self.black_timer_label = QtWidgets.QLabel("⏱ Қара: 05:00")

        timers_layout.addWidget(self.white_timer_label)
        timers_layout.addStretch()
        timers_layout.addWidget(self.black_timer_label)

        main_layout.addLayout(timers_layout)

        # Числа секунд
        self.white_time = 5 * 60
        self.black_time = 5 * 60

        # Активный игрок (white / black)
        self.active_player = "white"

        # Qt таймер
        self.turn_timer = QtCore.QTimer()
        self.turn_timer.timeout.connect(self.update_timers)
        self.turn_timer.start(1000)

        # ==============================
        #     ПОЛЕ ДЛЯ ШАШЕК
        # ==============================
        self.board_area = BoardWidget()
        main_layout.addWidget(self.board_area)

        # ==============================
        #     КНОПКИ УПРАВЛЕНИЯ
        # ==============================
        buttons_layout = QtWidgets.QHBoxLayout()

        self.surrender_btn = QtWidgets.QPushButton("⛔ Сдаться")
        self.surrender_btn.clicked.connect(self.surrender_btn_clicked)
        
        self.hint_btn = QtWidgets.QPushButton("💡 Подсказка")
        self.pause_btn = QtWidgets.QPushButton("⏸ Пауза")

        self.pause_btn.clicked.connect(self.toggle_pause)

        for b in (self.surrender_btn, self.hint_btn, self.pause_btn):
            buttons_layout.addWidget(b)

        main_layout.addLayout(buttons_layout)

    # ====================================================
    #                 ЛОГИКА ТАЙМЕРА ХОДА
    # ====================================================
    def update_timers(self):
        """Обновляет таймер активного игрока каждую секунду"""
        if self.active_player == "white":
            self.white_time -= 1
        else:
            self.black_time -= 1

        self.refresh_timer_labels()

    def refresh_timer_labels(self):
        """Преобразовать секунды в формат ММ:СС"""
        w_m = self.white_time // 60
        w_s = self.white_time % 60
        b_m = self.black_time // 60
        b_s = self.black_time % 60

        self.white_timer_label.setText(f"⏱ Ақ: {w_m:02d}:{w_s:02d}")
        self.black_timer_label.setText(f"⏱ Қара: {b_m:02d}:{b_s:02d}")

    def toggle_pause(self):
        """Пауза / продолжить игру"""
        if self.turn_timer.isActive():
            self.turn_timer.stop()
            self.pause_btn.setText("▶️ Продолжить")
        else:
            self.turn_timer.start()
            self.pause_btn.setText("⏸ Пауза")

    def surrender_btn_clicked(self):
        self.main_window.show()
        self.close()


# ====================================================
#             ЗАГЛУШКА ПОЛЯ ДЛЯ ШАШЕК
# ====================================================
class BoardWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()

        self.setFixedSize(600, 600)
        self.setStyleSheet("background-color: #ffffff; border: 4px solid #003366;")
        self.setFrameShape(QtWidgets.QFrame.Box)

    def paintEvent(self, event):
        """
        Простейшее рисование клетки 8×8.
        Можно позже заменить полной логикой игры.
        """
        painter = QtGui.QPainter(self)

        size = self.width() // 8
        colors = [QtGui.QColor("#c40000"), QtGui.QColor("#ffeecc")]

        for row in range(8):
            for col in range(8):
                painter.setBrush(colors[(row + col) % 2])
                painter.drawRect(col * size, row * size, size, size)
