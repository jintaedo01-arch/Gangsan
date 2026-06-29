from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel,
    QPushButton, QGridLayout, QDoubleSpinBox,
)
from PySide6.QtCore import Qt


class MarginCalculatorPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(20)

        header = QVBoxLayout()
        header.setSpacing(4)
        title = QLabel("마진 계산기")
        title.setObjectName("pageTitle")
        subtitle = QLabel("수수료 및 배송비를 포함한 수익 마진을 계산합니다")
        subtitle.setObjectName("pageSubtitle")
        header.addWidget(title)
        header.addWidget(subtitle)
        layout.addLayout(header)

        content = QHBoxLayout()
        content.setSpacing(20)

        input_card = self._build_input_card()
        result_card = self._build_result_card()

        content.addWidget(input_card, 1)
        content.addWidget(result_card, 1)
        layout.addLayout(content)
        layout.addStretch()

    def _build_input_card(self) -> QFrame:
        card = QFrame()
        card.setObjectName("card")
        grid = QGridLayout(card)
        grid.setContentsMargins(24, 24, 24, 24)
        grid.setSpacing(16)

        fields = [
            ("원가 (₩)", "cost"),
            ("판매가 (₩)", "sell"),
            ("플랫폼 수수료 (%)", "fee"),
            ("배송비 (₩)", "shipping"),
        ]

        self.inputs = {}
        for i, (label_text, key) in enumerate(fields):
            lbl = QLabel(label_text)
            lbl.setObjectName("formLabel")

            spin = QDoubleSpinBox()
            spin.setObjectName("formInput")
            spin.setRange(0, 99_999_999)
            spin.setDecimals(0 if key != "fee" else 1)
            spin.setSuffix("" if key != "fee" else " %")
            spin.setGroupSeparatorShown(True)
            spin.valueChanged.connect(self._calculate)

            grid.addWidget(lbl, i * 2, 0)
            grid.addWidget(spin, i * 2 + 1, 0)
            self.inputs[key] = spin

        self.inputs["fee"].setValue(10.8)

        calc_btn = QPushButton("마진 계산")
        calc_btn.setObjectName("primaryButton")
        calc_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        calc_btn.clicked.connect(self._calculate)
        grid.addWidget(calc_btn, len(fields) * 2, 0)

        return card

    def _build_result_card(self) -> QFrame:
        card = QFrame()
        card.setObjectName("card")
        layout = QVBoxLayout(card)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(20)

        title = QLabel("계산 결과")
        title.setObjectName("cardTitle")
        layout.addWidget(title)

        self.result_labels = {}
        results = [
            ("gross_profit", "총 이익"),
            ("net_profit", "순이익"),
            ("margin_rate", "마진율"),
            ("roi", "투자수익률"),
        ]

        for key, label_text in results:
            row = QVBoxLayout()
            row.setSpacing(4)

            lbl = QLabel(label_text)
            lbl.setObjectName("formLabel")

            val = QLabel("—")
            val.setObjectName("cardValue")
            val.setStyleSheet("font-size: 22px;")

            row.addWidget(lbl)
            row.addWidget(val)
            layout.addLayout(row)
            self.result_labels[key] = val

        layout.addStretch()
        return card

    def _calculate(self):
        cost = self.inputs["cost"].value()
        sell = self.inputs["sell"].value()
        fee_pct = self.inputs["fee"].value()
        shipping = self.inputs["shipping"].value()

        if sell <= 0:
            for val in self.result_labels.values():
                val.setText("—")
            return

        gross = sell - cost
        fee_amount = sell * (fee_pct / 100)
        net = gross - fee_amount - shipping
        margin = (net / sell) * 100 if sell else 0
        roi = (net / cost) * 100 if cost > 0 else 0

        self.result_labels["gross_profit"].setText(f"₩{gross:,.0f}")
        self.result_labels["net_profit"].setText(f"₩{net:,.0f}")
        self.result_labels["margin_rate"].setText(f"{margin:.1f}%")
        self.result_labels["roi"].setText(f"{roi:.1f}%")
