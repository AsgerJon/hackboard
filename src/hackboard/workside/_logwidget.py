"""LogWidget is as development widget. Instead of print statement for
debugging, call the 'tellMe' method on this widget."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import os
from typing import NoReturn

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QGridLayout, QFileDialog, QLabel
from icecream import ic
from worktoy.typetools import CallMeMaybe
from worktoy.waitaminute import ProceduralError

from hackboard import CoreWidget
from hackboard.workside import ListWidget

ic.configureOutput(includeContext=True)


class LogWidget(CoreWidget):
  """LogWidget is as development widget. Instead of print statement for
  debugging, call the 'tellMe' method on this widget.
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  receivedLog = Signal(str)
  clickedLog = Signal(str)
  doubleClickedLog = Signal(str)
  hoveredLog = Signal(str)
  overWritingSaveFile = Signal(str)

  def __init__(self, *args, **kwargs) -> None:
    CoreWidget.__init__(self, *args, **kwargs)
    self.setMouseTracking(True)
    self._baseLayout = None
    self._listWidget = None
    self._fileName = None
    self._headerLabel = None

  def setupWidgets(self) -> NoReturn:
    """Sets up the widgets"""
    self._listWidget = ListWidget()
    self._baseLayout = QGridLayout()
    self._baseLayout.addWidget(self._listWidget, 0, 0)
    self.setLayout(self._baseLayout)

  def setupActions(self) -> NoReturn:
    """Sets up the actions"""
    self._getListWidget().rowHover.connect(
      self.hoveredLog.emit)
    self._getListWidget().rowClicked.connect(
      self.clickedLog.emit)
    self._getListWidget().rowDoubleClicked.connect(
      self.doubleClickedLog.emit)

  @Slot()
  def initiateSaveLogs(self) -> NoReturn:
    """Saves the logs opening a save file dialog if necessary."""
    fileName = self._getFileName()
    if not isinstance(fileName, str):
      raise TypeError
    if not os.path.exists(fileName):
      self.overWritingSaveFile.emit()
    dirName = os.path.basename(fileName)
    if not os.path.exists(dirName):
      raise NotADirectoryError
    return self.saveLogs(fileName)

  @Slot(str)
  def saveLogs(self, fileName: str) -> NoReturn:
    """Performs the saving operation on the fileName received."""
    self._getListWidget().saveContents(fileName)

  def _createHeaderLabel(self) -> NoReturn:
    """Creator-function for the header label"""
    self._headerLabel = QLabel()

  def _getHeaderLabel(self, ) -> QLabel:
    """Getter-function for the header label"""
    if self._headerLabel is None:
      self._createHeaderLabel()
      return self._getHeaderLabel()
    if isinstance(self._headerLabel, QLabel):
      return self._headerLabel
    raise TypeError

  def _createListWidget(self) -> NoReturn:
    """Creator-function for the list widget"""
    self._listWidget = ListWidget()

  def _getListWidget(self) -> ListWidget:
    """Returns the list widget"""
    if self._listWidget is None:
      self._createListWidget()
      return self._getListWidget()
    if isinstance(self._listWidget, ListWidget):
      return self._listWidget

  def _createBaseLayout(self) -> NoReturn:
    """Creator-function for the base layout"""
    self._baseLayout = QGridLayout()

  def _getBaseLayout(self) -> QGridLayout:
    """Returns the base layout"""
    if self._baseLayout is None:
      self._createBaseLayout()
      return self._getBaseLayout()
    if isinstance(self._baseLayout, QGridLayout):
      return self._baseLayout

  def _createSaveFileDialog(self) -> NoReturn:
    """Creator-function for the save file dialog"""
    self._saveFileDialog = QFileDialog()
    self._saveFileDialog.setFileMode(QFileDialog.FileMode.AnyFile)
    self._saveFileDialog.setViewMode(QFileDialog.ViewMode.Detail)
    self._saveFileDialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
    self._saveFileDialog.fileSelected.connect(self._setFileName)

  def _getSaveFileDialog(self) -> QFileDialog:
    """Getter-function for the save file dialog"""
    if self._saveFileDialog is None:
      self._createSaveFileDialog()
      return self._getSaveFileDialog()
    if isinstance(self._saveFileDialog, QFileDialog):
      return self._saveFileDialog
    raise TypeError

  def _beginSaveOperation(self, callBack: CallMeMaybe) -> NoReturn:
    """Begins the saving operation"""
    self._getSaveFileDialog().show()
    if self._getFileName():
      callBack(self._getFileName())
    raise ProceduralError()

  def _setFileName(self, fileName: str) -> NoReturn:
    """Setter-function for the file name"""
    self._fileName = fileName

  def _getFileName(self) -> str:
    """Getter-function for file name"""
    if self._fileName is None:
      dialog = self._getSaveFileDialog()
      if dialog.show() or True:
        if self._fileName is None:
          raise ProceduralError()
        return self._getFileName()
    return self._fileName
