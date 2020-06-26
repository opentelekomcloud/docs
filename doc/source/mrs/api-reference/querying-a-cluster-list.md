# Querying a Cluster List<a name="EN-US_TOPIC_0172486178"></a>

## Function<a name="s574b5ee583b94ffbab4fe268e27e2343"></a>

This API is used to query a list of clusters created by a user. This API is incompatible with Sahara.

## URI<a name="s1cb646f533c145d9a1a04ed0b9b3a647"></a>

-   Format

    GET /v1.1/\{project\_id\}/cluster\_infos?pageSize=\{page\_size\}&currentPage=\{current\_page\}&clusterState=\{cluster\_state\}&tags=\{tags\}

-   Parameter description

    **Table  1**  URI parameter description

    <a name="t21b2aa2542454793b44287fb87dfb0ac"></a>
    <table><thead align="left"><tr id="rb0bb20718ca347669ce586fa1f2de564"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="ab56f6487a962459eb945e6a5a88e772c"><a name="ab56f6487a962459eb945e6a5a88e772c"></a><a name="ab56f6487a962459eb945e6a5a88e772c"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0110581913_p141410194812"><a name="en-us_topic_0110581913_p141410194812"></a><a name="en-us_topic_0110581913_p141410194812"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="a0126591dc6d646c4b5fff001272e8d0b"><a name="a0126591dc6d646c4b5fff001272e8d0b"></a><a name="a0126591dc6d646c4b5fff001272e8d0b"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="re49d731079e144eb943021afe7ce8b56"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a6b125162379044a79d63969da4d57f59"><a name="a6b125162379044a79d63969da4d57f59"></a><a name="a6b125162379044a79d63969da4d57f59"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a81c275de16cf4a2bbdb5f49e6c187ee6"><a name="a81c275de16cf4a2bbdb5f49e6c187ee6"></a><a name="a81c275de16cf4a2bbdb5f49e6c187ee6"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aadd2dc350def4816b09611f9cf49e1d6"><a name="aadd2dc350def4816b09611f9cf49e1d6"></a><a name="aadd2dc350def4816b09611f9cf49e1d6"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row124371739182013"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p97270257225"><a name="p97270257225"></a><a name="p97270257225"></a>pageSize</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p832311363224"><a name="p832311363224"></a><a name="p832311363224"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1643813492223"><a name="p1643813492223"></a><a name="p1643813492223"></a>Maximum number of clusters displayed on a page</p>
    <p id="p1438749112216"><a name="p1438749112216"></a><a name="p1438749112216"></a>Value range: 1 to 2147483646</p>
    </td>
    </tr>
    <tr id="row146311398202"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p137281925182220"><a name="p137281925182220"></a><a name="p137281925182220"></a>currentPage</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p143236366221"><a name="p143236366221"></a><a name="p143236366221"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4439174982212"><a name="p4439174982212"></a><a name="p4439174982212"></a>Current page number</p>
    </td>
    </tr>
    <tr id="row9842193911203"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p372822582211"><a name="p372822582211"></a><a name="p372822582211"></a>clusterState</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1232463611229"><a name="p1232463611229"></a><a name="p1232463611229"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p643954919229"><a name="p643954919229"></a><a name="p643954919229"></a>You can query a cluster list by cluster status.</p>
    <a name="ul7439124914227"></a><a name="ul7439124914227"></a><ul id="ul7439124914227"><li>starting: Query a list of clusters that are being started.</li><li>running: Query a list of running clusters.</li><li>terminated: Query a list of terminated clusters.</li><li>failed: Query a list of failed clusters.</li><li>abnormal: Query a list of abnormal clusters.</li><li>terminating: Query a list of clusters that are being terminated.</li><li>frozen: Query a list of frozen clusters.</li><li>scaling-out: Query a list of clusters that are being scaled out.</li><li>scaling-in: Query a list of clusters that are being scaled in.</li></ul>
    </td>
    </tr>
    <tr id="row82511740192020"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p77281825152216"><a name="p77281825152216"></a><a name="p77281825152216"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p142521940122012"><a name="p142521940122012"></a><a name="p142521940122012"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p10439104920228"><a name="p10439104920228"></a><a name="p10439104920228"></a>You can search for a cluster by its tag. If you specify multiple tags, the relationship between them is AND.</p>
    <a name="ul1439174910224"></a><a name="ul1439174910224"></a><ul id="ul1439174910224"><li>The format of the <strong id="b84235270617157"><a name="b84235270617157"></a><a name="b84235270617157"></a>tags</strong> parameter is <strong id="b842352706171437"><a name="b842352706171437"></a><a name="b842352706171437"></a>tags=k1*v1,k2*v2,k3*v3</strong>.</li><li>When the values of some tags are null, the format is <strong id="b87324588409"><a name="b87324588409"></a><a name="b87324588409"></a>tags=k1,k2,k3*v3</strong>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s2b7c5edf256248ba9ea7540792fb5391"></a>

None

## Response<a name="s2d7ef5f47cdd410894126452fe31b313"></a>

**Table  2**  Response parameter description

<a name="t06313921cd3b49b9a1e7ad6f50906514"></a>
<table><thead align="left"><tr id="r530cb4fed5254b59aa55a0befdae0173"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="a20285c3d3f614f1299f009e7728457b8"><a name="a20285c3d3f614f1299f009e7728457b8"></a><a name="a20285c3d3f614f1299f009e7728457b8"></a><strong id="b254941115231"><a name="b254941115231"></a><a name="b254941115231"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="aab74eea885f3420cbae6b4fc00f34ca4"><a name="aab74eea885f3420cbae6b4fc00f34ca4"></a><a name="aab74eea885f3420cbae6b4fc00f34ca4"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="a918aeea4c09a48e2b810df57b2d69c31"><a name="a918aeea4c09a48e2b810df57b2d69c31"></a><a name="a918aeea4c09a48e2b810df57b2d69c31"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r2501c5439407495cb6c99ccc1e15bcf5"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a7e23a00873e940b9855f250f5beb96d8"><a name="a7e23a00873e940b9855f250f5beb96d8"></a><a name="a7e23a00873e940b9855f250f5beb96d8"></a>clusterTotal</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="af0ee9b6acac542d58a4c4e6b6a4410a0"><a name="af0ee9b6acac542d58a4c4e6b6a4410a0"></a><a name="af0ee9b6acac542d58a4c4e6b6a4410a0"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a4ba0ec5d0eb44ea1927dbd8d667d5e30"><a name="a4ba0ec5d0eb44ea1927dbd8d667d5e30"></a><a name="a4ba0ec5d0eb44ea1927dbd8d667d5e30"></a>Total number of clusters in a list</p>
</td>
</tr>
<tr id="r0ee6713ae31b4089b4e9f0600c60bb23"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ad7128dd6db7c4132af674829744747bd"><a name="ad7128dd6db7c4132af674829744747bd"></a><a name="ad7128dd6db7c4132af674829744747bd"></a>clusters</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a176f5958e7e241a989067a5d2438af09"><a name="a176f5958e7e241a989067a5d2438af09"></a><a name="a176f5958e7e241a989067a5d2438af09"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a47e4657da88d4c70930f3180a2f7b63d"><a name="a47e4657da88d4c70930f3180a2f7b63d"></a><a name="a47e4657da88d4c70930f3180a2f7b63d"></a>Cluster parameters. For details, see <a href="#t55f6f36df8d04eb9a231842a70d06296">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **clusters**  parameter description

