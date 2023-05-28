"""MetaStyle is a metaclass relating to applying styles"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Any

from PySide6.QtGui import QPainter


class _MetaStyle(type):
  """MetaStyle is a metaclass relating to applying styles
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  def __matmul__(cls, other: Any) -> Any:
    """Enabling the @ operator"""


class MetaStyle(metaclass=_MetaStyle):
  """Intermediary class"""
  pass
