"""MainWindow"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent, QTextCursor
from loremify import lorem
from worktoy.typetools import Any

from hackboard.pyside import InputWindow


class MainWindow(InputWindow):
  """MainWindow
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  def __init__(self, ) -> None:
    InputWindow.__init__(self)
    self.setMinimumWidth(640)
    self.setMinimumHeight(480)
    self._toolBar.signalTextTransmit.connect(self._logWidget.tellMe)
    self._cursor = QTextCursor(self.documentWidget.document())

  def getCursor(self) -> QTextCursor:
    """Getter-function for QTextCursor"""
    return QTextCursor(self.documentWidget.document())

  def debugFunc01(self) -> NoReturn:
    """Inserts lorem ipsum to the document widget"""
    print('debugFunc01')
    self.tellMe('DebugFunc01')
    self.documentWidget.insertPlainText(lorem())

  def debugFunc02(self) -> NoReturn:
    """Debugger"""
    print('debugFunc02')
    self._logWidget.tellMe('block count: %s' % self._cursor)

  def iterateWords(self) -> Any:
    """"""

  def show(self) -> NoReturn:
    """Reimplementation"""
    InputWindow.show(self)
    self.setWindowTitle('HackBoard')

  def keyReleaseEvent(self, event: QKeyEvent) -> NoReturn:
    """Triggers spell checking"""
    InputWindow.keyReleaseEvent(self, event)
    # if event.key() == Qt.Key.Key_Space:
    #   self.spaceKeyRelease.emit()

  def keyPressEvent(self, event: QKeyEvent) -> NoReturn:
    """Triggers spell checking"""
    InputWindow.keyPressEvent(self, event)
