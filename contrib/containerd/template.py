pkgname = "containerd"
pkgver = "1.7.7"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = [
    "all",
    "man",
    f"REVISION=chimera-r{pkgrel}",
    f"VERSION={pkgver}",
]
make_install_args = ["install-man"]
make_check_target = "test"
make_check_args = ["TESTFLAGS_RACE="]
hostmakedepends = [
    "gmake",
    "go",
    "go-md2man",
]
makedepends = [
    "libbtrfs-devel",
    "libseccomp-devel",
    "linux-headers",
]
depends = [
    "cni-plugins",
    "runc",
]
pkgdesc = "Industry-standard container runtime"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/containerd/containerd"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "4c6042b13746a803766d76b07f756d03678a33a944b52c0b832c238609db1b2e"
# objcopy fails to split on ppc
# can't run tests inside namespaces
options = ["!debug", "!check"]


if self.profile().arch == "riscv64":
    broken = "cgo runtime stuff"


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def post_build(self):
    self.do("./bin/containerd", "config", "default")


def post_install(self):
    self.install_file(self.files_path / "config.toml", "etc/containerd")
    self.install_service(self.files_path / "containerd")


@subpackage("containerd-stress")
def _stress(self):
    self.pkgdesc = "Containerd benchmarking utility"

    return ["usr/bin/containerd-stress"]


@subpackage("containerd-ctr")
def _ctr(self):
    self.pkgdesc = "Debug / admin client for containerd"

    return ["usr/bin/ctr"]
