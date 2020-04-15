# Enabling NIC Multi-Queue<a name="EN-US_TOPIC_0058758453"></a>

## Scenarios<a name="section2585561135"></a>

Single-core CPU performance cannot meet the requirement of processing NIC interruptions incurred with the increase of network I/O bandwidth. NIC multi-queue enables multiple CPUs to process ECS NIC interruptions, thereby improving network PPS and I/O performance.

The ECS described in this section is assumed to comply with the requirements on specifications and virtualization type.

-   If the ECS was created using a public image listed in  [Support of NIC Multi-Queue](#section892862210138), NIC multi-queue has been enabled on the ECS by default. Therefore, you do not need to perform the operations described in this section.
-   In the ECS was created using a private image and the external image file is listed in  [Support of NIC Multi-Queue](#section892862210138), perform the following operations to enable NIC multi-queue:
    1.  [Importing the External Image File to the IMS Console](#section1659682611504)
    2.  [Setting NIC Multi-Queue for the Image](#section1949113217282)
    3.  [Creating an ECS Using a Private Image](#section1841681225617)
    4.  [Enabling NIC Multi-Queue](#section214227201118)


## Support of NIC Multi-Queue<a name="section892862210138"></a>

NIC multi-queue can be enabled on an ECS only when the ECS specifications, virtualization type, and image OS meet the requirements described in this section.

-   For details about the ECS specifications that support NIC multi-queue, see  [Instances](instance-(service-overview).md).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the number of NIC queues is greater than 1, NIC multi-queue is supported.  

-   Only KVM ECSs support NIC multi-queue.
-   The Linux public images listed in  [Table 1](#table1572993710538)  support NIC multi-queue.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   Windows public images have not supported NIC multi-queue. If you enable NIC multi-queue in a Windows public image, starting an ECS created using such an image may be slow.  
    >-   You are advised to upgrade the kernel version of the Linux ECS to 2.6.35 or later. Otherwise, NIC multi-queue is not supported.  
    >    Run the  **uname -r**  command to obtain the kernel version. If the kernel version is earlier than 2.6.35, contact technical support to upgrade the kernel.  


**Table  1**  Support of NIC multi-queue for KVM ECSs

<a name="table1572993710538"></a>
<table><thead align="left"><tr id="row972943718537"><th class="cellrowborder" valign="top" width="15.7%" id="mcps1.2.4.1.1"><p id="p38709187544"><a name="p38709187544"></a><a name="p38709187544"></a>OS</p>
</th>
<th class="cellrowborder" valign="top" width="59.27%" id="mcps1.2.4.1.2"><p id="p5147627165419"><a name="p5147627165419"></a><a name="p5147627165419"></a>Image</p>
</th>
<th class="cellrowborder" valign="top" width="25.03%" id="mcps1.2.4.1.3"><p id="p17291137195315"><a name="p17291137195315"></a><a name="p17291137195315"></a>Status</p>
</th>
</tr>
</thead>
<tbody><tr id="row972916372532"><td class="cellrowborder" rowspan="4" valign="top" width="15.7%" headers="mcps1.2.4.1.1 "><p id="p28700187548"><a name="p28700187548"></a><a name="p28700187548"></a>Windows</p>
</td>
<td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.2 "><p id="p472171412162"><a name="p472171412162"></a><a name="p472171412162"></a>Windows Server 2008 WEB R2 64bit</p>
</td>
<td class="cellrowborder" valign="top" width="25.03%" headers="mcps1.2.4.1.3 "><p id="p2886168192713"><a name="p2886168192713"></a><a name="p2886168192713"></a>Supported using private images</p>
</td>
</tr>
<tr id="row972953755310"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1647133215570"><a name="p1647133215570"></a><a name="p1647133215570"></a>Windows Server 2008 R2 Standard/DataCenter/Enterprise 64bit</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p557419131446"><a name="p557419131446"></a><a name="p557419131446"></a>Supported using private images</p>
</td>
</tr>
<tr id="row272913785318"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p265223212579"><a name="p265223212579"></a><a name="p265223212579"></a>Windows Server 2012 R2 Standard/DataCenter 64bit</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p15781139411"><a name="p15781139411"></a><a name="p15781139411"></a>Supported using private images</p>
</td>
</tr>
<tr id="row1936855185619"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p236185520564"><a name="p236185520564"></a><a name="p236185520564"></a>Windows Server 2016 Standard/DataCenter 64bit</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p13581213344"><a name="p13581213344"></a><a name="p13581213344"></a>Supported using private images</p>
</td>
</tr>
<tr id="row193625510561"><td class="cellrowborder" rowspan="7" valign="top" width="15.7%" headers="mcps1.2.4.1.1 "><p id="p10611235104510"><a name="p10611235104510"></a><a name="p10611235104510"></a>Linux</p>
</td>
<td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.2 "><p id="p11761032144514"><a name="p11761032144514"></a><a name="p11761032144514"></a>Ubuntu 14.04/16.04 server 64bit</p>
</td>
<td class="cellrowborder" valign="top" width="25.03%" headers="mcps1.2.4.1.3 "><p id="p1760618505216"><a name="p1760618505216"></a><a name="p1760618505216"></a>Supported</p>
</td>
</tr>
<tr id="row48211412576"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p317611322451"><a name="p317611322451"></a><a name="p317611322451"></a>OpenSUSE 42.2 64bit</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p26102501217"><a name="p26102501217"></a><a name="p26102501217"></a>Supported</p>
</td>
</tr>
<tr id="row128212165720"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p71761432124513"><a name="p71761432124513"></a><a name="p71761432124513"></a>SUSE Enterprise 12 SP1/SP2 64bit</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p146144501229"><a name="p146144501229"></a><a name="p146144501229"></a>Supported</p>
</td>
</tr>
<tr id="row382318120575"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p317643234518"><a name="p317643234518"></a><a name="p317643234518"></a>CentOS 6.8/6.9/7.0/7.1/7.2/7.3/7.4/7.5/7.6 64bit</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p4616155017215"><a name="p4616155017215"></a><a name="p4616155017215"></a>Supported</p>
</td>
</tr>
<tr id="row1823101135717"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p41761732134519"><a name="p41761732134519"></a><a name="p41761732134519"></a>Debian 8.0.0/8.8.0/8.9.0/9.0.0 64bit</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p261865018213"><a name="p261865018213"></a><a name="p261865018213"></a>Supported</p>
</td>
</tr>
<tr id="row198238116573"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1517793244513"><a name="p1517793244513"></a><a name="p1517793244513"></a>Fedora 24/25 64bit</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p12621135019218"><a name="p12621135019218"></a><a name="p12621135019218"></a>Supported</p>
</td>
</tr>
<tr id="row131071919135712"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p20177123211453"><a name="p20177123211453"></a><a name="p20177123211453"></a>EulerOS 2.2 64bit</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p562713501924"><a name="p562713501924"></a><a name="p562713501924"></a>Supported</p>
</td>
</tr>
</tbody>
</table>

## Importing the External Image File to the IMS Console<a name="section1659682611504"></a>

For details, see "Registering an Image File as a Private Image" in  _Image Management Service User Guide_.

## Setting NIC Multi-Queue for the Image<a name="section1949113217282"></a>

Windows OSs have not commercially supported NIC multi-queue. If you enable NIC multi-queue in a Windows image, starting an ECS created using such an image may be slow.

Use either of the following methods to set the NIC multi-queue attribute:

**Method 1:**

1.  Log in to the management console and click  **Image Management Service**  under  **Computing**.
2.  Click the  **Private Images**  tab, locate the row containing the target image, click  **Modify**  in the  **Operation**  column.
3.  Set the NIC multi-queue attribute of the image.

**Method 2:**

1.  Log in to the management console and click  **Image Management Service**  under  **Computing**.
2.  Click the  **Private Images**  tab. In the image list, click the name of the target image to switch to the page providing details about the image.
3.  Click  **Modify**  in the upper right corner. In the displayed  **Modify Image**  dialog box, set the NIC multi-queue attribute.

**Method 3:**  Add  **hw\_vif\_multiqueue\_enabled**  to an image through the API.

1.  <a name="en-us_topic_0085214115_li13762086162643"></a>For instructions about how to obtain the token, see  [Token Authentication](https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328003.html).
2.  For instructions about how to call an API to update image information, see "Updating Image Information \(Native OpenStack API\)" in  _Image Management Service API Reference_.
3.  Add  **X-Auth-Token**  to the request header.

    The value of  **X-Auth-Token**  is the token obtained in step  [1](#en-us_topic_0085214115_li13762086162643).

4.  Add  **Content-Type**  to the request header.

    The value of  **Content-Type**  is  **application/openstack-images-v2.1-json-patch**.

    The request URI is in the following format:

    PATCH /v2/images/\{image\_id\}

    The request body is as follows:

    ```
    [       
             { 
              "op":"add",
              "path":"/hw_vif_multiqueue_enabled", 
              "value": "true" 
             } 
     ]
    ```

    [Figure 1](#en-us_topic_0085214115_fig3215821216479)  shows an example request body for modifying the NIC multi-queue attribute.

    **Figure  1**  Example request body<a name="en-us_topic_0085214115_fig3215821216479"></a>  
    ![](figures/example-request-body.png "example-request-body")


## Creating an ECS Using a Private Image<a name="section1841681225617"></a>

For details, see  [Creating an ECS](creating-an-ecs.md). Note the following when setting the parameters:

-   **Region**: Select the region where the private image is located.
-   **Image**: Select  **Private image**  and then the desired image from the drop-down list.

## Enabling NIC Multi-Queue<a name="section214227201118"></a>

KVM Windows ECSs use private images to support NIC multi-queue. For details, see "How Do I Set NIC Multi-queue Feature of an Image?" in  _Image Management Service User Guide_.

This section uses a Linux ECS running CentOS 7.4 as an example to describe how to enable NIC multi-queue.

1.  Enable NIC multi-queue.

    1.  Log in to the ECS.
    2.  Run the following command to obtain the number of queues supported by the NIC and the number of queues with NIC multi-queue enabled:

        **ethtool -l **_NIC_

    3.  Run the following command to configure the number of queues used by the NIC:

        **ethtool -L** _NIC_ **combined** _Number of queues_

    An example is provided as follows:

    ```
    [root@localhost ~]# ethtool -l eth0  #View the number of queues used by NIC eth0.
    Channel parameters for eth0:
    Pre-set maximums:
    RX:               0
    TX:               0
    Other:                  0
    Combined: 4  #Indicates that a maximum of four queues can be enabled for the NIC.
    Current hardware settings:
    RX:               0
    TX:               0
    Other:                  0
    Combined: 1 #Indicates that one queue has been enabled.
    
    [root@localhost ~]# ethtool -L eth0 combined 4 #Enable four queues on NIC eth0.
    ```

2.  \(Optional\) Enable irqbalance so that the system automatically allocates NIC interrupts on multiple vCPUs.
    1.  Run the following command to enable irqbalance:

        **service irqbalance start**

    2.  Run the following command to view the irqbalance status:

        **service irqbalance status**

        If the  **Active**  value in the command output contains  **active\(running\)**, irqbalance has been enabled.

        **Figure  2**  Enabled irqbalance<a name="fig165114253253"></a>  
        ![](figures/enabled-irqbalance.png "enabled-irqbalance")

3.  \(Optional\) Enable interrupt binding.

    Enabling irqbalance allows the system to automatically allocate NIC interrupts, improving network performance. If the improved network performance still fails to meet your requirements, manually configure interrupt affinity on the ECS.

    To do so, perform the following operations:

    Configure the following script so that one ECS vCPU serves the interrupt requests initialized by one queue. One queue corresponds to one interrupt, and one interrupt binds to one vCPU.

    ```
    #!/bin/bash
    service irqbalance stop
    
    eth_dirs=$(ls -d /sys/class/net/eth*)
    if [ $? -ne 0 ];then
        echo "Failed to find eth*  , sleep 30" >> $ecs_network_log
        sleep 30
        eth_dirs=$(ls -d /sys/class/net/eth*)
    fi
    
    for eth in $eth_dirs
    do
        cur_eth=$(basename $eth)
        cpu_count=`cat /proc/cpuinfo| grep "processor"| wc -l`
        virtio_name=$(ls -l /sys/class/net/"$cur_eth"/device/driver/ | grep pci |awk {'print $9'})
    
        affinity_cpu=0
        virtio_input="$virtio_name""-input"
        irqs_in=$(grep "$virtio_input" /proc/interrupts | awk -F ":" '{print $1}')
        for irq in ${irqs_in[*]}
        do
            echo $((affinity_cpu%cpu_count)) > /proc/irq/"$irq"/smp_affinity_list
            affinity_cpu=$[affinity_cpu+2]
        done
    
        affinity_cpu=1
        virtio_output="$virtio_name""-output"
        irqs_out=$(grep "$virtio_output" /proc/interrupts | awk -F ":" '{print $1}')
        for irq in ${irqs_out[*]}
        do
            echo $((affinity_cpu%cpu_count)) > /proc/irq/"$irq"/smp_affinity_list
            affinity_cpu=$[affinity_cpu+2]
        done
    done
    ```

4.  \(Optional\) Enable XPS and RPS.

    XPS allows the system with NIC multi-queue enabled to select a queue by vCPU when sending a data packet.

    ```
    #!/bin/bash
    # enable XPS feature
    cpu_count=$(grep -c processor /proc/cpuinfo)
    dec2hex(){
      echo $(printf "%x" $1)
    }
    eth_dirs=$(ls -d /sys/class/net/eth*)
    if [ $? -ne 0 ];then
        echo "Failed to find eth* , sleep 30" >> $ecs_network_log
        sleep 30
        eth_dirs=$(ls -d /sys/class/net/eth*)
    fi
    for eth in $eth_dirs
    do
        cpu_id=1
        cur_eth=$(basename $eth)
        cur_q_num=$(ethtool -l $cur_eth | grep -iA5 current | grep -i combined | awk {'print $2'})
        for((i=0;i<cur_q_num;i++))
        do
            if [ $i -eq $ cpu_count ];then
                cpu_id=1
            fi
            xps_file="/sys/class/net/${cur_eth}/queues/tx-$i/xps_cpus"
            rps_file="/sys/class/net/${cur_eth}/queues/rx-$i/rps_cpus"
            cpuset=$(dec2hex "$cpu_id")
            echo $cpuset > $xps_file
            echo $cpuset > $rps_file
            let cpu_id=cpu_id*2
        done
    done
    ```


