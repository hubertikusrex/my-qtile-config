###################
### Importieren ###
###################

import os
import subprocess
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

##############
### Farben ###
##############

#################
### Shortcuts ###
#################

mod = "mod4"
terminal = "alacritty"
filemanager = "ranger"

keys = [
    ###############
    ### Layouts ###
    ###############

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    #############
    ### Fokus ###
    #############

    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    
    ###############
    ### Bewegen ###
    ###############

    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    
    ##############################
    ### Vergrößern/Verkleinern ###
    ##############################

    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    ####################
    ### Apps/Befehle ###
    ####################

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.spawn("rofi -show power-menu -modi power-menu:~/Github/Important/rofi-power-menu/./rofi-power-menu"), desc="Power Menu"),
    Key(["control"], "space", lazy.spawn("rofi -show drun -show-icons"), desc="Launch rofi drun"),
    Key([mod], "e", lazy.spawn("alacritty -e ranger"), desc="Launch ranger filemanager"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch firefox"),
    Key(["mod1"], "Tab", lazy.spawn("rofi -show window -show-icons"), desc="Launch rofi drun"),

   
    #############
    ### Audio ###
    #############

    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%-"), desc="Lower Volume by 5%"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+"), desc="Raise Volume by 5%"),
    Key([], "XF86AudioMute", lazy.spawn("amixer sset Master 1+ toggle"), desc="Mute/Unmute Volume"),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"), 

]

#######################
### Floating Layout ###
#######################


###############
### Layouts ###
###############

layouts = [
    layout.Columns( border_width=3, margin=8),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    layout.MonadWide(margin=8),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

##################
### Schriftart ###
##################

widget_defaults = dict(
    font="RobotoMonoNerdFont-Medium.ttf",
    fontsize=20,
    padding=3,
)
extension_defaults = widget_defaults.copy()

######################
### Eigene Gruppen ###
######################

groups = [Group('󰋜'), 
          Group('󰭹'), 
          Group('󰝚'),
          Group('󰊴'),
          Group('󰅩 ')]

group_keys = ["1", "2", "3", "4", "5"]

for i in range(len(groups)):
    group_key = group_keys[i]
    group_name = groups[i].name
    keys.append(Key([mod], group_key, lazy.group[group_name].toscreen()))
    keys.append(Key([mod, "control"], group_key, lazy.window.togroup(group_name, switch_group = False)))
    keys.append(Key([mod, "shift"], group_key, lazy.window.togroup(group_name, switch_group = True)))

##########################
### Gruppen Dekoration ###
##########################

powericon = {
    "decorations": [
        RectDecoration(colour="#2e3440", radius=15, filled=True, group=True, extrawidth=0)
    ],
}

arbeitsflächen = {
    "decorations": [
        RectDecoration(colour="#2e3440", radius=15, filled=True, group=True, extrawidth=5)
    ],
}

layouticon = {
    "decorations": [
        RectDecoration(colour="#2e3440", radius=15, filled=True, group=True, extrawidth=20)
    ],
}

windowname = {
    "decorations": [
        RectDecoration(colour="#2e3440", radius=15, filled=True, group=True, extrawidth=2)
    ],
}

wetter = {
    "decorations": [
        RectDecoration(colour="#2e3440", radius=15, filled=True, group=True, extrawidth=5)
    ],
}

telemetrie = {
    "decorations": [
        RectDecoration(colour="#2e3440", radius=15, filled=True, group=True, extrawidth=5)
    ],
}

volume = {
    "decorations": [
        RectDecoration(colour="#2e3440", radius=15, filled=True, group=True, extrawidth=5)
    ],
}

uhrzeit = {
    "decorations": [
        RectDecoration(colour="#2e3440", radius=15, filled=True, group=True, extrawidth=5)
    ],
}

###############
### Taskbar ###
###############

screens = [
    Screen(
        top=bar.Bar(
            [   
                ###################
                ### Linke Seite ###
                ###################

                widget.Sep(size_percent=0, linewidth=5),
                widget.Image(filename='~/Bilder/Icons/archlinux.png', margin=3, **powericon, mouse_callbacks = {'Button1': 
                             lazy.spawn("rofi -show power-menu -modi power-menu:~/Github/Important/rofi-power-menu/./rofi-power-menu")}),
                widget.Sep(size_percent=0, linewidth=5),
                widget.Sep(size_percent=0, linewidth=5, **arbeitsflächen),
                widget.GroupBox(highlight_method='text', fontsize=25, margin_y=4, spacing=25, padding=10, inactive='#ffffff', disable_drag=True, **arbeitsflächen),
                # widget.Sep(size_percent=0, linewidth=5),
                # widget.CurrentLayoutIcon(scale=0.7, **layouticon),
                widget.Spacer(),

                #####################
                ### Goldene Mitte ###
                #####################

                widget.OpenWeather(cityid='2881509', format='     {main_temp} °{units_temperature} {weather_details} ', language='de', **wetter),
                widget.Spacer(),

                ####################
                ### Rechte Seite ###
                ####################

                widget.Systray(),
                widget.Sep(size_percent=0, linewidth=5),
                widget.CPU(format='    {load_percent}%',**telemetrie),
                widget.Memory(format='   {MemPercent}% ',**telemetrie),

                widget.Sep(size_percent=0, linewidth=5),
                widget.Volume(volume_app='flatpak run org.pulseaudio.pavucontrol', fmt='   {} ', step=5, **volume),

                widget.Sep(size_percent=0, linewidth=5),
                widget.Clock(format=' 󰥔  %d.%m %H:%M ', **uhrzeit),
                widget.Sep(size_percent=0, linewidth=5),
                
            ],
            32, ### Taskbar Höhe
            background="#00000000",
            margin=5
        ),

        #######################
        ### Hintergrundbild ###
        #######################
        
        wallpaper='~/Bilder/Hintergrundbilder/Porsche1.jpg',
    ),
]

#####################
### Default Qtile ###
#####################

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

######################
### Autostart Apps ###
######################


from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])
