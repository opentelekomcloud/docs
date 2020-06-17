# What Are the Restrictions for Attaching a Disk to a BMS?<a name="EN-US_TOPIC_0102462512"></a>

-   The disk and the target BMS must be located in the same AZ.
-   The target BMS must be in  **Running**  or  **Stopped**  state.
-   **Device Type**  of the EVS disk must be set to  **SCSI**.
-   A non-shared EVS disk must be in  **Available**  state.

    A shared EVS disk must be in  **in use**  or  **Available**  state.

-   BMSs using some flavors or images cannot have EVS disks attached because the servers do not have SDI iNICs or for other reasons.

