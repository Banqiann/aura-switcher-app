#!/usr/bin/env python3
"""Builds AURA's language models (lang/<code>.txt) for languages whose spelling dictionary may be missing.

A model is the language's most frequent words plus letter-trigram statistics, so AURA can tell
"a word of this language typed in the wrong layout" from "an English typo" without a dictionary.

Sources (CC BY-SA 4.0, compatible with AURA's GPL-3.0):
  FrequencyWords by Hermit Dave — https://github.com/hermitdave/FrequencyWords (content/2018/<code>/<code>_50k.txt)
  Belarusian: word counts from be.wikipedia.org articles (one "word count" pair per line, same format)

Languages built: en uk ru (trigrams only), be el he ar cs fi ro hu de es fr it pt tr sv bg.
Usage: python3 tools/langmodel.py <dir with <code>.txt word lists> <out dir> <code>...
"""
import math, sys, collections, unicodedata

WORDS, TRIGRAMS = 3000, 3000
TRIGRAMS_ONLY = {"en", "uk", "ru"}  # have dictionaries; their trigrams only weigh the other side

# Hangul is modelled as the jamo a person types (2-set), so the model matches AURA's keystroke text
L = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"; V = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"; T = " ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"
VP = {"ㅘ": "ㅗㅏ", "ㅙ": "ㅗㅐ", "ㅚ": "ㅗㅣ", "ㅝ": "ㅜㅓ", "ㅞ": "ㅜㅔ", "ㅟ": "ㅜㅣ", "ㅢ": "ㅡㅣ"}
TP = {"ㄳ": "ㄱㅅ", "ㄵ": "ㄴㅈ", "ㄶ": "ㄴㅎ", "ㄺ": "ㄹㄱ", "ㄻ": "ㄹㅁ", "ㄼ": "ㄹㅂ", "ㄽ": "ㄹㅅ", "ㄾ": "ㄹㅌ", "ㄿ": "ㄹㅍ", "ㅀ": "ㄹㅎ", "ㅄ": "ㅂㅅ"}

def jamo(w):
    out = ""
    for ch in w:
        v = ord(ch)
        if not 0xAC00 <= v <= 0xD7A3: out += ch; continue
        i = v - 0xAC00; vv = V[(i % 588) // 28]; t = T[i % 28]
        out += L[i // 588] + VP.get(vv, vv) + (TP.get(t, t) if i % 28 else "")
    return out

def build(src, code):
    words = []
    for line in open(src, encoding="utf-8"):
        p = line.split()
        # letters and marks (Devanagari vowel signs are marks), apostrophe, hyphen
        if len(p) == 2 and p[1].isdigit() and all(unicodedata.category(ch)[0] in "LM" or ch in "'ʼ-" for ch in p[0]):
            words.append((p[0].lower(), int(p[1])))
    words = [(jamo(w) if code == "ko" else w, f) for w, f in words[:40000]]
    c = collections.Counter()
    for w, f in words:
        t = "^" + w + "$"
        for i in range(len(t) - 2): c[t[i:i + 3]] += math.log(1 + f)
    tot = sum(c.values())
    top, seen = [], set()
    for w, _ in words if code not in TRIGRAMS_ONLY else []:
        if len(w) >= 2 and w not in seen: seen.add(w); top.append(w)
        if len(top) == (0 if code in TRIGRAMS_ONLY else WORDS): break
    # score = -10·log p, rounded; unseen trigrams get the last kept score + 10
    tri = [(g, round(-10 * math.log(v / tot))) for g, v in c.most_common(TRIGRAMS)]
    return top, tri

if __name__ == "__main__":
    src, out, codes = sys.argv[1], sys.argv[2], sys.argv[3:]
    for code in codes:
        top, tri = build(f"{src}/{code}.txt", code)
        with open(f"{out}/{code}.txt", "w", encoding="utf-8") as f:
            f.write(f"# AURA language model ({code}): {len(top)} frequent words, then letter trigrams with -10·ln p.\n")
            f.write("# Data: FrequencyWords by Hermit Dave (CC BY-SA 4.0)" if code != "be" else "# Data: be.wikipedia.org (CC BY-SA 4.0)")
            f.write(". Built by tools/langmodel.py\n")
            f.write(" ".join(top) + "\n")
            f.write("\n".join(f"{g}\t{s}" for g, s in tri) + "\n")
        print(code, len(top), "words", len(tri), "trigrams")
