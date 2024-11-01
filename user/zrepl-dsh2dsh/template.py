pkgname = "zrepl-dsh2dsh"
pkgver = "0.8.10"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
depends = ["zfs"]
provides = [self.with_pkgver("zrepl")]
pkgdesc = "One-stop ZFS backup & replication solution - dsh2dsh enhanced fork"
maintainer = "Robert David <robert.david@posteo.net>"
license = "MIT"
url = "https://github.com/dsh2dsh/zrepl"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "9aaaecd4dd431075dd64a4905c3c4f918b609fb14af88cfd0e868d68a9ea629a"

# check needs to run zfs command
options = ["!check"]

def install(self):
    self.install_bin("build/zrepl")
    self.install_file("dist/freebsd/etc/zrepl/zrepl.yml", "etc/zrepl", name="zrepl.yml.sample")
    self.install_files("internal/config/samples", "usr/share/examples", name="zrepl")
    self.install_service(self.files_path / "zrepl")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_license("LICENSE")
