#!/bin/bash

set -e

echo "*****Starting the installation of Foglamp and Foglamp-GUI*****";

PkgName=("centos-release-scl-rh" "foglamp" "epel-release" "nginx" "foglamp-gui")

for i in "${PkgName[@]}"
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
