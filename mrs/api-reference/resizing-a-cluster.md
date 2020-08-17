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
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><a name="ul5350290520155"></a><a name="ul5350290520155"></a><ul id="ul5350290520155"><li><strong id="b758512561470"><a name="b758512561470"></a><a name="b758512561470"></a>scale_in</strong>: cluster scale-in</li><li><strong id="b5809259977"><a name="b5809259977"></a><a name="b5809259977"></a>scale_out</strong>: cluster scale-out</li></ul>
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
<a name="ul156684552518"></a><a name="ul156684552518"></a><ul id="ul156684552518"><li><strong id="b1984919146812"><a name="b1984919146812"></a><a name="b1984919146812"></a>true</strong>: Do not start components after scale-out.</li><li><strong id="b12884151712819"><a name="b12884151712819"></a><a name="b12884151712819"></a>false</strong>: Start components after scale-out.</li></ul>
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
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1229610391215"><a name="p1229610391215"></a><a name="p1229610391215"></a>Instance specifications of a Task node, for example, <strong id="b11521223494"><a name="b11521223494"></a><a name="b11521223494"></a>c2.2xlarge.linux.mrs</strong></p>
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
<a name="ul46838108114112"></a><a name="ul46838108114112"></a><ul id="ul46838108114112"><li><strong id="b493051517254"><a name="b493051517254"></a><a name="b493051517254"></a>succeeded</strong>: The operation is successful.</li><li><a href="#table101661350414">Table 6</a> describes the error codes returned upon operation failures.</li></ul>
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


