import sublime, sublime_plugin

settings = None

class GithubEmojiCompletions(sublime_plugin.EventListener):
    """
    Provide github emoji completions for markdown
    """

    def on_query_completions(self, view, prefix, locations):
        # settings = sublime.load_settings("GithubEmoji.sublime-settings")
        # Only trigger for markdown
        if not view.match_selector(locations[0],
                "text.html.markdown"):
            return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))

        # emoji completions
        if ch == ':':
            return settings.get("emojiCompletions")
        # emoji completions for commit messages
        if ch == '@':
            return settings.get("commitEmojiCompletions");
        return []

def plugin_loaded():
    global settings
    settings = sublime.load_settings("GithubEmoji.sublime-settings")