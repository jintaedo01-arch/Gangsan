from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QHeaderView, QAbstractItemView,
)
from PySide6.QtCore import Qt


PRODUCTS = [
    ("SKU-001", "무선 이어폰 프로", "판매중", "29,900", "48", "쿠팡"),
    ("SKU-002", "LED 데스크 램프", "판매중", "19,800", "127", "스마트스토어"),
    ("SKU-003", "휴대용 블렌더", "임시저장", "34,900", "0", "—"),
    ("SKU-004", "프리미엄 요가 매트", "판매중", "18,500", "63", "쿠팡"),
    ("SKU-005", "휴대폰 거치대", "판매중지", "9,900", "22", "스마트스토어"),
]


class ProductManagementPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(20)

        header_row = QHBoxLayout()
        header = QVBoxLayout()
        header.setSpacing(4)
        title = QLabel("상품 관리")
        title.setObjectName("pageTitle")
        subtitle = QLabel("상품 카탈로그 및 판매 목록을 관리합니다")
        subtitle.setObjectName("pageSubtitle")
        header.addWidget(title)
        header.addWidget(subtitle)
        header_row.addLayout(header, 1)

        add_btn = QPushButton("+ 상품 등록")
        add_btn.setObjectName("primaryButton")
        add_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        header_row.addWidget(add_btn, alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addLayout(header_row)

        search_bar = QHBoxLayout()
        search_bar.setSpacing(10)

        self.search_input = QLineEdit()
        self.search_input.setObjectName("searchInput")
        self.search_input.setPlaceholderText("SKU, 상품명 또는 판매처로 검색...")
        self.search_input.returnPressed.connect(self._on_search)

        search_btn = QPushButton("검색")
        search_btn.setObjectName("searchButton")
        search_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        search_btn.clicked.connect(self._on_search)

        search_bar.addWidget(self.search_input, 1)
        search_bar.addWidget(search_btn)
        layout.addLayout(search_bar)

        table_card = QFrame()
        table_card.setObjectName("card")
        table_layout = QVBoxLayout(table_card)
        table_layout.setContentsMargins(0, 0, 0, 0)

        self.table = QTableWidget(len(PRODUCTS), 6)
        self.table.setHorizontalHeaderLabels([
            "SKU", "상품명", "상태", "판매가", "재고", "판매처",
        ])

        header_view = self.table.horizontalHeader()
        header_view.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header_view.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header_view.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header_view.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header_view.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header_view.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)

        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setShowGrid(False)

        for row, data in enumerate(PRODUCTS):
            for col, value in enumerate(data):
                item = QTableWidgetItem(value)
                item.setTextAlignment(
                    Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
                )
                self.table.setItem(row, col, item)
            self.table.setRowHeight(row, 44)

        table_layout.addWidget(self.table)
        layout.addWidget(table_card, 1)

    def _on_search(self):
        query = self.search_input.text().strip().lower()
        for row in range(self.table.rowCount()):
            match = not query
            if query:
                for col in range(self.table.columnCount()):
                    item = self.table.item(row, col)
                    if item and query in item.text().lower():
                        match = True
                        break
            self.table.setRowHidden(row, not match)
