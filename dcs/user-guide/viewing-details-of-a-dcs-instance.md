# Viewing Details of a DCS Instance<a name="EN-US_TOPIC_0237964715"></a>

## Scenario<a name="section1590600"></a>

On the DCS console, you can view details about a DCS instance.

## Procedure<a name="section14315403"></a>

1.  Log in to the management console.
2.  Click![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose  **Database**  \>  **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  On the  **Cache Manager**  page,  Search for DCS instances using any of the following methods:

    -   Search by keyword.

        Enter a keyword to search.

    -   Select attributes and enter their keywords to search.

        Currently, you can search by name, ID, IP address, AZ, status, and instance type.

    For more information on how to search, click the question mark to the right of the search box.

6.  On the DCS instance list, click the name of the chosen DCS instance to display more details about it.

    **Table  1**  Parameters on the DCS instance details page

    <a name="table44346036"></a>
    <table><thead align="left"><tr id="row31746690"><th class="cellrowborder" valign="top" width="15.308469153084694%" id="mcps1.2.4.1.1"><p id="p21345065"><a name="p21345065"></a><a name="p21345065"></a>Category</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.407959204079592%" id="mcps1.2.4.1.2"><p id="p51228725"><a name="p51228725"></a><a name="p51228725"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.28357164283572%" id="mcps1.2.4.1.3"><p id="p55886094"><a name="p55886094"></a><a name="p55886094"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row30479771"><td class="cellrowborder" rowspan="13" valign="top" width="15.308469153084694%" headers="mcps1.2.4.1.1 "><p id="p52942405"><a name="p52942405"></a><a name="p52942405"></a>Instance Information</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.2.4.1.2 "><p id="p60476403"><a name="p60476403"></a><a name="p60476403"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.28357164283572%" headers="mcps1.2.4.1.3 "><p id="p66750478"><a name="p66750478"></a><a name="p66750478"></a>Name of the chosen instance. To modify the instance name, click the<a name="image158791713115915"></a><a name="image158791713115915"></a><span><img id="image158791713115915" src="figures/icon-edit.png"></span> icon.</p>
    </td>
    </tr>
    <tr id="row38079613"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p64549801"><a name="p64549801"></a><a name="p64549801"></a>Status</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p61151353"><a name="p61151353"></a><a name="p61151353"></a>Status of the chosen DCS instance.</p>
    </td>
    </tr>
    <tr id="row13491266"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p19050756"><a name="p19050756"></a><a name="p19050756"></a>Cache Engine</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p66716254"><a name="p66716254"></a><a name="p66716254"></a>Cache engine used by the chosen instance. Currently, only Redis 3.0 is supported.</p>
    </td>
    </tr>
    <tr id="row63575380"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p49332166"><a name="p49332166"></a><a name="p49332166"></a>Instance Type</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p36482533"><a name="p36482533"></a><a name="p36482533"></a>Type of the chosen instance. Currently, three types are supported: single-node, master/standby, and cluster.</p>
    </td>
    </tr>
    <tr id="row59907344"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p20656733"><a name="p20656733"></a><a name="p20656733"></a>Specification (GB)</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p62582666"><a name="p62582666"></a><a name="p62582666"></a>Specification of the chosen instance.</p>
    </td>
    </tr>
    <tr id="row26373084"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p55845053"><a name="p55845053"></a><a name="p55845053"></a>Used/Available Memory (MB)</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p27155410"><a name="p27155410"></a><a name="p27155410"></a>The used memory space and maximum allowed memory space of the chosen instance.</p>
    <p id="p43072099"><a name="p43072099"></a><a name="p43072099"></a>The used memory space includes:</p>
    <a name="ul52104579"></a><a name="ul52104579"></a><ul id="ul52104579"><li>Size of data stored on the DCS instance</li><li>Size of Redis-server buffers (including client buffer and repli-backlog) and internal data structures</li></ul>
    </td>
    </tr>
    <tr id="row621706"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p50358210"><a name="p50358210"></a><a name="p50358210"></a>Time Window</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p52483186"><a name="p52483186"></a><a name="p52483186"></a>Time range for any scheduled maintenance activities to occur for cache nodes of this DCS instance. To modify the maintenance time window, click the<a name="image1145514502013"></a><a name="image1145514502013"></a><span><img id="image1145514502013" src="figures/icon-edit.png"></span> icon next to <strong id="b23279683"><a name="b23279683"></a><a name="b23279683"></a>Time Window</strong>.</p>
    </td>
    </tr>
    <tr id="row8190559"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p59455556"><a name="p59455556"></a><a name="p59455556"></a>ID</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p51170717"><a name="p51170717"></a><a name="p51170717"></a>ID of the chosen instance.</p>
    </td>
    </tr>
    <tr id="row57883273"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p58033516"><a name="p58033516"></a><a name="p58033516"></a>Connection Address</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p3094327"><a name="p3094327"></a><a name="p3094327"></a>IP address and port number of the chosen instance.</p>
    </td>
    </tr>
    <tr id="row27848947"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p41172271"><a name="p41172271"></a><a name="p41172271"></a>Created</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p46619622"><a name="p46619622"></a><a name="p46619622"></a>Time at which the chosen instance was created.</p>
    </td>
    </tr>
    <tr id="row16923420"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p28619802"><a name="p28619802"></a><a name="p28619802"></a>Run</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p36502600"><a name="p36502600"></a><a name="p36502600"></a>Time at which the chosen instance entered the <strong id="b60087944"><a name="b60087944"></a><a name="b60087944"></a>Running</strong> state.</p>
    </td>
    </tr>
    <tr id="row3920590"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p49132373"><a name="p49132373"></a><a name="p49132373"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p20299268"><a name="p20299268"></a><a name="p20299268"></a>Description of the selected instance. To modify the description, click the<a name="image74776414219"></a><a name="image74776414219"></a><span><img id="image74776414219" src="figures/icon-edit.png"></span> icon.</p>
    </td>
    </tr>
    <tr id="row33628036"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p39516413"><a name="p39516413"></a><a name="p39516413"></a>Monitoring metrics</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p46712854"><a name="p46712854"></a><a name="p46712854"></a>Monitoring metrics of the chosen instance. Click the <strong id="b17203154910172"><a name="b17203154910172"></a><a name="b17203154910172"></a>View Metrics</strong> icon to switch to the Cloud Eye console on which monitoring metrics of the selected DCS instance are displayed.</p>
    </td>
    </tr>
    <tr id="row25644791"><td class="cellrowborder" rowspan="4" valign="top" width="15.308469153084694%" headers="mcps1.2.4.1.1 "><p id="p63962185"><a name="p63962185"></a><a name="p63962185"></a>Network</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.2.4.1.2 "><p id="p13554483"><a name="p13554483"></a><a name="p13554483"></a>AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.28357164283572%" headers="mcps1.2.4.1.3 "><p id="p24171358"><a name="p24171358"></a><a name="p24171358"></a>Availability zone in which the cache node running the chosen instance resides.</p>
    </td>
    </tr>
    <tr id="row16215635"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p38398082"><a name="p38398082"></a><a name="p38398082"></a>Security Group</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p23236933"><a name="p23236933"></a><a name="p23236933"></a>Security group that controls access to the chosen instance. To modify the security group, click the<a name="image147501537838"></a><a name="image147501537838"></a><span><img id="image147501537838" src="figures/icon-edit.png"></span> icon next to <strong id="b3143429"><a name="b3143429"></a><a name="b3143429"></a>Security Group</strong>.</p>
    </td>
    </tr>
    <tr id="row28290863"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p9858548"><a name="p9858548"></a><a name="p9858548"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p60344938"><a name="p60344938"></a><a name="p60344938"></a>VPC in which the chosen instance resides.</p>
    </td>
    </tr>
    <tr id="row6233535"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p35154304"><a name="p35154304"></a><a name="p35154304"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p28926407"><a name="p28926407"></a><a name="p28926407"></a>Subnet in which the chosen instance resides.</p>
    </td>
    </tr>
    </tbody>
    </table>


