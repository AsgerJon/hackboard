"""MainWindow"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from PySide6.QtGui import QKeyEvent, QTextCursor

from hackboard import InputWindow


class MainWindow(InputWindow):
  """MainWindow
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  def __init__(self, ) -> None:
    InputWindow.__init__(self)
    self.setMinimumWidth(640)
    self.setMinimumHeight(480)
    self._documentWidget = None

  def getCursor(self) -> QTextCursor:
    """Getter-function for QTextCursor"""
    raise NotImplementedError

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

  def debugFunc01(self) -> NoReturn:
    """Inserts lorem ipsum to the document widget"""
    print('debugFunc01')
    self.tellMe('DebugFunc01')

  def debugFunc02(self) -> NoReturn:
    """Debugger"""
    print('debugFunc02')
