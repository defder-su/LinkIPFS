import os
import re
import gevent
import html

from Plugin import PluginManager
from Config import config
from Debug import Debug

@PluginManager.registerTo("UiRequest")
class UiRequestPlugin(object):
    def actionSiteMedia(self, path, **kwargs):
        if path.startswith("/media/ipfs/") or path.startswith("/media/ipns/"):
        	path_parts = self.parsePath(path)
        	ipfs_path = "/%s/%s" % (path_parts["address"], path_parts["inner_path"])
        	return self.actionRedirect302("https://ipfs.io%s" % (ipfs_path))
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
        