import os
import sys
import json
import sqlite3
import webbrowser
# Disunic Corporation - 2022 All Rights Reserved
from PyQt5.QtGui import QFontDatabase, QIcon, QFont

from PyQt5.QtWidgets import QApplication
import Bin.main_window



# DB to open
connection = sqlite3.connect("BrowsingDatabase.db", check_same_thread=False)
# connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# Font
textFont = QFont("Times", 14)

if os.path.isfile("settings.json"):  # If settings file exists, then open it
    with open("settings.json", "r") as f:
        settings_data = json.load(f)
else:  # If settings not exists, then create a new file with default settings
    json_data = json.loads(
    """
    {
        "defaultSearchEngine": "Google",
        "startupPage": "https://disunicx.github.io",
        "newTabPage": "https://disunicx.github.io",
        "homeButtonPage": "https://disunicx.github.io"
    }
    """
    )
    with open("settings.json", "w") as f:
        json.dump(json_data, f, indent=2)
    with open("settings.json", "r") as f:
        settings_data = json.load(f)
        # ###########################

def main():
    gui_app = QApplication(sys.argv)

    # Disable shortcut in context menu
    gui_app.styleHints().setShowShortcutsInContextMenus(False)

    # Set the window name
    QApplication.setApplicationName("DisunicX")

    # Set the window icon
    QApplication.setWindowIcon(QIcon(os.path.join("VisualElements", "logos", "browser.ico")))

    # App styles
    # if os.path.isfile(os.path.join("styles", "styles.css")):
    #     with open(os.path.join("styles", "styles.css")) as f:
    #         gui_app.setStyleSheet(f.read())
    gui_app.setStyleSheet("""
                QPushButton#ContextMenuTriggerButn::menu-indicator {
  /* Hide context menu button dropdown icon */
  image: none;
}

QToolBar {
  background-color: white;
  border-bottom: none;
}

/* Style all contextmenus*/

/* Style right arrow of QMenu */

QMenu::right-arrow {
  /* image: url(VisualElements/right-arrow-context-menu.png); */ 
   height: 20px; 
   width: 20px;
}
QMenu{
  padding: 5px;
  background: rgb(255, 255, 255);
  border: 1px solid rgb(179, 179, 179);
  border-radius: 5px;
  color: red;
}

QMenu::item {
  /* Styling all context menus */
  background-color: rgb(255, 255, 255);
  padding-left: 10px;
  padding-right: 100px;
  padding-top: 10px;
  padding-bottom: 10px;
  width: 100px;
  color: rgb(0, 0, 0);
  border-radius: 8px;
  font-family: 
  -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}


/*
 The three dot menu 
*/

QMenu#ContextMenu,
QMenu#HelpMenu {
  /* border: 2px solid black; */
  /* font-family: sans-serif; */
  border-radius: 5px;
  border: 1px solid rgb(123, 123, 123);
  background: rgb(255, 255, 255);

}

QMenu#ContextMenu::item,
QMenu#HelpMenu::item {
  padding-right: 100px;
  padding-left: 28px;
  font-size: 12px;
  /* font-weight: 600; */
}

QMenu#ContextMenu::icon,
QMenu#HelpMenu::icon {
  padding-left: 40px;
}

QMenu#ContextMenu::separator {
  height: 1px;
  background-color: rgb(38, 38, 38);
  margin-left: 0%;
  margin-right: 0%;
}

QMenu#ContextMenu::item:selected,
QMenu#HelpMenu::item:selected {
  background-color: #e4e4e4;
}


/*
 Styling of toolip
*/

QToolTip {
  background-color: rgb(1, 1, 1);
  background-color: transparent;
  border-radius: 500px;
  color: white;
  font-weight: 600;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  padding: 6px 10px 6px 10px;
  border: 10px;
}

/* SSLinfo label */

QLabel#SSLIcon {
  /* ssl icon */
  border: 1px solid transparent;
  padding-left: 10px;
  padding-right: 10px;
  border-radius: 20px;
  width: 5px;
  height: 5px;
}

/* Button styling */

QPushButton#ContextMenuTriggerButn {
  /* Context menu button */
  border: 1px solid transparent;
  padding: 10px;
  border-radius: 16px;
  width: 10px;
  height: 10px;
  background-color: none;
  margin-left: 5px;
  margin-right: 5px;
  font-size: large;
}

QPushButton#back_btn {
  border: 1px solid transparent;
  padding: 10px;
  border-radius: 7px;
  width: 10px;
  height: 10px;
  background-color: none;
}

QPushButton#forward_butn {
  border: 1px solid transparent;
  padding: 10px;
  border-radius: 7px;
  width: 10px;
  height: 10px;
  background-color: none;
}

QPushButton#reload_butn {
  border: 1px solid transparent;
  padding: 10px;
  border-radius: 7px;
  width: 10px;
  height: 10px;
  background-color: none;
}

QPushButton#home_button {
  border: 1px solid transparent;
  padding: 10px;
  border-radius: 7px;
  width: 10px;
  height: 10px;
  background-color: none;
}

QPushButton#stop_butn {
  border: 1px solid transparent;
  padding: 10px;
  border-radius: 7px;
  width: 10px;
  height: 10px;
  background-color: none;
}

/*
* after hover
*/

QPushButton#stop_butn:hover {
  background-color: #dcdcdc;
}

QPushButton#back_btn:hover {
  background-color: #dcdcdc;
}

QPushButton#forward_butn:hover {
  background-color: #dcdcdc;
}

QPushButton#reload_butn:hover {
  background-color: #dcdcdc;
}

QPushButton#home_button:hover {
  background-color: #dcdcdc;
}

QPushButton#ContextMenuTriggerButn:hover {
  background-color: #dcdcdc;
}

/*
* after pressed
*/

QPushButton#stop_butn:pressed {
  background-color: #ebebeb;
}

QPushButton#back_btn:pressed {
  background-color: #ebebeb;
}

QPushButton#forward_butn:pressed {
  background-color: #ebebeb;
}

QPushButton#reload_butn:pressed {
  background-color: #ebebeb;
}

QPushButton#home_button:pressed {
  background-color: #ebebeb;
}

QPushButton#ContextMenuTriggerButn:pressed {
  background-color: #ebebeb;
}

    """)

    QFontDatabase.addApplicationFont(os.path.join("fonts", "fa-solid-900.ttf"))

    window = Bin.main_window.mainWindow()
    # app = QApplication([])
    
    sys.exit(gui_app.exec_())
