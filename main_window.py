from PyQt5 import QtWidgets, QtGui, QtCore
from game_field_window import GameWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("New Year Checkers ❄️🎄")

        # Немного увеличим окно
        self.resize(500, 600)

        # Новый год — снежно-голубой фон
        self.setStyleSheet("""
            QWidget {
                background-color: #e6f7ff; /* снежный фон */
            }

            QPushButton {
                background-color: #d32f2f; /* новогодний красный */
                color: white;
                font-size: 36px;
                font-weight: bold;
                border-radius: 20px;
                padding: 15px;
                border: 3px solid #ffffff;
            }

            QPushButton:hover {
                background-color: #f44336;
                border-color: #ffebee;
            }

            QPushButton:pressed {
                background-color: #b71c1c;
            }
        """)

        # Layout
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setSpacing(25)
        self.vertical_layout.setContentsMargins(80, 80, 80, 80)

        # Новогодние кнопки
        self.play_button = QtWidgets.QPushButton('🎁 Ойнау')
        self.play_button.clicked.connect(self.play_button_clicked)
        self.parameters_button = QtWidgets.QPushButton('⚙️ Параметрлер')
        self.best_button = QtWidgets.QPushButton('⭐ Үздіктер')
        self.exit_button = QtWidgets.QPushButton('⛄ Шығу')

        # Drop shadow (эффект тени под кнопками)
        for btn in [self.play_button, self.parameters_button, self.best_button, self.exit_button]:
            effect = QtWidgets.QGraphicsDropShadowEffect()
            effect.setBlurRadius(25)
            effect.setXOffset(0)
            effect.setYOffset(5)
            effect.setColor(QtGui.QColor(0, 0, 0, 120))
            btn.setGraphicsEffect(effect)
            self.vertical_layout.addWidget(btn)

        widget = QtWidgets.QWidget()
        widget.setLayout(self.vertical_layout)
        self.setCentralWidget(widget)

    def play_button_clicked(self):
        self.game_window = GameWindow(main_window=self)
        self.game_window.show()
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
