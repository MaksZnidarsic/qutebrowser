


#                __       __                                     
#   ____ ___  __/ /____  / /_  _________ _      __________  _____
#  / __ `/ / / / __/ _ \/ __ \/ ___/ __ \ | /| / / ___/ _ \/ ___/
# / /_/ / /_/ / /_/  __/ /_/ / /  / /_/ / |/ |/ (__  )  __/ /    
# \__, /\__,_/\__/\___/_.___/_/   \____/|__/|__/____/\___/_/     
#   /_/                                                          


# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html


config.load_autoconfig(False)

import catppuccin

c.fonts.default_family = 'UbuntuMono Nerd Font'
c.colors.webpage.darkmode.enabled = True
catppuccin.setup(c, 'mocha', True)

c.content.private_browsing = True
c.content.blocking.hosts.lists = [ 'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts' ]
c.content.local_content_can_access_remote_urls = True
c.content.javascript.can_open_tabs_automatically = False

c.completion.height = '30%'
c.completion.scrollbar.padding = 1
c.completion.min_chars = 1
c.completion.open_categories = [ 'searchengines', 'quickmarks', 'bookmarks', 'filesystem' ]

c.downloads.position = 'top'
c.downloads.prevent_mixed_content = True
c.downloads.remove_finished = 0
c.downloads.location.directory = '$HOME/downloads'

c.prompt.filebrowser = True
c.tabs.show = 'never'

c.hints.chars = 'asdfjkl' 
c.hints.find_implementation = 'javascript'
c.hints.radius = 1
c.hints.uppercase = True
c.hints.padding['left'] = 1
c.hints.padding['right'] = 1
c.hints.border = '0px'
c.colors.hints.bg = '#181825'
c.colors.hints.fg = '#ffffff'

c.url.default_page = 'about:blank'
c.url.start_pages = 'about:blank'
c.url.searchengines = {
    'DEFAULT' : 'https://duckduckgo.com/?kl=fr-fr&q={}',

    'f' : 'https://fran.si/iskanje?Query={}',
    'fr' : 'https://franja.si/iskanje?q={}',
    'm' : 'https://www.openstreetmap.org/search?query={}',
    's' : 'https://startpage.com/sp/search?q={}',

    'w' : 'https://fr.wikipedia.org/wiki/?search={}',
    'w.e' : 'https://en.wikipedia.org/wiki/?search={}',

    'wi' : 'https://fr.wiktionary.org/wiki/?search={}',
    'wi.e' : 'https://en.wiktionary.org/wiki/?search={}',

    'se.m' : 'https://math.stackexchange.com/search?q={}',
    'se.f' : 'https://french.stackexchange.com/search?q={}'
}

config.bind('<Escape>', 'mode-leave ;; jseval -q document.activeElement.blur()', mode = 'insert')
config.bind('<Ctrl-u>', 'spawn --userscript youtube-redirect', mode = 'normal')
