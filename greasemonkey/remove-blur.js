


// ==UserScript==
// @name            Remove blur
// @description     Removes blur from websites using simple css
// @run-at          document-end
// ==/UserScript==

(function removeBlur() {
    GM_addStyle('* { filter : blur(0) !important }')
})()
