"""InputWindow subclasses LayoutWindow"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from PySide6.QtGui import QKeyEvent

from hackboard.pyside import LayoutWindow


class InputWindow(LayoutWindow):
  """InputWindow subclasses LayoutWindow
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  def __init__(self, ) -> None:
    LayoutWindow.__init__(self)

  def show(self) -> NoReturn:
    """LOL"""
    LayoutWindow.show(self)

  def keyReleaseEvent(self, event: QKeyEvent) -> NoReturn:
    """Triggers spell checking"""
    LayoutWindow.keyReleaseEvent(self, event)

  def keyPressEvent(self, event: QKeyEvent) -> NoReturn:
    """Triggers spell checking"""
    LayoutWindow.keyPressEvent(self, event)
