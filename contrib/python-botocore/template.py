pkgname = "python-botocore"
pkgver = "1.35.14"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-dateutil",
    "python-jmespath",
    "python-urllib3",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Core module supporting boto3 and aws cli"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/boto/botocore"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "21ee2fc9cd22d11ce924b08eab41433dbbf00f2e655ece89650e3e36999cc9a2"
# takes forever
options = ["!check"]
