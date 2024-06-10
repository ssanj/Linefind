import sublime
import sublime_plugin
from typing import Optional
from . import regions_index as RI
from . import linefind_setting as SETTING
from . import settings_loader as SETTING_LOADER

class LinefindNextCommand(sublime_plugin.TextCommand):

  print("LinefindNext Text command has loaded.")

  def run(self, edit: sublime.Edit) -> None:
    if self and self.view:
      self.log("LinefindNext is running")
      self.settings: SETTING.LinefindSetting = self.load_settings()
      self.debug(f'settings: {self.settings}')
      if self.view:
        self.on_next(self.view)
    else:
      sublime.message_dialog("Could not initialise plugin")

  def on_next(self, view:sublime.View):
      if view.settings() and "Linefind" in view.settings():
        index_str = view.settings().get("Linefind")
        if index_str:
          self.debug(f'regionIndex from view: {str(index_str)}')
          regions_index = RI.RegionsIndex.from_json_str(index_str)
          region = regions_index.next()
          self.debug(f'next position : {str(region)}')

          view.sel().clear()
          view.sel().add(region)
          view.settings().set("Linefind", regions_index.as_json_str())
      else:
        self.log(f'Could not find "Linefind" key in View')

  def is_enabled(self) -> bool:
    return True

  def is_visible(self) -> bool:
    return True

  def load_settings(self) -> SETTING.LinefindSetting:
    loaded_settings: sublime.Settings = sublime.load_settings('Linefind.sublime-settings')
    return SETTING_LOADER.SettingsLoader(loaded_settings).load()

  def log_with_context(self, message: str, context: Optional[str]):
    if context is not None:
      print(f'[LinefindNext][{context}] - {message}')
    else:
      print(f'[LinefindNext] - {message}')

  def log(self, message: str):
    self.log_with_context(message, context=None)

  def debug(self, message: str):
    if self.settings.debug:
      self.log_with_context(message, context="DEBUG")
