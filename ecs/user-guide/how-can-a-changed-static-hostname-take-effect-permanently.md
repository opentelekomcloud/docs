# How Can a Changed Static Hostname Take Effect Permanently?<a name="EN-US_TOPIC_0050735736"></a>

## Symptom<a name="section319352620019"></a>

The static hostname of a Linux ECS is user defined and injected using Cloud-Init during the ECS creation. Although the hostname can be changed by running the  **hostname**  command, the changed hostname is restored after the ECS is restarted.

## Changing the Hostname on the ECS<a name="section14535183616249"></a>

To make the hostname changed by running the  **hostname**  command take effect even after the ECS is stopped or restarted, save the changed hostname into configuration files.

The changed hostname is assumed to be  **new\_hostname**.

1.  Modify the  **/etc/hostname**  configuration file.
    1.  Run the following command to edit the configuration file:

        **sudo vim /etc/hostname**

    2.  Change the hostname to the new one.
    3.  Run the following command to save and exit the configuration file:

        **:wq**

2.  Modify the  **/etc/sysconfig/network**  configuration file.
    1.  Run the following command to edit the configuration file:

        **sudo vim /etc/sysconfig/network**

    2.  Change the  **HOSTNAME**  value to the new hostname.

        **HOSTNAME=_Changed hostname_**

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If there is no  **HOSTNAME**  in the configuration file, manually add this parameter and set it to the changed hostname.  

        An example is provided as follows:

        **HOSTNAME=new\_hostname**

    3.  Run the following command to save and exit the configuration file:

        **:wq**

3.  Modify the  **/etc/cloud/cloud.cfg**  configuration file.
    1.  Run the following command to edit the configuration file:

        **sudo vim /etc/cloud/cloud.cfg**

    2.  Use either of the following methods to modify the configuration file:
        -   Method 1: Change the  **preserve\_hostname**  parameter value or add the  **preserve\_hostname**  parameter to the configuration file.

            If  **preserve\_hostname: false**  is already available in the  **/etc/cloud/cloud.cfg**  configuration file, change it to  **preserve\_hostname: true**. If  **preserve\_hostname**  is unavailable in the  **/etc/cloud/cloud.cfg**  configuration file, add  **preserve\_hostname: true**  before  **cloud\_init\_modules**.

            If you use method 1, the changed hostname still takes effect after the ECS is stopped or restarted. However, if the ECS is used to create a private image and the image is used to create a new ECS, the hostname of the new ECS is the hostname \(**new\_hostname**\) used by the private image, and user-defined hostnames cannot be injected using Cloud-Init.

        -   Method 2 \(recommended\): Delete or comment out  **- update\_hostname**.

            If you use method 2, the changed hostname still takes effect after the ECS is stopped or restarted. If the ECS is used to create a private image and the image is used to create a new ECS, the changed hostname permanently takes effect, and user-defined hostnames \(such as  **new\_new\_hostname**\) can be injected using Cloud-Init.


4.  Run the following command to restart the ECS:

    **sudo reboot**

5.  Run the following command to check whether the hostname has been changed:

    **sudo hostname**

    If the changed hostname is displayed in the command output, the hostname has been changed and the new name permanently takes effect.


