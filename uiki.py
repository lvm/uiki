#!/usr/bin/python
import re,sys;
a=lambda x,y:'<a href="%s">%s</a>'%(x,y);_S=' '*4;s='&nbsp;'*4;h1=lambda x:\
"<h1><a href='fullsearch.html'>%s</a></h1>"%x;pre=lambda x:"<pre>%s</pre>"%\
x;dh=lambda x:x.replace('<','&lt;').replace('>','&gt;');W='';_R=[["^# (.*)",
"<h1>\\1</h1>"],["^#{2} (.*)","<h2>\\1</h2>"],["^#{3} (.*)","<h3>\\1</h3>"],
["^#{4} (.*)","<h4>\\1</h4>"],["^#{5} (.*)","<h5>\\1</h5>"],["\*(.[^\*]*)\*",
"<strong>\\1</strong>"],["''(.[^']*)''","<em>\\1</em>"],["^{","<ul>"],[
"^@ (.*)","<li>\\1</li>"],["^}","</ul>"],["\[\[(\w+)\|(.[^]]*)\]\]",a(
"\\1.html","\\2")],["\[\[(\w+)\]\]",a("\\1.html","\\1")],[
"\(\((.[^ \$]*)\|(.[^\)]+)\)\)",a("\\1","\\2")],["_(.[^ \$]*)_",a("\\1","\\1")
],["-{4}","<hr/>"],["(.*)  \n(.*)","\\1<br/>\\2"],["%(.[^ \$]*)%",
"<img src='\\1' />"]];HF=[['<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Tran',
'sitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><htm',
'l xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type"',
' content="text/html; charset=UTF-8"/><title>uiki</title></head><body>'],[
'<br/><hr/><a href="uiki.html">uiki</a> wiki</body></html>']];
def wk(l):
  for r in _R: l=re.sub(r[0],r[1],l)
  return l
def W(p):
  return ''.join(['%s'%pre(dh(x.replace(_S,s))) \
            if x.startswith(_S)else wk(x) for x in p])
try:
  f=sys.argv[1];w=open(f);H="%s%s"%(h1(f.split('/')[-1].replace(\
  '.wiki','')),W(w.readlines()));w.close();
except:
  print"USAGE:\n\t"+sys.argv[0]+" file.wiki";sys.exit(1)
print ''.join(HF[0])+H+''.join(HF[1]);sys.exit(0)
