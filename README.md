# Initialize

## symlink new scripts folder
```bash
REPO_PATH="${HOME}/Applications/nautilus-addons"
SCRIPTS_PATH="${REPO_PATH}/scripts"

mkdir -p "${SCRIPTS_PATH}"
mkdir -p "${HOME}/.local/share/nautilus"

# remove old scripts folder or symlink
rm -rf -- "${HOME}/.local/share/nautilus/scripts"

# symlink new folder
ln -s "${SCRIPTS_PATH}" "${HOME}/.local/share/nautilus/scripts"

nautilus -q
```
---

## initialize templates
```bash
TEMPLATES_PATH="${REPO_PATH}/Templates"

mkdir -p "${TEMPLATES_PATH}"

# remove old templates folder or symlink
rm -rf -- "${HOME}/Templates"

# symlink new templates folder
ln -s "${TEMPLATES_PATH}" "${HOME}/Templates"

nautilus -q
```

# Nautilus Add-on Scripts

Small Nautilus right-click scripts for copying paths, creating files/shortcuts, changing permissions, and opening selections in editors.

## Install

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install nautilus zenity libnotify-bin xclip
```

Optional:

```bash
# sudo snap install code --classic
# sudo apt install sublime-text
```

Notes:

- `xclip` is for `Copy Path`
- `code` is for `Open in VS Code`
- `sublime-text` is only for `Open in Sublime Text`
