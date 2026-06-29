from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('강산셀러 AI PRO v0.1')
        self.resize(1280,800)

        c=QWidget()
        self.setCentralWidget(c)
        layout=QHBoxLayout(c)

        menu=QListWidget()
        menu.addItems(['🏠 대시보드','🔍 상품소싱','💰 마진계산','📦 상품관리','🤖 AI분석','⚙ 설정'])
        menu.setMaximumWidth(220)

        stack=QStackedWidget()

        dash=QWidget()
        dv=QVBoxLayout(dash)
        dv.addWidget(QLabel('<h1>강산셀러 AI PRO</h1>'))
        dv.addWidget(QLabel('프로젝트 시작 화면'))

        src=QWidget()
        sv=QVBoxLayout(src)
        sv.addWidget(QLabel('<h2>상품 소싱</h2>'))
        e=QLineEdit()
        e.setPlaceholderText('도매 사이트 URL 입력')
        sv.addWidget(e)
        sv.addWidget(QPushButton('상품 분석'))
        f=QFormLayout()
        f.addRow('상품명',QLabel('-'))
        f.addRow('원가',QLabel('-'))
        f.addRow('예상 판매가',QLabel('-'))
        f.addRow('예상 순마진',QLabel('-'))
        sv.addLayout(f)
        sv.addStretch()

        for w in [dash,src,QLabel('준비중'),QLabel('준비중'),QLabel('준비중'),QLabel('준비중')]:
            stack.addWidget(w)

        menu.currentRowChanged.connect(stack.setCurrentIndex)
        menu.setCurrentRow(0)

        layout.addWidget(menu)
        layout.addWidget(stack)
