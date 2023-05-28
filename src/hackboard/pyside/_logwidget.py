"""LogWidget"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from PySide6.QtCore import Slot, QStringListModel, Qt, Signal
from PySide6.QtGui import QKeyEvent, QFont
from PySide6.QtWidgets import QListView, QVBoxLayout, QWidget

from hackboard.pyside.style import FontStyle


class LogWidget(QWidget):
  """LogWidget"""
  logUpdated = Signal()
  messageHighlighted = Signal(str)
  scrolled = Signal()

  signalTextTransmit = Signal(str)
  textChanged = Signal(str)
  _font = QFont()
  _font.setFamily('Consolas')
  _font.setPointSize(16)

  @classmethod
  def getFont(cls) -> QFont:
    """Getter-function for _font"""
    return cls._font

  def __init__(self, parent: QWidget = None):
    self._parent = parent
    super().__init__()
    self.setFont(FontStyle.getNormalFont())
    self.layout = QVBoxLayout()
    self.list_view = QListView()
    self.list_view.setFont(self.getFont())
    self.model = QStringListModel()
    self.list_view.setModel(self.model)
    self.list_view.setWordWrap(True)
    self.list_view.setTextElideMode(Qt.ElideNone)
    self.list_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.list_view.selectionModel().selectionChanged.connect(
      self.highlighted)
    self.list_view.verticalScrollBar().valueChanged.connect(self.scrolled)
    self.layout.addWidget(self.list_view)
    self.setLayout(self.layout)

  @Slot(str)
  def tellMe(self, message: str) -> NoReturn:
    """LOL"""
    if not message:
      return
    row_count = self.model.rowCount()
    self.model.insertRow(row_count)
    index = self.model.index(row_count)
    self.model.setData(index, message)
    self.logUpdated.emit()

  @Slot()
  def highlighted(self):
    selected_indexes = self.list_view.selectedIndexes()
    if selected_indexes:
      selected_message = selected_indexes[0].data()
      self.messageHighlighted.emit(selected_message)

  @Slot()
  def scrolled(self):
    self.scrolled.emit()

  def keyPressEvent(self, event: QKeyEvent) -> NoReturn:
    """Transmits certain events to the parent"""
    key = event.key()
    if Qt.Key.Key_F1 <= key <= Qt.Key.Key_F35 and self._parent is not None:
      self._parent.keyPressEvent(event)

  def keyReleaseEvent(self, event: QKeyEvent) -> NoReturn:
    """Transmits certain events to the parent"""
    key = event.key()
    if Qt.Key.Key_F1 <= key <= Qt.Key.Key_F35 and self._parent is not None:
      self._parent.keyReleaseEvent(event)
