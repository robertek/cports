pkgname = "mimetreeparser"
pkgver = "24.08.1"
pkgrel = 0
build_style = "cmake"
make_check_args = ["-j1"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "gpgme-devel",
    "kcalendarcore-devel",
    "kcodecs-devel",
    "ki18n-devel",
    "kmbox-devel",
    "kmime-devel",
    "kwidgetsaddons-devel",
    "libkleo-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE parser for MIME trees"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-3.0-only AND GPL-3.0-only"
url = "https://invent.kde.org/pim/mimetreeparser"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/mimetreeparser-{pkgver}.tar.xz"
)
sha256 = "e379627c037cd7ac316c545756326ea873fac3e430380e3262377bee02a9ec4c"


@subpackage("mimetreeparser-devel")
def _(self):
    self.depends += [
        "ki18n-devel",
        "ki18n-devel",
        "kmbox-devel",
        "kmime-devel",
        "mailimporter-devel",
    ]
    return self.default_devel()