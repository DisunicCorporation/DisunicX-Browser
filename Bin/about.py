import os
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QDialogButtonBox,
    QDialog,
    QVBoxLayout,
    QLabel
)


class AboutDialog(QDialog):
    def __init__(self, parent=None, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.layout = QVBoxLayout()

        ok_btn = QDialogButtonBox.Ok
        self.button_box = QDialogButtonBox(ok_btn)

        self.init_ui()

    def init_ui(self):
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        # with open(os.path.join("styles", "about_style.css")) as f:
        #     self.button_box.button(QDialogButtonBox.Ok).setStyleSheet(f.read())

        logo = QLabel()
        pixmap = QPixmap(os.path.join("VisualElements", "logos", "browser.png"))
        pixmap = pixmap.scaled(80, 80)
        logo.setPixmap(pixmap)
        self.layout.addWidget(logo)

        title = QLabel("DisunicX Browser")
        title.setFont(QFont("-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif", 20))

        self.layout.addWidget(title)


        lbl1 = QLabel(
            '<center><p id="vr" style="color:blue;text-decoration: underline;font-size:17px;text-aling:center;font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Open Sans, Helvetica Neue, sans-serif;">Version - 1.0.5</p></center>'
            '<p id="vr" style="color:blue;font-size:15px;text-aling:center;font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Open Sans, Helvetica Neue, sans-serif;">Disunic Corporation - 2022 All Rights Reserved</p>'
        )
        lbl1.setFont(QFont("Times", 10))
        lbl1.setOpenExternalLinks(True)
        self.layout.addWidget(lbl1)

        # github_pg = QLabel(
        #     '<a style="color: #1064ff;font-sizw:25px;font-weight: 700;font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Open Sans, Helvetica Neue, sans-serif;" href="https://github.com/DisunicCorporation/DisunicX-Browser">Source Code</a>')

        # font = QFont("Font Awesome 5 Free Solid", 10)
        # github_pg.setFont(font)
        # github_pg.setOpenExternalLinks(True)
        # self.layout.addWidget(github_pg)

        for i in range(0, self.layout.count()):
            self.layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        self.layout.addWidget(self.button_box)

        self.setLayout(self.layout)

        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.resize(400, 250)
        self.setMaximumHeight(300)
        self.setMaximumWidth(500)
        self.setWindowTitle("About")
        self.setStyleSheet("""
                     QPushButton {
                        background-color: #2B5DD1;
                        color: #FFFFFF;
                        padding: 15px 20px 15px 20px ;
                        font: bold 14px;
                        border-radius: 3px;
                        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
                    }

                    /* QPushButton:hover {
                        background-color: #3769df;
                    }
                    QLabel{
                        color: #1064ff;
                        font-weight: 700;
                        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
                    } 
                    */
                    QLabel#vr{
                        text-decoration: underline;
                        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
                    }


        """)