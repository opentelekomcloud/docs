# DWS Database Concepts<a name="dws_01_0006"></a>

## Database<a name="section4715959816640"></a>

A data warehouse cluster is an analysis-oriented relational database platform that supports online analysis.

## OLAP<a name="section53675525104036"></a>

OLAP is a major function of data warehouse clusters. It supports complex analysis, provides decision-making support tailored to analysis results, and delivers intuitive query results.

## MPP<a name="section2895605910396"></a>

On each node in the data warehouse cluster, memory computing and disk storage systems are independent from each other. With MPP, DWS distributes service data to different nodes based on the database model and application characteristics. Nodes are connected through the network and collaboratively process computing tasks as a cluster and provide database services that meet service needs.

## Shared Nothing Architecture<a name="section3099522411559"></a>

Shared Nothing Architecture is a distributed computing architecture. Each node is independent so that nodes do not compete for resources, which improves work efficiency.

## Database Version<a name="section62224423104913"></a>

Each data warehouse cluster has a specific database version. You can check the version when creating a data warehouse cluster.

## Database Connection<a name="section63032001112247"></a>

You can use a client to connect to a data warehouse cluster on the public cloud and over the Internet.

## Database User<a name="section2400664121910"></a>

You can add and control users who can access the database of a data warehouse cluster by assigning specific permissions to them. The database administrator generated when you create a cluster is the default database user.

