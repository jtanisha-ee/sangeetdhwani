import os

with open('slideshow.hdr', 'r') as hdr:
    header = hdr.read()

with open('slideshow.ftr', 'r') as ftr:
    footer = ftr.read()

"""
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-src="tanisha.jpg" />\n<img src="spinner.gif" data-src="realimage2.gif" />
"""

with open('genshow.html', 'w') as gen:
    gen.write(header + '\n')

    IMAGES = 'images'
    #IMAGES = '../../Downloads/slideshow/images'
    list = os.listdir(IMAGES)
    numFiles = len(list)
    for ii,file in enumerate(list):
        block = '<div class="mySlides fade">\n<div class="numbertext">{}/{}</div>\n<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-src="{}" style="width:60%">\n</div>'.format(ii+1, numFiles, '/'.join([IMAGES, file]))
        #print block
        gen.write(block + '\n')
    
    gen.write(footer + '\n')
