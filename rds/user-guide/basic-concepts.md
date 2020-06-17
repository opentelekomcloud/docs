# **Basic Concepts**<a name="rds_01_0015"></a>

## **DB Instances**<a name="section1319213812395"></a>

An RDS DB instance is the minimum management unit of RDS and represents a relational database that can be run independently. You can use RDS to create and manage DB instances running various DB engines. For details about DB instance types, specifications, engines, versions, and statuses, see  [DB Instance Description](db_instance_description).

## **DB Engines**<a name="section79302616515"></a>

RDS  supports the following DB engines:

-   MySQL
-   PostgreSQL
-   Microsoft SQL Server

For details about the supported versions, see  [DB Engines and Versions](db-engines-and-versions.md).

## **DB Instance Types**<a name="section4661194916550"></a>

RDS DB instances are classified into two types: single and primary/standby. Different series support different DB engines and instance specifications.

For details about the product series, see  [DB Instance Introduction](db-instance-introduction.md)  and  [Function Comparison](function-comparison.md).

## **DB Instance Classes**<a name="section13364710386"></a>

For details about supported DB engines and instance classes, including the number of vCPUs and memory \(GB\), see  [DB Instance Classes](db-instance-classes.md).

## **Automated Backups**<a name="section138061426174214"></a>

When you create a DB instance, an automated backup policy is enabled by default. After the DB instance is created, you can modify the policy. RDS will automatically create full backups for DB instances based on your settings.

## **Manual Backups**<a name="section10188162964311"></a>

Manual backups are user-initiated full backups of DB instances. They are retained until you delete them manually.

## **Regions and AZs**<a name="section877771314110"></a>

A region and availability zone \(AZ\) identify the location of a data center. You can create resources in a specific region and AZ.

-   A region is a physical data center. Each region is completely independent, improving fault tolerance and stability. After a resource is created, its region cannot be changed.
-   An AZ is a physical location using independent power supplies and networks. Faults in an AZ do not affect other AZs. A region can contain multiple AZs, which are physically isolated but interconnected through internal networks. This ensures the independence of AZs and provides low-cost and low-latency network connections.


[Figure 1](#fig2922183194716)  shows the relationship between regions and AZs.

**Figure  1**  Regions and AZs<a name="fig2922183194716"></a>  
![](figures/regions-and-azs.png "regions-and-azs")

## **Projects**<a name="section3455131419443"></a>

Projects are used to group and isolate OpenStack resources \(computing resources, storage resources, and network resources\). A project can be a department or a project team. Multiple projects can be created for one account.

