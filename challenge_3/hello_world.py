import wikipedia as wiki

ARTICLE = "\"Hello,_World!\"_program"

print(wiki.summary(ARTICLE, auto_suggest=False))