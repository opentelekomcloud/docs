# Basic Concepts<a name="EN-US_TOPIC_0125375234"></a>

## Regions and AZs<a name="section64274328153132"></a>

A region is a geographic area where MRS is located.

MRS services in the same region can communicate with each other over an intranet, but those in different regions cannot.

Public cloud data centers are deployed worldwide in places such as North America, Europe, and Asia. MRS is therefore available in different regions. For example, applications can be designed to meet user requirements in specific regions or comply with local laws or regulations.

Each region contains many availability zones \(AZs\) where power and networks are physically isolated. AZs in the same region can communicate with each other over an intranet. Each AZ provides cost-effective and low-latency network connections that are unaffected by faults that may occur in other AZs. Using MRS deployed in an independent AZ protects your applications against failures in a single place.

## Project<a name="section9166165153435"></a>

Projects are used to group and isolate OpenStack resources \(computing resources, storage resources, and network resources\). A project can be a department or a project team. Multiple projects can be created for one tenant account.

A region has multiple projects, but one project is related to one region.

An MRS cluster in a project cannot communicate with an MRS cluster in another project.

