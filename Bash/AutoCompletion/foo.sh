_foo() 
{
    local current previous options         # define variables
    COMPREPLY=()
    current="${COMP_WORDS[COMP_CWORD]}"    # current word typed
    prevous="${COMP_WORDS[COMP_CWORD-1]}"  # previous word typed
    options="--help --verbose --version"   # list of options to complete

    if [[ ${current} == -* ]] ; then
        COMPREPLY=( $(compgen -W "${options}" -- ${current}) ) # the option completing is then handled by use of the compgen command via this line
        return 0
    fi
}
complete -F _foo foo