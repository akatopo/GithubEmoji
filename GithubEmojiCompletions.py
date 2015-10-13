import sublime, sublime_plugin, os

settings = None

class GithubEmojiCompletions(sublime_plugin.EventListener):
    """
    Provide github emoji completions for selected file extensions or names
    """

    def on_query_completions(self, view, prefix, locations):
        # Only trigger for valid file names
        if not is_valid_file_name(view.file_name()):
            return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))

        # emoji completions
        if ch == ':':
            return settings.get("emojiCompletions")
        # emoji completions for commit messages
        if ch == '@':
            return settings.get("commitEmojiCompletions")
        return []

class GithubEmojiAutoCompleteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("auto_complete")
        self.view.run_command("left_delete")
    def is_enabled(self):
        return is_valid_file_name(self.view.file_name())

def is_valid_file_name(file_name):
    if file_name is None:
        return False
    tail = os.path.split(file_name)[1]
    ext = os.path.splitext(tail)[1]
    return (ext in settings.get("emojiFileExtensions") or
        tail in settings.get("emojiFileNames"))

def plugin_loaded():
    global settings
    settings = sublime.load_settings("GithubEmoji.sublime-settings")