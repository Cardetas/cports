pkgname = "umbriel"
pkgver = "0_git20261022"
pkgrel = 0
_commit = "5d657581e27e1a3fe604693779ca1405610f4f21 "
build_style = "meson"
configure_args = [
    "-Djemalloc=disabled",
    "-Dtest_ipc=disabled",
    "-Dtracy=disabled",
]
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = [
    "cairo-devel",
    "lcms2-devel",
    "libdrm-devel",
    "libinput-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "mesa-devel",
    "mesa-gbm-devel",
    "nlohmann-json",
    "pango-devel",
    "pixman-devel",
    "tomlplusplus-devel",
    "udev-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.20-devel",
]
depends = ["dbus", "xwayland-satellite"]
pkgdesc = "Wayland compositor with a custom effects renderer"
license = "MIT"
url = "https://github.com/noctalia-dev/umbriel"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "e51e770fd4b2bc4af2d05c3695bfd41708dba3b9b117f001b38f6b4fd554dc2"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("umbrielfx/LICENSE", name="LICENSE.umbrielfx")
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)
