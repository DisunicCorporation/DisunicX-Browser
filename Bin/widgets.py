import os
import webbrowser

from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QLabel, QLineEdit, QTabWidget ,QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap # QFont
from PyQt5 import QtCore


class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setFocus()
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(4)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.setGraphicsEffect(self.shadow)


    # def mousePressEvent(self, e):
        # self.selectAll()
        # self.setCursor(pointer)

    def initAddressBar(self):
        # Set the placeholder text
        self.setPlaceholderText("Search Or Enter Web Address")

        # Set focus to the address bar
        self.setFocus()
        # with open(os.path.join("styles", "addr_bar.css")) as f:
        #     self.setStyleSheet(f.read())
        self.setStyleSheet("""
            QLineEdit{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            padding-top:4px;
            padding-left:8px;
            padding-bottom:4px;
            border:2px solid transparent;
            border-radius: 5px;
            font-size:15px;
            background-color: #fffefe;
            font-weight: 500;
            color: black;
            height: 22px;
            }

            QLineEdit:focus{
                border-color:#52a2f8;
                background: white;
            }

            QLineEdit:hover{
                border-color:#208bfd;
            }
            """)
        


class SSLIcon(QLabel):
    def __init__(self):
        super().__init__()
        self.InitSSLIcon()

    def InitSSLIcon(self):
        self.setObjectName("SSLIcon")
        icon = QPixmap(os.path.join("VisualElements", "lock-icon.png"))
        self.setPixmap(icon)


class Tabs(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setDocumentMode(True)

        # Set the tabs closable
        self.setTabsClosable(True)

        # Set the tabs movable
        self.setMovable(True)

        self.setFocus(True)

        # Add font family
        # font = QFont("Segoe UI", 8)
        # self.setFont(font)

        # Add some styles to the tabs
        # with open(
        #     os.path.join("styles", "tab_style.css")
        # ) as f:  # Open tab_styles.css file
        #     self.setStyleSheet(f.read())
        self.setStyleSheet("""
            QTabBar{
    background-color: white;
    border-bottom: none;
}

QTabBar::tab {
    color: #000000;
    text-align: left;
    margin-left: 4px;
    font-size: 11px;
    padding: 12px;
    margin-bottom: 0px;
    color: rgb(0, 0, 0);
    border-bottom: none;
    background: rgb(247, 247, 247);
    max-width: 400px;
    border-radius: 4px;
    margin-top:10px;
}

QTabBar::close-button {                         /* style the tab close button */
    image: url(./VisualElements/icons/closetabbutton.png);
    subcontrol-position: right;
    border: 0px solid gray;
    border-radius:3px;
    color: blue;
    background: gray;
    margin-left: 3px;
    
}

QTabBar::close-button:hover{                    /* close button hover */
    background-color: #1c76d7;
}

QTabBar::tab:hover{
    background-color: rgb(175, 175, 175);
    color: rgb(0, 0, 0);
}
QTabBar::tab:selected:hover{
    background-color: rgb(175, 175, 175);
    color: rgb(0, 0, 0);
}


QTabBar::tab:selected{                          /* selected tabs */
    background-color: rgb(218, 218, 218);
    color: rgb(0, 0, 0);
}


        """)


class customWebEnginePage(QWebEnginePage):
    def createWindow(self, _type):
        page = customWebEnginePage(self)
        page.urlChanged.connect(self.on_url_changed)
        return page

    @QtCore.pyqtSlot(QtCore.QUrl)
    def on_url_changed(self, url):
        page = self.sender()
        self.setUrl(url)
        page.deleteLater()
