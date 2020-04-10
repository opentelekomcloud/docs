# Advantages of Federated Identity Authentication<a name="en-us_topic_0079620341"></a>

If you have an identity authentication system, you do not need to recreate users in the SP system and can configure federated identity authentication to allow users in your system to access cloud resources directly through SSO.

Federated identity authentication is required for browser-based WebSSO or non-browser-based API calling access to the cloud system.

-   WebSSO: A browser is used as a communication media and can be used by common users to access the cloud system.
-   API calling: A development tool or an application is used as a communication media, for example, OpenStackClient, which is applicable to enterprises or users who use development tools to call APIs to access the cloud system.

    API calling has the SP-initiated and IdP-initiated federated identity authentication modes. Users can select a mode supported by the enterprise IdP system.


## Without Federated Identity Authentication<a name="section1938813653310"></a>

-   Enterprise IdP users cannot log in to the cloud system through SSO.

    The enterprise IdP is the IdP system of an enterprise management system. Users authenticated by their enterprise IdP cannot access the cloud system directly.

    **Figure  1**  User authentication model \(1\)<a name="fig39358512151043"></a>  
    ![](figures/user-authentication-model-(1).png "user-authentication-model-(1)")


-   User management is complex.

    The enterprise administrator has to create accounts separately in the enterprise management system and the cloud system.

-   User operations are complex.

    Users have to use different accounts to log in to the enterprise management system and cloud system.

    **Figure  2**  User login model \(1\)<a name="fig10591543151411"></a>  
    ![](figures/user-login-model-(1).png "user-login-model-(1)")


## With Federated Identity Authentication<a name="section1468942416348"></a>

-   IdP users can log in to the cloud system through SSO.

    Any user authenticated by the enterprise IdP can access the cloud system directly. The enterprise administrator does not need to create separate users in the cloud system.

    **Figure  3**  User authentication model \(2\)<a name="fig6128398015113"></a>  
    ![](figures/user-authentication-model-(2).png "user-authentication-model-(2)")


-   User management is more convenient.

    The enterprise administrator does not need to create separate users in the cloud system, reducing the cost of personnel management.

-   User operations are simplified.

    Users can access both the enterprise management system and the cloud system simply by logging in to the enterprise management system.

    **Figure  4**  User login model \(2\)<a name="fig35819891151116"></a>  
    ![](figures/user-login-model-(2).png "user-login-model-(2)")


