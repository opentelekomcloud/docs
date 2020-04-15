# What Should I Do If I Cannot Log In to an ECS with Cloud-Init Enabled?<a name="EN-US_TOPIC_0081525054"></a>

## Symptom<a name="section378516093915"></a>

For a key-pair-authenticated ECS, obtaining its login password using a private key file failed.

## Possible Causes<a name="section093552319396"></a>

The password fails to inject using Cloud-Init due to:

-   A network fault, leading to the failure of the connection from the ECS to the Cloud-Init server.
-   No configuration on the image for Cloud-Init to obtain the password.
-   Other reasons.

## Solution<a name="section1868684714415"></a>

If logging in to an ECS with Cloud-Init enabled failed, perform the following operations to locate the fault:

1.  Ensure that Cloud-Init has been correctly configured on the image based on which the ECS was created.

    Cloud-Init has been correctly configured for all public images. Skip this step for public images. Check the Cloud-Init configuration on non-public images.


1.  Ensure that the key pair for logging in to the ECS is correct.
2.  Ensure that DHCP is enabled in the VPC to which the ECS belongs.
3.  Ensure that the ECS has an EIP bound.
4.  View security group rules in the outbound direction and ensure that port 80 is accessible.

