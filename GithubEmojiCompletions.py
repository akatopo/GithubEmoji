import sublime
import sublime_plugin
import os
import sys
import json

settings = None
commit_emojis = None
emojis_emoji = emojis_alias = None

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

        complete_with_emoji = view.settings().get('github_emoji_complete_with_emoji') is True
        if complete_with_emoji:
            return emojis_emoji
        # emoji completions
        if ch == ':':

            return emojis_alias
        # emoji completions for commit messages
        if ch == '@':
            return settings.get("commitEmojiCompletions")
        return []

    def on_post_text_command(self, view, cmd, args):
        if cmd != 'commit_completion':
            return

        # the second condition is used to check whether it's a buggy emoji which
        # is printed as more than one character

        actual_emojis = list(map(lambda emo: emo[1], emojis))
        for region in view.sel():
            if view.substr(region.begin() - 1) not in actual_emojis \
                or view.substr(region.begin() - 2) in ':@':
                return

        view.run_command('move', {'forward': False, 'by': 'characters'})
        view.run_command('left_delete')
        view.run_command('move', {'forward': True, 'by': 'characters'})

class GithubEmojiAutoCompleteCommand(sublime_plugin.TextCommand):
    def run(self, edit, isCommitEmoji=False):
        self.view.run_command("auto_complete")
        if isCommitEmoji:
            self.view.run_command("left_delete")

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
    global settings, emojis_alias, emojis_emoji, emojis
    settings = sublime.load_settings("GithubEmoji.sublime-settings")
    emojis = sublime.decode_value(sublime.load_resource('Packages/GithubEmoji/emoji.json'))
    emojis_alias = []
    emojis_emoji = []
    for emo in emojis:
        emojis_alias.append([":{}: {}\t{}".format(*emo), emo[0] + ':'])
    for emo in emojis:
        emojis_emoji.append([":{}: {}\t{}".format(*emo), emo[1]])
