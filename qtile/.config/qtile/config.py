# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import socket

from typing import List  # noqa: F401
from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
myTerm = "alacritty"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod],
        "h",
        lazy.layout.left(),
        lazy.layout.decrease_nmaster(),
        desc="Shrink window (MonadTall), decrease number in master pane (Tile)"
        ),
    Key([mod],
        "l",
        lazy.layout.right(),
        lazy.layout.increase_nmaster(),
        desc="Expand window (MonadTall), increase number in master pane (Tile)"
        ),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod],
        "space",
        lazy.layout.next(),
        desc="Move window focus to other window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),
    Key([mod],
        "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'),
    Key([mod],
        "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"],
        "j",
        lazy.layout.section_down(),
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc="Move window up"),
    Key([mod, "shift"],
        "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"],
        "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"],
        "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"],
        "j",
        lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launch terminal"),

    ### Stack controls
    Key([mod, "shift"],
        "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'),
    Key([mod],
        "space",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'),
    Key([mod, "shift"],
        "space",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Move Focus To Monitors
    Key([mod], "w", lazy.to_screen(0), desc='Keyboard focus to monitor 1'),
    Key([mod], "e", lazy.to_screen(1), desc='Keyboard focus to monitor 2'),
    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen(),
        desc='Move focus to next monitor'),
    Key([mod], "comma", lazy.prev_screen(), desc='Move focus to prev monitor'),

    # My Extra Bindings
    # My Extra Bindings
    Key([mod], "d", lazy.spawn("rofi -show run"), desc="Launch rofi"),
    # Media keys on keyboard
    Key([],
        "XF86AudioRaiseVolume",
        lazy.spawn("pulseaudio-ctl up"),
        desc="Increase Volume"),
    Key([],
        "XF86AudioLowerVolume",
        lazy.spawn("pulseaudio-ctl down"),
        desc="Decrease Volume"),
    Key([], "XF86AudioMute", lazy.spawn("pulseaudio-ctl mute"), desc="Mute"),
    Key([],
        "XF86AudioMicMute",
        lazy.spawn("pulseaudio-ctl mute-input"),
        desc="Mute Mic"),
    # Play and Pause Button
    Key([],
        "XF86AudioPlay",
        lazy.spawn("playerctl play"),
        desc="Play button on keyboard"),
    Key([],
        "XF86AudioPause",
        lazy.spawn("playerctl pause"),
        desc="Play button on keyboard"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl prev"), desc="Previous"),
    # Brightness buttons
    Key([],
        "XF86MonBrightnessUp",
        lazy.spawn("xbacklight -inc 10"),
        desc="Increase Brightness By 10"),
    Key([],
        "XF86MonBrightnessDown",
        lazy.spawn("xbacklight -dec 10"),
        desc="Decrease Brightness By 10"),
    Key([mod],
        "p",
        lazy.spawn("passmenu"),
        desc="Runs passmenu to access my password"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod],
            i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"],
            i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": "e1acff",
    "border_normal": "1D2330"
}

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(font="Ubuntu",
                   fontsize=10,
                   sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
                   section_fontsize=10,
                   border_width=2,
                   bg_color="1c1f24",
                   active_bg="c678dd",
                   active_fg="000000",
                   inactive_bg="a9a1e1",
                   inactive_fg="1c1f24",
                   padding_left=0,
                   padding_x=0,
                   padding_y=5,
                   section_top=10,
                   section_bottom=20,
                   level_shift=8,
                   vspace=3,
                   panel_width=200),
    layout.Floating(**layout_theme)
]
# layouts = [
#     layout.MonadTall(),
#     # layout.Columns(border_focus_stack='#d75f5f'),
#     layout.Max(),
#     # Try more layouts by unleashing below layouts.
#     # layout.Stack(num_stacks=2),
#     # layout.Bsp(),
#     # layout.Matrix(),
#     # layout.MonadWide(),
#     # layout.RatioTile(),
#     # layout.Tile(),
#     # layout.TreeTab(),
#     # layout.VerticalTile(),
#     # layout.Zoomy(),
# ]

colors = [
    ["#282c34", "#282c34"],  # panel background
    ["#3d3f4b", "#434758"],  # background for current screen tab
    ["#ffffff", "#ffffff"],  # font color for group names
    ["#ff5555", "#ff5555"],  # border line color for current tab
    ["#74438f", "#74438f"
     ],  # border line color for 'other tabs' and color for 'odd widgets'
    ["#4f76c7", "#4f76c7"],  # color for the 'even widgets'
    ["#e1acff", "#e1acff"],  # window name
    ["#ecbbfb", "#ecbbfb"]
]  # backbround for inactive screens

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

widget_defaults = dict(font="Ubuntu Mono Font",
                       fontsize=12,
                       padding=2,
                       background=colors[2])
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.Sep(linewidth=0,
                   padding=6,
                   foreground=colors[2],
                   background=colors[0]),
        widget.Image(
            filename="~/.config/qtile/icons/python-white.png",
            scale="False",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(myTerm)}),
        widget.Sep(linewidth=0,
                   padding=6,
                   foreground=colors[2],
                   background=colors[0]),
        widget.GroupBox(font="Ubuntu Bold",
                        fontsize=9,
                        margin_y=3,
                        margin_x=0,
                        padding_y=5,
                        padding_x=3,
                        borderwidth=3,
                        active=colors[2],
                        inactive=colors[7],
                        rounded=False,
                        highlight_color=colors[1],
                        highlight_method="line",
                        this_current_screen_border=colors[6],
                        this_screen_border=colors[4],
                        other_current_screen_border=colors[6],
                        other_screen_border=colors[4],
                        foreground=colors[2],
                        background=colors[0]),
        widget.Prompt(prompt=prompt,
                      font="Ubuntu Mono",
                      padding=10,
                      foreground=colors[3],
                      background=colors[1]),
        widget.Sep(linewidth=0,
                   padding=40,
                   foreground=colors[2],
                   background=colors[0]),
        widget.WindowName(
            foreground=colors[6],
            background=colors[0],
            padding=None,
        ),
        # widget.Systray(background=colors[0], padding=5),
        widget.Sep(linewidth=0,
                   padding=6,
                   foreground=colors[0],
                   background=colors[0]),
        widget.TextBox(
            text='',
            background=colors[0],
            foreground=colors[4],
            padding=0,
            fontsize=37,
            margin=-2,
        ),
        widget.Net(interface="wlp4s0",
                   format='{down}  {up}',
                   font="Ubuntu Nerd Font",
                   foreground=colors[2],
                   background=colors[4],
                   use_bits=False,
                   padding=5),
        widget.TextBox(text='',
                       background=colors[4],
                       foreground=colors[5],
                       padding=0,
                       fontsize=37),
        # widget.TextBox(
        #          text = " 🌡 TEMP NOT SHOWN ",
        #          padding = 2,
        #          foreground = colors[2],
        #          background = colors[5],
        #          fontsize = 11
        #          ),
        widget.ThermalSensor(foreground=colors[2],
                             background=colors[5],
                             threshold=90,
                             padding=5),
        widget.TextBox(text='',
                       background=colors[5],
                       foreground=colors[4],
                       padding=0,
                       fontsize=37),
        widget.TextBox(text="累",
                       font="Ubuntu Nerd Font",
                       padding=2,
                       foreground=colors[2],
                       background=colors[4],
                       fontsize=14),
        widget.CheckUpdates(
            update_interval=1800,
            distro="Arch_checkupdates",
            display_format="{updates} Updates",
            foreground=colors[2],
            mouse_callbacks={
                'Button1':
                lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')
            },
            background=colors[4]),
        widget.TextBox(text='',
                       background=colors[4],
                       foreground=colors[5],
                       padding=0,
                       fontsize=37),
        widget.TextBox(text="",
                       font="Ubuntu Nerd Font",
                       foreground=colors[2],
                       background=colors[5],
                       padding=0,
                       fontsize=14),
        widget.Memory(foreground=colors[2],
                      background=colors[5],
                      mouse_callbacks={
                          'Button1':
                          lambda: qtile.cmd_spawn(myTerm + ' -e htop')
                      },
                      padding=5),
        widget.TextBox(text='',
                       background=colors[5],
                       foreground=colors[4],
                       padding=0,
                       fontsize=37),
        widget.TextBox(text=" ₿",
                       padding=0,
                       foreground=colors[2],
                       background=colors[4],
                       fontsize=12),
        widget.BitcoinTicker(foreground=colors[2],
                             background=colors[4],
                             padding=5),
        widget.TextBox(text='',
                       background=colors[4],
                       foreground=colors[5],
                       padding=0,
                       fontsize=37),
        widget.TextBox(text=" Vol:",
                       foreground=colors[2],
                       background=colors[5],
                       padding=0),
        widget.Volume(
            foreground=colors[2],
            background=colors[5],
            padding=5,
        ),
        widget.TextBox(text='',
                       background=colors[5],
                       foreground=colors[4],
                       padding=0,
                       fontsize=37),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[0],
            background=colors[4],
            padding=0,
            scale=0.7),
        widget.CurrentLayout(foreground=colors[2],
                             background=colors[4],
                             padding=5),
        widget.TextBox(text='',
                       background=colors[4],
                       foreground=colors[5],
                       padding=0,
                       fontsize=37),
        widget.Clock(foreground=colors[2],
                     background=colors[5],
                     format="%A, %B %d - %H:%M "),
    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[
        7:8]  # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2  # Monitor 2 will display all widgets in widgets_list


def init_screens():
    return [
        Screen(
            top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
        Screen(
            top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20))
    ]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


# Drag floating layouts.
mouse = [
    Drag([mod],
         "Button1",
         lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod],
         "Button3",
         lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(title='Confirmation'),  # tastyworks exit box
    Match(title='Qalculate!'),  # qalculate-gtk
    Match(wm_class='kdenlive'),  # kdenlive    
    Match(wm_class='pinentry-gtk-2'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
