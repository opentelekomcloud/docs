# Supported Services<a name="en-us_topic_0100236044"></a>

Once you enable CTS, the system automatically identifies cloud services enabled on the current cloud platform, captures key operations on the services, and reports traces of these operations to CTS.

The key operations performed by invoking IaaS OpenStack APIs are shown in  [Relationship Between Operations Triggered by IaaS OpenStack and Native OpenStack APIs](relationship-between-operations-triggered-by-iaas-openstack-and-native-openstack-apis.md).

Traces of global-level cloud services are only recorded at the central region of the current site. Multi-project scenarios are not supported.

The key operations of global-level services supported by CTS are as follows:

-   [Global-level Key Operations on DNS](global-level-key-operations-on-dns.md)
-   [Key Operations on MaaS](key-operations-on-maas.md)
-   [Key Operations on CDN](key-operations-on-cdn.md)
-   [Key Operations on IAM](key-operations-on-iam.md)
-   [Key Operations on TMS](key-operations-on-tms.md)

Traces of region-level cloud services are recorded in the target region or project to which the operated resources belong.

For key operations of region-level services supported by CTS, see  [Supported Services and Operation Lists](supported_services_and_operation_lists).

