from PySide6.QtWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('강산셀러 AI PRO v0.2')
        self.resize(1400,850)
        c=QWidget();self.setCentralWidget(c)
        h=QHBoxLayout(c)
        menu=QListWidget()
        menu.addItems(['🏠 대시보드','🔥 추천상품','🔍 상품소싱','💰 마진계산기','📦 상품관리','🤖 AI분석','⚙ 설정'])
        menu.setMaximumWidth(220)
        stack=QStackedWidget()
        d=QWidget();dv=QVBoxLayout(d);dv.addWidget(QLabel('<h1>강산셀러 AI PRO</h1>'));dv.addWidget(QLabel('v0.2'))
        s=QWidget();sv=QVBoxLayout(s);sv.addWidget(QLabel('<h2>상품 소싱</h2>'));e=QLineEdit();e.setPlaceholderText('도매 사이트 URL');sv.addWidget(e);sv.addWidget(QPushButton('상품 분석'));f=QFormLayout()
        [f.addRow(x,QLabel('-')) for x in ['상품명','브랜드','카테고리','원가','배송비','예상 판매가','예상 순마진','상태']]
        sv.addLayout(f);sv.addWidget(QPushButton('상품 저장'));sv.addStretch()
        for p in [d,s,QLabel('준비중'),QLabel('준비중'),QLabel('준비중'),QLabel('준비중')]:stack.addWidget(p)
        menu.currentRowChanged.connect(stack.setCurrentIndex);menu.setCurrentRow(0)
        h.addWidget(menu);h.addWidget(stack)
