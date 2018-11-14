# Awesome sublime stuff

## Packages

### UI

* [A File Icon](https://github.com/ihodev/a-file-icon) - file-specific icons in the sidebar
* [SideBarEnhancements](https://packagecontrol.io/packages/SideBarEnhancements)  - sidebar does loads more stuff
* [Monokai Extended](https://github.com/jonschlinkert/sublime-monokai-extended) - More Monokai highlighting (also to get Rainbowth to work...)

### Text related

* [HighlightWords](https://packagecontrol.io/packages/HighlightWords) - custom highlighting of e.g. TODO of DEBUG
* [InsertDate](https://packagecontrol.io/packages/InsertDate) - insert current data/time (bind to keyboard shortcuts)
* [MarkdownEditing](https://packagecontrol.io/packages/MarkdownEditing) - robust syntax highlighting for Markdown
* [Markdown Extended](https://github.com/jonschlinkert/sublime-markdown-extended) - more different Markdown syntax highlighting (does a better job of inline code highlighting, worse at bullets)
* [MarkdownPreview](https://packagecontrol.io/packages/MarkdownPreview) - allows for easy Markdown preview in the browser
* [PlainTasks](https://packagecontrol.io/packages/PlainTasks) - nice todo lists
* [Pandoc](https://packagecontrol.io/packages/Pandoc) - convert between different markup formats
* [Table Editor](https://packagecontrol.io/packages/Table%20Editor) - makes editing text tables much better
* [Rainbowth](https://github.com/whitequark/rainbowth) - Rainbow parantheses for Lisps
* [Parinfer](https://github.com/oakmac/sublime-text-parinfer) - Smart parentheses for Lisps

### General programming

* [BracketHighlighter](https://packagecontrol.io/packages/BracketHighlighter) - matches and highlights a variety of brackets
* [Generic Config](https://packagecontrol.io/packages/Generic%20Config) - generic highlighting of config files
* [Git](https://packagecontrol.io/packages/Git) - git integration
* [GitGutter](https://packagecontrol.io/packages/GitGutter) - see git diff in gutter
* [SublimeCodeIntel](https://packagecontrol.io/packages/SublimeCodeIntel) - autocomplete, goto definition etc.
* [SublimeLinter](https://packagecontrol.io/packages/SublimeLinter) - code linting
* [SublimeREPL](https://packagecontrol.io/packages/SublimeREPL) - run interpreter inside Sublime

### Python

* [AutoDocstring](https://packagecontrol.io/packages/AutoDocstring) - insert/update docstrings
* [Python Fix Imports](https://packagecontrol.io/packages/Python%20Fix%20Imports) - gets imports correctly ordered and formatted
* [PyYapf Python Formatter](https://packagecontrol.io/packages/PyYapf%20Python%20Formatter) - runs the [YAPF](https://github.com/google/yapf) 
Python formatter. Note that in order for it to not break with dictionary unpacking `**my_dict` you need the Python3.6+ version of `yapf`. See [here](https://stackoverflow.com/a/44254088/9839539) for instructions on how to set up Python3.6 and pip3.6. Then just do
```bash
pip3 uninstall yapf 
pip3.6 install yapf
whereis yapf
```
* [SublimeLinter-pylint](ttps://packagecontrol.io/packages/SublimeLinter-pylint) - because you need a Python linter


## Meta

* [Hooks](https://packagecontrol.io/packages/Hooks) - allows you to bind custom commands to Sublime hooks
* [Package Control](https://packagecontrol.io) - have to have this
* [PackageResourceViewer](https://packagecontrol.io/packages/PackageResourceViewer) - can view default snippets

## Misc

* [Carbon](https://github.com/molnarmark/carbonSublime) - making code snippets for presentations *etc.* (without having to print screen everything!)

## Making custom commands (keymap, command palette)

As an example, consider running `autoflake` on Python files you are editing. 

[`autoflake`](https://pypi.org/project/autoflake/) is a Python tool that trims used imports and variables.

You will need the following Python script saved in your `.config/sublime-text-3/Packages/User` folder (see [here](https://github.com/kylebebak/sublime_text_config/blob/master/autoflake.py))

### Custom command

```python
# autoflake.py

import sublime_plugin

import subprocess


class AutoflakeRemoveUnusedImportsCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        subprocess.check_call([
            # '/usr/local/bin/autoflake',
            '/home/railton/environments/default_3/bin/autoflake',
            '--in-place',
            '--remove-all-unused-imports',
            self.view.file_name(),
        ])

```

### Command palette

Append the following to `Default.sublime-commands` to have it available via the command palette.

```json
[
    // ...
    { "caption": "Custom: Autoflake Remove Unused Imports", "command": "autoflake_remove_unused_imports" }  
]
```
### Keymap

To do key binding, append the following to `Default (Linux).sublime-keymap`:

```json
[
    // ...
    { "keys": ["ctrl+alt+g"], "command": "autoflake_remove_unused_imports",
    "context": [
            { "key": "selector", "operator": "equal", 
            "operand": "source.python" }
        ]
    }
]
```

### Activate upon save

To activate upon save you will need the `Hooks` package, and to add the following to `Preferences.sublime-settings`:

```json
{
    // ...
    "on_post_save_user":
        [
            {
                "command": "autoflake_remove_unused_imports"
            }
        ],
}
```
*N.B.* don't actually do this as it can be pretty annoying - implementing it as a pre-commit hook is a much better idea (see [this gist](https://gist.github.com/annarailton/afa9c4fb40a2928547b2f14ed1fce8f6) for more info).
