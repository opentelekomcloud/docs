# How Can I Obtain the Mapping Between Disk Partitions and Disk Devices on a Linux ECS?<a name="EN-US_TOPIC_0087901488"></a>

For a Linux ECS, its disk partitions correspond to disk devices. This section uses a Linux ECS running Red Hat Enterprise Linux 7 as an example to describe how to obtain the mapping between disk partitions and disk devices.

1.  Log in to the Linux ECS as user  **root**.
2.  Right-click in the blank area of the desktop and choose  **Open Terminal**  from the shortcut menu.

    ![](figures/en-us_image_0087903699.png)

3.  Run the following command to view disk partitions and disk devices:

    **fdisk -l**

    ![](figures/en-us_image_0087903704.png)

    [Table 1](#table18572291102543)  lists the mapping between disk partitions and disk devices.

    **Table  1**  Mapping between disk partitions and disk devices

    <a name="table18572291102543"></a>
    <table><thead align="left"><tr id="row41136453102543"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p57921247102543"><a name="p57921247102543"></a><a name="p57921247102543"></a>Disk Partition</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p61109434102543"><a name="p61109434102543"></a><a name="p61109434102543"></a>Disk Device</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13113995102543"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p64587287102652"><a name="p64587287102652"></a><a name="p64587287102652"></a>xvda</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p64187774102652"><a name="p64187774102652"></a><a name="p64187774102652"></a>xvda</p>
    </td>
    </tr>
    <tr id="row66259557102543"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p18009654102652"><a name="p18009654102652"></a><a name="p18009654102652"></a>xvdb</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p49495871102652"><a name="p49495871102652"></a><a name="p49495871102652"></a>xvdb</p>
    </td>
    </tr>
    <tr id="row46710570102543"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p45030664102652"><a name="p45030664102652"></a><a name="p45030664102652"></a>xvdc</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p23605166102652"><a name="p23605166102652"></a><a name="p23605166102652"></a>xvdc</p>
    </td>
    </tr>
    <tr id="row38181009102543"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p28296922102652"><a name="p28296922102652"></a><a name="p28296922102652"></a>xvdd</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p10349350102652"><a name="p10349350102652"></a><a name="p10349350102652"></a>xvdd</p>
    </td>
    </tr>
    <tr id="row28140310102543"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p28483713102652"><a name="p28483713102652"></a><a name="p28483713102652"></a>xvde</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p25479437102652"><a name="p25479437102652"></a><a name="p25479437102652"></a>xvde</p>
    </td>
    </tr>
    <tr id="row41708350102543"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p52463771102652"><a name="p52463771102652"></a><a name="p52463771102652"></a>xvdf</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p21707025102652"><a name="p21707025102652"></a><a name="p21707025102652"></a>xvdf</p>
    </td>
    </tr>
    <tr id="row4820905102622"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p53838539102652"><a name="p53838539102652"></a><a name="p53838539102652"></a>xvdg</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p65954406102652"><a name="p65954406102652"></a><a name="p65954406102652"></a>xvdg</p>
    </td>
    </tr>
    <tr id="row57521478102622"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p30815488102652"><a name="p30815488102652"></a><a name="p30815488102652"></a>xvdh</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p13026569102652"><a name="p13026569102652"></a><a name="p13026569102652"></a>xvdh</p>
    </td>
    </tr>
    <tr id="row16821092102622"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p34018989102652"><a name="p34018989102652"></a><a name="p34018989102652"></a>xvdi</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p4074750102652"><a name="p4074750102652"></a><a name="p4074750102652"></a>xvdi</p>
    </td>
    </tr>
    <tr id="row44080360102622"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p17703441102652"><a name="p17703441102652"></a><a name="p17703441102652"></a>xvdj</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p24692629102652"><a name="p24692629102652"></a><a name="p24692629102652"></a>xvdj</p>
    </td>
    </tr>
    <tr id="row41411196102622"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p15751024102652"><a name="p15751024102652"></a><a name="p15751024102652"></a>xvdk</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p764576102652"><a name="p764576102652"></a><a name="p764576102652"></a>xvdk</p>
    </td>
    </tr>
    <tr id="row34889124102631"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p20505175102652"><a name="p20505175102652"></a><a name="p20505175102652"></a>xvdl</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p50306493102652"><a name="p50306493102652"></a><a name="p50306493102652"></a>xvdl</p>
    </td>
    </tr>
    <tr id="row48077717102631"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p31994075102652"><a name="p31994075102652"></a><a name="p31994075102652"></a>xvdm</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p41383314102652"><a name="p41383314102652"></a><a name="p41383314102652"></a>xvdm</p>
    </td>
    </tr>
    <tr id="row65977729102631"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p36555994102652"><a name="p36555994102652"></a><a name="p36555994102652"></a>xvdn</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p8245514102652"><a name="p8245514102652"></a><a name="p8245514102652"></a>xvdn</p>
    </td>
    </tr>
    <tr id="row35001738102631"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p38291255102652"><a name="p38291255102652"></a><a name="p38291255102652"></a>xvdo</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p14583964102652"><a name="p14583964102652"></a><a name="p14583964102652"></a>xvdo</p>
    </td>
    </tr>
    <tr id="row33010075102631"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p28509473102652"><a name="p28509473102652"></a><a name="p28509473102652"></a>xvdp</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p27565956102652"><a name="p27565956102652"></a><a name="p27565956102652"></a>xvdp</p>
    </td>
    </tr>
    <tr id="row13673019104238"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p3316577110430"><a name="p3316577110430"></a><a name="p3316577110430"></a>xvdq</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p2678866210434"><a name="p2678866210434"></a><a name="p2678866210434"></a>xvdq</p>
    </td>
    </tr>
    <tr id="row29955953104238"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1865648710430"><a name="p1865648710430"></a><a name="p1865648710430"></a>xvdr</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p25566510434"><a name="p25566510434"></a><a name="p25566510434"></a>xvdr</p>
    </td>
    </tr>
    <tr id="row8154855104238"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p4458881510430"><a name="p4458881510430"></a><a name="p4458881510430"></a>xvds</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p5216221710434"><a name="p5216221710434"></a><a name="p5216221710434"></a>xvds</p>
    </td>
    </tr>
    <tr id="row34522295104238"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p2455622210430"><a name="p2455622210430"></a><a name="p2455622210430"></a>xvdt</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p4263981910434"><a name="p4263981910434"></a><a name="p4263981910434"></a>xvdt</p>
    </td>
    </tr>
    <tr id="row31650820104238"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p5052831110430"><a name="p5052831110430"></a><a name="p5052831110430"></a>xvdu</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p1302452110434"><a name="p1302452110434"></a><a name="p1302452110434"></a>xvdu</p>
    </td>
    </tr>
    <tr id="row65530809104238"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p5948166910430"><a name="p5948166910430"></a><a name="p5948166910430"></a>xvdv</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p3252643010434"><a name="p3252643010434"></a><a name="p3252643010434"></a>xvdv</p>
    </td>
    </tr>
    <tr id="row19535177104238"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p981119610430"><a name="p981119610430"></a><a name="p981119610430"></a>xvdw</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p2233895710434"><a name="p2233895710434"></a><a name="p2233895710434"></a>xvdw</p>
    </td>
    </tr>
    <tr id="row52264303104238"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p3882251710430"><a name="p3882251710430"></a><a name="p3882251710430"></a>xvdx</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p4475517010434"><a name="p4475517010434"></a><a name="p4475517010434"></a>xvdx</p>
    </td>
    </tr>
    </tbody>
    </table>


