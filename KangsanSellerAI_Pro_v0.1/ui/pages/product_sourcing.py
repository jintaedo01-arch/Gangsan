from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel,
    QLineEdit, QPushButton, QGridLayout,
)
from PySide6.QtCore import Qt


DUMMY_RESULT = {
    "상품명": "테스트 상품",
    "원가": "12000원",
    "판매가": "24900원",
    "예상마진": "7800원",
    "상태": "분석 완료",
}


class ProductSourcingPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(20)

        header = QVBoxLayout()
        header.setSpacing(4)
        title = QLabel("상품 소싱")
        title.setObjectName("pageTitle")
        subtitle = QLabel("상품 URL을 입력하고 AI 분석을 실행하세요")
        subtitle.setObjectName("pageSubtitle")
        header.addWidget(title)
        header.addWidget(subtitle)
        layout.addLayout(header)

        input_card = self._build_input_card()
        layout.addWidget(input_card)

        result_card = self._build_result_card()
        layout.addWidget(result_card)

        layout.addStretch()

    def _build_input_card(self) -> QFrame:
        card = QFrame()
        card.setObjectName("card")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(24, 20, 24, 20)
        card_layout.setSpacing(14)

        section_title = QLabel("상품 URL 입력")
        section_title.setObjectName("cardTitle")
        card_layout.addWidget(section_title)

        row = QHBoxLayout()
        row.setSpacing(10)

        self.url_input = QLineEdit()
        self.url_input.setObjectName("searchInput")
        self.url_input.setPlaceholderText("https://example.com/product/...")
        self.url_input.returnPressed.connect(self.analyze_product)

        self.analyze_button = QPushButton("상품 분석")
        self.analyze_button.setObjectName("searchButton")
        self.analyze_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.analyze_button.clicked.connect(self.analyze_product)

        row.addWidget(self.url_input, 1)
        row.addWidget(self.analyze_button)
        card_layout.addLayout(row)

        return card

    def _build_result_card(self) -> QFrame:
        card = QFrame()
        card.setObjectName("card")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(24, 20, 24, 24)
        card_layout.setSpacing(16)

        section_title = QLabel("분석 결과")
        section_title.setObjectName("cardTitle")
        card_layout.addWidget(section_title)

        grid = QGridLayout()
        grid.setHorizontalSpacing(24)
        grid.setVerticalSpacing(16)
        grid.setColumnStretch(1, 1)

        self.result_labels = {}
        fields = ["상품명", "원가", "판매가", "예상마진", "상태"]

        for row, field in enumerate(fields):
            name_lbl = QLabel(field)
            name_lbl.setObjectName("formLabel")

            value_lbl = QLabel("—")
            value_lbl.setObjectName("resultValue")
            value_lbl.setStyleSheet(
                "font-size: 15px; font-weight: 600; color: #1a1a2e;"
            )

            grid.addWidget(name_lbl, row, 0, Qt.AlignmentFlag.AlignTop)
            grid.addWidget(value_lbl, row, 1, Qt.AlignmentFlag.AlignTop)
            self.result_labels[field] = value_lbl

        card_layout.addLayout(grid)
        return card

    def analyze_product(self):
        result = DUMMY_RESULT
        for field, value in result.items():
            self.result_labels[field].setText(value)

        if result["상태"] == "분석 완료":
            self.result_labels["상태"].setStyleSheet(
                "font-size: 15px; font-weight: 600; color: #22c55e;"
            )
