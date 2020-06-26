# Resizing a Cluster<a name="EN-US_TOPIC_0172486188"></a>

## Function<a name="section2925263114112"></a>

This API is used to manually scale out or scale in Core or Task nodes in a cluster that has been created. After an MRS cluster is created, the number of Master nodes cannot be adjusted. That is, Master nodes cannot be scaled in or out. This API is incompatible with Sahara.

Only clusters in the  **Running**  state can be scaled out or in.

## URI<a name="section52142445114112"></a>

-   Format

    PUT /v1.1/\{project\_id\}/cluster\_infos/\{cluster\_id\}

-   Parameter description

    **Table  1**  URI parameter description

    <a name="table41315249114112"></a>
    <table><thead align="left"><tr id="row60032614114112"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p30803602114112"><a name="p30803602114112"></a><a name="p30803602114112"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p12063801114112"><a name="p12063801114112"></a><a name="p12063801114112"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p37643845114112"><a name="p37643845114112"></a><a name="p37643845114112"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row27185353142450"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p54529999142450"><a name="p54529999142450"></a><a name="p54529999142450"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p54853805142450"><a name="p54853805142450"></a><a name="p54853805142450"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p13973260142450"><a name="p13973260142450"></a><a name="p13973260142450"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row29252638114112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p20653483114112"><a name="p20653483114112"></a><a name="p20653483114112"></a>cluster_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p62319445114112"><a name="p62319445114112"></a><a name="p62319445114112"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p14710275114112"><a name="p14710275114112"></a><a name="p14710275114112"></a>Cluster ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section65283615114112"></a>

**Table  2**  Request parameter description

