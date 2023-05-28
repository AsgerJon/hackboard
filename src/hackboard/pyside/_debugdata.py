"""Debugging data"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from PySide6.QtWidgets import QWidget, QVBoxLayout, QFormLayout
from worktoy.parsing import extractArg
from worktoy.stringtools import stringList
from worktoy.waitaminute import ProceduralError


class DebugData(QWidget):
  """Debugging data
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  def __init__(self, *args, **kwargs) -> None:
    parentKeys = stringList('parent, main, mainWindow')
    data = extractArg(QWidget, parentKeys, *args, **kwargs)
    parent: QWidget
    parent, args, kwargs = data
    if parent is None:
      raise ProceduralError('parent', QWidget, None)
    QWidget.__init__(self, parent)
    self._baseWidget: QWidget
    self._baseLayout: QFormLayout
    self.parent.
  def setupWidgets(self) -> NoReturn:
    """Setting up the widgets"""
