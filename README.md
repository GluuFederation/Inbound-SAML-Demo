# Proxy-client


* Proxy-client is the demo application in node.js to test [**Passport Inbound SSO**](https://github.com/GluuFederation/gluu-passport/wiki/Passport-Inbound-SSO) 


>It is very easy to run. You just require latest node-js installed on your machine 
###Steps

1. Clone project using git clone
1. Register new OIDC client in you gluu server with redirect uri _http://localhost:3000/profile_ and copy clientID and secrete.
1. open **client-config.json** and file details like openid ClientID clinetSecret and hostname
1. copy same **passport-saml-config.json** which you used in setting up [**Passport Inbound SSO**](https://github.com/GluuFederation/gluu-passport/wiki/Passport-Inbound-SSO) 
1. open terminal navigate to project directory
1. execute following commands 
    1. `npm install`
    1.  `node server.js`
1. Thats it to open demo ,hit http:localhost:3000 in browser.


### Demo video link 
https://youtu.be/ubhDgGU8C8s