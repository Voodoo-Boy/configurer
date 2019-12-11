" Desc: wanghan's _vimrc for gvim windows
" Date: 2018.07.23

" TODO support input parameter, path

" {{{ General
" clipboard
set clipboard+=unnamed              " Add system clipboard to vim

" Window Setting
set splitbelow                      " Split horizontal window to below
set splitright                      " Split vertical window to right

filetype indent plugin on           " turn on filtype detection, indent, plugin
syntax on
set backspace=indent,eol,start      " or set backspace=2, make backspace work like most other programs
set ruler                           " line number, column number, relative position at right bottom
set wrap                            " wrap too long line
set hls                             " highlight search results
set noincsearch                     " diable incremental search
set noshowmode                      " we use lightline plugin instead of default status line
set tabstop=4                       " tab width=4
set shiftwidth=4                    " shift width-4
set expandtab                       " On pressing tab, expand to space
set showmatch                       " show match brackets
set cinoptions=g-1                  " cindent style
set foldmethod=syntax
set foldlevel=99                    " set fold level to not fold at first
set cursorline                      " highlight current line
set laststatus=2                    " always display status line
set scrolloff=0                     " force no line above and below cursor when scrolling
set autochdir                       " auto change current work directory to the location of current file
set fileencodings=utf-8,ucs-bom,gbk2312,gbk,gb18030,cp936   " set candidate encodings for an existing file.
if has("multi_byte")
    if &termencoding == ""
        let &termencoding = &encoding
    endif
    set encoding=utf-8
    setglobal fileencoding=utf-8
    "setglobal bomb
    set fileencodings=ucs-bom,utf-8,latin1
endif
set lcs=tab:>-,trail:-      " Set chars to display invisible characters (:list! to toggle invisible symbol display)

" Remeber last exit postion for file
set viminfo='10,\"100,:20,%,n~/_viminfo
function! ResCur()
  if line("'\"") <= line("$")
    normal! g`"
    return 1
  endif
endfunction
augroup resCur
  autocmd!
  autocmd BufWinEnter * call ResCur()
augroup END

augroup wanghan_vim
    " Remove all other autocmds
    au!
	" Enable marker and fold all maker for vim files
    au Filetype vim setlocal foldmethod=marker | setlocal foldlevel=0
    " Clear all buffers when exit
    au VimLeavePre * exe '%bd'
    " Turn off automatically comment next line
    au Filetype * setlocal formatoptions-=c formatoptions-=r formatoptions-=o
    " Use cpp syntax for c# to enable folding
    au Filetype cs setlocal syntax=cpp
augroup end
" }}}

" {{{ Plugin
" Install vim-plugin if not exist.
if empty(glob('~/.vim/autoload/plug.vim'))
  silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

call plug#begin()
" Plugins
Plug 'ctrlpvim/ctrlp.vim'               " fuzzy find file and open.         'https://github.com/ctrlpvim/ctrlp.vim'
Plug 'itchyny/lightline.vim'            " great status line.                'https://github.com/itchyny/lightline.vim'
Plug 'tomtom/tcomment_vim'              " comment wrapped region.           'https://github.com/tomtom/tcomment_vim'
Plug 'ntpeters/vim-better-whitespace'   " display annoying whitespaces.     'https://github.com/ntpeters/vim-better-whitespace'
call plug#end()

" Plugin Setting
" lightline: Display full path of file;
"            Colorscheme=snow_dark
let g:lightline = {
      \ 'active': {
      \   'left': [ [ 'mode', 'paste' ], [ 'readonly', 'absolutepath', 'modified' ] ],
      \ }
      \ }
" }}}

" {{{ Key Mapping
" <leader>s edit .vimrc
map <leader>s :Vimrc<CR>
" \<space> source .vimrc
map <leader><space> :source $MYVIMRC<CR>
" <F2> for toggle paste mode
set pastetoggle=<F2>
" When yank in visual mode, cursor will stay at the last character.
vnoremap y y`]
" go to next/previous tab.
nnoremap <C-s>h :tabp<CR>
nnoremap <C-s><C-h> :tabp<CR>
nnoremap <C-s>l :tabn<CR>
nnoremap <C-s><C-l> :tabn<CR>
" go to next, previous, last edited buffer.
nnoremap <C-s>j :bn<CR>
nnoremap <C-s><C-j> :bn<CR>
nnoremap <C-s>k :bp<CR>
nnoremap <C-s><C-k> :bp<CR>
nnoremap <C-s>s :b#<CR>
nnoremap <C-s><C-s> :b#<CR>
" resize splited window.
nnoremap <leader>= :vertical resize +4<CR>
nnoremap <leader>- :vertical resize -4<CR>
nnoremap <leader>0 <C-w>=
"double click <Esc> to set nohls
nnoremap <Esc><Esc> :nohlsearch<Bar>:echo<CR>
"<leader>b to build.
nnoremap <leader>b :ccl<CR>:wa<CR>:silent make\|redraw!\|copen<CR><C-W>t<C-W>H
"<Ctrl-j> to next error.
nnoremap <C-j> :cnext<CR>
"<leader>i to display invisible characters.
nnoremap <leader>i :set list!<CR>
" }}}

