# Functions<a name="dis_01_0003"></a>

DIS manages the infrastructure, storage, networking, and configuration needed to stream your data. You do not have to worry about provisioning, deployment, and constant maintenance of hardware. In addition, DIS synchronously replicates data across availability zones, providing high availability and data durability.

## Key Modules<a name="section43072214172543"></a>

DIS consists of the following four functional modules:

-   Service control
    -   Creates, deletes, and configures DIS streams; synchronizes user information to the data plane.
    -   Allocates resources and automatically deploys DIS on the data plane.

-   Data processing
    -   Receives user requests, and receives and stores authenticated data.
    -   Receives data read requests and returns the requested data to authorized users.
    -   Removes old data from DIS streams according to data aging policies.
    -   Stores user data into OBS.

-   Service maintenance
    -   Installs and upgrades DIS.
    -   Performs configuration, preventive maintenance, monitoring, and log collection and analysis for DIS.
    -   Processes service orders.

-   User SDK
    -   Provides Java APIs for users to push and pull data.
    -   Encrypts data.


## Key Capabilities<a name="section24807479"></a>

-   Scalable: A DIS stream can seamlessly scale its data throughput from megabytes to terabytes per hour, and from thousands to millions of PUT records per second.
-   Easy to use: You can create a DIS stream within seconds. It is easy to put data into a stream, and build a data processing application.
-   Low cost: DIS has no upfront cost and you only pay for the resources you use.
-   Parallel processing: DIS allows you to have multiple DIS applications processing the same stream concurrently. For example, you can have one application running real-time analytics and another sending data to OBS from the same stream.
-   Reliable: DIS preserves data for  _N_  x 24 hours, reducing the probability of data loss in case of application failures, machine failures, or facility failures. The value of  _N_  is an integer from 1 to 7.

