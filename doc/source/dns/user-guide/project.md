# Project<a name="en-us_topic_0070518924"></a>

Projects are used to group and isolate OpenStack resources, including computing, storage, and network resources. Multiple projects can be created for one account. A project can be a department or a project team.

In the DNS service, public zones are global-level resources, and private zones and PTR records are resources at the region level. Therefore, the system will isolate and manage private zones and PTR records based on projects. Before creating, querying, and configuring private zones or PTR records, you need to specify a region and project.