<a name="t55f6f36df8d04eb9a231842a70d06296"></a>
<table><thead align="left"><tr id="r5f0075ce195d4645a8b196da4327c2a1"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="en-us_topic_0110581913_p648748144716"><a name="en-us_topic_0110581913_p648748144716"></a><a name="en-us_topic_0110581913_p648748144716"></a><strong id="b109068221241"><a name="b109068221241"></a><a name="b109068221241"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="a13ce060de8884172a09382116b2285e1"><a name="a13ce060de8884172a09382116b2285e1"></a><a name="a13ce060de8884172a09382116b2285e1"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="a74200a11f925487795b5a00257c1711e"><a name="a74200a11f925487795b5a00257c1711e"></a><a name="a74200a11f925487795b5a00257c1711e"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r8b80ecaa4ad240398fe848635a719fea"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ab61ce8e7ba944ed9b9d1fad63181357f"><a name="ab61ce8e7ba944ed9b9d1fad63181357f"></a><a name="ab61ce8e7ba944ed9b9d1fad63181357f"></a>clusterId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ab5ad448d1761497bbc3d7316f595d623"><a name="ab5ad448d1761497bbc3d7316f595d623"></a><a name="ab5ad448d1761497bbc3d7316f595d623"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ab57aa81b1f8948f489da1e8da6829b35"><a name="ab57aa81b1f8948f489da1e8da6829b35"></a><a name="ab57aa81b1f8948f489da1e8da6829b35"></a>Cluster ID</p>
</td>
</tr>
<tr id="r3b52cf27f6574e88b91818cf72896303"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a6580f76ca77d48db9744138ab40ca1db"><a name="a6580f76ca77d48db9744138ab40ca1db"></a><a name="a6580f76ca77d48db9744138ab40ca1db"></a>clusterName</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0110581913_p346145215818"><a name="en-us_topic_0110581913_p346145215818"></a><a name="en-us_topic_0110581913_p346145215818"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a04a6de6c77d84a9a97f0ec5ff5fa4786"><a name="a04a6de6c77d84a9a97f0ec5ff5fa4786"></a><a name="a04a6de6c77d84a9a97f0ec5ff5fa4786"></a>Cluster name</p>
</td>
</tr>
<tr id="r77a19550cc11494392ccdcdb7ef46655"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="adfc178faa2814266813bbcad58f5abfd"><a name="adfc178faa2814266813bbcad58f5abfd"></a><a name="adfc178faa2814266813bbcad58f5abfd"></a>masterNodeNum</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a88b52b3ee4314db4aafa90e2dbca7ab0"><a name="a88b52b3ee4314db4aafa90e2dbca7ab0"></a><a name="a88b52b3ee4314db4aafa90e2dbca7ab0"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ad309959c548c428684d69a6f26707ea2"><a name="ad309959c548c428684d69a6f26707ea2"></a><a name="ad309959c548c428684d69a6f26707ea2"></a>Number of Master nodes deployed in a cluster</p>
</td>
</tr>
<tr id="r98b8168bb13247e08b2aac3a062628ea"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110581913_p515909414533"><a name="en-us_topic_0110581913_p515909414533"></a><a name="en-us_topic_0110581913_p515909414533"></a>coreNodeNum</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="aa22fbe8c185841d2ad2a22266fba4b11"><a name="aa22fbe8c185841d2ad2a22266fba4b11"></a><a name="aa22fbe8c185841d2ad2a22266fba4b11"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a8e2ef1f9ce5d4367a10f14ba2d41a25a"><a name="a8e2ef1f9ce5d4367a10f14ba2d41a25a"></a><a name="a8e2ef1f9ce5d4367a10f14ba2d41a25a"></a>Number of Core nodes deployed in a cluster</p>
</td>
</tr>
<tr id="row1718814371713"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p518813438179"><a name="p518813438179"></a><a name="p518813438179"></a>totalNodeNum</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1636321171817"><a name="p1636321171817"></a><a name="p1636321171817"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p43634121819"><a name="p43634121819"></a><a name="p43634121819"></a>Total number of nodes deployed in a cluster</p>
</td>
</tr>
<tr id="r0c2287d77308466f9f396f01694520bc"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ae0783d944cd44261b67fef58299e7037"><a name="ae0783d944cd44261b67fef58299e7037"></a><a name="ae0783d944cd44261b67fef58299e7037"></a>clusterState</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0110581913_p740379615818"><a name="en-us_topic_0110581913_p740379615818"></a><a name="en-us_topic_0110581913_p740379615818"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><div class="p" id="a223c0b7f640443f784ad474d90a8143c"><a name="a223c0b7f640443f784ad474d90a8143c"></a><a name="a223c0b7f640443f784ad474d90a8143c"></a>Cluster status. Valid values include:<a name="u042ceaf297394c92b183c4d7f8f5a8f6"></a><a name="u042ceaf297394c92b183c4d7f8f5a8f6"></a><ul id="u042ceaf297394c92b183c4d7f8f5a8f6"><li>starting: The cluster is being started.</li><li>running: The cluster is running.</li><li>terminated: The cluster has been terminated.</li><li>failed: The cluster fails.</li><li>abnormal: The cluster is abnormal.</li><li>terminating: The cluster is being terminated.</li><li>frozen: The cluster has been frozen.</li><li>scaling-out: The cluster is being scaled out.</li><li>scaling-in: The cluster is being scaled in.</li></ul>
</div>
</td>
</tr>
<tr id="r31b8f66270ef4699afaf043b52b704cc"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a3cce747ae83543879d69ec170b90473f"><a name="a3cce747ae83543879d69ec170b90473f"></a><a name="a3cce747ae83543879d69ec170b90473f"></a>createAt</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ae2f361b335de4a9ebd8657bffafab637"><a name="ae2f361b335de4a9ebd8657bffafab637"></a><a name="ae2f361b335de4a9ebd8657bffafab637"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a472bbc80cc6442d19865aef1212dbffd"><a name="a472bbc80cc6442d19865aef1212dbffd"></a><a name="a472bbc80cc6442d19865aef1212dbffd"></a>Cluster creation time, which is a 10-bit timestamp</p>
</td>
</tr>
<tr id="r996897e26f8547a5b48f9747adee4fd3"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="afec076188fe6446dad1c4a5c7b7d62a8"><a name="afec076188fe6446dad1c4a5c7b7d62a8"></a><a name="afec076188fe6446dad1c4a5c7b7d62a8"></a>updateAt</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a6aa0280b4cf149dfa954e495d1554eda"><a name="a6aa0280b4cf149dfa954e495d1554eda"></a><a name="a6aa0280b4cf149dfa954e495d1554eda"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a57790f48a87941e7aec19eec4e702fdc"><a name="a57790f48a87941e7aec19eec4e702fdc"></a><a name="a57790f48a87941e7aec19eec4e702fdc"></a>Cluster update time, which is a 10-bit timestamp</p>
</td>
</tr>
<tr id="rfc458d4bd6b64e2e9049f324ee026e7c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ac03430959964424aa08cae11bdaa5d71"><a name="ac03430959964424aa08cae11bdaa5d71"></a><a name="ac03430959964424aa08cae11bdaa5d71"></a>billingType</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a6451ed910f8649a193dcb66304558acb"><a name="a6451ed910f8649a193dcb66304558acb"></a><a name="a6451ed910f8649a193dcb66304558acb"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a530c6b4c02be4e4b9cffc97681278d3a"><a name="a530c6b4c02be4e4b9cffc97681278d3a"></a><a name="a530c6b4c02be4e4b9cffc97681278d3a"></a>Cluster billing mode</p>
</td>
</tr>
<tr id="rcdd45dcfa0dc441e96d6458efb401d8a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a811da5e5dff644b0b8711bd3c6941315"><a name="a811da5e5dff644b0b8711bd3c6941315"></a><a name="a811da5e5dff644b0b8711bd3c6941315"></a>dataCenter</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a09aa2e2429404f2d9a33a24037785148"><a name="a09aa2e2429404f2d9a33a24037785148"></a><a name="a09aa2e2429404f2d9a33a24037785148"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="afbf19bcde3394cfeb9c3cec84ed768f2"><a name="afbf19bcde3394cfeb9c3cec84ed768f2"></a><a name="afbf19bcde3394cfeb9c3cec84ed768f2"></a>Cluster work region</p>
</td>
</tr>
<tr id="r806be8a4d61041a48f773e470b8430be"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a174fb6437a214b1d955c9712cb6d3586"><a name="a174fb6437a214b1d955c9712cb6d3586"></a><a name="a174fb6437a214b1d955c9712cb6d3586"></a>vpc</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a498f167b670a46cd9ebabc30f81f2cf2"><a name="a498f167b670a46cd9ebabc30f81f2cf2"></a><a name="a498f167b670a46cd9ebabc30f81f2cf2"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a735c95fa42b34be0a98c3275c678846c"><a name="a735c95fa42b34be0a98c3275c678846c"></a><a name="a735c95fa42b34be0a98c3275c678846c"></a>VPC name</p>
</td>
</tr>
<tr id="r2506a47b261246c7b9717a40e29d8e39"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a5e0a0aa004df45e8872b87588765a71a"><a name="a5e0a0aa004df45e8872b87588765a71a"></a><a name="a5e0a0aa004df45e8872b87588765a71a"></a>fee</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a23ddcb5894904fd6a856057e4b39079f"><a name="a23ddcb5894904fd6a856057e4b39079f"></a><a name="a23ddcb5894904fd6a856057e4b39079f"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a9f4564f1b0f04eb695f35256648390a4"><a name="a9f4564f1b0f04eb695f35256648390a4"></a><a name="a9f4564f1b0f04eb695f35256648390a4"></a>Cluster creation fee, which is automatically calculated</p>
</td>
</tr>
<tr id="rc2bb1033a81d4eefa8bed28eb88e2cde"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110581913_p685107915313"><a name="en-us_topic_0110581913_p685107915313"></a><a name="en-us_topic_0110581913_p685107915313"></a>hadoopVersion</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a28bf87170a4f4e7f82ae07f5bd34e99b"><a name="a28bf87170a4f4e7f82ae07f5bd34e99b"></a><a name="a28bf87170a4f4e7f82ae07f5bd34e99b"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a46c1f8c48df54e63be3d7a9bc0c81c42"><a name="a46c1f8c48df54e63be3d7a9bc0c81c42"></a><a name="a46c1f8c48df54e63be3d7a9bc0c81c42"></a>Hadoop version</p>
</td>
</tr>
<tr id="r19a9d028587a4b51b0c8c4e2810b892b"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a933b18ebd0cd43ee88a7275a9769c6b9"><a name="a933b18ebd0cd43ee88a7275a9769c6b9"></a><a name="a933b18ebd0cd43ee88a7275a9769c6b9"></a>masterNodeSize</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ab85dea4d975b4ac88456d975082f2792"><a name="ab85dea4d975b4ac88456d975082f2792"></a><a name="ab85dea4d975b4ac88456d975082f2792"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ab059544a106845ac9f20977b6b5648d1"><a name="ab059544a106845ac9f20977b6b5648d1"></a><a name="ab059544a106845ac9f20977b6b5648d1"></a>Instance specifications of a Master node </p>
</td>
</tr>
<tr id="r43f1c0b3b1014929aaf8d5d2e5d5c847"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a16e80e6b671447b09f2abdb5aa6d41c4"><a name="a16e80e6b671447b09f2abdb5aa6d41c4"></a><a name="a16e80e6b671447b09f2abdb5aa6d41c4"></a>coreNodeSize</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a046b1ef2861f40d18ecf63c58ba7d364"><a name="a046b1ef2861f40d18ecf63c58ba7d364"></a><a name="a046b1ef2861f40d18ecf63c58ba7d364"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a98351f1daca34fc7a812972a2079b755"><a name="a98351f1daca34fc7a812972a2079b755"></a><a name="a98351f1daca34fc7a812972a2079b755"></a>Instance specifications of a Core node </p>
</td>
</tr>
<tr id="r25cc638379e74ef996650fc7a23ea281"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ab5e2f08e0dd84cd190f840772177973c"><a name="ab5e2f08e0dd84cd190f840772177973c"></a><a name="ab5e2f08e0dd84cd190f840772177973c"></a>componentList</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="aa3bd46eecfd14b138cc1a2c428022693"><a name="aa3bd46eecfd14b138cc1a2c428022693"></a><a name="aa3bd46eecfd14b138cc1a2c428022693"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ae1fbfbb60d0b4d2ea58c3a929e1d0724"><a name="ae1fbfbb60d0b4d2ea58c3a929e1d0724"></a><a name="ae1fbfbb60d0b4d2ea58c3a929e1d0724"></a>Component list. For details, see <a href="#tfad8f6bab79e4a158065bed4334934f2">Table 4</a>.</p>
</td>
</tr>
<tr id="r761c9c01517240cd865957c647c5a2bd"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a52a78b309a204abaad4998af393e1d99"><a name="a52a78b309a204abaad4998af393e1d99"></a><a name="a52a78b309a204abaad4998af393e1d99"></a>externalIp</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a48f42532d04045d4ad2bf39c18d25ee1"><a name="a48f42532d04045d4ad2bf39c18d25ee1"></a><a name="a48f42532d04045d4ad2bf39c18d25ee1"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a42d7deb5457f4b87ae028061458b1543"><a name="a42d7deb5457f4b87ae028061458b1543"></a><a name="a42d7deb5457f4b87ae028061458b1543"></a>External IP address</p>
</td>
</tr>
<tr id="r489b2da1b1ce484e880510cc66b8f11d"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a32e4d567645d42779af568514080ffb6"><a name="a32e4d567645d42779af568514080ffb6"></a><a name="a32e4d567645d42779af568514080ffb6"></a>externalAlternateIp</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a48b6c18cf75b40e39bcfeb6db940c79d"><a name="a48b6c18cf75b40e39bcfeb6db940c79d"></a><a name="a48b6c18cf75b40e39bcfeb6db940c79d"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a180df81bdff448a798fbdfac00aa0439"><a name="a180df81bdff448a798fbdfac00aa0439"></a><a name="a180df81bdff448a798fbdfac00aa0439"></a>Backup external IP address</p>
</td>
</tr>
<tr id="r7febf00c6df34dbc9949ade0d616ecd9"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a3341680efae549a0b38ea8988f0332e0"><a name="a3341680efae549a0b38ea8988f0332e0"></a><a name="a3341680efae549a0b38ea8988f0332e0"></a>internalIp</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ac2d4729cec47455db8aacd06535bcce5"><a name="ac2d4729cec47455db8aacd06535bcce5"></a><a name="ac2d4729cec47455db8aacd06535bcce5"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a3a94a1a2ed2c442f9224dd59bad9bae1"><a name="a3a94a1a2ed2c442f9224dd59bad9bae1"></a><a name="a3a94a1a2ed2c442f9224dd59bad9bae1"></a>Internal IP address</p>
</td>
</tr>
<tr id="r88b199831b464409b39cec1f0181738c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="af2de7dea9b3b46a9914d25395494a2e1"><a name="af2de7dea9b3b46a9914d25395494a2e1"></a><a name="af2de7dea9b3b46a9914d25395494a2e1"></a>deploymentId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ada9ff11421ea4ac389a5f4e0b8f87e97"><a name="ada9ff11421ea4ac389a5f4e0b8f87e97"></a><a name="ada9ff11421ea4ac389a5f4e0b8f87e97"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a812fbea211da4029b49cb8a252e62f02"><a name="a812fbea211da4029b49cb8a252e62f02"></a><a name="a812fbea211da4029b49cb8a252e62f02"></a>Cluster deployment ID</p>
</td>
</tr>
<tr id="raee1d1dd8ea5493085e26fcb2c55b686"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="af163dd44edb849f1a1e324ace1678c95"><a name="af163dd44edb849f1a1e324ace1678c95"></a><a name="af163dd44edb849f1a1e324ace1678c95"></a>remark</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ac505f9599e5946f4ae79c99619803217"><a name="ac505f9599e5946f4ae79c99619803217"></a><a name="ac505f9599e5946f4ae79c99619803217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a2723d8cb336741629429a7bb471b7fda"><a name="a2723d8cb336741629429a7bb471b7fda"></a><a name="a2723d8cb336741629429a7bb471b7fda"></a>Cluster remarks</p>
</td>
</tr>
<tr id="r8175a338db8647c9be3a4049e0c4b0cf"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110581913_p67821615426"><a name="en-us_topic_0110581913_p67821615426"></a><a name="en-us_topic_0110581913_p67821615426"></a>orderId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a0f5289c1691143faa01b9f0b2599598c"><a name="a0f5289c1691143faa01b9f0b2599598c"></a><a name="a0f5289c1691143faa01b9f0b2599598c"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="afa7402e6e5644953a74756c85bcaf8ab"><a name="afa7402e6e5644953a74756c85bcaf8ab"></a><a name="afa7402e6e5644953a74756c85bcaf8ab"></a>Cluster creation order ID</p>
</td>
</tr>
<tr id="rd2a271efb3444a3c973c2c8eb0cd236d"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ac3ceaa2c06ba4c2f803043904e4b7f69"><a name="ac3ceaa2c06ba4c2f803043904e4b7f69"></a><a name="ac3ceaa2c06ba4c2f803043904e4b7f69"></a>azId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a2e115e3b36574f45a2c6f6447b272345"><a name="a2e115e3b36574f45a2c6f6447b272345"></a><a name="a2e115e3b36574f45a2c6f6447b272345"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="af6c65067fc23440b91b567cc210fedd5"><a name="af6c65067fc23440b91b567cc210fedd5"></a><a name="af6c65067fc23440b91b567cc210fedd5"></a>AZ ID</p>
</td>
</tr>
<tr id="r0cad9be84e4a4984b61d73eba43431dc"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ae65c11e43bfc42f797554088975921dd"><a name="ae65c11e43bfc42f797554088975921dd"></a><a name="ae65c11e43bfc42f797554088975921dd"></a>masterNodeProductId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a29180b491638472ebc25174507033906"><a name="a29180b491638472ebc25174507033906"></a><a name="a29180b491638472ebc25174507033906"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ad1df1119b23f4a1982fa0322faffebb8"><a name="ad1df1119b23f4a1982fa0322faffebb8"></a><a name="ad1df1119b23f4a1982fa0322faffebb8"></a>Product ID of a Master node</p>
</td>
</tr>
<tr id="r1f29de2d879945419160b62d43761815"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a9c1a37a760284d0d82d12542962f692c"><a name="a9c1a37a760284d0d82d12542962f692c"></a><a name="a9c1a37a760284d0d82d12542962f692c"></a>masterNodeSpecId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a830082c006f648339fb32ad91c9ab4e5"><a name="a830082c006f648339fb32ad91c9ab4e5"></a><a name="a830082c006f648339fb32ad91c9ab4e5"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a34e1e9e36d1945759125732545d36204"><a name="a34e1e9e36d1945759125732545d36204"></a><a name="a34e1e9e36d1945759125732545d36204"></a>Specification ID of a Master node</p>
</td>
</tr>
<tr id="rd4fe029568d54cfdb03c68c5b8e0975c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a2e65010710f54cb8a8bf3ede666ac7db"><a name="a2e65010710f54cb8a8bf3ede666ac7db"></a><a name="a2e65010710f54cb8a8bf3ede666ac7db"></a>coreNodeProductId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="af650b02421ea4996a4c3dd18426ac35a"><a name="af650b02421ea4996a4c3dd18426ac35a"></a><a name="af650b02421ea4996a4c3dd18426ac35a"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aa7499f07b4cd4eb1b696fb07637937df"><a name="aa7499f07b4cd4eb1b696fb07637937df"></a><a name="aa7499f07b4cd4eb1b696fb07637937df"></a>Product ID of a Core node</p>
</td>
</tr>
<tr id="rdbee90a2d07145b8a9b9fe27af32b29c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="acb2f12bb03c342c1a3937090d3e664fc"><a name="acb2f12bb03c342c1a3937090d3e664fc"></a><a name="acb2f12bb03c342c1a3937090d3e664fc"></a>coreNodeSpecId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a40d90f0817fd4221ac6c533a50f4985a"><a name="a40d90f0817fd4221ac6c533a50f4985a"></a><a name="a40d90f0817fd4221ac6c533a50f4985a"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a547bca118bf54942b3957f2d4895c857"><a name="a547bca118bf54942b3957f2d4895c857"></a><a name="a547bca118bf54942b3957f2d4895c857"></a>Specification ID of a Core node</p>
</td>
</tr>
<tr id="r93411bd5da6d4ff6bce357191b6cd3e5"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aeea73aeac7aa42ebaf15d2b41669e44d"><a name="aeea73aeac7aa42ebaf15d2b41669e44d"></a><a name="aeea73aeac7aa42ebaf15d2b41669e44d"></a>azName</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a4d0660d64b314a35bd4a80d130265735"><a name="a4d0660d64b314a35bd4a80d130265735"></a><a name="a4d0660d64b314a35bd4a80d130265735"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a73ff6a78be854ad0b3ec076e6454437a"><a name="a73ff6a78be854ad0b3ec076e6454437a"></a><a name="a73ff6a78be854ad0b3ec076e6454437a"></a>AZ name</p>
</td>
</tr>
<tr id="rf92d002984c24a78a57b33dc2e62eb7c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aa484db932bed45489bbdaa697876de0e"><a name="aa484db932bed45489bbdaa697876de0e"></a><a name="aa484db932bed45489bbdaa697876de0e"></a>instanceId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a0f8d98581eb0476c8aad0ac5969b14ae"><a name="a0f8d98581eb0476c8aad0ac5969b14ae"></a><a name="a0f8d98581eb0476c8aad0ac5969b14ae"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a44e00139633a48a6ba64a941400c7d63"><a name="a44e00139633a48a6ba64a941400c7d63"></a><a name="a44e00139633a48a6ba64a941400c7d63"></a>Instance ID</p>
</td>
</tr>
<tr id="r26e86364bac54a7bbaf768a07d0d4ab5"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="affae8991e4844f32a2ad8f1fca0dd453"><a name="affae8991e4844f32a2ad8f1fca0dd453"></a><a name="affae8991e4844f32a2ad8f1fca0dd453"></a>vnc</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="abbfeaf105a5147c7b43fc3ade0d76d46"><a name="abbfeaf105a5147c7b43fc3ade0d76d46"></a><a name="abbfeaf105a5147c7b43fc3ade0d76d46"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ae0be2badb4db45f7b383dad6d153e465"><a name="ae0be2badb4db45f7b383dad6d153e465"></a><a name="ae0be2badb4db45f7b383dad6d153e465"></a>URI for remotely logging in to an ECS</p>
</td>
</tr>
<tr id="rcf9a3834c9c24805a8cd01c63bc94984"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a61487a81861b4961b154340d21a11250"><a name="a61487a81861b4961b154340d21a11250"></a><a name="a61487a81861b4961b154340d21a11250"></a>tenantId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a0711a7dbc5514e81834d38e9b08aa433"><a name="a0711a7dbc5514e81834d38e9b08aa433"></a><a name="a0711a7dbc5514e81834d38e9b08aa433"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581913_p93786111019"><a name="en-us_topic_0110581913_p93786111019"></a><a name="en-us_topic_0110581913_p93786111019"></a>Project ID</p>
</td>
</tr>
<tr id="r18ed6bea18c1494da28e44db70c57c11"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a4e5826e5d1814c31bb5b70915316d4b9"><a name="a4e5826e5d1814c31bb5b70915316d4b9"></a><a name="a4e5826e5d1814c31bb5b70915316d4b9"></a>volumeSize</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a882533b337f04f4696b0f2a819a25310"><a name="a882533b337f04f4696b0f2a819a25310"></a><a name="a882533b337f04f4696b0f2a819a25310"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a21219a1de55a47bbad02821472e6ef6c"><a name="a21219a1de55a47bbad02821472e6ef6c"></a><a name="a21219a1de55a47bbad02821472e6ef6c"></a>Disk storage space</p>
</td>
</tr>
<tr id="r423ae048fac44a0c80d9c865d2a6f28c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a8d13d4e406574354888da66e3931c3ed"><a name="a8d13d4e406574354888da66e3931c3ed"></a><a name="a8d13d4e406574354888da66e3931c3ed"></a>volumeType</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a38443a303ac34df4acc2885c8f56a189"><a name="a38443a303ac34df4acc2885c8f56a189"></a><a name="a38443a303ac34df4acc2885c8f56a189"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a4eeeeeda939a4917b45d7dde0b401e4a"><a name="a4eeeeeda939a4917b45d7dde0b401e4a"></a><a name="a4eeeeeda939a4917b45d7dde0b401e4a"></a>Disk type</p>
</td>
</tr>
<tr id="rd72d3f36d4234410b19c61f9a94f77d7"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ad4f1b24079fc4ef8a20fcf0e8ebdd205"><a name="ad4f1b24079fc4ef8a20fcf0e8ebdd205"></a><a name="ad4f1b24079fc4ef8a20fcf0e8ebdd205"></a>subnetId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a991b29fb04ee453ca36b2e4a295308f6"><a name="a991b29fb04ee453ca36b2e4a295308f6"></a><a name="a991b29fb04ee453ca36b2e4a295308f6"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581913_p662768111214"><a name="en-us_topic_0110581913_p662768111214"></a><a name="en-us_topic_0110581913_p662768111214"></a>Subnet ID</p>
</td>
</tr>
<tr id="r82f8fee0a317411f853cb7539ec5e370"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110581913_p437573616274"><a name="en-us_topic_0110581913_p437573616274"></a><a name="en-us_topic_0110581913_p437573616274"></a>clusterType</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ab4aad63c16c34ff7b707bac1afab05f8"><a name="ab4aad63c16c34ff7b707bac1afab05f8"></a><a name="ab4aad63c16c34ff7b707bac1afab05f8"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a8359234403964a4892193ecf64d3e17c"><a name="a8359234403964a4892193ecf64d3e17c"></a><a name="a8359234403964a4892193ecf64d3e17c"></a>Cluster type</p>
</td>
</tr>
<tr id="r9df0ce113c0b4a05953d9b92cab48642"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a089c116f70b14b04924b8e6e5d44675e"><a name="a089c116f70b14b04924b8e6e5d44675e"></a><a name="a089c116f70b14b04924b8e6e5d44675e"></a>subnetName</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0110581913_p856954216274"><a name="en-us_topic_0110581913_p856954216274"></a><a name="en-us_topic_0110581913_p856954216274"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a803a71410f9749bea2a17239904e01e3"><a name="a803a71410f9749bea2a17239904e01e3"></a><a name="a803a71410f9749bea2a17239904e01e3"></a>Subnet name</p>
</td>
</tr>
<tr id="r43a604234cd4424c98fb349ef0db8757"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a08c73591f78e401fac62d0f02ef93199"><a name="a08c73591f78e401fac62d0f02ef93199"></a><a name="a08c73591f78e401fac62d0f02ef93199"></a>securityGroupsId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a81bb2e908afd4f2192fc813ff16ed122"><a name="a81bb2e908afd4f2192fc813ff16ed122"></a><a name="a81bb2e908afd4f2192fc813ff16ed122"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a11f63406b963425bbf2c928158e44ca4"><a name="a11f63406b963425bbf2c928158e44ca4"></a><a name="a11f63406b963425bbf2c928158e44ca4"></a>Security group ID</p>
</td>
</tr>
<tr id="r75716ff264b143bdb1c747829fde1d08"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a42af07eff7ad462bb508c763a9fd800e"><a name="a42af07eff7ad462bb508c763a9fd800e"></a><a name="a42af07eff7ad462bb508c763a9fd800e"></a>slaveSecurityGroupsId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0110581913_p592256011214"><a name="en-us_topic_0110581913_p592256011214"></a><a name="en-us_topic_0110581913_p592256011214"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581913_p996533211214"><a name="en-us_topic_0110581913_p996533211214"></a><a name="en-us_topic_0110581913_p996533211214"></a>Security group ID of a non-Master node. Currently, one MRS cluster uses only one security group. Therefore, this field has been discarded.</p>
</td>
</tr>
<tr id="rbd484563b118440482cdc77d05e6b595"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a24f81ddb125c48bbb1a1f10513858df7"><a name="a24f81ddb125c48bbb1a1f10513858df7"></a><a name="a24f81ddb125c48bbb1a1f10513858df7"></a>stageDesc</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a819e20ff9367457ea952563e0e5fd585"><a name="a819e20ff9367457ea952563e0e5fd585"></a><a name="a819e20ff9367457ea952563e0e5fd585"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a3570ebeb1f2648d18eb2fb2b8b9966ff"><a name="a3570ebeb1f2648d18eb2fb2b8b9966ff"></a><a name="a3570ebeb1f2648d18eb2fb2b8b9966ff"></a>Cluster operation progress description</p>
<div class="p" id="a16b05e2c057646c49d5972aacbb62b97"><a name="a16b05e2c057646c49d5972aacbb62b97"></a><a name="a16b05e2c057646c49d5972aacbb62b97"></a>The cluster installation progress includes:<a name="ue74d13dece3147ef838b2d7ac22f1369"></a><a name="ue74d13dece3147ef838b2d7ac22f1369"></a><ul id="ue74d13dece3147ef838b2d7ac22f1369"><li>Verifying cluster parameters: Cluster parameters are being verified.</li><li>Applying for cluster resources: Cluster resources are being applied for.</li><li>Creating VMs: The VMs are being created.</li><li>Initializing VMs: The VMs are being initialized.</li><li>Installing MRS Manager: MRS Manager is being installed.</li><li>Deploying the cluster: The cluster is being deployed.</li><li>Cluster installation failed: Failed to install the cluster.</li></ul>
</div>
<div class="p" id="acf692a12a1c143528b5818c8127f6686"><a name="acf692a12a1c143528b5818c8127f6686"></a><a name="acf692a12a1c143528b5818c8127f6686"></a>The cluster scale-out progress includes:<a name="u91f4c5595c6a46ac8ac6f948c18cbff1"></a><a name="u91f4c5595c6a46ac8ac6f948c18cbff1"></a><ul id="u91f4c5595c6a46ac8ac6f948c18cbff1"><li>Preparing for scale-out: Cluster scale-out is being prepared.</li><li>Creating VMs: The VMs are being created.</li><li>Initializing VMs: The VMs are being initialized.</li><li>Adding nodes to the cluster: The nodes are being added to the cluster.</li><li>Scale-out failed: Failed to scale out the cluster.</li></ul>
</div>
<div class="p" id="af5e822f0cc1c498d9acd6e6589f8c434"><a name="af5e822f0cc1c498d9acd6e6589f8c434"></a><a name="af5e822f0cc1c498d9acd6e6589f8c434"></a>The cluster scale-in progress includes:<a name="u7d2ccc73258c434da1819ece1f35d318"></a><a name="u7d2ccc73258c434da1819ece1f35d318"></a><ul id="u7d2ccc73258c434da1819ece1f35d318"><li>Preparing for scale-in: Cluster scale-in is being prepared.</li><li>Decommissioning instance: The instance is being decommissioned.</li><li>Deleting VMs: The VMs are being deleted.</li><li>Deleting nodes from the cluster: The nodes are being deleted from the cluster.</li><li>Scale-in failed: Failed to scale in the cluster.</li></ul>
</div>
<p id="a243a943d17cc4f9798fb008422540fb1"><a name="a243a943d17cc4f9798fb008422540fb1"></a><a name="a243a943d17cc4f9798fb008422540fb1"></a>If the cluster installation, scale-out, or scale-in fails, <strong id="b84235270619322"><a name="b84235270619322"></a><a name="b84235270619322"></a>stageDesc</strong> will display the failure cause. For details, see <a href="resizing-a-cluster.md#table5548695114444">Table 6</a>.</p>
</td>
</tr>
<tr id="r4bb0d14a6e7545b5bbfaf51c738f2a1d"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a8bb043be751a482eb767b6090d72eda0"><a name="a8bb043be751a482eb767b6090d72eda0"></a><a name="a8bb043be751a482eb767b6090d72eda0"></a>mrsManagerFinish</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ac5923002e94e43559763ac5b5962d9ff"><a name="ac5923002e94e43559763ac5b5962d9ff"></a><a name="ac5923002e94e43559763ac5b5962d9ff"></a>boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a7603bccf23574b7e81a389d95f98bf83"><a name="a7603bccf23574b7e81a389d95f98bf83"></a><a name="a7603bccf23574b7e81a389d95f98bf83"></a>Whether MRS Manager installation is finished during cluster creation</p>
<a name="u48b2d769e6b54c1881357cba6123a789"></a><a name="u48b2d769e6b54c1881357cba6123a789"></a><ul id="u48b2d769e6b54c1881357cba6123a789"><li>true: MRS Manager installation is finished.</li><li>false: MRS Manager installation is not finished.</li></ul>
</td>
</tr>
<tr id="re97b216b845447fa9b711456e4708d74"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aedfcb28940584313aea8567938cc7ad6"><a name="aedfcb28940584313aea8567938cc7ad6"></a><a name="aedfcb28940584313aea8567938cc7ad6"></a>safeMode</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0110581913_p665372211214"><a name="en-us_topic_0110581913_p665372211214"></a><a name="en-us_topic_0110581913_p665372211214"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581913_p208064211214"><a name="en-us_topic_0110581913_p208064211214"></a><a name="en-us_topic_0110581913_p208064211214"></a>Running mode of an MRS cluster</p>
<a name="ud4b3a41b5dde4ff98fbcc8bfc4fbb0c2"></a><a name="ud4b3a41b5dde4ff98fbcc8bfc4fbb0c2"></a><ul id="ud4b3a41b5dde4ff98fbcc8bfc4fbb0c2"><li>0: normal cluster</li><li>1: security cluster</li></ul>
</td>
</tr>
<tr id="r5f5e7fe25e854055b542fee9c42f90a3"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a68e087f6e38c41c0a942814c9ef9b935"><a name="a68e087f6e38c41c0a942814c9ef9b935"></a><a name="a68e087f6e38c41c0a942814c9ef9b935"></a>clusterVersion</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a9bb71a7635d246af9dfab653889a1d5f"><a name="a9bb71a7635d246af9dfab653889a1d5f"></a><a name="a9bb71a7635d246af9dfab653889a1d5f"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a970fc2d287534450afb3368eb5dc4e22"><a name="a970fc2d287534450afb3368eb5dc4e22"></a><a name="a970fc2d287534450afb3368eb5dc4e22"></a>Cluster version</p>
</td>
</tr>
<tr id="r844af456b7ae4ece9ad657908fd675ed"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110581913_p428413211214"><a name="en-us_topic_0110581913_p428413211214"></a><a name="en-us_topic_0110581913_p428413211214"></a>nodePublicCertName</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="afd9a60aca7dd490f84bc942540779336"><a name="afd9a60aca7dd490f84bc942540779336"></a><a name="afd9a60aca7dd490f84bc942540779336"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a0548a5f95fea45258d214f4b54f731fd"><a name="a0548a5f95fea45258d214f4b54f731fd"></a><a name="a0548a5f95fea45258d214f4b54f731fd"></a>Name of the key file</p>
</td>
</tr>
<tr id="r4b50a6d872514a049a1a91b290a89ce5"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="af7a1c77a46824a35ab16ae98c10b3dea"><a name="af7a1c77a46824a35ab16ae98c10b3dea"></a><a name="af7a1c77a46824a35ab16ae98c10b3dea"></a>masterNodeIp</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a888773b7f43544f68706a93787447dda"><a name="a888773b7f43544f68706a93787447dda"></a><a name="a888773b7f43544f68706a93787447dda"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581913_p70885811214"><a name="en-us_topic_0110581913_p70885811214"></a><a name="en-us_topic_0110581913_p70885811214"></a>IP address of a Master node</p>
</td>
</tr>
<tr id="r59426445e326481fb5b65a617eefad1e"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aa210721845244eee95122c4684988ed4"><a name="aa210721845244eee95122c4684988ed4"></a><a name="aa210721845244eee95122c4684988ed4"></a>privateIpFirst</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a052007f87d4a4487a9d71d1631f640cd"><a name="a052007f87d4a4487a9d71d1631f640cd"></a><a name="a052007f87d4a4487a9d71d1631f640cd"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a5a5d0c9ff30e4f8f93451fe0faf3af0e"><a name="a5a5d0c9ff30e4f8f93451fe0faf3af0e"></a><a name="a5a5d0c9ff30e4f8f93451fe0faf3af0e"></a>Preferred private IP address</p>
</td>
</tr>
<tr id="rd7f7d659d77a440d858d0ed29a6c8fb1"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ac3432e3ddc024ce6b05b66f3fe202daf"><a name="ac3432e3ddc024ce6b05b66f3fe202daf"></a><a name="ac3432e3ddc024ce6b05b66f3fe202daf"></a>errorInfo</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ade9c6dca6e71490bb3676ae8bc272a7b"><a name="ade9c6dca6e71490bb3676ae8bc272a7b"></a><a name="ade9c6dca6e71490bb3676ae8bc272a7b"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a454a54af97c44b9491abe66caf87a652"><a name="a454a54af97c44b9491abe66caf87a652"></a><a name="a454a54af97c44b9491abe66caf87a652"></a>Error message</p>
</td>
</tr>
<tr id="r9aa84084fb9746d09a6a1089882a633c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a4c061b5b747d4e61bc510282a91f0a33"><a name="a4c061b5b747d4e61bc510282a91f0a33"></a><a name="a4c061b5b747d4e61bc510282a91f0a33"></a>chargingStartTime</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a9d8cbb73ce01413ab97bfe1a9972985d"><a name="a9d8cbb73ce01413ab97bfe1a9972985d"></a><a name="a9d8cbb73ce01413ab97bfe1a9972985d"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a4312b91de5fe4f929274da0f289789d3"><a name="a4312b91de5fe4f929274da0f289789d3"></a><a name="a4312b91de5fe4f929274da0f289789d3"></a>Start time of billing</p>
</td>
</tr>
<tr id="r91d1969782a84e4d9e1d5a029bcf367b"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a1caa7c0a5b09413689d1f94bd39ec06f"><a name="a1caa7c0a5b09413689d1f94bd39ec06f"></a><a name="a1caa7c0a5b09413689d1f94bd39ec06f"></a>logCollection</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a4bbab8f9d5614608add5ed3f5155b385"><a name="a4bbab8f9d5614608add5ed3f5155b385"></a><a name="a4bbab8f9d5614608add5ed3f5155b385"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a743fb829700c4d0d84f482ff60b7898a"><a name="a743fb829700c4d0d84f482ff60b7898a"></a><a name="a743fb829700c4d0d84f482ff60b7898a"></a>Whether to collect logs when cluster installation fails</p>
<a name="u131b9eca681f439387fd675dc04041ac"></a><a name="u131b9eca681f439387fd675dc04041ac"></a><ul id="u131b9eca681f439387fd675dc04041ac"><li>0: Do not collect</li><li>1: Collect</li></ul>
</td>
</tr>
<tr id="r31d596980e6c4b66af97b3a1be93cb9f"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="adb071e0d669d46e9b1d510fe2e59dbd9"><a name="adb071e0d669d46e9b1d510fe2e59dbd9"></a><a name="adb071e0d669d46e9b1d510fe2e59dbd9"></a>taskNodeGroups</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p152220981413"><a name="p152220981413"></a><a name="p152220981413"></a>List&lt;NodeGroup&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a494d753a893647929e4d29561697e62a"><a name="a494d753a893647929e4d29561697e62a"></a><a name="a494d753a893647929e4d29561697e62a"></a>List of Task nodes For more parameter description, see <a href="#t8c0e29f53f5d4b5da5cba38419aac352">Table 5</a>.</p>
</td>
</tr>
<tr id="row164542381215"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1946152361218"><a name="p1946152361218"></a><a name="p1946152361218"></a>nodeGroups</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p132453481216"><a name="p132453481216"></a><a name="p132453481216"></a>List&lt;NodeGroup&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p8324113411215"><a name="p8324113411215"></a><a name="p8324113411215"></a>List of Master, Core and Task nodes For more parameter description, see <a href="#t8c0e29f53f5d4b5da5cba38419aac352">Table 5</a>.</p>
</td>
</tr>
<tr id="r10d1ac7d13ac4bbcbca2163c4dd6d1f4"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a8f4558640d5148b996c1084dfae5b6fd"><a name="a8f4558640d5148b996c1084dfae5b6fd"></a><a name="a8f4558640d5148b996c1084dfae5b6fd"></a>masterDataVolumeType</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a31a8ac04203e4dc9a816c2429b8f9ee9"><a name="a31a8ac04203e4dc9a816c2429b8f9ee9"></a><a name="a31a8ac04203e4dc9a816c2429b8f9ee9"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a34de1f0bdd944951b872fc9c2214fe80"><a name="a34de1f0bdd944951b872fc9c2214fe80"></a><a name="a34de1f0bdd944951b872fc9c2214fe80"></a>Data disk storage type of the Master node. Currently, SATA, SAS, and SSD are supported.</p>
</td>
</tr>
<tr id="r30ff57f79280497e9924838d681f4fd0"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a4a9c7d960c954f65adfcfdde38dd4a86"><a name="a4a9c7d960c954f65adfcfdde38dd4a86"></a><a name="a4a9c7d960c954f65adfcfdde38dd4a86"></a>masterDataVolumeSize</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="affa8aebf69344776bd4c13e989faa1aa"><a name="affa8aebf69344776bd4c13e989faa1aa"></a><a name="affa8aebf69344776bd4c13e989faa1aa"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a27214fc130684d8a95bd09d05118e220"><a name="a27214fc130684d8a95bd09d05118e220"></a><a name="a27214fc130684d8a95bd09d05118e220"></a>Data disk storage space of the Master node To increase data storage capacity, you can add disks at the same time when creating a cluster.</p>
<p id="a28cfd68281d04f0790270cef365e3b72"><a name="a28cfd68281d04f0790270cef365e3b72"></a><a name="a28cfd68281d04f0790270cef365e3b72"></a>Value range: 100 GB to 32,000 GB</p>
</td>
</tr>
<tr id="r07529c11e0b64712b12127324cf51d13"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a3a02e96cdead45bc86550cfab241f630"><a name="a3a02e96cdead45bc86550cfab241f630"></a><a name="a3a02e96cdead45bc86550cfab241f630"></a>masterDataVolumeCount</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ab9b3b0a4698d43d6b6b194ee88573ac0"><a name="ab9b3b0a4698d43d6b6b194ee88573ac0"></a><a name="ab9b3b0a4698d43d6b6b194ee88573ac0"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aa3cd953c8c75497fb799580825893f4c"><a name="aa3cd953c8c75497fb799580825893f4c"></a><a name="aa3cd953c8c75497fb799580825893f4c"></a>Number of data disks of the Master node</p>
<p id="aaa20197f0e6b4187a39c6dd944e34c4e"><a name="aaa20197f0e6b4187a39c6dd944e34c4e"></a><a name="aaa20197f0e6b4187a39c6dd944e34c4e"></a>The value can be set to <strong id="b1452211450484"><a name="b1452211450484"></a><a name="b1452211450484"></a>1</strong> only.</p>
</td>
</tr>
<tr id="r72189a5406e64cda902c9a5a3ec368e1"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a66d66a833e324237b9687e0ad7b2339a"><a name="a66d66a833e324237b9687e0ad7b2339a"></a><a name="a66d66a833e324237b9687e0ad7b2339a"></a>coreDataVolumeType</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a6b7ba8936aa941ee8cebb6115116d939"><a name="a6b7ba8936aa941ee8cebb6115116d939"></a><a name="a6b7ba8936aa941ee8cebb6115116d939"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a06f6aa38f451463984249c73b7d493a4"><a name="a06f6aa38f451463984249c73b7d493a4"></a><a name="a06f6aa38f451463984249c73b7d493a4"></a>Data disk storage type of the Core node. Currently, SATA, SAS, and SSD are supported.</p>
</td>
</tr>
<tr id="rce8d9726fa244b7ea0f54556ce1c05ef"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a7a5743ed341745bebfe5ff8dddbe793d"><a name="a7a5743ed341745bebfe5ff8dddbe793d"></a><a name="a7a5743ed341745bebfe5ff8dddbe793d"></a>coreDataVolumeSize</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a6e77b6ecd0af4528a2ba1c4d850f4e76"><a name="a6e77b6ecd0af4528a2ba1c4d850f4e76"></a><a name="a6e77b6ecd0af4528a2ba1c4d850f4e76"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a161c0c12698e455187be966384aa9010"><a name="a161c0c12698e455187be966384aa9010"></a><a name="a161c0c12698e455187be966384aa9010"></a>Data disk storage space of the Core node. To increase data storage capacity, you can add disks at the same time when creating a cluster.</p>
<p id="a0e5ceede566d43fda96c8940a1da355f"><a name="a0e5ceede566d43fda96c8940a1da355f"></a><a name="a0e5ceede566d43fda96c8940a1da355f"></a>Value range: 100 GB to 32,000 GB</p>
</td>
</tr>
<tr id="r737115818d9a43faa4c5830053ae6da8"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a61f7d0b2e0e145029af455e89dc8e957"><a name="a61f7d0b2e0e145029af455e89dc8e957"></a><a name="a61f7d0b2e0e145029af455e89dc8e957"></a>coreDataVolumeCount</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="abf13c2f764b644a38fca1da6c35d8968"><a name="abf13c2f764b644a38fca1da6c35d8968"></a><a name="abf13c2f764b644a38fca1da6c35d8968"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a9021e5bee83b4c5a8d2441c557c16c6a"><a name="a9021e5bee83b4c5a8d2441c557c16c6a"></a><a name="a9021e5bee83b4c5a8d2441c557c16c6a"></a>Number of data disks of the Core node.</p>
<p id="a02a49ecc50784040afa2c34e97011d87"><a name="a02a49ecc50784040afa2c34e97011d87"></a><a name="a02a49ecc50784040afa2c34e97011d87"></a>Value range: 1 to 10</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **componentList**  parameter description

