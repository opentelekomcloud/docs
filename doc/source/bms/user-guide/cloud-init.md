# Cloud-Init<a name="EN-US_TOPIC_0083745263"></a>

## What Is Cloud-Init?<a name="section1539283145511"></a>

Cloud-Init is an open-source cloud initialization program, which initializes specified customized configurations, such as the host name, key, and user data, of a newly created BMS.

Currently, all standard images \(in Standard\__xxx_  format\) support Cloud-Init.

Using Cloud-Init to initialize BMS configurations will influence your BMS and IMS services.

## Impact on IMS<a name="section528893335315"></a>

To ensure that BMSs created using private images support customized configurations, you must install Cloud-Init or Cloudbase-Init when creating private images.

-   For Windows OSs, download and install Cloudbase-Init.
-   For Linux OSs, download and install Cloud-Init.

After Cloud-Init or Cloudbase-Init is installed in an image, Cloud-Init or Cloudbase-Init automatically configures initial BMS attributes when the BMS is created. For details about how to install Cloud-Init and Cloudbase-Init, see  _Bare Metal Server Private Image Creation Guide_.

## Impact on BMS<a name="section951214112013"></a>

-   When creating a BMS, if the selected image supports Cloud-Init, you can use user data injection to inject customized configuration, such as BMS login password, for initializing. For details, see  [Injecting User Data into BMSs](injecting-user-data-into-bmss.md).
-   After Cloud-Init is supported, you can view and use the metadata service to configure and manage running BMSs. For more information, see  [Metadata](metadata.md).

## Notes<a name="section14228108367"></a>

-   When using Cloud-Init, enable DHCP in the VPC to which the BMS belongs.
-   When using Cloud-Init, ensure that security group rules in the outbound direction meet the following requirements so that you can access the metadata service:

    -   Protocol: TCP
    -   Port Range: 80
    -   Remote End: 169.254.0.0/16

    >![](/images/icon-note.gif) **NOTE:**   
    >If you use the default security group rules in the outbound direction, the preceding requirements are met, and the metadata service can be accessed. The default outbound security group rule is as follows:  
    >-   Protocol: ANY  
    >-   Port Range: ANY  
    >-   Remote End: 0.0.0.0/16  


