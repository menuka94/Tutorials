_xm() 
{
    local current previous options base
    COMPREPLY=()
    current="${COMP_WORDS[COMP_CWORD]}"
    previous="${COMP_WORDS[COMP_CWORD-1]}"

    #
    #  The basic options we'll complete.
    #
    options="console create list"


    #
    #  Complete the arguments to some of the basic commands.
    #
    case "${previous}" in
        console)
            local running=$(for x in `xm list --long | grep \(name | grep -v Domain-0 | awk '{ print $2 }' | tr -d \)`; do echo ${x} ; done )
            COMPREPLY=( $(compgen -W "${running}" -- ${current}) )
            return 0
            ;;
        create)
            local names=$(for x in `ls -1 /etc/xen/*.cfg`; do echo ${x/\/etc\/xen\//} ; done )
            COMPREPLY=( $(compgen -W "${names}" -- ${current}) )
            return 0
            ;;
        *)
        ;;
    esac

   COMPREPLY=($(compgen -W "${options}" -- ${current}))  
   return 0
}
complete -F _xm xm