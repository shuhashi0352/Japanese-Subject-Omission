import fugashi

# This is our sample text.
# "Fugashi" is a Japanese snack primarily made of gluten.
text = "病理所見は中心静脈周囲に広範な肝細胞脱落，出血，マクロファージ，リンパ球，形質細胞浸潤を認めた．"

# The Tagger object holds state about the dictionary.
tagger = fugashi.GenericTagger('-r /opt/homebrew/etc/mecabrc -d /opt/homebrew/lib/mecab/dic/ipadic')

words = [word.surface for word in tagger(text)]
result = " ".join(words)
print(result)