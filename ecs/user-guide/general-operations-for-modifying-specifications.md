# General Operations for Modifying Specifications<a name="EN-US_TOPIC_0013771092"></a>

## Scenarios<a name="en-us_topic_0013859511_section14602858172718"></a>

If the ECS specifications do not meet service requirements, you can modify the ECS specifications, including vCPUs and memory. Certain ECSs allow you to change their types when you modify their specifications.

Specifications can be modified between general-purpose \(S1, C1, C2, or M1\) and H1 ECSs, from Xen to KVM ECSs, and between KVM ECSs.

-   If you want to change a general-purpose ECS to an H1 ECS, manually configure the source ECS, install the required driver on it, and modify the specifications. For details, see  [Changing a General-Purpose ECS to an H1 ECS](changing-a-general-purpose-ecs-to-an-h1-ecs.md).
-   If you want to change an H1 ECS to a general-purpose ECS, perform the operations provided in this section.
-   Before changing a Xen ECS to a KVM ECS, manually install the required driver on the ECS. Otherwise, the ECS will be unavailable after the modification is performed. For example, starting the OS will fail. The process of changing a Xen ECS to a KVM ECS is as follows:
    -   [Changing a Xen ECS to a KVM ECS \(Windows\)](changing-a-xen-ecs-to-a-kvm-ecs-(windows).md)
    -   [Automatically Changing a Xen ECS to a KVM ECS \(Linux\)](automatically-changing-a-xen-ecs-to-a-kvm-ecs-(linux).md)
    -   [Manually Changing a Xen ECS to a KVM ECS \(Linux\)](manually-changing-a-xen-ecs-to-a-kvm-ecs-(linux).md)

-   For instructions about how to modify the specifications of other ECSs, for example, between KVM ECSs, see this section.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   Xen ECSs include S1, C1, C2, and M1 ECSs.  
>-   To obtain KVM ECSs, see the  **Virtualization Type**  column in  [ECS Specifications](ecs-specifications.md).  
>-   Before changing a Xen ECS to a KVM ECS, install the desired driver on the ECS. Otherwise, the ECS will be unavailable after the modification is performed. For example, starting the OS will fail.  

## Background<a name="section15710213610"></a>

To obtain the virtualization type of an ECS, perform the following operations:

1.  On the page providing details about the ECS, view the ECS specifications.

    **Figure  1**  Viewing ECS specifications<a name="fig14561414141716"></a>  
    ![](figures/viewing-ecs-specifications.png "viewing-ecs-specifications")

2.  Check the specifications tables in  [ECS Types](ecs-types.md)  for the virtualization type.

## Notes<a name="en-us_topic_0013859511_section57753505172833"></a>

-   If ECS specifications are downgraded, the ECS performance is deteriorated.
-   Certain ECSs do not support specifications modification currently. For details about available ECS types as well as their functions and usage, see "Notes" in  [ECS Types](ecs-types.md).
-   When the disk status is  **Expanding**, you are not allowed to modify the specifications of the ECS where the disk is attached.
-   Before modifying the specifications of a Windows ECS, modify the SAN policy by following the instructions provided in  [What Should I Do If a Disk Is Offline?](what-should-i-do-if-a-disk-is-offline.md)  to prevent offline disks after the specifications are modified.
-   Before modifying specifications, make sure that the ECS has been stopped.

## Step 1: Modify Specifications<a name="section997143905215"></a>

The following section provides general operations for modifying specifications. For instructions about how to change a general-purpose ECS to an H1 ECS, see  [Changing a General-Purpose ECS to an H1 ECS](changing-a-general-purpose-ecs-to-an-h1-ecs.md). For instructions about how to change a Xen ECS to a KVM ECS, see the following operations.

