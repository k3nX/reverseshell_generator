#!/bin/bash
script=reverse.py
name=reverseshell-gen
filepath=/usr/bin


requirement(){
if ! [ -x "$(command -v git)" ]; then
  echo -e "\e[1;31m Error: Git is not found"
  echo $(apt install git)
else
  echo -e "\e[1;34m \t\t\t Git is found"
fi

if ! [ -x "$(command -v python3)" ]; then
  echo -e "\e[1;31m Error: Python is not found"
  echo $(apt install python3)
else
  echo -e "\e[1;34m \t\t\tPython is found"
fi
if ! [ -x "$(command -v nc)" ]; then
  echo -e "\e[1;31m Error : NC is not found "
  echo $(apt install nc)
else
  echo -e "\e[1;34m \t\t\t NC is found"
fi
}

changing(){
	chmod +x $script
	mv $script $name
	cp $name $filepath
	rm $name

}


main(){
if [ $UID -ne 0 ]; then
	echo "Pls run with root access"
	exit
else
	echo -e "\e[1;32m \t\t\t Checking some Requirements"
	requirement
	sleep 5
	changing

fi
if ! [ -x "$(command -v reverseshell-gen)" ]; then
	echo -e "\e[1;31m Installation and Changing Fail"
else
	echo -e "\e[1;32m Installation Successfull and You can use start use with reverseshell-gen command"
fi
}
main

