# we call it this because 'glycin' is for the rust crate, and -loaders is for the loaders
pkgname = "glycin-loaders"
pkgver = "1.1.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "cargo-auditable",
    "gettext",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "cairo-devel",
    "gtk4-devel",
    "libheif-devel",
    "libjxl-devel",
    "librsvg-devel",
    "libseccomp-devel",
    "pango-devel",
    "rust-std",
]
depends = ["bubblewrap"]
checkdepends = [*depends]
pkgdesc = "Sandboxed and extendable image decoding"
maintainer = "triallax <triallax@tutanota.com>"
license = "MPL-2.0 OR LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/sophie-h/glycin"
source = f"$(GNOME_SITE)/glycin/{pkgver[:-2]}/glycin-{pkgver}.tar.xz"
sha256 = "2ca8d6146f0d01e91aaa940b930d6527b73f4ce364a13aa3c3e68e3d59e990df"
# gobject-introspection
# check: for some divine reason, it always passes locally and never on the builders (??)
options = ["!cross", "!check"]


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)
    # so target/release is not triple-prefixed for buildsystem integration
    del self.make_env["CARGO_BUILD_TARGET"]


@subpackage("libglycin-devel")
def _(self):
    return self.default_devel()


# matches upstream lib naming
@subpackage("libglycin-gtk4")
def _(self):
    self.subdesc = "C GTK4 bindings"
    self.depends = [self.parent]
    return [
        "lib:libglycin-gtk4-1.so.*",
        "usr/lib/girepository-1.0/GlyGtk4-1.typelib",
    ]


@subpackage("libglycin")
def _(self):
    self.subdesc = "C bindings"
    self.depends = [self.parent]
    return [
        "lib:libglycin-1.so.*",
        "usr/lib/girepository-1.0/Gly-1.typelib",
    ]