## Cloud-Init

Cloud-Init is an open-source cloud initialization program, which initializes
specified customized configurations, such as the host name, key, and user data,
of a newly created ECS.

All standard (Standard_xxx) and enterprise (Enterprise_xxx) images support
Cloud-Init. Only certain community images (Community_xxx) do not support it.

Using Cloud-Init to initialize ECS configurations will influence your IMS, ECS,
and AS services.

### Impact on IMS

To ensure that ECSs created using private images support customized
configurations, you must install Cloud-Init or Cloudbase-Init before creating
private images.


- For Windows OSs, download and install Cloudbase-Init.

- For Linux OSs, download and install Cloud-init.

After Cloud-Init or Cloudbase-Init is installed in an image, Cloud-Init or
Cloudbase-Init automatically configures initial ECS attributes when the ECS is
created. For instructions about how to install Cloud-Init or Cloudbase-Init, see
***Image Management Service User Guide***.

### Impact on ECS

<ul>
<li>When creating an ECS, if the selected image supports Cloud-Init, you can use user data injection to inject customized configuration, such as ECS login password, for initializing. For details, see section 3.5.1 (Optional) Injecting User Data into ECSs.</li>


<li>After Cloud-Init is supported, ECSs do not support password authentication any more. All newly created ECSs use key pair authentication. This change will influence your ECS logins. For details, see the following sections:
    
<ul>
<li><a href="Logging In to an ECS.md">Logging In to an ECS</a></li>
<li>5.2.2 What Is the cloudbase-init Account in Windows ECSs?</li>
<li>5.4.9 Why Was My Login to a Linux ECS with a Key File Unsuccessful?</li>
<li>5.4.10 Why Does the System Display a Message Indicating that the Password for Logging In to a Windows ECS Cannot Be Queried?</li>
<li>5.4.11 How Do I Log In to an ECS Once All Images Support Cloud-Init?</li></ul>

<li>After Cloud-Init is supported, you can view and use metadata to configure and manage running ECSs. For more information, see section 4.13 Managing ECS Metadata.</li></ul>

### Impact on AS

-   When creating an AS configuration, you can use user data injection to specify ECS configurations for initialization. If the AS configuration has taken effect in an AS group, the ECSs newly created in the AS group will automatically initialize their configurations.

-   For an existing AS configuration, if its private image has Cloud-Init or Cloudbase-Init not installed, the login mode of the ECSs created in the AS group where the AS configuration takes effect will be influenced. To resolve this issue, see section "How Does Cloud-Init Influence the AS Service?" in ***Auto Scaling User Guide***.

For more information about AS, see ***Auto Scaling User Guide***.
