#!/bin/sh

# begin of config

USE_VCS=0 # change it to 1 to enable.

VCS=''    # git, svn, bzr, hg
VCS_AD="" # opt to add files.
VCS_CI="" # opt commit changes
VCS_PU="" # opt to push changes
VCS_ME="" # commit message

# end of config.

W=$1
H=$2
HEAD="<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN' 'htt/www."
HEAD="${HEAD}w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'><html xmlns='http:/"
HEAD="${HEAD}/www.w3.org/1999/xhtml'><head><meta http-equiv='Content-Type' con"
HEAD="${HEAD}tent='text/html; charset=UTF-8'/><title>uiki</title></head><body>"
HEAD="${HEAD}<h1>fullsearch</h1>"
FOOT="<br/><hr/><a href='uiki.html'>uiki</a> wiki</body></html>";
PAGES="";
PG=''

stop(){
  echo "ERROR:\n\t$1\n\nUSAGE:\n\t`basename $0` WIKI_DIR HTML_DIR";
  exit 1
}

if [ $# != 2 ]
then
  stop "Missing parameter."
else
  [ -d $W ] || stop "WIKI_DIR dir not found.";
  [ -d $H ] || stop "HTML_DIR dir not found.";
  for P in $W/*.wiki;
  do 
    uiki.py $P>$(echo $P|sed -e"s/^$W/$H/g" -e"s/wiki$/html/g");
    PG=$(echo $P|sed -e"s/^$W\///g" -e"s/wiki$//g")
    PAGES="${PAGES}* <a href='$PG'>$PG</a><br/>"
  done
  echo "$HEAD$PAGES$FOOT">$H/fullsearch.html  
  if [ $USE_VCS = 1 ];
  then
    cd $H;
    $VCS $VCS_AD; $VCS $VCS_CI $VCS_ME && [ -n $VCS_PU ] && $VCS $VCS_PU;
  fi  
fi
