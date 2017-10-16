import os

with open('slideshow.hdr', 'r') as hdr:
    header = hdr.read()

with open('slideshow.ftr', 'r') as ftr:
    footer = ftr.read()

with open('genshow.html', 'w') as gen:
    gen.write(header + '\n')

    IMAGES = 'images'
    #list = os.listdir(IMAGES)
    list = [os.path.join(dp, ff) for dp, dn, filenames in os.walk(IMAGES) for ff in filenames if "." in ff]
    numFiles = len(list)
    for ii,file in enumerate(list):
        block = '<div class="mySlides fade">\n<div class="numbertext">{}/{}</div>\n<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-src="{}" style="width:60%">\n</div>'.format(ii+1, numFiles, file)
        #print block
        gen.write(block + '\n')
    
    gen.write(footer + '\n')