<a name="tfad8f6bab79e4a158065bed4334934f2"></a>
<table><thead align="left"><tr id="r5cdd583aca4b4755881b19b62f09ccec"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="ac254da0dab1441ec92a6b33f1a6eb0b3"><a name="ac254da0dab1441ec92a6b33f1a6eb0b3"></a><a name="ac254da0dab1441ec92a6b33f1a6eb0b3"></a><strong id="b8888954155013"><a name="b8888954155013"></a><a name="b8888954155013"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="a8b1273cf6c0140e6b474ce7c8d105e6c"><a name="a8b1273cf6c0140e6b474ce7c8d105e6c"></a><a name="a8b1273cf6c0140e6b474ce7c8d105e6c"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="en-us_topic_0110581913_p949969815937"><a name="en-us_topic_0110581913_p949969815937"></a><a name="en-us_topic_0110581913_p949969815937"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r39314b8086f442f48eda8af464423342"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aed175543b6454ef9ad425f18d592120e"><a name="aed175543b6454ef9ad425f18d592120e"></a><a name="aed175543b6454ef9ad425f18d592120e"></a>componentId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a69d7a7e94eb344b49a7baf4aabe6e2c6"><a name="a69d7a7e94eb344b49a7baf4aabe6e2c6"></a><a name="a69d7a7e94eb344b49a7baf4aabe6e2c6"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a2cbc5a24356749c3ac36314ab4c3f090"><a name="a2cbc5a24356749c3ac36314ab4c3f090"></a><a name="a2cbc5a24356749c3ac36314ab4c3f090"></a>Component ID</p>
<a name="ul193151412181318"></a><a name="ul193151412181318"></a><ul id="ul193151412181318"><li>Component IDs of MRS 2.1.0 are as follows: <a name="ul23161412191313"></a><a name="ul23161412191313"></a><ul id="ul23161412191313"><li>MRS 2.1.0_001: Hadoop</li><li>MRS 2.1.0_002: Spark</li><li>MRS 2.1.0_003: HBase</li><li>MRS 2.1.0_004: Hive</li><li>MRS 2.1.0_005: Hue</li><li>MRS 2.1.0_006: Kafka</li><li>MRS 2.1.0_007: Storm</li><li>MRS 2.1.0_008: Loader</li><li>MRS 2.1.0_009: Flume</li><li>MRS 2.1.0_010: Tez</li><li>MRS 2.1.0_011: Presto</li><li>MRS 2.1.0_014: Flink</li></ul>
</li></ul>
<a name="ul157259529017"></a><a name="ul157259529017"></a><ul id="ul157259529017"><li>Component IDs of MRS 1.9.2 are as follows: <a name="ul918122913275"></a><a name="ul918122913275"></a><ul id="ul918122913275"><li>MRS 1.9.2_001: Hadoop</li><li>MRS 1.9.2_002: Spark</li><li>MRS 1.9.2_003: HBase</li><li>MRS 1.9.2_004: Hive</li><li>MRS 1.9.2_005: Hue</li><li>MRS 1.9.2_006: Kafka</li><li>MRS 1.9.2_007: Storm</li><li>MRS 1.9.2_008: Loader</li><li>MRS 1.9.2_009: Flume</li><li>MRS 1.9.2_010: Presto</li><li>MRS 1.9.2_011: KafkaManager</li><li>MRS 1.9.2_012: Flink</li><li>MRS 1.9.2_013: OpenTSDB</li><li>MRS 1.9.2_015: Alluxio</li><li>MRS 1.9.2_16: Ranger</li><li>MRS 1.9.2_17: Tez</li></ul>
</li><li>Component IDs of MRS 1.7.2 and MRS 1.6.3 are as follows:<a name="ul1379931812111"></a><a name="ul1379931812111"></a><ul id="ul1379931812111"><li>MRS 1.7.2_001: Hadoop</li><li>MRS 1.7.2_002: Spark</li><li>MRS 1.7.2_003: HBase</li><li>MRS 1.7.2_004: Hive</li><li>MRS 1.7.2_005: Hue</li><li>MRS 1.7.2_006: Kafka</li><li>MRS 1.7.2_007: Storm</li><li>MRS 1.7.2_008: Loader</li><li>MRS 1.7.2_009: Flume</li></ul>
</li></ul>
<p id="p666562343819"><a name="p666562343819"></a><a name="p666562343819"></a>For example, the <strong id="b1084011143113"><a name="b1084011143113"></a><a name="b1084011143113"></a>component_id</strong> of Hadoop is MRS 2.1.0_001, MRS 1.9.2_001, MRS 1.7.2_001, or MRS 1.6.3_001.</p>
</td>
</tr>
<tr id="r2786a9524cff4d728bb1e6924db9604f"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ae2fc48462fa9475699eee62f3dd0c571"><a name="ae2fc48462fa9475699eee62f3dd0c571"></a><a name="ae2fc48462fa9475699eee62f3dd0c571"></a>componentName</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a93a9337114124ee3bc25fd02a9e3b3ae"><a name="a93a9337114124ee3bc25fd02a9e3b3ae"></a><a name="a93a9337114124ee3bc25fd02a9e3b3ae"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581913_p601825815950"><a name="en-us_topic_0110581913_p601825815950"></a><a name="en-us_topic_0110581913_p601825815950"></a>Component name</p>
<a name="ul4211784545"></a><a name="ul4211784545"></a><ul id="ul4211784545"><li>MRS 2.1.0 or later support the following components: Presto, Hadoop, Spark, HBase, Hive, Tez, Hue, Loader, Flink, Flume, Kafka, and Storm</li><li>MRS 1.9.2 supports the following components: Presto, Hadoop, Spark, HBase, OpenTSDB, Hive, Hue, Loader, Tez, Flink, Alluxio, Ranger, Flume, Kafka, KafkaManager, and Storm</li><li>MRS 1.7.2 and MRS 1.6.3 support the following components: Hadoop, Spark, HBase, Hive, Hue, Loader, Flume, Kafka, and Storm</li></ul>
</td>
</tr>
<tr id="rdeb58819b19a47c4b396fe25d0ac3d36"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ad027a7c5fda74a5dac59c2e7bf7e8550"><a name="ad027a7c5fda74a5dac59c2e7bf7e8550"></a><a name="ad027a7c5fda74a5dac59c2e7bf7e8550"></a>componentVersion</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a5f3a3feb65b946c38297b7f2c19908fd"><a name="a5f3a3feb65b946c38297b7f2c19908fd"></a><a name="a5f3a3feb65b946c38297b7f2c19908fd"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a87f565dffa3b48f9a22328317768b405"><a name="a87f565dffa3b48f9a22328317768b405"></a><a name="a87f565dffa3b48f9a22328317768b405"></a>Component version</p>
<a name="ul31291258111712"></a><a name="ul31291258111712"></a><ul id="ul31291258111712"><li>MRS 2.1.0 supports the following component versions:<div class="p" id="p623832344416"><a name="p623832344416"></a><a name="p623832344416"></a>Component versions of an analysis cluster:<a name="ul8238122314418"></a><a name="ul8238122314418"></a><ul id="ul8238122314418"><li>Presto: 308</li><li>Hadoop: 3.1.1</li><li>Spark: 2.3.2</li><li>HBase: 2.1.1</li><li>Hive: 3.1.0</li><li>Tez: 0.9.1</li><li>Hue: <span id="text79788306250"><a name="text79788306250"></a><a name="text79788306250"></a>3.11.0</span></li><li>Loader: <span id="text4978130112511"><a name="text4978130112511"></a><a name="text4978130112511"></a>2.0.0</span></li><li>Flink: 1.7.0</li></ul>
</div>
<div class="p" id="p18239182310441"><a name="p18239182310441"></a><a name="p18239182310441"></a>Component versions of a streaming cluster:<a name="ul023912237441"></a><a name="ul023912237441"></a><ul id="ul023912237441"><li>Kafka: 1.1.0</li><li>Storm: 1.2.1</li><li>Flume: <span id="text497918307257"><a name="text497918307257"></a><a name="text497918307257"></a>1.6.0</span></li></ul>
</div>
</li><li>MRS 1.9.2 supports the following component versions:<div class="p" id="p3990164033612"><a name="p3990164033612"></a><a name="p3990164033612"></a>Component versions of an analysis cluster:<a name="ul2099020407363"></a><a name="ul2099020407363"></a><ul id="ul2099020407363"><li>Presto: 0.216</li><li>Hadoop: 2.8.3</li><li>Spark: 2.2.2</li><li>HBase: 1.3.1</li><li>OpenTSDB: 2.3.0</li><li>Hive: 2.3.3</li><li>Hue: <span id="text2796102174115"><a name="text2796102174115"></a><a name="text2796102174115"></a>3.11.0</span></li><li>Loader: <span id="text1181562310410"><a name="text1181562310410"></a><a name="text1181562310410"></a>2.0.0</span></li><li>Tez: 0.9.1</li><li>Flink: 1.7.0</li><li>Alluxio: 2.0.1</li><li>Ranger: 1.0.1</li></ul>
</div>
<div class="p" id="p19991174063615"><a name="p19991174063615"></a><a name="p19991174063615"></a>Component versions of a streaming cluster:<a name="ul39911540123610"></a><a name="ul39911540123610"></a><ul id="ul39911540123610"><li>Kafka: 1.1.0</li><li>KafkaManager: 1.3.3.1</li><li>Storm: 1.2.1</li><li>Flume: <span id="text1415216261"><a name="text1415216261"></a><a name="text1415216261"></a>1.6.0</span></li></ul>
</div>
</li><li>MRS 1.7.2 supports the following component versions:<div class="p" id="p31541581173"><a name="p31541581173"></a><a name="p31541581173"></a>Component versions of an analysis cluster:<a name="ul17160158111712"></a><a name="ul17160158111712"></a><ul id="ul17160158111712"><li>Hadoop: 2.8.3</li><li>Spark: 2.2.1</li><li>HBase: <span id="text682075583020"><a name="text682075583020"></a><a name="text682075583020"></a>1.3.1</span></li><li>Hive: <span id="text16419155793011"><a name="text16419155793011"></a><a name="text16419155793011"></a>1.2.1</span></li><li>Hue: <span id="text1416119361586"><a name="text1416119361586"></a><a name="text1416119361586"></a>3.11.0</span></li><li>Loader: <span id="text644277441"><a name="text644277441"></a><a name="text644277441"></a>2.0.0</span></li></ul>
</div>
<div class="p" id="p132551058131720"><a name="p132551058131720"></a><a name="p132551058131720"></a>Component versions of a streaming cluster:<a name="ul1226119585179"></a><a name="ul1226119585179"></a><ul id="ul1226119585179"><li>Kafka: 0.10.2.0</li><li>Storm: <span id="text02971058101711"><a name="text02971058101711"></a><a name="text02971058101711"></a>1.0.2</span></li><li>Flume: <span id="text999318377582"><a name="text999318377582"></a><a name="text999318377582"></a>1.6.0</span></li></ul>
</div>
</li></ul>
<a name="u6738a612b0cf455592b3bcd33ff9c354"></a><a name="u6738a612b0cf455592b3bcd33ff9c354"></a><ul id="u6738a612b0cf455592b3bcd33ff9c354"><li>MRS 1.6.3 supports the following component versions:<div class="p" id="ae323927123e541b8a490aaebcf7632df"><a name="ae323927123e541b8a490aaebcf7632df"></a><a name="ae323927123e541b8a490aaebcf7632df"></a>Component versions of an analysis cluster:<a name="u04a4ea3e8b3f4048bf440a213250110d"></a><a name="u04a4ea3e8b3f4048bf440a213250110d"></a><ul id="u04a4ea3e8b3f4048bf440a213250110d"><li>Hadoop: <span id="t0f87b3845ded40438cdf1016322a128b"><a name="t0f87b3845ded40438cdf1016322a128b"></a><a name="t0f87b3845ded40438cdf1016322a128b"></a>2.7.2</span></li><li>Spark: 2.1.0</li><li>HBase: <span id="t855985d1b3a54c7b8880dcc78fb9571c"><a name="t855985d1b3a54c7b8880dcc78fb9571c"></a><a name="t855985d1b3a54c7b8880dcc78fb9571c"></a>1.3.1</span></li><li>Hive: <span id="t94e4a14080954d8689219835533c7696"><a name="t94e4a14080954d8689219835533c7696"></a><a name="t94e4a14080954d8689219835533c7696"></a>1.2.1</span></li><li>Hue: <span id="teddc07a7bf2b4ecc8d497039dab5ef6e"><a name="teddc07a7bf2b4ecc8d497039dab5ef6e"></a><a name="teddc07a7bf2b4ecc8d497039dab5ef6e"></a>3.11.0</span></li><li>Loader: <span id="tde62c720d17042dea0cc702abdaefea7"><a name="tde62c720d17042dea0cc702abdaefea7"></a><a name="tde62c720d17042dea0cc702abdaefea7"></a>2.0.0</span></li></ul>
</div>
<div class="p" id="af8e44931e7644cf8a13b9ee363c297e7"><a name="af8e44931e7644cf8a13b9ee363c297e7"></a><a name="af8e44931e7644cf8a13b9ee363c297e7"></a>Component versions of a streaming cluster:<a name="u5afd4973364e44c4b228bf66ffe35503"></a><a name="u5afd4973364e44c4b228bf66ffe35503"></a><ul id="u5afd4973364e44c4b228bf66ffe35503"><li>Kafka: <span id="tee4cc20227124a9c991e3e95d41a3dd9"><a name="tee4cc20227124a9c991e3e95d41a3dd9"></a><a name="tee4cc20227124a9c991e3e95d41a3dd9"></a>0.10.0.0</span></li><li>Storm: <span id="text198413291333"><a name="text198413291333"></a><a name="text198413291333"></a>1.0.2</span></li><li>Flume: <span id="tb130c3fba76444bf9f7722679fd50e95"><a name="tb130c3fba76444bf9f7722679fd50e95"></a><a name="tb130c3fba76444bf9f7722679fd50e95"></a>1.6.0</span></li></ul>
</div>
</li></ul>
</td>
</tr>
<tr id="rff3b68eefb0f4fbd8a889ae3aafdd8cb"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ac4efd0130b414871bbda101ed18b829a"><a name="ac4efd0130b414871bbda101ed18b829a"></a><a name="ac4efd0130b414871bbda101ed18b829a"></a>componentDesc</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a4d6168334a7d49eaa98687dd37b6e759"><a name="a4d6168334a7d49eaa98687dd37b6e759"></a><a name="a4d6168334a7d49eaa98687dd37b6e759"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="abd24f96372cf4ce680ba21c7bc5cbe40"><a name="abd24f96372cf4ce680ba21c7bc5cbe40"></a><a name="abd24f96372cf4ce680ba21c7bc5cbe40"></a>Component description</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **NodeGroup**  parameter description

