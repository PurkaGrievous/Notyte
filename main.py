
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
)


class NonyteWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 1. Konfiguracja okna
        self.setWindowTitle("Notyte")
        self.resize(1100, 700)

        # 2. Style aplikacji
        self.setStyleSheet("""
            
        """)

        # 3. Główny widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 4. Główny układ
        main_layout = QHBoxLayout(central_widget)

        
        # 5. Sidebar
        sidebar = QWidget()
        sidebar.setFixedWidth(220)

        sidebar.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
            }
        """)

        sidebar_layout = QVBoxLayout(sidebar)

        libraryButton = QPushButton("Library")
        backlogButton = QPushButton("Backlog")
        playingButton = QPushButton("Playing")
        completedButton = QPushButton("Completed")
        sidebar_layout.addWidget(libraryButton)
        sidebar_layout.addWidget(backlogButton)
        sidebar_layout.addWidget(playingButton)
        sidebar_layout.addWidget(completedButton)

        sidebar.setStyleSheet("""
        QPushButton {
            background-color: #2d2d2d;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 12px;
            text-align: left;
        }

        QPushButton:hover {
            background-color: #404040;
        }
        """)

        # Wolne miejsce pod przyciskami
        sidebar_layout.addStretch()

        # TODO: Ustaw szerokość sidebaru

        # TODO: Dodaj przyciski nawigacji
        # TODO: Dodaj odstęp na dole

        # 6. Główny panel
        content = QWidget()
        content_layout = QVBoxLayout(content)

        content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # TODO: Dodaj tytuł
        title_layout = QHBoxLayout()
        title = QLabel("NONYTE - Your Gaming Copilot")
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: white;
            margin: auto;
        """)

        title_layout.addStretch()
        title_layout.addWidget(title)
        title_layout.addStretch()
        content_layout.addLayout(title_layout)
        
        # TODO: Dodaj podtytuł
        # TODO: Dodaj zawartość panelu

        # 7. Połączenie elementów
        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)


# 8. Uruchomienie aplikacji
app = QApplication(sys.argv)

window = NonyteWindow()
window.setWindowIcon(QIcon("logo.png"))
window.show()

sys.exit(app.exec())
