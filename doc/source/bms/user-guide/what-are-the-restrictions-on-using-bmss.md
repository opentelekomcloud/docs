# What Are the Restrictions on Using BMSs?<a name="EN-US_TOPIC_0053536930"></a>

-   External hardware devices \(such as USB devices, bank U key, external hard disks, and dongle\) cannot be directly loaded.
-   You cannot create a raw server with no OS, that is, a BMS must have an OS.
-   The OSs of BMSs cannot be changed.
-   The OSs of Windows BMSs using public images are activated by default. The virtual OSs installed on the BMSs must be activated manually.
-   Custom BMS configuration is not supported. BMS specifications cannot be changed.
-   Only EVS disks whose device type is  **SCSI**  can be attached to a BMS.
-   BMSs using some flavors or images cannot have EVS disks attached because the servers do not have SDI iNICs or for other reasons.
-   Do not delete or modify built-in plug-ins of the image, such as Cloud-Init and bms-network-config. Otherwise, BMS basic functions will be affected.
-   If you choose to assign an IP address automatically when creating a BMS, do not change the private IP address of the BMS after the BMS is provisioned. Otherwise, the IP address may conflict with that of another BMS.
-   BMSs do not support bridge NICs which will cause network interruptions.
-   Do not upgrade the OS kernel. Otherwise, the hardware driver may be incompatible with the BMS, adversely affecting BMS reliability.

