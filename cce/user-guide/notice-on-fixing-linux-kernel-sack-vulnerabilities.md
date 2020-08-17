# Notice on Fixing Linux Kernel SACK Vulnerabilities<a name="cce_01_0206"></a>

The Linux Kernel SACK vulnerabilities have been fixed. This section describes the solution to these vulnerabilities.

## Vulnerability Details<a name="section14399183415550"></a>

On June 18, 2019, Red Hat released a security notice, stating that three security vulnerabilities \(CVE-2019-11477, CVE-2019-11478, and CVE-2019-11479\) were found on the TCP SACK module of the Linux kernel. These vulnerabilities are related to the maximum segment size \(MSS\) and TCP selective acknowledgment \(SACK\) packets. Remote attackers can exploit these vulnerabilities to trigger a denial of service \(DoS\), resulting in server unavailability or breakdown.

Helpful links:

[https://www.suse.com/support/kb/doc/?id=7023928](https://www.suse.com/support/kb/doc/?id=7023928)

[https://access.redhat.com/security/vulnerabilities/tcpsack](https://access.redhat.com/security/vulnerabilities/tcpsack)

[https://www.debian.org/lts/security/2019/dla-1823](https://www.debian.org/lts/security/2019/dla-1823)

[https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/SACKPanic?](https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/SACKPanic?)

[https://github.com/Netflix/security-bulletins/blob/master/advisories/third-party/2019-001.md](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-party/2019-001.md)

**Table  1**  Vulnerability information

<a name="table124875855510"></a>
<table><thead align="left"><tr id="row1649155811555"><th class="cellrowborder" valign="top" width="25.72742725727427%" id="mcps1.2.5.1.1"><p id="p1516913249564"><a name="p1516913249564"></a><a name="p1516913249564"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.688131186881314%" id="mcps1.2.5.1.2"><p id="p1216962415619"><a name="p1216962415619"></a><a name="p1216962415619"></a>CVE-ID</p>
</th>
<th class="cellrowborder" valign="top" width="24.75752424757524%" id="mcps1.2.5.1.3"><p id="p1916932413568"><a name="p1916932413568"></a><a name="p1916932413568"></a>Discovered</p>
</th>
<th class="cellrowborder" valign="top" width="30.826917308269174%" id="mcps1.2.5.1.4"><p id="p616920246567"><a name="p616920246567"></a><a name="p616920246567"></a>Fixed</p>
</th>
</tr>
</thead>
<tbody><tr id="row24985819559"><td class="cellrowborder" valign="top" width="25.72742725727427%" headers="mcps1.2.5.1.1 "><p id="p16641153545619"><a name="p16641153545619"></a><a name="p16641153545619"></a>Input validation flaw</p>
</td>
<td class="cellrowborder" valign="top" width="18.688131186881314%" headers="mcps1.2.5.1.2 "><p id="p064163519566"><a name="p064163519566"></a><a name="p064163519566"></a><a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477" target="_blank" rel="noopener noreferrer">CVE-2019-11477</a></p>
</td>
<td class="cellrowborder" valign="top" width="24.75752424757524%" headers="mcps1.2.5.1.3 "><p id="p4641103525615"><a name="p4641103525615"></a><a name="p4641103525615"></a>2019-06-17</p>
</td>
<td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p464183516563"><a name="p464183516563"></a><a name="p464183516563"></a>2019-07-06</p>
</td>
</tr>
<tr id="row1549195865511"><td class="cellrowborder" valign="top" width="25.72742725727427%" headers="mcps1.2.5.1.1 "><p id="p964133555616"><a name="p964133555616"></a><a name="p964133555616"></a>Resource management flaw</p>
</td>
<td class="cellrowborder" valign="top" width="18.688131186881314%" headers="mcps1.2.5.1.2 "><p id="p106411935125617"><a name="p106411935125617"></a><a name="p106411935125617"></a><a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478" target="_blank" rel="noopener noreferrer">CVE-2019-11478</a></p>
</td>
<td class="cellrowborder" valign="top" width="24.75752424757524%" headers="mcps1.2.5.1.3 "><p id="p196415352561"><a name="p196415352561"></a><a name="p196415352561"></a>2019-06-17</p>
</td>
<td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p1464212357560"><a name="p1464212357560"></a><a name="p1464212357560"></a>2019-07-06</p>
</td>
</tr>
<tr id="row24965816558"><td class="cellrowborder" valign="top" width="25.72742725727427%" headers="mcps1.2.5.1.1 "><p id="p764216351564"><a name="p764216351564"></a><a name="p764216351564"></a>Resource management flaw</p>
</td>
<td class="cellrowborder" valign="top" width="18.688131186881314%" headers="mcps1.2.5.1.2 "><p id="p1264253595610"><a name="p1264253595610"></a><a name="p1264253595610"></a><a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479" target="_blank" rel="noopener noreferrer">CVE-2019-11479</a></p>
</td>
<td class="cellrowborder" valign="top" width="24.75752424757524%" headers="mcps1.2.5.1.3 "><p id="p19642435185613"><a name="p19642435185613"></a><a name="p19642435185613"></a>2019-06-17</p>
</td>
<td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p4642133595612"><a name="p4642133595612"></a><a name="p4642133595612"></a>2019-07-06</p>
</td>
</tr>
</tbody>
</table>

## Impact<a name="section1128815452562"></a>

Linux 2.6.29 and later versions \(CVE-2019-11477\)

## Solution<a name="section37521058125620"></a>

>![](public_sys-resources/icon-notice.gif) **NOTICE:** 
>-   EulerOS 2.2 supports an upgrade to the kernel version 3.10.0-327.62.59.83.h162.x86\_64.
>-   The node must be accessible to external networks. After the kernel is upgraded, restart the system.
>-   The following errors may be encountered during the upgrade. However, they do not affect system functions and can be ignored.
>    ```
>    depmod: ERROR: fstatat(9, vport-gre.ko): No such file or directory
>    depmod: ERROR: fstatat(9, vport-vxlan.ko): No such file or directory
>    depmod: ERROR: fstatat(9, vport-geneve.ko): No such file or directory
>    depmod: ERROR: fstatat(9, openvswitch.ko): No such file or directory
>    depmod: ERROR: fstatat(5, vport-gre.ko): No such file or directory
>    depmod: ERROR: fstatat(5, vport-vxlan.ko): No such file or directory
>    depmod: ERROR: fstatat(5, vport-geneve.ko): No such file or directory
>    depmod: ERROR: fstatat(5, openvswitch.ko): No such file or directory
>    ```

1.  Log in to the node as the root user and run the following command to update the kernel:

    **yum update kernel -y**

2.  When the  **yum update**  command is used to upgrade the operating system, container network components could become unavailable. Run the following command to restore the components:

    ```
    #!/bin/bash
    function upgrade_kmod()
    {
        openvswicth_mod_path=$(rpm -qal openvswitch-kmod)
        rpm_version=$(rpm -qal openvswitch-kmod|grep -w openvswitch|head -1|awk -F "/" '{print $4}')
        sys_version=`cat /boot/grub2/grub.cfg | grep EulerOS|awk 'NR==1{print $3}' | sed 's/[()]//g'`
    
        if [[ "${rpm_version}" != "${sys_version}" ]];then
            mkdir -p /lib/modules/"${sys_version}"/extra/openvswitch
            for path in ${openvswicth_mod_path[@]};do
                name=$(echo "$path" | awk -F "/" '{print $NF}')
                rm -f /lib/modules/"${sys_version}"/updates/"${name}"
    			rm -f /lib/modules/"${sys_version}"/extra/openvswitch/"${name}"
                ln -s "${path}" /lib/modules/"${sys_version}"/extra/openvswitch/"${name}"
            done
        fi
    	depmod ${sys_version}
    }
    upgrade_kmod
    ```

3.  Restart the VM.

    **reboot**


