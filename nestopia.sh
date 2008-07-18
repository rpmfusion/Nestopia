#!/bin/bash

# Nestopia launch script
# Jul 16 2008 Andrea Musuruane <musuruan@gmail.com>

EXECNAME=nst
DATADIR=/usr/share/Nestopia
USERDIR=$HOME/.nestopia

# Push current working directory
pushd . > /dev/null

# See if user already has his personal directoy
if ! [ -d $USERDIR ]
then
	# No, let's set it up!
	mkdir -p $USERDIR
	cd $USERDIR

	# Create links to files which are not (usually) modified by users
	for i in $DATADIR/NstDatabase.xml
	do
		ln -s $i
	done

	# Copy files which can be modified by users
	for i in $DATADIR/nstcontrols
	do
		cp $i .
	done
fi

# Remove and update user files
if [ -L $USERDIR/NstDatabase.dat ]
then
	cd $USERDIR
	rm NstDatabase.dat
	ln -s $DATADIR/NstDatabase.xml
fi

# Pop working directory
popd > /dev/null

# Run main program
exec $EXECNAME "$@"

