# Public Zone<a name="en-us_topic_0035855360"></a>

There are a large number of DNS servers on the Internet, constituting DNS domain namespaces. Each DNS server has its own domain name resolution responsibilities. Only when a DNS server cannot resolve a domain name itself, it forwards the request to another DNS server. Domain namespaces are managed by segment. That is, a large space is divided into several separately hosted zones.

Each public zone is a part of the namespace that is administered by a particular DNS server. For example, a DNS server is configured on the cloud platform to resolve all domain names in the namespace **example.com**.

Public zones are accessible to hosts on the Internet.

