# Is My Data Secure in DWS?<a name="dws_03_0022"></a>

Yes. DWS is aware that data security is one of the biggest issues for customers. In the big data era, data is the core asset of users. To safeguard security of the core asset, the public cloud commits not to touch customers' data, which ensures business success of the public cloud and partners.

DWS engineers enhance the data warehousing system for telecom-class security with years of experience and expertise in the telecommunication industry, especially data security and privacy. Moreover, DWS on the public cloud delivers carrier-class quality, which can satisfy data security and privacy requirements of governments, financial organizations, and carriers. Therefore, DWS is widely used by various industries. DWS on the public cloud wins the following security authentication:

-   ICSL authentication: The authentication is in compliance with cyber security standards issued by UK authorities.
-   PSA authentication issued by Germany privacy and security management authorities: This authentication meets the EU's requirements of data security and privacy.

## Service Data Security<a name="section153899390312"></a>

DWS of the public cloud is built on the infrastructure, such as ECSs and OBS, of the public cloud. 

Service data of DWS users is stored in the ECSs in the cluster. The ECSs are transparent to DWS users and provide the data warehouse access service for users only. Neither users nor public cloud O&M administrators can log in to the ECSs in the cluster.

The OS of ECSs is hardened for security, including kernel hardening, installation of the latest patch, permission control, port management, and protocol and port anti-attack.

DWS provides complete security measures, such as password policies, ID authentication, session management, user rights management, and database audit.

## Snapshot Data Security<a name="section102591944143117"></a>

DWS backups are stored in the snapshot format on the OBS. OBS supports access permission control, key access, and data encryption features. DWS snapshot data can be used for data backup and restoration only and cannot be accessed by any users. DWS administrators can view how much OBS space is occupied by snapshot data through the DWS console and the public cloud bills.

## Network Access Security<a name="section1858424814313"></a>

The network security deployment design of DWS implements 100% isolation between the layer-2 and layer-3 networks, meeting demanding network isolation requirements of government and financial users.

-   DWS is deployed in the tenant-dedicated ECS environment, which is not shared with other tenants. Therefore, data leakage due to computing resource sharing is impossible physically.
-   ECSs in a data warehouse cluster are isolated through VPC, preventing the ECSs from being discovered and intruded by other tenants.
-   The network is divided into the service plane and management plane. The two planes are physically isolated, ensuring security of the networks.
-   The tenants can flexibly customize the security group and set the access rules of the security domain based on their needs.

-   External application software can access DWS using the SSL.
-   Data imported from the OBS can be transmitted in encryption mode.

