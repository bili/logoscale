# coding: utf8

import sys
import os
import string
from PIL import Image

#自动创建指定的各种尺寸的logo
#python crop.py 1024.png ./ -o 90 100 192
#python crop.py 1024.png ./
def crop():
    #只允许创建的尺寸
    includes = ''

    sizes = []
    name = sys.argv[1]
    folder = sys.argv[2]

    if len(sys.argv) > 4:
        if sys.argv[3] == '-o': 
            includes = sys.argv[4:]

    icon = Image.open(name)
    ext = os.path.splitext(name)[1][1:]

    if includes:
        for inc in includes:
            sizes.append((string.atoi(inc), string.atoi(inc)))
    else:
        #默认创建的所有尺寸
        sizes = [ 
                (29, 29),
                (40, 40),
                (48, 48),
                (50, 50),
                (57, 57),
                (58, 58),
                (72, 72),
                (76, 76),
                (80, 80),
                (96, 96),
                (100, 100),
                (114, 114),
                (120, 120),
                (144, 144),
                (152, 152),
                (320, 320),
                (512, 512),
                (640, 640),
                (1024, 1024),
                (2048, 2048)
                ]

    #重置大小
    for size in sizes:
        img = icon.resize(size, Image.ANTIALIAS)
        w, h = size
        img.save('%s/%s_%s.%s' % (folder, w, h, ext), icon.format)

crop()
