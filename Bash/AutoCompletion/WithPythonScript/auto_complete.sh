_complete_prog()
{
    local CURRENT="${COMP_WORDS[$COMP_CWORD]}"
    COMPREPLY=( $(python autocomplete.py "$CURRENT" ) )
}
complete -F _complete_prog prog;