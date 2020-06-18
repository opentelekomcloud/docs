# Creating a BMS Supporting Quick Provisioning<a name="EN-US_TOPIC_0053536894"></a>

## Scenarios<a name="section3085770410423"></a>

When provisioning a common BMS, you need to download its OS from the cloud and install it. The download costs a long time. BMSs using EVS disks as system disks can be provisioned quickly.

BMSs supporting quick provisioning have the following advantages over other BMSs:

-   BMSs booted from EVS disks can be provisioned within about 5 minutes.
-   BMSs support CSBS backups, ensuring data security.
-   BMS rebuilding upon faults is supported, enabling quick service recovery.
-   An Image of a BMS can be exported to apply configurations of the BMS to other BMSs without the need of configuring the BMSs again.

On the page for creating a BMS, select a flavor that supports quick BMS provisioning, set the system disk type and capacity, and configure other required parameters to obtain a BMS.

## Procedure<a name="section3498539110333"></a>

You can create a BMS supporting quick provisioning by following the instructions in  [Creating a BMS](creating-a-bms.md).

When creating the BMS, pay attention to the following parameters:

-   **Flavor**: Select  **physical.h2.large**. For more information about flavors, see  [Instance Family](instance-family.md).
-   **Image**: Select a public image that supports quick provisioning.
-   **Disk**: Set the system disk type and size.

