# -*- coding: utf-8 -*-

import httplib
import urllib

TIMEOUT=3
urllib.socket.setdefaulttimeout(TIMEOUT)

udpaddr = '255.0.0.65:1234'
try:
    connectp = urllib.urlopen('http://proxytv.ru/iptv/php/onechan.php?ip= %s' % udpaddr)
except:
    print 'Сервер не ответил'
else:
    udpxyaddr = connectp.read()
    try:
        connectu = httplib.HTTPConnection(udpxyaddr)
    except:
        print 'udpxy дохлый'
    else:
        connectu.request('GET', '/status')
        gresponse = connectu.getresponse()
        if gresponse.status == 200:
            namefile = 'plist.m3u'
            namechann = 'Arena'
            extm3u = '#EXTM3U\n'
            extinf = '#EXTINF:-1,%s\n' % namechann
            stream = 'http://%s/udp/%s\n' % (udpxyaddr, udpaddr)
            m3ufile = open(namefile, 'w')
            m3ufile.write(extm3u)
            m3ufile.write(extinf)
            m3ufile.write(stream)
            m3ufile.close()
            print 'Плейлист сформирован успешно'
        if gresponse.status != 200:
            print 'Это не udpxy'
            
            
    