" {{{ Custom Highlight
" Clang Comment
autocmd filetype c,cpp syn match   myLINK   "https\=://\S*"
autocmd filetype c,cpp syn keyword myREF    contained REF
autocmd filetype c,cpp syn keyword myDEBUG  contained DEBUG
autocmd filetype c,cpp syn keyword myTODO   contained TODO
autocmd filetype c,cpp syn keyword myNOTE   contained NOTE
autocmd filetype c,cpp syn keyword myLEARN  contained LEARN
autocmd filetype c,cpp syn keyword myNAME   contained WHAN Whan whan DAVID David
autocmd filetype c,cpp syn cluster cCommentGroup    add=myTODO,myNOTE,myLEARN,myNAME,myDEBUG,myREF,myLINK

highlight myDEBUG   cterm=bold              ctermfg=Green       ctermbg=none    gui=bold              guifg=LightGoldenrod1     guibg=NONE
highlight myTODO    cterm=bold              ctermfg=Yellow      ctermbg=none    gui=bold              guifg=SkyBlue             guibg=NONE
highlight myNOTE    cterm=bold              ctermfg=Blue        ctermbg=none    gui=bold              guifg=LightSteelBlue1     guibg=NONE
highlight myLEARN   cterm=bold,standout     ctermfg=Yellow      ctermbg=none    gui=bold,standout     guifg=Wheat               guibg=NONE
highlight myNAME    cterm=italic,underline  ctermfg=DarkGreen   ctermbg=none    gui=italic,underline  guifg=fg                  guibg=NONE
highlight myREF     cterm=bold,underline    ctermfg=DarkGreen   ctermbg=none    gui=bold,underline    guifg=DarkOliveGreen1     guibg=NONE
highlight myLINK    cterm=italic,underline  ctermfg=DarkGreen   ctermbg=none    gui=italic,underline  guifg=DarkOliveGreen1     guibg=NONE
" }}}

" {{{ Custom Command
" Toggle auto comment
let g:NoAutoComment=1
function! ToggleAutoComment()
  if g:NoAutoComment == 1
	setlocal formatoptions+=cro
	let g:NoAutoComment = 0
  else
	setlocal formatoptions-=cro
	let g:NoAutoComment = 1
  endif
endfunction
command! Comment call ToggleAutoComment()

" Tab2Space & Space2Tab
:command! -range=% -nargs=0 Tab2Space execute '<line1>,<line2>s#^\t\+#\=repeat(" ", len(submatch(0))*' . &ts . ')'
:command! -range=% -nargs=0 Space2Tab execute '<line1>,<line2>s#^\( \{'.&ts.'\}\)\+#\=repeat("\t", len(submatch(0))/' . &ts . ')'

" Open vimrc
if has('win32')
    let VimrcFile="~/_vimrc"
else
    let VimrcFile="~/.vimrc"
endif
command! Vimrc execute 'e '.VimrcFile

" Open a windows explorer of current directory
command! WinExplore execute '!start explorer .'

" Remove all ^M
command! UnixEOL execute '%s///g'

" Alias
"cabbrev cdwsa cd C:\Users\t-hawan\Source\Repos\WSAMicrosoftDoc
" }}}

" {{{ Misc
" Json Formatter
function! FormatJSON()
  %!python -m json.tool
endfunction
autocmd filetype json nnoremap <leader>f :call FormatJSON()<CR>

" Color palette
command! Palette call palette#Palette()
command! PaletteCompact call palette#PaletteCompact()
" }}}
