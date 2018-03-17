set nu
set hls
syntax on
set termencoding=utf-8
set encoding=utf-8
set fileencodings=ucs-bom,utf-8,cp936
set fileencoding=utf-8
set tabstop=4
filetype on
set bex=.bak
set backup
set list
set listchars=tab:>-,trail:-
set paste
highlight Comment ctermfg =Magenta
"au BufNewFile,BufRead *.pl call SetSpace()
au BufNewFile,BufRead *.pl set expandtab
au BufNewFile,BufRead *.py set expandtab
func SetSpace()
    if &filetype == 'pl'
        set expandtab
    endif
    if &filetype == 'py?
        set expandtab
    endif
endfunc
