from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QGridLayout,
)
from PySide6.QtCore import Qt


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(24)

        header = self._build_header()
        layout.addLayout(header)

        cards = self._build_stat_cards()
        layout.addLayout(cards)

        recent = self._build_recent_activity()
        layout.addWidget(recent, 1)

    def _build_header(self) -> QVBoxLayout:
        header = QVBoxLayout()
        header.setSpacing(4)

        title = QLabel("대시보드")
        title.setObjectName("pageTitle")
        subtitle = QLabel("소싱 및 판매 현황을 한눈에 확인하세요")
        subtitle.setObjectName("pageSubtitle")

        header.addWidget(title)
        header.addWidget(subtitle)
        return header

    def _build_stat_cards(self) -> QGridLayout:
        grid = QGridLayout()
        grid.setSpacing(16)

        stats = [
            ("등록 상품", "128", "이번 주 +12"),
            ("평균 마진율", "34.2%", "전월 대비 +2.1%"),
            ("판매중 상품", "96", "검토 대기 32건"),
            ("AI 추천", "14", "신규 추천 3건"),
        ]

        for i, (label, value, change) in enumerate(stats):
            card = self._create_stat_card(label, value, change)
            grid.addWidget(card, 0, i)

        return grid

    def _create_stat_card(self, label: str, value: str, change: str) -> QFrame:
        card = QFrame()
        card.setObjectName("card")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(20, 18, 20, 18)
        card_layout.setSpacing(8)

        lbl = QLabel(label)
        lbl.setObjectName("cardTitle")

        val = QLabel(value)
        val.setObjectName("cardValue")

        chg = QLabel(change)
        chg.setObjectName("cardChange")

        card_layout.addWidget(lbl)
        card_layout.addWidget(val)
        card_layout.addWidget(chg)
        return card

    def _build_recent_activity(self) -> QFrame:
        card = QFrame()
        card.setObjectName("card")
        layout = QVBoxLayout(card)
        layout.setContentsMargins(24, 20, 24, 20)
        layout.setSpacing(12)

        title = QLabel("최근 작업내역")
        title.setObjectName("cardTitle")
        layout.addWidget(title)

        activities = [
            "도매 공급처 카탈로그에서 상품 5건 등록",
            "\"무선 이어폰 프로\" AI 분석 완료",
            "판매 목록 12건 마진 재계산",
            "가격 경쟁력 검토 대상 상품 3건 발견",
        ]

        for text in activities:
            row = QHBoxLayout()
            dot = QLabel("●")
            dot.setStyleSheet("color: #4361ee; font-size: 8px;")
            dot.setFixedWidth(16)

            lbl = QLabel(text)
            lbl.setStyleSheet("color: #4a4a68; font-size: 13px;")

            row.addWidget(dot)
            row.addWidget(lbl, 1)
            layout.addLayout(row)

        layout.addStretch()
        return card
