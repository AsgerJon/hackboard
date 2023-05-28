"""BaseWindow"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence

from __future__ import annotations

import os
from typing import NoReturn

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction, QPixmap, QKeyEvent
from PySide6.QtWidgets import QMainWindow, QMenu, QLabel, QStatusBar, \
  QSizePolicy, QWidget

from hackboard.pyside import getStyle


class BaseWindow(QMainWindow):
  """
  A subclass of QMainWindow that provides menus and actions for a simple
  word processing application.

  This class creates File and Edit menus with basic actions for creating,
  opening, saving, cutting, copying, and pasting files.
  You can add more widgets and layouts to this subclass later on to create
  your word processing application.

  Signals:
  -------
  None

  Slots:
  -----
  new_file()
      Creates a new file.
  open_file()
      Opens an existing file.
  save_file()
      Saves the current file.
  save_file_as()
      Saves the current file with a new name.
  cut()
      Cuts the selected text.
  copy()
      Copies the selected text.
  paste()
      Pastes the copied or cut text.

  """

  spaceKeyRelease = Signal()
  spaceKeyPress = Signal()

  def __init__(self, parent: QWidget = None) -> None:
    QMainWindow.__init__(self, parent)
    statusBar = QLabel()
    statusBar.setStyleSheet(getStyle('QLabel'))
    policy = QSizePolicy()
    policy.setVerticalPolicy(QSizePolicy.Policy.Maximum)
    policy.setHorizontalPolicy(QSizePolicy.Policy.Expanding)
    statusBar.setSizePolicy(policy)
    self.statusBar().addWidget(statusBar)

    # Create menus
    file_menu = self.menuBar().addMenu("&File")
    edit_menu = self.menuBar().addMenu("&Edit")
    helpMenu = self.menuBar().addMenu("&Help")

    # Create actions
    new_action = QAction("&New", self)
    open_action = QAction("&Open", self)
    save_action = QAction("&Save", self)
    save_as_action = QAction("Save &As...", self)
    exit_action = QAction("&Exit", self)

    cut_action = QAction("Cu&t", self)
    copy_action = QAction("&Copy", self)
    paste_action = QAction("&Paste", self)

    # Add actions to menus
    file_menu.addAction(new_action)
    file_menu.addAction(open_action)
    file_menu.addAction(save_action)
    file_menu.addAction(save_as_action)
    file_menu.addSeparator()
    file_menu.addAction(exit_action)

    edit_menu.addAction(cut_action)
    edit_menu.addAction(copy_action)
    edit_menu.addAction(paste_action)

    # Connect signals and slots
    new_action.triggered.connect(self.new_file)
    open_action.triggered.connect(self.open_file)
    save_action.triggered.connect(self.save_file)
    save_as_action.triggered.connect(self.save_file_as)
    exit_action.triggered.connect(self.close)

    cut_action.triggered.connect(self.cut)
    copy_action.triggered.connect(self.copy)
    paste_action.triggered.connect(self.paste)

    self.debugAction01 = QAction("Debug 01", self)
    self.debugAction02 = QAction("Debug 02", self)
    self.debugAction03 = QAction("Debug 03", self)
    self.debugAction04 = QAction("Debug 04", self)
    self.debugAction05 = QAction("Debug 05", self)
    self.debugAction06 = QAction("Debug 06", self)
    self.debugAction07 = QAction("Debug 07", self)
    self.debugAction08 = QAction("Debug 08", self)
    self.debugAction09 = QAction("Debug 09", self)
    self.debugAction10 = QAction("Debug 10", self)
    self.debugAction11 = QAction("Debug 11", self)
    self.debugAction12 = QAction("Debug 12", self)
    helpMenu.addAction(self.debugAction01)
    helpMenu.addAction(self.debugAction02)
    helpMenu.addAction(self.debugAction03)
    helpMenu.addAction(self.debugAction04)
    helpMenu.addAction(self.debugAction05)
    helpMenu.addAction(self.debugAction06)
    helpMenu.addAction(self.debugAction07)
    helpMenu.addAction(self.debugAction08)
    helpMenu.addAction(self.debugAction09)
    helpMenu.addAction(self.debugAction10)
    helpMenu.addAction(self.debugAction11)
    helpMenu.addAction(self.debugAction12)

    self.debugAction01.setShortcut("QKeySequence.fromString('F1')")
    self.debugAction01.setShortcutContext(
      Qt.ShortcutContext.ApplicationShortcut)
    self.debugAction01.triggered.connect(self.debugFunc01)

    self.debugAction02.setShortcut("QKeySequence.fromString('F2')")
    self.debugAction02.setShortcutContext(
      Qt.ShortcutContext.ApplicationShortcut)
    self.debugAction02.triggered.connect(self.debugFunc02)

    self.debugAction03.setShortcut("QKeySequence.fromString('F3')")
    self.debugAction03.setShortcutContext(
      Qt.ShortcutContext.ApplicationShortcut)
    self.debugAction03.triggered.connect(self.debugFunc03)

    self.debugAction04.setShortcut("QKeySequence.fromString('F4')")
    self.debugAction04.setShortcutContext(
      Qt.ShortcutContext.ApplicationShortcut)
    self.debugAction04.triggered.connect(self.debugFunc04)

    self.debugAction05.setShortcut("QKeySequence.fromString('F5')")
    self.debugAction05.setShortcutContext(
      Qt.ShortcutContext.ApplicationShortcut)
    self.debugAction05.triggered.connect(self.debugFunc05)

    self.debugAction06.setShortcut("QKeySequence.fromString('F6')")
    self.debugAction06.setShortcutContext(
      Qt.ShortcutContext.ApplicationShortcut)
    self.debugAction06.triggered.connect(self.debugFunc06)

    self.debugAction07.setShortcut("QKeySequence.fromString('F7')")
    self.debugAction07.setShortcutContext(
      Qt.ShortcutContext.ApplicationShortcut)
    self.debugAction07.triggered.connect(self.debugFunc07)

    self.debugAction08.setShortcut("QKeySequence.fromString('F8')")
    self.debugAction08.setShortcutContext(
      Qt.ShortcutContext.ApplicationShortcut)
    self.debugAction08.triggered.connect(self.debugFunc08)

    self.debugAction09.setShortcut("QKeySequence.fromString('F9')")
    self.debugAction09.setShortcutContext(
      Qt.ShortcutContext.ApplicationShortcut)
    self.debugAction09.triggered.connect(self.debugFunc09)

    self.debugAction10.setShortcut("QKeySequence.fromString('F10')")
    self.debugAction10.setShortcutContext(
      Qt.ShortcutContext.ApplicationShortcut)
    self.debugAction10.triggered.connect(self.debugFunc10)

    self.debugAction11.setShortcut("QKeySequence.fromString('F11')")
    self.debugAction11.setShortcutContext(
      Qt.ShortcutContext.ApplicationShortcut)
    self.debugAction11.triggered.connect(self.debugFunc11)

    self.debugAction12.setShortcut("QKeySequence.fromString('F12')")
    self.debugAction12.setShortcutContext(
      Qt.ShortcutContext.ApplicationShortcut)
    self.debugAction12.triggered.connect(self.debugFunc12)

  def show(self) -> NoReturn:
    """Sets up debuggers"""
    self.setupDebuggers()
    QMainWindow.show(self)

  def setupDebuggers(self) -> NoReturn:
    """Sets up the debuggers"""
    print('Setting up debuggers!')

  def keyReleaseEvent(self, event: QKeyEvent) -> NoReturn:
    """Triggers spell checking"""
    QMainWindow.keyReleaseEvent(self, event)

  def keyPressEvent(self, event: QKeyEvent) -> NoReturn:
    """Triggers spell checking"""
    QMainWindow.keyPressEvent(self, event)

  def debugFunc01(self) -> NoReturn:
    """Debugger 01"""

  def debugFunc02(self) -> NoReturn:
    """Debugger 02"""

  def debugFunc03(self) -> NoReturn:
    """Debugger 03"""

  def debugFunc04(self) -> NoReturn:
    """Debugger 04"""

  def debugFunc05(self) -> NoReturn:
    """Debugger 05"""

  def debugFunc06(self) -> NoReturn:
    """Debugger 06"""

  def debugFunc07(self) -> NoReturn:
    """Debugger 07"""

  def debugFunc08(self) -> NoReturn:
    """Debugger 08"""

  def debugFunc09(self) -> NoReturn:
    """Debugger 09"""

  def debugFunc10(self) -> NoReturn:
    """Debugger 10"""

  def debugFunc11(self) -> NoReturn:
    """Debugger 11"""

  def debugFunc12(self) -> NoReturn:
    """Debugger 12"""

  # Define slots
  def new_file(self):
    """
    Creates a new file.

    Parameters:
    ----------
    None

    Returns:
    -------
    None
    """
    pass

  def open_file(self):
    """
    Opens an existing file.

    Parameters:
    ----------
    None

    Returns:
    -------
    None
    """
    pass

  def save_file(self):
    """
    Saves the current file.

    Parameters:
    ----------
    None

    Returns:
    -------
    None
    """
    pass

  def save_file_as(self):
    """
    Saves the current file with a new name.

    Parameters:
    ----------
    None

    Returns:
    -------
    None
    """
    pass

  def cut(self):
    """
    Cuts the selected text.

    Parameters:
    ----------
    None

    Returns:
    -------
    None
    """
    pass

  def copy(self):
    """
    Copies the selected text.

    Parameters:
    ----------
    None

    Returns:
    -------
    None
    """
    pass

  def paste(self):
    """
    Pastes the copied or cut text.

    Parameters:
    ----------
    None

    Returns:
    -------
    None
    """
    pass
