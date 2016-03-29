'use strict';

// emoji.json provided by gemoji (https://github.com/github/gemoji)
const emojiInfo = require('./emoji.json');

module.exports = {
  getSublimeCompletions,
};

/////////////////////////////////////////////////////////////


function getSublimeCompletions() {
  const completions = [];

  emojiInfo.forEach(function (emoji, emojiIndex) {
    emoji.aliases.forEach(function (alias, aliasIndex) {
      // don't prepend ':' (issue #2)
      const content = append(':', stringOrEmpty(alias));
      const tabTrigger = prepend(':', content) + prepend(' ', stringOrEmpty(emoji.emoji));
      const description = stringOrEmpty(emoji.description);

      completions.push([
        tabTrigger + prepend('\t', stringOrEmpty(description)),
        content
      ]);
    });
  });

  return completions;
}

function stringOrEmpty(s) {
  return s ? s.toString() : '';
}

function append(suffix, s) {
  s = s || '';
  suffix = suffix || '';

  return s ? s.toString() + suffix : '';
}

function prepend(prefix, s) {
  s = s || '';
  prefix = prefix || '';

  return s ? prefix + s.toString() : '';
}