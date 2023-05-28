"""BaseWindow"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence

from __future__ import annotations

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QMenu


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

  def __init__(self):
    super().__init__()

    # Create menus
    file_menu = self.menuBar().addMenu("&File")
    edit_menu = self.menuBar().addMenu("&Edit")

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
