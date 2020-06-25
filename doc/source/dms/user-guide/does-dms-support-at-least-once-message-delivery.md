# Does DMS Support "At Least Once" Message Delivery?<a name="EN-US_TOPIC_0144327159"></a>

Yes. DMS stores message copies in multiple servers to achieve message backup and high availability. In rare cases, a server storing message replicas may be unavailable when you request or delete messages. If this happens, the message replicas will not be deleted from that server and may be sent when the connection is restored. This process is called "at-least-once" delivery. To avoid any adverse impact from processing the same message multiple times, ensure that your application processes messages idempotently.

