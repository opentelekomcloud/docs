# SP Initiated<a name="iam_02_0001"></a>

OpenStack and Shibboleth are widely used open-source federated identity authentication solutions. They provide powerful SSO capabilities and connect users to various applications both inside and outside enterprises. This section describes how to use OpenStackClient and Shibboleth ECP Client to obtain the federated authentication token.

## Flowchart<a name="section59576151105219"></a>

The following figure shows the SP-initiated federation authentication process.

**Figure  1**  Flowchart \(SP-initiated\)<a name="fig28153389558"></a>  
![](figures/flowchart-(sp-initiated).png "flowchart-(sp-initiated)")

## Description<a name="section27567425105336"></a>

1.  The client calls the API \(federated token obtained in the SP-initiated mode\) provided by the public cloud system.
2.  The public cloud system searches for the metadata file based on the user and IdP information in the URL and sends the SAML request to the client.
3.  The client encapsulates the SAML request and forwards the SAML request to the IdP.
4.  A user enters a username and password on the IdP server for identity authentication.
5.  After the user passes the authentication, IdP constructs an assertion carrying the user identity information and sends the SAML response. The response passes through the client.
6.  The client encapsulates the SAML response and forwards the SAML response to the public cloud.
7.  The public cloud verifies and authenticates the assertion, and generates a temporary access credential according to the identity conversion rule configured by users in the identity provider.
8.  Users can access public cloud resources according to their permissions.

## OpenStackClient<a name="section4882433491913"></a>

You must have permissions of user  **root**  to install the unified command-line client. To perform the following operations, you only need to have the permissions of a common user.

>![](/images/icon-notice.gif) **NOTICE:**   
>The API calling operation must be performed in a secure network environment \(in a VPN or a cloud server of a domain\). Otherwise, this operation may be under the man-in-the-middle \(MITM\) attack.  

