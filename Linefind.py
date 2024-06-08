import sublime
import sublime_plugin
from typing import Optional, List
from . import linefind_setting as SETTING
from . import settings_loader as SETTING_LOADER

class LinefindCommand(sublime_plugin.TextCommand):

  print("Linefind Text command has loaded.")

  def run(self, edit: sublime.Edit) -> None:
    if self and self.view:
      self.log("Linefind is running")
      self.settings: SETTING.LinefindSetting = self.load_settings()
      self.debug(f'settings: {self.settings}')
      self.view.window().show_input_panel(caption = "search", initial_text = ":", on_done = lambda term: self.on_search(self.view, term), on_cancel = self.on_cancel, on_change = None)
    else:
      sublime.message_dialog("Could not initialise plugin")

  def on_search(self, view:sublime.View, term: str):
    terms = term.split(":", maxsplit = 1)
    if len(terms) == 2:
      line = int(terms[0])
      search_term = terms[1]
      matched_regions = view.find_all(search_term)
      matched_line = [r for r in matched_regions if view.rowcol(r.begin())[0] + 1 == line]
      if matched_line:
        result = matched_line[0]
        view.sel().clear()
        view.sel().add(result)
        view.show_at_center(result)
      else:
        self.log(f'Could not find {search_term} on line {line}')
    else:
      self.log(f'Could not parse search text: {term}')

  def on_cancel(self):
    sublime.message_dialog("you canceled")

  def is_enabled(self) -> bool:
    return True

  def is_visible(self) -> bool:
    return True

  def load_settings(self) -> SETTING.LinefindSetting:
    loaded_settings: sublime.Settings = sublime.load_settings('Linefind.sublime-settings')
    return SETTING_LOADER.SettingsLoader(loaded_settings).load()

  def log_with_context(self, message: str, context: Optional[str]):
    if context is not None:
      print(f'[Linefind][{context}] - {message}')
    else:
      print(f'[Linefind] - {message}')

  def log(self, message: str):
    self.log_with_context(message, context=None)

  def debug(self, message: str):
    if self.settings.debug:
      self.log_with_context(message, context="DEBUG")