-   [Table 6](#table101661350414)  describes the error codes returned upon operation failures.

    **Table  6**  Error codes

    <a name="table101661350414"></a>
    <table><thead align="left"><tr id="row915923519414"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p151591735184113"><a name="p151591735184113"></a><a name="p151591735184113"></a>Error Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p14159435134111"><a name="p14159435134111"></a><a name="p14159435134111"></a>Message</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row81611135194113"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p4160143516413"><a name="p4160143516413"></a><a name="p4160143516413"></a>12000001</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p2160143554113"><a name="p2160143554113"></a><a name="p2160143554113"></a>Identity verification is invalid</p>
    </td>
    </tr>
    <tr id="row71613355411"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p1416120352413"><a name="p1416120352413"></a><a name="p1416120352413"></a>12000002</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p15161113512416"><a name="p15161113512416"></a><a name="p15161113512416"></a>The parameter is invalid.</p>
    </td>
    </tr>
    <tr id="row1016183518412"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p16161835174116"><a name="p16161835174116"></a><a name="p16161835174116"></a>12000003</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p216143514114"><a name="p216143514114"></a><a name="p216143514114"></a>The cluster does not exist.</p>
    </td>
    </tr>
    <tr id="row141613354414"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p516113517411"><a name="p516113517411"></a><a name="p516113517411"></a>12000009</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p21617358418"><a name="p21617358418"></a><a name="p21617358418"></a>The method parameter is invalid.</p>
    </td>
    </tr>
    <tr id="row716133513417"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p191616356417"><a name="p191616356417"></a><a name="p191616356417"></a>12000013</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p5161163574110"><a name="p5161163574110"></a><a name="p5161163574110"></a>Scale-in of cluster <i><span class="varname" id="varname6518406615933"><a name="varname6518406615933"></a><a name="varname6518406615933"></a>XX</span></i> failed.</p>
    </td>
    </tr>
    <tr id="row1616293517414"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p716111352416"><a name="p716111352416"></a><a name="p716111352416"></a>12000014</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p12162203544110"><a name="p12162203544110"></a><a name="p12162203544110"></a>Scale-out of cluster <i><span class="varname" id="varname2951684115939"><a name="varname2951684115939"></a><a name="varname2951684115939"></a>XX</span></i> failed.</p>
    </td>
    </tr>
    <tr id="row11162163504117"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p16162113515413"><a name="p16162113515413"></a><a name="p16162113515413"></a>12000017</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p121621435144114"><a name="p121621435144114"></a><a name="p121621435144114"></a>Scale-out or scale-in is not allowed for clusters that are not in the <strong id="b9681114661011"><a name="b9681114661011"></a><a name="b9681114661011"></a>Running</strong> state.</p>
    </td>
    </tr>
    <tr id="row816213554117"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p11162113519411"><a name="p11162113519411"></a><a name="p11162113519411"></a>12000018</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p116211357415"><a name="p116211357415"></a><a name="p116211357415"></a>Scale-out or scale-in cannot be performed again because it is in progress.</p>
    </td>
    </tr>
    <tr id="row5162113544113"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p1116243511412"><a name="p1116243511412"></a><a name="p1116243511412"></a>12000019</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p616283534118"><a name="p616283534118"></a><a name="p616283534118"></a>Failed to obtain hosts of the cluster.</p>
    </td>
    </tr>
    <tr id="row12162435104110"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p151621635204111"><a name="p151621635204111"></a><a name="p151621635204111"></a>12000028</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p13162103519414"><a name="p13162103519414"></a><a name="p13162103519414"></a>The maximum number of Core nodes in a cluster is <i><span class="varname" id="varname49786155151054"><a name="varname49786155151054"></a><a name="varname49786155151054"></a>N</span></i>.</p>
    </td>
    </tr>
    <tr id="row816223519416"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p151625351418"><a name="p151625351418"></a><a name="p151625351418"></a>12000029</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p161621935134111"><a name="p161621935134111"></a><a name="p161621935134111"></a>Failed to obtain the quota.</p>
    </td>
    </tr>
    <tr id="row15163835184118"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p12162133554113"><a name="p12162133554113"></a><a name="p12162133554113"></a>12000030</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p1916215352414"><a name="p1916215352414"></a><a name="p1916215352414"></a>The requested number of nodes in the cluster exceeds the available quota.</p>
    </td>
    </tr>
    <tr id="row216311359411"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p18163173534110"><a name="p18163173534110"></a><a name="p18163173534110"></a>12000031</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p81631535164116"><a name="p81631535164116"></a><a name="p81631535164116"></a>The requested number of vCPUs in the cluster exceeds the available quota.</p>
    </td>
    </tr>
    <tr id="row4163123512418"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p216303512413"><a name="p216303512413"></a><a name="p216303512413"></a>12000032</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p416310355412"><a name="p416310355412"></a><a name="p416310355412"></a>The requested memory of the cluster exceeds the available quota.</p>
    </td>
    </tr>
    <tr id="row116343524117"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p1316303594110"><a name="p1316303594110"></a><a name="p1316303594110"></a>12000033</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p1716373554119"><a name="p1716373554119"></a><a name="p1716373554119"></a>The requested number of disks in the cluster exceeds the available quota.</p>
    </td>
    </tr>
    <tr id="row916353534116"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p161631735144112"><a name="p161631735144112"></a><a name="p161631735144112"></a>12000034</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p151632352415"><a name="p151632352415"></a><a name="p151632352415"></a>The requested disk capacity of the cluster exceeds the available quota.</p>
    </td>
    </tr>
    <tr id="row2163535164112"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p11163113594117"><a name="p11163113594117"></a><a name="p11163113594117"></a>12000054</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p3163123518414"><a name="p3163123518414"></a><a name="p3163123518414"></a>The operation is not supported.</p>
    </td>
    </tr>
    <tr id="row1516313359412"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p1016333504112"><a name="p1016333504112"></a><a name="p1016333504112"></a>12000067</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p31633355417"><a name="p31633355417"></a><a name="p31633355417"></a>The cluster cannot be scaled out because its version is too early. Upgrade the cluster to the latest version.</p>
    </td>
    </tr>
    <tr id="row1416443510410"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p20163535154112"><a name="p20163535154112"></a><a name="p20163535154112"></a>12000068</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p18164203564113"><a name="p18164203564113"></a><a name="p18164203564113"></a>The status of some nodes is not running in the cluster. Try again later.</p>
    </td>
    </tr>
    <tr id="row1316410357419"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p1316413352414"><a name="p1316413352414"></a><a name="p1316413352414"></a>12000121</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p81644351412"><a name="p81644351412"></a><a name="p81644351412"></a>Scale-out is not allowed because the cluster has an unpaid order. Scale out the cluster again after you pay the order.</p>
    </td>
    </tr>
    <tr id="row1216433534115"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p11641635174116"><a name="p11641635174116"></a><a name="p11641635174116"></a>MRS.101</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p91641935164118"><a name="p91641935164118"></a><a name="p91641935164118"></a>Your request could not be fulfilled because your quota is insufficient. Contact technical support to increase the quota.</p>
    </td>
    </tr>
    <tr id="row201641635184111"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p1616412359412"><a name="p1616412359412"></a><a name="p1616412359412"></a>MRS.102</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p161649353419"><a name="p161649353419"></a><a name="p161649353419"></a>The token cannot be null or invalid. Try again later or contact customer service.</p>
    </td>
    </tr>
    <tr id="row31642351413"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p17164153574118"><a name="p17164153574118"></a><a name="p17164153574118"></a>MRS.103</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p116473554110"><a name="p116473554110"></a><a name="p116473554110"></a>Invalid request. Try again later or contact customer service.</p>
    </td>
    </tr>
    <tr id="row1716510358412"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p516553517416"><a name="p516553517416"></a><a name="p516553517416"></a>MRS.104</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p81659351418"><a name="p81659351418"></a><a name="p81659351418"></a>Insufficient resources. Try again later or contact customer service.</p>
    </td>
    </tr>
    <tr id="row1216515357410"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p5165935184112"><a name="p5165935184112"></a><a name="p5165935184112"></a>MRS.105</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p1216563516419"><a name="p1216563516419"></a><a name="p1216563516419"></a>Insufficient IP addresses in the existing subnet. Try again later or contact customer service.</p>
    </td>
    </tr>
    <tr id="row131651935184115"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p1116553512417"><a name="p1116553512417"></a><a name="p1116553512417"></a>MRS.201</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p16165535194114"><a name="p16165535194114"></a><a name="p16165535194114"></a>Failed due to an ECS error. Try again later or contact customer service. (ECS: <em id="i143527504193"><a name="i143527504193"></a><a name="i143527504193"></a>xxxx</em>, ECS error information)</p>
    </td>
    </tr>
    <tr id="row516520355419"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p916510352415"><a name="p916510352415"></a><a name="p916510352415"></a>MRS.202</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p8165153516411"><a name="p8165153516411"></a><a name="p8165153516411"></a>Failed due to an IAM error. Try again later or contact customer service. (IAM: <em id="i12866909201"><a name="i12866909201"></a><a name="i12866909201"></a>xxxx</em>, IAM error information)</p>
    </td>
    </tr>
    <tr id="row10165935144115"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6165173515413"><a name="p6165173515413"></a><a name="p6165173515413"></a>MRS.203</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p11652353412"><a name="p11652353412"></a><a name="p11652353412"></a>Failed due to a VPC error. Try again later or contact customer service. (VPC: <em id="i5729224132017"><a name="i5729224132017"></a><a name="i5729224132017"></a>xxxx</em>, VPC error information)</p>
    </td>
    </tr>
    <tr id="row16166193594116"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p5166133518415"><a name="p5166133518415"></a><a name="p5166133518415"></a>MRS.300</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4166193514413"><a name="p4166193514413"></a><a name="p4166193514413"></a>MRS system error. Try again later or contact customer service.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   For the description about error status codes, see  [Status Codes](status-codes.md).

