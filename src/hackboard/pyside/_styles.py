"""Styles"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import os


def getStyle(context: str) -> str:
  """Get the style for the given context"""
  if context.lower() == 'qlabel':
    root = os.getcwd()
    fid = os.path.join(root, 'src', 'hackboard', 'pyside', '_qlabel.css')
    with open(fid, 'r') as f:
      labelStyle = f.read()
    return labelStyle
