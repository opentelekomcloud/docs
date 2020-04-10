# Processing ECP Assertion Requests<a name="en-us_topic_0057845614"></a>

## Function Description<a name="section46562811165510"></a>

This interface is used to receive the response to AuthnRequest when an IAM service \(functioning as a service provider specified in the SAM L2.0 specification\) performs SSO login in an identity provider. AuthnRequest refers to the assertion request sent from the ECP to the service provider.

For the SAML2.0 specification, see  [https://en.wikipedia.org/wiki/SAML\_2.0](https://en.wikipedia.org/wiki/SAML_2.0).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You are not advised to obtain a token by directly calling this interface. You are advised to obtain a token using OpenStackClient.  

## URI<a name="section273229165510"></a>

URI format

POST /v3-ext/auth/OS-FEDERATION/SSO/SAML2/ECP

