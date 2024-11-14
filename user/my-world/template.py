pkgname = "my-world"
pkgver = "0.2"
pkgrel = 0
build_style = "meta"
pkgdesc = "Robertek's package selection"
maintainer = "Robertek <robert.david@posteo.net>"
license = "custom:meta"
url = "https://github.com/robertek"


@subpackage("my-world-base")
def _(self):
    self.subdesc = "base system"
    self.install_if = [self.parent]
    self.depends = [
            "base-full",
            "fwupd",
            "chimera-repo-user",
            "chimerautils",
            "cronie",
            "linux-lts",
            "linux-lts-zfs-bin",
            "tlp",
            "zfs",
            "zsh",
    ]
    return []

@subpackage("my-world-firmware")
def _(self):
    self.subdesc = "firmware"
    self.install_if = [self.parent]
    self.depends = [
            "!base-full-firmware", # a lot of unnecessary firmware
            "firmware-linux-i915",
            "firmware-linux-intel-audio",
            "firmware-linux-intel-bt",
            "firmware-linux-iwlwifi",
    ]
    return []

@subpackage("my-world-net")
def _(self):
    self.subdesc = "network tools"
    self.install_if = [self.parent]
    self.depends = [
            "!base-full-net",
            "bind-progs",
            "curl",
            "dnsmasq",
            "networkmanager",
            "networkmanager-openconnect",
            "nmap",
            "openssh",
            "wget2",
            "wireguard-tools-wg-quick",
            "!resolvconf-symlink", # static dnsmasq resolv.conf
    ]
    return []

@subpackage("my-world-tools")
def _(self):
    self.subdesc = "cli tools"
    self.install_if = [self.parent]
    self.depends = [
            "bat",
            "bpftrace",
            "delta",
            "dmidecode",
            "eza",
            "fd",
            "fzf",
            "git",
            "gptfdisk",
            "htop",
            "imagemagick",
            "jq",
            "lsof",
            "nodejs",
            "nvme-cli",
            "powertop",
            "ripgrep",
            "screen",
            "smartmontools",
            "starship",
            "strace",
            "tmux",
            "unzip",
            "vim",
            "xlsclients",
            "yt-dlp",
    ]
    return []

@subpackage("my-world-devel")
def _(self):
    self.subdesc = "development tools"
    self.depends = [
            "android-tools",
            "ctags",
            "gdb",
            "github-cli",
            "openssl-devel",
            "pkgconf",
            "udev-devel",
    ]
    return []

@subpackage("my-world-printing")
def _(self):
    self.subdesc = "printing tools"
    self.install_if = [self.parent]
    self.depends = [
            "cups-filters",
            "hplip",
            "system-config-printer",
    ]
    return []

@subpackage("my-world-fonts")
def _(self):
    self.subdesc = "fonts"
    self.install_if = [self.parent]
    self.depends = [
            "!base-full-fonts", # cjk fonts not needed
            "fonts-dejavu",
            "fonts-liberation",
    ]
    return []

@subpackage("my-world-plasma")
def _(self):
    self.subdesc = "plasma desktop"
    self.depends = [
            "discover",
            "dolphin-plugins",
            "ffmpegthumbnailer", # video thumbnails
            "kinfocenter",
            "!mesa-vulkan",
            "plasma-desktop",
            "!plasma-desktop-accessibility-meta",
            "!plasma-desktop-apps-meta",
            "!plasma-desktop-devtools-meta",
            "!plasma-desktop-games-meta",
            "!plasma-desktop-kdepim-meta",
            "!plasma-desktop-multimedia-meta",
            "xdg-desktop-portal-gnome",
    ]
    return []

@subpackage("my-world-apps")
def _(self):
    self.subdesc = "plasma and gui apps"
    self.depends = [
            "ark",
            "gwenview",
            "kalk",
            "kate",
            "kdeconnect",
            "ktorrent",
            "okular",
            "skanlite",
            "spectacle",
            "yakuake",
    ]
    return []
