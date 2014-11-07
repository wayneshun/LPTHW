# -*- coding: utf-8 -*-
#
#    Copyright © 2008 Pierre Raybaut
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#    
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import os, sys, shutil, re
from time import ctime
from _winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE

__version__ = '1.0.6'
XY = 'Python(x,y)'
PYTHON_EXE = sys.executable
PYTHON_EXE_WIN = os.path.join( os.path.split( PYTHON_EXE )[0], 'pythonw.exe' )
SCRIPTDIR = os.path.join(sys.prefix, 'Scripts')
POSTINSTALL_SUFFIX = ['_win_post_install.py', '_postinstall.py']


# Windows registry ------
def get_package_name(filename):
    package_name = os.path.split(filename)[1]
    for suffix in POSTINSTALL_SUFFIX:
        package_name = package_name.replace(suffix,'')
    return package_name
    
def get_install_key(program):
    keystr = "Software\%s" % program
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,keystr)
    except WindowsError:
        try:
            key = OpenKey(HKEY_CURRENT_USER,keystr)
        except WindowsError:
            raise WindowsError, "%s is not installed on this computer" % program
    return key

def get_install_param(program, param=''):
    try:
        value = QueryValueEx(get_install_key(program), param)[0]
        if param:
            param = param + ': '
#        print "Plugin '%s' was found (%s%s)" % (program, param, value)
    except WindowsError:
        print "Warning: Module '"+program+"' is not installed on this computer"
        return None
    return value

VERSION = get_install_param(XY,'Version')
DOC = get_install_param(XY,'DocPath')

# Post-install log file ------
def get_log_filename(name):
    if os.path.exists(name): # name is a filename
        name = get_package_name(name)
    path = get_install_param(name)
    return os.path.join(path, 'post_install.log')

def create_log_file(name):
    sys.stderr = open( get_log_filename(name) ,'w')
    sys.stdout = sys.stderr
    width = 80
    sep = "-"*width
    infos = [sep, XY+" post-install log (xyinstall "+__version__+")",
             "Module name: "+name,ctime(), sep]
    for line in infos:
        print line.center(width)+"\n"
    print "\n"
    
def remove_log_file(name):
    path = get_log_filename(name)
    if os.path.exists(path):
        os.remove(path)


# Manipulating text files ------
def find_line(lines,findstr):
    i_find_list = [lines.index(line) for line in lines if line.find(findstr)>-1]
    if len(i_find_list):
        return i_find_list[0]
    return i_find_list
    
def replace_in_file(filename, findstr, replacestr):
    lines = file(filename).readlines()
    i_find = find_line(lines, findstr)
    if i_find:
        lines[i_find] = lines[i_find].replace(findstr,replacestr)
        file(filename, 'w').writelines(lines)

def insert_or_replace_line(filename, line, findstr1, findstr2=None ):
    if not line.endswith('\n'):
        line += '\n'
    lines = file(filename).readlines()
    i_find = find_line(lines, findstr1)
    if i_find:
        lines[i_find] = line
    else:
        i_find = find_line(lines, findstr2) if findstr2 else len(lines)
        lines.insert(i_find+1, line)
    file(filename, 'w').writelines(lines)

def remove_line(filename, findstr_list):
    lines = file(filename).readlines()
    if not isinstance(findstr_list,list):
        findstr_list = [findstr_list]
    for findstr in findstr_list:
        i_find = find_line(lines,findstr)
        if i_find:
            lines.remove(lines[i_find])
    file(filename, 'w').writelines(lines)

# Scripts ------
def copy_script( raw, py, exe ):
    '''fixes the python executable line if exists'''
    first_line_re = re.compile('^#!.*python[0-9.]*\s*')
    f = open(raw, "r")
    first_line = f.readline()
    match = first_line_re.match(first_line)
    if match:
        outf = open(py, "w")
        outf.write("#!%s\n" % (exe))
        outf.writelines(f.readlines())
        outf.close()
        f.close()
    else:
        f.close()
        shutil.copy(raw, py)
        
def install_scripts(programs=[]):
    if not programs:
        return
    print "\nAdding %d scripts..." % len(programs),
    for program in programs:
        raw = os.path.join(SCRIPTDIR, program).replace('*', '')
        py = raw + '-script.py'
        using_start = ""
        exe = os.path.basename(PYTHON_EXE)
        if program.endswith('*'):
            py+='w'
            using_start = r'start "" '
            exe = os.path.basename(PYTHON_EXE_WIN)
        bat = raw + '.bat'
        copy_script(raw, py, exe)
        #shutil.copy(raw, py)
        bat_file = file(bat,'w')
        bat_file.write("@%s\"%s\" \"%s\" %%*" % (using_start, exe, py))
        bat_file.close()
    print "OK"

def remove_scripts(programs=[]):
    for program in programs:
        raw = os.path.join(SCRIPTDIR, program).replace('*', '')
        [ os.remove(path) for path in [raw+'.bat', raw+'-script.py',
        raw+'-script.pyw'] if os.path.exists(path) ]


# Install/Uninstall ------
def install(file=None, scriptlist=[], other=[]):
    if file:
        create_log_file(file)
    install_scripts(scriptlist)
    if other:
        if not isinstance(other,list):
            other = [other]
        for package_name in other:
            for suffix in POSTINSTALL_SUFFIX:
                os.chdir( os.path.dirname(file) )
                post_install = package_name+suffix
                if os.path.exists(post_install):
                    print "Executing %s post-install script..." % package_name,
                    print "( %s )" % post_install,
                    os.system(post_install+' -install')
                    print "OK"
    print "\n\nPost-install script has been successfully executed."

def remove(file, scriptlist=[], other=[]):
    remove_log_file(file)
    remove_scripts(scriptlist)


# Main ------
def main(file, argv, scripts=[], prefs_filename='', prefs=(), other=[]):
    if len(argv) > 1:
        if argv[1] == '-install':
            install(file, scriptlist=scripts, other=other)
        elif argv[1] == '-remove':
            remove(file, scriptlist=scripts, other=other)
        else:
            print "Script was called with option %s" % sys.argv[1]
    else:
        print "Module <xyinstall.main>: options -install or -remove"
        print "(xyinstall %s)" % __version__
