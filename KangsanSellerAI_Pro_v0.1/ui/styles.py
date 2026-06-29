APP_STYLESHEET = """
QWidget {
    background-color: #f5f6f8;
    color: #1a1a2e;
    font-family: "Malgun Gothic", sans-serif;
    font-size: 13px;
}

/* ── Sidebar ── */
QFrame#sidebar {
    background-color: #ffffff;
    border-right: 1px solid #e8eaed;
}

QLabel#sidebarTitle {
    font-size: 18px;
    font-weight: 700;
    color: #1a1a2e;
    padding: 24px 20px 8px 20px;
}

QLabel#sidebarSubtitle {
    font-size: 11px;
    color: #8b8fa3;
    padding: 0px 20px 16px 20px;
}

QPushButton#navButton {
    background-color: transparent;
    border: none;
    border-radius: 8px;
    text-align: left;
    padding: 12px 16px;
    margin: 2px 12px;
    color: #4a4a68;
    font-size: 13px;
    font-weight: 500;
}

QPushButton#navButton:hover {
    background-color: #f0f2f5;
    color: #1a1a2e;
}

QPushButton#navButton:checked {
    background-color: #eef2ff;
    color: #4361ee;
    font-weight: 600;
}

/* ── Content area ── */
QFrame#contentArea {
    background-color: #f5f6f8;
}

QLabel#pageTitle {
    font-size: 24px;
    font-weight: 700;
    color: #1a1a2e;
    padding: 0;
    margin: 0;
}

QLabel#pageSubtitle {
    font-size: 13px;
    color: #8b8fa3;
    padding: 0;
    margin: 4px 0 0 0;
}

/* ── Cards ── */
QFrame#card {
    background-color: #ffffff;
    border: 1px solid #e8eaed;
    border-radius: 12px;
}

QLabel#cardTitle {
    font-size: 12px;
    font-weight: 600;
    color: #8b8fa3;
    letter-spacing: 0px;
}

QLabel#cardValue {
    font-size: 28px;
    font-weight: 700;
    color: #1a1a2e;
}

QLabel#cardChange {
    font-size: 12px;
    color: #22c55e;
    font-weight: 500;
}

/* ── Search bar ── */
QLineEdit#searchInput {
    background-color: #ffffff;
    border: 1px solid #dde1e7;
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 13px;
    color: #1a1a2e;
    min-height: 20px;
}

QLineEdit#searchInput:focus {
    border: 1px solid #4361ee;
    outline: none;
}

QLineEdit#searchInput::placeholder {
    color: #b0b4c3;
}

QPushButton#searchButton {
    background-color: #4361ee;
    color: #ffffff;
    border: none;
    border-radius: 8px;
    padding: 10px 24px;
    font-size: 13px;
    font-weight: 600;
    min-height: 20px;
}

QPushButton#searchButton:hover {
    background-color: #3a56d4;
}

QPushButton#searchButton:pressed {
    background-color: #2f47b8;
}

QPushButton#primaryButton {
    background-color: #4361ee;
    color: #ffffff;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 13px;
    font-weight: 600;
}

QPushButton#primaryButton:hover {
    background-color: #3a56d4;
}

QPushButton#secondaryButton {
    background-color: #ffffff;
    color: #4a4a68;
    border: 1px solid #dde1e7;
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 13px;
    font-weight: 500;
}

QPushButton#secondaryButton:hover {
    background-color: #f0f2f5;
    border-color: #c8cdd6;
}

/* ── Table ── */
QTableWidget {
    background-color: #ffffff;
    border: 1px solid #e8eaed;
    border-radius: 12px;
    gridline-color: #f0f2f5;
    selection-background-color: #eef2ff;
    selection-color: #1a1a2e;
    outline: none;
}

QTableWidget::item {
    padding: 8px 12px;
    border-bottom: 1px solid #f0f2f5;
}

QTableWidget::item:selected {
    background-color: #eef2ff;
}

QHeaderView::section {
    background-color: #fafbfc;
    color: #8b8fa3;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0px;
    padding: 10px 12px;
    border: none;
    border-bottom: 1px solid #e8eaed;
    border-right: 1px solid #f0f2f5;
}

QHeaderView::section:last {
    border-right: none;
}

/* ── Form inputs ── */
QLineEdit#formInput, QSpinBox#formInput, QDoubleSpinBox#formInput {
    background-color: #ffffff;
    border: 1px solid #dde1e7;
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 13px;
    min-height: 18px;
}

QLineEdit#formInput:focus, QSpinBox#formInput:focus, QDoubleSpinBox#formInput:focus {
    border: 1px solid #4361ee;
}

QLabel#formLabel {
    font-size: 12px;
    font-weight: 600;
    color: #4a4a68;
    margin-bottom: 4px;
}

QTextEdit#formTextArea {
    background-color: #ffffff;
    border: 1px solid #dde1e7;
    border-radius: 8px;
    padding: 10px;
    font-size: 13px;
}

QTextEdit#formTextArea:focus {
    border: 1px solid #4361ee;
}

QScrollBar:vertical {
    background: #f5f6f8;
    width: 8px;
    border-radius: 4px;
}

QScrollBar::handle:vertical {
    background: #c8cdd6;
    border-radius: 4px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover {
    background: #8b8fa3;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

QScrollBar:horizontal {
    background: #f5f6f8;
    height: 8px;
    border-radius: 4px;
}

QScrollBar::handle:horizontal {
    background: #c8cdd6;
    border-radius: 4px;
    min-width: 30px;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0;
}
"""
