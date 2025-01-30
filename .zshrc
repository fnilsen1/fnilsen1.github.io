export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="robbyrussell"
plugins=(git zsh-syntax-highlighting)

source $ZSH/oh-my-zsh.sh
eval "$(starship init zsh)"

alias matlab="/usr/local/MATLAB/R2024b/bin/matlab -opengl"
alias slice="python3 '/home/morad/Clone go here/fnilsen1.github.io/Python Projects/Enkeltfiler/slice.py'"
alias ripes="./Downloads/Ripes-v2.2.6-linux-x86_64.AppImage &"
alias naob="python3 '/home/morad/Clone go here/fnilsen1.github.io/Python Projects/Enkeltfiler/naob.py'"
alias gcc=""

# Kilde: (Kleven, 2024), https://gitlab.com/farlusiva/dotfiles/-/blob/master/zsh/.zshrc
# ranger_cd for the shell
ranger_cd() {
    temp_file="$(mktemp -t "ranger_cd.XXXXXXXXXX")"
    env ranger --choosedir="$temp_file" "$@"
    if chosen_dir="$(cat -- "$temp_file")" && [ -n "$chosen_dir" ] && [ "$chosen_dir" != "$PWD" ]; then
        builtin cd -- "$chosen_dir"
    fi
    rm -f -- "$temp_file"
}

# https://thevaluable.dev/zsh-line-editor-configuration-mouseless/
_ranger_cd() {
	CUTBUFFER=""
	zle .kill-whole-line
	zle -U " ranger_cd
$CUTBUFFER"
}

# This binds Ctrl-O to ranger-cd:
zle -N _ranger_cd
bindkey "^O" _ranger_cd

export EDITOR=code
export VISUAL=code
#neofetch --ascii_distro Debian
neofetch --ascii_distro NixOS