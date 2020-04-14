# User Guide

-   [Service Overview]
    -   [What Is AS?](what-is-as.md)
    -   [AS Advantages](as-advantages.md)
    -   [Lifecycle](lifecycle.md)
    -   [Use Restrictions](use-restrictions.md)
    -   [AS and Other Services](as-and-other-services.md)
    -   [User Permissions](user-permissions.md)
    -   [Basic Concepts](basic-concepts.md)

-   [Best Practices]
    -   [Setting Up an Automatically Scalable Discuz! Forum Website](setting-up-an-automatically-scalable-discuz-forum-website.md)

-   [Quick Start]
    -   [Wizard-based Process of Using AS](wizard-based-process-of-using-as.md)
    -   [Creating an AS Group Quickly](creating-an-as-group-quickly.md)

-   [AS Management]
    -   [AS Group]
        -   [Creating an AS Group](creating-an-as-group.md)
        -   [\(Optional\) Adding a Load Balancer to an AS Group]((optional)-adding-a-load-balancer-to-an-as-group.md)
        -   [Replacing AS Configuration in an AS Group](replacing-as-configuration-in-an-as-group.md)
        -   [Enabling an AS Group](enabling-an-as-group.md)
        -   [Disabling an AS Group](disabling-an-as-group.md)
        -   [Modifying an AS Group](modifying-an-as-group.md)
        -   [Deleting an AS Group](deleting-an-as-group.md)

    -   [AS Configuration]
        -   [Creating an AS Configuration](creating-an-as-configuration.md)
        -   [Using an Existing ECS to Create an AS Configuration](using-an-existing-ecs-to-create-an-as-configuration.md)
        -   [Using a New Specifications Template to Create an AS Configuration](using-a-new-specifications-template-to-create-an-as-configuration.md)
        -   [Copying an AS Configuration](copying-an-as-configuration.md)
        -   [Deleting an AS Configuration](deleting-an-as-configuration.md)

    -   [AS Policy]
        -   [Overview](overview.md)
        -   [Creating an AS Policy](creating-an-as-policy.md)
        -   [Managing AS Policies](managing-as-policies.md)

    -   [Scaling Action]
        -   [Dynamically Expanding Resources](dynamically-expanding-resources.md)
        -   [Expanding Resources as Planned](expanding-resources-as-planned.md)
        -   [Manually Expanding Resources](manually-expanding-resources.md)
        -   [Configuring an Instance Removal Policy](configuring-an-instance-removal-policy.md)
        -   [Viewing a Scaling Action](viewing-a-scaling-action.md)
        -   [Configuring Instance Protection](configuring-instance-protection.md)

    -   [Bandwidth Scaling]
        -   [Creating a Bandwidth Scaling Policy](creating-a-bandwidth-scaling-policy.md)
        -   [Viewing Details About a Bandwidth Scaling Policy](viewing-details-about-a-bandwidth-scaling-policy.md)
        -   [Managing a Bandwidth Scaling Policy](managing-a-bandwidth-scaling-policy.md)

    -   [AS Group and Instance Monitoring]
        -   [Health Check](health-check.md)
        -   [Recording AS Resource Operations](recording-as-resource-operations.md)
        -   [Marking AS Groups and Instances](marking-as-groups-and-instances.md)
        -   [Monitoring Metrics](monitoring-metrics.md)
        -   [Viewing Monitoring Metrics](viewing-monitoring-metrics.md)
        -   [Setting Monitoring Alarm Rules](setting-monitoring-alarm-rules.md)


