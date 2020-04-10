# Optimization Process<a name="EN-US_TOPIC_0047501112"></a>

ECSs require Xen Guest OS driver \(PV driver\) and KVM Guest OS driver \(UVP VMTools\). To ensure that ECSs support both Xen and KVM and to improve network performance, the PV driver and UVP VMTools must be installed for the image.

1.  Create an ECS using the Windows private image to be optimized and log in to the ECS.
2.  Install the latest version of PV driver on the ECS.

    For details, see  [Installing the PV Driver](installing-the-pv-driver.md).

3.  Install the UVP VMTools required for creating ECSs in the KVM virtual resource pool.

    For details, see  [Installing UVP VMTools](installing-uvp-vmtools.md).

4.  On the ECS, choose  **Control Panel**  \>  **Power Options**. Click  **Choose when to turn off the display**, select  **Never**  for  **Turn off the display**, and save the changes.
5.  Clear system logs and then stop the ECS.

    For details, see  [Clearing System Logs](clearing-system-logs-(windows).md).

6.  Create a Windows private image using the ECS.

