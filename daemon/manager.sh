#!/usr/bin/env bash
# tymer manager
########################################################
VERSION=0.1.0
IFS=$'\n'
TYMERS_DIR=~/.tymer
TYMERS_FILE=~/.tymer/tymers.txt

CURRENT_TIME=$(date)
CURRENT_TIME_SEC=$(date +%s)
FUTURE_TIME=$(date -v +30M)
FUTURE_TIME_SEC=$(date -v +30M +%s)
DEFAULT_TYME="+30M"

TYMER_DESC=""

# variables
whichMethod=$1
########################################################

if [ ! -f $TYMERS_FILE ]; then
  mkdir -p $TYMERS_DIR
  touch $TYMERS_FILE
fi


# helper functions
########################################################
convertsecs() {
  ((h=${1}/3600))
  ((m=(${1}%3600)/60))
  ((s=${1}%60))
  printf "%02d:%02d:%02d\n" $h $m $s
}


########################################################
function listTymers() {

  while read p; do
    seconds=`echo $p | sed 's/:.*//'`
    human_readable_time=`echo $p | sed 's/[^:]*://'`
    human_readable_time=`echo $human_readable_time | sed 's/=.*//'`
    current_tymer_desc=`echo $p | sed 's/[^=].*=//'`
    time_left=$((seconds - CURRENT_TIME_SEC))
    time_left=$(convertsecs $time_left)

    echo $current_tymer_desc ":" $human_readable_time ":" $time_left
  done< $TYMERS_FILE
}


########################################################
function addTymer() {

  printf "Creating New Tymer:\n"
  printf "\t"$TYMER_DESC"\n"
  printf "\t"$FUTURE_TIME"\n"
  printf "\t"$TYMER_LENGTH"\n"

  FUTURE_TIME=$(date -v $TYMER_LENGTH)
  FUTURE_TIME_SEC=$(date -v $TYMER_LENGTH +%s)

  if [[ $TYMER_DESC == "" ]]; then
    TYMER_DESC="No Description"
  fi
  echo $FUTURE_TIME_SEC:$FUTURE_TIME=$TYMER_DESC >> $TYMERS_FILE
}

########################################################
function deleteTymer() {
  line=$1
  sed -i '' "\:$line:d" $TYMERS_FILE
}

########################################################
function checkTymers() {
  # check each line of the file and compare to current time
  while read p; do
    seconds=`echo $p | sed 's/:.*//'`
    human_readable_time=`echo $p | sed 's/[^:]*://'`
    human_readable_time=`echo $human_readable_time | sed 's/=.*//'`
    current_tymer_desc=`echo $p | sed 's/[^=].*=//'`
    if [[ $seconds -lt $CURRENT_TIME_SEC ]]; then
      echo "######################################################"
      echo $seconds
      echo $human_readable_time
      echo $current_tymer_desc
      notifier $current_tymer_desc $human_readable_time
      deleteTymer $seconds
    fi
  done < $TYMERS_FILE
}


function notifier() {
  /usr/local/bin/terminal-notifier -title 'Tymer' -subtitle "$2" -message "$1"': Tymer has finished!'  -sound 'Ping'
}

########################################################
case $whichMethod in
  list     ) listTymers ;;
  ls       ) listTymers ;;
  add      ) TYMER_DESC=$2; TYMER_LENGTH=${3:-$DEFAULT_TYME}; addTymer ;;
  check    ) checkTymers ;;
  *        ) checkTymers ;;
esac
########################################################
