local wezterm = require("wezterm")

return {
  default_prog = { "msh.exe" },
  font = wezterm.font_with_fallback({
    "Iosevka Term",
    "Iosevka",
    "JetBrains Mono",
  }),
  color_scheme = "Chalk",
  keys = {
    {
      key = "Enter",
      mods = "ALT",
      action = wezterm.action.SpawnTab("CurrentPaneDomain"),
    },
    {
      key = ";",
      mods = "ALT",
      action = wezterm.action.SplitHorizontal({ domain = "CurrentPaneDomain" }),
    },
    {
      key = "-",
      mods = "ALT",
      action = wezterm.action.SplitVertical({ domain = "CurrentPaneDomain" }),
    },
    {
      key = "j",
      mods = "ALT",
      action = wezterm.action.ActivatePaneDirection("Down"),
    },
    {
      key = "k",
      mods = "ALT",
      action = wezterm.action.ActivatePaneDirection("Up"),
    },
    {
      key = "l",
      mods = "ALT",
      action = wezterm.action.ActivatePaneDirection("Right"),
    },
    {
      key = "h",
      mods = "ALT",
      action = wezterm.action.ActivatePaneDirection("Left"),
    },
    {
      key = "n",
      mods = "ALT",
      action = wezterm.action.ActivateTabRelative(1),
    },
    {
      key = "p",
      mods = "ALT",
      action = wezterm.action.ActivateTabRelative(-1),
    },
  },
}
