'use strict';

// emoji.json provided by gemoji (https://github.com/github/gemoji)
var emojiInfo = require('./emoji.json');
var completions = new Array(emojiInfo.length);

emojiInfo.forEach(function (emoji, emojiIndex) {
  emoji.aliases.forEach(function (alias, aliasIndex) {
    var tabTrigger;
    var content;
    var description;

    content = append(':', prepend(':', stringOrEmpty(alias)));
    tabTrigger = content + prepend(' ', stringOrEmpty(emoji.emoji));
    description = stringOrEmpty(emoji.description);

    completions[emojiIndex + aliasIndex] = [
      tabTrigger + prepend('\t', stringOrEmpty(description)),
      content
    ];
  });
});

console.log(JSON.stringify(completions, undefined, 2));

/////////////////////////////////////////////////////////////

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