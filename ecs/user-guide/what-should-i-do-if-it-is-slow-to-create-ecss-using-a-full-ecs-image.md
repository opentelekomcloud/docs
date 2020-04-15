# What Should I Do If It Is Slow to Create ECSs Using a Full-ECS Image?<a name="EN-US_TOPIC_0102391480"></a>

## Symptom<a name="section949111527416"></a>

When a full-ECS image created using a CSBS backup was used to create ECSs, the process was time-consuming or the system displayed a message, indicating that this image cannot be used to rapidly create ECSs.

## Cause Analysis<a name="section1463615352495"></a>

The original backup format provided by CSBS cannot be used to rapidly create ECSs. Therefore, if your full-ECS image is in the original backup format, this issue occurs.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   CSBS has provided a new backup format. This issue is resolved if you use a full-ECS image created using a CSBS backup in the new format.  

## Solution<a name="section14961317195115"></a>

If you want to use a full-ECS image to rapidly create ECSs, ensure that the full-ECS image is created using a CSBS backup in the new format. The procedure is as follows:

-   Scenario 1: The ECS based on which the target CSBS backup is created is still available.

    Back up the original ECS on the  **Cloud Server Backup Service**  page and use the new backup to create a full-ECS image. The created full-ECS image can be used to rapidly create ECSs.

    -   For instructions about how to back up an ECS, see  _Cloud Server Backup Service User Guide_.
    -   For instructions about how create a full-ECS image, see  _Image Management Service User Guide_.


-   Scenario 2: The ECS based on which the target CSBS backup is created is unavailable.
    1.  Use the full-ECS image to create a new ECS.
    2.  Back up the ECS.

        For details, see  _Cloud Server Backup Service User Guide_.

    3.  Use the CSBS backup to create a full-ECS image again.

        For details, see  _Image Management Service User Guide_.

        The created full-ECS image can be used to rapidly create ECSs.