1.  Create an environment variable file under the installation directory of OpenStackClient. Modify the environment variable file in a text editor. Add parameters, such as the username, password, region, SAML protocol version, and the IP address and port number of IAM, to the file.  [Table 1](#table2616118811159)  describes the parameters.

    For example:

    **export OS\_IDENTITY\_API\_VERSION=3**

    **export OS\_AUTH\_TYPE=v3samlpassword**

    **export OS\_AUTH\_URL=https://iam.eu-de.otc.t-systems.com:443/v3**

    **export OS\_IDENTITY\_PROVIDER=idpid**

    **export OS\_PROTOCOL=saml**

    **export OS\_IDENTITY\_PROVIDER\_URL=https://idp.example.com/idp/profile/SAML2/SOAP/ECP**

    **export OS\_USERNAME=username**

    **export OS\_PASSWORD=userpassword**

    **export OS\_DOMAIN\_NAME=example-domain-name**

    **Table  1**  Parameter description

    <a name="table2616118811159"></a>
    <table><thead align="left"><tr id="row964009311159"><th class="cellrowborder" valign="top" width="41.410000000000004%" id="mcps1.2.3.1.1"><p id="p2459196311159"><a name="p2459196311159"></a><a name="p2459196311159"></a><strong id="b842352706183148"><a name="b842352706183148"></a><a name="b842352706183148"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.2.3.1.2"><p id="p3186528411159"><a name="p3186528411159"></a><a name="p3186528411159"></a><strong id="b20601766145329"><a name="b20601766145329"></a><a name="b20601766145329"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6315442511159"><td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.3.1.1 "><p id="p6145384811159"><a name="p6145384811159"></a><a name="p6145384811159"></a>OS_IDENTITY_API_VERSION</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.3.1.2 "><p id="p141497811159"><a name="p141497811159"></a><a name="p141497811159"></a>Indicates the authentication API version. The value is fixed at <strong id="b842352706163656"><a name="b842352706163656"></a><a name="b842352706163656"></a>3</strong>.</p>
    </td>
    </tr>
    <tr id="row4912462111159"><td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.3.1.1 "><p id="p1770061211159"><a name="p1770061211159"></a><a name="p1770061211159"></a>OS_AUTH_TYPE</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.3.1.2 "><p id="p2195067811159"><a name="p2195067811159"></a><a name="p2195067811159"></a>Indicates the authentication type. The value is fixed at <strong id="b842352706163941"><a name="b842352706163941"></a><a name="b842352706163941"></a>v3samlpassword</strong>.</p>
    </td>
    </tr>
    <tr id="row6006483511159"><td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.3.1.1 "><p id="p3868335311159"><a name="p3868335311159"></a><a name="p3868335311159"></a>OS_AUTH_URL</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.3.1.2 "><p id="p5892303511159"><a name="p5892303511159"></a><a name="p5892303511159"></a>Indicates the authentication URL. The value format is <strong id="b842352706164022"><a name="b842352706164022"></a><a name="b842352706164022"></a>https://</strong><em id="i896633800164012"><a name="i896633800164012"></a><a name="i896633800164012"></a>IAM</em> <em id="i1159210620164012"><a name="i1159210620164012"></a><a name="i1159210620164012"></a>IP address</em>:<em id="i2129740593164012"><a name="i2129740593164012"></a><a name="i2129740593164012"></a>Port number</em>/<em id="i523599690164012"><a name="i523599690164012"></a><a name="i523599690164012"></a>API version</em>.</p>
    <a name="ul6607261211159"></a><a name="ul6607261211159"></a><ul id="ul6607261211159"><li><em id="i84235269716419"><a name="i84235269716419"></a><a name="i84235269716419"></a>Port number</em> is fixed at <strong id="b842352706164123"><a name="b842352706164123"></a><a name="b842352706164123"></a>443</strong>.</li><li><em id="i842352697164143"><a name="i842352697164143"></a><a name="i842352697164143"></a>API version</em> is fixed at <strong id="b842352706163656_1"><a name="b842352706163656_1"></a><a name="b842352706163656_1"></a>v3</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row670881411159"><td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.3.1.1 "><p id="p6258503011159"><a name="p6258503011159"></a><a name="p6258503011159"></a>OS_IDENTITY_PROVIDER</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0117430799_p673860111159"><a name="en-us_topic_0117430799_p673860111159"></a><a name="en-us_topic_0117430799_p673860111159"></a>Indicates the name of an identity provider created by a user in the cloud system. For example: Publiccloud-Shibboleth.</p>
    </td>
    </tr>
    <tr id="row5188181311159"><td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.3.1.1 "><p id="p2864808511159"><a name="p2864808511159"></a><a name="p2864808511159"></a>OS_DOMAIN_NAME</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.3.1.2 "><p id="p191566411159"><a name="p191566411159"></a><a name="p191566411159"></a>Indicates the domain name to be authenticated.</p>
    </td>
    </tr>
    <tr id="row352821311159"><td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.3.1.1 "><p id="p710320411159"><a name="p710320411159"></a><a name="p710320411159"></a>OS_PROTOCOL</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.3.1.2 "><p id="p331103911159"><a name="p331103911159"></a><a name="p331103911159"></a>Indicates the SAML protocol version. The value is fixed at <strong id="b842352706173913"><a name="b842352706173913"></a><a name="b842352706173913"></a>saml</strong>.</p>
    </td>
    </tr>
    <tr id="row4918301011159"><td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.3.1.1 "><p id="p3501460111159"><a name="p3501460111159"></a><a name="p3501460111159"></a>OS_IDENTITY_PROVIDER_URL</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.3.1.2 "><p id="p5623476111318"><a name="p5623476111318"></a><a name="p5623476111318"></a>Indicates the URL of the identity provider used to handle the authentication request initialized by the ECP.</p>
    </td>
    </tr>
    <tr id="row5886868711159"><td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.3.1.1 "><p id="p1132443811159"><a name="p1132443811159"></a><a name="p1132443811159"></a>OS_USERNAME</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.3.1.2 "><p id="p4587034311159"><a name="p4587034311159"></a><a name="p4587034311159"></a>Indicates the name of a user who is authenticated in the identity provider.</p>
    </td>
    </tr>
    <tr id="row6598712211159"><td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.3.1.1 "><p id="p2199843211159"><a name="p2199843211159"></a><a name="p2199843211159"></a>OS_PASSWORD</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.3.1.2 "><p id="p4795367211159"><a name="p4795367211159"></a><a name="p4795367211159"></a>Indicates the password of a user who is authenticated in the identity provider.</p>
    </td>
    </tr>
    </tbody>
    </table>

2.  Run the following command to set environment variables:

    **source keystonerc**

3.  Run the following command to obtain a token:

    **openstack token issue**

    ```
    >>openstack token issue 
    command: token issue -> openstackclient.identity.v3.token.IssueToken (auth=True)
    Using auth plugin: v3samlpassword
    +-----------------------------------------------------------------------------------------------------------
    | Field   | Value
    | expires | 2018-04-16T03:46:51+0000                              
    | id      | MIIDbQYJKoZIhvcNAQcCoIIDXjXXX...
    | user_id | 9B7CJy5ME14f0fQKhb6HJVQdpXXX...
    ```

    In the command output,  **id**  is the obtained federated authentication token.


## Shibboleth ECP Client<a name="section4918283814425"></a>

1.  Configure the  **metadata-providers.xml**  file in Shibboleth IdP v3 and save the  **metadata.xml**  file in the corresponding path.

    ```
    <MetadataProvider id="LocalMetadata1"xsi:type="FilesystemMetadataProvider" metadataFile="C:\Program Files (x86)\Shibboleth\IdP\metadata\web_metadata.xml"/>
    <MetadataProvider id="LocalMetadata2"xsi:type="FilesystemMetadataProvider" metadataFile="C:\Program Files (x86)\Shibboleth\IdP\metadata\api_metadata.xml"/>
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >-   **MetadataProvider id**  indicates the name of the downloaded metadata file of the SP system.  
    >-   **metadataFile**  indicates the path for storing the metadata file of the SP system in the enterprise IdP.  

2.  Configure the  **attribute-filter.xml**  file in Shibboleth IdP v3.

    ```
    <afp:AttributeFilterPolicy id="example1">
        <afp:PolicyRequirementRule xsi:type="basic:AttributeRequesterString" value="https://auth.example.com/" />
        <afp:AttributeRule attributeID="eduPersonPrincipalName">
            <afp:PermitValueRule xsi:type="basic:ANY" />
        </afp:AttributeRule>
        <afp:AttributeRule attributeID="uid">
            <afp:PermitValueRule xsi:type="basic:ANY" />
        </afp:AttributeRule>
        <afp:AttributeRule attributeID="mail">
            <afp:PermitValueRule xsi:type="basic:ANY" />
        </afp:AttributeRule>
    </afp:AttributeFilterPolicy>
    
    <afp:AttributeFilterPolicy id="example2">
        <afp:PolicyRequirementRule xsi:type="basic:AttributeRequesterString" value="https://iam.{region_id}.example.com" />
        <afp:AttributeRule attributeID="eduPersonPrincipalName">
            <afp:PermitValueRule xsi:type="basic:ANY" />
        </afp:AttributeRule>
        <afp:AttributeRule attributeID="uid">
            <afp:PermitValueRule xsi:type="basic:ANY" />
        </afp:AttributeRule>
        <afp:AttributeRule attributeID="mail">
            <afp:PermitValueRule xsi:type="basic:ANY" />
        </afp:AttributeRule>
    </afp:AttributeFilterPolicy>
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >**AttributeFilterPolicy id**  indicates the name of the downloaded metadata file of the SP system.  
    >**value**  indicates the  **EntityID**  in the metadata file of the SP system.  

3.  Configure the endpoint address of the enterprise IdP in the  [ecp.py](https://wiki.shibboleth.net/confluence/display/SHIB2/Contributions#Contributions-simplepython)  script.

    ```
    # mapping from user friendly names or tags to IdP ECP enpoints
    IDP_ENDPOINTS = {
        "idp1": "https://idp.example.com/idp/profile/SAML2/SOAP/ECP"
    }
    ```

4.  Run the  **ecp.py**  script to obtain the federated authentication token.

    ```
    >>python ecp.py
    Usage: ecp.py [options] IdP_tag target_url login
    >>python ecp.py -d idp1 https://iam.{region_id}.example.com/v3/OS-FEDERATION/identity_providers/idp_example/protocols/saml/auth {username}
    X-Subject-Token: MIIDbQYJKoZIhvcNAQcCoIIDXXX...
    ```

    **X-Subject-Token**  is the obtained federated authentication token.


