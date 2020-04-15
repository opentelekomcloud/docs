# Login Overview<a name="EN-US_TOPIC_0013771089"></a>

## Constraints<a name="section15584113212291"></a>

-   For ECSs created using public images, login usernames, passwords, and constraints vary depending on OSs running on the ECSs. For details, see  _[Public Images Introduction](https://docs.otc.t-systems.com/en-us/ims/index.html)_.
-   An ECS must have an EIP bound for logins using SSH.

## Login Modes<a name="section206683732817"></a>

Only a running ECS can be logged in.

A Linux ECS can be logged in using either VNC or SSH.

-   Management console \(VNC\)

    If no EIP is bound to an ECS, you can remotely log in to the ECS on the management console.

    For details, see  [Login Using VNC](login-using-vnc-(linux).md).

-   SSH

    This method applies only to Linux ECSs. You can use a remote login tool, such as PuTTY, to log in to your ECS. Ensure that the ECS has an EIP bound.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Both an SSH key and an SSH password can be used for logins.  

    For details, see:

    [Login Using an SSH Key](login-using-an-ssh-key.md)

    [Login Using an SSH Password](login-using-an-ssh-password.md)


