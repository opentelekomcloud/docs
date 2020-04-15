# Configuring an Auto Scaling Rule<a name="EN-US_TOPIC_0172486193"></a>

## Function<a name="section17052835105155"></a>

This API is used to configure an auto scaling rule.

The API used for cluster creation and job execution can also be used to creation an auto scaling rule.

## URI<a name="section161439810524"></a>

-   Format

    POST /v1.1/\{project\_id\}/autoscaling-policy/\{cluster\_id\}

-   Parameter description

    **Table  1**  URI parameter description

    <a name="table49499141194754"></a>
    <table><thead align="left"><tr id="row33700024194754"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p16571835194812"><a name="p16571835194812"></a><a name="p16571835194812"></a><strong id="b4115161720318"><a name="b4115161720318"></a><a name="b4115161720318"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p141410194812"><a name="p141410194812"></a><a name="p141410194812"></a><strong id="b353812019314"><a name="b353812019314"></a><a name="b353812019314"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p11454278194812"><a name="p11454278194812"></a><a name="p11454278194812"></a><strong id="b32828241738"><a name="b32828241738"></a><a name="b32828241738"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37407495194754"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p56702435194812"><a name="p56702435194812"></a><a name="p56702435194812"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p29494508194812"><a name="p29494508194812"></a><a name="p29494508194812"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p40820562194812"><a name="p40820562194812"></a><a name="p40820562194812"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row9793450141337"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p42588366141346"><a name="p42588366141346"></a><a name="p42588366141346"></a>cluster_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p27105608141346"><a name="p27105608141346"></a><a name="p27105608141346"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p6137976141354"><a name="p6137976141354"></a><a name="p6137976141354"></a>Cluster ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section7976792193238"></a>

**Request parameters**

