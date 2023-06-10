"""HackBoard is a PySide6 word processor"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Any

from worktoy.waitaminute import n00bError

from ._basewindow import BaseWindow
from ._layoutwindow import LayoutWindow
from ._inputwindow import InputWindow
from ._mainwindow import MainWindow


def __getattr__(name) -> Any:
  """Don't use star imports"""
  if name == '__all__':
    raise n00bError
