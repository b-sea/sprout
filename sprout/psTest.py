import re

import config

lookup = config.FILE_SAVE_FORMAT
lookup = lookup.replace('.', '\\.')

for x in config.FileNameKeys.hashValues():
    if x == config.FileNameKeys.Prefix:
        lookup = lookup.replace(config.FileNameKeys.Prefix, '(.+)')
        continue

    lookup = lookup.replace(x, '\\w+')

print lookup

fileName = 'Shot01_Anim_n2w.v001.ma'

found = re.match(lookup, fileName)
if found:
    print found.group(1)
