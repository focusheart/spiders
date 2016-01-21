# -*- coding: utf8 -*-
#!/usr/bin/env python
import mechanize
import cookielib
import time
import random
from datetime import datetime
from optparse import OptionParser

DEFAULT_PDF_PATH = './pdfs'

pdf_path = DEFAULT_PDF_PATH

def dbg(msg):
    print '%s %s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), msg)

def prepare_path(path):
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    pdf_path = path
        
def download_acm_proceedings(url):
    '''Download ACM Proceedings by given url
    the url MUST be flat layout of acm proceeding page
    for example:
        L@S2015: http://dl.acm.org/citation.cfm?id=2724660&preflayout=flat
    '''
    # create a browser()
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36')]
    
    # get the whole page
    dbg('Read page of %s' % url)
    r = br.open(url)
    links = [link for link in br.links(url_regex='ft_gateway')]
    dbg('Found %s PDF links' % len(links))
    
    # download each paper
    for i in range(len(links)):
        print '*'*40
        dbg('Begin download paper %s/%s' % (i, len(links)))
        br.follow_link(links[i])
        print br.response().info()
        pdf = br.response().read()
        open(os.path.join(pdf_path, 'NO.%s.pdf' % (1000+i)), 
            'wb').write(pdf)
        dbg('Saved paper %s/%s' % (i, len(links)))
        br.back()
        dbg('Done %s/%s' % (i, len(links)))
        slp = random.randint(5, 15)
        dbg('Sleep for %s seconds...' % slp)
        time.sleep(slp)


if __name__=='__main__':
    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url",
        help="ACM Proceedings FLAT URL to download.\nFox example: L@S2015: http://dl.acm.org/citation.cfm?id=2724660&preflayout=flat")
    parser.add_option("-p", "--path", dest="path",
        help="where to store the downloaded pdfs? default is ./pdfs")

    (options, args) = parser.parse_args()
    if options.path:
        PDF_PATH = 
    if options.url:
        download_acm_proceedings(options.url)
    else:
        parser.print_help()
