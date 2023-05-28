"""LayoutWindow"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations
from PySide6.QtWidgets import QLabel, QLineEdit, QTextEdit, QVBoxLayout, \
    QHBoxLayout, QWidget


class LayoutWindow(BaseWindow):
    """
    A subclass of BaseWindow that provides layouts and widgets for a simple
    word processing application.

    This class adds a vertical layout to the QMainWindow and populates it
    with a QLabel, a QLineEdit, and a QTextEdit.
    The QLabel displays the current file name, the QLineEdit is used for
    entering search terms, and the QTextEdit is used for editing text.
    """

    def __init__(self):
        super().__init__()

        # Create widgets
        self.file_label = QLabel("No file selected")
        self.search_edit = QLineEdit()
        self.text_edit = QTextEdit()

        # Create layouts
        main_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        # Add widgets to layouts
        top_layout.addWidget(self.file_label)
        top_layout.addWidget(self.search_edit)
        bottom_layout.addWidget(self.text_edit)

        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)

        # Create central widget and set layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        # Set central widget
        self.setCentralWidget(central_widget)
