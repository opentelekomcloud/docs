# DNS<a name="en-us_topic_0035467691"></a>

Domain Name Service \(DNS\) provides highly available and scalable authoritative DNS services and domain name management services. It translates domain names or application resources into IP addresses required for network connection. By doing so, visitors' access requests are directed to the desired resources.

## Function<a name="section10420986221359"></a>

The DNS service provides the following functions:

-   Private zone
    -   Enables you to flexibly customize private domain names in your VPCs.
    -   Allows one private zone to be associated with multiple VPCs for unified management.
    -   Provides private DNS servers to quickly respond to requests for accessing ECSs in VPCs as well as OBS and RDS resources, preventing DNS spoofing.
-   Record management
    -   Provides stable, secure, and quick domain name resolution capabilities.
    -   Supports commonly used record types, such as A, AAAA, MX, CNAME, TXT, and NS.
    -   Supports reverse resolution, DKIM, and wildcard records.

## Application Scenarios<a name="section45534066221631"></a>

-   General DNS resolution
-   Online and offline service management
-   Multi-application deployment

