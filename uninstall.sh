#!/bin/bash

commandpath=/usr/bin/reverseshell-gen
uninstall(){
	read -p "Are you sure to want to install this (Y|n): " choice
	if [ $choice == 'Y' ]; then
		rm $commandpath
		#rm -rf $(pwd)
	fi 
	if [ $choice == 'y' ]; then
		rm $commandpath
		#rm -rf $(pwd)
	else
		exit
	fi	
}
main(){
	echo -e "\e[1;31m \t\t\t Unistallation Script "
	uninstall
}
main
