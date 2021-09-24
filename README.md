# Github :octocat: Emoji :panda_face: for Sublime Text

A Sublime Text plugin for inserting github emoji in markdown documents. Also supports [commit message emoji](https://github.com/dannyfritz/commit-message-emoji)

## Usage

<img src="screenshots/emoji-completions.gif" alt="emoji completion" width="688">

When editing a markdown document type `:` and then press <kbd>TAB</kbd> to display the auto-complete popup for github emoji. You can type `@` instead of `:` for commit message emoji.

Alternatively, for non-commit emoji, you can add this to your `auto_complete_triggers` in the user preferences:

```js
"auto_complete_triggers": [
  //...
  {
    "characters": ":",
    "selector": "text.html.markdown"
  },
  // ...
],
```

In Sublime Text __4__ you do the same for commit emojis:
```js
{ "characters": [":", "@"],
  "selector": "text.html.markdown, text.git.commit"},
```

This way when you type `:` (or `@` in ST4) in markdown documents you'll get the autocompletion popup.

You can customize the available emoji, scopes, and filenames by copying and editing the default settings (`Preferences > Package Settings > GithubEmoji > Settings – Default`) and saving them into your own user settings (`Preferences > Package Settings > GithubEmoji > Settings – User`)

You can check available github emoji at the [emoji cheat sheet](http://www.emoji-cheat-sheet.com/)

**Note:** On linux you will need a font that includes emoji in order to see emoji characters in the auto-complete popup. Here's [one](https://github.com/MorbZ/OpenSansEmoji)

## Installation

### Package Control (preferred)

1. [Install Sublime Package Control](http://wbond.net/sublime_packages/package_control/installation)
2. From inside Sublime Text, open Package Control's Command Pallet: <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>P</kbd> (Windows, Linux) or <kbd>CMD</kbd> + <kbd>SHIFT</kbd> + <kbd>P</kbd> on Mac.
3. Type `install package` and hit Return. A list of available packages will be displayed.
4. Type `GithubEmoji` and hit Return. The package will be downloaded to the appropriate directory.

### Manual Installation

Download or clone this repository to a directory `GithubEmoji` in the Sublime Text Packages directory for your platform:

**Mac:**

```shell
git clone https://github.com/akatopo/GithubEmoji.git ~/Library/Application\ Support/Sublime\ Text/Packages/GithubEmoji
```

**Windows:**

```shell
git clone https://github.com/akatopo/GithubEmoji.git %APPDATA%\Sublime/ Text/\GithubEmoji
```

**Linux:**

```shell
git clone https://github.com/akatopo/GithubEmoji.git ~/.Sublime\ Text/Packages/GithubEmoji
```

## Credits

Special thanks to @eugenesvk for adding sublime text 4 support.

The list of github emoji ([emoji.json](https://github.com/github/gemoji/blob/3f6057146c9a12e154c7bf00be4b125a76f413e0/db/emoji.json)) is taken from [gemoji](https://github.com/github/gemoji).

Installation instructions ripped from [MarkdownEditing](https://github.com/SublimeText-Markdown/MarkdownEditing)'s readme.

## Similar Plugins

The [Emoji](https://github.com/ethanal/SublimeEmoji/) plugin allows you to insert emoji characters from the command palette.
