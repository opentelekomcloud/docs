# Application Scenarios<a name="en-us_topic_0035467693"></a>

-   Public zone

    To enable an Elastic Cloud Server \(ECS\) accessible to Internet users, you must register a domain name with a domain name registrar, configure a public zone in the DNS service, and change the registrar's NS addresses to those provided by the public zone so that the DNS service can resolve the domain name.

    > ![](public_sys-resources/icon-note.gif) **NOTE:** 

    > The ap-sg region does not support public zones.

-   Private zone

    Hosts in all VPC subnets use private network DNS servers provided by the DNS service on the public cloud platform for domain name resolution.


