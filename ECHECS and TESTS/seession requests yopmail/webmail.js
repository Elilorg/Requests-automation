var lc = false;
var nbmails = 0;
var login;
var idaff;
var mailopt;
var yscrl = 0;
var page = 1;
var deleting = false;
var cptfocus = false;
var gHi;
var gHm;
var sp = true;
var ft = false;
var md = null;
sd();
var domain = 'yopmail.com';
var timeout;
var gmnu;
var ratio = 1;
var dkey;
function Gelt(n) { var elt = document.getElementById(n)
   ; if (elt) { return elt;
}
 else { return Geltmail(n);
}
 }
 function Geltmail(n) { var f = w.frames[mailframename()]
   ; if (f && f.document) return f.document.getElementById(n) }
    function showhide(n) { if (visible(n)) hide(n)
   ; else show(n);
}

function visible(n) { return (Gelt(n).style.display != 'none');
}

function show(n, display) { if (!display) Gelt(n).style.display = '';
else Gelt(n).style.display = display;
}
 function hide(n) { Gelt(n).style.display = 'none';
}
 function showandhide(a, b) { hide(b)
   ; show(a);
}
 function swap(n, txt1, txt2) { if (Gelt(n).innerText == txt1) Gelt(n).innerText = txt2
   ; else Gelt(n).innerText = txt1;
}
 function menushowhide(mnu) { clearTimeout(timeout)
   ; showhide(mnu);
}
 function menuvoir(mnu) { clearTimeout(timeout)
   ; show(mnu);
}
 function menucacher(mnu) { gmnu = mnu
   ; timeout = setTimeout('mcach()', 300);
}
 function mcach() { hide(gmnu);
}
 function ObjVisible(e) { return !!(e.offsetWidth || e.offsetHeight || e.getClientRects().length);
}
 function Previous() { refr(page - 1);
}
 function Next() { refr(page + 1);
}
 function getscrl() { yscrl = inboxframe().document.documentElement.scrollTop;
}
 function setscrl(inscrl) { if (inscrl !== undefined) yscrl = inscrl
   ; inboxframe().document.documentElement.scrollTop = yscrl
   ; yscrl = 0;
}
 function nodl() { alert('Acces denied, File potentially dangerous');
}
 function clipboard(id) { const el = document.createElement('textarea');
el.value = Gelt(id).innerText;
el.setAttribute('readonly', '');
el.style.position = 'absolute';
el.style.left = '-9999px';
document.body.appendChild(el);
el.select();
document.execCommand('copy');
document.body.removeChild(el);
Gelt('cptooltip').innerHTML = 'Copied';
}
 function showmessage(msg, undo) { hidemessage()
   ; if (msg != '') { Gelt('message').innerHTML = msg;
if (undo) show('msgundo');
else hide('msgundo');
show('messagectn');
}
 }
 function hidemessage() { Gelt('message').innerHTML = '';
hide('messagectn');
hide('msgundo');
}
 function activatebut(butname, act) { var but = Gelt(butname)
   ; if (act) but.removeAttribute('disabled');
else but.setAttribute('disabled', '');
}
 function selectbut(butname, select) { var but = Gelt(butname)
   ; if (select) but.setAttribute('selected', '');
else but.removeAttribute('selected');
}
 function sendingbut(butname, sending) { var but = Gelt(butname)
   ; if (sending) but.setAttribute('sending', '');
else but.removeAttribute('sending');
activatebut(butname, !sending);
}
 function gch() { return mailframe().document.location.href }
 function finrmail(nbmtot, p, sp, sn, undo, altcpt, msg) { nbmails = nbmtot
   ; page = p
   ; var ok = altcpt != '';
Gelt('refresh').setAttribute('loading', '');
Gelt('page').innerText = p;
var s = '';
if (nbmtot > 1) s = 's';
Gelt('nbmail').innerHTML = nbmtot + ' mail' + s;
SetAltCpt(altcpt);
setTimeout(function () { deleting = false;
}
, 700);
activatebut('delall', nbmtot > 0);
activatebut('undodel', undo);
activatebut('newmail', ok);
activatebut('rssfeed', ok);
ck();
showmessage(msg, undo);
if (sp == 1) showandhide('previous', 'previousinact');
else showandhide('previousinact', 'previous');
if (sn == 1) showandhide('next', 'nextinact');
else showandhide('nextinact', 'next');
if (nbmtot == 0 && gch().indexOf('nomail', 0) < 0) hidemail(true);
showinbox();
if (pc()) g();
else if (currentmail()) currentmail().removeAttribute('currentmail');
setscrl();
}
 function firstmail() { return inboxframe().document.querySelectorAll('.m').item(0);
}
 function currentmail() { return inboxframe().document.querySelector('.m[currentmail]');
}
 function currentmid() { if (typeof mid === 'undefined') { if (currentmail()) return currentmail().id;
}
 else return mid;
}
 function nextmid() { var next = currentmail().nextElementSibling
   ; if (next.className == 'mday') next = next.nextElementSibling;
if (next.className == 'm') return next.id;
}
 function affm(o, c, rc) { mailopt = o
   ; if (!c) c = login
   ; var u = 'mail?b=' + c + '&id=' + o + currentmid();
if (rc) u = u + '&r_c=' + rc;
if (ratio != 1 && o.toLowerCase() == 'i') u = u + '&r=' + ratio.toFixed(8);
mailnav(u);
}
 function g(c, o) { ratio = 1
   ; if (!c) c = login
   ; if (!o) o = 'm';
if (currentmid()) { affm(o, c);
}
 }
 function setcm(inm) { hidemessage()
   ; if (currentmail()) { currentmail().removeAttribute('loading');
currentmail().removeAttribute('currentmail');
}
 inm.setAttribute('currentmail', '');
}
 function ck() { activatebut('delsel', inboxframe().document.querySelectorAll('.mc:checked').length > 0);
}
 function SetAltCpt(alt) { if (alt != '') { Gelt('autoaltcpt').innerHTML = '<em>' + alt + '</em>@' + domain;
show('cpalias', 'inline-flex');
}
 }
 function newm() { if (login != '') { showinbox(true)
   ; mailnav('write?b=' + login + '&id=');
}
 }
 function forward() { mailnav('forward?b=' + login + '&id=' + currentmid());
}
 function reply() { mailnav('reply?b=' + login + '&id=' + currentmid());
}
 function down() { var link = document.createElement('a');
link.setAttribute('download', '');
link.href = '/downmail?b=' + login + '&id=' + currentmid() + '&dk=' + dkey;
document.body.appendChild(link);
link.click();
link.remove();
}
 function nav(l) { w.document.location.href = l;
}
 function egengo() { w.document.location.href = '.?login=' + login;
}
 function newgen() { document.cookie = 'ygen=;
ath=/;
omain=yopmail.com;
;
document.location.reload();
}
 function genrss() { if (login != '') document.location.href = 'gen-rss?login=' + login;
}
 function sendsub() { Geltmail('msgbody').innerHTML = Geltmail('inputbody').innerHTML;
return true;
}
 function kp(pEnvent) { if (pEnvent.keyCode == 46 && !cptfocus && currentmid()) suppr();
}
 function suppr() { if (inboxframe().document.querySelectorAll('.mc:checked').length > 0) suppr_sel();
else suppr_mail();
}
 function suppr_all(msg) { if (deleting) return
   ; if (confirm('Are you sure you want to delete all messages?')) { deleting = true
   ; hidemail(true)
   ; setTimeout(function () { refr(1, '', 'all', firstmail().id);
}
, 50);
}
 }
 function suppr_undo() { if (!deleting) { deleting = true
   ; refr(1, '', 'undo');
}
 }
 function suppr_sel() { if (!deleting) { deleting = true
   ; ch = '';
var chs = inboxframe().document.querySelectorAll('.mc:checked');
for (var i = 0
   ; i < chs.length
   ; i++) { ch = ch + chs.item(i).parentNode.id + '|';
}
 if (ch != '') { hidemail(true)
   ; setTimeout(function () { refr(page, '', ch.substring(0, ch.length - 1), '');
}
, 50);
}
 else { showmessage('No mail selected');
deleting = false;
}
 }
 }
 function suppr_mail() { if (!deleting) { deleting = true
   ; getscrl()
   ; if (nextmid()) nextmailid = nextmid()
   ; else nextmailid = 'last';
if (!pc()) { window.history.back();
}
 hidemail(true);
setTimeout(function () { refr(page, nextmailid, currentmid(), '');
}
, 50);
}
 }
 function foc() { Gelt('login').focus();
}
 var reg_login = /^[-a-zA-Z0-9@_.+]{1,}
