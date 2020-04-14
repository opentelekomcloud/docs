# How Do I Prevent Instances Manually Added to an AS Group from Being Removed Automatically?<a name="EN-US_TOPIC_0165071401"></a>

If you have manually added N instances into an AS group and do not want these instances to be removed automatically, you can use either of the following methods to ensure this:

## Method 1<a name="section366321514332"></a>

Perform following configurations in the AS group:

-   Set the minimum number of instances in the AS group to N or greater than N.
-   Set  **Instance Removal Policy**  to  **Oldest instance created from oldest AS configuration**  or  **Newest instance created from oldest AS configuration**.

Based on the scaling rules, the manually added instances do not correspond to any AS configuration \(because they are not created using the AS configuration\). Therefore, the instances automatically created using the AS configuration are removed at first. Only when such instances are removed, the instances manually added are removed. Since you have set the minimum number of instances to N or greater than N, the instances manually added are not selected.

Note: If the instances manually added are stopped or they malfunction, they are regarded as unhealthy and removed from the AS group. This is because health check ensures that instances in the AS group must be healthy.

## Method 2<a name="section11231148173413"></a>

Enable instance protection for the N instances. For details, see  [Configuring Instance Protection](configuring-instance-protection.md).

You can enable instance protection for the N instances at the same time. When an AS group reduces the capacity, protected instances will not be removed from the AS group. Note: Instances that fail to pass a health check will still be removed from the AS group.