<a name="t8c0e29f53f5d4b5da5cba38419aac352"></a>
<table><thead align="left"><tr id="rb71a09c44d4845bb9e005db6c92bac3d"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="a94285558ebf148e393ca16fc271aa713"><a name="a94285558ebf148e393ca16fc271aa713"></a><a name="a94285558ebf148e393ca16fc271aa713"></a><strong id="b990316783414"><a name="b990316783414"></a><a name="b990316783414"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="aa72743b5263a4616b05119a37403b12a"><a name="aa72743b5263a4616b05119a37403b12a"></a><a name="aa72743b5263a4616b05119a37403b12a"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="ad9f74d87937e492daff9830ae1eaa065"><a name="ad9f74d87937e492daff9830ae1eaa065"></a><a name="ad9f74d87937e492daff9830ae1eaa065"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r772c2a2c36894025883ba35bf6a9652f"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a21ea093161dc4b28b54210d0214483e5"><a name="a21ea093161dc4b28b54210d0214483e5"></a><a name="a21ea093161dc4b28b54210d0214483e5"></a>groupName</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ab11033caf61a4fa4a86a15439fb5daff"><a name="ab11033caf61a4fa4a86a15439fb5daff"></a><a name="ab11033caf61a4fa4a86a15439fb5daff"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="af8330597bc564ca8b62a4c22f87c0b5b"><a name="af8330597bc564ca8b62a4c22f87c0b5b"></a><a name="af8330597bc564ca8b62a4c22f87c0b5b"></a>Node group name</p>
</td>
</tr>
<tr id="r685acdcd63804970be9df9ccb752824c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a9a6835b784d045deb7520c63ee38ad2e"><a name="a9a6835b784d045deb7520c63ee38ad2e"></a><a name="a9a6835b784d045deb7520c63ee38ad2e"></a>nodeNum</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a92ccc56708e54ecf9a23c77eb3efc231"><a name="a92ccc56708e54ecf9a23c77eb3efc231"></a><a name="a92ccc56708e54ecf9a23c77eb3efc231"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581913_p604125417392"><a name="en-us_topic_0110581913_p604125417392"></a><a name="en-us_topic_0110581913_p604125417392"></a>Number of nodes. The value ranges from 0 to 500. The minimum number of Master and Core nodes is 1 and the total number of Core and Task nodes cannot exceed 500.</p>
</td>
</tr>
<tr id="r3ff0d41b7fa44f67a30507227df1df19"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110581913_p425651111412"><a name="en-us_topic_0110581913_p425651111412"></a><a name="en-us_topic_0110581913_p425651111412"></a>nodeSize</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0110581913_p60006581181"><a name="en-us_topic_0110581913_p60006581181"></a><a name="en-us_topic_0110581913_p60006581181"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="abfaa8eeb949c4ee5a98200fc6528e42e"><a name="abfaa8eeb949c4ee5a98200fc6528e42e"></a><a name="abfaa8eeb949c4ee5a98200fc6528e42e"></a>Instance specifications of a node </p>
</td>
</tr>
<tr id="rfb678198b0ba4844a39f0cf9366168ea"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="af8a5b305e2754841a9490a5bb1984d86"><a name="af8a5b305e2754841a9490a5bb1984d86"></a><a name="af8a5b305e2754841a9490a5bb1984d86"></a>nodeSpecId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a397e7084c91744e386c50135480aff85"><a name="a397e7084c91744e386c50135480aff85"></a><a name="a397e7084c91744e386c50135480aff85"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aa8db59e414e645cc9cb8ec2dc4d7479e"><a name="aa8db59e414e645cc9cb8ec2dc4d7479e"></a><a name="aa8db59e414e645cc9cb8ec2dc4d7479e"></a>Instance specification ID of a node</p>
</td>
</tr>
<tr id="r5e6ec48632bc4a20b39222b03003e2ea"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aac6c899a4c9d4d958226d208be51f5a2"><a name="aac6c899a4c9d4d958226d208be51f5a2"></a><a name="aac6c899a4c9d4d958226d208be51f5a2"></a>nodeProductId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a6134c6e5eeef4805b21a92ddb0b4f43a"><a name="a6134c6e5eeef4805b21a92ddb0b4f43a"></a><a name="a6134c6e5eeef4805b21a92ddb0b4f43a"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a5bc3f61bd74a49eda19d271c1ea45d1d"><a name="a5bc3f61bd74a49eda19d271c1ea45d1d"></a><a name="a5bc3f61bd74a49eda19d271c1ea45d1d"></a>Instance product ID of a node</p>
</td>
</tr>
<tr id="r44088dff65db49e7adcfe1689612064a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aac3e491b249443f0818bc7fb586d81ee"><a name="aac3e491b249443f0818bc7fb586d81ee"></a><a name="aac3e491b249443f0818bc7fb586d81ee"></a>vmProductId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="af0c4b33732e445548b7bc7be8368e8ae"><a name="af0c4b33732e445548b7bc7be8368e8ae"></a><a name="af0c4b33732e445548b7bc7be8368e8ae"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a2de7baded5a74a2d97517286b00261f5"><a name="a2de7baded5a74a2d97517286b00261f5"></a><a name="a2de7baded5a74a2d97517286b00261f5"></a>VM product ID of a node</p>
</td>
</tr>
<tr id="r001eacc59c634fc0b761167070eb116f"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ad5e229de9769478f9fdef9c0d30d0052"><a name="ad5e229de9769478f9fdef9c0d30d0052"></a><a name="ad5e229de9769478f9fdef9c0d30d0052"></a>vmSpecCode</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ad0294285f7e442999ce6cfbb45361b44"><a name="ad0294285f7e442999ce6cfbb45361b44"></a><a name="ad0294285f7e442999ce6cfbb45361b44"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a003c6b4040ee4c01b2fb5f51c6367d9d"><a name="a003c6b4040ee4c01b2fb5f51c6367d9d"></a><a name="a003c6b4040ee4c01b2fb5f51c6367d9d"></a>VM specifications of a node</p>
</td>
</tr>
<tr id="r62dc652909934b839ed5ab0dbab7d55e"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ab908078805b747188f065a8d46f3210d"><a name="ab908078805b747188f065a8d46f3210d"></a><a name="ab908078805b747188f065a8d46f3210d"></a>rootVolumeSize</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ab21d0fc2d1074e8baf95bbb736e93e67"><a name="ab21d0fc2d1074e8baf95bbb736e93e67"></a><a name="ab21d0fc2d1074e8baf95bbb736e93e67"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581913_p200757511847"><a name="en-us_topic_0110581913_p200757511847"></a><a name="en-us_topic_0110581913_p200757511847"></a>System disk size of a node. This parameter is not configurable and its default value is <strong id="b84235270620266"><a name="b84235270620266"></a><a name="b84235270620266"></a>40 GB</strong>.</p>
</td>
</tr>
<tr id="ra1145762730546c595def5fe555b451a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a445d8504e2df46e38e3e20862d5a4517"><a name="a445d8504e2df46e38e3e20862d5a4517"></a><a name="a445d8504e2df46e38e3e20862d5a4517"></a>rootVolumeProductId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ac05728f1dbff41daa43670cb6c2a7be8"><a name="ac05728f1dbff41daa43670cb6c2a7be8"></a><a name="ac05728f1dbff41daa43670cb6c2a7be8"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a1b1f30e9690f4527b4c1f1cb19d16d38"><a name="a1b1f30e9690f4527b4c1f1cb19d16d38"></a><a name="a1b1f30e9690f4527b4c1f1cb19d16d38"></a>System disk product ID of a node</p>
</td>
</tr>
<tr id="ra94f567604e94dce8d62dbd7c32a9295"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a4164ec2b2020429c9c3933749379ab98"><a name="a4164ec2b2020429c9c3933749379ab98"></a><a name="a4164ec2b2020429c9c3933749379ab98"></a>rootVolumeType</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a4ce29b1d4bc74f038b1c756d56fe9251"><a name="a4ce29b1d4bc74f038b1c756d56fe9251"></a><a name="a4ce29b1d4bc74f038b1c756d56fe9251"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a46f150f4f39142538cd1a3fed0bc1ee7"><a name="a46f150f4f39142538cd1a3fed0bc1ee7"></a><a name="a46f150f4f39142538cd1a3fed0bc1ee7"></a>System disk type of a node</p>
</td>
</tr>
<tr id="rbd0491d62d7849878ad92ffc473c5bbb"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a14cdc064b9ff4bd3b2ff31b606ce189e"><a name="a14cdc064b9ff4bd3b2ff31b606ce189e"></a><a name="a14cdc064b9ff4bd3b2ff31b606ce189e"></a>rootVolumeResourceSpecCode</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a4d00b1aa898b459ea05525398eb34fcf"><a name="a4d00b1aa898b459ea05525398eb34fcf"></a><a name="a4d00b1aa898b459ea05525398eb34fcf"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ad44fb03082fd4d8399f5a1590c2da2aa"><a name="ad44fb03082fd4d8399f5a1590c2da2aa"></a><a name="ad44fb03082fd4d8399f5a1590c2da2aa"></a>System disk product specifications of a node</p>
</td>
</tr>
<tr id="rccf420005b74474987f58a8c0508808d"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ae1c0d77a20e44534b3aae6cfb00c72e4"><a name="ae1c0d77a20e44534b3aae6cfb00c72e4"></a><a name="ae1c0d77a20e44534b3aae6cfb00c72e4"></a>rootVolumeResourceType</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a2ae3d79db3734c23964156fe2daf9add"><a name="a2ae3d79db3734c23964156fe2daf9add"></a><a name="a2ae3d79db3734c23964156fe2daf9add"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a2621e2f95d0c4ad587cf61a7eb27e5cc"><a name="a2621e2f95d0c4ad587cf61a7eb27e5cc"></a><a name="a2621e2f95d0c4ad587cf61a7eb27e5cc"></a>System disk product type of a node</p>
</td>
</tr>
<tr id="rc4b398e9fe8c47ed9eab7783efcf874a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aa3da3db1c5844bfe80e0afb2325570b4"><a name="aa3da3db1c5844bfe80e0afb2325570b4"></a><a name="aa3da3db1c5844bfe80e0afb2325570b4"></a>dataVolumeType</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ade6cdf58add24c5e93acd30a43d77c58"><a name="ade6cdf58add24c5e93acd30a43d77c58"></a><a name="ade6cdf58add24c5e93acd30a43d77c58"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aa790158b0b444a67a47b75fa6ac4d09b"><a name="aa790158b0b444a67a47b75fa6ac4d09b"></a><a name="aa790158b0b444a67a47b75fa6ac4d09b"></a>Data disk storage type of a node. Currently, SATA, SAS, and SSD are supported.</p>
<a name="u9f5e1d8806514426a6e9c525d6c02ae4"></a><a name="u9f5e1d8806514426a6e9c525d6c02ae4"></a><ul id="u9f5e1d8806514426a6e9c525d6c02ae4"><li>SATA: Common I/O</li><li>SAS: High I/O</li><li>SSD: Ultra-high I/O</li></ul>
</td>
</tr>
<tr id="r88ceb6f16ec2420c9b3d352c6c2ce247"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a5e309b28f6e54d6590c66cf9700b157d"><a name="a5e309b28f6e54d6590c66cf9700b157d"></a><a name="a5e309b28f6e54d6590c66cf9700b157d"></a>dataVolumeCount</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a1b6b88569b804f2f92d6afc483561f7d"><a name="a1b6b88569b804f2f92d6afc483561f7d"></a><a name="a1b6b88569b804f2f92d6afc483561f7d"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a2d988c7551df4a81854d7b9a4dbfdef9"><a name="a2d988c7551df4a81854d7b9a4dbfdef9"></a><a name="a2d988c7551df4a81854d7b9a4dbfdef9"></a>Number of data disks of a node</p>
</td>
</tr>
<tr id="racc1050d22de4f54aabbd2c2ced25c2c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aab3c5eac8ee74fd9a48c935f4b0b8d86"><a name="aab3c5eac8ee74fd9a48c935f4b0b8d86"></a><a name="aab3c5eac8ee74fd9a48c935f4b0b8d86"></a>dataVolumeSize</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a5bd2105a280041f189c918e86c6131c4"><a name="a5bd2105a280041f189c918e86c6131c4"></a><a name="a5bd2105a280041f189c918e86c6131c4"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a506ed75cabee4f2faba58f6c4d481fa9"><a name="a506ed75cabee4f2faba58f6c4d481fa9"></a><a name="a506ed75cabee4f2faba58f6c4d481fa9"></a>Data disk storage space of a node</p>
</td>
</tr>
<tr id="r52a96e7d17ce4f3a9eadc7d7cc31880e"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ac4a609c326424822bcd0243aa38a0155"><a name="ac4a609c326424822bcd0243aa38a0155"></a><a name="ac4a609c326424822bcd0243aa38a0155"></a>dataVolumeProductId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ad2f91538b2c44b48979ad38a8620f059"><a name="ad2f91538b2c44b48979ad38a8620f059"></a><a name="ad2f91538b2c44b48979ad38a8620f059"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a3cc4de2d5a564fe7a1be33a103c850fe"><a name="a3cc4de2d5a564fe7a1be33a103c850fe"></a><a name="a3cc4de2d5a564fe7a1be33a103c850fe"></a>Data disk product ID of a node</p>
</td>
</tr>
<tr id="r1cb3bcf5b93f4e588020e361de63a209"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="abef89f6ae16646a3a6ee31b211851f90"><a name="abef89f6ae16646a3a6ee31b211851f90"></a><a name="abef89f6ae16646a3a6ee31b211851f90"></a>dataVolumeResourceSpecCode</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a78420bba01144cf48c60043c1b2f2370"><a name="a78420bba01144cf48c60043c1b2f2370"></a><a name="a78420bba01144cf48c60043c1b2f2370"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a7dadecb9771948ecbeecdbe5a3eee6bb"><a name="a7dadecb9771948ecbeecdbe5a3eee6bb"></a><a name="a7dadecb9771948ecbeecdbe5a3eee6bb"></a>Data disk product specifications of a node</p>
</td>
</tr>
<tr id="r0a2a9426d6274990a3f406be65b77b34"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a1baaf1591f2448ab8ec85a9278681587"><a name="a1baaf1591f2448ab8ec85a9278681587"></a><a name="a1baaf1591f2448ab8ec85a9278681587"></a>dataVolumeResourceType</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a54bab5459e034e66bd296b444e31e957"><a name="a54bab5459e034e66bd296b444e31e957"></a><a name="a54bab5459e034e66bd296b444e31e957"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a13c8af6c0a6247869bcf6ca3c57348b3"><a name="a13c8af6c0a6247869bcf6ca3c57348b3"></a><a name="a13c8af6c0a6247869bcf6ca3c57348b3"></a>Data disk product type of a node</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section06612321592"></a>

