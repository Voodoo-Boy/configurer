function! palette#Palette()
    call clearmatches()
    new
    setlocal buftype=nofile bufhidden=wipe noswapfile
    0read $VIMRUNTIME/rgb.txt
    let find_color = '^\s*\(\d\+\s*\)\{3}\zs\w*$'
    silent execute 'v/'.find_color.'/d'
    silent g/grey/d
    let namedcolors=[]
    1
    while search(find_color, 'W') > 0
        let w = expand('<cword>')
        call add(namedcolors, w)
    endwhile

    for w in namedcolors
        execute 'hi col_'.w.'_1 guibg=NONE'
        execute 'hi col_'.w.' guifg=black guibg='.w
        execute 'hi col_'.w.'_fg guifg='.w.' guibg=NONE'
        execute '%s/\<'.w.'\>/'.printf("%-28s%s", w, w).'/g'

        execute 'syn match col_'.w.'_1 '.'"'.w.'\s\+"'
        execute 'syn match col_'.w.'_fg '.'"'.w.'$"'
        execute 'syn keyword col_'.w.' '.w.' contained containedin=col_'.w.'_1'
    endfor
    1
    nohlsearch
    setlocal nocursorline
endfunction

function! palette#PaletteCompact()
    " Create scratch buffer and read palette string to it
    new
    setlocal buftype=nofile bufhidden=wipe noswapfile filetype=vim
    let CompactPalette = expand('<sfile>:p:h')."/CompactPalette"
    read CompactPalette
    0delete
    " Color
    setlocal nohlsearch
    call search('^" BEGIN_COLOR_LIST', 'e')
    while search('\w\+') > 0
      let w = expand('<cword>')
      if w == 'END_COLOR_LIST'
        break
      endif
      execute 'hi col_'.w.' guifg=black guibg='.w
      execute 'syn keyword col_'.w.' '.w.' contained containedin=vimLineComment'
    endwhile
    call search('^" BEGIN_COLOR_LIST')
    setlocal nocursorline
    normal 0zt
endfunction
