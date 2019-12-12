################ My Settings ################

# set PS1
parse_git_branch()
{
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
PS1='${debian_chroot:+($debian_chroot)}\[\033[36m\]\u@\h\[\033[00m\] \[\033[37m\]\w\[\033[32m\]$(parse_git_branch) \[\033[00m\]\$ '

# aliases
alias ll='ls -lF --color=auto'
alias l.='ls -d .* --color=auto'
# alias l='ls -CF --color=auto'

alias ali='ssh wanghan@104.41.184.211'
alias azure='ssh -o ServerAliveInterval=10 wanghan@52.229.224.254'
export ALIVM=wanghan@39.107.109.141
export AZVM=wanghan@52.229.224.254
export GITHUB=https://github.com/Voodoo-Boy

echo ":P"
