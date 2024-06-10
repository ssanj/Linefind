import json
from typing import List, Tuple, Dict, Any
import sublime

class RegionsIndex:
  def __init__(self, regions: List[sublime.Region], pos: int = 0):

    assert len(regions) != 0, "Zero regions supplied"
    self.regions = regions
    self.pos = pos
    self.length = len(regions)

  def current(self) -> sublime.Region:
    return self.regions[self.pos]

  def next(self) -> sublime.Region:
    self.pos += 1
    if self.pos >= self.length:
      self.pos = 0

    return self.regions[self.pos]

  def prev(self) -> sublime.Region:
    self.pos -= 1
    if self.pos < 0:
      self.pos = self.length - 1

    return self.regions[self.pos]

  def as_json_str(self):
    regions = [(r.begin(), r.end()) for r in self.regions]
    pos = self.pos

    return json.dumps({"regions": regions, "pos": pos})

  @staticmethod
  def from_json_str(json_str: str):
    json_content: Dict[str, Any] = json.loads(json_str)
    regions_pairs: List[Tuple[int, int]] = json_content["regions"]
    pos: int = json_content["pos"]

    regions = [(sublime.Region(r[0], r[1])) for r in regions_pairs]

    return RegionsIndex(regions, pos)

  def __str__(self) -> str:
    return f'RegionsIndex(regions={self.regions}, pos={self.pos})'

  def __repr__(self) -> str:
    return f'[RegionsIndex(regions={self.regions}, pos={self.pos})]'
