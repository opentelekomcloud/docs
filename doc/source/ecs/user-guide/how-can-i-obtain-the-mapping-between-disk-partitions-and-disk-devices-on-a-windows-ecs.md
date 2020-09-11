# How Can I Obtain the Mapping Between Disk Partitions and Disk Devices on a Windows ECS?<a name="EN-US_TOPIC_0087680813"></a>

This section uses an ECS running Windows Server 2008 R2 64bit as an example to describe how to obtain the mapping between disk partitions and disk devices.

1.  Log in to the Windows ECS.
2.  Click  **Start**  in the lower left corner of the desktop.
3.  Choose  **Control Panel**  \>  **Administrative Tools**  \>  **Computer Management**.
4.  In the navigation pane on the left, choose  **Storage**  \>  **Disk Management**.

    **Figure  1**  Disk Management<a name="fig63278226101115"></a>  
    ![](figures/disk-management-19.png "disk-management-19")

5.  Taking disk 1 marked in  [Figure 1](#fig63278226101115)  as an example, view the disk device for disk 1.
    1.  Right-click the gray area where disk 1 is located, as shown in the red box in  [Figure 1](#fig63278226101115).
    2.  Click  **Properties**.

        The  **SCSI Disk Device Properties**  dialog box is displayed, as shown in  [Figure 2](#fig22437283101545).

        **Figure  2**  Disk properties<a name="fig22437283101545"></a>  
        ![](figures/disk-properties.png "disk-properties")

    3.  Click the  **Details**  tab and set  **Property**  to  **Parent**.

        **Figure  3**  Disk device details<a name="fig2821199710173"></a>  
        ![](figures/disk-device-details.png "disk-device-details")

    4.  Record the digits following  **&**  in the parameter value, for example,  **51776**, which is the master and slave device number corresponding to the disk partition.
    5.  Obtain the disk device according to the information listed in  [Table 1](#table2257401020521).

        The disk device corresponding to  **51776**  is  **xvde**. The disk device used by disk 1 is xvde.

        **Table  1**  Mapping between disk partitions and disk devices

        <a name="table2257401020521"></a>
        <table><thead align="left"><tr id="row3849274020521"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p970281020521"><a name="p970281020521"></a><a name="p970281020521"></a>Master and Slave Device Number for a Disk Partition</p>
        </th>
        <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p4773015520521"><a name="p4773015520521"></a><a name="p4773015520521"></a>Disk Device</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row2691821520521"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p3450267120732"><a name="p3450267120732"></a><a name="p3450267120732"></a>51712</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p4325299020732"><a name="p4325299020732"></a><a name="p4325299020732"></a>xvda</p>
        </td>
        </tr>
        <tr id="row2027256120521"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p5737281420732"><a name="p5737281420732"></a><a name="p5737281420732"></a>51728</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p1668634720732"><a name="p1668634720732"></a><a name="p1668634720732"></a>xvdb</p>
        </td>
        </tr>
        <tr id="row5366127520521"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1764277420732"><a name="p1764277420732"></a><a name="p1764277420732"></a>51744</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p1977855520732"><a name="p1977855520732"></a><a name="p1977855520732"></a>xvdc</p>
        </td>
        </tr>
        <tr id="row3256032420521"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p5726985920732"><a name="p5726985920732"></a><a name="p5726985920732"></a>51760</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p834703520732"><a name="p834703520732"></a><a name="p834703520732"></a>xvdd</p>
        </td>
        </tr>
        <tr id="row5277246420521"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p4519097220732"><a name="p4519097220732"></a><a name="p4519097220732"></a>51776</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p3659014420732"><a name="p3659014420732"></a><a name="p3659014420732"></a>xvde</p>
        </td>
        </tr>
        <tr id="row400362392070"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p3199633320732"><a name="p3199633320732"></a><a name="p3199633320732"></a>51792</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p4156621520732"><a name="p4156621520732"></a><a name="p4156621520732"></a>xvdf</p>
        </td>
        </tr>
        <tr id="row633352432070"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p3567367620732"><a name="p3567367620732"></a><a name="p3567367620732"></a>51808</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p388661420732"><a name="p388661420732"></a><a name="p388661420732"></a>xvdg</p>
        </td>
        </tr>
        <tr id="row1351782070"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1476952420732"><a name="p1476952420732"></a><a name="p1476952420732"></a>51824</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p5548079220732"><a name="p5548079220732"></a><a name="p5548079220732"></a>xvdh</p>
        </td>
        </tr>
        <tr id="row2827831620521"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p4596186720732"><a name="p4596186720732"></a><a name="p4596186720732"></a>51840</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p3192378020732"><a name="p3192378020732"></a><a name="p3192378020732"></a>xvdi</p>
        </td>
        </tr>
        <tr id="row5750996020720"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p5276908720732"><a name="p5276908720732"></a><a name="p5276908720732"></a>51856</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p4643765420732"><a name="p4643765420732"></a><a name="p4643765420732"></a>xvdj</p>
        </td>
        </tr>
        <tr id="row5353100120720"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p3018259620732"><a name="p3018259620732"></a><a name="p3018259620732"></a>51872</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p2887118720732"><a name="p2887118720732"></a><a name="p2887118720732"></a>xvdk</p>
        </td>
        </tr>
        <tr id="row1042597020720"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p4202114320732"><a name="p4202114320732"></a><a name="p4202114320732"></a>51888</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p4826938420732"><a name="p4826938420732"></a><a name="p4826938420732"></a>xvdl</p>
        </td>
        </tr>
        <tr id="row1711351020720"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p2333650820732"><a name="p2333650820732"></a><a name="p2333650820732"></a>51904</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p1120903420732"><a name="p1120903420732"></a><a name="p1120903420732"></a>xvdm</p>
        </td>
        </tr>
        <tr id="row510996920720"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p5121369920732"><a name="p5121369920732"></a><a name="p5121369920732"></a>51920</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p5466891820732"><a name="p5466891820732"></a><a name="p5466891820732"></a>xvdn</p>
        </td>
        </tr>
        <tr id="row558482020720"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p5808556620732"><a name="p5808556620732"></a><a name="p5808556620732"></a>51936</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p731038620732"><a name="p731038620732"></a><a name="p731038620732"></a>xvdo</p>
        </td>
        </tr>
        <tr id="row1933641220720"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p2767143520732"><a name="p2767143520732"></a><a name="p2767143520732"></a>51952</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p2679376920732"><a name="p2679376920732"></a><a name="p2679376920732"></a>xvdp</p>
        </td>
        </tr>
        <tr id="row22290127103632"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p66393420103632"><a name="p66393420103632"></a><a name="p66393420103632"></a>268439552</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p9157974103632"><a name="p9157974103632"></a><a name="p9157974103632"></a>xvdq</p>
        </td>
        </tr>
        <tr id="row6676146103632"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p60085315103632"><a name="p60085315103632"></a><a name="p60085315103632"></a>268439808</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p35072375103632"><a name="p35072375103632"></a><a name="p35072375103632"></a>xvdr</p>
        </td>
        </tr>
        <tr id="row23614195103632"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p11201170103632"><a name="p11201170103632"></a><a name="p11201170103632"></a>268440064</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p34879610103632"><a name="p34879610103632"></a><a name="p34879610103632"></a>xvds</p>
        </td>
        </tr>
        <tr id="row31586991103632"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p15847469103632"><a name="p15847469103632"></a><a name="p15847469103632"></a>268440320</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p8576578103632"><a name="p8576578103632"></a><a name="p8576578103632"></a>xvdt</p>
        </td>
        </tr>
        <tr id="row3791880103632"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p34126925103632"><a name="p34126925103632"></a><a name="p34126925103632"></a>268440576</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p12817530103632"><a name="p12817530103632"></a><a name="p12817530103632"></a>xvdu</p>
        </td>
        </tr>
        <tr id="row29071593103632"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p60317750103632"><a name="p60317750103632"></a><a name="p60317750103632"></a>268440832</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p53899605103632"><a name="p53899605103632"></a><a name="p53899605103632"></a>xvdv</p>
        </td>
        </tr>
        <tr id="row52532677103632"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p3032052103632"><a name="p3032052103632"></a><a name="p3032052103632"></a>268441088</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p44269646103632"><a name="p44269646103632"></a><a name="p44269646103632"></a>xvdw</p>
        </td>
        </tr>
        <tr id="row21619288103632"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p60355865103632"><a name="p60355865103632"></a><a name="p60355865103632"></a>268441344</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p56986857103632"><a name="p56986857103632"></a><a name="p56986857103632"></a>xvdx</p>
        </td>
        </tr>
        </tbody>
        </table>



