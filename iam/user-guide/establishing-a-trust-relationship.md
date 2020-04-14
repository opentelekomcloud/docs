# Establishing a Trust Relationship<a name="en-us_topic_0059870090"></a>

Establish a trust relationship between the two systems by exchanging metadata files.

1.  Download the metadata file of the cloud system. If a user needs to use both Web Single Sign-On \(WebSSO\) and API calling functions, the user has to download the metadata files of both the WebSSO and the API.
    -   WebSSO: Visit  [https://auth.otc.t-systems.com/authui/saml/metadata.xml](https://auth.otc.t-systems.com/authui/saml/metadata.xml). Right-click, choose  **Save As**, and set a file name, for example,  **websso-metadata.xml**.
    -   API calling: Visit https://_Endpoint address of a region_/v3-ext/auth/OS-FEDERATION/SSO/metadata, right-click on the page and choose  **Save As**, and set a file name, for example,  **api-metadata-region.xml**.

        The cloud system provides API gateways depending on the region for users to call APIs. To access multiple regions, a user needs to download metadata files of the corresponding regions.

2.  Obtain the metadata file of the enterprise IdP. For details about how to obtain this file, contact the administrator of the enterprise management system.
3.  Upload the metadata file of the cloud system to the enterprise IdP server. For details about how to upload the file, contact the administrator of the enterprise management system.
4.  Upload the metadata file of the enterprise IdP to the IAM server. For details, see section  [Creating an IdP](creating-an-idp.md).

