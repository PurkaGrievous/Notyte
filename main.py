
import sys

from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
)


class NotyteWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ==========================================
        # 1. KONFIGURACJA OKNA
        # ==========================================

        self.setWindowTitle("Notyte")
        self.resize(1100, 700)
        self.setWindowIcon(QIcon("logo.png"))

        # ==========================================
        # 2. GŁÓWNY WIDGET I LAYOUT
        # ==========================================

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)

        # ==========================================
        # 3. SIDEBAR
        # ==========================================

        sidebar = QWidget()
        sidebar.setFixedWidth(220)

        sidebar_layout = QVBoxLayout(sidebar)

        # ==========================================
        # 4. HEADER
        # ==========================================

        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(15, 15, 15, 15)
        search_input = QLineEdit()
        search_input.setPlaceholderText("Search your library...")

        header_layout.addWidget(search_input)

        # ==========================================
        # 5. MAIN CONTENT
        # ==========================================

        main_content = QWidget()
        main_content_layout = QVBoxLayout(main_content)

        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        right_layout.addWidget(header)
        right_layout.addWidget(main_content)

        # --- Przyciski nawigacji ---

        library_button = QPushButton("Library")
        backlog_button = QPushButton("Backlog")
        playing_button = QPushButton("Playing")
        completed_button = QPushButton("Completed")

        sidebar_layout.addWidget(library_button)
        sidebar_layout.addWidget(backlog_button)
        sidebar_layout.addWidget(playing_button)
        sidebar_layout.addWidget(completed_button)

        # --- Wolna przestrzeń ---

        sidebar_layout.addStretch()

        # TODO: Dodaj przycisk Settings na dole

        # --- Nagłówek ---

        # TODO: Dodaj tytuł panelu

        # --- Podtytuł ---

        # TODO: Dodaj podtytuł

        # --- Zawartość ---

        # TODO: Dodaj zawartość panelu

        # ==========================================
        # 5. POŁĄCZENIE LAYOUTÓW
        # ==========================================

        main_layout.addWidget(sidebar)
        main_layout.addWidget(right_panel)

        # ==========================================
        # 6. STYLE
        # ==========================================

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
            }

            QPushButton {
                background-color: #2d2d2d;
                border: none;
                border-radius: 8px;
                padding: 12px;
                text-align: left;
            }

            QPushButton:hover {
                background-color: #404040;
            }
        """)


# ==========================================
# 7. URUCHOMIENIE APLIKACJI
# ==========================================

app = QApplication(sys.argv)

window = NotyteWindow()
window.show()

sys.exit(app.exec())
