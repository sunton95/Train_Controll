# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-03-17
# =============================================================================
""""""
# =============================================================================
# Imports
import sys
from ui_pyQT.Widget_switch import *
# =============================================================================

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Testing UI")
        width = 800
        height = 480
        self.setFixedWidth(width)
        self.setFixedHeight(height)

        self.label = QLabel(self)
        self.centralWidget = self.label
        self.setCentralWidget(self.centralWidget)

        self.layout = QHBoxLayout(self.centralWidget)
        self.layout.addWidget(windowLayout(self))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    #win.show()
    win.showFullScreen() 
    sys.exit(app.exec_())