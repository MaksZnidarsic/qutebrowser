


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
c.content.blocking.hosts.lists = ['https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts']
c.content.local_content_can_access_remote_urls = True
config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')

c.completion.height = '30%'
c.completion.scrollbar.padding = 2
c.completion.min_chars = 1
c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'filesystem']

c.downloads.position = 'top'
c.downloads.prevent_mixed_content = True
c.downloads.remove_finished = 1000

c.prompt.filebrowser = True

c.tabs.position = 'left'
c.tabs.show = 'never'
c.tabs.show_switching_delay = 500
c.tabs.width = 300
c.tabs.wrap = True

c.url.default_page = 'about:blank'
c.url.start_pages = 'about:blank'
c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?q={}', 
    'g': 'https://www.google.com/search?hl=en&q={}', 
    'y': 'https://yandex.com/?q={}',

    'w': 'https://wikipedia.org/wiki/{}', 
    'wd': 'https://wikipedia.org/wiki/{}_(disambiguation)', 
    'wi': 'https://wiktionary.org/wiki/{}', 
    'wa': 'https://wiki.archlinux.org/?search={}', 
    'wp' : 'https://proofwiki.org/wiki/{}',
}

c.downloads.location.directory = '$HOME/downloads'