<a name="table19445385114112"></a>
<table><thead align="left"><tr id="row1790422114112"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p10806517114112"><a name="p10806517114112"></a><a name="p10806517114112"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p2912680114112"><a name="p2912680114112"></a><a name="p2912680114112"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p34600536114112"><a name="p34600536114112"></a><a name="p34600536114112"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p51180012114112"><a name="p51180012114112"></a><a name="p51180012114112"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row51940301114112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p46414818114112"><a name="p46414818114112"></a><a name="p46414818114112"></a>service_id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1503891114112"><a name="p1503891114112"></a><a name="p1503891114112"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p54706378114112"><a name="p54706378114112"></a><a name="p54706378114112"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p5242971143043"><a name="p5242971143043"></a><a name="p5242971143043"></a>Service ID</p>
<p id="p85664451112"><a name="p85664451112"></a><a name="p85664451112"></a>Reserve the parameter for extending APIs. You do not need to set the parameter.</p>
</td>
</tr>
<tr id="row18284370114112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4638978114112"><a name="p4638978114112"></a><a name="p4638978114112"></a>plan_id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p40212947114112"><a name="p40212947114112"></a><a name="p40212947114112"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p36023276114112"><a name="p36023276114112"></a><a name="p36023276114112"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p39399911143043"><a name="p39399911143043"></a><a name="p39399911143043"></a>Plan ID</p>
<p id="p1293515312119"><a name="p1293515312119"></a><a name="p1293515312119"></a>Reserve the parameter for extending APIs. You do not need to set the parameter.</p>
</td>
</tr>
<tr id="row21403053114112"><td class="cellrowborder" colspan="4" valign="top" headers="mcps1.2.5.1.1 mcps1.2.5.1.2 mcps1.2.5.1.3 mcps1.2.5.1.4 "><p id="p55925731114112"><a name="p55925731114112"></a><a name="p55925731114112"></a><strong id="b4794803095120"><a name="b4794803095120"></a><a name="b4794803095120"></a>parameters</strong></p>
</td>
</tr>
<tr id="row96444520052"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p6455462620155"><a name="p6455462620155"></a><a name="p6455462620155"></a>order_id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p484210368556"><a name="p484210368556"></a><a name="p484210368556"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1886541520155"><a name="p1886541520155"></a><a name="p1886541520155"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p5170365220155"><a name="p5170365220155"></a><a name="p5170365220155"></a>Order ID obtained by the system during scale-out or scale-in. You do not need to set the parameter.</p>
</td>
</tr>
<tr id="row379372720056"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4389012920155"><a name="p4389012920155"></a><a name="p4389012920155"></a>scale_type</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p6543955220155"><a name="p6543955220155"></a><a name="p6543955220155"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p6611238420155"><a name="p6611238420155"></a><a name="p6611238420155"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><a name="ul5350290520155"></a><a name="ul5350290520155"></a><ul id="ul5350290520155"><li>scale_in: cluster scale-in</li><li>scale_out: cluster scale-out</li></ul>
</td>
</tr>
<tr id="row4709391120059"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p905339020155"><a name="p905339020155"></a><a name="p905339020155"></a>node_id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p6223601520155"><a name="p6223601520155"></a><a name="p6223601520155"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p795249320155"><a name="p795249320155"></a><a name="p795249320155"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p4017220720155"><a name="p4017220720155"></a><a name="p4017220720155"></a>ID of the newly added or removed node. The parameter value is fixed to <strong id="b29051354193713"><a name="b29051354193713"></a><a name="b29051354193713"></a>node_orderadd</strong>. The ID of a newly added or removed node includes <strong id="b18819104910381"><a name="b18819104910381"></a><a name="b18819104910381"></a>node_orderadd</strong>, for example, <strong id="b185575711391"><a name="b185575711391"></a><a name="b185575711391"></a>node-orderadd-TBvSr.com</strong>.</p>
</td>
</tr>
<tr id="row307600151034"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p84046841034"><a name="p84046841034"></a><a name="p84046841034"></a>node_group</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p96907931034"><a name="p96907931034"></a><a name="p96907931034"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p467567501034"><a name="p467567501034"></a><a name="p467567501034"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><div class="p" id="p292004201034"><a name="p292004201034"></a><a name="p292004201034"></a>Node group to be scaled out or in<a name="ul32513041103128"></a><a name="ul32513041103128"></a><ul id="ul32513041103128"><li>If the value of <strong id="b1019744333912"><a name="b1019744333912"></a><a name="b1019744333912"></a>node_group</strong> is <strong id="b134910489391"><a name="b134910489391"></a><a name="b134910489391"></a>core_node_default_group</strong>, the node group is a Core node group.</li><li>If the value of <strong id="b6949227104017"><a name="b6949227104017"></a><a name="b6949227104017"></a>node_group</strong> is <strong id="b69795326403"><a name="b69795326403"></a><a name="b69795326403"></a>task_node_default_group</strong>, the node group is a Task node group.</li></ul>
</div>
<p id="p37442890101023"><a name="p37442890101023"></a><a name="p37442890101023"></a>If it is left blank, the default value <strong id="b13154182720411"><a name="b13154182720411"></a><a name="b13154182720411"></a>core_node_default_group</strong> is used.</p>
</td>
</tr>
<tr id="row5791272619467"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p5145248619467"><a name="p5145248619467"></a><a name="p5145248619467"></a>task_node_info</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p56323100194641"><a name="p56323100194641"></a><a name="p56323100194641"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p56024715194641"><a name="p56024715194641"></a><a name="p56024715194641"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p5133168319467"><a name="p5133168319467"></a><a name="p5133168319467"></a>Task node specifications. For more parameter description, see <a href="#table629219569398">Table 3</a>.</p>
<a name="ul8020525195052"></a><a name="ul8020525195052"></a><ul id="ul8020525195052"><li>When the number of Task nodes is <strong id="b76411567429"><a name="b76411567429"></a><a name="b76411567429"></a>0</strong>, this parameter is used to specify Task node specifications.</li><li>When the number of Task nodes is greater than <strong id="b1117154435"><a name="b1117154435"></a><a name="b1117154435"></a>0</strong>, this parameter is unavailable.</li></ul>
</td>
</tr>
<tr id="row925607920135"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p2607476920155"><a name="p2607476920155"></a><a name="p2607476920155"></a>instances</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p3168158220155"><a name="p3168158220155"></a><a name="p3168158220155"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1607133920155"><a name="p1607133920155"></a><a name="p1607133920155"></a>String/Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p2671006420155"><a name="p2671006420155"></a><a name="p2671006420155"></a>Number of nodes to be added or removed</p>
<a name="ul3906399020155"></a><a name="ul3906399020155"></a><ul id="ul3906399020155"><li>The maximum number of nodes to be added is 500 minus the number of Core and Task nodes. For example, the current number of Core nodes is 3, the number of nodes to be added must be less than or equal to 497.<p id="p1006658720155"><a name="p1006658720155"></a><a name="p1006658720155"></a>A maximum of 500 Core and Task nodes are supported by default. If more than 500 Core and Task nodes are required, contact technical support engineers or call a background API to modify the database.</p>
</li><li>Nodes can be deleted for cluster scale-out when the number of Core nodes is greater than 3 or the number of Task nodes is greater than 0. For example, if there are 5 Core nodes and 5 Task nodes in a cluster, only 2 (5 minus 3) Core nodes are available for deletion and 5 or fewer than 5 Task nodes can be deleted.</li></ul>
</td>
</tr>
<tr id="row4757201215719"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p17783192325712"><a name="p17783192325712"></a><a name="p17783192325712"></a>skip_bootstrap_scripts</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p67831423145718"><a name="p67831423145718"></a><a name="p67831423145718"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p147851323105719"><a name="p147851323105719"></a><a name="p147851323105719"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p10785122313579"><a name="p10785122313579"></a><a name="p10785122313579"></a>This parameter is valid only when a bootstrap action is configured during cluster creation and takes effect during scale-out. It indicates whether the bootstrap action specified during cluster creation is performed on nodes added during scale-out. The default value is <strong id="b11317141813562"><a name="b11317141813562"></a><a name="b11317141813562"></a>false</strong>, indicating that the bootstrap action is performed. MRS 1.7.2 or later supports this parameter.</p>
</td>
</tr>
<tr id="row1468114814288"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p75301135254"><a name="p75301135254"></a><a name="p75301135254"></a>scale_without_start</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p153010352516"><a name="p153010352516"></a><a name="p153010352516"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p13864202412515"><a name="p13864202412515"></a><a name="p13864202412515"></a>boolean</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1676101093516"><a name="p1676101093516"></a><a name="p1676101093516"></a>Whether to start components on the added nodes after cluster scale-out</p>
<a name="ul156684552518"></a><a name="ul156684552518"></a><ul id="ul156684552518"><li>true: Do not start components after scale-out</li><li>false: Start components after scale-out</li></ul>
<p id="p13228122014356"><a name="p13228122014356"></a><a name="p13228122014356"></a>This parameter is valid only in MRS 1.7.2 or later.</p>
</td>
</tr>
<tr id="row13864195573820"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p16865155518386"><a name="p16865155518386"></a><a name="p16865155518386"></a>server_ids</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p586605518384"><a name="p586605518384"></a><a name="p586605518384"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p12656164711125"><a name="p12656164711125"></a><a name="p12656164711125"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1567251310332"><a name="p1567251310332"></a><a name="p1567251310332"></a>ID list of Task nodes to be deleted during task node scale-in.</p>
<a name="ul1674611563315"></a><a name="ul1674611563315"></a><ul id="ul1674611563315"><li>This parameter does not take effect when <strong id="b9275653101112"><a name="b9275653101112"></a><a name="b9275653101112"></a>scale_type</strong> is set to <strong id="b1952083471210"><a name="b1952083471210"></a><a name="b1952083471210"></a>scale-out</strong>.</li><li>If <strong id="b129354471211"><a name="b129354471211"></a><a name="b129354471211"></a>scale_type</strong> is set to <strong id="b166151259151219"><a name="b166151259151219"></a><a name="b166151259151219"></a>scale-in</strong> and cannot be left blank, the system deletes the specified Task nodes.</li><li>When <strong id="b6397714111414"><a name="b6397714111414"></a><a name="b6397714111414"></a>scale_type</strong> is set to <strong id="b4376530151414"><a name="b4376530151414"></a><a name="b4376530151414"></a>scale-in</strong> and <strong id="b145522347146"><a name="b145522347146"></a><a name="b145522347146"></a>server_ids</strong> is left blank, the system automatically deletes the Task nodes based on the system rules.</li></ul>
</td>
</tr>
<tr id="row17742752114112"><td class="cellrowborder" colspan="4" valign="top" headers="mcps1.2.5.1.1 mcps1.2.5.1.2 mcps1.2.5.1.3 mcps1.2.5.1.4 "><p id="p27876844114112"><a name="p27876844114112"></a><a name="p27876844114112"></a><strong id="b5218011095435"><a name="b5218011095435"></a><a name="b5218011095435"></a>previous_values</strong></p>
</td>
</tr>
<tr id="row580648682027"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p2701443720235"><a name="p2701443720235"></a><a name="p2701443720235"></a>plan_id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p4068575220235"><a name="p4068575220235"></a><a name="p4068575220235"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p721165320235"><a name="p721165320235"></a><a name="p721165320235"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p4727301020235"><a name="p4727301020235"></a><a name="p4727301020235"></a>Reserve the parameter for extending APIs.</p>
<p id="p49500591155628"><a name="p49500591155628"></a><a name="p49500591155628"></a>You do not need to set the parameter.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **task\_node\_info**  parameter description

