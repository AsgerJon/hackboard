"""This file provides style settings relating to fonts"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPen, QColor, QPainter
from PySide6.QtWidgets import QWidget
from worktoy.parsing import maybeType

from hackboard.pyside.style import MetaStyle


class FontStyle(MetaStyle):
  """This file provides style settings relating to fonts
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  _normalFont = QFont()
  _normalFont.setFamily('Courier')
  _normalFont.setPointSize(16)
  _textPen = QPen()
  _textPen.setStyle(Qt.PenStyle.SolidLine)
  _textPen.setColor(QColor(0, 0, 0, 255))
  _textPen.setWidth(1)

  @classmethod
  def getNormalFont(cls) -> QFont:
    """Getter-function for the normal font"""
    return cls._normalFont

  @classmethod
  def getTextPen(cls) -> QPen:
    """Getter-function for normal pen"""
    return cls._textPen

  @classmethod
  def __call__(cls, *args, ) -> QPainter | QWidget:
    """Calling the style applies the font and pen to the argument."""
    print('lol')
    return cls.apply(cls, *args)

  @classmethod
  def __matmul__(cls, other: QPainter | QWidget) -> QPainter | QWidget:
    """Calling the style applies the font and pen to the argument."""
    return cls.apply(other)

  @classmethod
  def apply(cls, *args) -> QPainter | QWidget:
    """Applies the font and pen to the argument."""
    painter = maybeType(QPainter, *args)
    widget = maybeType(QWidget, *args)
    if painter is None:
      widget.setFont(cls._normalFont)
      return widget
    painter.setFont(cls._normalFont)
    painter.setPen(cls._textPen)
    return painter

  def loadFromDisk(self) -> NoReturn:
    """Loads color styles from disk"""
    raise NotImplementedError
