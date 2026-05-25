


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


import pink

c.colors.webpage.darkmode.enabled = True
pink.setup(c)


c.fonts.default_family = 'UbuntuMono Nerd Font'

c.content.private_browsing = True
c.content.blocking.hosts.lists = [ 'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts' ]
c.content.local_content_can_access_remote_urls = True
c.content.javascript.can_open_tabs_automatically = False

c.completion.height = '30%'
c.completion.scrollbar.padding = 1
c.completion.min_chars = 1
c.completion.open_categories = [ 'searchengines', 'bookmarks' ]

c.downloads.position = 'top'
c.downloads.prevent_mixed_content = False
c.downloads.remove_finished = 0
c.downloads.location.directory = '$HOME/downloads'

c.prompt.filebrowser = True
c.tabs.show = 'never'

c.hints.chars = 'asdfjkl' 
c.hints.radius = 0
c.hints.uppercase = False
c.hints.padding['left'] = 1
c.hints.padding['right'] = 1


from os.path import expanduser

start_page = expanduser('~/.config/qutebrowser/start_page.html')
c.url.default_page = start_page
c.url.start_pages = [start_page]

c.url.searchengines = {
    'DEFAULT' : 'https://duckduckgo.com/?kl=fr-fr&q={}',

    'f' : 'https://fran.si/iskanje?Query={}',
    'fr' : 'https://franja.si/iskanje?q={}',

    'm' : 'https://www.openstreetmap.org/search?query={}',
    's' : 'https://startpage.com/sp/search?q={}',

    'w' : 'https://fr.wikipedia.org/wiki/?search={}',
    'w.e' : 'https://en.wikipedia.org/wiki/?search={}',

    'wi' : 'https://fr.wiktionary.org/wiki/?search={}',
    'wi.d' : 'https://de.wiktionary.org/wiki/?search={}',
    'wi.e' : 'https://en.wiktionary.org/wiki/?search={}',
    'wi.i' : 'https://it.wiktionary.org/wiki/?search={}',
    'wi.s' : 'https://es.wiktionary.org/wiki/?search={}',

    'se.m' : 'https://math.stackexchange.com/search?q={}',
    'se.f' : 'https://french.stackexchange.com/search?q={}',
}


config.bind('<Escape>', 'mode-leave ;; jseval -q document.activeElement.blur()', mode = 'insert')
