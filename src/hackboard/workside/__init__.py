"""The workstyle module provides more utilities relating to PySide6."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from ._corewidget import CoreWidget
from ._label import Label
from ._listwidget import ListWidget
from ._logwidget import LogWidget

from icecream import ic

ic.configureOutput(includeContext=True)
