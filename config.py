


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

c.url.default_page = 'about:blank'
c.url.start_pages = 'about:blank'
c.url.searchengines = {
    'DEFAULT' : 'https://duckduckgo.com/?kl=fr-fr&q={}',

    'f' : 'https://fran.si/iskanje?Query={}',
    'fr' : 'https://franja.si/iskanje?q={}',
    'w' : 'https://fr.wikipedia.org/wiki/?search={}',
    'wi' : 'https://fr.wiktionary.org/wiki/?search={}',
    's' : 'https://startpage.com/do/search?q={}',
}

config.bind('<Escape>', 'mode-leave ;; jseval -q document.activeElement.blur()', mode = 'insert')