-   [Changing a Xen ECS to a KVM ECS \(Windows\)](changing-a-xen-ecs-to-a-kvm-ecs-(windows).md)
-   [Automatically Changing a Xen ECS to a KVM ECS \(Linux\)](automatically-changing-a-xen-ecs-to-a-kvm-ecs-(linux).md)
-   [Manually Changing a Xen ECS to a KVM ECS \(Linux\)](manually-changing-a-xen-ecs-to-a-kvm-ecs-(linux).md)

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  On the  **Elastic Cloud Server**  page, view the status of the target ECS.

    If the ECS is not in  **Stopped**  state, click  **More**  in the  **Operation**  column and select  **Stop**.

5.  Click  **More**  in the  **Operation**  column and select  **Modify Specifications**.

    The  **Modify ECS Specifications**  page is displayed.

6.  Select the new ECS type, vCPUs, and memory as prompted.
7.  \(Optional\) Set  **DeH**.

    If the ECS is created on a DeH, the system allows you to change the DeH.

    To do so, select the target DeH from the drop-down list. If no DeH is available in the drop-down list, remaining DeH resources are insufficient and cannot be used to create the ECS with specifications modified.

8.  \(Optional\) Select the check box to confirm the ECS configuration.
    -   If a general-purpose ECS is changed to an H1 ECS, manually configure the ECS by following the instructions provided in  [Changing a General-Purpose ECS to an H1 ECS](changing-a-general-purpose-ecs-to-an-h1-ecs.md). After the configuration, select the check box and confirm the operation.
    -   If a Xen ECS is changed to a KVM ECS, configure the ECS by following the instructions provided in  [Changing a Xen ECS to a KVM ECS \(Windows\)](changing-a-xen-ecs-to-a-kvm-ecs-(windows).md),  [Automatically Changing a Xen ECS to a KVM ECS \(Linux\)](automatically-changing-a-xen-ecs-to-a-kvm-ecs-(linux).md), or  [Manually Changing a Xen ECS to a KVM ECS \(Linux\)](manually-changing-a-xen-ecs-to-a-kvm-ecs-(linux).md). After the configuration, select the check box and confirm the operation.

9.  Click  **OK**.
10. On the  **Modify ECS Specifications**  page, confirm the modified vCPU and memory specifications and click  **Submit**.
11. Check whether the specifications have been modified.

    After modifying the specifications, you can check whether the specifications have been modified in  **Failures**.

    1.  Check whether  **Failures**  is displayed on the management console. For details, see  [Viewing Failures](viewing-failures.md).
        -   If yes, go to step  [11.b](#li6253192246).
        -   If no, the specifications have been modified.

    2.  <a name="li6253192246"></a>Click  **Failures**. Then, in the  **Failures**  dialog box, click  **Operation Failures**  and check whether the task is contained in the list by  **Name/ID**,  **Operated At**, or  **Task**.
        -   If yes, the specifications modification failed. See  [Follow-up Procedure](#section9461027528)  for failure causes.
        -   If no, the specifications have been modified.



## Step 2: Check Disk Attachment<a name="section88041642132813"></a>

After specifications are modified, disk attachment may fail. Therefore, check disk attachment after specifications modification. If disks are properly attached, the specifications modification is successful.

-   Windows

    For details, see  [What Should I Do If the Data Disk of a Windows ECS Becomes Offline After the ECS Specifications Are Modified?](what-should-i-do-if-the-data-disk-of-a-windows-ecs-becomes-offline-after-the-ecs-specifications-are.md)

-   Linux

    For details, see  [What Should I Do If the Disk of a Linux ECS Becomes Offline After the ECS Specifications Are Modified?](what-should-i-do-if-the-disk-of-a-linux-ecs-becomes-offline-after-the-ecs-specifications-are-modifie.md)


## Follow-up Procedure<a name="section9461027528"></a>

Perform the following operations in the event of a specifications modification failure:

1.  Log in to the management console.
2.  Under  **Management & Deployment**, click  **Cloud Trace Service**.
3.  In the navigation pane on the left, choose  **Trace List**.
4.  In the  **Trace Name**  column, locate the  **resizeServer**  event by resource ID.

    The resource ID is the ID of the ECS on which the specifications modification failed.

5.  Click  **View Trace**  in the  **Operation**  column to view the failure cause.

    If the fault cannot be rectified based on logs, contact technical support.