[Table 2](#table27243156151210)  and  [Table 3](#table50379282141720)  describes the request parameters.

**Table  2** **node\_group**  parameter description

<a name="table27243156151210"></a>
<table><thead align="left"><tr id="row17848224151210"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p59344636151210"><a name="p59344636151210"></a><a name="p59344636151210"></a><strong id="b1432318461618"><a name="b1432318461618"></a><a name="b1432318461618"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p42186216151210"><a name="p42186216151210"></a><a name="p42186216151210"></a><strong id="b6631250167"><a name="b6631250167"></a><a name="b6631250167"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p61640332151210"><a name="p61640332151210"></a><a name="p61640332151210"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p26811025151210"><a name="p26811025151210"></a><a name="p26811025151210"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row39972639151210"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p16558360151210"><a name="p16558360151210"></a><a name="p16558360151210"></a>node_group</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p66158789151210"><a name="p66158789151210"></a><a name="p66158789151210"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p57261711151210"><a name="p57261711151210"></a><a name="p57261711151210"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p7687005151210"><a name="p7687005151210"></a><a name="p7687005151210"></a>Type of the node to which an auto scaling rule applies. Currently, only Task nodes are supported, that is, the request value is <strong id="b2058614615174"><a name="b2058614615174"></a><a name="b2058614615174"></a>task_node_default_group</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **auto\_scaling\_policy**  parameter description

<a name="table50379282141720"></a>
<table><thead align="left"><tr id="en-us_topic_0172486173_raf51026a1f504a8788e1403658120f2f"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="en-us_topic_0172486173_a6b57643863a6437a8c107916b9c7695d"><a name="en-us_topic_0172486173_a6b57643863a6437a8c107916b9c7695d"></a><a name="en-us_topic_0172486173_a6b57643863a6437a8c107916b9c7695d"></a><strong id="en-us_topic_0172486173_b1784095713486"><a name="en-us_topic_0172486173_b1784095713486"></a><a name="en-us_topic_0172486173_b1784095713486"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="en-us_topic_0172486173_a3fff5ea955e54459addfcbbb35b643ec"><a name="en-us_topic_0172486173_a3fff5ea955e54459addfcbbb35b643ec"></a><a name="en-us_topic_0172486173_a3fff5ea955e54459addfcbbb35b643ec"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0172486173_aa1457e2336bd448ea6d9616e20227777"><a name="en-us_topic_0172486173_aa1457e2336bd448ea6d9616e20227777"></a><a name="en-us_topic_0172486173_aa1457e2336bd448ea6d9616e20227777"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="en-us_topic_0172486173_a5321d724cd884c23b9ae748f98ba4424"><a name="en-us_topic_0172486173_a5321d724cd884c23b9ae748f98ba4424"></a><a name="en-us_topic_0172486173_a5321d724cd884c23b9ae748f98ba4424"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0172486173_ra90fcd7439104b2c98d8b7081bfdef71"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a8e70a35d4222449cb92a4041ef7f0137"><a name="en-us_topic_0172486173_a8e70a35d4222449cb92a4041ef7f0137"></a><a name="en-us_topic_0172486173_a8e70a35d4222449cb92a4041ef7f0137"></a>auto_scaling_enable</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_ae90c66ff525b4f18b199fba818fcc23e"><a name="en-us_topic_0172486173_ae90c66ff525b4f18b199fba818fcc23e"></a><a name="en-us_topic_0172486173_ae90c66ff525b4f18b199fba818fcc23e"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a2c10267f0ea74faba0b9fb771d478e67"><a name="en-us_topic_0172486173_a2c10267f0ea74faba0b9fb771d478e67"></a><a name="en-us_topic_0172486173_a2c10267f0ea74faba0b9fb771d478e67"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_a8b16bd6c0885436e8051b80f0aea7c8d"><a name="en-us_topic_0172486173_a8b16bd6c0885436e8051b80f0aea7c8d"></a><a name="en-us_topic_0172486173_a8b16bd6c0885436e8051b80f0aea7c8d"></a>Whether to enable the auto scaling rule</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_r1fe6b7d60f7345d3b8d1c1d8cb8806bd"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a379d490f2095437fad3072496b931b39"><a name="en-us_topic_0172486173_a379d490f2095437fad3072496b931b39"></a><a name="en-us_topic_0172486173_a379d490f2095437fad3072496b931b39"></a>min_capacity</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a67bf7a6b811a47d1accfd408095436fb"><a name="en-us_topic_0172486173_a67bf7a6b811a47d1accfd408095436fb"></a><a name="en-us_topic_0172486173_a67bf7a6b811a47d1accfd408095436fb"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_en-us_topic_0110581924_p230787112654"><a name="en-us_topic_0172486173_en-us_topic_0110581924_p230787112654"></a><a name="en-us_topic_0172486173_en-us_topic_0110581924_p230787112654"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_a6339dac619fd4e838c5285c78f3162f9"><a name="en-us_topic_0172486173_a6339dac619fd4e838c5285c78f3162f9"></a><a name="en-us_topic_0172486173_a6339dac619fd4e838c5285c78f3162f9"></a>Minimum number of nodes left in the node group</p>
<p id="en-us_topic_0172486173_ac2a776ad7e134fadb625996c4d1d83d6"><a name="en-us_topic_0172486173_ac2a776ad7e134fadb625996c4d1d83d6"></a><a name="en-us_topic_0172486173_ac2a776ad7e134fadb625996c4d1d83d6"></a>Value range: 0 to 500</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_r8b569e44ff74496d9a7eb20ac8a742e4"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a7eaed7f858d7454b8c65783319c39b04"><a name="en-us_topic_0172486173_a7eaed7f858d7454b8c65783319c39b04"></a><a name="en-us_topic_0172486173_a7eaed7f858d7454b8c65783319c39b04"></a>max_capacity</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a67bf8fb9a84542bd8757eeb97a31418f"><a name="en-us_topic_0172486173_a67bf8fb9a84542bd8757eeb97a31418f"></a><a name="en-us_topic_0172486173_a67bf8fb9a84542bd8757eeb97a31418f"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a3ecf064ee466445781aeb1a335395cba"><a name="en-us_topic_0172486173_a3ecf064ee466445781aeb1a335395cba"></a><a name="en-us_topic_0172486173_a3ecf064ee466445781aeb1a335395cba"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_a27bf42b5a44f47378f54aad66fef804f"><a name="en-us_topic_0172486173_a27bf42b5a44f47378f54aad66fef804f"></a><a name="en-us_topic_0172486173_a27bf42b5a44f47378f54aad66fef804f"></a>Maximum number of nodes in the node group</p>
<p id="en-us_topic_0172486173_a480eee70830e4129964adad7def22b88"><a name="en-us_topic_0172486173_a480eee70830e4129964adad7def22b88"></a><a name="en-us_topic_0172486173_a480eee70830e4129964adad7def22b88"></a>Value range: 0 to 500</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_row109862440157"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_p99881444155"><a name="en-us_topic_0172486173_p99881444155"></a><a name="en-us_topic_0172486173_p99881444155"></a>resources_plans</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_p1998854481510"><a name="en-us_topic_0172486173_p1998854481510"></a><a name="en-us_topic_0172486173_p1998854481510"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_p59886442157"><a name="en-us_topic_0172486173_p59886442157"></a><a name="en-us_topic_0172486173_p59886442157"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_p189881644171514"><a name="en-us_topic_0172486173_p189881644171514"></a><a name="en-us_topic_0172486173_p189881644171514"></a>Resource plan list. For details, see <a href="creating-a-cluster-and-running-a-job.md#table10281451162111">Table 8</a>. If this parameter is left blank, the resource plan is disabled.</p>
<p id="en-us_topic_0172486173_p9402141913220"><a name="en-us_topic_0172486173_p9402141913220"></a><a name="en-us_topic_0172486173_p9402141913220"></a>When auto scaling is enabled, either a resource plan or an auto scaling rule must be configured.</p>
<p id="en-us_topic_0172486173_p332510443181"><a name="en-us_topic_0172486173_p332510443181"></a><a name="en-us_topic_0172486173_p332510443181"></a>MRS 1.6.3 or later supports this parameter.</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_row36011313174"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_p337232320178"><a name="en-us_topic_0172486173_p337232320178"></a><a name="en-us_topic_0172486173_p337232320178"></a>exec_scripts</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_p337220231170"><a name="en-us_topic_0172486173_p337220231170"></a><a name="en-us_topic_0172486173_p337220231170"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_p11372152341713"><a name="en-us_topic_0172486173_p11372152341713"></a><a name="en-us_topic_0172486173_p11372152341713"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_p93729233178"><a name="en-us_topic_0172486173_p93729233178"></a><a name="en-us_topic_0172486173_p93729233178"></a>List of custom scaling automation scripts. For details, see <a href="creating-a-cluster-and-running-a-job.md#table1921110172216">Table 9</a>. If this parameter is left blank, a hook script is disabled.</p>
<p id="en-us_topic_0172486173_p03726234173"><a name="en-us_topic_0172486173_p03726234173"></a><a name="en-us_topic_0172486173_p03726234173"></a>MRS 1.7.2 or later supports this parameter.</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_r4755a3babff849968d83bd43129dc7eb"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a308e43c85e40439b8c59d08440843dc6"><a name="en-us_topic_0172486173_a308e43c85e40439b8c59d08440843dc6"></a><a name="en-us_topic_0172486173_a308e43c85e40439b8c59d08440843dc6"></a>rules</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a98d5257b9540482989b03783ec10a561"><a name="en-us_topic_0172486173_a98d5257b9540482989b03783ec10a561"></a><a name="en-us_topic_0172486173_a98d5257b9540482989b03783ec10a561"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_ae314628f2d8a4766924313079bbabe68"><a name="en-us_topic_0172486173_ae314628f2d8a4766924313079bbabe68"></a><a name="en-us_topic_0172486173_ae314628f2d8a4766924313079bbabe68"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_ac2e02b36ba1e434fb0df7479bd8acd50"><a name="en-us_topic_0172486173_ac2e02b36ba1e434fb0df7479bd8acd50"></a><a name="en-us_topic_0172486173_ac2e02b36ba1e434fb0df7479bd8acd50"></a>List of auto scaling rules. For details, see <a href="creating-a-cluster-and-running-a-job.md#t4c9e3e169631470d81d260543affb7e1">Table 10</a>.</p>
<p id="en-us_topic_0172486173_p6516143522217"><a name="en-us_topic_0172486173_p6516143522217"></a><a name="en-us_topic_0172486173_p6516143522217"></a>When auto scaling is enabled, either a resource plan or an auto scaling rule must be configured.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **resources\_plan**  parameter description

<a name="table1979310416120"></a>
<table><thead align="left"><tr id="en-us_topic_0172486173_row21077515215"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="en-us_topic_0172486173_p11361051162118"><a name="en-us_topic_0172486173_p11361051162118"></a><a name="en-us_topic_0172486173_p11361051162118"></a><strong id="en-us_topic_0172486173_b7261143718239"><a name="en-us_topic_0172486173_b7261143718239"></a><a name="en-us_topic_0172486173_b7261143718239"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="en-us_topic_0172486173_p1815835115218"><a name="en-us_topic_0172486173_p1815835115218"></a><a name="en-us_topic_0172486173_p1815835115218"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0172486173_p2018015511218"><a name="en-us_topic_0172486173_p2018015511218"></a><a name="en-us_topic_0172486173_p2018015511218"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="en-us_topic_0172486173_p5198351122117"><a name="en-us_topic_0172486173_p5198351122117"></a><a name="en-us_topic_0172486173_p5198351122117"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0172486173_row1121555192110"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_p18632144118282"><a name="en-us_topic_0172486173_p18632144118282"></a><a name="en-us_topic_0172486173_p18632144118282"></a>period_type</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_p4632164118286"><a name="en-us_topic_0172486173_p4632164118286"></a><a name="en-us_topic_0172486173_p4632164118286"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_p166321418282"><a name="en-us_topic_0172486173_p166321418282"></a><a name="en-us_topic_0172486173_p166321418282"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_p963214419289"><a name="en-us_topic_0172486173_p963214419289"></a><a name="en-us_topic_0172486173_p963214419289"></a>Cycle type of a resource plan. Currently, only the following cycle type is supported:</p>
<a name="en-us_topic_0172486173_ul363284116288"></a><a name="en-us_topic_0172486173_ul363284116288"></a><ul id="en-us_topic_0172486173_ul363284116288"><li>daily</li></ul>
</td>
</tr>
<tr id="en-us_topic_0172486173_row1531855116213"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_p11633174182818"><a name="en-us_topic_0172486173_p11633174182818"></a><a name="en-us_topic_0172486173_p11633174182818"></a>start_time</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_p196331041132814"><a name="en-us_topic_0172486173_p196331041132814"></a><a name="en-us_topic_0172486173_p196331041132814"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_p19633114122816"><a name="en-us_topic_0172486173_p19633114122816"></a><a name="en-us_topic_0172486173_p19633114122816"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_p13633154112816"><a name="en-us_topic_0172486173_p13633154112816"></a><a name="en-us_topic_0172486173_p13633154112816"></a>Start time of a resources plan. The value is in the format of <strong id="en-us_topic_0172486173_b972495515249"><a name="en-us_topic_0172486173_b972495515249"></a><a name="en-us_topic_0172486173_b972495515249"></a>hour:minute</strong>, indicating that the time ranges from 0:00 to 23:59.</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_row7405105118211"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_p126333415281"><a name="en-us_topic_0172486173_p126333415281"></a><a name="en-us_topic_0172486173_p126333415281"></a>end_time</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_p2063344114284"><a name="en-us_topic_0172486173_p2063344114284"></a><a name="en-us_topic_0172486173_p2063344114284"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_p863364112819"><a name="en-us_topic_0172486173_p863364112819"></a><a name="en-us_topic_0172486173_p863364112819"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_p2633174117282"><a name="en-us_topic_0172486173_p2633174117282"></a><a name="en-us_topic_0172486173_p2633174117282"></a>End time of a resources plan. The value is in the same format as that of <span class="parmname" id="en-us_topic_0172486173_parmname108341828162917"><a name="en-us_topic_0172486173_parmname108341828162917"></a><a name="en-us_topic_0172486173_parmname108341828162917"></a><b>start_time</b></span>. The interval between <strong id="en-us_topic_0172486173_b1917973215256"><a name="en-us_topic_0172486173_b1917973215256"></a><a name="en-us_topic_0172486173_b1917973215256"></a>end_time</strong> and <strong id="en-us_topic_0172486173_b149161137152511"><a name="en-us_topic_0172486173_b149161137152511"></a><a name="en-us_topic_0172486173_b149161137152511"></a>start_time</strong> must be greater than or equal to 30 minutes.</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_row19532851132116"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_p206334415288"><a name="en-us_topic_0172486173_p206334415288"></a><a name="en-us_topic_0172486173_p206334415288"></a>min_capacity</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_p2633184112285"><a name="en-us_topic_0172486173_p2633184112285"></a><a name="en-us_topic_0172486173_p2633184112285"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_p116331241202817"><a name="en-us_topic_0172486173_p116331241202817"></a><a name="en-us_topic_0172486173_p116331241202817"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_p6633141102810"><a name="en-us_topic_0172486173_p6633141102810"></a><a name="en-us_topic_0172486173_p6633141102810"></a>Minimum number of the preserved nodes in a node group in a resource plan.</p>
<p id="en-us_topic_0172486173_p3629135317296"><a name="en-us_topic_0172486173_p3629135317296"></a><a name="en-us_topic_0172486173_p3629135317296"></a>Value range: 0 to 500</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_row176245516217"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_p263304119287"><a name="en-us_topic_0172486173_p263304119287"></a><a name="en-us_topic_0172486173_p263304119287"></a>max_capacity</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_p146331041172818"><a name="en-us_topic_0172486173_p146331041172818"></a><a name="en-us_topic_0172486173_p146331041172818"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_p156331241162818"><a name="en-us_topic_0172486173_p156331241162818"></a><a name="en-us_topic_0172486173_p156331241162818"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_p19633174118288"><a name="en-us_topic_0172486173_p19633174118288"></a><a name="en-us_topic_0172486173_p19633174118288"></a>Maximum number of the preserved nodes in a node group in a resource plan.</p>
<p id="en-us_topic_0172486173_p16373013020"><a name="en-us_topic_0172486173_p16373013020"></a><a name="en-us_topic_0172486173_p16373013020"></a>Value range: 0 to 500</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **exec\_script**  parameter description

<a name="tefd2eb7c7838496eadbf4b310193de4a"></a>
<table><thead align="left"><tr id="en-us_topic_0172486173_row1428214111224"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="en-us_topic_0172486173_p15297171172210"><a name="en-us_topic_0172486173_p15297171172210"></a><a name="en-us_topic_0172486173_p15297171172210"></a><strong id="en-us_topic_0172486173_b14579436112615"><a name="en-us_topic_0172486173_b14579436112615"></a><a name="en-us_topic_0172486173_b14579436112615"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="en-us_topic_0172486173_p8318816229"><a name="en-us_topic_0172486173_p8318816229"></a><a name="en-us_topic_0172486173_p8318816229"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0172486173_p19332191122219"><a name="en-us_topic_0172486173_p19332191122219"></a><a name="en-us_topic_0172486173_p19332191122219"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="en-us_topic_0172486173_p934614122220"><a name="en-us_topic_0172486173_p934614122220"></a><a name="en-us_topic_0172486173_p934614122220"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0172486173_row16364151162210"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_p2716626113010"><a name="en-us_topic_0172486173_p2716626113010"></a><a name="en-us_topic_0172486173_p2716626113010"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_p9716122653011"><a name="en-us_topic_0172486173_p9716122653011"></a><a name="en-us_topic_0172486173_p9716122653011"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_p12716172613308"><a name="en-us_topic_0172486173_p12716172613308"></a><a name="en-us_topic_0172486173_p12716172613308"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_p1271632643011"><a name="en-us_topic_0172486173_p1271632643011"></a><a name="en-us_topic_0172486173_p1271632643011"></a>Name of a custom automation script. It must be unique in a same cluster.</p>
<p id="en-us_topic_0172486173_p971662623010"><a name="en-us_topic_0172486173_p971662623010"></a><a name="en-us_topic_0172486173_p971662623010"></a>The value can contain only digits, letters, spaces, hyphens (-), and underscores (_) and cannot start with a space.</p>
<p id="en-us_topic_0172486173_p2716192613010"><a name="en-us_topic_0172486173_p2716192613010"></a><a name="en-us_topic_0172486173_p2716192613010"></a>The value can contain 1 to 64 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_row1446317117222"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_p1671632619307"><a name="en-us_topic_0172486173_p1671632619307"></a><a name="en-us_topic_0172486173_p1671632619307"></a>uri</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_p771612265306"><a name="en-us_topic_0172486173_p771612265306"></a><a name="en-us_topic_0172486173_p771612265306"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_p37169268302"><a name="en-us_topic_0172486173_p37169268302"></a><a name="en-us_topic_0172486173_p37169268302"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_p15716132603020"><a name="en-us_topic_0172486173_p15716132603020"></a><a name="en-us_topic_0172486173_p15716132603020"></a>Path of a custom automation script. Set this parameter to an OBS bucket path or a local VM path.</p>
<a name="en-us_topic_0172486173_ul2716122616303"></a><a name="en-us_topic_0172486173_ul2716122616303"></a><ul id="en-us_topic_0172486173_ul2716122616303"><li>OBS bucket path: Enter a script path manually, for example, <strong id="en-us_topic_0172486173_b862319216300"><a name="en-us_topic_0172486173_b862319216300"></a><a name="en-us_topic_0172486173_b862319216300"></a>s3a://<em id="en-us_topic_0172486173_i17361161133015"><a name="en-us_topic_0172486173_i17361161133015"></a><a name="en-us_topic_0172486173_i17361161133015"></a>XXX</em>/scale.sh</strong>.</li><li>Local VM path: Enter a script path. The script path must start with a slash (/) and end with <strong id="en-us_topic_0172486173_b2635103117309"><a name="en-us_topic_0172486173_b2635103117309"></a><a name="en-us_topic_0172486173_b2635103117309"></a>.sh</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0172486173_row25607102210"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_p361414413374"><a name="en-us_topic_0172486173_p361414413374"></a><a name="en-us_topic_0172486173_p361414413374"></a>parameters</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_p361484123715"><a name="en-us_topic_0172486173_p361484123715"></a><a name="en-us_topic_0172486173_p361484123715"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_p146149414371"><a name="en-us_topic_0172486173_p146149414371"></a><a name="en-us_topic_0172486173_p146149414371"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_p8614746374"><a name="en-us_topic_0172486173_p8614746374"></a><a name="en-us_topic_0172486173_p8614746374"></a>Parameters of a custom automation script</p>
<a name="en-us_topic_0172486173_ul19405172713813"></a><a name="en-us_topic_0172486173_ul19405172713813"></a><ul id="en-us_topic_0172486173_ul19405172713813"><li>Multiple parameters are separated by space.</li><li>The following predefined system parameters can be transferred:<a name="en-us_topic_0172486173_ul740512275389"></a><a name="en-us_topic_0172486173_ul740512275389"></a><ul id="en-us_topic_0172486173_ul740512275389"><li>${mrs_scale_node_num}: Number of the nodes to be added or removed</li><li>${mrs_scale_type}: Scaling type. The value can be <strong id="en-us_topic_0172486173_b209806114324"><a name="en-us_topic_0172486173_b209806114324"></a><a name="en-us_topic_0172486173_b209806114324"></a>scale_out</strong> or <strong id="en-us_topic_0172486173_b16355132010329"><a name="en-us_topic_0172486173_b16355132010329"></a><a name="en-us_topic_0172486173_b16355132010329"></a>scale_in</strong>.</li><li>${mrs_scale_node_hostnames}: Host names of the nodes to be added or removed</li><li>${mrs_scale_node_ips}: IP addresses of the nodes to be added or removed</li><li>${mrs_scale_rule_name}: Name of the rule that triggers auto scaling</li></ul>
</li><li>Other user-defined parameters are used in the same way as those of common shell scripts. Parameters are separated by space.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0172486173_row870514172210"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_p106161244377"><a name="en-us_topic_0172486173_p106161244377"></a><a name="en-us_topic_0172486173_p106161244377"></a>nodes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_p661616418371"><a name="en-us_topic_0172486173_p661616418371"></a><a name="en-us_topic_0172486173_p661616418371"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_p14616244375"><a name="en-us_topic_0172486173_p14616244375"></a><a name="en-us_topic_0172486173_p14616244375"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_p56161649373"><a name="en-us_topic_0172486173_p56161649373"></a><a name="en-us_topic_0172486173_p56161649373"></a>Type of a node where the custom automation script is executed. The node type can be Master, Core, or Task.</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_row67891315228"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_p1733982111374"><a name="en-us_topic_0172486173_p1733982111374"></a><a name="en-us_topic_0172486173_p1733982111374"></a>active_master</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_p153391921173710"><a name="en-us_topic_0172486173_p153391921173710"></a><a name="en-us_topic_0172486173_p153391921173710"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_p4339142163715"><a name="en-us_topic_0172486173_p4339142163715"></a><a name="en-us_topic_0172486173_p4339142163715"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_p833952163716"><a name="en-us_topic_0172486173_p833952163716"></a><a name="en-us_topic_0172486173_p833952163716"></a>Whether the custom automation script runs only on the active Master node.</p>
<p id="en-us_topic_0172486173_p13391218375"><a name="en-us_topic_0172486173_p13391218375"></a><a name="en-us_topic_0172486173_p13391218375"></a>The default value is <strong id="en-us_topic_0172486173_b98671943018"><a name="en-us_topic_0172486173_b98671943018"></a><a name="en-us_topic_0172486173_b98671943018"></a>false</strong>, indicating that the custom automation script can run on all Master nodes.</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_row3891131122219"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_p195951338133710"><a name="en-us_topic_0172486173_p195951338133710"></a><a name="en-us_topic_0172486173_p195951338133710"></a>action_stage</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_p1759563815377"><a name="en-us_topic_0172486173_p1759563815377"></a><a name="en-us_topic_0172486173_p1759563815377"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_p195951038123720"><a name="en-us_topic_0172486173_p195951038123720"></a><a name="en-us_topic_0172486173_p195951038123720"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_p5595438133717"><a name="en-us_topic_0172486173_p5595438133717"></a><a name="en-us_topic_0172486173_p5595438133717"></a>Time when a script is executed.</p>
<p id="en-us_topic_0172486173_p175951038193717"><a name="en-us_topic_0172486173_p175951038193717"></a><a name="en-us_topic_0172486173_p175951038193717"></a>The following four options are supported:</p>
<a name="en-us_topic_0172486173_ul959511385379"></a><a name="en-us_topic_0172486173_ul959511385379"></a><ul id="en-us_topic_0172486173_ul959511385379"><li>before_scale_out: before scale-out</li><li>before_scale_in: before scale-in</li><li>after_scale_out: after scale-out</li><li>after_scale_in: after scale-in</li></ul>
</td>
</tr>
<tr id="en-us_topic_0172486173_row173493683712"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_p1595838193720"><a name="en-us_topic_0172486173_p1595838193720"></a><a name="en-us_topic_0172486173_p1595838193720"></a>fail_action</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_p1595138123712"><a name="en-us_topic_0172486173_p1595138123712"></a><a name="en-us_topic_0172486173_p1595138123712"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_p159611387376"><a name="en-us_topic_0172486173_p159611387376"></a><a name="en-us_topic_0172486173_p159611387376"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_p959633833712"><a name="en-us_topic_0172486173_p959633833712"></a><a name="en-us_topic_0172486173_p959633833712"></a>Whether to continue to execute subsequent scripts and create a cluster after the custom automation script fails to be executed.</p>
<a name="en-us_topic_0172486173_ul1859673813372"></a><a name="en-us_topic_0172486173_ul1859673813372"></a><ul id="en-us_topic_0172486173_ul1859673813372"><li>continue: Continue to execute subsequent scripts.</li><li>errorout: Stop the action.<div class="note" id="en-us_topic_0172486173_note1637813387373"><a name="en-us_topic_0172486173_note1637813387373"></a><a name="en-us_topic_0172486173_note1637813387373"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0172486173_ul117517425369"></a><a name="en-us_topic_0172486173_ul117517425369"></a><ul id="en-us_topic_0172486173_ul117517425369"><li>You are advised to set this parameter to <strong id="en-us_topic_0172486173_b842352706114220"><a name="en-us_topic_0172486173_b842352706114220"></a><a name="en-us_topic_0172486173_b842352706114220"></a>continue</strong> in the commissioning phase so that the cluster can continue to be installed and started no matter whether the custom automation script is executed successfully.</li><li>The scale-in operation cannot be undone. Therefore <span class="parmname" id="en-us_topic_0172486173_parmname47251253810"><a name="en-us_topic_0172486173_parmname47251253810"></a><a name="en-us_topic_0172486173_parmname47251253810"></a><b>fail_action</b></span> must be set to <span class="parmvalue" id="en-us_topic_0172486173_parmvalue7529192612381"><a name="en-us_topic_0172486173_parmvalue7529192612381"></a><a name="en-us_topic_0172486173_parmvalue7529192612381"></a><b>continue</b></span> for the scripts that are executed after scale-in.</li></ul>
</div></div>
</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  6** **rules**  parameter description

<a name="t46230cdbc4f641f6b17d64de5747728b"></a>
<table><thead align="left"><tr id="en-us_topic_0172486173_r04dab5da98994243b13ab537426a3a97"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="en-us_topic_0172486173_ad679ccb275b24cc496175d3841c71d4a"><a name="en-us_topic_0172486173_ad679ccb275b24cc496175d3841c71d4a"></a><a name="en-us_topic_0172486173_ad679ccb275b24cc496175d3841c71d4a"></a><strong id="en-us_topic_0172486173_b136101356781"><a name="en-us_topic_0172486173_b136101356781"></a><a name="en-us_topic_0172486173_b136101356781"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="en-us_topic_0172486173_a640760dee401468b9b46729570e2c885"><a name="en-us_topic_0172486173_a640760dee401468b9b46729570e2c885"></a><a name="en-us_topic_0172486173_a640760dee401468b9b46729570e2c885"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0172486173_acb08948a5f1440c3b9925d7b25fd1cfc"><a name="en-us_topic_0172486173_acb08948a5f1440c3b9925d7b25fd1cfc"></a><a name="en-us_topic_0172486173_acb08948a5f1440c3b9925d7b25fd1cfc"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="en-us_topic_0172486173_ae3354bfaa9f549358e263c7ff419fb0b"><a name="en-us_topic_0172486173_ae3354bfaa9f549358e263c7ff419fb0b"></a><a name="en-us_topic_0172486173_ae3354bfaa9f549358e263c7ff419fb0b"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0172486173_rb70a6fabcd634bb488830fad4df3ec23"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a30a512ec6a824430b85d412a03a87f01"><a name="en-us_topic_0172486173_a30a512ec6a824430b85d412a03a87f01"></a><a name="en-us_topic_0172486173_a30a512ec6a824430b85d412a03a87f01"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a9821fa2ef3a545c6918722356913f19d"><a name="en-us_topic_0172486173_a9821fa2ef3a545c6918722356913f19d"></a><a name="en-us_topic_0172486173_a9821fa2ef3a545c6918722356913f19d"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a79be49bbaf734f838a223ef00e505777"><a name="en-us_topic_0172486173_a79be49bbaf734f838a223ef00e505777"></a><a name="en-us_topic_0172486173_a79be49bbaf734f838a223ef00e505777"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_aba48112f6b6643379185e9024b158818"><a name="en-us_topic_0172486173_aba48112f6b6643379185e9024b158818"></a><a name="en-us_topic_0172486173_aba48112f6b6643379185e9024b158818"></a>Name of an auto scaling rule</p>
<p id="en-us_topic_0172486173_ad2dfd75a61e449daba07a8aec95b70af"><a name="en-us_topic_0172486173_ad2dfd75a61e449daba07a8aec95b70af"></a><a name="en-us_topic_0172486173_ad2dfd75a61e449daba07a8aec95b70af"></a>It contains only 1 to 64 characters. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
<p id="en-us_topic_0172486173_a4fb8ccd95fd84f4e9167a742ea119278"><a name="en-us_topic_0172486173_a4fb8ccd95fd84f4e9167a742ea119278"></a><a name="en-us_topic_0172486173_a4fb8ccd95fd84f4e9167a742ea119278"></a>Rule names must be unique in a node group.</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_r43e582bae8d7452ba656dde618f5200c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a4db367e43bb943eeb5a845fa7b3209a6"><a name="en-us_topic_0172486173_a4db367e43bb943eeb5a845fa7b3209a6"></a><a name="en-us_topic_0172486173_a4db367e43bb943eeb5a845fa7b3209a6"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_aa3ce5a5274894b5c8ff040dbda4d893a"><a name="en-us_topic_0172486173_aa3ce5a5274894b5c8ff040dbda4d893a"></a><a name="en-us_topic_0172486173_aa3ce5a5274894b5c8ff040dbda4d893a"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a5229ef45bcb04550a546ed9ef4541966"><a name="en-us_topic_0172486173_a5229ef45bcb04550a546ed9ef4541966"></a><a name="en-us_topic_0172486173_a5229ef45bcb04550a546ed9ef4541966"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_a54e73e7a5fe84ea68e0c68c676c69078"><a name="en-us_topic_0172486173_a54e73e7a5fe84ea68e0c68c676c69078"></a><a name="en-us_topic_0172486173_a54e73e7a5fe84ea68e0c68c676c69078"></a>Description about an auto scaling rule.</p>
<p id="en-us_topic_0172486173_a3913d07fc617486c800f3e34ebc28224"><a name="en-us_topic_0172486173_a3913d07fc617486c800f3e34ebc28224"></a><a name="en-us_topic_0172486173_a3913d07fc617486c800f3e34ebc28224"></a>It contains a maximum of 1024 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_r63d765b129664dad957626f380819572"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a44f544e08b0a41de95dabf9bf4e1434a"><a name="en-us_topic_0172486173_a44f544e08b0a41de95dabf9bf4e1434a"></a><a name="en-us_topic_0172486173_a44f544e08b0a41de95dabf9bf4e1434a"></a>adjustment_type</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_aeef54466240a420aa0b5613dbb65143d"><a name="en-us_topic_0172486173_aeef54466240a420aa0b5613dbb65143d"></a><a name="en-us_topic_0172486173_aeef54466240a420aa0b5613dbb65143d"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a433b89c3fb244d7e954a41597d978cf8"><a name="en-us_topic_0172486173_a433b89c3fb244d7e954a41597d978cf8"></a><a name="en-us_topic_0172486173_a433b89c3fb244d7e954a41597d978cf8"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_afb3bb8888f944246b9b844cf271c4ab2"><a name="en-us_topic_0172486173_afb3bb8888f944246b9b844cf271c4ab2"></a><a name="en-us_topic_0172486173_afb3bb8888f944246b9b844cf271c4ab2"></a>Auto scaling rule adjustment type. The options are as follows:</p>
<a name="en-us_topic_0172486173_u18ec9abfa0234393b376df8ff616d19b"></a><a name="en-us_topic_0172486173_u18ec9abfa0234393b376df8ff616d19b"></a><ul id="en-us_topic_0172486173_u18ec9abfa0234393b376df8ff616d19b"><li>scale_out: cluster scale-out</li><li>scale_in: cluster scale-in</li></ul>
</td>
</tr>
<tr id="en-us_topic_0172486173_r6f9ebcd76459417a908a73ec838efe7c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a8f20410dbaee433abb560ec4458140af"><a name="en-us_topic_0172486173_a8f20410dbaee433abb560ec4458140af"></a><a name="en-us_topic_0172486173_a8f20410dbaee433abb560ec4458140af"></a>cool_down_minutes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_ace0d1386b05a420fad2f53bd4dbd7f4f"><a name="en-us_topic_0172486173_ace0d1386b05a420fad2f53bd4dbd7f4f"></a><a name="en-us_topic_0172486173_ace0d1386b05a420fad2f53bd4dbd7f4f"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a125498882f804fa99362663be962a9ec"><a name="en-us_topic_0172486173_a125498882f804fa99362663be962a9ec"></a><a name="en-us_topic_0172486173_a125498882f804fa99362663be962a9ec"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_a962e8faec9684b4b9388ddaae5f20f25"><a name="en-us_topic_0172486173_a962e8faec9684b4b9388ddaae5f20f25"></a><a name="en-us_topic_0172486173_a962e8faec9684b4b9388ddaae5f20f25"></a>Cluster cooling time after an auto scaling rule is triggered, when no auto scaling operation is performed. The unit is minute.</p>
<p id="en-us_topic_0172486173_a934200a982984f90a54b157715b28542"><a name="en-us_topic_0172486173_a934200a982984f90a54b157715b28542"></a><a name="en-us_topic_0172486173_a934200a982984f90a54b157715b28542"></a>Value range: 0 to 10080. One week is equal to 10080 minutes.</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_r83dc95f88c514f349fe399e2daec1acf"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a1bf156eb290c4eacac485c8e69bb9b8a"><a name="en-us_topic_0172486173_a1bf156eb290c4eacac485c8e69bb9b8a"></a><a name="en-us_topic_0172486173_a1bf156eb290c4eacac485c8e69bb9b8a"></a>scaling_adjustment</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_ac34a827ef47d41c19cb0a362521c1749"><a name="en-us_topic_0172486173_ac34a827ef47d41c19cb0a362521c1749"></a><a name="en-us_topic_0172486173_ac34a827ef47d41c19cb0a362521c1749"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a8ed38e14158144d1a1feee5d0c6672f9"><a name="en-us_topic_0172486173_a8ed38e14158144d1a1feee5d0c6672f9"></a><a name="en-us_topic_0172486173_a8ed38e14158144d1a1feee5d0c6672f9"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_acf6914ca275e493ba883ebb8a607a1ad"><a name="en-us_topic_0172486173_acf6914ca275e493ba883ebb8a607a1ad"></a><a name="en-us_topic_0172486173_acf6914ca275e493ba883ebb8a607a1ad"></a>Number of nodes that can be adjusted once</p>
<p id="en-us_topic_0172486173_a665de6492d5f41e183c5fdfa2a65629a"><a name="en-us_topic_0172486173_a665de6492d5f41e183c5fdfa2a65629a"></a><a name="en-us_topic_0172486173_a665de6492d5f41e183c5fdfa2a65629a"></a>Value range: 1 to 100</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_r66369f0421994b56a9ed58368cc08d5a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a5817b59eda8846d1ae9d530bd1ab342d"><a name="en-us_topic_0172486173_a5817b59eda8846d1ae9d530bd1ab342d"></a><a name="en-us_topic_0172486173_a5817b59eda8846d1ae9d530bd1ab342d"></a>trigger</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_aee6e5978de8143a7bfdc40db6e9304b2"><a name="en-us_topic_0172486173_aee6e5978de8143a7bfdc40db6e9304b2"></a><a name="en-us_topic_0172486173_aee6e5978de8143a7bfdc40db6e9304b2"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_afd9beb4a2ace493390bc25ced1fecf8d"><a name="en-us_topic_0172486173_afd9beb4a2ace493390bc25ced1fecf8d"></a><a name="en-us_topic_0172486173_afd9beb4a2ace493390bc25ced1fecf8d"></a>Trigger</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_a2c60fdaa8e8b434d91a9aaf1e369eff6"><a name="en-us_topic_0172486173_a2c60fdaa8e8b434d91a9aaf1e369eff6"></a><a name="en-us_topic_0172486173_a2c60fdaa8e8b434d91a9aaf1e369eff6"></a>Condition for triggering a rule. For details, see <a href="creating-a-cluster-and-running-a-job.md#t03bd10dc0ec94a3babc71b2d5d57c3fe">Table 11</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **trigger**  parameter description

<a name="tb0fcdad7ce8f4ebdb4fd9e76d805b5e8"></a>
<table><thead align="left"><tr id="en-us_topic_0172486173_rff8c363cdf464eb5a3a11207ffdf1cd8"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="en-us_topic_0172486173_af7ff5d0628724b4fa7b5cf884ea1b773"><a name="en-us_topic_0172486173_af7ff5d0628724b4fa7b5cf884ea1b773"></a><a name="en-us_topic_0172486173_af7ff5d0628724b4fa7b5cf884ea1b773"></a><strong id="en-us_topic_0172486173_b476928132219"><a name="en-us_topic_0172486173_b476928132219"></a><a name="en-us_topic_0172486173_b476928132219"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="en-us_topic_0172486173_a56f9bf71c2fc47b5a8e8e7c679965679"><a name="en-us_topic_0172486173_a56f9bf71c2fc47b5a8e8e7c679965679"></a><a name="en-us_topic_0172486173_a56f9bf71c2fc47b5a8e8e7c679965679"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0172486173_a8933d7f27ddb4c9798f80813eb864963"><a name="en-us_topic_0172486173_a8933d7f27ddb4c9798f80813eb864963"></a><a name="en-us_topic_0172486173_a8933d7f27ddb4c9798f80813eb864963"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="en-us_topic_0172486173_a1f9301595b084bb0a1226a00ef63cf3a"><a name="en-us_topic_0172486173_a1f9301595b084bb0a1226a00ef63cf3a"></a><a name="en-us_topic_0172486173_a1f9301595b084bb0a1226a00ef63cf3a"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0172486173_re14becd52b854699886dab346ddbbca9"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_ad3f42958ab364805946248b8a97a5681"><a name="en-us_topic_0172486173_ad3f42958ab364805946248b8a97a5681"></a><a name="en-us_topic_0172486173_ad3f42958ab364805946248b8a97a5681"></a>metric_name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a5e62e69cca49432484b604bd6c10da4f"><a name="en-us_topic_0172486173_a5e62e69cca49432484b604bd6c10da4f"></a><a name="en-us_topic_0172486173_a5e62e69cca49432484b604bd6c10da4f"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_af5d60c6023c64eb3af69213451e45a08"><a name="en-us_topic_0172486173_af5d60c6023c64eb3af69213451e45a08"></a><a name="en-us_topic_0172486173_af5d60c6023c64eb3af69213451e45a08"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_a67c5bbe2340144a0ac4ae630da919fdb"><a name="en-us_topic_0172486173_a67c5bbe2340144a0ac4ae630da919fdb"></a><a name="en-us_topic_0172486173_a67c5bbe2340144a0ac4ae630da919fdb"></a>Metric name</p>
<p id="en-us_topic_0172486173_ad6898742fd8c4b3d90f62a110092174a"><a name="en-us_topic_0172486173_ad6898742fd8c4b3d90f62a110092174a"></a><a name="en-us_topic_0172486173_ad6898742fd8c4b3d90f62a110092174a"></a>This triggering condition makes a judgment according to the value of the metric.</p>
<p id="en-us_topic_0172486173_adb15d44ef9cd49719e1558f955af8fe0"><a name="en-us_topic_0172486173_adb15d44ef9cd49719e1558f955af8fe0"></a><a name="en-us_topic_0172486173_adb15d44ef9cd49719e1558f955af8fe0"></a>A metric name contains a maximum of 64 characters.</p>
<p id="en-us_topic_0172486173_a249e5e0f422a474eb818f01e56c3c6e2"><a name="en-us_topic_0172486173_a249e5e0f422a474eb818f01e56c3c6e2"></a><a name="en-us_topic_0172486173_a249e5e0f422a474eb818f01e56c3c6e2"></a><a href="creating-a-cluster-and-running-a-job.md#t27de3279a99a48968dacb015c498d9cb">Table 12</a> lists the supported metric names.</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_rdf8d159ee61f4397920756d6db18f225"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_aaefe5f406be947a9bc590420af9fa60a"><a name="en-us_topic_0172486173_aaefe5f406be947a9bc590420af9fa60a"></a><a name="en-us_topic_0172486173_aaefe5f406be947a9bc590420af9fa60a"></a>metric_value</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_ad6ce5627219640d1a928ec145a5c9543"><a name="en-us_topic_0172486173_ad6ce5627219640d1a928ec145a5c9543"></a><a name="en-us_topic_0172486173_ad6ce5627219640d1a928ec145a5c9543"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_ae5eed36b433c4a778931e35c51c255c0"><a name="en-us_topic_0172486173_ae5eed36b433c4a778931e35c51c255c0"></a><a name="en-us_topic_0172486173_ae5eed36b433c4a778931e35c51c255c0"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_af6f48d7468d64a0394a3a4213d2a2268"><a name="en-us_topic_0172486173_af6f48d7468d64a0394a3a4213d2a2268"></a><a name="en-us_topic_0172486173_af6f48d7468d64a0394a3a4213d2a2268"></a>Metric threshold to trigger a rule</p>
<p id="en-us_topic_0172486173_a9cb6280b4c514776b95dd786fe3b71b9"><a name="en-us_topic_0172486173_a9cb6280b4c514776b95dd786fe3b71b9"></a><a name="en-us_topic_0172486173_a9cb6280b4c514776b95dd786fe3b71b9"></a>The parameter value must be an integer or number with two decimal places only. <a href="creating-a-cluster-and-running-a-job.md#t27de3279a99a48968dacb015c498d9cb">Table 12</a> provides values types and ranges corresponding to <strong id="en-us_topic_0172486173_b1161104445418"><a name="en-us_topic_0172486173_b1161104445418"></a><a name="en-us_topic_0172486173_b1161104445418"></a>metric_name</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_re4671e894e4448eb87e9d7ff852aecb5"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_af47cf271b63941ac96944f24e87910b2"><a name="en-us_topic_0172486173_af47cf271b63941ac96944f24e87910b2"></a><a name="en-us_topic_0172486173_af47cf271b63941ac96944f24e87910b2"></a>comparison_operator</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_ab55411f4b2a54e7195864b2dc799f3bb"><a name="en-us_topic_0172486173_ab55411f4b2a54e7195864b2dc799f3bb"></a><a name="en-us_topic_0172486173_ab55411f4b2a54e7195864b2dc799f3bb"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a933e80262e8c483dbfbf38aa2ec35333"><a name="en-us_topic_0172486173_a933e80262e8c483dbfbf38aa2ec35333"></a><a name="en-us_topic_0172486173_a933e80262e8c483dbfbf38aa2ec35333"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_adf4bb9d515db4212bee56e7a4389a892"><a name="en-us_topic_0172486173_adf4bb9d515db4212bee56e7a4389a892"></a><a name="en-us_topic_0172486173_adf4bb9d515db4212bee56e7a4389a892"></a>Metric judgment logic operator. The options are as follows:</p>
<a name="en-us_topic_0172486173_u7169b3049e9342e185a5074148528db2"></a><a name="en-us_topic_0172486173_u7169b3049e9342e185a5074148528db2"></a><ul id="en-us_topic_0172486173_u7169b3049e9342e185a5074148528db2"><li>LT: less than</li><li>GT: greater than</li><li>LTOE: less than or equal to</li><li>GTOE: greater than or equal to</li></ul>
</td>
</tr>
<tr id="en-us_topic_0172486173_rf50d0c4b959f434f956a9cd587368b68"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a03c9f551658b4130989f42292477ab3a"><a name="en-us_topic_0172486173_a03c9f551658b4130989f42292477ab3a"></a><a name="en-us_topic_0172486173_a03c9f551658b4130989f42292477ab3a"></a>evaluation_periods</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a036fbc2365fe431f9752b41bf56b6913"><a name="en-us_topic_0172486173_a036fbc2365fe431f9752b41bf56b6913"></a><a name="en-us_topic_0172486173_a036fbc2365fe431f9752b41bf56b6913"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_aaf1bc273e1ea46b3bd11b243b4223b90"><a name="en-us_topic_0172486173_aaf1bc273e1ea46b3bd11b243b4223b90"></a><a name="en-us_topic_0172486173_aaf1bc273e1ea46b3bd11b243b4223b90"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_aac0eda51209e440da2832133da986fe2"><a name="en-us_topic_0172486173_aac0eda51209e440da2832133da986fe2"></a><a name="en-us_topic_0172486173_aac0eda51209e440da2832133da986fe2"></a>Number of consecutive five-minute periods, during which a metric threshold is reached</p>
<p id="en-us_topic_0172486173_ab1eaebbe8f6a4f64ba521a9e4558f4b4"><a name="en-us_topic_0172486173_ab1eaebbe8f6a4f64ba521a9e4558f4b4"></a><a name="en-us_topic_0172486173_ab1eaebbe8f6a4f64ba521a9e4558f4b4"></a>Value range: 1 to 288</p>
</td>
</tr>
</tbody>
</table>

**Table  8**  Auto scaling metrics

<a name="td49a8d90c5444d929b277b709d35c445"></a>
<table><thead align="left"><tr id="en-us_topic_0172486173_r6f513581428249f08e517a602d698e15"><th class="cellrowborder" valign="top" width="15.598440155984402%" id="mcps1.2.5.1.1"><p id="en-us_topic_0172486173_a438235aa61f14211bfc4a1a5b83eb558"><a name="en-us_topic_0172486173_a438235aa61f14211bfc4a1a5b83eb558"></a><a name="en-us_topic_0172486173_a438235aa61f14211bfc4a1a5b83eb558"></a>Cluster Type</p>
</th>
<th class="cellrowborder" valign="top" width="24.437556244375564%" id="mcps1.2.5.1.2"><p id="en-us_topic_0172486173_abe5e348bbff341ce8105e23a1ed1773b"><a name="en-us_topic_0172486173_abe5e348bbff341ce8105e23a1ed1773b"></a><a name="en-us_topic_0172486173_abe5e348bbff341ce8105e23a1ed1773b"></a>Metric Name</p>
</th>
<th class="cellrowborder" valign="top" width="15.22847715228477%" id="mcps1.2.5.1.3"><p id="en-us_topic_0172486173_a682d9e227f744055822e498bf9c5856d"><a name="en-us_topic_0172486173_a682d9e227f744055822e498bf9c5856d"></a><a name="en-us_topic_0172486173_a682d9e227f744055822e498bf9c5856d"></a>Value Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.73552644735527%" id="mcps1.2.5.1.4"><p id="en-us_topic_0172486173_a253484a6f10b4e48932213cd57a12322"><a name="en-us_topic_0172486173_a253484a6f10b4e48932213cd57a12322"></a><a name="en-us_topic_0172486173_a253484a6f10b4e48932213cd57a12322"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0172486173_r3d35885bfaf34dd19a45669ca955ca07"><td class="cellrowborder" rowspan="7" valign="top" width="15.598440155984402%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a5114f66cbef24be89bf81e8698e641bf"><a name="en-us_topic_0172486173_a5114f66cbef24be89bf81e8698e641bf"></a><a name="en-us_topic_0172486173_a5114f66cbef24be89bf81e8698e641bf"></a>Streaming cluster</p>
</td>
<td class="cellrowborder" valign="top" width="24.437556244375564%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_ac72545b57c754656979548eb610a6870"><a name="en-us_topic_0172486173_ac72545b57c754656979548eb610a6870"></a><a name="en-us_topic_0172486173_ac72545b57c754656979548eb610a6870"></a>StormSlotAvailable</p>
</td>
<td class="cellrowborder" valign="top" width="15.22847715228477%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a335961e130ae43bbad38525916ff3c50"><a name="en-us_topic_0172486173_a335961e130ae43bbad38525916ff3c50"></a><a name="en-us_topic_0172486173_a335961e130ae43bbad38525916ff3c50"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="44.73552644735527%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_a6798fd17f81446d7bc23b65c206e62df"><a name="en-us_topic_0172486173_a6798fd17f81446d7bc23b65c206e62df"></a><a name="en-us_topic_0172486173_a6798fd17f81446d7bc23b65c206e62df"></a>Number of available Storm slots</p>
<p id="en-us_topic_0172486173_af8a8f569acf143b1b0641749d9a8958c"><a name="en-us_topic_0172486173_af8a8f569acf143b1b0641749d9a8958c"></a><a name="en-us_topic_0172486173_af8a8f569acf143b1b0641749d9a8958c"></a>Value range: 0 to 2147483646</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_rb933f33ebd4043ba9e917d0d2f4852e3"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_ab02fb123f43e415b8bb10a908a8acb3b"><a name="en-us_topic_0172486173_ab02fb123f43e415b8bb10a908a8acb3b"></a><a name="en-us_topic_0172486173_ab02fb123f43e415b8bb10a908a8acb3b"></a>StormSlotAvailablePercentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a52893a2e940f4c5ab48c2e5473ce2f0a"><a name="en-us_topic_0172486173_a52893a2e940f4c5ab48c2e5473ce2f0a"></a><a name="en-us_topic_0172486173_a52893a2e940f4c5ab48c2e5473ce2f0a"></a>Percentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a019e6f8ac83a4aa88544fb69ef775a38"><a name="en-us_topic_0172486173_a019e6f8ac83a4aa88544fb69ef775a38"></a><a name="en-us_topic_0172486173_a019e6f8ac83a4aa88544fb69ef775a38"></a>Percentage of available Storm slots, that is, the proportion of the available slots to total slots</p>
<p id="en-us_topic_0172486173_ac2fa579fd8b34e32bee870e7fc7f2ac9"><a name="en-us_topic_0172486173_ac2fa579fd8b34e32bee870e7fc7f2ac9"></a><a name="en-us_topic_0172486173_ac2fa579fd8b34e32bee870e7fc7f2ac9"></a>Value range: 0 to 100</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_r08070c64771a42b6a113d6febbfaa29d"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a691509a26b894eb482bc9ba4b595edb1"><a name="en-us_topic_0172486173_a691509a26b894eb482bc9ba4b595edb1"></a><a name="en-us_topic_0172486173_a691509a26b894eb482bc9ba4b595edb1"></a>StormSlotUsed</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_abe031b1f053a4e3ead22c147dcafa3aa"><a name="en-us_topic_0172486173_abe031b1f053a4e3ead22c147dcafa3aa"></a><a name="en-us_topic_0172486173_abe031b1f053a4e3ead22c147dcafa3aa"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a277ae72eb6754de2bf11608cd9e6e12e"><a name="en-us_topic_0172486173_a277ae72eb6754de2bf11608cd9e6e12e"></a><a name="en-us_topic_0172486173_a277ae72eb6754de2bf11608cd9e6e12e"></a>Number of the used Storm slots</p>
<p id="en-us_topic_0172486173_ae765f078f7354dacb24c79349c9a5e6c"><a name="en-us_topic_0172486173_ae765f078f7354dacb24c79349c9a5e6c"></a><a name="en-us_topic_0172486173_ae765f078f7354dacb24c79349c9a5e6c"></a>Value range: 0 to 2147483646</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_re0b727e5886646b49fe255ac2e7a2951"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_afd137ca4d82b4bceb58798293de6c8d4"><a name="en-us_topic_0172486173_afd137ca4d82b4bceb58798293de6c8d4"></a><a name="en-us_topic_0172486173_afd137ca4d82b4bceb58798293de6c8d4"></a>StormSlotUsedPercentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a880db12e66534c39810fd1d0bd16093a"><a name="en-us_topic_0172486173_a880db12e66534c39810fd1d0bd16093a"></a><a name="en-us_topic_0172486173_a880db12e66534c39810fd1d0bd16093a"></a>Percentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_ad49e3d813f2d4239a469338f348c3077"><a name="en-us_topic_0172486173_ad49e3d813f2d4239a469338f348c3077"></a><a name="en-us_topic_0172486173_ad49e3d813f2d4239a469338f348c3077"></a>Percentage of the used Storm slots, that is, the proportion of the used slots to total slots</p>
<p id="en-us_topic_0172486173_ada4c81170b0d4b93b744a65a698d5174"><a name="en-us_topic_0172486173_ada4c81170b0d4b93b744a65a698d5174"></a><a name="en-us_topic_0172486173_ada4c81170b0d4b93b744a65a698d5174"></a>Value range: 0 to 100</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_row177919386154"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_p135088571721"><a name="en-us_topic_0172486173_p135088571721"></a><a name="en-us_topic_0172486173_p135088571721"></a>StormSupervisorMemAverageUsage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_p1950845719217"><a name="en-us_topic_0172486173_p1950845719217"></a><a name="en-us_topic_0172486173_p1950845719217"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_p165082571219"><a name="en-us_topic_0172486173_p165082571219"></a><a name="en-us_topic_0172486173_p165082571219"></a>Average memory usage of the Supervisor process of Storm</p>
<p id="en-us_topic_0172486173_p165194141793"><a name="en-us_topic_0172486173_p165194141793"></a><a name="en-us_topic_0172486173_p165194141793"></a>Value range: 0 to 2147483646</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_row631194414155"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_p188210636"><a name="en-us_topic_0172486173_p188210636"></a><a name="en-us_topic_0172486173_p188210636"></a>StormSupervisorMemAverageUsagePercentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_p6821801732"><a name="en-us_topic_0172486173_p6821801732"></a><a name="en-us_topic_0172486173_p6821801732"></a>Percentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_p88213018314"><a name="en-us_topic_0172486173_p88213018314"></a><a name="en-us_topic_0172486173_p88213018314"></a>Average percentage of the used memory of the Supervisor process of Storm to the total memory of the system</p>
<p id="en-us_topic_0172486173_p3227151918108"><a name="en-us_topic_0172486173_p3227151918108"></a><a name="en-us_topic_0172486173_p3227151918108"></a>Value range: 0 to 100</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_row7783194871512"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_p794819218319"><a name="en-us_topic_0172486173_p794819218319"></a><a name="en-us_topic_0172486173_p794819218319"></a>StormSupervisorCPUAverageUsagePercentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_p1494842533"><a name="en-us_topic_0172486173_p1494842533"></a><a name="en-us_topic_0172486173_p1494842533"></a>Percentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_p1948121837"><a name="en-us_topic_0172486173_p1948121837"></a><a name="en-us_topic_0172486173_p1948121837"></a>Average percentage of the used CPUs of the Supervisor process of Storm to the total CPUs</p>
<p id="en-us_topic_0172486173_p1690164451113"><a name="en-us_topic_0172486173_p1690164451113"></a><a name="en-us_topic_0172486173_p1690164451113"></a>Value range: 0 to 6000</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_ra430378d169b44c29d0139187c0f4a11"><td class="cellrowborder" rowspan="14" valign="top" width="15.598440155984402%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_af2c3361bef3e4acda820a0b5349dab94"><a name="en-us_topic_0172486173_af2c3361bef3e4acda820a0b5349dab94"></a><a name="en-us_topic_0172486173_af2c3361bef3e4acda820a0b5349dab94"></a>Analysis cluster</p>
</td>
<td class="cellrowborder" valign="top" width="24.437556244375564%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a2ebc162d44404c4b9171628d2937cac6"><a name="en-us_topic_0172486173_a2ebc162d44404c4b9171628d2937cac6"></a><a name="en-us_topic_0172486173_a2ebc162d44404c4b9171628d2937cac6"></a>YARNAppPending</p>
</td>
<td class="cellrowborder" valign="top" width="15.22847715228477%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a49aea79e2e884b39906752aeb50f6a38"><a name="en-us_topic_0172486173_a49aea79e2e884b39906752aeb50f6a38"></a><a name="en-us_topic_0172486173_a49aea79e2e884b39906752aeb50f6a38"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="44.73552644735527%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0172486173_ad5b596886c494b288346f643daa764e9"><a name="en-us_topic_0172486173_ad5b596886c494b288346f643daa764e9"></a><a name="en-us_topic_0172486173_ad5b596886c494b288346f643daa764e9"></a>Number of pending tasks on YARN</p>
<p id="en-us_topic_0172486173_a35def1222c304e88a59b86583ce0130d"><a name="en-us_topic_0172486173_a35def1222c304e88a59b86583ce0130d"></a><a name="en-us_topic_0172486173_a35def1222c304e88a59b86583ce0130d"></a>Value range: 0 to 2147483646</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_r1c774463d2a14083a7fdfd96cbaefcef"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a26a74b6270f741a09b3bc5dec2b8a129"><a name="en-us_topic_0172486173_a26a74b6270f741a09b3bc5dec2b8a129"></a><a name="en-us_topic_0172486173_a26a74b6270f741a09b3bc5dec2b8a129"></a>YARNAppPendingRatio</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a8867793be2584544838efdc864b1b199"><a name="en-us_topic_0172486173_a8867793be2584544838efdc864b1b199"></a><a name="en-us_topic_0172486173_a8867793be2584544838efdc864b1b199"></a>Ratio</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a16e41ae39c3542cea4823cc61c96a5d3"><a name="en-us_topic_0172486173_a16e41ae39c3542cea4823cc61c96a5d3"></a><a name="en-us_topic_0172486173_a16e41ae39c3542cea4823cc61c96a5d3"></a>Ratio of pending tasks on YARN, that is, the ratio of pending tasks to running tasks on YARN</p>
<p id="en-us_topic_0172486173_a2d50ce28b3f445d49825f72dd917624d"><a name="en-us_topic_0172486173_a2d50ce28b3f445d49825f72dd917624d"></a><a name="en-us_topic_0172486173_a2d50ce28b3f445d49825f72dd917624d"></a>Value range: 0 to 2147483646</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_ra094fb90825148839fb3e3c750b09969"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_aa9ba37f3d402455d8e6f9d17b3b83329"><a name="en-us_topic_0172486173_aa9ba37f3d402455d8e6f9d17b3b83329"></a><a name="en-us_topic_0172486173_aa9ba37f3d402455d8e6f9d17b3b83329"></a>YARNAppRunning</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a985a37b47e8541daa74672ec40190b2d"><a name="en-us_topic_0172486173_a985a37b47e8541daa74672ec40190b2d"></a><a name="en-us_topic_0172486173_a985a37b47e8541daa74672ec40190b2d"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_ab56444e8f8054590a8eb9776184ee285"><a name="en-us_topic_0172486173_ab56444e8f8054590a8eb9776184ee285"></a><a name="en-us_topic_0172486173_ab56444e8f8054590a8eb9776184ee285"></a>Number of running tasks on YARN</p>
<p id="en-us_topic_0172486173_a6bb7fc15c9cc497b9befea371482ee14"><a name="en-us_topic_0172486173_a6bb7fc15c9cc497b9befea371482ee14"></a><a name="en-us_topic_0172486173_a6bb7fc15c9cc497b9befea371482ee14"></a>Value range: 0 to 2147483646</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_r877ab3607fb24199a4f8f5e6027e2d83"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a5e1a1fcebf9c4f5f96457b335d8d3524"><a name="en-us_topic_0172486173_a5e1a1fcebf9c4f5f96457b335d8d3524"></a><a name="en-us_topic_0172486173_a5e1a1fcebf9c4f5f96457b335d8d3524"></a>YARNContainerAllocated</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a4582c276628b40d69800e7c2f0f3e496"><a name="en-us_topic_0172486173_a4582c276628b40d69800e7c2f0f3e496"></a><a name="en-us_topic_0172486173_a4582c276628b40d69800e7c2f0f3e496"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a8dd055b550404e3586a2d008b49cb4aa"><a name="en-us_topic_0172486173_a8dd055b550404e3586a2d008b49cb4aa"></a><a name="en-us_topic_0172486173_a8dd055b550404e3586a2d008b49cb4aa"></a>Number of containers allocated to YARN </p>
<p id="en-us_topic_0172486173_a0af753d126374689b243d324b8b62643"><a name="en-us_topic_0172486173_a0af753d126374689b243d324b8b62643"></a><a name="en-us_topic_0172486173_a0af753d126374689b243d324b8b62643"></a>Value range: 0 to 2147483646</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_rf899d1058342458c8922fce992d570cc"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a3c879e53204943baa6f00e332603b436"><a name="en-us_topic_0172486173_a3c879e53204943baa6f00e332603b436"></a><a name="en-us_topic_0172486173_a3c879e53204943baa6f00e332603b436"></a>YARNContainerPending</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a9a4b0bf584494168ad484b62945df5ab"><a name="en-us_topic_0172486173_a9a4b0bf584494168ad484b62945df5ab"></a><a name="en-us_topic_0172486173_a9a4b0bf584494168ad484b62945df5ab"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_abd01e06bb70544e38882c07fdf1e5fbe"><a name="en-us_topic_0172486173_abd01e06bb70544e38882c07fdf1e5fbe"></a><a name="en-us_topic_0172486173_abd01e06bb70544e38882c07fdf1e5fbe"></a>Number of pending containers on YARN</p>
<p id="en-us_topic_0172486173_a93d072fada4a4322bb38029de44e1ea2"><a name="en-us_topic_0172486173_a93d072fada4a4322bb38029de44e1ea2"></a><a name="en-us_topic_0172486173_a93d072fada4a4322bb38029de44e1ea2"></a>Value range: 0 to 2147483646</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_r6eea766caaa8483ba2889235d08f1fb1"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a554108d1a4ac4d548d0d7c913d2c0e96"><a name="en-us_topic_0172486173_a554108d1a4ac4d548d0d7c913d2c0e96"></a><a name="en-us_topic_0172486173_a554108d1a4ac4d548d0d7c913d2c0e96"></a>YARNContainerPendingRatio</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a2f421b01c38b4dacab515d5013a94ec6"><a name="en-us_topic_0172486173_a2f421b01c38b4dacab515d5013a94ec6"></a><a name="en-us_topic_0172486173_a2f421b01c38b4dacab515d5013a94ec6"></a>Ratio</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a3ff2b486a44e4a079f2893a62ebe1057"><a name="en-us_topic_0172486173_a3ff2b486a44e4a079f2893a62ebe1057"></a><a name="en-us_topic_0172486173_a3ff2b486a44e4a079f2893a62ebe1057"></a>Ratio of pending containers on YARN, that is, the ratio of pending containers to running containers on YARN.</p>
<p id="en-us_topic_0172486173_afbecb57893244882aa592c19c2c6d4ca"><a name="en-us_topic_0172486173_afbecb57893244882aa592c19c2c6d4ca"></a><a name="en-us_topic_0172486173_afbecb57893244882aa592c19c2c6d4ca"></a>Value range: 0 to 2147483646</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_rada32b2ffd544cdb9aceb4f9499866c0"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_aa85783e97d85436eaf8172c7a9377839"><a name="en-us_topic_0172486173_aa85783e97d85436eaf8172c7a9377839"></a><a name="en-us_topic_0172486173_aa85783e97d85436eaf8172c7a9377839"></a>YARNCPUAllocated</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_ae9db170af0a74db097a4118d3c6acbd5"><a name="en-us_topic_0172486173_ae9db170af0a74db097a4118d3c6acbd5"></a><a name="en-us_topic_0172486173_ae9db170af0a74db097a4118d3c6acbd5"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a83a9e1639ef541398ad1326edfbe5652"><a name="en-us_topic_0172486173_a83a9e1639ef541398ad1326edfbe5652"></a><a name="en-us_topic_0172486173_a83a9e1639ef541398ad1326edfbe5652"></a>Number of virtual CPUs (vCPUs) allocated to YARN</p>
<p id="en-us_topic_0172486173_a647834b124bd4911a4e811ad0d5fab4e"><a name="en-us_topic_0172486173_a647834b124bd4911a4e811ad0d5fab4e"></a><a name="en-us_topic_0172486173_a647834b124bd4911a4e811ad0d5fab4e"></a>Value range: 0 to 2147483646</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_r24f9d8b6e19347a6af3a2b2602817b67"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a56f523a1e5d3450bbfdda7743eb92854"><a name="en-us_topic_0172486173_a56f523a1e5d3450bbfdda7743eb92854"></a><a name="en-us_topic_0172486173_a56f523a1e5d3450bbfdda7743eb92854"></a>YARNCPUAvailable</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a1879208a01884bc3bd21a4d2c696aad8"><a name="en-us_topic_0172486173_a1879208a01884bc3bd21a4d2c696aad8"></a><a name="en-us_topic_0172486173_a1879208a01884bc3bd21a4d2c696aad8"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a0ae5d086156342deba2460f41206c148"><a name="en-us_topic_0172486173_a0ae5d086156342deba2460f41206c148"></a><a name="en-us_topic_0172486173_a0ae5d086156342deba2460f41206c148"></a>Number of available vCPUs on YARN</p>
<p id="en-us_topic_0172486173_aee8087bc3ad8436fa0f8ef040ba673ab"><a name="en-us_topic_0172486173_aee8087bc3ad8436fa0f8ef040ba673ab"></a><a name="en-us_topic_0172486173_aee8087bc3ad8436fa0f8ef040ba673ab"></a>Value range: 0 to 2147483646</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_rb1a623bacb3446a7ad80947e61db5e14"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a14553be3cec14ae38983fbfb99f29d83"><a name="en-us_topic_0172486173_a14553be3cec14ae38983fbfb99f29d83"></a><a name="en-us_topic_0172486173_a14553be3cec14ae38983fbfb99f29d83"></a>YARNCPUAvailablePercentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a4ba6a334b5624002aea5c16ec2bef623"><a name="en-us_topic_0172486173_a4ba6a334b5624002aea5c16ec2bef623"></a><a name="en-us_topic_0172486173_a4ba6a334b5624002aea5c16ec2bef623"></a>Percentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a7f11c0314e0d4bcba94eaf62b670b6f1"><a name="en-us_topic_0172486173_a7f11c0314e0d4bcba94eaf62b670b6f1"></a><a name="en-us_topic_0172486173_a7f11c0314e0d4bcba94eaf62b670b6f1"></a>Percentage of available vCPUs on YARN, that is, the proportion of available vCPUs to total vCPUs</p>
<p id="en-us_topic_0172486173_a50104756cbae4a11afe22dfe9b28fd26"><a name="en-us_topic_0172486173_a50104756cbae4a11afe22dfe9b28fd26"></a><a name="en-us_topic_0172486173_a50104756cbae4a11afe22dfe9b28fd26"></a>Value range: 0 to 100</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_r0d968a43dce44f34bc59e65763a42dff"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_aaf82b0df6bd1489b9e4835f72e66848b"><a name="en-us_topic_0172486173_aaf82b0df6bd1489b9e4835f72e66848b"></a><a name="en-us_topic_0172486173_aaf82b0df6bd1489b9e4835f72e66848b"></a>YARNCPUPending</p>
<p id="en-us_topic_0172486173_adb1ad1fe51bc4d9097f76ed15949faee"><a name="en-us_topic_0172486173_adb1ad1fe51bc4d9097f76ed15949faee"></a><a name="en-us_topic_0172486173_adb1ad1fe51bc4d9097f76ed15949faee"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a182e236f3a6547c1b0c9ddeedc1cb812"><a name="en-us_topic_0172486173_a182e236f3a6547c1b0c9ddeedc1cb812"></a><a name="en-us_topic_0172486173_a182e236f3a6547c1b0c9ddeedc1cb812"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a091982b0354948558a83a2972fc10d78"><a name="en-us_topic_0172486173_a091982b0354948558a83a2972fc10d78"></a><a name="en-us_topic_0172486173_a091982b0354948558a83a2972fc10d78"></a>Number of pending vCPUs on YARN</p>
<p id="en-us_topic_0172486173_a28c518ff6e6f4720a9f248b1785b1a2b"><a name="en-us_topic_0172486173_a28c518ff6e6f4720a9f248b1785b1a2b"></a><a name="en-us_topic_0172486173_a28c518ff6e6f4720a9f248b1785b1a2b"></a>Value range: 0 to 2147483646</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_r07797e16294f41f2bd22c3d3e0f4fd86"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_af491e04ac4c749678edb5ccd96ecad9c"><a name="en-us_topic_0172486173_af491e04ac4c749678edb5ccd96ecad9c"></a><a name="en-us_topic_0172486173_af491e04ac4c749678edb5ccd96ecad9c"></a>YARNMemoryAllocated</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_ab2771fecf43a4a048713d458958feac6"><a name="en-us_topic_0172486173_ab2771fecf43a4a048713d458958feac6"></a><a name="en-us_topic_0172486173_ab2771fecf43a4a048713d458958feac6"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_ab22cfcbebf544c61b8dc9284e58cf92a"><a name="en-us_topic_0172486173_ab22cfcbebf544c61b8dc9284e58cf92a"></a><a name="en-us_topic_0172486173_ab22cfcbebf544c61b8dc9284e58cf92a"></a>Memory allocated to YARN. The unit is MB.</p>
<p id="en-us_topic_0172486173_a482cb09ec7f146e997111e48c2165fad"><a name="en-us_topic_0172486173_a482cb09ec7f146e997111e48c2165fad"></a><a name="en-us_topic_0172486173_a482cb09ec7f146e997111e48c2165fad"></a>Value range: 0 to 2147483646</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_re4224e170a464ddcb72136c05158e75b"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_a2e28017342644f3eb52611d00003d7b7"><a name="en-us_topic_0172486173_a2e28017342644f3eb52611d00003d7b7"></a><a name="en-us_topic_0172486173_a2e28017342644f3eb52611d00003d7b7"></a>YARNMemoryAvailable</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_ab709decebd9e4b69a20482fd11472034"><a name="en-us_topic_0172486173_ab709decebd9e4b69a20482fd11472034"></a><a name="en-us_topic_0172486173_ab709decebd9e4b69a20482fd11472034"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a561342c4dfc44654a5ea5ebfcb97c989"><a name="en-us_topic_0172486173_a561342c4dfc44654a5ea5ebfcb97c989"></a><a name="en-us_topic_0172486173_a561342c4dfc44654a5ea5ebfcb97c989"></a>Available memory on YARN. The unit is MB.</p>
<p id="en-us_topic_0172486173_abfa4f9cfe2094a23b33bdd2f66070f57"><a name="en-us_topic_0172486173_abfa4f9cfe2094a23b33bdd2f66070f57"></a><a name="en-us_topic_0172486173_abfa4f9cfe2094a23b33bdd2f66070f57"></a>Value range: 0 to 2147483646</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_refec09246ff047d7a9e3bf7d06a42cfd"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_aaa3390f6e15d4e5ea1140e5d599e6035"><a name="en-us_topic_0172486173_aaa3390f6e15d4e5ea1140e5d599e6035"></a><a name="en-us_topic_0172486173_aaa3390f6e15d4e5ea1140e5d599e6035"></a>YARNMemoryAvailablePercentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a67ac734ecc7b4b018a960953697740ed"><a name="en-us_topic_0172486173_a67ac734ecc7b4b018a960953697740ed"></a><a name="en-us_topic_0172486173_a67ac734ecc7b4b018a960953697740ed"></a>Percentage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_ac111dffe2233485382eab7979f3b65b3"><a name="en-us_topic_0172486173_ac111dffe2233485382eab7979f3b65b3"></a><a name="en-us_topic_0172486173_ac111dffe2233485382eab7979f3b65b3"></a>Percentage of available memory on YARN, that is, the proportion of available memory to total memory on YARN</p>
<p id="en-us_topic_0172486173_ae0f790dfccb9435484818f104234f1ea"><a name="en-us_topic_0172486173_ae0f790dfccb9435484818f104234f1ea"></a><a name="en-us_topic_0172486173_ae0f790dfccb9435484818f104234f1ea"></a>Value range: 0 to 100</p>
</td>
</tr>
<tr id="en-us_topic_0172486173_r0c96fd2f38dc41c6abb55f6997c2f4ad"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0172486173_af44c9409613840b281cd58f04122b5f8"><a name="en-us_topic_0172486173_af44c9409613840b281cd58f04122b5f8"></a><a name="en-us_topic_0172486173_af44c9409613840b281cd58f04122b5f8"></a>YARNMemoryPending</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0172486173_a462b3630c14b4fdcb4fbeabe4d5767cb"><a name="en-us_topic_0172486173_a462b3630c14b4fdcb4fbeabe4d5767cb"></a><a name="en-us_topic_0172486173_a462b3630c14b4fdcb4fbeabe4d5767cb"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0172486173_a4a7656ef0e7d41e994bb809330d24e1f"><a name="en-us_topic_0172486173_a4a7656ef0e7d41e994bb809330d24e1f"></a><a name="en-us_topic_0172486173_a4a7656ef0e7d41e994bb809330d24e1f"></a>Pending memory on YARN</p>
<p id="en-us_topic_0172486173_a5a450cbc34414ab599f331078b5f7d88"><a name="en-us_topic_0172486173_a5a450cbc34414ab599f331078b5f7d88"></a><a name="en-us_topic_0172486173_a5a450cbc34414ab599f331078b5f7d88"></a>Value range: 0 to 2147483646</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>When the value type is percentage or ratio in  [Table 12](creating-a-cluster-and-running-a-job.md#t27de3279a99a48968dacb015c498d9cb), the valid value can be accurate to percentile. The percentage metric value is a decimal value with a percent sign \(%\) removed. For example, 16.80 represents 16.80%.  

## Response<a name="section38599577193858"></a>

**Table  9**  Response parameter description

<a name="table8319691114112"></a>
<table><thead align="left"><tr id="row39824979114112"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p4597879114112"><a name="p4597879114112"></a><a name="p4597879114112"></a><strong id="b9293634164919"><a name="b9293634164919"></a><a name="b9293634164919"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p34804503114112"><a name="p34804503114112"></a><a name="p34804503114112"></a><strong id="b12817153744911"><a name="b12817153744911"></a><a name="b12817153744911"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p592484114112"><a name="p592484114112"></a><a name="p592484114112"></a><strong id="b221992140"><a name="b221992140"></a><a name="b221992140"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row47991225114112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p62084031114112"><a name="p62084031114112"></a><a name="p62084031114112"></a>result</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p44067044114112"><a name="p44067044114112"></a><a name="p44067044114112"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p12660774114112"><a name="p12660774114112"></a><a name="p12660774114112"></a>Operation result</p>
<a name="ul46838108114112"></a><a name="ul46838108114112"></a><ul id="ul46838108114112"><li>succeeded: The operation is successful.</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1210015461189"></a>

-   Example request

    ```
    {
      "node_group":"task_node_default_group",
      "auto_scaling_policy": {
          "auto_scaling_enable": true,
          "min_capacity": "1",
          "max_capacity": "3",
          "resources_plans": [{
             "period_type": "daily",
             "start_time": "9:50",
             "end_time": "10:20",
             "min_capacity": "2",
             "max_capacity": "3"
             },{
             "period_type": "daily",
             "start_time": "10:20",
             "end_time": "12:30",
             "min_capacity": "0",
             "max_capacity": "2"
           }],
           "exec_scripts": [{
             "name": "before_scale_out",
             "uri": "s3a://XXX/zeppelin_install.sh",
             "parameters": "",
             "nodes": [
               "master",
               "core",
               "task"
             ],
             "active_master": "true",
             "action_stage": "before_scale_out",
             "fail_action": "continue"
             },{
             "name": "after_scale_out",
             "uri": "s3a://XXX/storm_rebalance.sh",
             "parameters": "",
             "nodes": [
               "master",
               "core",
               "task"
             ],
             "active_master": "true",
             "action_stage": "after_scale_out",
             "fail_action": "continue"
          }],
          "rules": [{
             "name": "default-expand-1",
             "adjustment_type": "scale_out",
             "cool_down_minutes": 5,
             "scaling_adjustment": 1,
             "trigger": {
                "metric_name": "YARNMemoryAvailablePercentage",
                "metric_value": "25",
                "comparison_operator": "LT",
                "evaluation_periods": 10
                }
              },
             {
              "name": "default-shrink-1",
              "adjustment_type": "scale_in",
              "cool_down_minutes": 5,
              "scaling_adjustment": 1,
              "trigger": {
                 "metric_name": "YARNMemoryAvailablePercentage",
                 "metric_value": "70",
                 "comparison_operator": "GT",
                 "evaluation_periods": 10
                  }
               }]
         }
    }
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >A new auto scaling rule will overwrite the auto scaling rule saved in the original database. If you want to modify the original rule, query the original rule first, modify the rule, and submit a modification task. For details, see  [Querying Cluster Details](querying-cluster-details.md).  

-   Example response

    ```
    {       "result": "succeeded"  }
    ```


## Status Code<a name="section56352013105226"></a>

[Table 10](#table5043525610328)  describes the status code of this API.

**Table  10**  Status code

<a name="table5043525610328"></a>
<table><thead align="left"><tr id="row1549446910328"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p4709251510328"><a name="p4709251510328"></a><a name="p4709251510328"></a><strong id="b1022570061"><a name="b1022570061"></a><a name="b1022570061"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p5639738110328"><a name="p5639738110328"></a><a name="p5639738110328"></a><strong id="b815133566"><a name="b815133566"></a><a name="b815133566"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row478517210328"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p5205464710328"><a name="p5205464710328"></a><a name="p5205464710328"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p5567688710328"><a name="p5567688710328"></a><a name="p5567688710328"></a>The cluster has been successfully created.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