<a name="table629219569398"></a>
<table><thead align="left"><tr id="row19304156153916"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p6308115612399"><a name="p6308115612399"></a><a name="p6308115612399"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p183111656143913"><a name="p183111656143913"></a><a name="p183111656143913"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p123151656163910"><a name="p123151656163910"></a><a name="p123151656163910"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p15319165617397"><a name="p15319165617397"></a><a name="p15319165617397"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1348531874713"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p7485191816471"><a name="p7485191816471"></a><a name="p7485191816471"></a>node_size</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p01358124498"><a name="p01358124498"></a><a name="p01358124498"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p3133131244910"><a name="p3133131244910"></a><a name="p3133131244910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1229610391215"><a name="p1229610391215"></a><a name="p1229610391215"></a>Instance specifications of a Task node, for example, c2.2xlarge.linux.mrs</p>
<p id="ad01e9ad191694f6aa53b3afd86badcf4"><a name="ad01e9ad191694f6aa53b3afd86badcf4"></a><a name="ad01e9ad191694f6aa53b3afd86badcf4"></a>For details about instance specifications, see <a href="ecs-specifications-used-by-mrs.md">ECS Specifications Used by MRS</a>.</p>
</td>
</tr>
<tr id="row11323195610397"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p164051907406"><a name="p164051907406"></a><a name="p164051907406"></a>data_volume_type</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p569755411283"><a name="p569755411283"></a><a name="p569755411283"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p848551810474"><a name="p848551810474"></a><a name="p848551810474"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p17517192513260"><a name="p17517192513260"></a><a name="p17517192513260"></a>Data disk storage type of the Task node, supporting SATA, SAS, and SSD currently</p>
<a name="ul1451715253266"></a><a name="ul1451715253266"></a><ul id="ul1451715253266"><li>SATA: Common I/O</li><li>SAS: High I/O</li><li>SSD: Ultra-high I/O</li></ul>
</td>
</tr>
<tr id="row1333685617398"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1140380164017"><a name="p1140380164017"></a><a name="p1140380164017"></a>data_volume_count</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1912623210493"><a name="p1912623210493"></a><a name="p1912623210493"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1712617328491"><a name="p1712617328491"></a><a name="p1712617328491"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p13168356124914"><a name="p13168356124914"></a><a name="p13168356124914"></a>Number of data disks of a Task node</p>
<p id="p39809337500"><a name="p39809337500"></a><a name="p39809337500"></a>Value range: 1 to 10</p>
</td>
</tr>
<tr id="row13222100164117"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p15222604413"><a name="p15222604413"></a><a name="p15222604413"></a>data_volume_size</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p5200426104918"><a name="p5200426104918"></a><a name="p5200426104918"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p14200142618495"><a name="p14200142618495"></a><a name="p14200142618495"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p168701345134914"><a name="p168701345134914"></a><a name="p168701345134914"></a>Data disk storage space of a Task node</p>
<p id="p3870104513495"><a name="p3870104513495"></a><a name="p3870104513495"></a>Value range: 100 GB to 32,000 GB</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section41483722114112"></a>