$/;
function chkl() { var c = Gelt('login').value.trim();
if (c.indexOf('@') > 0) c = c.substring(0, c.indexOf('@'));
if (!reg_login.test(c)) return false;
if (c.length > 25) return false;
return chkc();
}
 function chkc() { if (Gelt('cons-pop') && Gelt('cons-pop').className == 'explicit' && Gelt('cons-pop').style.display == '' && lc == false) { if (Gelt('cons-pop').getBoundingClientRect().width == 0) { loadconsent('nset', false);
return true;
}
 return false;
}
 return true;
}
 function clearbut() { Gelt('clearbut').style.display = 'none';
Gelt('login').value = '';
foc();
CptonKeyUp();
}
 function CptonKeyUp() { var c = Gelt('login').value.trim();
if (c.length > 0) show('clearbut');
else hide('clearbut');
if (c.indexOf('@') > 0) c = c.substring(0, c.indexOf('@'));
if (c.length > 0 && !(reg_login.test(c))) { Gelt('ycptcpt').style.borderColor = 'red';
cpterror('<b>Use only : a-z 0-9 . _ -</b>');
return;
}
 if (c.length > 25) { Gelt('ycptcpt').style.borderColor = 'red';
cpterror('<b>25 characters max !</b>');
return;
}
 cpterror('');
Gelt('ycptcpt').style.borderColor = '';
}
 function cpterror(msg) { var a = Gelt('errorcpt');
if (msg.length > 0) { if (a.innerHTML.length == 0) visopac(a, true)
   ; a.innerHTML = msg;
}
 else { if (a.innerHTML.length > 0) visopac(a, false)
   ; a.innerHTML = '';
}
 }
 function visopac(obj, vis) { var a = Gelt(obj)
   ; if (vis) { obj.style.visibility = 'visible';
obj.style.opacity = 1;
}
 else { obj.style.visibility = 'hidden';
obj.style.opacity = 0;
}
 }
 function sd() { var d = new Date()
   ; document.cookie = "ytime=" + d.getHours() + ":" + d.getMinutes() + ";ath=/;domain=yopmail.com";
}
 function setp(n, v) { try { w.frames['ifcall'].document.location.href = 'setp?n=' + n + '&v=' + v;
}
 catch (ex) { }
 }
 function printmail() { try { mailframe().focus()
   ; mailframe().print();
}
 catch (ex) { }
 }
 function ifr(id, ctn, display) { var iframe = document.createElement('iframe');
iframe.frameBorder = 0;
iframe.width = '100%';
iframe.height = '100%';
iframe.setAttribute('frameborder', '0');
iframe.setAttribute('src', '');
iframe.setAttribute('name', id);
iframe.setAttribute('onload', 'onload' + id + '()');
iframe.id = id;
if (!display) iframe.style.display = 'none';
Gelt(ctn).appendChild(iframe);
}
 function ifpcm() { try { Gelt('wmmailmain').removeChild(Gelt('ifmail'));
}
 catch (ex) { }
 ifr('ifmail', 'wmmailmain', true);
}
 function ifmobm() { try { Gelt('webmail').removeChild(Gelt('ifmobmail'));
}
 catch (ex) { }
 ifr('ifmobmail', 'webmail', true);
Gelt('ifmobmail').setAttribute('state', 'hidden');
}
 function inb() { try { Gelt('wminboxmain').removeChild(Gelt('ifinbox'));
}
 catch (ex) { }
 ifr('ifinbox', 'wminboxmain', true);
try { Gelt('wminboxmain').removeChild(Gelt('ifnoinb'));
}
 catch (ex) { }
 ifr('ifnoinb', 'wminboxmain', false);
refr_load();
}
 function pc() { var e = document.getElementById('wmmailmain');
return (e && ObjVisible(e));
}
 function mailframename() { if (pc()) return 'ifmail';
else return 'ifmobmail';
}
 function mailframe() { var fn = mailframename(); 
    var f = w.frames[fn]
   ; if (!f) { if (pc()) ifpcm()
   ; else ifmobm();
}
try { if (f) f.document;}
catch (ex) { if (pc()) ifpcm()
   ; else ifmobm();}
 return w.frames[fn];
}
 function inboxframe() { var f = w.frames['ifinbox'];
try { if (f) f.document;
}
 catch (ex) { inb();
}
 return w.frames['ifinbox'];
}
 function onloadifinbox() { Gelt('refresh').removeAttribute('loading');
}
 function onloadifnoinb() { }
 function onloadifmobmail() { onloadifmail();
}
 function onloadifmail() { }
 function mailend() { if (currentmail()) scalemail()
   ; showmail(true);
}
 function mailload() { if (currentmail()) { currentmail().removeAttribute('loading');
scalemail();
}
 }
 function mailnav(u, href) { if (gch().indexOf(u) < 0) { if (currentmail() && u.includes(currentmid())) currentmail().setAttribute('loading', '');
if (pc()) hidemail();
if (href) mailframe().document.location.href = u;
else mailframe().document.location.replace(u);
}
 else { showmail(true);
}
 }
 window.onpopstate = function (event) { if (event.state && event.state.poped) { showmail(false);
}
 else { hidemail();
}
 }
