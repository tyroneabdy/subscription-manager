# Notes on AutoTools

AutoTools is a very old system for configuring and compiling code.  It is
composed of multiple components, but for our purposes we are using two: autoconf
and automake.

## Autoconf

Autoconf starts with a file named `configure.ac`.  This file contains a series
of macros that are interpreted by M4.  The result is `configure` which is a
Bourne-shell compatible shell script that runs a series of checks and then takes
all the `Makefile.in` files that you give it and transforms them in to
Makefiles.  Autoconf can accept conditionals so that if you run `./configure
--enable-yum` for example, the resultant `Makefile` installs files related to
yum support.

## Automake

Automake starts with files named `Makefile.am`.  The `Makefile.am` file uses a
special syntax to denote source files, man pages, CFLAGS and LDFLAGS, etc.  That
file is then turned into a `Makefile.in` file which is in turn converted into a
`Makefile` by `configure`.

## The Difference

If the absurd level of indirection involved in Automake bothers you, you can
just write your own `Makefile.in` and autoconf will be happy to transform that
for you.  Autoconf is actually completely ignorant of Automake.

## How Do I AutoTool?

This branch just contains the `Makefile.am` files and `configure.ac` file.  In
order to get started, you will need to run `autoreconf -ivf`.  This will copy in
a lot of strange auxiliary files that AutoTools needs for some reason.  It will
also "compile" the `configure.ac` file and `Makefile.am` files into their
respective `configure` and `Makefile.in` artifacts.

At this point, you can run `./configure` with any options you like and then the
standard `make && make install` steps.

ProTip: Run `./configure --prefix=/tmp/some_temp_dir` when you are testing and
the `make install` step will dump everything under that directory instead of
defiling your actual system.
