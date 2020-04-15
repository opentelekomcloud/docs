# An ECS Fails to Access a File System<a name="sfs_01_0058"></a>

## Symptom<a name="section41158684111639"></a>

An ECS fails to access a file system. The system displays a message indicating that the access request is denied. All services on the ECS are abnormal.

## Possible Causes<a name="section31326994111720"></a>

-   Cause 1: The file system is abnormal.
-   Cause 2: After a forcible unmount operation on the ECS, mount fails.

## Fault Diagnosis<a name="section34776262111735"></a>

Take troubleshooting measures based on possible causes.

## Solution<a name="section28103453161025"></a>

-   Cause 1: The file system is abnormal.

    Log in to the management console. On the  **Scalable File System**  page, check whether the file system is in the  **Available**  state.

    -   If yes, go to Cause 2.
    -   If no, see  [The File System Is Abnormal](the-file-system-is-abnormal.md)  to restore the file system to the available state, and then access the file system again.

-   Cause 2: After a forcible unmount operation on the ECS, mount fails.
    1.  This problem is caused by an inherent defect of ECSs. Restart the ECS to resolve this problem.
    2.  Check whether the file system can be properly mounted and accessed.
        -   If yes, no further action is required.
        -   If no, contact technical support.



