


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


from colorschemes import pink

c.colors.webpage.darkmode.enabled = True
pink.setup(c)


c.fonts.default_family = 'UbuntuMono Nerd Font'


c.content.private_browsing = True

c.content.javascript.can_open_tabs_automatically = False
c.content.local_content_can_access_remote_urls = True
c.content.notifications.enabled = False

c.content.autoplay = False

c.content.geolocation = False
c.content.dns_prefetch = False
c.content.webgl = False
c.content.webrtc_ip_handling_policy = "default-public-interface-only"


c.content.blocking.enabled = True
c.content.blocking.method = "both"

c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
]

c.content.blocking.hosts.lists = [
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',
    'https://someonewhocares.org/hosts/zero/hosts'
]


c.completion.height = '30%'
c.completion.scrollbar.padding = 1
c.completion.min_chars = 1
c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks']


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

start_page = expanduser('~/.config/qutebrowser/start-page.html')
c.url.default_page = start_page
c.url.start_pages = [start_page]

c.url.searchengines = {

    'DEFAULT' : 'https://noai.duckduckgo.com/?q={}',
    #'https://duckduckgo.com/?kl=fr-fr&assist=false&q={}'
    #'https://duckduckgo.com/?&noai=1&q={}'

    'f' : 'https://fran.si/iskanje?Query={}',
    'fr' : 'https://franja.si/iskanje?q={}',

    'm' : 'https://www.openstreetmap.org/search?query={}',

    's' : 'https://www.startpage.com/do/search?query={}',

    'w' : 'https://en.wikipedia.org/wiki/?search={}',
    'w.f' : 'https://fr.wikipedia.org/wiki/?search={}',

    'wi' : 'https://fr.wiktionary.org/wiki/?search={}',
    'wi.e' : 'https://en.wiktionary.org/wiki/?search={}',

}


config.bind('I', 'config-cycle colors.webpage.darkmode.enabled')
config.bind('F', 'hint all right-click')
config.bind('Y', 'hint links yank')
config.bind('R', 'reload -f')
config.bind('<Escape>', 'mode-leave ;; jseval -q document.activeElement.blur()', mode = 'insert')
config.bind('<Escape>', 'fake-key <Escape>', mode = 'normal')
