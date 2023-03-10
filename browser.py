import sys
import tkinter as tk
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QWidget,QMainWindow

class PrivateBrowser(QWebEngineView):
    def __init__(self):
        super().__init__()
        profile = self.page().profile()
        profile.setHttpCacheType(QWebEngineProfile.NoCache)
        profile.setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)
        self.setUrl(QUrl("https://www.google.com"))
        self.show()
        
class MainWindow(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.browser = PrivateBrowser()
        self.url_bar = QLineEdit()
        self.go_button = QPushButton("Go")
        self.back_button = QPushButton("<-")
        self.forward_button = QPushButton("->")
        self.init_ui()
        
    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addwidget(self.browser)
        h_layout = QHBoxLayout()
        h_layout = addwidget(self.back_button)
        h_layout = addwidget(self.forward_button)
        h_layout = addwidget(self.url_bar)
        h_layout = addwidget(self.go_button)
        layout.addLayout(h_layout)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.go_button.clicked.connect(self.load_url)
        self.back_button.clicked.connect(self.browser.back)
        self.forward_button.clicked.connect(self.browser.forward)
        self.url_bar.returnPressed.connect(self.load_url)
        
    def load_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://"+ url
            
        self.browser.setUrl(QUrl(url))
        
if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

app = QApplication([])

# Create a QWebEngineView widget
web_view = QWebEngineView()
web_view.load(QUrl("http://www.google.com"))

# Create a QVBoxLayout
layout = QVBoxLayout()

# Add the web_view widget to the layout
layout.addWidget(web_view)

button_layout = QHBoxLayout()

back_button = QPushButton("Back")
back_button.clicked.connect(web_view.back)

forward_button = QPushButton("Forward")
forward_button.clicked.connect(web_view.forward)

button_layout.addWidget(back_button)
button_layout.addWidget(forward_button)

layout.addLayout(button_layout)

# Create a QWidget and set the layout
widget = QWidget()
widget.setLayout(layout)

# Show the widget
widget.show()

# Start the event loop
app.exec_()



class TabbedBrowser(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.tabs = {}
        self.current_tab = None

        # Create a notebook widget to hold the tabs
        self.notebook = tk.ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

    def add_tab(self, url):
        # Create a new tab and add it to the notebook
        tab = tk.Frame(self.notebook)
        self.notebook.add(tab, text="New Tab")
        self.notebook.select(tab)

        # Save the tab in a dictionary to keep track of it
        self.tabs[url] = tab
        self.current_tab = tab

    def switch_to_tab(self, url):
        # Show the selected tab
        tab = self.tabs[url]
        self.notebook.select(tab)
        self.current_tab = tab

if __name__ == "__main__":
    browser = TabbedBrowser()
    browser.add_tab("https://www.google.com")
    browser.mainloop()
