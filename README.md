# Proxy-client


Proxy-client is a node.js demo application to test [**Passport SAML Inbound single sign-on (SSO)**](https://github.com/GluuFederation/gluu-passport/wiki/Passport-Inbound-SSO). 

The sample app requires the latest version of node-js installed on your machine 


## Steps

1. Clone project using git clone
1. Register new OIDC client in you gluu server with redirect uri `http://localhost:3000/profile` and copy clientID and secrete.
1. Open **client-config.json** and file details like openid ClientID clinetSecret and hostname
1. Copy same **passport-saml-config.json** which you used in setting up [**Passport Inbound SSO**](https://github.com/GluuFederation/gluu-passport/wiki/Passport-Inbound-SSO) 
1. Open terminal navigate to project directory
1. Execute following commands 
    1. `npm install`
    1.  `node server.js`
1. Navigate to `http:localhost:3000` in your browser.


## Demo video link 
https://youtu.be/ubhDgGU8C8s
