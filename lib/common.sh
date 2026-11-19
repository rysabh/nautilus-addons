# Shared helpers for the Nautilus scripts. Each script sets SCRIPT_NAME, then
# sources this file. It lives outside scripts/ because Nautilus shows every
# file in that folder as a menu entry.

notify() {
  if command -v notify-send >/dev/null 2>&1; then
    notify-send "$SCRIPT_NAME" "$1"
  fi
}

die() {
  notify "$1"
  printf '%s: %s\n' "$SCRIPT_NAME" "$1" >&2
  exit 1
}

# Prints the selected local paths, one per line, without blank lines.
selected_paths() {
  printf '%s\n' "${NAUTILUS_SCRIPT_SELECTED_FILE_PATHS:-}" | sed '/^$/d'
}

copy_to_clipboard() {
  if command -v xclip >/dev/null 2>&1 && xclip -selection clipboard; then
    return 0
  fi

  if command -v xsel >/dev/null 2>&1 && xsel --clipboard --input; then
    return 0
  fi

  if command -v wl-copy >/dev/null 2>&1 && wl-copy; then
    return 0
  fi

  return 1
}

# Prints the first candidate that can be run. A candidate is a command name
# or an absolute path; command -v handles both.
find_command() {
  local candidate

  for candidate in "$@"; do
    if command -v "$candidate" >/dev/null 2>&1; then
      command -v "$candidate"
      return 0
    fi
  done

  return 1
}