-   Example request

    None

-   Example response

    ```
    {
        "clusterTotal": 1,
        "clusters": [
            {
                "clusterId": "bc134369-294c-42b7-a707-b2036ba38524",
                "clusterName": "mrs_D0zW",
                "masterNodeNum": "2",
                "coreNodeNum": "3",
                "clusterState": "terminated",
                "createAt": "1498272043",
                "updateAt": "1498636753",
                "chargingStartTime": "1498273733",
                "logCollection": 1,
                "billingType": "Metered",
                "dataCenter": "eu-de",
                "vpc": null,
                "duration": "0",
                "fee": null,
                "hadoopVersion": null,
                "masterNodeSize": null,
                "coreNodeSize": null,
                "componentList": [
                    {
                      "componentId": "MRS 2.1.0_001",
                      "componentName": "Hadoop",
                      "componentVersion": "3.1.1",
                      "componentDesc": "A framework that allows for the distributed processing of large data sets across clusters."
                    },
                    {
                      "componentId": "MRS 2.1.0_003",
                      "componentName": "HBase",
                      "componentVersion": "2.1.1",
                      "componentDesc": "A scalable, distributed database that supports structured data storage for large tables."
                    },
                    {
                      "componentId": "MRS 2.1.0_002",
                      "componentName": "Spark",
                      "componentVersion": "2.3.2",
                      "componentDesc": "A fast and general engine for large-scale data processing."
                    },
                    {
                      "componentId": "MRS 2.1.0_004",
                      "componentName": "Hive",
                      "componentVersion": "3.1.0",
                      "componentDesc": "A data warehouse infrastructure that provides data summarization and ad hoc querying."
                    },
                    {
                      "componentId": "MRS 2.1.0_005",
                      "componentName": "Hue",
                      "componentVersion": "3.11.0",
                      "componentDesc": "A component that provides the Hadoop UI capability, which enables users to analyze and process Hadoop cluster data on browsers."
                    },
                    {
                      "componentId": "MRS 2.1.0_008",
                      "componentName": "Loader",
                      "componentVersion": "2.0.0",
                      "componentDesc": "A tool developed based on open source Sqoop 1.99.7, designed for efficiently transferring bulk data between Apache Hadoop and structured datastores such as relational databases."
                    },
                    {
                      "componentId": "MRS 2.1.0_010",
                      "componentName": "Tez",
                      "componentVersion": "0.9.1",
                      "componentDesc": "An application framework which allows for a complex directed-acyclic-graph of tasks for processing data."
                    },
                    {
                      "componentId": "MRS 2.1.0_011",
                      "componentName": "Presto",
                      "componentVersion": "308",
                      "componentDesc": "An open source distributed SQL query engine."
                    },
                    {
                      "componentId": "MRS 2.1.0_014",
                      "componentName": "Flink",
                      "componentVersion": "1.7.0",
                      "componentDesc": "A framework and distributed processing engine for stateful computations over unbounded and bounded data streams."
                    }
                ],
                "externalIp": null,
                "externalAlternateIp": null,
                "internalIp": null,
                "deploymentId": null,
                "remark": "",
                "orderId": null,
                "azId": null,
                "masterNodeProductId": null,
                "masterNodeSpecId": null,
                "coreNodeProductId": null,
                "coreNodeSpecId": null,
                "azName": "eu-de-01",
                "instanceId": null,
                "vnc": "v2/5a3314075bfa49b9ae360f4ecd333695/servers/e2cda891-232e-4703-995e-3b1406add01d/action",
                "tenantId": null,
                "volumeSize": 0,
                "volumeType": null,
                "subnetId": null,
                "subnetName": null,
                "securityGroupsId": null,
                "slaveSecurityGroupsId": null,
                "mrsManagerFinish": false,
                "stageDesc": "Installing MRS Manager",
                "safeMode": 0,
                "clusterVersion": null,
                "nodePublicCertName": null,
                "masterNodeIp": "unknown",
                "privateIpFirst": null,
                "errorInfo": "",
                "clusterType": 0,
                "nodeGroups": [
                   {
                     "groupName": "master_node_default_group",
                     "nodeNum": 1,
                     "nodeSize": "s1.xlarge.linux.mrs",
                     "nodeSpecId": "cdc6035a249a40249312f5ef72a23cd7",
                     "vmProductId": "",
                     "vmSpecCode": null,
                     "nodeProductId": "dc970349d128460e960a0c2b826c427c",
                     "rootVolumeSize": 40,
                     "rootVolumeProductId": "16c1dcf0897249758b1ec276d06e0572",
                     "rootVolumeType": "SATA",
                     "rootVolumeResourceSpecCode": "",
                     "rootVolumeResourceType": "",
                     "dataVolumeType": "SATA",
                     "dataVolumeCount": 1,
                     "dataVolumeSize": 100,
                     "dataVolumeProductId": "16c1dcf0897249758b1ec276d06e0572",
                     "dataVolumeResourceSpecCode": "",
                     "dataVolumeResourceType": "",
                   },
                   {
                     "groupName": "core_node_analysis_group",
                     "nodeNum": 1,
                     "nodeSize": "s1.xlarge.linux.mrs",
                     "nodeSpecId": "cdc6035a249a40249312f5ef72a23cd7",
                     "vmProductId": "",
                     "vmSpecCode": null,
                     "nodeProductId": "dc970349d128460e960a0c2b826c427c",
                     "rootVolumeSize": 40,
                     "rootVolumeProductId": "16c1dcf0897249758b1ec276d06e0572",
                     "rootVolumeType": "SATA",
                     "rootVolumeResourceSpecCode": "",
                     "rootVolumeResourceType": "",
                     "dataVolumeType": "SATA",
                     "dataVolumeCount": 1,
                     "dataVolumeSize": 100,
                     "dataVolumeProductId": "16c1dcf0897249758b1ec276d06e0572",
                     "dataVolumeResourceSpecCode": "",
                     "dataVolumeResourceType": "",
                   },
                   {
                     "groupName": "task_node_analysis_group",
                     "nodeNum": 1,
                     "nodeSize": "s1.xlarge.linux.mrs",
                     "nodeSpecId": "cdc6035a249a40249312f5ef72a23cd7",
                     "vmProductId": "",
                     "vmSpecCode": null,
                     "nodeProductId": "dc970349d128460e960a0c2b826c427c", 
                     "rootVolumeSize": 40, 
                     "rootVolumeProductId": "16c1dcf0897249758b1ec276d06e0572", 
                     "rootVolumeType": "SATA", 
                     "rootVolumeResourceSpecCode": "", 
                     "rootVolumeResourceType": "", 
                     "dataVolumeType": "SATA", 
                     "dataVolumeCount": 1, 
                     "dataVolumeSize": 100, 
                     "dataVolumeProductId": "16c1dcf0897249758b1ec276d06e0572", 
                     "dataVolumeResourceSpecCode": "", 
                     "dataVolumeResourceType": "", 
                   } 
    
                ],
                "taskNodeGroups": [
                   {
                     "groupName": "task_node_default_group",
                     "nodeNum": 1,
                     "nodeSize": "s1.xlarge.linux.mrs",
                     "nodeSpecId": "cdc6035a249a40249312f5ef72a23cd7",
                     "vmProductId": "",
                     "vmSpecCode": null,
                     "nodeProductId": "dc970349d128460e960a0c2b826c427c",
                     "rootVolumeSize": 40,
                     "rootVolumeProductId": "16c1dcf0897249758b1ec276d06e0572",
                     "rootVolumeType": "SATA",
                     "rootVolumeResourceSpecCode": "",
                     "rootVolumeResourceType": "",
                     "dataVolumeType": "SATA",
                     "dataVolumeCount": 1,
                     "dataVolumeSize": 100,
                     "dataVolumeProductId": "16c1dcf0897249758b1ec276d06e0572",
                     "dataVolumeResourceSpecCode": "",
                     "dataVolumeResourceType": "",
                   }
                ],
             "masterDataVolumeType": "SATA",
             "masterDataVolumeSize": 200,
             "masterDataVolumeCount": 1,
             "coreDataVolumeType": "SATA",
             "coreDataVolumeSize": 100,
             "coreDataVolumeCount": 1,
            }
        ]
    }
    ```


