# Manually Expanding Resources<a name="EN-US_TOPIC_0042018379"></a>

## Scenarios<a name="section2495449014355"></a>

Expand resources by manually adding instances to an AS group, removing instances from an AS group, or changing the expected number of instances.

## Procedure<a name="section53233117153934"></a>

**Adding instances to an AS group**

If an AS group is enabled and has no ongoing scaling action, and the current number of instances is less than the maximum, you can manually add instances to the AS group.

Before adding instances to an AS group, ensure that the following conditions are met:

-   The instances are not in other AS groups.
-   The instances must be in the same VPC as the AS group.
-   The AZ to which the instances belong must be within the AZ to which the AS group belongs.
-   After instances are added, the total number of instances is less than or equal to the maximum number of instances allowed.
-   A batch operation can be performed on a maximum of 10 instances at a time.

To add instances to an AS group, perform the following steps:

1.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**.
2.  Click the AS group name on the  **AS Groups**  tab.
3.  On the  **Instances**  tab, click  **Add**.
4.  Select the instances to be added and click  **OK**.

**Removing instances from an AS group**

You can remove an instance from an AS group, update the instance or rectify the instance fault, and add the instance to the AS group again. The instance removed out of the AS group does not carry application traffic any more.

For example, you can modify the AS configuration for an AS group at any time. However, the AS group does not allow the update of an instance that is running. In such an event, terminate the instance and replace it in the AS group. Alternatively, remove the instance out of the AS group, update the instance software, and add the instance to the AS group again.

Restrictions on instance removal are as follows:

-   The AS group does not have a scaling action that is being performed, the instances are enabled, and the total number of instances after removal is not less than the minimum number of instances allowed.
-   Instances can be removed from an AS group and deleted only if the AS group has no scaling action ongoing, and the instances are automatically created and enabled, and are not used in Storage Disaster Recovery Service \(SDRS\).
-   Instances manually added to an AS group can only be removed, and cannot be removed and deleted.
-   A batch operation can be performed on a maximum of 10 instances at a time.

To remove an instance from an AS group, perform the following steps:

1.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**.
2.  Click the AS group name on the  **AS Groups**  tab.
3.  On the  **Instances**  tab, locate the row containing the target instance and click  **Remove**  or  **Remove and Delete**  in the  **Operation**  column.
4.  To delete multiple instances from an AS group, select the check boxes in front of them and click  **Remove**  or  **Remove and Delete**.

To delete all instances from an AS group, select the check box on the left of  **Instance Name**  and click  **Remove**  or  **Remove and Delete**.

**Changing the expected number of instances**

Manually change the expected number of instances to add or reduce the number of instances in an AS group for expanding resources.

For details, see section  [Modifying an AS Group](modifying-an-as-group.md).

