#!/usr/bin/env python

import os, shutil, glob, subprocess

passportpath = '/opt/gluu/node/passport/server'
oxAuthCustomPageAuth = '/opt/gluu/jetty/oxauth/custom/pages/auth'
oxAuthCustomPagePassport = '/opt/gluu/jetty/oxauth/custom/pages/auth/passport'
configfilePath = '/etc/gluu/conf'


def run(args, cwd=None, env=None, usewait=False):
    try:
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd, env=env)
        if usewait:
            code = p.wait()
        else:
            output, err = p.communicate()
            if output:
                print (output)
            if err:
                print (err)
    except:
        print ("Error running command : %s" % " ".join(args), True)


if not os.path.exists(os.path.join(passportpath, "idp-metadata")):
    os.makedirs(os.path.join(passportpath, "idp-metadata"))

if not os.path.exists(oxAuthCustomPageAuth):
    os.makedirs(oxAuthCustomPageAuth)

if not os.path.exists(oxAuthCustomPagePassport):
    os.makedirs(oxAuthCustomPagePassport)

shutil.copyfile("passportpostlogin.xhtml", os.path.join(oxAuthCustomPagePassport, 'passportpostlogin.xhtml'))
shutil.copyfile("app.js", os.path.join(passportpath, 'app.js'))
shutil.copyfile("configureStrategies.js", os.path.join(passportpath, 'auth', 'configureStrategies.js'))
shutil.copyfile("saml.js", os.path.join(passportpath, 'auth', 'saml.js'))
shutil.copyfile("index.js", os.path.join(passportpath, 'routes', 'index.js'))
shutil.copyfile("passport-saml-config.json", os.path.join(configfilePath, 'passport-saml-config.json'))

run(['npm', 'install', 'passport-saml', '--save'], os.path.join('/opt', 'gluu', 'node', 'passport'),os.environ.copy(), True)

print ("setup done please restart oxAuth server and passport server with commands in side gluu-server's chroot ")
print ("\n service gluu-server-3.1.1 login  //to login inside gluu server's chroot")
print ("\n service oxauth stop")
print ("\n service oxauth start")
print ("\n service passport stop")
print ("\n service passport start")

# run(['cd', os.path.join('opt', 'gluu', 'node', 'passport')], os.environ.copy(), True)

