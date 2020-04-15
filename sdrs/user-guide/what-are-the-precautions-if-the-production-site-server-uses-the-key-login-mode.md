# What Are the Precautions If the Production Site Server Uses the Key Login Mode?<a name="sdrs_faq_0005"></a>

-   If the production site server runs Windows and uses the key login mode, you need to ensure that the key pair of the production site server exists when you create a protected instance or a DR drill. Otherwise, the DR site server or DR drill server may fail to create, causing the protected instance creation or DR drill creation failure.
-   If the production site server runs Linux and uses the key login mode, you can create a protected instance and DR drill no matter whether the key pair of the production site server exists. However, the key pair information will not be displayed on the details page of the created DR site server or DR drill server. You can use the key pair of the production site server to log in to the created DR site server and DR drill server.

