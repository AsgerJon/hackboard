"""LayoutWindow"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from PySide6.QtGui import QKeyEvent, QTextDocument, QTextCursor
from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout
from PySide6.QtWidgets import QHBoxLayout, QWidget, QPushButton
from worktoy.core import maybe

from hackboard.pyside import BaseWindow, DocWidget, CustomToolBar, LogWidget

wordStart = QTextCursor.MoveOperation.StartOfWord
wordEnd = QTextCursor.MoveOperation.EndOfWord
move = QTextCursor.MoveMode.MoveAnchor
mark = QTextCursor.MoveMode.KeepAnchor


class LayoutWindow(BaseWindow):
  """
  A subclass of BaseWindow that provides layouts and widgets for a simple
  word processing application.

  This class adds a vertical layout to the QMainWindow and populates it
  with a QLabel, a QLineEdit, and a QTextEdit.
  The QLabel displays the current file name, the QLineEdit is used for
  entering search terms, and the QTextEdit is used for editing text.
  """

  def __init__(self, parent: QWidget = None) -> None:
    BaseWindow.__init__(self, parent)

    # Create widgets
    self._baseHeaderWidget = QWidget()
    self._baseWidget = QWidget()
    self._toolBar = CustomToolBar()
    self.file_label = QLabel("No file selected")
    self.search_edit = QLineEdit()
    self._logWidget = LogWidget()
    self._logWidget.setMaximumWidth(240)

    self.documentWidget = DocWidget()
    self.debugButton = QPushButton()
    self._centralWidget = QWidget()

  def setupWidgets(self) -> NoReturn:
    """Sets up the widgets"""
    main_layout = QVBoxLayout()
    bottom_layout = QHBoxLayout()
    bottom_layout.addWidget(self.documentWidget)
    bottom_layout.addWidget(self._logWidget)
    main_layout.addWidget(self._toolBar)
    main_layout.addLayout(bottom_layout)
    self._centralWidget.setLayout(main_layout)
    self.setCentralWidget(self._centralWidget)

  def getDoc(self) -> QTextDocument:
    """Getter-function for the underlying document"""
    return self.documentWidget.getDocument()

  def getCursor(self) -> QTextCursor:
    """Getter-function for underlying text cursor"""
    return self.documentWidget.textCursor()

  def __iter__(self, ) -> QWidget:
    """Implementation of iteration"""
    self.getCursor().movePosition()
    return self

  def show(self) -> NoReturn:
    """Sets up the widgets before invoking the show super call"""
    self.setupWidgets()
    BaseWindow.show(self)

  def tellMe(self, msg: str) -> NoReturn:
    """Transmits the message to the log widget"""
    if maybe(msg):
      self._logWidget.tellMe(msg)

  def keyReleaseEvent(self, event: QKeyEvent) -> NoReturn:
    """Triggers spell checking"""
    BaseWindow.keyReleaseEvent(self, event)

  def keyPressEvent(self, event: QKeyEvent) -> NoReturn:
    """Triggers spell checking"""
    BaseWindow.keyPressEvent(self, event)
