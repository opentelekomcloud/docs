# How Can I Enable Automatic Initialization of EVS Disks of Instances That Have Been Added in a Scaling Action to an AS Group?<a name="EN-US_TOPIC_0042018406"></a>

## Scenarios<a name="section19634929"></a>

After an ECS is created, EVS disks attached to the ECS must be initialized. If multiple ECSs are added to the AS group in scaling actions, you must manually initialize the EVS disks of each ECS, which requires a long period of time.

This section describes how to configure scripts to enable automatic initialization of EVS disks, including disk partitioning and attaching specified directories. The scripts can only be used to initialize one EVS disk.

This section uses CentOS 6.5 as an example. For details about how to configure DHCP on other OSs, see the relevant OS documentation.

## Procedure<a name="section42496641"></a>

1.  Log in to the instance as user  **root**.
2.  Run a command to switch to the directory storing the script:

    **cd /_script directory_**

    An example is as follows:

    **cd /home**

3.  Run the following command to create a script:

    **vi  _script name_**

    An example is as follows:

    **vi fdisk\_mount.sh**

4.  Press  **i**  to go to the script editing page.

    The following script is used as an example to show how to implement automatic initialization of one data disk:

    ```
    #!/bin/bash 
    bash_scripts_name=fdisk_mount.sh 
    ini_path=/home/fdisk.ini 
    disk= 
    size= 
    mount= 
    partition= 
     
    function get_disk_from_ini() 
    { 
    disk=`cat $ini_path|grep disk| awk -F '=' '{print $2}'` 
    if [ $disk = "" ] 
    then 
        echo "disk is null in file,exit" 
        exit 
    fi 
    result=`fdisk -l $disk | grep $disk` 
    if [ $result = 1 ] 
    then 
        echo "disk path is not exist in linux,exit" 
        exit 
    fi 
     
    } 
     
    function get_size() 
    { 
    size=`cat $ini_path| grep size|awk -F '=' '{print $2}'` 
    if [ $size = "" ] 
    then 
        echo "size is null,exit" 
        exit 
    fi 
    } 
     
    function make_fs_mount() 
    { 
    mkfs.ext4 -T largefile $partition 
    if [ $? -ne 0 ] 
    then 
        echo "mkfs disk failed,exit" 
        exit 
    fi  
     
    dir=`cat $ini_path|grep mount |awk -F '=' '{print $2}'` 
    if [ $dir = "" ] 
    then 
        echo "mount dir is null in file,exit" 
        exit 
    fi 
     
    if [ ! -d $dir ] 
    then 
        mkdir -p $dir 
    fi 
     
    mount $partition $dir 
    if [ $? -ne 0 ] 
    then 
        echo "mount disk failed,exit" 
        exit 
    fi  
     
    echo "$partition $dir ext3 defaults 0 0" >> /etc/fstab 
    } 
     
    function remove_rc() 
    { 
    cat /etc/rc.local | grep $bash_scripts_name 
    if [ $? ne 0 ] 
    then 
        sed -i '/'$bash_scripts_name'/d' /etc/rc.local 
    fi 
    } 
     
    ################## start ####################### 
    ##1. Check whether the configuration file exists.
    if [ ! -f $ini_path ] 
    then 
        echo "ini file not exist,exit" 
        exit 
    fi 
     
    ##2. Obtain the device path for the specified disk from the configuration file.
    get_disk_from_ini 
     
    ##3. Obtain the size of the size partition from the configuration file.
    get_size 
     
    ##4. Partition the disk.
    fdisk $disk  <<EOF 
    n 
    p 
    1 
    1 
    $size        
    w 
    EOF 
    partition=`fdisk -l $disk 2>/dev/null| grep "^/dev/[xsh].*d" | awk '{print $1}'` 
     
    ##5. Format the partition and attach the partition to the specified directory.
    make_fs_mount 
     
    ##6. Change startup items to prevent re-execution of the scripts.
    remove_rc 
    echo 'SUCESS'
    ```

5.  Press  **Esc**, enter  **:wq**, and press  **Enter**  to save the changes and exit.
6.  Run the following command to create the configuration file:

    **vi fdisk.ini**

7.  Press  **i**  to go to the file editing page.

    The drive letter, size, and directory of the EVS disk are configured in the configuration file. You can change the settings based on the following displayed information.

    ```
    disk=/dev/xdev 
    size=+100G 
    mount=/opt/test
    ```

8.  Press  **Esc**, enter  **:wq**, and press  **Enter**  to save the changes and exit.
9.  Run the following command to open configuration file  **rc.local**:

    **vi /etc/rc.local**

10. Press  **i**  to add the following content to the  **rc.local**  file:

    **/home/fdisk\_mount.sh**

    After the  **rc.local**  file is configured, the EVS disk initialization script will be automatically executed when the ECS starts.

11. Press  **Esc**, enter  **:wq**, and press  **Enter**  to save the changes and exit.
12. Create a private image using an ECS.
13. Create an AS configuration.

    When you specify the AS configuration information, select the private image created in the preceding step and select an EVS disk.

14. Create an AS group.

    When you configure the AS group, select the AS configuration created in the preceding step.

    After the AS group is created, EVS disks of new ECSs added in scaling actions to this AS group will be automatically initialized based on the configuration in the private image.


