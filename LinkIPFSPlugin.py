import os
import re
import gevent
import html

from Plugin import PluginManager
from Config import config
from Debug import Debug

from urllib.request import urlopen, Request
from urllib.parse import quote
from urllib.error import URLError, HTTPError

@PluginManager.registerTo("UiRequest")
class UiRequestPlugin(object):
    def actionSiteMedia(self, path, **kwargs):
        if path.startswith("/media/ipfs/") or path.startswith("/media/ipns/"):
        	path_parts = self.parsePath(path)
        	ipfs_path = "/%s/%s" % (path_parts["address"], path_parts["inner_path"])
        	local_url = "http://127.0.0.1:8080%s" % (ipfs_path)
        	gateway_url = "https://ipfs.io%s" % (ipfs_path)        	
        	try:
        		request = Request(local_url)
        		response = urlopen(request, timeout=1)
        		return self.actionRedirect302(local_url)
        	except (HTTPError, URLError) as err:
        		return self.actionRedirect302(gateway_url)
        return super(UiRequestPlugin, self).actionSiteMedia(path, **kwargs)
    def actionRedirect302(self, url):
        self.start_response('302 Redirect', [('Location', str(url))])
        yield self.formatRedirect302(url)
    def formatRedirect302(self, url):
        return """
            <html>
            <body>
            Redirecting to <a href="{0}" target="_top">{0}</a>
            <script>
            window.top.location = "{0}"
            </script>
            </body>
            </html>
        """.format(html.escape(url))
        