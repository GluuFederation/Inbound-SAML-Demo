#!/usr/bin/env python

import os, shutil, glob



passportpath = '/opt/gluu-server-3.1.1/opt/gluu/node/passport/server'
oxAuthCustomPageAuth = '/opt/gluu-server-3.1.1/opt/gluu/jetty/oxauth/custom/pages/auth'
oxAuthCustomPagePassport = '/opt/gluu-server-3.1.1/opt/gluu/jetty/oxauth/custom/pages/auth/passport'
configfilePath = '/opt/gluu-server-3.1.1/etc/gluu/conf'

if not os.path.exists(os.path.join(oxAuthCustomPageAuth,"idp-metadata")):
    os.makedirs(os.path.join(oxAuthCustomPageAuth,"idp-metadata"))

if not os.path.exists(oxAuthCustomPageAuth):
    os.makedirs(oxAuthCustomPageAuth)

if not os.path.exists(oxAuthCustomPagePassport):
    os.makedirs(oxAuthCustomPagePassport)

shutil.copyfile("passportpostlogin.xhtml", os.path.join(oxAuthCustomPagePassport, 'passportpostlogin.xhtml'))
shutil.copyfile("app.js", os.path.join(passportpath, 'app.js'))
shutil.copyfile("configureStrategies.js", os.path.join(passportpath, 'auth', 'index.js'))
shutil.copyfile("saml.js", os.path.join(passportpath, 'auth', 'saml.js'))
shutil.copyfile("index.js", os.path.join(passportpath, 'routes', 'index.js'))
shutil.copyfile("passport-saml-config.json", os.path.join(configfilePath,'passport-saml-config.json'))