**Response parameters**

[Table 4](#table8319691114112)  describes the response parameters.

**Table  4**  Response parameter description

<a name="table8319691114112"></a>
<table><thead align="left"><tr id="row39824979114112"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p4597879114112"><a name="p4597879114112"></a><a name="p4597879114112"></a><strong id="b204233013295"><a name="b204233013295"></a><a name="b204233013295"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p34804503114112"><a name="p34804503114112"></a><a name="p34804503114112"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p592484114112"><a name="p592484114112"></a><a name="p592484114112"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row47991225114112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p62084031114112"><a name="p62084031114112"></a><a name="p62084031114112"></a>result</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p44067044114112"><a name="p44067044114112"></a><a name="p44067044114112"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p12660774114112"><a name="p12660774114112"></a><a name="p12660774114112"></a>Operation result</p>
<a name="ul46838108114112"></a><a name="ul46838108114112"></a><ul id="ul46838108114112"><li>succeeded: The operation is successful.</li><li><a href="#table5548695114444">Table 6</a> describes the error codes returned upon operation failures.</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section494173511917"></a>

-   Example request

    Scaling out Core nodes:

    ```
    { 
        "service_id": "",  
        "plan_id": "",  
        "parameters": { 
            "order_id": "",  
            "scale_type": "scale_out",  
            "node_id": "node_orderadd",  
            "node_group": "core_node_default_group",
            "instances": "1",
           "skip_bootstrap_scripts":false,
           "scale_without_start":false
        },  
        "previous_values": { 
            "plan_id": "" 
        } 
    }
    ```

    Scaling out Task nodes when the number of the existing Task nodes is greater than zero:

    ```
    { 
        "service_id": "",  
        "plan_id": "",  
        "parameters": { 
            "order_id": "",  
            "scale_type": "scale_out",  
            "node_id": "node_orderadd",  
            "node_group": "task_node_default_group",
            "instances": "1",
            "skip_bootstrap_scripts":false,  
            "scale_without_start":false
        },  
        "previous_values": { 
            "plan_id": "" 
        } 
    }
    ```

    Scaling out Task nodes when the number of the existing Task nodes is zero:

    ```
    { 
        "service_id": "",  
        "plan_id": "",  
        "parameters": { 
            "order_id": "",  
            "scale_type": "scale_out",  
            "node_id": "node_orderadd",  
            "node_group": "task_node_default_group",
            "task_node_info": {
                      "node_size": "s1.xlarge.linux.mrs",
                      "data_volume_type":"SATA",
                      "data_volume_count":2,
                      "data_volume_size":200
                      },
            "instances": "1",  
            "scale_without_start":false
    
    
        },  
        "previous_values": { 
            "plan_id": "" 
        } 
    }
    ```

    Scaling in Core nodes:

    ```
    { 
        "service_id": "",  
        "plan_id": "",  
        "parameters": { 
            "order_id": "",  
            "scale_type": "scale_in",  
            "node_id": "node_orderadd",  
            "node_group": "core_node_default_group",
            "instances": "1"  
    
     
        },  
        "previous_values": { 
            "plan_id": "" 
        } 
    }
    ```

    Scaling in Task nodes:

    ```
    { 
        "service_id": "",  
        "plan_id": "",  
        "parameters": { 
            "order_id": "",  
            "scale_type": "scale_in",  
            "node_id": "node_orderadd",  
            "node_group": "task_node_default_group",
            "instances": "1"  
    
     
        },  
        "previous_values": { 
            "plan_id": "" 
        } 
    }
    ```

    The following is an example of a specified Task node scale-in:

    ```
    { 
        "service_id": "",  
        "plan_id": "",  
        "parameters": { 
            "order_id": "",  
            "scale_type": "scale_in",  
            "node_id": "node_orderadd",  
            "node_group": "task_node_default_group",
            "instances": "2",
            "server_ids": ["c9573435-7814-4b2c-9131-ad78b814414c", "a4951009-6a0f-4e7b-9c81-9d4bd1f8c537"]  
        },  
        "previous_values": { 
            "plan_id": "" 
        } 
    }
    ```


-   Example response

    ```
    {
        "result": "succeeded"
    }
    ```


## Status Code<a name="section53677969114112"></a>

-   [Table 5](#table60948494114112)  describes the status code of this API.

    **Table  5**  Status code

    <a name="table60948494114112"></a>
    <table><thead align="left"><tr id="row32904183114112"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p47993149114112"><a name="p47993149114112"></a><a name="p47993149114112"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p62239897114112"><a name="p62239897114112"></a><a name="p62239897114112"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8266864114112"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p65636268114112"><a name="p65636268114112"></a><a name="p65636268114112"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p14937525114112"><a name="p14937525114112"></a><a name="p14937525114112"></a>The Core or Task nodes have been successfully scaled out or in.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   [Table 6](#table5548695114444)  describes the error codes returned upon operation failures.

    **Table  6**  Error code

    <a name="table5548695114444"></a>
    <table><thead align="left"><tr id="row354818814444"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p20367198144415"><a name="p20367198144415"></a><a name="p20367198144415"></a>Error Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p10278616144415"><a name="p10278616144415"></a><a name="p10278616144415"></a>Message</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row338920616126"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p1039014661217"><a name="p1039014661217"></a><a name="p1039014661217"></a>12000001</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p113903641211"><a name="p113903641211"></a><a name="p113903641211"></a>Identity verification is invalid</p>
    </td>
    </tr>
    <tr id="row2775248914444"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p31629184144415"><a name="p31629184144415"></a><a name="p31629184144415"></a>12000002</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p2566243615843"><a name="p2566243615843"></a><a name="p2566243615843"></a>The parameter is invalid.</p>
    </td>
    </tr>
    <tr id="row455618081518"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p666277931518"><a name="p666277931518"></a><a name="p666277931518"></a>12000003</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4386421515843"><a name="p4386421515843"></a><a name="p4386421515843"></a>The cluster does not exist.</p>
    </td>
    </tr>
    <tr id="row50558415112"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p4095231915112"><a name="p4095231915112"></a><a name="p4095231915112"></a>12000009</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p1951166515843"><a name="p1951166515843"></a><a name="p1951166515843"></a>The method parameter is invalid.</p>
    </td>
    </tr>
    <tr id="row24029515153"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p1946391215153"><a name="p1946391215153"></a><a name="p1946391215153"></a>12000013</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p3564219515843"><a name="p3564219515843"></a><a name="p3564219515843"></a>Scale-in of cluster <i><span class="varname" id="varname6518406615933"><a name="varname6518406615933"></a><a name="varname6518406615933"></a>XX</span></i> failed.</p>
    </td>
    </tr>
    <tr id="row3081635115117"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p1309648715117"><a name="p1309648715117"></a><a name="p1309648715117"></a>12000014</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p5734685115843"><a name="p5734685115843"></a><a name="p5734685115843"></a>Scale-out of cluster <i><span class="varname" id="varname2951684115939"><a name="varname2951684115939"></a><a name="varname2951684115939"></a>XX</span></i> failed.</p>
    </td>
    </tr>
    <tr id="row2422751815149"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p1627192815149"><a name="p1627192815149"></a><a name="p1627192815149"></a>12000017</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p5283368015843"><a name="p5283368015843"></a><a name="p5283368015843"></a>Scale-out or scale-in is not allowed for clusters that are not in the <strong id="b9681114661011"><a name="b9681114661011"></a><a name="b9681114661011"></a>Running</strong> state.</p>
    </td>
    </tr>
    <tr id="row6474546915121"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p989163215121"><a name="p989163215121"></a><a name="p989163215121"></a>12000018</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p553800115843"><a name="p553800115843"></a><a name="p553800115843"></a>Scale-out or scale-in cannot be performed again because it is in progress.</p>
    </td>
    </tr>
    <tr id="row894492811213"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p109441528191215"><a name="p109441528191215"></a><a name="p109441528191215"></a>12000019</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p494411282126"><a name="p494411282126"></a><a name="p494411282126"></a>Failed to obtain hosts of the cluster.</p>
    </td>
    </tr>
    <tr id="row2031112315126"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p3458829815126"><a name="p3458829815126"></a><a name="p3458829815126"></a>12000028</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4940400515843"><a name="p4940400515843"></a><a name="p4940400515843"></a>The maximum number of Core nodes in a cluster is <i><span class="varname" id="varname49786155151054"><a name="varname49786155151054"></a><a name="varname49786155151054"></a>N</span></i>.</p>
    </td>
    </tr>
    <tr id="row3626742915135"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p5198063515135"><a name="p5198063515135"></a><a name="p5198063515135"></a>12000029</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p2416507615843"><a name="p2416507615843"></a><a name="p2416507615843"></a>Failed to obtain the quota.</p>
    </td>
    </tr>
    <tr id="row2120380015144"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p3978626015144"><a name="p3978626015144"></a><a name="p3978626015144"></a>12000030</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p795069915843"><a name="p795069915843"></a><a name="p795069915843"></a>The requested number of nodes in the cluster exceeds the available quota.</p>
    </td>
    </tr>
    <tr id="row4882755215140"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6271760115140"><a name="p6271760115140"></a><a name="p6271760115140"></a>12000031</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p5168179515843"><a name="p5168179515843"></a><a name="p5168179515843"></a>The requested number of vCPUs in the cluster exceeds the available quota.</p>
    </td>
    </tr>
    <tr id="row2789653215442"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p4502659115442"><a name="p4502659115442"></a><a name="p4502659115442"></a>12000032</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p863711315843"><a name="p863711315843"></a><a name="p863711315843"></a>The requested memory of the cluster exceeds the available quota.</p>
    </td>
    </tr>
    <tr id="row3294536315447"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p5132878315447"><a name="p5132878315447"></a><a name="p5132878315447"></a>12000033</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p6634488615843"><a name="p6634488615843"></a><a name="p6634488615843"></a>The requested number of disks in the cluster exceeds the available quota.</p>
    </td>
    </tr>
    <tr id="row33930181550"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p63990741550"><a name="p63990741550"></a><a name="p63990741550"></a>12000034</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p3653911215843"><a name="p3653911215843"></a><a name="p3653911215843"></a>The requested disk capacity of the cluster exceeds the available quota.</p>
    </td>
    </tr>
    <tr id="row439500831553"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p31869531553"><a name="p31869531553"></a><a name="p31869531553"></a>12000054</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p3965690215843"><a name="p3965690215843"></a><a name="p3965690215843"></a>The operation is not supported.</p>
    </td>
    </tr>
    <tr id="row19723174915129"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p07235494127"><a name="p07235494127"></a><a name="p07235494127"></a>12000067</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p3723149181219"><a name="p3723149181219"></a><a name="p3723149181219"></a>The cluster cannot be scaled out because its version is too early. Upgrade the cluster to the latest version.</p>
    </td>
    </tr>
    <tr id="row10629505122"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p36312508121"><a name="p36312508121"></a><a name="p36312508121"></a>12000068</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p8639501123"><a name="p8639501123"></a><a name="p8639501123"></a>The status of some nodes is not running in the cluster. Try again later.</p>
    </td>
    </tr>
    <tr id="row16344539181213"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p16593202110202"><a name="p16593202110202"></a><a name="p16593202110202"></a>12000121</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p1259313215206"><a name="p1259313215206"></a><a name="p1259313215206"></a>Scale-out is not allowed because the cluster has an unpaid order. Scale out the cluster again after you pay the order.</p>
    </td>
    </tr>
    <tr id="row4665542592215"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p652559869269"><a name="p652559869269"></a><a name="p652559869269"></a>MRS.101</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p6302598892543"><a name="p6302598892543"></a><a name="p6302598892543"></a>Your request could not be fulfilled because your quota is insufficient. Contact technical support to increase the quota.</p>
    </td>
    </tr>
    <tr id="row273178692215"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p585383229269"><a name="p585383229269"></a><a name="p585383229269"></a>MRS.102</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4348230092543"><a name="p4348230092543"></a><a name="p4348230092543"></a>The token cannot be null or invalid. Try again later or contact customer service.</p>
    </td>
    </tr>
    <tr id="row4059790292215"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p603085559269"><a name="p603085559269"></a><a name="p603085559269"></a>MRS.103</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p2321304192543"><a name="p2321304192543"></a><a name="p2321304192543"></a>Invalid request. Try again later or contact customer service.</p>
    </td>
    </tr>
    <tr id="row122128292215"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p86307109269"><a name="p86307109269"></a><a name="p86307109269"></a>MRS.104</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p1087352692543"><a name="p1087352692543"></a><a name="p1087352692543"></a>Insufficient resources. Try again later or contact customer service.</p>
    </td>
    </tr>
    <tr id="row6095817692215"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p506636729269"><a name="p506636729269"></a><a name="p506636729269"></a>MRS.105</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p795517592543"><a name="p795517592543"></a><a name="p795517592543"></a>Insufficient IP addresses in the existing subnet. Try again later or contact customer service.</p>
    </td>
    </tr>
    <tr id="row5045911592215"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p239418839269"><a name="p239418839269"></a><a name="p239418839269"></a>MRS.201</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p2796061492543"><a name="p2796061492543"></a><a name="p2796061492543"></a>Failed due to an ECS error. Try again later or contact customer service. (ECS: <em id="i143527504193"><a name="i143527504193"></a><a name="i143527504193"></a>xxxx</em>, ECS error information)</p>
    </td>
    </tr>
    <tr id="row623339092215"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p53281139269"><a name="p53281139269"></a><a name="p53281139269"></a>MRS.202</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4930191792543"><a name="p4930191792543"></a><a name="p4930191792543"></a>Failed due to an IAM error. Try again later or contact customer service. (IAM: <em id="i12866909201"><a name="i12866909201"></a><a name="i12866909201"></a>xxxx</em>, IAM error information)</p>
    </td>
    </tr>
    <tr id="row724554392228"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p589898489269"><a name="p589898489269"></a><a name="p589898489269"></a>MRS.203</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p3785593792543"><a name="p3785593792543"></a><a name="p3785593792543"></a>Failed due to a VPC error. Try again later or contact customer service. (VPC: <em id="i5729224132017"><a name="i5729224132017"></a><a name="i5729224132017"></a>xxxx</em>, VPC error information)</p>
    </td>
    </tr>
    <tr id="row4869322992228"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p539262569269"><a name="p539262569269"></a><a name="p539262569269"></a>MRS.300</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p1523559692543"><a name="p1523559692543"></a><a name="p1523559692543"></a>MRS system error. Try again later or contact customer service.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   For the description about error status codes, see  [Status Codes](status-codes.md).

