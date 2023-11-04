# Some programs like Gparted and etcher usb flashing requires some authentication
# agent to run at background.
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# easyeffects for sound eq and mic settings
# easyeffects --gapplication-service

# wifi
nm-applet &

# Ssh daemon
eval "$(ssh-agent -s)"

# gnome-keyring-daemon
eval $(gnome-keyring-daemon --start)
export SSH_AUTH_SOCK

# load Xresources
xrdb -load ~/.Xresources

/usr/bin/gammastep-indicator -l ${RS_LAT}:${RS_LON} -m wayland -t ${RS_DAY}:${RS_NIGHT}
