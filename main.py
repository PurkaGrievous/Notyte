
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

        # 1. Konfiguracja okna
        self.setWindowTitle("GameKit")
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

        # TODO: Ustaw szerokość sidebaru

        sidebar_layout = QVBoxLayout(sidebar)

        # TODO: Dodaj logo
        # TODO: Dodaj przyciski nawigacji
        # TODO: Dodaj odstęp na dole

        # 6. Główny panel
        content = QWidget()
        content_layout = QVBoxLayout(content)

        # TODO: Dodaj tytuł
        # TODO: Dodaj podtytuł
        # TODO: Dodaj zawartość panelu

        # 7. Połączenie elementów
        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)


# 8. Uruchomienie aplikacji
app = QApplication(sys.argv)

window = GameKitWindow()
window.show()

sys.exit(app.exec())