## Status Code<a name="sbf624641707045ed8595540f4d7e0061"></a>

[Table 6](#t58f8687ecee1484aad44fb227671ad60)  describes the status code of this API.

**Table  6**  Status code

<a name="t58f8687ecee1484aad44fb227671ad60"></a>
<table><thead align="left"><tr id="r84c29e6e6fda4774838951f2853ac2f1"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="aad4c7612f25c4d37b54c3535e460e3ef"><a name="aad4c7612f25c4d37b54c3535e460e3ef"></a><a name="aad4c7612f25c4d37b54c3535e460e3ef"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="a60bba23a5882406cb63be05bcbd66966"><a name="a60bba23a5882406cb63be05bcbd66966"></a><a name="a60bba23a5882406cb63be05bcbd66966"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r4f34c85918d94b139eaf2df3e73e0c79"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="aa81e2fafd5664cd8b8eb1281bfa54450"><a name="aa81e2fafd5664cd8b8eb1281bfa54450"></a><a name="aa81e2fafd5664cd8b8eb1281bfa54450"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="a7ca1ab95bc384ca29b7fb947bbd44204"><a name="a7ca1ab95bc384ca29b7fb947bbd44204"></a><a name="a7ca1ab95bc384ca29b7fb947bbd44204"></a>The cluster list information has been successfully queried.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

