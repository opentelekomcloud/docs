# Do I Need to Detach the Disk from Its Server Before Expanding the Disk Capacity?<a name="evs_faq_0028"></a>

An expansion consists of two phases:

1.  Expand the disk capacity on the management console.
    -   A shared, In-use disk cannot be expanded. You must detach the shared disk from all its servers and then expand its capacity.
    -   A non-shared, In-use disk can be expanded, but you can leave the disk attached during expansion only when all the following conditions are met:
        -   The disk's server is in the  **Running**  or  **Stopped**  state.
        -   The disk's server OS supports the expansion of In-use disks.

2.  Log in to the server and allocate the additional space to an existing partition or a new partition.
    -   In Windows: A partition unmount is not required whatever the extension operation is performed.
    -   In Linux:
        -   When allocating the additional space to an existing partition, that is, extending an existing partition, you must use the  **umount**  command to unmount the partition first and then perform subsequent operations.
        -   When allocating the additional space to a new partition, that is, creating a new partition, you do not need to unmount the existing partition.



