from AppOpener import open , close
c = input('what you said?  ')
if 'open' in c:
    c = c.replace('open','')
    open(c)
if 'close' in c:
    c = c.replace('c','')
    close(c)
