#!/bin/bash

set -e

echo "*****Starting the installation of Foglamp and Foglamp-GUI*****";

Pkg_Name=("centos-release-scl-rh" "foglamp" "epel-release" "nginx" "foglamp-gui")

for i in "${Pkg_Name[@]}"
do
	if ! rpm -q $i;
	then
		yum install -y $i

		if [ $? == 0 ]
		then
			echo "$i Installation Complete"
		else
			echo "$i Installation failed"
		fi
	fi
done
