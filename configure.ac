#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])
AC_INIT([subscription-manager], [1.20.0], [])

# A file that should be in the src directory
AC_CONFIG_SRCDIR([src/__init__.py])
AM_INIT_AUTOMAKE([foreign subdir-objects])

# Checks for programs.
AC_PROG_AWK
AC_PROG_CC
AC_PROG_CPP
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET

# Minimum version of Python required
AM_PATH_PYTHON([2.6])

AC_ARG_ENABLE(
    [yum],
    [AS_HELP_STRING([--enable-yum], [enable yum plugins; default = yes])],
    [with_yum=$enableval],
    [with_yum=yes]
)

AC_ARG_ENABLE(
    [dnf],
    [AS_HELP_STRING([--enable-dnf], [enable dnf plugins; default = no])],
    [with_dnf=$enableval],
    [with_dnf=no]
)

AC_ARG_ENABLE(
    [ostree],
    [AS_HELP_STRING([--enable-ostree], [enable ostree; default = no])],
    [with_ostree=$enableval],
    [with_ostree=no]
)

AC_ARG_WITH(
    [gtk2],
    [AS_HELP_STRING([--with-gtk2], [use GTK2; default = no])],
    [with_gtk2=$enableval],
    [with_gtk2=no]
)

AC_ARG_WITH(
    [kitchen],
    [AS_HELP_STRING([--with-kitchen], [use python-kitchen; default = yes])],
    [with_kitchen=$enableval],
    [with_kitchen=yes]
)

# Checks for header files.
AC_CHECK_HEADERS(
    [fcntl.h libintl.h locale.h stdlib.h string.h sys/file.h sys/time.h unistd.h])

# See http://tirania.org/blog/archive/2012/Oct-20.html
if pkg-config glib-2.0; then
    GLIB_CFLAGS=`pkg-config --cflags glib-2.0`
    GLIB_LIBS=`pkg-config --libs glib-2.0`
else
    AC_MSG_ERROR([Missing glib])
fi
AC_SUBST([GLIB_CFLAGS])
AC_SUBST([GLIB_LIBS])

if pkg-config libnotify gconf-2.0 dbus-glib-1; then
    ICON_CFLAGS=`pkg-config --cflags libnotify gconf-2.0 dbus-glib-1`
    ICON_LIBS=`pkg-config --libs libnotify gconf-2.0 dbus-glib-1`
else
    AC_MSG_ERROR([Missing libnotify, gconf-2.0, and/or dbus-glib-1])
fi
AC_SUBST([ICON_CFLAGS])
AC_SUBST([ICON_LIBS])

if pkg-config gtk+-3.0; then
    GTK_CFLAGS=`pkg-config --cflags gtk+-3.0`
    GTK_LIBS=`pkg-config --libs gtk+-3.0`
else
    AC_MSG_ERROR([Missing gtk+-3.0])
fi
AC_SUBST([GTK_CFLAGS])
AC_SUBST([GTK_LIBS])

# Checks for typedefs, structures, and compiler characteristics.
AC_CHECK_HEADER_STDBOOL
AC_TYPE_SIZE_T

# Checks for library functions.
AC_FUNC_ERROR_AT_LINE
AC_FUNC_FORK
AC_FUNC_MALLOC
AC_CHECK_FUNCS([gettimeofday setlocale strerror strndup])

AC_CONFIG_FILES([Makefile \
                 src/Makefile \
                 src/daemons/Makefile \
                 src/rhsm_icon/Makefile \
                 src/rct/Makefile \
])
AC_OUTPUT
