# IdP Initiated<a name="iam_02_0002"></a>

This section uses the  **Client4ShibbolethIdP**  script as an example to describe how to obtain a federated authentication token in the IdP-initiated mode. The  **Client4ShibbolethIdP**  script simulates a user who logs in to the enterprise IdP using a browser. Therefore, by comparing the form data submitted by the browser and the client implementation data, this section helps users develop the client scripts of their enterprise IdP.

## **Prerequisites**<a name="section48708258144634"></a>

-   IdP-initiated federated identity authentication is supported by the enterprise IdP server.
-   The  **beautifulsoup4**  package of the Python module has been installed on the client.

## Flowchart<a name="section564187174136"></a>

The following figure shows the IdP-initiated federation authentication process.

**Figure  1**  Flowchart \(IdP-initiated\)<a name="fig563751422"></a>  
![](figures/flowchart-(idp-initiated).png "flowchart-(idp-initiated)")

## **Description**<a name="section13188540101541"></a>

1.  The client calls the login link provided by IdP based on the IdP-initiated mode and sets the public cloud address in the login link, that is,  **entityID**  in the metadata file of the public cloud.
2.  The client obtains the login page of the IdP. Users submit identity information to IdP for authentication through the client.
3.  After users pass the authentication, IdP constructs an assertion carrying the user identity information and sends the SAML response. The response passes through the client.
4.  The client encapsulates the SAML response, forwards the SAML response, and calls the API \(federated token obtained in the IdP-initiated mode\) provided by the public cloud system.
5.  The public cloud verifies and authenticates the assertion, and generates a temporary access credential according to the identity conversion rule configured by users in the identity provider.
6.  Users can access public cloud resources according to their permissions.

## Implementation on the Client<a name="section27488823174127"></a>

Download the  **Client4ShibbolethIdP.py**  script \(for reference only\) from the following website to implement the federated identity authentication script from the enterprise IdP to the API/CLI side of the cloud system:

