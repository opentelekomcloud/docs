# Creating a Cluster<a name="dws_01_0019"></a>

To use DWS in the public cloud environment, you need to create a data warehouse cluster by specifying only the node flavor and scale. 

This section describes how to create a data warehouse cluster on the DWS management console.

## Preparations Before Creating a Cluster<a name="section15419130142012"></a>

-   The flavor of nodes in the cluster has been evaluated.

    Choose as many nodes as possible to ensure high-performance storage and computing capabilities for service applications based on service requirements. A node in a data warehouse cluster contains two DataNodes. The DataNode instance stores service data \(support for row-based, column-based, and hybrid storage\), executes the data query tasks, and returns the execution results.

-   A network access topology has been designed.

    Plan an appropriate AZ and configure the network to isolate the data warehouse cluster from other public cloud services based on the service application requirements.

-   Ensure that the number of available nodes meets the following conditions. Otherwise, the cluster cannot be created. In this case, click  **Increase quota**  to submit a work order and apply for higher node quota.
    -   The number of available nodes must be greater than or equal to three, because at least three nodes are required for creating a cluster. You can view the number of available nodes on the  **Cluster Management**  page.
    -   The number of nodes in the cluster to be created must be less than or equal to the number of available nodes.


## Creating a Cluster<a name="section19523079142249"></a>

