
import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)


class GameKitWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GameKit")
        self.resize(1100, 700)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #15171c;
            }

            QLabel {
                color: #f0f0f0;
            }

            QPushButton {
                background-color: #22252c;
                color: #dcdfe6;
                border: none;
                padding: 12px;
                text-align: left;
                border-radius: 6px;
            }

            QPushButton:hover {
                background-color: #343944;
            }
        """)

        # Główny widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Główny układ
        main_layout = QHBoxLayout(central_widget)

        # Sidebar
        sidebar = QWidget()
        sidebar.setFixedWidth(220)
        sidebar.setStyleSheet(
            "background-color: #1c1f26;"
        )

        sidebar_layout = QVBoxLayout(sidebar)

        logo = QLabel("GAMEKIT")
        logo.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #7c9cff;
        """)

        sidebar_layout.addWidget(logo)

        library_button = QPushButton("Biblioteka")
        backlog_button = QPushButton("Do ogrania")
        completed_button = QPushButton("Ukończone")

        sidebar_layout.addWidget(library_button)
        sidebar_layout.addWidget(backlog_button)
        sidebar_layout.addWidget(completed_button)

        sidebar_layout.addStretch()

        # Główny panel
        content = QWidget()
        content_layout = QVBoxLayout(content)

        title = QLabel("Moja biblioteka")
        title.setStyleSheet("font-size: 32px;")

        subtitle = QLabel(
            "Twoje gry w jednym miejscu."
        )
        subtitle.setStyleSheet(
            "color: #9298a5; font-size: 14px;"
        )

        content_layout.addWidget(title)
        content_layout.addWidget(subtitle)
        content_layout.addStretch()

        # Dodanie elementów do głównego układu
        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)


app = QApplication(sys.argv)

window = GameKitWindow()
window.show()

sys.exit(app.exec())
