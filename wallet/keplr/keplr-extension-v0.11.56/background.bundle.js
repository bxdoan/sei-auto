!function(e){function n(n){for(var r,u,c=n[0],a=n[1],s=n[2],f=0,p=[];f<c.length;f++)u=c[f],Object.prototype.hasOwnProperty.call(o,u)&&o[u]&&p.push(o[u][0]),o[u]=0;for(r in a)Object.prototype.hasOwnProperty.call(a,r)&&(e[r]=a[r]);for(l&&l(n);p.length;)p.shift()();return i.push.apply(i,s||[]),t()}function t(){for(var e,n=0;n<i.length;n++){for(var t=i[n],r=!0,c=1;c<t.length;c++){var a=t[c];0!==o[a]&&(r=!1)}r&&(i.splice(n--,1),e=u(u.s=t[0]))}return e}var r={},o={11:0},i=[];function u(n){if(r[n])return r[n].exports;var t=r[n]={i:n,l:!1,exports:{}};return e[n].call(t.exports,t,t.exports,u),t.l=!0,t.exports}u.m=e,u.c=r,u.d=function(e,n,t){u.o(e,n)||Object.defineProperty(e,n,{enumerable:!0,get:t})},u.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},u.t=function(e,n){if(1&n&&(e=u(e)),8&n)return e;if(4&n&&"object"==typeof e&&e&&e.__esModule)return e;var t=Object.create(null);if(u.r(t),Object.defineProperty(t,"default",{enumerable:!0,value:e}),2&n&&"string"!=typeof e)for(var r in e)u.d(t,r,function(n){return e[n]}.bind(null,r));return t},u.n=function(e){var n=e&&e.__esModule?function(){return e.default}:function(){return e};return u.d(n,"a",n),n},u.o=function(e,n){return Object.prototype.hasOwnProperty.call(e,n)},u.p="";var c=window.webpackJsonp=window.webpackJsonp||[],a=c.push.bind(c);c.push=n,c=c.slice();for(var s=0;s<c.length;s++)n(c[s]);var l=a;i.push([1127,2,4,8,3,1,7,0,5,6,9,10]),t()}({1127:function(e,n,t){e.exports=t(1128)},1128:function(e,n,t){"use strict";t.r(n);var r=t(3),o=t(58),i=t(21),u=t(37),c=t(329),a=t.n(c),s=t(2),l=t(246),f=function(e,n,t,r){return new(t||(t=Promise))((function(o,i){function u(e){try{a(r.next(e))}catch(e){i(e)}}function c(e){try{a(r.throw(e))}catch(e){i(e)}}function a(e){var n;e.done?o(e.value):(n=e.value,n instanceof t?n:new t((function(e){e(n)}))).then(u,c)}a((r=r.apply(e,n||[])).next())}))};const p=new o.ExtensionRouter(o.ExtensionEnv.produceEnv);p.addGuard(o.ExtensionGuards.checkOriginIsValid),p.addGuard(o.ExtensionGuards.checkMessageIsInternal),Object(u.init)(p,e=>new i.ExtensionKVStore(e),new o.ContentScriptMessageRequester,l.b,l.c,l.c,l.a,{rng:e=>Promise.resolve(crypto.getRandomValues(e)),scrypt:(e,n)=>f(void 0,void 0,void 0,(function*(){return yield a.a.scrypt(s.Buffer.from(e),s.Buffer.from(n.salt,"hex"),n.n,n.r,n.p,n.dklen)}))},{create:e=>{browser.notifications.create({type:"basic",iconUrl:e.iconRelativeUrl?browser.runtime.getURL(e.iconRelativeUrl):void 0,title:e.title,message:e.message})}}),p.listen(r.BACKGROUND_PORT)}});