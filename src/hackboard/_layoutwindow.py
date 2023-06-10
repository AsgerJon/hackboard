"""LayoutWindow"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from PySide6.QtGui import QKeyEvent, QTextDocument, QTextCursor
from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QGridLayout
from PySide6.QtWidgets import QHBoxLayout, QWidget, QPushButton
from worktoy.core import maybe

from hackboard import BaseWindow
from hackboard.settings import headerStyle
from hackboard.workside import LogWidget, CoreWidget, Label

wordStart = QTextCursor.MoveOperation.StartOfWord
wordEnd = QTextCursor.MoveOperation.EndOfWord
move = QTextCursor.MoveMode.MoveAnchor
mark = QTextCursor.MoveMode.KeepAnchor


class LayoutWindow(BaseWindow):
  """A subclass of BaseWindow that provides layouts and widgets for a simple
  word processing application.

  This class adds a vertical layout to the QMainWindow and populates it
  with a QLabel, a QLineEdit, and a QTextEdit.
  The QLabel displays the current file name, the QLineEdit is used for
  entering search terms, and the QTextEdit is used for editing text."""

  def __init__(self, parent: QWidget = None) -> None:
    BaseWindow.__init__(self, parent)
    self._logWidget = None
    self._baseHeaderWidget = None
    self._baseWidget = None
    self._fileLabel = None
    self._searchEdit = None
    self._centralWidget = None
    self._baseGridLayout = None
    self._baseVerticalBoxLayout = None
    self._baseHorizontalBoxLayout = None

  def _createBaseVerticalLayout(self) -> NoReturn:
    """Creator-function for the vertical base layout"""
    self._baseVerticalBoxLayout = QVBoxLayout()

  def _getBaseVerticalBoxLayout(self) -> QVBoxLayout:
    """Getter-function for the vertical base layout"""
    if self._baseVerticalBoxLayout is None:
      self._createBaseVerticalLayout()
      return self._getBaseVerticalBoxLayout()
    if isinstance(self._baseVerticalBoxLayout, QVBoxLayout):
      return self._baseVerticalBoxLayout
    raise TypeError

  def _createBaseLayout(self) -> NoReturn:
    """Creator-function for the base layout"""
    self._baseGridLayout = QGridLayout()

  def _getBaseLayout(self) -> QGridLayout:
    """Getter-function for the base layout"""
    if self._baseGridLayout is None:
      self._createBaseLayout()
      return self._getBaseLayout()
    if isinstance(self._baseGridLayout, QGridLayout):
      return self._baseGridLayout

  def _createCentralWidget(self) -> NoReturn:
    """Creator-function for the central widget"""
    self._centralWidget = CoreWidget

  def _getCentralWidget(self) -> CoreWidget:
    """Getter-function for the central widget"""
    if self._centralWidget is None:
      self._createCentralWidget()
      return self._getCentralWidget()
    if isinstance(self._centralWidget, CoreWidget):
      return self._centralWidget

  def _createSearchEdit(self) -> NoReturn:
    """Creator-function for the search edit widget"""
    self._searchEdit = QLineEdit()

  def _getSearchEdit(self) -> QLineEdit:
    """Getter-function for the search edit line"""
    if self._searchEdit is None:
      self._createSearchEdit()
      return self._getSearchEdit()
    if isinstance(self._searchEdit, QLineEdit):
      return self._searchEdit
    raise TypeError

  def _createBaseHeaderWidget(self) -> NoReturn:
    """Creator-function for the header widget"""
    self._baseHeaderWidget = Label()
    headerStyle @ self._baseHeaderWidget

  def _getBaseHeaderWidget(self) -> CoreWidget:
    """Getter-function for the header widget"""
    if self._baseHeaderWidget is None:
      self._createBaseHeaderWidget()
      return self._getBaseHeaderWidget()
    if isinstance(self._baseHeaderWidget, CoreWidget):
      return self._baseHeaderWidget

  def _createBaseWidget(self) -> NoReturn:
    """Creator-function for the base widget"""
    self._baseWidget = CoreWidget()

  def _getBaseWidget(self) -> CoreWidget:
    """Getter-function for the base widget"""
    if self._baseWidget is None:
      self._createBaseWidget()
      return self._getBaseWidget()
    if isinstance(self._baseWidget, CoreWidget):
      return self._baseWidget

  def setupWidgets(self) -> NoReturn:
    """Sets up the widgets"""
    self._getBaseLayout().addWidget(self._getLogWidget(), 0, 0)

  def getDoc(self) -> QTextDocument:
    """Getter-function for the underlying document"""

  def getCursor(self) -> QTextCursor:
    """Getter-function for underlying text cursor"""

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

  def _createLogWidget(self) -> NoReturn:
    """Creator-function for the log widget"""
    self._logWidget = LogWidget

  def _getLogWidget(self) -> LogWidget:
    """Getter-function for the log widget"""
    if self._logWidget is None:
      self._createLogWidget()
      return self._getLogWidget()
    if isinstance(self._logWidget, LogWidget):
      return self._logWidget
    raise TypeError
