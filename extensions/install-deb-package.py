# Adds "Install Deb Package" to the right-click menu, only when every selected
# item is a .deb file. The install itself is done by the "Install Deb Package"
# Bash script next to this file.

import os
import subprocess

import gi

# Ubuntu 22.04 ships Nautilus API 3.0. Ubuntu 24.04 and later ship 4.0.
try:
    gi.require_version("Nautilus", "4.0")
except ValueError:
    gi.require_version("Nautilus", "3.0")
from gi.repository import GObject, Nautilus

SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "Install Deb Package")
DEB_MIME_TYPE = "application/vnd.debian.binary-package"


class InstallDebPackage(GObject.GObject, Nautilus.MenuProvider):
    # Nautilus 3.0 passes (window, files). Nautilus 4.0 passes (files).
    def get_file_items(self, *args):
        files = args[-1]
        is_local_deb = lambda f: f.get_uri_scheme() == "file" and f.is_mime_type(DEB_MIME_TYPE)
        if not files or not all(is_local_deb(f) for f in files):
            return []

        item = Nautilus.MenuItem(name="InstallDebPackage::Install", label="Install Deb Package")
        item.connect("activate", self.install, files)
        return [item]

    def install(self, menu, files):
        # Pass the selection the same way Nautilus passes it to scripts.
        paths = "".join(f.get_location().get_path() + "\n" for f in files)
        env = dict(os.environ, NAUTILUS_SCRIPT_SELECTED_FILE_PATHS=paths)
        subprocess.Popen([SCRIPT_PATH], env=env)
