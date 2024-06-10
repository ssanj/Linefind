# Linefind

[Sublime Text](https://www.sublimetext.com/) plugin that Finds text on a given line number

![]()

## Installation

- Open the command palette with `CMD + SHIFT + P`
- Select `Package Control: Add Repository`
- Enter https://github.com/ssanj/Linefind for the repository
- Select `Package Control: Install Package`
- Choose Linefind


## Functionality

![Linefind in Action](linefind-vid-2.gif)

Lets you search for some text on a given line.

From the command palette choose `Linefind: Finds text on a given line number` and enter a line number you want to search on followed by a `:` and the text to search by. You can also use `SHIFT+CTRL+G` to launch the finder.

![Searching with Linefind](linefind.png)

### Find next match

If there are multiple matches you can move to the next match with the `LinefindNext: Finds next match on a given line number` command or with `SHIFT+SUPER+=`.

### Find previous match

If there are multiple matches you can move to the previous match with the `LinefindPrev: Finds previous match on a given line number` command or with `SHIFT+SUPER+-`.


## Settings

```
{
  // Whether to turn on debug logging
  "debug": true
}
```
