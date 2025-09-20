# dwm

![Desktop](assets/desktop.png)

# Requeriments compilation tools for:

## Arch

```bash
sudo pacman -S --noconfirm base-devel libx11 libxft libxinerama wget unzip
```

## Debian

```bash
sudo apt install -y build-essential libxft-dev libxinerama-dev libx11-dev wget unzip
```

## Void

```bash
sudo xbps-install -y base-devel libx11-devel libxft-devel libxinerama-devel wget unzip
```

## Install the following packages

- xorg
- xorg-xinit or xinit
- dunst
- acpi
- brightnessctl
- pamixer
- pipewire
- lsd
- feh
- network-manager-applet
- pacman-contrib
- sensors
- pywal16
- network-manager-applet
- Font: JetBrainsMono Nerd Font
- [nsxiv](https://codeberg.org/nsxiv/nsxiv)

# Tips

### Add in this path "/etc/X11/xorg.conf.d/30-touchpad.conf"

```conf
Section "InputClass"
    Identifier "touchpad"
    MatchIsTouchpad "on"
    MatchDriver "libinput"
    Option "Tapping" "on"
    Option "NaturalScrolling" "true"
    Option "ScrollMethod" "twofinger"
EndSection

Section "InputClass"
    Identifier "mouse"
    MatchIsPointer "on"
    MatchDriver "libinput"
    Option "NaturalScrolling" "false"
EndSection
```

### These lines fix the functionality of mouse and touchpad
