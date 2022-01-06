'''
this script creates a boilerplate for a php
projects by the pre-installed bitnami LAMP package 
configurations.
Gabriele Boccarusso -- 2022/01/05
'''
import shutil
import os
import re

def get_name():
    flag = 'n'
    name = input("enter name of the project: ")

    while flag == 'n':
        while ' ' in name:
           name = input("enter a valid name: ")
        print("Are you sure of the such name?")
        print("-- " + name)
        flag = input("[Y/n] ")
    
    return name

def make_app(name):
    '''
    makes httpd-app.conf
    '''
    fl = open(name + "/conf/httpd-app.conf", 'w')
    lines = [
        '<Directory "/home/boccarusso/lamp/apps/$$$/htdocs">',
        '\t' + 'Options Indexes MultiViews',
        '\t' + 'AllowOverride All',
        '\t' + '<IfVersion < 2.3 >',
        '\t' + 'Order allow,deny',
        '\t' + 'Allow from all',
        '\t' + '</IfVersion>',
        '\t' + '<IfVersion >= 2.3>',
        '\t' + 'Require all granted',
        '\t' + '</IfVersion>',
        '</Directory>'
        ]
    lines[0] = re.sub('(\$\$\$)', name, lines[0])

    for line in lines:
        fl.write(line)
        fl.write('\n')

    fl.close()

def make_prefix(name):
    '''
    makes httpd-prefix.conf
    '''
    fl = open(name + "/conf/httpd-prefix.conf", 'w')
    lines = [
        'Alias /$$$/ "/home/boccarusso/lamp/apps/$$$/htdocs/"',
        'Alias /$$$ "/home/boccarusso/lamp/apps/$$$/htdocs"',
        '',
        'Include "/home/boccarusso/lamp/apps/$$$/conf/httpd-app.conf"'
    ]

    for line in lines:
        line = re.sub('(\$\$\$)', name, line)
        fl.write(line)
        fl.write('\n')

    fl.close()

def make_vhosts(name):
    '''
    makes https-vhosts.conf
    '''
    fl = open(name + "/conf/httpd-vhosts.conf", 'w')
    lines = [
        '<VirtualHost *:8080>',
        '\t' + 'ServerName $$$.example.com',
        '\t' + 'DocumentRoot "/home/boccarusso/lamp/apps/$$$/htdocs"',
        '\t' + 'Include "/home/boccarusso/lamp/apps/$$$/conf/httpd-app.conf"',
        '</VirtualHost>'
    ]

    for line in lines:
        line = re.sub('(\$\$\$)', name, line)
        fl.write(line)
        fl.write('\n')

    fl.close()

def make_htdocs(name):
    '''
    creates a sample index.php file
    '''
    fl = open(name + "/htdocs/index.php", 'w')
    lines = [
        '<!DOCTYPE html>',
        '<html lang="en">',
        '<head>',
        '\n' + '<meta charset="UTF-8">',
        '\n' + '<meta http-equiv="X-UA-Compatible" content="IE=edge">',
        '\n' + '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '\n' + '<title>$$$</title>',
        '</head>',
        '<body>',
        '\n' + '<h1> $$$ is ready </h1>',
        '</body>',
        '</html>'
    ]

    for line in lines:
        line = re.sub('(\$\$\$)', name, line)
        fl.write(line)
        fl.write('\n')

    fl.close()

def move(name):
    '''
    moves the newly created folder into the 
    designated folder
    '''
    name += '/'
    target = '../lamp/apps/'
    shutil.move(name, target)

def include(name):
    '''
    appends the newly created folder with the other applications
    '''
    target = '../lamp/apache2/conf/bitnami/bitnami-apps-prefix.conf'
    fl = open(target, 'a')
    line = 'Include "/home/boccarusso/lamp/apps/$$$/conf/httpd-prefix.conf"'

    line = re.sub('(\$\$\$)', name, line)
    fl.write(line)
    fl.write('\n')

    fl.close()

def make_prj():
    '''
    make a new projects
    from zero
    '''
    name = get_name()

    os.mkdir(name)
    os.mkdir(name + "/conf")
    os.mkdir(name + "/htdocs")

    make_app(name)
    make_prefix(name)
    make_vhosts(name)

    make_htdocs(name)
    move(name)
    include(name)

    print(name, "was successfully created")
    print('--', 'restart apache web server')
    print('--', "go \"localhost:8080/" + name + "\"")

if __name__ == '__main__':
    make_prj()
