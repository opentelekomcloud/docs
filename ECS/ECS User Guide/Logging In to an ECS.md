Logging In to an ECS
--------------------

1.  Overview

You can only log in to a running ECS. Login methods include using VNC, SSH
(Linux), and MSTSC (Windows).

For ECSs created using public images, login username, password, as well as
restrictions and limitations vary depending on OSs running on the ECSs. For
details, see [Public Images
Introduction](https://docs.otc.t-systems.com/ims_dld/index.html).

-   Logging in to an ECS using VNC

You can use the management console to remotely log in to an ECS without a bound
EIP. For details, see section 3.3.1 Logging In to an ECS Using VNC.

![](media/7d66479e50c17f99a9e35c5fbe2b1ae3.png)

GPU-optimized g2 ECSs do not support remote login provided by the public cloud
platform. Before logging in to such an ECS using VNC, install the VNC server on
the ECS. For more information, see section 5.4.2 How Can I Log In to a
GPU-optimized g2 ECS Using VNC?

-   Logging in to an ECS using SSH

This option applies only to ECSs running Linux. You can use a remote login tool,
such as PuTTY, to log in to an ECS. The ECS must have a bound EIP.

You can log in to a Linux ECS using a username and password or a key pair. For
instructions about how to log in to an ECS using a username and password, see
section 3.3.3 Logging In to a Linux ECS Using a Password (SSH). For instructions
about how to log in to an ECS using a key pair, see section 3.3.2 Logging In to
a Linux ECS Using a Key Pair (SSH).

-   Logging in to an ECS using MSTSC

This option applies only to ECSs running Windows. You can run the **mstsc**
command on a local computer to log in to an ECS. The ECS must have a bound EIP.

You can only log in to a Windows ECS using a username and password. For details,
see section 3.3.4 Logging In to a Windows ECS Using a Password (MSTSC).

![](media/7d66479e50c17f99a9e35c5fbe2b1ae3.png)

If you log in to a GPU-optimized ECS using MSTSC, graphics acceleration will
fail. This is because MSTSC replaces the WDDM GPU driver with a non-accelerated
remote desktop display driver.

Therefore, you must use other methods to log in to the ECS, such as VNC. If the
remote login function available on the management console fails to meet your
service requirements, you must install a suitable remote login tool on the ECS.
