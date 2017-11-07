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


print ("make sure you are running from gluu-server's chroot....")

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

nodeEnv = os.environ.copy()
nodeEnv['PATH'] = '%s/bin:' % '/opt/node' + nodeEnv['PATH']
run(['npm', 'install', 'passport-saml', '--save'], os.path.join('/opt', 'gluu', 'node', 'passport'),nodeEnv, True)
run(['npm', 'install', '-P'], os.path.join('/opt', 'gluu', 'node', 'passport'), nodeEnv, True)
subprocess.call(['chmod', '-R', '+w', os.path.join('/opt', 'gluu', 'node', 'passport')])


print ("setup done please restart oxAuth server and passport server with commands")
print ("\n service oxauth stop")
print ("\n service oxauth start")
print ("\n service passport stop")
print ("\n service passport start")

