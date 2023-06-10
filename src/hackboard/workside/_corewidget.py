"""CoreWidget subclasses QWidget providing common and general
functionality."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from PySide6.QtCore import QRectF
from PySide6.QtGui import QBrush, QPen
from PySide6.QtWidgets import QWidget, QSizePolicy
from worktoy.parsing import extractArg
from worktoy.stringtools import stringList

from hackboard.settings import BaseStyle


class CoreWidget(QWidget):
  """CoreWidget subclasses QWidget providing common and general
  functionality.
  #  MIT Licence
  #  Copyright (c) 2023 Asger Jon Vistisen"""

  @staticmethod
  def createSizePolicy(*args, **kwargs) -> QSizePolicy:
    """Creator function for a size policy according to specification given
    in arguments"""
    verticalKeys = stringList('vertical, v, verticalPolicy')
    verticalSizePolicy, args, kwargs = extractArg(
      QSizePolicy.Policy, verticalKeys, *args, **kwargs)
    horizontalKeys = stringList('horizontal, h, horizontalPolicy')
    horizontalSizePolicy, args, kwargs = extractArg(
      QSizePolicy.Policy, horizontalKeys, *args, **kwargs)
    policy = QSizePolicy()
    policy.setVerticalPolicy(verticalSizePolicy)
    policy.setHorizontalPolicy(horizontalSizePolicy)
    return policy

  @classmethod
  def expandVerticalPolicy(cls) -> QSizePolicy:
    """Creator function for a size policy expanding vertically,
    and contracting horizontally"""
    return cls.createSizePolicy(
      vertical=QSizePolicy.Policy.MinimumExpanding,
      horizontal=QSizePolicy.Policy.Maximum)

  @classmethod
  def expandHorizontalPolicy(cls) -> QSizePolicy:
    """Creator function for a size policy expanding vertically,
    and contracting horizontally"""
    return cls.createSizePolicy(
      horizontal=QSizePolicy.Policy.Maximum,
      vertical=QSizePolicy.Policy.MinimumExpanding, )

  @staticmethod
  def parseParent(*args, **kwargs) -> QWidget:
    """Parses arguments to parent"""
    parentKeys = stringList('parent, main, mainWindow, window')
    parent, args, kwargs = extractArg(QWidget, parentKeys, *args, **kwargs)
    if isinstance(parent, QWidget):
      return parent

  def __init__(self, *args, **kwargs) -> None:
    parent = self.parseParent(*args, **kwargs)
    QWidget.__init__(self, parent)
    self._style = None
    self.setupWidgets()
    self.setupActions()

  def getStyle(self) -> BaseStyle:
    """Getter-function for the style"""
    if isinstance(self._style, BaseStyle):
      return self._style
    raise TypeError

  def setStyle(self, style: BaseStyle) -> NoReturn:
    """Setter-function for the style"""
    self._style = style

  def setupWidgets(self) -> NoReturn:
    """Sets up the widgets"""

  def setupActions(self) -> NoReturn:
    """Sets up the actions"""

  def show(self) -> NoReturn:
    """Reimplementation"""
    self.setupWidgets()
    self.setupActions()
    return QWidget.show(self)
