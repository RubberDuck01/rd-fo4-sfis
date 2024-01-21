import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rubber Duck's Simple FallUI Item Sorter")
        
        self.layout = QVBoxLayout()
        self.lblWelcome = QLabel("Welcome to Rubber Duck's Simple FallUI Item Sorter", self)
        self.lblWelcome.setGeometry(50, 20, 300, 15)
        self.setGeometry(100, 100, 800, 600)

        self.btnLoad = QPushButton("Load CSV", self)
        self.btnLoad.setGeometry(50, 50, 100, 30)

        self.lblLoadPath = QLabel("No CSV Loaded", self)
        self.lblLoadPath.setGeometry(200, 50, 150, 30)
        
        # self.button2 = QPushButton("Button 2", self)
        # self.button2.setGeometry(50, 100, 100, 30)

        # self.textbox1 = QLineEdit(self)
        # self.textbox1.setGeometry(200, 50, 150, 30)

        # self.textbox2 = QLineEdit(self)
        # self.textbox2.setGeometry(200, 100, 150, 30)


if __name__ == "__main__":
    print("Welcome to SFIS!")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
