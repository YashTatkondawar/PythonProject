#!/bin/bash

set -e

echo "*****Starting the uninstallation of Foglamp and Foglamp-GUI*****";

Pkg_Name=("foglamp-gui" "nginx" "epel-release" "foglamp" "centos-release-scl-rh")

for i in "${Pkg_Name[@]}"
do
	if rpm -q $i;
	then
		yum remove -y $i

		if [ $? == 0 ]
		then
			echo "$i removed successfully"
		else
			echo "Failed to removed $i"
		fi
	fi
done
