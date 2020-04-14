# How Can I Handle an AS Group Exception?<a name="EN-US_TOPIC_0042018408"></a>

The handling method varies depending on the possible cause.

-   Issue description: Insufficient quota for ECSs, EVS disks, or EIPs.

    Possible cause: insufficient quota

    Handling method: Increase the quota or delete unnecessary resources, and then enable the AS group.

-   Issue description: The VPC or subnet does not exist.

    Possible cause: The VPC service encounters an exception or resources have been deleted.

    Handling method: Wait until the VPC service recovers, or modify parameters of the VPC and subnet in the AS group, and then enable the AS group.

-   Issue description: The ELB listener or backend ECS group does not exist, and the load balancer is unavailable.

    Possible cause: The ELB service encounters an exception or resources have been deleted.

    Handling method: Wait until the ELB service recovers, or modify load balance parameters in the AS group, and then enable the AS group.

-   Issue description: The number of backend ECSs that you add to the ELB listener exceeds the upper limit.

    Possible cause: If classical load balancer is used by an AS group, instances added to the AS group are automatically added to the ELB listener. A maximum of 300 backend ECSs can be added to an ELB listener.

    Handling method: Remove the backend ECSs that are both not required and not in the AS group from the listener. Then enable the AS group.

-   Issue description: The image used by the AS configuration, the flavor, or the key pair does not exist.

    Possible cause: Resources have been deleted.

    Handling method: Change the AS configuration for the AS group and then enable the AS group.

-   Issue description: The subnet you select does not have enough private IP addresses.

    Possible cause: Private IP addresses in the subnet used by the AS group have been used up.

    Handling method: Modify the subnet information and enable the AS group.

-   Issue description: The ECS resources of this type in the selected AZ have been sold out.

    Possible cause: ECSs of this type have been sold out or are not supported in the AZ selected for the AS group. ECSs of this type are the ECS flavor selected in the AS configuration.

    Handling method: Change the AS configuration for the AS group and then enable the AS group. If there is no instance in the AS group, you can also change the AZ for the AS group and then enable the AS group.

-   Issue description: The selected specifications and the disk do not match.

    Possible cause: The ECS type in the AS configuration does not match the disk type, leading to the ECS creation failure.

    Handling method: Change the AS configuration for the AS group and then enable the AS group.

-   Issue description: The selected specifications and the image do not match.

    Possible cause: The ECS type in the AS configuration does not match the disk type, leading to the ECS creation failure.

    Handling method: Change the AS configuration for the AS group and then enable the AS group.

-   Issue description: Storage resources of this type have been sold out in the selected AZ.

    Possible cause: Storage resources of this type have been sold out or are not supported in the AZ selected for the AS group. Storage resources of this type refer to the system and data disk types selected for the AS configuration.

    Handling method: Change the AS configuration for the AS group and then enable the AS group. If there is no instance in the AS group, you can also change the AZ for the AS group and then enable the AS group.

-   Issue description: A system error has occurred.

    Possible cause: An error has occurred in the AS service, peripheral service, or network.

    Handling method: Try again later or contact technical support.

-   Issue description: The specification defined in the AS configuration is unavailable.

    Handling method: Change specifications by creating an AS configuration as prompted by the error message and use this AS configuration for the AS group. Then enable the AS group.

-   Issue description: The selected AS configuration cannot be used by the AS group.

    Handling method: Create an AS configuration as prompted by the error message and use this AS configuration for the AS group. Then enable the AS group.


