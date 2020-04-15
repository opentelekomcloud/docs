# Managing EVS Disk Transfer<a name="evs_01_0042"></a>

## Scenarios<a name="section2078706916510"></a>

Through the EVS disk transfer function, EVS disks can be transferred from one tenant to another. After the transfer succeeds, the ownerships of the EVS disks belong to the target tenant only. Currently, only data disks can be transferred.

Currently, users can use the disk transfer function by making API calls only. For details, see chapter  **EVS Disk Transfer**  in the  _Elastic Volume Service API Reference_.

## Constraints<a name="section3505785917301"></a>

-   Encrypted EVS disks cannot be transferred.
-   EVS disks with backups and snapshots available cannot be transferred.
-   EVS disks associated with backup policies cannot be transferred.
-   EVS disks used as system disks cannot be transferred.
-   EVS disks in EVS replication pairs cannot be transferred.

## Procedure<a name="section4128178173158"></a>

The following example shows you how to transfer an EVS disk from tenant A to tenant B. User A belongs to tenant A, and user B belongs to tenant B. User A creates the transfer. User B accepts the transfer through the transfer ID \(transfer\_id\) and authentication key \(auth\_key\). After the transfer has been accepted, the transfer is complete.  [Figure 1](#fig327011712137)  shows the basic transfer process.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   transfer\_id specifies the disk transfer ID. Each EVS disk transfer has a transfer ID, and user B uses this ID to accept the disk transfer.  
>-   auth\_key specifies the identity authentication key of the disk transfer. Each EVS disk transfer has an authentication key, and user B uses this key for authentication when accepting the disk transfer.  

**Figure  1**  Operation procedure \(EVS disk transfer\)<a name="fig327011712137"></a>  
![](figures/operation-procedure-(evs-disk-transfer).png "operation-procedure-(evs-disk-transfer)")

1.  User A creates the transfer. For details, see  **Creating an EVS Disk Transfer**  in the  _Elastic Volume Service API Reference_.

    After the transfer is successfully created,  **transfer\_id**  and  **auth\_key**  are returned.

2.  \(Optional\) User A can view the disk transfer. For details, see  **Querying Details of an EVS Disk Transfer**  in the  _Elastic Volume Service API Reference_. If multiple disk transfers have been created, user A can also query all disk transfers. For details, see  **Querying All EVS Disk Transfers**  or  **Querying Details of All EVS Disk Transfers**  in the  _Elastic Volume Service API Reference_.
3.  User A delivers the returned  **transfer\_id**  and  **auth\_key**  to user B.
4.  Check whether user B is going to accept the disk transfer.
    -   If yes, go to  [5](#li61046537173317).
    -   If no, no further action is required.

        User A can delete the unaccepted disk transfer. For details, see  **Deleting an EVS Disk Transfer**  in the  **Elastic Volume Service API Reference**.

5.  <a name="li61046537173317"></a>User B accepts  **transfer\_id**  and  **auth\_key**.
6.  User B accepts the transfer through  **transfer\_id**  and  **auth\_key**. For details, see  **Accepting an EVS Disk Transfer**  in the  _Elastic Volume Service API Reference_.

