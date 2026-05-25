


def setup(c):

    colors = {
        'base' : '#100b12',
        'base-light' : '#171019',
        'text' : '#ffffff',
    
        'pink' : '#ffc5d3',
        'pink-dark' : '#ff809f',
        'yellow' : '#ffff99',
        'orange' : '#ff964f',
        'red' : '#ff746c',
        'purple' : '#b198d9',
    }


    c.colors.completion.category.bg = colors['base']
    c.colors.completion.category.border.bottom = colors['base']
    c.colors.completion.category.border.top = colors['base']
    c.colors.completion.category.fg = colors['pink']
    c.colors.completion.even.bg = colors['base']
    c.colors.completion.odd.bg = colors['base-light']
    c.colors.completion.fg = colors['text']

    c.colors.completion.item.selected.bg = colors['pink']
    c.colors.completion.item.selected.border.bottom = colors['pink']
    c.colors.completion.item.selected.border.top = colors['pink']
    c.colors.completion.item.selected.fg = colors['base']
    c.colors.completion.item.selected.match.fg = colors['pink-dark']
    c.colors.completion.match.fg = colors['pink-dark']

    c.colors.completion.scrollbar.bg = colors['base']
    c.colors.completion.scrollbar.fg = colors['base-light']


    c.colors.downloads.bar.bg = colors['base']
    c.colors.downloads.error.bg = colors['base']
    c.colors.downloads.start.bg = colors['base']
    c.colors.downloads.stop.bg = colors['base']

    c.colors.downloads.error.fg = colors['red']
    c.colors.downloads.start.fg = colors['text']
    c.colors.downloads.stop.fg = colors['pink-dark']
    c.colors.downloads.system.fg = 'none'
    c.colors.downloads.system.bg = 'none'

    c.colors.hints.bg = colors['base']
    c.colors.hints.fg = colors['text']

    c.hints.border = '0px'
    c.colors.hints.match.fg = colors['pink-dark']
    c.colors.keyhint.bg = colors['base']
    c.colors.keyhint.fg = colors['text']
    c.colors.keyhint.suffix.fg = colors['pink-dark']


    c.colors.messages.error.bg = colors['base']
    c.colors.messages.error.border = colors['base']
    c.colors.messages.error.fg = colors['red']

    c.colors.messages.info.bg = colors['base']
    c.colors.messages.info.border = colors['base']
    c.colors.messages.info.fg = colors['text']

    c.colors.messages.warning.bg = colors['base']
    c.colors.messages.warning.border = colors['base']
    c.colors.messages.warning.fg = colors['yellow']


    c.colors.statusbar.normal.bg = colors['base']
    c.colors.statusbar.normal.fg = colors['text']

    c.colors.statusbar.insert.bg = colors['pink']
    c.colors.statusbar.insert.fg = colors['base']

    c.colors.statusbar.progress.bg = colors['base']

    c.colors.statusbar.command.bg = colors['base']
    c.colors.statusbar.command.fg = colors['text']

    c.colors.statusbar.passthrough.bg = colors['base']
    c.colors.statusbar.passthrough.fg = colors['text']

    c.colors.statusbar.caret.bg = colors['base']
    c.colors.statusbar.caret.selection.bg = colors['base']
    c.colors.statusbar.caret.fg = colors['text']
    c.colors.statusbar.caret.selection.fg = colors['pink-dark']

    c.colors.statusbar.url.error.fg = colors['red']
    c.colors.statusbar.url.fg = colors['text']
    c.colors.statusbar.url.hover.fg = colors['purple']
    c.colors.statusbar.url.success.http.fg = colors['pink']
    c.colors.statusbar.url.success.https.fg = colors['pink']
    c.colors.statusbar.url.warn.fg = colors['yellow']

    c.colors.statusbar.private.bg = colors['base']
    c.colors.statusbar.private.fg = colors['text']
    c.colors.statusbar.command.private.bg = colors['base']
    c.colors.statusbar.command.private.fg = colors['text']


    c.colors.tabs.bar.bg = colors['base']

    c.colors.tabs.odd.bg = colors['base-light']
    c.colors.tabs.odd.fg = colors['text']

    c.colors.tabs.even.bg = colors['base']
    c.colors.tabs.even.fg = colors['text']

    c.colors.tabs.selected.odd.bg = colors['pink']
    c.colors.tabs.selected.odd.fg = colors['base']

    c.colors.tabs.selected.even.bg = colors['pink']
    c.colors.tabs.selected.even.fg = colors['base']

    c.colors.tabs.indicator.error = colors['red']
    c.colors.tabs.indicator.system = 'none'

    c.colors.contextmenu.menu.bg = colors['base']
    c.colors.contextmenu.menu.fg = colors['text']

    c.colors.contextmenu.disabled.bg = colors['base']
    c.colors.contextmenu.disabled.fg = colors['pink']

    c.colors.contextmenu.selected.bg = colors['base']
    c.colors.contextmenu.selected.fg = colors['pink-dark']

    c.colors.webpage.bg = colors['base']
