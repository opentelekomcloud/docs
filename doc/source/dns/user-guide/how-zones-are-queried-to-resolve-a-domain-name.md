# How Zones Are Queried to Resolve a Domain Name?<a name="dns_faq_011"></a>

When a domain name resolution request is initiated, the domain name is first queried in the zone of a subdomain if there is any.

-   If the zone has been created, the system returns the result from the zone configuration file.
-   Otherwise, the system queries the domain name from the zone configuration file of a higher-level domain name.

For example:

For example, you have created a zone for **example.com** and add an A record set for **www.example.com**, and also, you have created a zone for **www.example.com** and have not added an A record set for it.

In this case, if a visitor tries to access **www.example.com**, it is first queried in the configuration file of the **www.example.com** zone. However, because you have not added an A record set in the zone, no result will be returned.

