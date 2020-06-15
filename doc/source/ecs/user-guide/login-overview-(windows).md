# Login Overview<a name="EN-US_TOPIC_0092494943"></a>

## Constraints<a name="section109631817183419"></a>

-   Only a running ECS can be logged in.
-   If an ECS uses key pair authentication, use the password obtaining function provided by the management console to decrypt the private key used during ECS creation to obtain a password.
-   For ECSs created using public images, login usernames, passwords, and constraints vary depending on OSs running on the ECSs. For details, see  _[Public Images Introduction](https://docs.otc.t-systems.com/en-us/ims/index.html)_.
-   G6 ECSs do not support remote login provided by the public cloud platform. Before logging in to such an ECS using VNC, install the VNC server \(obtained by yourself\) during image creation. Otherwise, the login using VNC will fail.

    You can log in to such an ECS using MSTSC. For details, see  [Login Using MSTSC](login-using-mstsc.md).

-   G2 ECSs do not support remote login provided by the public cloud platform. Before logging in to such an ECS using VNC, install the VNC server \(obtained by yourself\) during image creation. Otherwise, the login using VNC will fail.

    You can log in to such an ECS using MSTSC. For details, see  [Login Using MSTSC](login-using-mstsc.md).

-   Logins using MSTSC can only be used on Windows ECSs.
-   An ECS must have an EIP bound for logins using MSTSC.
-   If you log in to a GPU-accelerated ECS using MSTSC, GPU acceleration will fail. This is because MSTSC replaces the WDDM GPU driver with a non-accelerated remote desktop display driver. In such an event, you must use other methods to log in to the ECS, such as VNC. If the remote login function available on the management console fails to meet your service requirements, you must install a suitable remote login tool on the ECS, such as TightVNC.

    To download TightVNC, log in at  [https://www.tightvnc.com/download.php](https://www.tightvnc.com/download.php).


## Login Modes<a name="section361333632514"></a>

Only a running ECS can be logged in.

A Windows ECS can be logged in using either VNC or MSTSC.

-   Login using VNC

    If no EIP is bound to an ECS, you can remotely log in to the ECS on the management console.

    For details, see  [Login Using VNC](login-using-vnc-(windows).md).

-   Login using MSTSC

    This function applies only to Windows ECSs with an EIP bound.

    For details, see  [Login Using MSTSC](login-using-mstsc.md).


