from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QFrame,
    QPushButton, QLabel, QStackedWidget, QButtonGroup,
)
from PySide6.QtCore import Qt

from ui.styles import APP_STYLESHEET
from ui.pages.dashboard import DashboardPage
from ui.pages.product_sourcing import ProductSourcingPage
from ui.pages.margin_calculator import MarginCalculatorPage
from ui.pages.product_management import ProductManagementPage
from ui.pages.ai_analysis import AIAnalysisPage


NAV_ITEMS = [
    ("대시보드", DashboardPage),
    ("상품 소싱", ProductSourcingPage),
    ("마진 계산기", MarginCalculatorPage),
    ("상품 관리", ProductManagementPage),
    ("AI 분석", AIAnalysisPage),
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("강산셀러 AI PRO v0.1")
        self.resize(1400, 800)
        self.setMinimumSize(1200, 700)
        self.setStyleSheet(APP_STYLESHEET)

        central = QWidget()
        self.setCentralWidget(central)

        root = QHBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        sidebar = self._build_sidebar()
        content = self._build_content()

        root.addWidget(sidebar)
        root.addWidget(content, 1)

    def _build_sidebar(self) -> QFrame:
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(240)

        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        title = QLabel("강산셀러 AI")
        title.setObjectName("sidebarTitle")

        subtitle = QLabel("PRO v0.1")
        subtitle.setObjectName("sidebarSubtitle")

        layout.addWidget(title)
        layout.addWidget(subtitle)

        separator = QFrame()
        separator.setFixedHeight(1)
        separator.setStyleSheet("background-color: #e8eaed; margin: 0 16px;")
        layout.addWidget(separator)
        layout.addSpacing(8)

        self.nav_group = QButtonGroup(self)
        self.nav_group.setExclusive(True)

        for i, (label, _) in enumerate(NAV_ITEMS):
            btn = QPushButton(f"  {label}")
            btn.setObjectName("navButton")
            btn.setCheckable(True)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(lambda checked, idx=i: self._switch_page(idx))
            self.nav_group.addButton(btn, i)
            layout.addWidget(btn)

        layout.addStretch()

        footer = QLabel("  © 2026 강산셀러")
        footer.setStyleSheet("color: #b0b4c3; font-size: 11px; padding: 16px 20px;")
        layout.addWidget(footer)

        return sidebar

    def _build_content(self) -> QFrame:
        content = QFrame()
        content.setObjectName("contentArea")

        layout = QVBoxLayout(content)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.stack = QStackedWidget()
        for _, page_cls in NAV_ITEMS:
            self.stack.addWidget(page_cls())

        layout.addWidget(self.stack)

        self.nav_group.button(0).setChecked(True)
        self.stack.setCurrentIndex(0)

        return content

    def _switch_page(self, index: int):
        self.stack.setCurrentIndex(index)