;
function go() { if (Gelt('login').value.trim() != '') Gelt('f').submit();
}
 function refr_load() { if (typeof this.refrok == 'undefined') { this.refrok = 1
   ; if (inboxframe().document.location.href.substring(1, 4) != 'http') refr();
}
 }
 var rb = 0;
function r() { hideinbox()
   ; if (rb == 1) { Gelt('refresh').setAttribute('loading', '');
setTimeout(function () { Gelt('refresh').removeAttribute('loading');
showinbox();
}
, 200);
return;
}
 rb = 1;
setTimeout(function () { rb = 0;
}
, 2000);
refr('r');
}
 var nextrf = 0;
var nIId;
var nTId;
function refr(p, i, d, ctrl, r_c) { hideinbox()
   ; Gelt('refresh').setAttribute('loading', '');
clearTimeout(nIId);
clearInterval(nTId);
nTId = setTimeout(function () { refr_(p, i, d, ctrl, r_c)
   ; nextrf = 1200;
}
, nextrf);
nIId = setInterval(function () { if (nextrf <= 0) { clearInterval(nIId)
   ; nextrf = 0
   ; return;
}
 nextrf -= 100;
}
, 100);
}
 function refr_(p, i, d, ctrl, r_c) { try { sd()
   ; if (!p) var p = '1';
if ((Gelt('login').value != login && p == 'r') || p == 'f') Gelt('f').submit();
else { Gelt('refresh').setAttribute('loading', '');
if (inboxframe()) { if (!p) var p = '1';
if (p == 'r') p = '1';
if (!i) var i = idaff;
if (!d) var d = '';
if (md != null) d = md;
md = null;
if (!ctrl) var ctrl = '';
if (!r_c) var r_c = '';
inboxframe().document.location.replace('inbox?login=' + login + '&p=' + p + '&d=' + d + '&ctrl=' + ctrl + '&yp=' + Gelt('yp').value + '&yj=OAQN5ZmD1ZwxlZwH3ZGN2ZGt&v=' + ver + '&r_c=' + r_c + '&id=' + i);
}
 else w.setTimeout('refr()', 100);
}
 }
 catch (ex) { }
 }
 function showinbox(force) { if (nbmails > 0 || force) { if (w.frames['ifnoinb'].document.location.href.indexOf('noinb', 0) >= 0) { hidemail(true)
   ; w.frames['ifnoinb'].document.location.replace('about:blank');
}
 showandhide('ifinbox', 'ifnoinb');
inboxframe().frameElement.setAttribute('state', 'full');
Gelt('ifnoinb').setAttribute('state', 'hidden');
}
 else { if (nbmails != -1) shownoinb(0);
}
 }
 function shownoinb(n) { if (n == 0) { showandhide('ifnoinb', 'ifinbox');
inboxframe().frameElement.setAttribute('state', 'hidden');
Gelt('ifnoinb').setAttribute('state', 'full');
}
 if (w.frames['ifnoinb'].document.location.href.indexOf('noinb', 0) < 0) { if (n == 0) { w.frames['ifinbox'].document.location.replace('about:blank');
mailframe().document.location.replace('about:blank');
}
 if (n > 10 || (w.frames['ifinbox'].document.location.href == 'about:blank' && gch() == 'about:blank')) { w.frames['ifnoinb'].document.location.replace('noinb');
if (pc()) mailnav('nomail');
}
 else setTimeout(function () { shownoinb(++n);
}
, 50);
}
 }
 function swapscale() { if (Geltmail('mail').style.transform == '') scalemail(true);
else scalemail(true, 1);
}
 function scalemail(force = false, val) { var mlctn = Geltmail('mailctn');
var ml = Geltmail('mail');
if (ml) { if (val) ratio = val
   ; else ratio = Math.min(1, Math.max(0.4, (mlctn.offsetWidth / ml.scrollWidth)));
if (ratio != 1 || force) { if (ratio == 1) { ml.style.transform = '';
ml.style.height = '';
Geltmail('mratio').style.opacity = '1';
}
 else { if (['m', 'h', 't', 'i'].includes(mailopt.toLowerCase()) || force) { if (mailframe().frameElement.getAttribute('state') == 'full') ml.setAttribute('trans', '');
ml.style.transform = 'scale(' + ratio + ')';
ml.style.height = (ml.scrollHeight).toFixed(2) + 'px';
ml.setAttribute('trans', '');
Geltmail('mratio').style.opacity = '0.6';
}
 Geltmail('mratio').style.display = '';
}
 }
 return ratio;
}
 return 0;
}
 function hideinbox() { inboxframe().frameElement.setAttribute('state', 'hidden');
Gelt('ifnoinb').setAttribute('state', 'hidden');
}
 function showmail(push) { if (!pc() && mailframe().frameElement.getAttribute('state') != 'full' && push) window.history.pushState({ 'poped': true }
, null, '');
mailframe().frameElement.setAttribute('state', 'full');
}
 function hidemail(remove) { if (remove) mailframe().document.location.replace('about:blank');
mailframe().frameElement.setAttribute('state', 'hidden');
}
 function cookiesparams() { Gelt('cons-txt').style.display = 'none';
Gelt('cons-cookies').style.display = '';
Gelt('cookiesparams').style.display = 'none';
Gelt('saveparams').style.display = '';
}
 function saveparams() { p = Gelt('preferences').checked;
s = Gelt('statistics').checked;
m = Gelt('marketing').checked;
loadconsent('1' + ((p) ? '1' : '0') + ((s) ? '1' : '0') + ((m) ? '1' : '0'));
validate(p, s, m);
}
 function necesary() { loadconsent('deny');
}
 function accept() { loadconsent('accept');
validate(true, true, true);
}
 function validate(p, s, m) { if (s) { try { loadAna();
}
 catch (ex) { }
 }
 if (m) { try { sa(0);
}
 catch (ex) { }
 }
 }
 function loadconsent(s, as) { if (Gelt('cons-pop') && Gelt('cons-pop').style.display == '') { Gelt('cons-pop').style.display = 'none';
var as = (typeof as !== 'undefined') ? as : true;
var xmlHttp = new XMLHttpRequest();
xmlHttp.open("GET", '/consent?c=' + s, as);
xmlHttp.onload = function () { try { cl();
}
 catch (ex) { }
;
}
;
xmlHttp.send(null);
lc = true;
}
 }
 function callpost(u, ok, err) { w.sendingbut('msgsend', true);
var XHR = new XMLHttpRequest();
XHR.addEventListener('load', ok);
XHR.addEventListener('error', err);
XHR.open('POST', u);
XHR.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
var args = arguments;
var s = '';
var v;
for (var i = 3
   ; i < args.length
   ; i = i + 2) { s += (s ? '&' : '') + args[i] + '=' + encodeURIComponent(args[i + 1]).replace(/%20/g, '+');
}
 XHR.send(s);
}
 function showsenderror(ret) { var t = ret.split('|');
var elt = w.Gelt((t[0]));
if (elt) elt.setAttribute('error', '');
w.Gelt('msgerr').innerHTML = t[1];
w.Gelt('msgerr').style.opacity = 1;
}
 function showsendpopup(ret) { var t = ret.split('|');
if (t[1] == 'hide') showandhide('popbuthide', 'popbutback');
else if (t[1] == 'back') showandhide('popbutback', 'popbuthide');
else if (t[1] == 'mobback' && !pc()) showandhide('popbutback', 'popbuthide');
else if (t[1] == 'mobhide' && !pc()) showandhide('popbuthide', 'popbutback');
else { hide('popbutctn');
}
 Gelt('msgpopmsg').innerHTML = t[2];
w.show('msgpop');
}


