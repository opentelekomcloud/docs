# Injecting Files into ECSs<a name="EN-US_TOPIC_0013898301"></a>

## Scenarios<a name="section59120639141539"></a>

Use the file injection function to inject files into ECSs to:

-   Simplify ECS configuration.
-   Initialize the ECS OS configuration.
-   Upload your scripts to ECSs during ECS creation.
-   Perform other tasks using scripts.

>![](/images/icon-note.gif) **NOTE:**   
>KVM ECSs do not support file injection. You are advised to use user data injection for such ECSs. For details, see  [Injecting User Data into ECSs](injecting-user-data-into-ecss.md).  

## Use Restrictions<a name="section31714110141539"></a>

-   Linux
    -   Only user  **root**  can execute injected files.
    -   You can inject files into any directory of a Linux EVS system disk. The names of the files to be injected and directories in which they are stored can contain only letters, digits, underscores \(\_\), and periods \(.\), for example,  **/etc/foo.txt**.
    -   The file systems supported by Linux EVS system disks are ext3 and ext4.
    -   The default permission of the injected files is read and write.

        To change file permissions, log in to the ECS as user  **root**, switch to the directory containing the injected files, and run  **chmod 755 **_Name of the injected file_.

    -   Injected files can be manually or automatically executed.
    -   To enable the automatic execution of injected files, the files must be stored in the  **/etc/init.d**  directory and you must have changed the permission of the files.
    -   The file size must be less than or equal to 1 KB.

-   Windows
    -   Only user  **administrator**  can execute injected files.
    -   You can inject files only into the root directory of drive C. You cannot change the directory for storing the injected files during the file injection process.
    -   The file system supported by Windows EVS system disks is NTFS.
    -   Injected files can only be manually executed.
    -   The file size must be less than or equal to 1 KB.


## How to Use File Injection<a name="section60709488141539"></a>

1.  Create a script file that meets your requirements and is compatible with the OS.
2.  During ECS creation, select the created script file and set the directory for storing the file.
3.  The system automatically creates the ECS and injects the file into the ECS.
4.  \(Linux\) Change the permission of the script file.
5.  Execute the script.

## Case 1<a name="section24296060141539"></a>

This case illustrates how to use the file injection function to simplify ECS configuration.

In this example, vim is configured to enable syntax highlighting, display line numbers, and set the tab stop to  **4**. The .vimrc configuration file is created and injected into the  **/root/.vimrc**  directory during ECS creation. After the ECS is created, vim is automatically configured based on your requirements. This improves ECS configuration efficiency, especially in batch ECS creation scenarios.

The content of the script file to be injected is as follows:

```
syntax on
set tabstop=4
set number
```

## Case 2<a name="section42838600141539"></a>

This case illustrates how to use the file injection function to initialize ECS configuration.

In this example, the firewall configuration is automatically initialized upon ECS startup. The firewall configuration is written to script file  **initial.sh**, and the file is injected into the  **/etc/init.d**  directory.

The content of the script file to be injected is as follows:

```
#! /bin/sh
iptables -A INPUT -p tcp --dport 21 -j ACCEPT 
iptables -A INPUT -p tcp --dport 49152:65534 -j ACCEPT
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED -j ACCEPT
```

By default, the injected script file permission is read and write. You must perform the following operations on the ECS that has the script file injected when you use the ECS for the first time.

Log in to the ECS as user  **root**  and run the following commands to change the permission on the injected file and add the file link:

**cd /etc/init.d**

**chmod 775 initial.sh**

**ln -s /etc/init.d/initial.sh /etc/rc.d/rc3.d/S98initial**

>![](/images/icon-note.gif) **NOTE:**   
>In the preceding commands:  
>-   **/etc/rc.d/rc3.d**  indicates the directory for automatically executed script files when the OS runlevel is 3. If the OS runlevel is different, you must change the directory accordingly. For example, if the OS runlevel is 2, change the directory to  **/etc/rc.d/rc2.d**.  
>-   The  **S**  parameter in  **S98initial**  indicates that the script is executed during OS startup. The  **98**  parameter in  **S98initial**  indicates the script startup sequence, meaning that the script is executed in the ninety-eighth place. You can change this value as required. The OS executes scripts one by one in ascending order based on their startup sequence.  

After these commands are executed, each time you start the ECS, the  **initial.sh**  script is automatically executed to initialize the firewall configuration.

## Case 3<a name="section22603169194910"></a>

This case illustrates how to use the file injection function to activate user  **root**  permission to log in to an ECS. After injecting the file, you can log in to the ECS as user  **root**  using SSH key pair authentication.

The content of the script file to be injected is as follows:

```
#cloud-config
disable_root: false
runcmd:
- sed -i 's/^PermitRootLogin.*$/PermitRootLogin without-password/' /etc/ssh/sshd_config
- sed -i '/^KexAlgorithms.*$/d' /etc/ssh/sshd_config
- service sshd restart
```

