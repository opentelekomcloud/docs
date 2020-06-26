# How Do I Install growpart for SUSE 11 SP4?<a name="EN-US_TOPIC_0078454810"></a>

## Scenarios<a name="section1565613201325"></a>

growpart for SUSE and openSUSE is an independent toolkit that does not start with  **cloud-\***. Perform the following operations to install growpart:

## Procedure<a name="section11829153012218"></a>

1.  Run the following commands to check whether Cloud-Init and growpart have been installed:

    **rpm -qa | grep cloud-init**

    The command output is as follows:

    ```
    cloud-init-0.7.8-39.2
    ```

    **rpm -qa | grep growpart**

    The command output is as follows:

    ```
    growpart-0.29-8.1
    ```

2.  Run the following command to uninstall Cloud-Init and growpart:

    **zypper remove cloud-init growpart**

3.  Run the following commands to clear residual files:

    **rm -fr /etc/cloud/\***

    **rm -fr /var/lib/cloud/\***

4.  Run the following command to install growpart:

    **zypper install http://download.opensuse.org/repositories/home:/garloff:/OTC:/cloudinit/SLE\_11\_SP4/noarch/growpart-0.27-1.1.noarch.rpm**

5.  Run the following command to install python-oauth:

    **zypper install http://download.opensuse.org/repositories/home:/garloff:/OTC:/cloudinit/SLE\_11\_SP4/x86\_64/python-oauth-1.0.1-35.1.x86\_64.rpm**

6.  Run the following command to install Cloud-Init:

    **zypper install http://download.opensuse.org/repositories/home:/garloff:/OTC:/cloudinit/SLE\_11\_SP4/x86\_64/cloud-init-0.7.6-27.23.1.x86\_64.rpm**

7.  Run the following commands to check whether growpart, python-oauth, and Cloud-Init have been installed successfully:

    **rpm -qa | grep growpart**

    The command output is as follows:

    ```
    growpart-0.27-1.1
    ```

    **rpm -qa | grep python-oauth**

    The command output is as follows:

    ```
    python-oauthlib-0.6.0-1.5
    python-oauth-1.0.1-35.1
    ```

    **rpm -qa | grep cloud-init**

    The command output is as follows:

    ```
    cloud-init-0.7.6-27.19.1
    ```

8.  Run the following command to check the configuration:

    **chkconfig cloud-init-local on;chkconfig cloud-init on;chkconfig cloud-config on;chkconfig cloud-final on**


