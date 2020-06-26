# Processing WebSSO Assertion Requests<a name="en-us_topic_0057845580"></a>

## Function Description<a name="section36235907165523"></a>

This interface is used to receive the response message \(that is, the assertion request sent by the IdP to the SP\) of the AuthnRequest request when the IAM service serves as the service provider \(SP\) in SAML 2.0 specifications and when the SP and Identity Provider \(IdP\) implement the single sign-on \(SSO\).

For the SAML2.0 specification, see  [https://en.wikipedia.org/wiki/SAML\_2.0](https://en.wikipedia.org/wiki/SAML_2.0).

>![](/images/icon-note.gif) **NOTE:**   
>You are not advised to obtain a token by directly calling this interface. You are advised to obtain a token using OpenStackClient.  

## URI<a name="section22949270165523"></a>

URI format

POST /v3-ext/auth/OS-FEDERATION/SSO/SAML2/POST

