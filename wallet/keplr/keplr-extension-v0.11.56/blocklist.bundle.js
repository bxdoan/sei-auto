!function(e){function t(t){for(var r,o,c=t[0],s=t[1],l=t[2],f=0,d=[];f<c.length;f++)o=c[f],Object.prototype.hasOwnProperty.call(i,o)&&i[o]&&d.push(i[o][0]),i[o]=0;for(r in s)Object.prototype.hasOwnProperty.call(s,r)&&(e[r]=s[r]);for(u&&u(t);d.length;)d.shift()();return a.push.apply(a,l||[]),n()}function n(){for(var e,t=0;t<a.length;t++){for(var n=a[t],r=!0,c=1;c<n.length;c++){var s=n[c];0!==i[s]&&(r=!1)}r&&(a.splice(t--,1),e=o(o.s=n[0]))}return e}var r={},i={20:0},a=[];function o(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,o),n.l=!0,n.exports}o.m=e,o.c=r,o.d=function(e,t,n){o.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},o.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.t=function(e,t){if(1&t&&(e=o(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(o.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)o.d(n,r,function(t){return e[t]}.bind(null,r));return n},o.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return o.d(t,"a",t),t},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.p="";var c=window.webpackJsonp=window.webpackJsonp||[],s=c.push.bind(c);c.push=t,c=c.slice();for(var l=0;l<c.length;l++)t(c[l]);var u=s;a.push([2134,2,4,8,3,1,7,0,5,6,9]),n()}({2134:function(e,t,n){e.exports=n(2135)},2135:function(e,t,n){"use strict";n.r(t),n.d(t,"BlocklistPage",(function(){return d}));var r=n(3),i=n(58),a=n(0),o=n.n(a),c=n(37),s=n(103),l=n.n(s),u=n(292),f=n.n(u);const d=()=>{const e=new URLSearchParams(window.location.search).get("origin")||"";return o.a.createElement("div",{className:f.a.container},o.a.createElement("div",{className:f.a.inner},o.a.createElement("img",{className:f.a.image,src:n(2137),alt:""}),o.a.createElement("div",null,o.a.createElement("h1",{className:f.a.title},"SECURITY ALERT"),o.a.createElement("p",{className:f.a.description},"Keplr has detected that this domain has been flagged as a phishing site. To protect the safety of your assets, we recommend you exit this website immediately."),o.a.createElement("button",{className:f.a.link,onClick:()=>(new i.InExtensionMessageRequester).sendMessage(r.BACKGROUND_PORT,new c.URLTempAllowMsg(e)).then(()=>{window.location.replace(e)})},"Continue to ",e," (unsafe)"))))};l.a.render(o.a.createElement(d,null),document.getElementById("app"))},2136:function(e,t,n){(t=n(25)(!1)).push([e.i,".container--Pgy6G5TzIg48Wwcx5hW8{display:flex;align-items:center;justify-content:center;margin:-8px;width:100vw;height:100vh}.inner-2VD86_FW5ydgqioSxMfmRd{display:flex;align-items:center;gap:54px;text-align:left;padding:24px;max-width:1024px}.title-2kdbi3BmwqtKdvC447H_N7{font-weight:600;font-size:48px;line-height:58px;color:#37373e;margin:0}.description-1YT-p_AefS0yEAXmuwdZJq{font-weight:400;font-size:16px;line-height:19px;letter-spacing:-0.005em;margin:28px 0;color:#9a9aa2}.link-3UJhMYA1faTn0zvyzS7kVJ{appearance:none;border:0;padding:0;background:transparent;text-decoration:underline;font-weight:400;font-size:16px;line-height:19px;letter-spacing:-0.005em;color:#64646d}@media screen and (max-width: 768px){.inner-2VD86_FW5ydgqioSxMfmRd{flex-direction:column;text-align:center}.image-383pxaCj0CVHVzD7z-aHvv{margin:0 auto;max-width:max(60%,260px)}.title-2kdbi3BmwqtKdvC447H_N7{font-size:32px;line-height:39px}.description-1YT-p_AefS0yEAXmuwdZJq{max-width:max(75%,320px);margin:20px auto}}",""]),t.locals={container:"container--Pgy6G5TzIg48Wwcx5hW8",inner:"inner-2VD86_FW5ydgqioSxMfmRd",title:"title-2kdbi3BmwqtKdvC447H_N7",description:"description-1YT-p_AefS0yEAXmuwdZJq",link:"link-3UJhMYA1faTn0zvyzS7kVJ",image:"image-383pxaCj0CVHVzD7z-aHvv"},e.exports=t},2137:function(e,t){e.exports="assets/blocklist.svg"},25:function(e,t,n){"use strict";e.exports=function(e){var t=[];return t.toString=function(){return this.map((function(t){var n=function(e,t){var n=e[1]||"",r=e[3];if(!r)return n;if(t&&"function"==typeof btoa){var i=(o=r,c=btoa(unescape(encodeURIComponent(JSON.stringify(o)))),s="sourceMappingURL=data:application/json;charset=utf-8;base64,".concat(c),"/*# ".concat(s," */")),a=r.sources.map((function(e){return"/*# sourceURL=".concat(r.sourceRoot||"").concat(e," */")}));return[n].concat(a).concat([i]).join("\n")}var o,c,s;return[n].join("\n")}(t,e);return t[2]?"@media ".concat(t[2]," {").concat(n,"}"):n})).join("")},t.i=function(e,n,r){"string"==typeof e&&(e=[[null,e,""]]);var i={};if(r)for(var a=0;a<this.length;a++){var o=this[a][0];null!=o&&(i[o]=!0)}for(var c=0;c<e.length;c++){var s=[].concat(e[c]);r&&i[s[0]]||(n&&(s[2]?s[2]="".concat(n," and ").concat(s[2]):s[2]=n),t.push(s))}},t}},26:function(e,t,n){"use strict";var r,i=function(){return void 0===r&&(r=Boolean(window&&document&&document.all&&!window.atob)),r},a=function(){var e={};return function(t){if(void 0===e[t]){var n=document.querySelector(t);if(window.HTMLIFrameElement&&n instanceof window.HTMLIFrameElement)try{n=n.contentDocument.head}catch(e){n=null}e[t]=n}return e[t]}}(),o=[];function c(e){for(var t=-1,n=0;n<o.length;n++)if(o[n].identifier===e){t=n;break}return t}function s(e,t){for(var n={},r=[],i=0;i<e.length;i++){var a=e[i],s=t.base?a[0]+t.base:a[0],l=n[s]||0,u="".concat(s," ").concat(l);n[s]=l+1;var f=c(u),d={css:a[1],media:a[2],sourceMap:a[3]};-1!==f?(o[f].references++,o[f].updater(d)):o.push({identifier:u,updater:g(d,t),references:1}),r.push(u)}return r}function l(e){var t=document.createElement("style"),r=e.attributes||{};if(void 0===r.nonce){var i=n.nc;i&&(r.nonce=i)}if(Object.keys(r).forEach((function(e){t.setAttribute(e,r[e])})),"function"==typeof e.insert)e.insert(t);else{var o=a(e.insert||"head");if(!o)throw new Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.");o.appendChild(t)}return t}var u,f=(u=[],function(e,t){return u[e]=t,u.filter(Boolean).join("\n")});function d(e,t,n,r){var i=n?"":r.media?"@media ".concat(r.media," {").concat(r.css,"}"):r.css;if(e.styleSheet)e.styleSheet.cssText=f(t,i);else{var a=document.createTextNode(i),o=e.childNodes;o[t]&&e.removeChild(o[t]),o.length?e.insertBefore(a,o[t]):e.appendChild(a)}}function p(e,t,n){var r=n.css,i=n.media,a=n.sourceMap;if(i?e.setAttribute("media",i):e.removeAttribute("media"),a&&"undefined"!=typeof btoa&&(r+="\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(a))))," */")),e.styleSheet)e.styleSheet.cssText=r;else{for(;e.firstChild;)e.removeChild(e.firstChild);e.appendChild(document.createTextNode(r))}}var m=null,h=0;function g(e,t){var n,r,i;if(t.singleton){var a=h++;n=m||(m=l(t)),r=d.bind(null,n,a,!1),i=d.bind(null,n,a,!0)}else n=l(t),r=p.bind(null,n,t),i=function(){!function(e){if(null===e.parentNode)return!1;e.parentNode.removeChild(e)}(n)};return r(e),function(t){if(t){if(t.css===e.css&&t.media===e.media&&t.sourceMap===e.sourceMap)return;r(e=t)}else i()}}e.exports=function(e,t){(t=t||{}).singleton||"boolean"==typeof t.singleton||(t.singleton=i());var n=s(e=e||[],t);return function(e){if(e=e||[],"[object Array]"===Object.prototype.toString.call(e)){for(var r=0;r<n.length;r++){var i=c(n[r]);o[i].references--}for(var a=s(e,t),l=0;l<n.length;l++){var u=c(n[l]);0===o[u].references&&(o[u].updater(),o.splice(u,1))}n=a}}}},292:function(e,t,n){var r=n(26),i=n(2136);"string"==typeof(i=i.__esModule?i.default:i)&&(i=[[e.i,i,""]]);var a={insert:"head",singleton:!1};r(i,a);e.exports=i.locals||{}}});