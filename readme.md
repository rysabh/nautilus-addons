# Initialize

## symlink new scripts folder
```bash
SCRIPTS_PATH="${HOME}/Applications/nautilus-addons/scripts"

mkdir -p "${SCRIPTS_PATH}"

# backup old scripts folder
if [ -e "${HOME}/.local/share/nautilus/scripts" ]; then
  mv "${HOME}/.local/share/nautilus/scripts" "${HOME}/.local/share/nautilus/scripts.bak-20260314-0430"
fi

# symlink new folder
ln -s "${SCRIPTS_PATH}" "${HOME}/.local/share/nautilus/scripts"

nautilus -q
```
---

## initialize templates
```bash
TEMPLATES_PATH="${HOME}/Applications/nautilus-addons/Templates"

mkdir -p "${TEMPLATES_PATH}"

# backup old templates folder
if [ -e "${HOME}/Templates" ]; then
  mv "${HOME}/Templates" "${HOME}/Templates.bak-20260314-0430"
fi

# symlink new templates folder
ln -s "${TEMPLATES_PATH}" "${HOME}/Templates"

nautilus -q
```