-   [FAQs]
    -   [General]
        -   [What Are Restrictions on Using AS?](what-are-restrictions-on-using-as.md)
        -   [Are ELB and Cloud Eye Mandatory for AS?](are-elb-and-cloud-eye-mandatory-for-as.md)
        -   [Does an Abrupt Change on Monitoring Indicator Values Cause an Incorrect Scaling Action?](does-an-abrupt-change-on-monitoring-indicator-values-cause-an-incorrect-scaling-action.md)
        -   [How Many AS Policies and AS Configurations Can I Create and Use?](how-many-as-policies-and-as-configurations-can-i-create-and-use.md)
        -   [Can AS Automatically Scale Up or Down vCPUs, Memory, and Bandwidth of ECSs?](can-as-automatically-scale-up-or-down-vcpus-memory-and-bandwidth-of-ecss.md)
        -   [What Is the AS Quota?](what-is-the-as-quota.md)
        -   [Why is a message displayed indicating that the key pair does not exist and the operation is discontinued when several users under the same account operate AS resources?](why-is-a-message-displayed-indicating-that-the-key-pair-does-not-exist-and-the-operation-is-disconti.md)

    -   [AS Group]
        -   [Why Does Not the ELB Health Check Used by an AS Group Take Effect Immediately?](why-does-not-the-elb-health-check-used-by-an-as-group-take-effect-immediately.md)
        -   [What Can I Do If the AS Group Fails to Be Enabled?](what-can-i-do-if-the-as-group-fails-to-be-enabled.md)
        -   [How Can I Handle an AS Group Exception?](how-can-i-handle-an-as-group-exception.md)
        -   [What Is Health Check Grace Period?](what-is-health-check-grace-period.md)
        -   [What Operation Will Be Suspended After An AS Group Is Disabled?](what-operation-will-be-suspended-after-an-as-group-is-disabled.md)

    -   [AS Policy]
        -   [How Many AS Policies Can Be Enabled?](how-many-as-policies-can-be-enabled.md)
        -   [What Are the Conditions to Trigger an Alarm in the AS Policy?](what-are-the-conditions-to-trigger-an-alarm-in-the-as-policy.md)
        -   [What Is a Cooldown Period? Why Is It Required?](what-is-a-cooldown-period-why-is-it-required.md)
        -   [What Will Monitoring Metrics for an AS Group Be Affected If OTC tools Are Not Installed on ECSs?](what-will-monitoring-metrics-for-an-as-group-be-affected-if-otc-tools-are-not-installed-on-ecss.md)
        -   [What Can I Do If an AS Policy Fails to Be Enabled?](what-can-i-do-if-an-as-policy-fails-to-be-enabled.md)

    -   [Instance]
        -   [How Do I Prevent Instances Manually Added to an AS Group from Being Removed Automatically?](how-do-i-prevent-instances-manually-added-to-an-as-group-from-being-removed-automatically.md)
        -   [Will the Application Data on an Instance Be Retained After the Instance Is Removed from an AS Group and Deleted?](will-the-application-data-on-an-instance-be-retained-after-the-instance-is-removed-from-an-as-group.md)
        -   [Can Instances That Have Been Added Based on an AS Policy Be Automatically Deleted When They Are Not Required?](can-instances-that-have-been-added-based-on-an-as-policy-be-automatically-deleted-when-they-are-not.md)
        -   [What Is the Expected Number of Instances?](what-is-the-expected-number-of-instances.md)
        -   [How Do I Delete an ECS Created During a Scaling Action?](how-do-i-delete-an-ecs-created-during-a-scaling-action.md)
        -   [How Should I Handle Abnormal Instances in an AS Group?](how-should-i-handle-abnormal-instances-in-an-as-group.md)
        -   [What Can I Do If Instances in an AS Group Frequently Fail in Health Checks and Are Deleted and Then Created Repeatedly?](what-can-i-do-if-instances-in-an-as-group-frequently-fail-in-health-checks-and-are-deleted-and-then.md)
        -   [How Do I Prevent ECSs from Being Removed from an AS Group Automatically?](how-do-i-prevent-ecss-from-being-removed-from-an-as-group-automatically.md)
        -   [Why Is an Instance Removed and Deleted from an AS Group Still Displayed in the ECS List?](why-is-an-instance-removed-and-deleted-from-an-as-group-still-displayed-in-the-ecs-list.md)

    -   [Others]
        -   [What Can I Do to Enable My Application to Be Automatically Deployed on an Instance?](what-can-i-do-to-enable-my-application-to-be-automatically-deployed-on-an-instance.md)
        -   [How Can I Run Existing Services on an Instance Newly Added to an AS Group?](how-can-i-run-existing-services-on-an-instance-newly-added-to-an-as-group.md)
        -   [Why Cannot I Use a Key File to Log In to an ECS?](why-cannot-i-use-a-key-file-to-log-in-to-an-ecs.md)
        -   [Do I Need to Configure an EIP in an AS Configuration When A Load Balancer Has Been Enabled in an AS Group?](do-i-need-to-configure-an-eip-in-an-as-configuration-when-a-load-balancer-has-been-enabled-in-an-as.md)
        -   [How Can I Enable Automatic Initialization of EVS Disks of Instances That Have Been Added in a Scaling Action to an AS Group?](how-can-i-enable-automatic-initialization-of-evs-disks-of-instances-that-have-been-added-in-a-scalin.md)


-  
