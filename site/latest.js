// The latest release, for the update page (/update/). Edit on every release: version + what's new.
// Notes: Ukrainian and English; other languages show the English notes.
const LATEST = {
  version: "0.7.2",
  notes: {
    uk: ["Однолітерне слово перед виправленим теж виправляється: «z ,ele» → «я буду», «Ш think» → «I think». Англійське «a» не чіпає.",
         "Смайли на кшталт :D, :P, :O більше не перетворюються на «ЖВ», «ЖЗ», «ЖЩ».",
         "Якщо словник мови не завантажено (macOS приймає будь-яке слово), AURA не виправляє автоматично в цю мову — англійські описки більше не стають нісенітницею. Подвійний ⇧ працює як раніше.",
         "Решта — як у 0.7.1: «Перевірити оновлення…», буфер обміну не губиться, виправлення для VS Code, консолей і Caps Lock."],
    en: ["A one-letter word before a corrected word is corrected too: “z ,ele” → “я буду”, “Ш think” → “I think”. An English “a” is left alone.",
         "Emoticons like :D, :P, :O are no longer turned into «ЖВ», «ЖЗ», «ЖЩ».",
         "If a language's dictionary isn't downloaded (macOS then accepts any word), AURA won't autocorrect into it, so English typos no longer turn into gibberish. Double ⇧ works as before.",
         "Everything else as in 0.7.1: “Check for updates…”, the clipboard is kept, fixes for VS Code, consoles and Caps Lock."],
  },
};
