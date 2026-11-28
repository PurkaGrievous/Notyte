
import sys

from PySide6.QtGui import QIcon, QPixmap, QPainter
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
    QFrame,
)


class BackgroundWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.background = QPixmap("background_image.png")

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.drawPixmap(
            self.rect(),
            self.background
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
        self.setMinimumSize(900, 600)

        # ==========================================
        # 2. GŁÓWNY WIDGET I LAYOUT
        # ==========================================

        central_widget = BackgroundWidget()
        self.setCentralWidget(central_widget)
        central_widget.setObjectName("central_widget")

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
        search_box = QFrame()
        search_box.setObjectName("search_box")
        search_box.setFixedHeight(46)

        search_layout = QHBoxLayout(search_box)

        search_layout.setContentsMargins(12, 0, 12, 0)
        search_layout.setSpacing(6)

        search_icon = QLabel()
        search_pixmap = QPixmap("search.png").scaled(
            16, 16,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        search_icon.setPixmap(search_pixmap)

        search_input = QLineEdit()
        search_input.setPlaceholderText("Search your library...")

        search_layout.addWidget(search_icon)
        search_layout.addWidget(search_input)
        header_layout.addWidget(search_box, 2)
        header_layout.addStretch(1)

        search_box.setObjectName("search_box")
        search_icon.setObjectName("search_icon")

        search_input.setStyleSheet("""
            QLineEdit {
                background-color: transparent;
                color: #F4F2FF;
                border: none;
                padding: 8px 0px;
                font-size: 14px;
        }
        """)

        search_box.setStyleSheet("""
            QFrame#search_box {
                background-color: #0B0B18;
                border: 1px solid #333451;
                border-radius: 23px;
            }

            QFrame#search_box:hover {
                border: 1px solid #6D4AFF;
            }

            QLabel#search_icon {
                background: transparent;
                border: none;
            }
        """)

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
        logo_title = QLabel("Notyte")
        logo_box = QWidget()
        logo_layout = QHBoxLayout(logo_box)
        logo_img = QPixmap("logo.png")
        logo_img = logo_img.scaled(
            40, 40,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        logo_label = QLabel()
        logo_label.setPixmap(logo_img)

        logo_layout.addWidget(logo_label)
        logo_layout.addWidget(logo_title)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setStyleSheet("""
            QFrame {
                background-color: #555555;
                border: none;
            }
        """)
        
        library_button = QPushButton("Library")
        backlog_button = QPushButton("Backlog")
        playing_button = QPushButton("Playing")
        completed_button = QPushButton("Completed")
        settings_button = QPushButton("Settings")

        for button in [
            library_button,
            backlog_button,
            playing_button,
            completed_button,
            settings_button,
        ]:
            button.setCursor(Qt.CursorShape.PointingHandCursor)

        sidebar_layout.addWidget(logo_box)
        sidebar_layout.addWidget(library_button)
        sidebar_layout.addWidget(backlog_button)
        sidebar_layout.addWidget(playing_button)
        sidebar_layout.addWidget(completed_button)
        sidebar_layout.addSpacing(15)
        sidebar_layout.addWidget(separator)
        sidebar_layout.addSpacing(15)
        sidebar_layout.addWidget(settings_button)

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
                color: white;
            }

            QPushButton {
                background-color: #292B4A;
                color: #F4F2FF;
                border: 1px solid #333451;
                border-radius: 8px;
                padding: 12px;
            }

            QPushButton:hover {
                background-color: #6D4AFF;
            }

            #central_widget {
                background-image: url("background_image.png");
                background-repeat: no-repeat;
                background-position: center;
            }
        """)


# ==========================================
# 7. URUCHOMIENIE APLIKACJI
# ==========================================

app = QApplication(sys.argv)

window = NotyteWindow()
window.show()

sys.exit(app.exec())
