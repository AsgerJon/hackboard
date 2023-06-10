"""ListWidget subclasses QListWidget creating a list of items in a
scrollable area."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import time
from typing import NoReturn

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QGridLayout
from icecream import ic
from worktoy.core import maybe
from worktoy.waitaminute import ProceduralError

from hackboard import CoreWidget

ic.configureOutput(includeContext=True)


class ListWidget(CoreWidget, QListWidget):
  """ListWidget subclasses QListWidget creating a list of items in a
  scrollable area.
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""
  rowHover = Signal(str)
  rowClicked = Signal(str)
  rowDoubleClicked = Signal(str)

  def __init__(self, *args, **kwargs) -> None:
    parent = CoreWidget.parseParent(*args, **kwargs)
    QListWidget.__init__(self, parent)
    CoreWidget.__init__(self, *args, **kwargs)
    self.setMouseTracking(True)
    self._logs = []
    self._baseLayout = None
    self._saveFileDialog = None
    self._loadFileDialog = None
    self._name = None
    self._hoverItem = None

  @Slot(str)
  def insertText(self, label: str) -> NoReturn:
    """Inserts the given text"""
    self._logs.append(label)
    item = QListWidgetItem(label)
    QListWidget.insertItem(self, 0, item)
    self.scrollToItem(item)

  def _createBaseLayout(self) -> NoReturn:
    """Creator-function for the base layout"""
    self._baseLayout = QGridLayout()

  def _getBaseLayout(self) -> QGridLayout:
    """Getter-function for the base layout"""
    if self._baseLayout is None:
      self._createBaseLayout()
      return self._getBaseLayout()
    if isinstance(self._baseLayout, QGridLayout):
      return self._baseLayout
    raise TypeError

  def setupActions(self) -> NoReturn:
    """Sets up the actions"""
    self.itemPressed.connect(self._itemPressedFunc)
    self.itemEntered.connect(self._setHoverItem)
    self.itemDoubleClicked.connect(self._itemDoubleClickedFunc)

  def _itemPressedFunc(self, item: QListWidgetItem) -> NoReturn:
    """Function handling item pressed signal"""
    index = self.indexFromItem(item).row()
    self.rowClicked.emit(self._getLogs()[index])

  def _itemDoubleClickedFunc(self, item: QListWidgetItem) -> NoReturn:
    """Function handling item double-clicked signal"""
    index = self.indexFromItem(item).row()
    self.rowDoubleClicked.emit(self._getLogs()[index])

  def _getName(self) -> str:
    """Getter-function for the name of the instance"""
    name = maybe(self._name, 'ListWidget')
    if isinstance(name, str):
      return name
    raise TypeError

  def _setName(self, name: str) -> NoReturn:
    """Setter-function for the name of the instance"""
    self._name = name

  def _getHeader(self) -> str:
    """Getter-function for the header string"""
    return '%s contents from %s' % (self._getName(), time.ctime())

  @Slot(str)
  def saveContents(self, fileName: str) -> NoReturn:
    """Saves the logs to disk"""
    with open(fileName, 'w') as f:
      header = self._getHeader()
      data = '%s\n%s' % (header, '\n'.join(self._logs))
      f.write(data)

  def _getLogs(self) -> list[str]:
    """Getter-function for the logs"""
    if self._logs is None:
      self._logs = []
      return self._getLogs()
    if isinstance(self._logs, list):
      return self._logs
    raise TypeError

  def _getHoverItem(self) -> QListWidgetItem:
    """Getter-function for the hovered item"""
    if isinstance(self._hoverItem, QListWidgetItem):
      return self._hoverItem
    if self._hoverItem is None:
      raise ProceduralError
    raise TypeError

  def _setHoverItem(self, hoverItem: QListWidgetItem) -> NoReturn:
    """Setter-function for the hovered item"""
    self._hoverItem = hoverItem
    self.rowHover.emit(hoverItem.text())
