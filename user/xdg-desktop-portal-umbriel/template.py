pkgname = "xdg-desktop-portal-umbriel"
pkgver = "0_git20261022"
pkgrel = 0
_commit = "1cc6eb18ba0d6c82dd66999646d7e554f76a85b6"
build_style = "meson"
configure_args = ["-Dpicker=enabled"]
hostmakedepends = ["glib-devel", "meson", "pkgconf", "wayland-progs"]
makedepends = [
    "cairo-devel",
    "gtk4-devel",
    "libdrm-devel",
    "mesa-gbm-devel",
    "nlohmann-json",
    "pipewire-devel",
    "sdbus-cpp-devel",
    "tomlplusplus-devel",
    "wayland-devel",
    "wayland-protocols",
]
depends = ["xdg-desktop-portal", "xdg-desktop-portal-gtk"]
pkgdesc = "XDG desktop portal backend for Umbriel"
license = "MIT"
url = "https://github.com/noctalia-dev/xdg-desktop-portal-umbriel"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "862e2ae91bbd5408ac67d60803f5445776c77e4c44de2dc435197b895482b141"


def post_install(self):
    self.install_license("LICENSE")
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)
