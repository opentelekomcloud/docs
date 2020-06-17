# Installing the NVIDIA GPU Driver and CUDA Toolkit on a P2 BMS<a name="EN-US_TOPIC_0140740386"></a>

## Scenarios<a name="section263791112917"></a>

After a GPU-accelerated P2 BMS \(using the physical.p2.large flavor\) is created, the NVIDIA GPU driver and CUDA Toolkit must be installed on it for computing acceleration.

## Prerequisites<a name="section9977817203914"></a>

-   An EIP has been bound to the BMS.
-   You have obtained the required driver installation packages.

    **Table  1**  Download paths for the NVIDIA GPU driver and CUDA Toolkit

    <a name="table7349118172716"></a>
    <table><thead align="left"><tr id="row1134728172710"><th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.4.1.1"><p id="p6347889271"><a name="p6347889271"></a><a name="p6347889271"></a>OS</p>
    </th>
    <th class="cellrowborder" valign="top" width="35.35353535353536%" id="mcps1.2.4.1.2"><p id="p43474842718"><a name="p43474842718"></a><a name="p43474842718"></a>Driver</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.41414141414141%" id="mcps1.2.4.1.3"><p id="p153472820273"><a name="p153472820273"></a><a name="p153472820273"></a>How to Obtain</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1034720812277"><td class="cellrowborder" rowspan="2" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p113471884270"><a name="p113471884270"></a><a name="p113471884270"></a>CentOS 7.4</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.35353535353536%" headers="mcps1.2.4.1.2 "><p id="p13347383279"><a name="p13347383279"></a><a name="p13347383279"></a>NVIDIA GPU driver installation package: <strong id="b842352706111915"><a name="b842352706111915"></a><a name="b842352706111915"></a>NVIDIA-Linux-x86_64-384.81.run</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.4.1.3 "><p id="p18347489273"><a name="p18347489273"></a><a name="p18347489273"></a><a href="https://www.nvidia.com/download/driverResults.aspx/124722/en-us" target="_blank" rel="noopener noreferrer">https://www.nvidia.com/download/driverResults.aspx/124722/en-us</a></p>
    </td>
    </tr>
    <tr id="row103491815276"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p183478872720"><a name="p183478872720"></a><a name="p183478872720"></a>CUDA Toolkit installation package: <strong id="b6101155264214"><a name="b6101155264214"></a><a name="b6101155264214"></a>cuda_9.0.176_384.81_linux.run</strong></p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p10349208112719"><a name="p10349208112719"></a><a name="p10349208112719"></a><a href="https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_384.81_linux-run" target="_blank" rel="noopener noreferrer">https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_384.81_linux-run</a></p>
    </td>
    </tr>
    </tbody>
    </table>


## CentOS 7.4<a name="section8829131916256"></a>

1.  Log in to the target BMS and run the following command to switch to user  **root**:

    **su** **root**

2.  \(Optional\) If the  **gcc**,  **gcc-c++**,  **make**, and  **kernel-devel**  dependency packages do not exist, run the following commands to install the gcc, gcc-c++, make, and kernel-devel tools:

    **yum** **install** **gcc**

    **yum** **install** **gcc-c++**

    **yum** **install** **make**

    **yum** **install** ****kernel-devel-\`uname**** ****-r\`****

3.  \(Optional\) Add the Nouveau driver to the blacklist.

    If the Nouveau driver has been installed and loaded, perform the following operations to add the Nouveau driver to the blacklist to avoid conflicts:

    1.  Add  **blacklist nouveau**  to the end of the  **/etc/modprobe.d/blacklist.conf**  file.
    2.  Run the following commands to back up and reconstruct initramfs:

        **mv** **/boot/initramfs-$\(uname** **-r\).img** **/boot/initramfs-$\(uname** **-r\).img.bak**

        **dracut** **-v** **/boot/initramfs-$\(uname** **-r\).img** **$\(uname** **-r\)**

    3.  Run the  **reboot**  command to restart the BMS.

4.  \(Optional\) If the X service is running, run the  **systemctl** **set-default** **multi-user.target**  command and restart the BMS to enter multi-user mode.
5.  \(Optional\) Install the NVIDIA GPU driver.

    If you selected a specified version of NVIDIA GPU driver rather than a version contained in the CUDA Toolkit, perform this step.

    1.  Download NVIDIA GPU driver installation package  **NVIDIA-Linux-x86\_64-**_xxx.yy_**.run**  from  [https://www.nvidia.com/Download/index.aspx?lang=en](https://www.nvidia.com/Download/index.aspx?lang=en), and upload this package to the  **/tmp**  directory on the BMS.

        **Figure  1**  Searching for the NVIDIA GPU driver package \(CentOS 7.4\)<a name="en-us_topic_0095251850_fig84466243358"></a>  
        ![](figures/searching-for-the-nvidia-gpu-driver-package-(centos-7-4).png "searching-for-the-nvidia-gpu-driver-package-(centos-7-4)")

    2.  Run the following command to install the NVIDIA GPU driver:

        **sh** **./NVIDIA-Linux-x86\_64-**_xxx.yy_**.run**

    3.  Run the following command to delete the installation package:

        **rm** **-f** **NVIDIA-Linux-x86\_64-**_xxx.yy_**.run**

6.  Install the CUDA Toolkit.
    1.  Download CUDA Toolkit installation package  **cuda\_**_a.b.cc\_xxx.yy_**\_linux.run**  from  [https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads), and upload this package to the  **/tmp**  directory on the BMS.
    2.  Run the following command to change the permission to the installation package:

        **chmod** **+x** ****cuda\_****_a.b.cc\_xxx.yy_****\_linux.run****

    3.  Run the following command to install the CUDA Toolkit:

        **./**cuda\_****_a.b.cc\_xxx.yy_****\_linux.run**** **-toolkit** **-samples** **-silent** **-override** **--tmpdir=/tmp/**

    4.  Run the following command to delete the installation package:

        **rm** **-f** **cuda**_**\_**a.b.cc\_xxx.yy_**\_linux.run**

    5.  Run the following commands to check whether the installation is successful:

        **cd** **/usr/local/cuda/samples/1\_Utilities/deviceQueryDrv/**

        **make**

        **./deviceQueryDrv**

        If the command output contains "Result = PASS", the CUDA Toolkit and the NVIDIA GPU driver have been installed successfully.



