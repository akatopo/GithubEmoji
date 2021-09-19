import sublime
import sublime_plugin
import os

settings = None

st_version = int(sublime.version())
invoked_manually = False

class GithubEmojiCompletions(sublime_plugin.EventListener):
    """
    Provide github emoji completions for selected file extensions or names
    """

    def on_query_completions(self, view, prefix, locations):
        # Only trigger for valid file names and scopes
        if not is_valid_file_name(view.file_name()) and \
                not is_valid_scope(view, locations[0]):
            return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))

        # emoji completions
        if ch == ':':
            if st_version < 4000:
                return settings.get("emojiCompletions3")
            else:
                return settings.get("emojiCompletions")
        # emoji completions for commit messages
        if ch == '@':
            if st_version < 4000:
                return settings.get("commitEmojiCompletions3")
            global invoked_manually
            if invoked_manually:
                invoked_manually = False
                return settings.get("commitEmojiCompletions")
            else:
                return settings.get("commitEmojiCompletionsAuto")
        return []

class GithubEmojiAutoCompleteCommand(sublime_plugin.TextCommand):
    def run(self, edit, isCommitEmoji=False):
        global invoked_manually
        invoked_manually = True
        self.view.run_command("auto_complete")
        if isCommitEmoji:
            self.view.run_command("left_delete")
            if st_version >= 4000:
                self.view.run_command("insert", {"characters":":"})

    def is_enabled(self):
        return is_valid_file_name(self.view.file_name()) or \
            is_valid_scope(self.view, self.view.sel()[0].begin())

def is_valid_file_name(file_name):
    if file_name is None:
        return False
    tail = os.path.split(file_name)[1]

    return tail in settings.get("emojiFileNames")

def is_valid_scope(view, point):
    for scope in settings.get("emojiScopes"):
        if view.match_selector(point, scope):
            return True
    return False

def plugin_loaded():
    global settings
    settings = sublime.load_settings("GithubEmoji.sublime-settings")