[https://obs-iam-download.obs.eu-de.otc.t-systems.com/non-ecp-script/Client4ShibblethIdP.py](https://obs-iam-download.obs.eu-de.otc.t-systems.com/non-ecp-script/Client4ShibblethIdP.py)

1.  Configure the login URL of enterprise IdP.

    **Table  1**  Login URLs of common IdP products

    <a name="table22155984174553"></a>
    <table><thead align="left"><tr id="row47284103174553"><th class="cellrowborder" valign="top" width="23.18%" id="mcps1.2.4.1.1"><p id="p43264414174553"><a name="p43264414174553"></a><a name="p43264414174553"></a>IdP</p>
    </th>
    <th class="cellrowborder" valign="top" width="27.32%" id="mcps1.2.4.1.2"><p id="p14756651174553"><a name="p14756651174553"></a><a name="p14756651174553"></a>SP Identification Parameter in URL</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.5%" id="mcps1.2.4.1.3"><p id="p54438101174553"><a name="p54438101174553"></a><a name="p54438101174553"></a>Login URL Example</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20180864174553"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p24037279174553"><a name="p24037279174553"></a><a name="p24037279174553"></a>ADFS</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.32%" headers="mcps1.2.4.1.2 "><p id="p29271455174744"><a name="p29271455174744"></a><a name="p29271455174744"></a>logintorp</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.5%" headers="mcps1.2.4.1.3 "><p id="p2916699817486"><a name="p2916699817486"></a><a name="p2916699817486"></a>https://adfs-server.contoso.com/adfs/ls/IdpInitiatedSignon.aspx?logintorp=https://iam.example.com</p>
    </td>
    </tr>
    <tr id="row24861241174553"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p494601174553"><a name="p494601174553"></a><a name="p494601174553"></a>Shibboleth</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.32%" headers="mcps1.2.4.1.2 "><p id="p18864399174749"><a name="p18864399174749"></a><a name="p18864399174749"></a>providerId</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.5%" headers="mcps1.2.4.1.3 "><p id="p52181416174814"><a name="p52181416174814"></a><a name="p52181416174814"></a>https://idp.example.org/idp/profile/SAML2/Unsolicited/SSO?providerId=iam.example.com</p>
    </td>
    </tr>
    <tr id="row13347950174553"><td class="cellrowborder" valign="top" width="23.18%" headers="mcps1.2.4.1.1 "><p id="p7442185174553"><a name="p7442185174553"></a><a name="p7442185174553"></a>SimpleSAMLphp</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.32%" headers="mcps1.2.4.1.2 "><p id="p9906613174756"><a name="p9906613174756"></a><a name="p9906613174756"></a>spentityid</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.5%" headers="mcps1.2.4.1.3 "><p id="p11716400174821"><a name="p11716400174821"></a><a name="p11716400174821"></a>https://idp.example.org/simplesaml/saml2/idp/SSOService.php?spentityid=iam.example.com</p>
    </td>
    </tr>
    </tbody>
    </table>

    After the configuration, enter the login URL in the browser address box. The following page is displayed.

    **Figure  2**  Login Page<a name="fig18437552204714"></a>  
    ![](figures/login-page.jpg "login-page")

    Client4ShibbolethIdP script implementation:

    ```
    import sys
    import requests
    import getpass
    import re
    from bs4 import BeautifulSoup
    from urlparse import urlparse
    
    # SSL certificate verification: Whether or not strict certificate
    # verification is done, False should only be used for dev/test
    sslverification = True
    
    # Get the federated credentials from the user
    print "Username:",
    username = raw_input()
    password = getpass.getpass()
    print ''
    
    session = requests.Session()
    
    # The initial url that starts the authentication process.
    idp_entry_url = 'https://idp.example.com/idp/profile/SAML2/Unsolicited/SSO?providerId=https://iam.example.com'
    
    # Programmatically get the SAML assertion,open the initial IdP url# and follows all of the HTTP302 redirects, and gets the resulting# login page
    formresponse = session.get(idp_entry_url, verify=sslverification)
    # Capture the idp_authform_submit_url,which is the final url after# all the 302s
    idp_authform_submit_url = formresponse.url
    ```


1.  The client submits authentication information. The client parses the login page using the beautifulsoup4 module, captures the user information input box and requested action, constructs the request parameters, and initiates identity authentication to the IdP.

    Obtain all form data submitted for the login page from the browser.

    **Figure  3**  Authentication information \(1\)<a name="fig1887664312288"></a>  
    ![](figures/authentication-information-(1).png "authentication-information-(1)")

    Client4ShibbolethIdP script implementation:

    ```
    # Parse the response and extract all the necessary values in order to build a dictionary of all of the form values the IdP expects
    formsoup = BeautifulSoup(formresponse.text.decode('utf8'), "lxml")
    payload = {}
    
    for inputtag in formsoup.find_all(re.compile('(INPUT|input)')):
        name = inputtag.get('name', '')
        value = inputtag.get('value', '')
        if "username" in name.lower():
            payload[name] = username
        elif "password" in name.lower():
            payload[name] = password
        else:
            payload[name] = value
    
    for inputtag in formsoup.find_all(re.compile('(FORM|form)')):
        action = inputtag.get('action')
        if action:
            parsedurl = urlparse(idp_entry_url)
            idp_authform_submit_url = parsedurl.scheme + "://" + parsedurl.netloc + action
    
    # please test on browser first, add other parameters in payload
    payload["_eventId_proceed"] = ""
    
    formresponse = session.post(
        idp_authform_submit_url, data=payload, verify=sslverification)
    ```

2.  The client parses the next page. \(Some enterprise IdPs provide pages containing user attributes.\)

    Obtain all form data submitted for the login page from the browser.

    **Figure  4**  Authentication information \(2\)<a name="fig179001019556"></a>  
    ![](figures/authentication-information-(2).jpg "authentication-information-(2)")

    Client4ShibbolethIdP script implementation:

    ```
    # In shebbleth IdP v3, browser will show attributes page for user,# so we need parse the page
    formsoup = BeautifulSoup(formresponse.text.decode('utf8'), "lxml")
    payload = {}
    
    # Add other form data required from browser to payload
    _shib_idp_consentIds = []
    for inputtag in formsoup.find_all(re.compile('input')):
        name = inputtag.get("name")
        value = inputtag.get("value")
        if name == "_shib_idp_consentIds":
            _shib_idp_consentIds.append(value)
    payload["_shib_idp_consentIds"] = _shib_idp_consentIds
    payload["_shib_idp_consentOptions"] = "_shib_idp_rememberConsent"
    payload["_eventId_proceed"] = "Accept"
    
    # user can get the action url from the html file
    nexturl = "https://idp.example.com/idp/profile/SAML2/Unsolicited/SSO?execution=e1s2"
    
    for inputtag in formsoup.find_all(re.compile('(FORM|form)')):
        action = inputtag.get('action')
        if action:
            parsedurl = urlparse(idp_entry_url)
            nexturl = parsedurl.scheme + "://" + parsedurl.netloc + action
    
    response = session.post(
        nexturl, data=payload, verify=sslverification)
    ```

3.  The client parses the response message sent from the IdP. The client submits user information to the enterprise IdP for authentication. After authenticating the user information, the IdP sends a response message to the client. The client parses the  **SAMLResponse**  parameter in the response message.

    Client4ShibbolethIdP script implementation:

    ```
    # Decode the response and extract the SAML assertion
    soup = BeautifulSoup(response.text.decode('utf8'), "lxml")
    SAMLResponse = ''
    
    # Look for the SAMLResponse attribute of the input tag
    for inputtag in soup.find_all('input'):
        if (inputtag.get('name') == 'SAMLResponse'):
            SAMLResponse = inputtag.get('value')
    
    # Better error handling is required for production use.
    if (SAMLResponse == ''):
        print 'Response did not contain a valid SAML assertion, please troubleshooting in Idp side.'
        sys.exit(0)
    ```

4.  Obtain an unscoped token. For details, see  [Obtaining an Unscoped Token in Federated Identity Authentication Mode \(IdP Initiated\)](obtaining-an-unscoped-token-in-federated-identity-authentication-mode-(idp-initiated).md).

    Client4ShibbolethIdP script implementation:

    ```
    # Set headers
    headers = {}
    headers["X-Idp-Id"] = "test_local_idp"
    
    # IAM API url: get unscoped token on IDP initiated mode
    sp_unscoped_token_url = "https://iam.example.com/v3.0/OS-FEDERATION/tokens"
    
    # Set form data
    payload = {}
    payload["SAMLResponse"] = SAMLResponse
    response = session.post(
        sp_unscoped_token_url, data=payload, headers=headers, verify=sslverification)
    
    # Debug only
    print(response.text)
    print "Status Code: " + str(response.status_code)
    if response.status_code != 201:
        sys.exit(1)
    
    unscoped_token = response.headers.get("X-Subject-Token") if "X-Subject-Token" in response.headers.keys() else None
    if unscoped_token:
        print ">>>>>>X-Subject-Token: " + unscoped_token
    ```

5.  Obtain a scoped token. For details, see  [Obtaining a Scoped Token in Federated Identity Authentication Mode](obtaining-a-scoped-token-in-federated-identity-authentication-mode.md).

    Client4ShibbolethIdP script implementation:

    ```
    payload = {
        "auth": {
            "identity": {
                "methods": ["token"],
                "token": {
                    "id": unscoped_token
                }
            },
            "scope": {
                "project": {
                    "name": "{region_id}_test1"
                }
            }
        }
    }
    
    sp_scoped_token_url = "https://10.120.171.90:31943/v3/auth/tokens"
    
    response = session.post(
        sp_scoped_token_url, json=payload, verify=sslverification)
    
    # Debug only
    print "Status Code: " + str(response.status_code)
    if response.status_code != 201:
        print response.text
        sys.exit(1)
    
    scoped_token = response.text if response.status_code == 201 else None
    if scoped_token:
        print ">>>>>>Scoped Token:" + scoped_token
    ```

6.  Obtain a temporary AK/SK. For details, see  [Obtaining a Temporary AK/SK](obtaining-a-temporary-ak-sk.md).

    Client4ShibbolethIdP script implementation:

    ```
    # Set form data
    payload = {
        "auth": {
            "identity": {
                "methods": ["token"],
                "token": {
                    "duration-seconds": "900"
                }
            }
        }
    }
    
    # Set headers
    headers = {}
    headers["X-Auth-Token"] = unscoped_token
    
    sp_STS_token_url = "https://10.120.171.90:31943/v3.0/OS-CREDENTIAL/securitytokens"
    
    response = session.post(
        sp_STS_token_url, json=payload, headers=headers, verify=sslverification)
    
    # Debug only
    print "Status Code: " + str(response.status_code)
    if response.status_code != 201:
        print response.text
        sys.exit(1)
    
    sts_token = response.text if response.status_code == 201 else None
    if sts_token:
        print ">>>>>>STS Token:" + sts_token
    ```


