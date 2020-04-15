# Can Multiple Disks Be Attached to an ECS?<a name="EN-US_TOPIC_0018073215"></a>

Yes. Disk functions have been upgraded recently. The ECSs created after the disk function upgrade can be attached with up to 60 disks.

-   When creating an ECS, you can add 24 disks to it.
-   After an ECS is created, up to 60 disks can be attached to it. For details, see  [Table 1](#table132723712109).

    **Table  1**  Numbers of disks that can be attached to newly created ECSs

    <a name="table132723712109"></a>
    <table><thead align="left"><tr id="row02721979101"><th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.6.1.1"><p id="p027217761015"><a name="p027217761015"></a><a name="p027217761015"></a>ECS Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.6.1.2"><p id="p917894151219"><a name="p917894151219"></a><a name="p917894151219"></a>Maximum VBD Disks</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.6.1.3"><p id="p152727719108"><a name="p152727719108"></a><a name="p152727719108"></a>Maximum SCSI Disks</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.6.1.4"><p id="p12723714105"><a name="p12723714105"></a><a name="p12723714105"></a>Maximum Local Disks</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.584158415841586%" id="mcps1.2.6.1.5"><p id="p6373121871215"><a name="p6373121871215"></a><a name="p6373121871215"></a>Constraint</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row92722781013"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.6.1.1 "><p id="p19272177171019"><a name="p19272177171019"></a><a name="p19272177171019"></a>Xen</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.6.1.2 "><p id="p327217161014"><a name="p327217161014"></a><a name="p327217161014"></a>60</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.6.1.3 "><p id="p1727287171014"><a name="p1727287171014"></a><a name="p1727287171014"></a>59</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.6.1.4 "><p id="p4272187101010"><a name="p4272187101010"></a><a name="p4272187101010"></a>59</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.584158415841586%" headers="mcps1.2.6.1.5 "><p id="p627207101011"><a name="p627207101011"></a><a name="p627207101011"></a>VBD disks + SCSI disks + Local disks ≤ 60</p>
    </td>
    </tr>
    <tr id="row132721977109"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.6.1.1 "><p id="p827212711020"><a name="p827212711020"></a><a name="p827212711020"></a>KVM (excepting D2 ECSs)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.6.1.2 "><p id="p132721174105"><a name="p132721174105"></a><a name="p132721174105"></a>24</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.6.1.3 "><p id="p192721675101"><a name="p192721675101"></a><a name="p192721675101"></a>59</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.6.1.4 "><p id="p1427216719100"><a name="p1427216719100"></a><a name="p1427216719100"></a>59</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.584158415841586%" headers="mcps1.2.6.1.5 "><a name="ul2906196141610"></a><a name="ul2906196141610"></a><ul id="ul2906196141610"><li>VBD disks + SCSI disks + Local disks ≤ 60</li><li>SCSI disks + Local disks ≤ 59</li></ul>
    </td>
    </tr>
    <tr id="row927215717107"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.6.1.1 "><p id="p122725791017"><a name="p122725791017"></a><a name="p122725791017"></a>D2</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.6.1.2 "><p id="p152726711019"><a name="p152726711019"></a><a name="p152726711019"></a>24</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.6.1.3 "><p id="p82725711108"><a name="p82725711108"></a><a name="p82725711108"></a>30</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.6.1.4 "><p id="p1827218718109"><a name="p1827218718109"></a><a name="p1827218718109"></a>30</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.584158415841586%" headers="mcps1.2.6.1.5 "><a name="ul112430493112"></a><a name="ul112430493112"></a><ul id="ul112430493112"><li>VBD disks + SCSI disks + Local disks ≤ 60</li><li>SCSI disks + Local disks ≤ 59</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   The system disk of an ECS is of VBD type. Therefore, the maximum number of SCSI and local disks is 59.  
    >-   For a D2 ECS, its local disks use two SCSI controllers, indicating that 30 SCSI drive letters are used. Therefore, a maximum of 30 SCSI disks can be attached to a D2 ECS.  


The maximum number of disks attached to an ECS that is created before the disk function upgrade remains unchanged, as shown in  [Table 2](#table560419017214).

**Table  2**  Numbers of disks that can be attached to existing ECSs

<a name="table560419017214"></a>
<table><thead align="left"><tr id="row6604130162112"><th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.6.1.1"><p id="p4131938142112"><a name="p4131938142112"></a><a name="p4131938142112"></a>ECS Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.6.1.2"><p id="p1513133811212"><a name="p1513133811212"></a><a name="p1513133811212"></a>Maximum VBD Disks</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.6.1.3"><p id="p181311438122113"><a name="p181311438122113"></a><a name="p181311438122113"></a>Maximum SCSI Disks</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.6.1.4"><p id="p181312038112118"><a name="p181312038112118"></a><a name="p181312038112118"></a>Maximum Local Disks</p>
</th>
<th class="cellrowborder" valign="top" width="41.41414141414141%" id="mcps1.2.6.1.5"><p id="p19146103818212"><a name="p19146103818212"></a><a name="p19146103818212"></a>Constraint</p>
</th>
</tr>
</thead>
<tbody><tr id="row1860480112111"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.6.1.1 "><p id="p15636044182114"><a name="p15636044182114"></a><a name="p15636044182114"></a>Xen</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.6.1.2 "><p id="p1960410182120"><a name="p1960410182120"></a><a name="p1960410182120"></a>60</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.6.1.3 "><p id="p146044012211"><a name="p146044012211"></a><a name="p146044012211"></a>59</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.6.1.4 "><p id="p14604105212"><a name="p14604105212"></a><a name="p14604105212"></a>59</p>
</td>
<td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.6.1.5 "><p id="p106049018217"><a name="p106049018217"></a><a name="p106049018217"></a>VBD disks + SCSI disks + Local disks ≤ 60</p>
</td>
</tr>
<tr id="row1060413042110"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.6.1.1 "><p id="p17652154482116"><a name="p17652154482116"></a><a name="p17652154482116"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.6.1.2 "><p id="p106048016214"><a name="p106048016214"></a><a name="p106048016214"></a>24</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.6.1.3 "><p id="p1260416011216"><a name="p1260416011216"></a><a name="p1260416011216"></a>23</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.6.1.4 "><p id="p239139133411"><a name="p239139133411"></a><a name="p239139133411"></a>59</p>
</td>
<td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.6.1.5 "><p id="p1360415014219"><a name="p1360415014219"></a><a name="p1360415014219"></a>VBD disks + SCSI disks ≤ 24</p>
</td>
</tr>
</tbody>
</table>

To attach 60 disks, enable advanced disk. For details, see  [Enabling Advanced Disk](enabling-advanced-disk.md).

## How Can I Check Whether an ECS Is Created Before or After the Disk Function Upgrade?<a name="section137641439201"></a>

1.  Log in to management console.
2.  Under  **Computing**, click  **Elastic Cloud Server**.
3.  Click the name of the target ECS. The page providing details about the ECS is displayed.
4.  Click the  **Disks**  tab.
5.  Check the number of disks that can be attached to the ECS to determine the total number of disks.
    -   If the total number of disks that can be attached is 24 \(including the system disk\), the ECS is created before the disk function upgrade. In such a case, you can enable advanced disk as prompted so that up to 60 disks can be attached to the ECS. For details, see  [Enabling Advanced Disk](enabling-advanced-disk.md).
    -   If the total number of disks that can be attached is 60 \(including the system disk\), the ECS is created after the disk function upgrade.


