"""ToolBar"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QToolBar, QLineEdit, QPushButton

from hackboard.pyside import minPol, hPol


class CustomToolBar(QToolBar):
  """ToolBar
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  signalTextTransmit = Signal(str)
  textChanged = Signal(str)
  _font = QFont()
  _font.setFamily('Consolas')
  _font.setPointSize(16)

  @classmethod
  def getFont(cls) -> QFont:
    """Getter-function for _font"""
    return cls._font

  def __init__(self, parent=None) -> None:
    super().__init__(parent)
    self.setAllowedAreas(Qt.ToolBarArea.TopToolBarArea)
    self.setOrientation(Qt.Orientation.Horizontal)
    self.lineEdit = QLineEdit()
    self.lineEdit.setSizePolicy(hPol)
    self.lineEdit.setMinimumHeight(32)
    self.lineEdit.setFont(self.getFont())
    self.pushButton2 = QPushButton("Reset")
    self.pushButton2.setSizePolicy(minPol)
    self.pushButton1 = QPushButton("Submit")
    self.pushButton1.setSizePolicy(minPol)
    self.addWidget(self.lineEdit)
    self.addWidget(self.pushButton1)
    self.addWidget(self.pushButton2)
    self.lineEdit.textEdited.connect(self.textChanged)
    self.pushButton2.clicked.connect(self.lineEdit.clear)
    self.pushButton1.clicked.connect(self.transmitText)

  def transmitText(self, ) -> NoReturn:
    """Resets the text in the line edit"""
    self.signalTextTransmit.emit(self.lineEdit.text())
