"""DocWidget"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent, QTextDocument
from PySide6.QtWidgets import QPlainTextEdit
from icecream import ic

from hackboard.pyside.style import FontStyle

ic.configureOutput(includeContext=True)


class DocWidget(QPlainTextEdit):
  """Document Widget"""

  def __init__(self, parent=None) -> None:
    self._parent = parent
    QPlainTextEdit.__init__(self, parent)

  def getDocument(self) -> QTextDocument:
    """Getter-function for the underlying document"""
    return self.document()

  def keyPressEvent(self, event: QKeyEvent) -> NoReturn:
    """Transmits certain events to the parent"""
    QPlainTextEdit.keyPressEvent(self, event)
    key = event.key()
    if Qt.Key.Key_F1 <= key <= Qt.Key.Key_F35 and self._parent is not None:
      self._parent.keyPressEvent(event)

  def keyReleaseEvent(self, event: QKeyEvent) -> NoReturn:
    """Transmits certain events to the parent"""
    QPlainTextEdit.keyReleaseEvent(self, event)
    key = event.key()
    if Qt.Key.Key_F1 <= key <= Qt.Key.Key_F35 and self._parent is not None:
      self._parent.keyReleaseEvent(event)