1.  Log in to the management console at  [https://console.otc.t-systems.com/dws/](https://console.otc.t-systems.com/dws/).
2.  On the  **Cluster Management**  page, click  **Create DWS Cluster**.
3.  Select the  **Region**.

    **Table  1**  Region parameters

    <a name="table108461995918"></a>
    <table><thead align="left"><tr id="row11089193597"><th class="cellrowborder" valign="top" width="21.78%" id="mcps1.2.4.1.1"><p id="p12115219195917"><a name="p12115219195917"></a><a name="p12115219195917"></a><strong id="b29551244112357"><a name="b29551244112357"></a><a name="b29551244112357"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.47%" id="mcps1.2.4.1.2"><p id="p312571955912"><a name="p312571955912"></a><a name="p312571955912"></a><strong id="b5196504143335"><a name="b5196504143335"></a><a name="b5196504143335"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.75%" id="mcps1.2.4.1.3"><p id="p6135201920598"><a name="p6135201920598"></a><a name="p6135201920598"></a><strong id="b60793810112357"><a name="b60793810112357"></a><a name="b60793810112357"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8143819165910"><td class="cellrowborder" valign="top" width="21.78%" headers="mcps1.2.4.1.1 "><p id="p418216169501"><a name="p418216169501"></a><a name="p418216169501"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.47%" headers="mcps1.2.4.1.2 "><p id="p716213192595"><a name="p716213192595"></a><a name="p716213192595"></a>Select the actual region where the cluster nodes run. </p>
    <p id="p1479822031911"><a name="p1479822031911"></a><a name="p1479822031911"></a>For more information about AZs, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p1820114196592"><a name="p1820114196592"></a><a name="p1820114196592"></a>eu-de</p>
    </td>
    </tr>
    <tr id="row521517197596"><td class="cellrowborder" valign="top" width="21.78%" headers="mcps1.2.4.1.1 "><p id="p17939155916330"><a name="p17939155916330"></a><a name="p17939155916330"></a>AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.47%" headers="mcps1.2.4.1.2 "><p id="p172251819145914"><a name="p172251819145914"></a><a name="p172251819145914"></a>Select an AZ associated with the cluster region.</p>
    <p id="p162288199594"><a name="p162288199594"></a><a name="p162288199594"></a>An AZ contains one or more physical DCs. It has independent cooling, fire extinguishing, moisture-proof, and electricity facilities. Within an AZ, computing, network, storage, and other resources are logically divided into multiple clusters. AZs within a region are interconnected using high-speed optical fibers to realize cross-AZ high availability for the system.</p>
    <a name="ul204221759932"></a><a name="ul204221759932"></a>
    </td>
    <td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p1628816195595"><a name="p1628816195595"></a><a name="p1628816195595"></a>eu-de-01</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Configure the node-related parameters.

    >![](/images/icon-note.gif) **NOTE:**   
    >The number of nodes in a new cluster cannot exceed the quota that can be used by a user or 32. If the node quota is insufficient, click  **Increase quota**  to submit a work order and apply for higher node quota.  

    **Figure  1**  View of configuring node-related parameters<a name="fig3550151115141"></a>  
    ![](figures/view-of-configuring-node-related-parameters.png "view-of-configuring-node-related-parameters")

    **Table  2**  Node configuration parameters

    <a name="table11569171131419"></a>
    <table><thead align="left"><tr id="row1858451161414"><th class="cellrowborder" valign="top" width="21.62%" id="mcps1.2.4.1.1"><p id="p859013118144"><a name="p859013118144"></a><a name="p859013118144"></a><strong id="b18455557143338"><a name="b18455557143338"></a><a name="b18455557143338"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.76%" id="mcps1.2.4.1.2"><p id="p16598111101411"><a name="p16598111101411"></a><a name="p16598111101411"></a><strong id="b2031400697"><a name="b2031400697"></a><a name="b2031400697"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.62%" id="mcps1.2.4.1.3"><p id="p10605111110145"><a name="p10605111110145"></a><a name="p10605111110145"></a><strong id="b171032388"><a name="b171032388"></a><a name="b171032388"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row361421141419"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="p4467319276"><a name="p4467319276"></a><a name="p4467319276"></a>Node Flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.2 "><p id="p56239110143"><a name="p56239110143"></a><a name="p56239110143"></a>Select vCPU and memory resources for the nodes in the cluster. <a href="#table111901234141316">Table 3</a> lists the node flavors supported by DWS.</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.62%" headers="mcps1.2.4.1.3 "><p id="p9172175111559"><a name="p9172175111559"></a><a name="p9172175111559"></a>dws.m3.xlarge</p>
    </td>
    </tr>
    <tr id="row4633711181419"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="p1263811191417"><a name="p1263811191417"></a><a name="p1263811191417"></a>Nodes</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.2 "><p id="p364381181414"><a name="p364381181414"></a><a name="p364381181414"></a>Specify the number of nodes in the cluster.</p>
    <p id="p1645121119149"><a name="p1645121119149"></a><a name="p1645121119149"></a>The number of nodes ranges from 3 to 32.</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.62%" headers="mcps1.2.4.1.3 "><p id="p186497115143"><a name="p186497115143"></a><a name="p186497115143"></a>3</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Flavor description

    <a name="table111901234141316"></a>
    <table><thead align="left"><tr id="row1222193461316"><th class="cellrowborder" valign="top" width="29.630000000000003%" id="mcps1.2.6.1.1"><p id="p1123813348130"><a name="p1123813348130"></a><a name="p1123813348130"></a><strong id="b571358716"><a name="b571358716"></a><a name="b571358716"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.94%" id="mcps1.2.6.1.2"><p id="p72462034201310"><a name="p72462034201310"></a><a name="p72462034201310"></a><strong id="b142834586"><a name="b142834586"></a><a name="b142834586"></a>vCPU Cores</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.45%" id="mcps1.2.6.1.3"><p id="p52541134191315"><a name="p52541134191315"></a><a name="p52541134191315"></a><strong id="b1053883782"><a name="b1053883782"></a><a name="b1053883782"></a>Memory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.97%" id="mcps1.2.6.1.4"><p id="p326853417138"><a name="p326853417138"></a><a name="p326853417138"></a><strong id="b1824025355"><a name="b1824025355"></a><a name="b1824025355"></a>Disk Size</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.01%" id="mcps1.2.6.1.5"><p id="p12761734181310"><a name="p12761734181310"></a><a name="p12761734181310"></a><strong id="b1092947105"><a name="b1092947105"></a><a name="b1092947105"></a>Disk Type</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3331203413136"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.6.1.1 "><p id="p1434743418139"><a name="p1434743418139"></a><a name="p1434743418139"></a>dws.m1.xlarge.ultrahigh</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.94%" headers="mcps1.2.6.1.2 "><p id="p734753411319"><a name="p734753411319"></a><a name="p734753411319"></a>4</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.45%" headers="mcps1.2.6.1.3 "><p id="p43541134111313"><a name="p43541134111313"></a><a name="p43541134111313"></a>32 GB</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.97%" headers="mcps1.2.6.1.4 "><p id="p11362103419130"><a name="p11362103419130"></a><a name="p11362103419130"></a>256 GB</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.01%" headers="mcps1.2.6.1.5 "><p id="p1817754218151"><a name="p1817754218151"></a><a name="p1817754218151"></a>General-purpose generation I, SSD</p>
    </td>
    </tr>
    <tr id="row9424123491313"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.6.1.1 "><p id="p194331534151311"><a name="p194331534151311"></a><a name="p194331534151311"></a>dws.d1.xlarge</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.94%" headers="mcps1.2.6.1.2 "><p id="p19440334161320"><a name="p19440334161320"></a><a name="p19440334161320"></a>4</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.45%" headers="mcps1.2.6.1.3 "><p id="p744913347132"><a name="p744913347132"></a><a name="p744913347132"></a>32 GB</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.97%" headers="mcps1.2.6.1.4 "><p id="p13457123411317"><a name="p13457123411317"></a><a name="p13457123411317"></a>1.68 TB</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.01%" headers="mcps1.2.6.1.5 "><p id="p6427158171519"><a name="p6427158171519"></a><a name="p6427158171519"></a>Local disk (HDD)</p>
    </td>
    </tr>
    <tr id="row0471103412137"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.6.1.1 "><p id="p1947111349132"><a name="p1947111349132"></a><a name="p1947111349132"></a>dws.d2.15xlarge</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.94%" headers="mcps1.2.6.1.2 "><p id="p1648863412133"><a name="p1648863412133"></a><a name="p1648863412133"></a>60</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.45%" headers="mcps1.2.6.1.3 "><p id="p748814343136"><a name="p748814343136"></a><a name="p748814343136"></a>540 GB</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.97%" headers="mcps1.2.6.1.4 "><p id="p650453412137"><a name="p650453412137"></a><a name="p650453412137"></a>13.41 TB</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.01%" headers="mcps1.2.6.1.5 "><p id="p1224351611164"><a name="p1224351611164"></a><a name="p1224351611164"></a>Disk-intensive generation II (KVM), local disk (HDD)</p>
    </td>
    </tr>
    <tr id="row20518834101316"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.6.1.1 "><p id="p16526123471319"><a name="p16526123471319"></a><a name="p16526123471319"></a>dws.d2.xlarge</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.94%" headers="mcps1.2.6.1.2 "><p id="p153493410139"><a name="p153493410139"></a><a name="p153493410139"></a>4</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.45%" headers="mcps1.2.6.1.3 "><p id="p195431134141317"><a name="p195431134141317"></a><a name="p195431134141317"></a>32 GB</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.97%" headers="mcps1.2.6.1.4 "><p id="p1755013481312"><a name="p1755013481312"></a><a name="p1755013481312"></a>1.68 TB</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.01%" headers="mcps1.2.6.1.5 "><p id="p1624452811612"><a name="p1624452811612"></a><a name="p1624452811612"></a>Disk-intensive generation II (KVM), local disk (HDD)</p>
    </td>
    </tr>
    <tr id="row18660183401313"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.6.1.1 "><p id="p1966733471316"><a name="p1966733471316"></a><a name="p1966733471316"></a>dws.m3.xlarge</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.94%" headers="mcps1.2.6.1.2 "><p id="p8675034131315"><a name="p8675034131315"></a><a name="p8675034131315"></a>4</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.45%" headers="mcps1.2.6.1.3 "><p id="p16753343135"><a name="p16753343135"></a><a name="p16753343135"></a>32 GB</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.97%" headers="mcps1.2.6.1.4 "><p id="p1268318346136"><a name="p1268318346136"></a><a name="p1268318346136"></a>160 GB</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.01%" headers="mcps1.2.6.1.5 "><p id="p16510123115163"><a name="p16510123115163"></a><a name="p16510123115163"></a>General-purpose generation III (KVM), SSD</p>
    </td>
    </tr>
    </tbody>
    </table>

      

5.  Configure cluster-related parameters.

    **Figure  2**  View of configuring the cluster<a name="fig14469944499"></a>  
    ![](figures/view-of-configuring-the-cluster.png "view-of-configuring-the-cluster")

    **Table  4**  Parameter description

    <a name="table175013003914"></a>
    <table><thead align="left"><tr id="row9384101317142"><th class="cellrowborder" valign="top" width="21.62%" id="mcps1.2.4.1.1"><p id="p1438491319146"><a name="p1438491319146"></a><a name="p1438491319146"></a><strong id="b5863685143335"><a name="b5863685143335"></a><a name="b5863685143335"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.76%" id="mcps1.2.4.1.2"><p id="p1138413133148"><a name="p1138413133148"></a><a name="p1138413133148"></a><strong id="b684577358"><a name="b684577358"></a><a name="b684577358"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.62%" id="mcps1.2.4.1.3"><p id="p038431301410"><a name="p038431301410"></a><a name="p038431301410"></a><strong id="b18263659143335"><a name="b18263659143335"></a><a name="b18263659143335"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13844134148"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="p133848139147"><a name="p133848139147"></a><a name="p133848139147"></a>Cluster Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.2 "><p id="p338481314148"><a name="p338481314148"></a><a name="p338481314148"></a>Set the name of the data warehouse cluster. </p>
    <p id="p9384181313143"><a name="p9384181313143"></a><a name="p9384181313143"></a>Enter 4 to 64 characters. Only case-insensitive letters, digits, hyphens (-), and underscores (_) are allowed. The value must start with a letter. </p>
    </td>
    <td class="cellrowborder" valign="top" width="24.62%" headers="mcps1.2.4.1.3 "><p id="p6386191361418"><a name="p6386191361418"></a><a name="p6386191361418"></a>dws-demo</p>
    </td>
    </tr>
    <tr id="row13861713161413"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="p183862131145"><a name="p183862131145"></a><a name="p183862131145"></a>Cluster Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.2 "><p id="p138631318140"><a name="p138631318140"></a><a name="p138631318140"></a>Display the version of the database instance installed in the cluster.</p>
    <div class="note" id="note1138691316140"><a name="note1138691316140"></a><a name="note1138691316140"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p6386151315146"><a name="p6386151315146"></a><a name="p6386151315146"></a>The version number is the default one and, as of publication, cannot be changed.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="24.62%" headers="mcps1.2.4.1.3 "><p id="p16386181319148"><a name="p16386181319148"></a><a name="p16386181319148"></a>1.2.1</p>
    </td>
    </tr>
    <tr id="row14386171315141"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="p038613131142"><a name="p038613131142"></a><a name="p038613131142"></a>Default Database</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.2 "><p id="p1386191331411"><a name="p1386191331411"></a><a name="p1386191331411"></a>The default database name of the cluster is <span class="parmvalue" id="parmvalue1174220013392"><a name="parmvalue1174220013392"></a><a name="parmvalue1174220013392"></a><b>postgres</b></span>. </p>
    <div class="note" id="note738761313143"><a name="note738761313143"></a><a name="note738761313143"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p6387121361412"><a name="p6387121361412"></a><a name="p6387121361412"></a>This name cannot be changed.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="24.62%" headers="mcps1.2.4.1.3 "><p id="p1838751311416"><a name="p1838751311416"></a><a name="p1838751311416"></a>-</p>
    </td>
    </tr>
    <tr id="row73871513111412"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="p143871813151417"><a name="p143871813151417"></a><a name="p143871813151417"></a>Administrator Account</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.2 "><p id="p8387191381414"><a name="p8387191381414"></a><a name="p8387191381414"></a>Set the administrator name of the database.</p>
    <p id="p1438712134144"><a name="p1438712134144"></a><a name="p1438712134144"></a>The administrator username must:</p>
    <a name="ul1838791391412"></a><a name="ul1838791391412"></a><ul id="ul1838791391412"><li>Consist of lowercase letters, digits, or underscores.</li><li>Start with a lowercase letter or an underscore.</li><li>Contain 1 to 63 characters.</li><li>Cannot be a keyword of the DWS database. For details about the keywords of the DWS database, see section <span class="filepath" id="filepath6792184255817"><a name="filepath6792184255817"></a><a name="filepath6792184255817"></a><b>Keyword</b></span> in the <em id="i2084564732611"><a name="i2084564732611"></a><a name="i2084564732611"></a>Data Warehouse Service Database Developer Guide</em>.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="24.62%" headers="mcps1.2.4.1.3 "><p id="p438751319147"><a name="p438751319147"></a><a name="p438751319147"></a>dbadmin</p>
    </td>
    </tr>
    <tr id="row10387113111411"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="p163871139146"><a name="p163871139146"></a><a name="p163871139146"></a>Administrator Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.2 "><p id="p11387121313141"><a name="p11387121313141"></a><a name="p11387121313141"></a>Set the password of the database administrator account.</p>
    <div class="p" id="p16387141311415"><a name="p16387141311415"></a><a name="p16387141311415"></a>The password complexity requirements are as follows:<a name="ul13418111318144"></a><a name="ul13418111318144"></a><ul id="ul13418111318144"><li>Consists of 8 to 32 characters.</li><li>Cannot be the same as the username or the username written in reverse order.</li><li>Must contain at least 3 of the following character types: uppercase letters, lowercase letters, digits, and special characters ~!@#%^&amp;*()-_=+|[{}];:,&lt;.&gt;/?</li><li>Passes the weak password check.</li></ul>
    </div>
    <div class="note" id="note5387181341412"><a name="note5387181341412"></a><a name="note5387181341412"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p192851549957"><a name="p192851549957"></a><a name="p192851549957"></a>Change the password regularly and keep it secure.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="24.62%" headers="mcps1.2.4.1.3 "><p id="p14387213131410"><a name="p14387213131410"></a><a name="p14387213131410"></a>Dws2018demo!</p>
    </td>
    </tr>
    <tr id="row14387141315145"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="p338717134144"><a name="p338717134144"></a><a name="p338717134144"></a>Confirm Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.2 "><p id="p238720135147"><a name="p238720135147"></a><a name="p238720135147"></a>Enter the database administrator password again.</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.62%" headers="mcps1.2.4.1.3 "><p id="p8387213111412"><a name="p8387213111412"></a><a name="p8387213111412"></a>Dws2018demo!</p>
    </td>
    </tr>
    <tr id="row938781319144"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="p73871513131416"><a name="p73871513131416"></a><a name="p73871513131416"></a>Database Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.2 "><p id="p9387513171414"><a name="p9387513171414"></a><a name="p9387513171414"></a>Set the port used when the client or application connects to the database in the cluster.</p>
    <p id="p15387101320146"><a name="p15387101320146"></a><a name="p15387101320146"></a>The port ranges from 8000 to 10000.</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.62%" headers="mcps1.2.4.1.3 "><p id="p43872130149"><a name="p43872130149"></a><a name="p43872130149"></a>8000</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Configure network parameters.

    **Figure  3**  View of configuring the network<a name="fig393813695215"></a>  
    ![](figures/view-of-configuring-the-network.png "view-of-configuring-the-network")

    **Table  5**  Network parameters

    <a name="table16335123418419"></a>
    <table><thead align="left"><tr id="row3540181381411"><th class="cellrowborder" valign="top" width="21.62%" id="mcps1.2.4.1.1"><p id="p1540313181410"><a name="p1540313181410"></a><a name="p1540313181410"></a><strong id="b40793968144420"><a name="b40793968144420"></a><a name="b40793968144420"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.76%" id="mcps1.2.4.1.2"><p id="p7540313141414"><a name="p7540313141414"></a><a name="p7540313141414"></a><strong id="b729327017213"><a name="b729327017213"></a><a name="b729327017213"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.62%" id="mcps1.2.4.1.3"><p id="p65405135141"><a name="p65405135141"></a><a name="p65405135141"></a><strong id="b19079452144420"><a name="b19079452144420"></a><a name="b19079452144420"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1540171331413"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="p454011136140"><a name="p454011136140"></a><a name="p454011136140"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.2 "><p id="p17540313111411"><a name="p17540313111411"></a><a name="p17540313111411"></a>Specify a virtual private network for nodes in a cluster to isolate networks of different services.</p>
    <p id="p0540151317149"><a name="p0540151317149"></a><a name="p0540151317149"></a>If you create a data warehouse cluster for the first time and have not configured the VPC, click <span class="uicontrol" id="uicontrol4891633712228"><a name="uicontrol4891633712228"></a><a name="uicontrol4891633712228"></a><b>View VPC</b></span>. On the VPC management console that is displayed, create a new VPC that satisfies your needs.</p>
    <p id="p165411113171414"><a name="p165411113171414"></a><a name="p165411113171414"></a>For details about how to create a VPC, see section <span class="filepath" id="filepath1055331361414"><a name="filepath1055331361414"></a><a name="filepath1055331361414"></a><b>Creating a VPC</b></span> in the <i><cite id="cite92ace8dc725e4eb6b9051e53943f28d3134156"><a name="cite92ace8dc725e4eb6b9051e53943f28d3134156"></a><a name="cite92ace8dc725e4eb6b9051e53943f28d3134156"></a>Virtual Private Cloud User Guide</cite></i>.</p>
    <p id="p16541181391415"><a name="p16541181391415"></a><a name="p16541181391415"></a>After selecting a VPC from the drop-down list, click <span class="uicontrol" id="uicontrol733273424119"><a name="uicontrol733273424119"></a><a name="uicontrol733273424119"></a><b>View VPC</b></span> to enter the VPC management console and view the detailed information about the VPC.</p>
    <p id="p3541151301418"><a name="p3541151301418"></a><a name="p3541151301418"></a>You can click <a name="image15726345135818"></a><a name="image15726345135818"></a><span><img id="image15726345135818" src="figures/icon-dws-refresh.png"></span> to refresh the options in the <span class="parmname" id="parmname571132519124912"><a name="parmname571132519124912"></a><a name="parmname571132519124912"></a><b>VPC</b></span> drop-down list.</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.62%" headers="mcps1.2.4.1.3 "><p id="p95412131144"><a name="p95412131144"></a><a name="p95412131144"></a>vpc-dws</p>
    </td>
    </tr>
    <tr id="row1054151312147"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="p1454151321416"><a name="p1454151321416"></a><a name="p1454151321416"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.2 "><p id="p15411513171415"><a name="p15411513171415"></a><a name="p15411513171415"></a>Specify a subnet for the VPC.</p>
    <p id="p3541131311143"><a name="p3541131311143"></a><a name="p3541131311143"></a>A subnet provides dedicated network resources that are isolated from other networks, improving network security.</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.62%" headers="mcps1.2.4.1.3 "><p id="p554111135141"><a name="p554111135141"></a><a name="p554111135141"></a>subnet-dws</p>
    </td>
    </tr>
    <tr id="row85411713171419"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="p3541513121416"><a name="p3541513121416"></a><a name="p3541513121416"></a>Security Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.2 "><p id="p4541171351418"><a name="p4541171351418"></a><a name="p4541171351418"></a>Specify a security group for the VPC.</p>
    <p id="p1254191311411"><a name="p1254191311411"></a><a name="p1254191311411"></a>A security group restricts access rules to enhance security when DWS and other services access each other.</p>
    <a name="ul244311341000"></a><a name="ul244311341000"></a><ul id="ul244311341000"><li>Automatically create a security group.<p id="p71561188314"><a name="p71561188314"></a><a name="p71561188314"></a>If <span class="parmvalue" id="parmvalue1788460266105252"><a name="parmvalue1788460266105252"></a><a name="parmvalue1788460266105252"></a><b>Automatic creation</b></span> is selected, the system automatically creates a default security group. This option is selected by default.</p>
    <p id="p754151312143"><a name="p754151312143"></a><a name="p754151312143"></a>The rule of the default security group is as follows: The outbound allows all access requests, while the inbound is only open to the database port that you set to connect to the data warehouse cluster.</p>
    <p id="p1754111341418"><a name="p1754111341418"></a><a name="p1754111341418"></a>The format of the default security group's name is dws-&lt;<em id="i151231534105623"><a name="i151231534105623"></a><a name="i151231534105623"></a>cluster name</em>&gt;-&lt;<em id="i783314206105623"><a name="i783314206105623"></a><a name="i783314206105623"></a>database port of the data warehouse cluster</em>&gt;, for example, <strong id="b842352706105715"><a name="b842352706105715"></a><a name="b842352706105715"></a>dws-dws-demo-8000</strong>.</p>
    <div class="note" id="note4217101371018"><a name="note4217101371018"></a><a name="note4217101371018"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1221741315103"><a name="p1221741315103"></a><a name="p1221741315103"></a>If the quotas of the security group and the security group rule are insufficient, an error message will be displayed after you submit the cluster creation application. Select an existing group and retry.</p>
    </div></div>
    </li><li>Manually create and configure a security group.<p id="p1467461213432"><a name="p1467461213432"></a><a name="p1467461213432"></a>You can also log in to the VPC management console to manually create a security group. Then, go back to the page for creating data warehouse clusters, click the <a name="image1734202181112"></a><a name="image1734202181112"></a><span><img id="image1734202181112" src="figures/icon-dws-refresh.png"></span> button next to the <span class="parmname" id="parmname1140614311489"><a name="parmname1140614311489"></a><a name="parmname1140614311489"></a><b>Security Group</b></span> drop-down list to refresh the page, and select the new security group.</p>
    <p id="p1483411371220"><a name="p1483411371220"></a><a name="p1483411371220"></a>To enable the DWS client to connect to the cluster, you need to add an inbound rule to the new security group to grant the access permission to the database port of the data warehouse cluster. An example of the inbound rule is as follows:</p>
    <a name="ul834751052511"></a><a name="ul834751052511"></a><ul id="ul834751052511"><li><strong id="b842352706111211"><a name="b842352706111211"></a><a name="b842352706111211"></a>Protocol</strong>: <strong id="b842352706111216"><a name="b842352706111216"></a><a name="b842352706111216"></a>TCP</strong></li><li><strong id="b2418462181044"><a name="b2418462181044"></a><a name="b2418462181044"></a>Port</strong>: <strong id="b40326830181048"><a name="b40326830181048"></a><a name="b40326830181048"></a>8000</strong> Use the database port set when creating the data warehouse cluster. This port is used for receiving client connections to DWS.</li><li><strong id="b842352706111337"><a name="b842352706111337"></a><a name="b842352706111337"></a>Source</strong>: Select <strong id="b842352706111342"><a name="b842352706111342"></a><a name="b842352706111342"></a>IP address</strong> and use the host IP address of the client, for example, <strong id="b842352706111428"><a name="b842352706111428"></a><a name="b842352706111428"></a>192.168.0.10/32</strong>.</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="24.62%" headers="mcps1.2.4.1.3 "><p id="p165411013191418"><a name="p165411013191418"></a><a name="p165411013191418"></a>Automatic creation</p>
    </td>
    </tr>
    <tr id="row138021539133519"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="p23911422201011"><a name="p23911422201011"></a><a name="p23911422201011"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.2 "><p id="p11377151183513"><a name="p11377151183513"></a><a name="p11377151183513"></a>Specify whether users can use a client to connect to a cluster's database over the Internet. The following methods are supported:</p>
    <a name="ul43786513356"></a><a name="ul43786513356"></a><ul id="ul43786513356"><li><span class="parmvalue" id="parmvalue1938535118354"><a name="parmvalue1938535118354"></a><a name="parmvalue1938535118354"></a><b>Do not use</b></span>: The EIP is not required.</li><li><span class="parmname" id="parmname11211185125913"><a name="parmname11211185125913"></a><a name="parmname11211185125913"></a><b>Automatically assign</b></span>: Users specify the bandwidth of the EIP and the system automatically assigns an EIP that exclusively uses bandwidth to each cluster so that users can use the EIP to access the cluster over the Internet.</li><li><span class="parmname" id="parmname1287810333579"><a name="parmname1287810333579"></a><a name="parmname1287810333579"></a><b>Specify</b></span>: A specified EIP is bound to the cluster. If no available EIPs are displayed in the drop-down list, click <span class="uicontrol" id="uicontrol844472198201519"><a name="uicontrol844472198201519"></a><a name="uicontrol844472198201519"></a><b>Create EIP</b></span> to go to the <strong id="b84235270611450"><a name="b84235270611450"></a><a name="b84235270611450"></a>Elastic IP</strong> page and create an EIP that satisfies your needs. You can set the bandwidth as needed.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="24.62%" headers="mcps1.2.4.1.3 "><p id="p32366214217"><a name="p32366214217"></a><a name="p32366214217"></a>Automatically assign</p>
    </td>
    </tr>
    <tr id="row68992056153010"><td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.4.1.1 "><p id="p169001456153010"><a name="p169001456153010"></a><a name="p169001456153010"></a>Bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.2 "><p id="p490011568308"><a name="p490011568308"></a><a name="p490011568308"></a>When <span class="parmname" id="parmname13682105414266"><a name="parmname13682105414266"></a><a name="parmname13682105414266"></a><b>EIP</b></span> is set to <span class="parmname" id="parmname117174712268"><a name="parmname117174712268"></a><a name="parmname117174712268"></a><b>Automatically assign</b></span>, you specify the bandwidth of the used EIP, which ranges from 1 Mbit/s to 100 Mbit/s.</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.62%" headers="mcps1.2.4.1.3 "><p id="p1290019565304"><a name="p1290019565304"></a><a name="p1290019565304"></a>50 Mbit/s</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Select either of the following options for  **Advanced Settings**:
    -   **Default**: Indicates that the following advanced settings use the default configurations.
        -   **Parameter Group**: The default database parameter group  **Default-Parameter-Group-DWS**  is associated with the cluster.
        -   **Tag**: By default, no tag is added to the cluster.
        -   **Automated Snapshot**: By default, the policy for automatically generating cluster snapshots is disabled.

    -   **Custom**: If you select this option, set the following advanced settings:

        **Figure  4**  Custom advanced settings<a name="fig543116212020"></a>  
        ![](figures/custom-advanced-settings.png "custom-advanced-settings")

        -   **Parameter Group**

            A parameter group is a set of database parameters. You need to select a parameter group from the drop-down list and associate it with the cluster during cluster creation. You can select the default parameter group  **Default-Parameter-Group-DWS**  or a customized parameter group.

            For details about parameter groups, see section  [Managing Parameter Groups](managing-parameter-groups.md).

        -   **Tag**

            A tag is a key-value pair used to identify a cluster. For details about the keys and values, see  [Table 6](#table59181441134820).

            For more information about tags, see section  [Tagging Overview](tagging-overview.md).

            **Table  6**  Tag parameters

            <a name="table59181441134820"></a>
            <table><thead align="left"><tr id="dws_01_0105_row17486121763113"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.1"><p id="dws_01_0105_p12486181715313"><a name="dws_01_0105_p12486181715313"></a><a name="dws_01_0105_p12486181715313"></a><strong id="dws_01_0105_b84235270617387"><a name="dws_01_0105_b84235270617387"></a><a name="dws_01_0105_b84235270617387"></a>Parameter</strong></p>
            </th>
            <th class="cellrowborder" valign="top" width="71%" id="mcps1.2.4.1.2"><p id="dws_01_0105_p1191704514113"><a name="dws_01_0105_p1191704514113"></a><a name="dws_01_0105_p1191704514113"></a><strong id="dws_01_0105_b842352706101627"><a name="dws_01_0105_b842352706101627"></a><a name="dws_01_0105_b842352706101627"></a>Description</strong></p>
            </th>
            <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.3"><p id="dws_01_0105_p18486151713117"><a name="dws_01_0105_p18486151713117"></a><a name="dws_01_0105_p18486151713117"></a><strong id="dws_01_0105_b60793810112357"><a name="dws_01_0105_b60793810112357"></a><a name="dws_01_0105_b60793810112357"></a>Example Value</strong></p>
            </th>
            </tr>
            </thead>
            <tbody><tr id="dws_01_0105_row11486131733111"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="dws_01_0105_p1433134915503"><a name="dws_01_0105_p1433134915503"></a><a name="dws_01_0105_p1433134915503"></a>Tag key</p>
            </td>
            <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.2 "><p id="dws_01_0105_p4183104918156"><a name="dws_01_0105_p4183104918156"></a><a name="dws_01_0105_p4183104918156"></a>You can:</p>
            <a name="dws_01_0105_ul149381653121514"></a><a name="dws_01_0105_ul149381653121514"></a><ul id="dws_01_0105_ul149381653121514"><li>Select a predefined tag key or an existing resource tag key from the drop-down list of the text box.<div class="note" id="dws_01_0105_note354311061312"><a name="dws_01_0105_note354311061312"></a><a name="dws_01_0105_note354311061312"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="dws_01_0105_p19473813185311"><a name="dws_01_0105_p19473813185311"></a><a name="dws_01_0105_p19473813185311"></a>To add a predefined tag, you need to create one on TMS and select it from the drop-down list of <span class="parmname" id="dws_01_0105_parmname890218564101210"><a name="dws_01_0105_parmname890218564101210"></a><a name="dws_01_0105_parmname890218564101210"></a><b>Tag key</b></span>. You can click <span class="uicontrol" id="dws_01_0105_uicontrol941000013191930"><a name="dws_01_0105_uicontrol941000013191930"></a><a name="dws_01_0105_uicontrol941000013191930"></a><b>View predefined tags</b></span> to enter the <span class="wintitle" id="dws_01_0105_wintitle72946297619202"><a name="dws_01_0105_wintitle72946297619202"></a><a name="dws_01_0105_wintitle72946297619202"></a><b>Predefined Tag</b></span> page of TMS. Then, click <span class="uicontrol" id="dws_01_0105_uicontrol1385059717192149"><a name="dws_01_0105_uicontrol1385059717192149"></a><a name="dws_01_0105_uicontrol1385059717192149"></a><b>Create Tag</b></span> to create a predefined tag. For details, see section <span class="filepath" id="dws_01_0105_filepath79624027716543"><a name="dws_01_0105_filepath79624027716543"></a><a name="dws_01_0105_filepath79624027716543"></a><b>Creating Predefined Tags</b></span> in the <em id="dws_01_0105_i842352697104314"><a name="dws_01_0105_i842352697104314"></a><a name="dws_01_0105_i842352697104314"></a>Tag Management Service User Guide</em>.</p>
            </div></div>
            </li></ul>
            <a name="dws_01_0105_ul154819568159"></a><a name="dws_01_0105_ul154819568159"></a><ul id="dws_01_0105_ul154819568159"><li>Enter a tag key in the text box. A tag key can contain a maximum of 36 Unicode characters, which cannot be null. The first and last characters cannot be spaces.<p id="dws_01_0105_p1740919129378"><a name="dws_01_0105_p1740919129378"></a><a name="dws_01_0105_p1740919129378"></a>Contain only uppercase letters (A to Z), lowercase letters (a to z), digits (0-9), hyphens (-), and underscores (_).</p>
            <div class="p" id="dws_01_0105_p922511632019"><a name="dws_01_0105_p922511632019"></a><a name="dws_01_0105_p922511632019"></a><div class="note" id="dws_01_0105_note206991233134612"><a name="dws_01_0105_note206991233134612"></a><a name="dws_01_0105_note206991233134612"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="dws_01_0105_p10699733104619"><a name="dws_01_0105_p10699733104619"></a><a name="dws_01_0105_p10699733104619"></a>The key name must be unique in the same cluster.</p>
            </div></div>
            </div>
            </li></ul>
            </td>
            <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.3 "><p id="dws_01_0105_p848641718314"><a name="dws_01_0105_p848641718314"></a><a name="dws_01_0105_p848641718314"></a>tagkey01</p>
            </td>
            </tr>
            <tr id="dws_01_0105_row19486151715318"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="dws_01_0105_p1548761710317"><a name="dws_01_0105_p1548761710317"></a><a name="dws_01_0105_p1548761710317"></a>Tag value</p>
            </td>
            <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.2 "><p id="dws_01_0105_p34521618101419"><a name="dws_01_0105_p34521618101419"></a><a name="dws_01_0105_p34521618101419"></a>You can:</p>
            <a name="dws_01_0105_ul12885203215142"></a><a name="dws_01_0105_ul12885203215142"></a><ul id="dws_01_0105_ul12885203215142"><li>Select a predefined tag value or resource tag value from the drop-down list of the text box.</li><li>Enter a tag value in the text box. A tag key can contain a maximum of 43 Unicode characters, which can be null. The first and last characters cannot be spaces.<p id="dws_01_0105_p1110383711457"><a name="dws_01_0105_p1110383711457"></a><a name="dws_01_0105_p1110383711457"></a>Contain only uppercase letters (A to Z), lowercase letters (a to z), digits (0-9), hyphens (-), and underscores (_).</p>
            </li></ul>
            </td>
            <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.3 "><p id="dws_01_0105_p14487201712310"><a name="dws_01_0105_p14487201712310"></a><a name="dws_01_0105_p14487201712310"></a>value01</p>
            </td>
            </tr>
            </tbody>
            </table>

        -   **Automated Snapshot**

            Click  **Automated Snapshot**  to enable or disable the automatic snapshot policy for the cluster. After the automated snapshot policy is enabled, the system automatically creates snapshots based on the preset time and period.

            ![](figures/icon-button2.png)  indicates that the policy is enabled.

            ![](figures/icon-dws-off.jpg)  indicates that the policy is disabled \(default\).

            When it is enabled, configure the following parameters:

            **Table  7**  Parameter description

            <a name="table34471941398"></a>
            <table><thead align="left"><tr id="dws_01_0089_row555312181040"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.3.1.1"><p id="dws_01_0089_p1055313187410"><a name="dws_01_0089_p1055313187410"></a><a name="dws_01_0089_p1055313187410"></a><strong id="dws_01_0089_b84235270692541"><a name="dws_01_0089_b84235270692541"></a><a name="dws_01_0089_b84235270692541"></a>Parameter</strong></p>
            </th>
            <th class="cellrowborder" valign="top" width="72%" id="mcps1.2.3.1.2"><p id="dws_01_0089_p1755314181848"><a name="dws_01_0089_p1755314181848"></a><a name="dws_01_0089_p1755314181848"></a><strong id="dws_01_0089_b842352706181449"><a name="dws_01_0089_b842352706181449"></a><a name="dws_01_0089_b842352706181449"></a>Description</strong></p>
            </th>
            </tr>
            </thead>
            <tbody><tr id="dws_01_0089_row155542181842"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="dws_01_0089_p04771730104018"><a name="dws_01_0089_p04771730104018"></a><a name="dws_01_0089_p04771730104018"></a>Retention Days</p>
            </td>
            <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="dws_01_0089_p19553121817411"><a name="dws_01_0089_p19553121817411"></a><a name="dws_01_0089_p19553121817411"></a>It is used to set the retention days of the snapshots that are automatically created. The value ranges from 1 to 10 days.</p>
            <div class="note" id="dws_01_0089_note125545181345"><a name="dws_01_0089_note125545181345"></a><a name="dws_01_0089_note125545181345"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="dws_01_0089_p555319181643"><a name="dws_01_0089_p555319181643"></a><a name="dws_01_0089_p555319181643"></a>You cannot delete the snapshots that are automatically created. The system automatically deletes these snapshots when their retention duration expires.</p>
            </div></div>
            </td>
            </tr>
            <tr id="dws_01_0089_row7556518248"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="dws_01_0089_p7399234124010"><a name="dws_01_0089_p7399234124010"></a><a name="dws_01_0089_p7399234124010"></a>Start Time</p>
            </td>
            <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="dws_01_0089_p14556918545"><a name="dws_01_0089_p14556918545"></a><a name="dws_01_0089_p14556918545"></a>It is used to set the time when the automatic snapshot creation begins. The time must be set to an integer. The automatic creation task is triggered within one hour after the creation start time you set. </p>
            </td>
            </tr>
            <tr id="dws_01_0089_row35566181148"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="dws_01_0089_p20322183715408"><a name="dws_01_0089_p20322183715408"></a><a name="dws_01_0089_p20322183715408"></a>Execution Period</p>
            </td>
            <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="dws_01_0089_p9556121819416"><a name="dws_01_0089_p9556121819416"></a><a name="dws_01_0089_p9556121819416"></a>It is used to set the automatic snapshot creation cycle.</p>
            </td>
            </tr>
            </tbody>
            </table>


8.  Click  **Create Now**. The  **Details**  page is displayed.

    >![](/images/icon-note.gif) **NOTE:**   
    >If the number of applied nodes, vCPU \(cores\), or memory \(GB\) exceed the user's remaining quota, a warning dialog box is displayed indicating insufficient quota and displaying the detailed remaining quota and the current quota application information. In this case, you can click  **Increase quota**  in the warning dialog box to submit a work order and apply for higher node quota.  
    >For details about quota, see  [What Is User Quota?](what-is-user-quota.md).  

9.  Click  **Submit**.

    After the submission,  **Cluster Status**  of the newly created cluster is  **Creating**. Wait several minutes. Clusters in the  **Available**  state are ready for use.


