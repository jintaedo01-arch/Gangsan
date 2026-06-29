from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel,
    QLineEdit, QPushButton, QTextEdit, QTableWidget,
    QTableWidgetItem, QHeaderView, QAbstractItemView,
)
from PySide6.QtCore import Qt


INSIGHTS = [
    ("무선 이어폰 프로", "높음", "시장 평균 대비 8% 저가 — 진입 적기"),
    ("휴대용 블렌더", "낮음", "포화된 카테고리 — 차별화 전략 필요"),
    ("프리미엄 요가 매트", "높음", "홈트레이닝 시장 성장 추세"),
    ("LED 데스크 램프", "보통", "안정적 수요 — 상품 키워드 최적화 권장"),
]


class AIAnalysisPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(20)

        header = QVBoxLayout()
        header.setSpacing(4)
        title = QLabel("AI 분석")
        title.setObjectName("pageTitle")
        subtitle = QLabel("AI 기반 상품 인사이트 및 시장 추천")
        subtitle.setObjectName("pageSubtitle")
        header.addWidget(title)
        header.addWidget(subtitle)
        layout.addLayout(header)

        search_bar = QHBoxLayout()
        search_bar.setSpacing(10)

        self.search_input = QLineEdit()
        self.search_input.setObjectName("searchInput")
        self.search_input.setPlaceholderText("상품 URL 또는 상품명을 입력하여 AI 분석을 실행하세요...")
        self.search_input.returnPressed.connect(self._on_analyze)

        analyze_btn = QPushButton("분석")
        analyze_btn.setObjectName("searchButton")
        analyze_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        analyze_btn.clicked.connect(self._on_analyze)

        search_bar.addWidget(self.search_input, 1)
        search_bar.addWidget(analyze_btn)
        layout.addLayout(search_bar)

        content = QHBoxLayout()
        content.setSpacing(20)

        table_card = QFrame()
        table_card.setObjectName("card")
        table_layout = QVBoxLayout(table_card)
        table_layout.setContentsMargins(0, 0, 0, 0)

        self.table = QTableWidget(len(INSIGHTS), 3)
        self.table.setHorizontalHeaderLabels([
            "상품", "기회 점수", "AI 추천",
        ])

        header_view = self.table.horizontalHeader()
        header_view.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header_view.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header_view.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setShowGrid(False)

        for row, (product, score, rec) in enumerate(INSIGHTS):
            for col, value in enumerate([product, score, rec]):
                item = QTableWidgetItem(value)
                item.setTextAlignment(
                    Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
                )
                self.table.setItem(row, col, item)
            self.table.setRowHeight(row, 44)

        table_layout.addWidget(self.table)
        content.addWidget(table_card, 3)

        detail_card = QFrame()
        detail_card.setObjectName("card")
        detail_layout = QVBoxLayout(detail_card)
        detail_layout.setContentsMargins(20, 20, 20, 20)
        detail_layout.setSpacing(12)

        detail_title = QLabel("분석 요약")
        detail_title.setObjectName("cardTitle")

        self.summary = QTextEdit()
        self.summary.setObjectName("formTextArea")
        self.summary.setReadOnly(True)
        self.summary.setPlaceholderText("상품을 선택하거나 분석을 실행하면 상세 내용이 표시됩니다...")
        self.summary.setText(
            "현재 시장 데이터 기준:\n\n"
            "• 마진 잠재력이 높은 상품 3건\n"
            "• 경쟁이 치열한 상품 1건\n"
            "• 홈트레이닝 카테고리 상승 추세\n\n"
            "새 분석을 실행하여 상품별 인사이트를 확인하세요."
        )

        detail_layout.addWidget(detail_title)
        detail_layout.addWidget(self.summary, 1)
        content.addWidget(detail_card, 2)

        layout.addLayout(content, 1)

        self.table.itemSelectionChanged.connect(self._on_selection_changed)

    def _on_analyze(self):
        query = self.search_input.text().strip()
        if query:
            self.summary.setText(
                f"분석 대상: {query}\n\n"
                "시장 수요: 보통 ~ 높음\n"
                "경쟁 수준: 보통\n"
                "권장 판매가: ₩24,900 ~ ₩29,900\n"
                "예상 마진: 52~58%\n\n"
                "추천: 적절한 차별화 전략으로 진입 가능한 상품입니다. "
                "독특한 패키징과 빠른 배송으로 경쟁력을 확보하세요."
            )

    def _on_selection_changed(self):
        rows = self.table.selectionModel().selectedRows()
        if not rows:
            return
        row = rows[0].row()
        product = self.table.item(row, 0).text()
        score = self.table.item(row, 1).text()
        rec = self.table.item(row, 2).text()
        self.summary.setText(
            f"상품: {product}\n"
            f"기회 점수: {score}\n\n"
            f"{rec}"
        )
