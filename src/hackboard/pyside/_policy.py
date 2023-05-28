"""Size policies"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from PySide6.QtWidgets import QSizePolicy

maxPol = QSizePolicy()
maxPol.setVerticalPolicy(QSizePolicy.Policy.Expanding)
maxPol.setHorizontalPolicy(QSizePolicy.Policy.Expanding)

minPol = QSizePolicy()
minPol.setVerticalPolicy(QSizePolicy.Policy.Maximum)
minPol.setHorizontalPolicy(QSizePolicy.Policy.Maximum)

vPol = QSizePolicy()
vPol.setVerticalPolicy(QSizePolicy.Policy.Expanding)
vPol.setHorizontalPolicy(QSizePolicy.Policy.Maximum)

hPol = QSizePolicy()
hPol.setVerticalPolicy(QSizePolicy.Policy.Maximum)
hPol.setHorizontalPolicy(QSizePolicy.Policy.Expanding)
