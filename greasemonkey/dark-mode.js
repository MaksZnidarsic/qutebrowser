


// ==UserScript==
// @name            Dark reader
// @icon            https://darkreader.org/images/darkreader-icon-256x256.png
// @namespace       DarkReader
// @description	    Inverts the brightness of pages to reduce eye strain
// @version         4.7.15
// @author          https://github.com/darkreader/darkreader#contributors
// @homepageURL     https://darkreader.org/ | https://github.com/darkreader/darkreader
// @run-at          document-end
// @grant           none
// @include         http*
// @exclude         https://www.youtube*
// @require         https://cdn.jsdelivr.net/npm/darkreader/darkreader.min.js
// @noframes
// ==UserScript==

DarkReader.enable({
    brightness : 10,
    contrast : 100,
    sepia : 50,
})
