# Querying Cluster Details<a name="EN-US_TOPIC_0172486194"></a>

## Function<a name="s90d885d2c6494412a68e00200c056e9d"></a>

This API is used to query details about a specified cluster. This API is incompatible with Sahara.

## URI<a name="sae9ae362f1d24e14924dddda463a37e0"></a>

-   Format

    GET /v1.1/\{project\_id\}/cluster\_infos/\{cluster\_id\}

-   Parameter description

    **Table  1**  URI parameter description

    <a name="t53c0ce7eb2c24c3295f983454e0d8569"></a>
    <table><thead align="left"><tr id="rb517ff72222649df8710bb759867055b"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="ac5398c49057349e9a46eb0e19bd805e8"><a name="ac5398c49057349e9a46eb0e19bd805e8"></a><a name="ac5398c49057349e9a46eb0e19bd805e8"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0110581853_p141410194812"><a name="en-us_topic_0110581853_p141410194812"></a><a name="en-us_topic_0110581853_p141410194812"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="a54f026c2dd1f4793878c53b639957163"><a name="a54f026c2dd1f4793878c53b639957163"></a><a name="a54f026c2dd1f4793878c53b639957163"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r9a17a79dd7054082b04ce89eb7bc9bc9"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a7faa08390d744aecbea092efcbc9781c"><a name="a7faa08390d744aecbea092efcbc9781c"></a><a name="a7faa08390d744aecbea092efcbc9781c"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a1621d72258c047a991375efc40a27fa7"><a name="a1621d72258c047a991375efc40a27fa7"></a><a name="a1621d72258c047a991375efc40a27fa7"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aecc355743de44972ac55cb6d9f531387"><a name="aecc355743de44972ac55cb6d9f531387"></a><a name="aecc355743de44972ac55cb6d9f531387"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="re0f9daa536804569904dd76ff23a10d6"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a8a0d6239574c4ee78d4c00ad2866397b"><a name="a8a0d6239574c4ee78d4c00ad2866397b"></a><a name="a8a0d6239574c4ee78d4c00ad2866397b"></a>cluster_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ad2db122963ef45a297b52cfc6a02bf81"><a name="ad2db122963ef45a297b52cfc6a02bf81"></a><a name="ad2db122963ef45a297b52cfc6a02bf81"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a7f704b234e064ecdaffbc3145b1f4fd4"><a name="a7f704b234e064ecdaffbc3145b1f4fd4"></a><a name="a7f704b234e064ecdaffbc3145b1f4fd4"></a>Cluster ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s8db3fe63ec90463a80cc5feb8c451c70"></a>

**Request parameters**

None.

## Response<a name="s31ca7c3d28464888b7f77d3a2da053d3"></a>

**Table  2**  Response parameter description

<a name="t06d88cb9fce84af1bb7a6b24600cd60d"></a>
<table><thead align="left"><tr id="r220682c0596b4b27987943ac011bcad0"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="ab7280794d83941d5873657b56296246b"><a name="ab7280794d83941d5873657b56296246b"></a><a name="ab7280794d83941d5873657b56296246b"></a><strong id="b420194915427"><a name="b420194915427"></a><a name="b420194915427"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0110581853_p335463411742"><a name="en-us_topic_0110581853_p335463411742"></a><a name="en-us_topic_0110581853_p335463411742"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="en-us_topic_0110581853_p328991811742"><a name="en-us_topic_0110581853_p328991811742"></a><a name="en-us_topic_0110581853_p328991811742"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rc34e62d38cfd4f8696e5fb615cd3b489"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a10688aa1cfc04dadb7e3e8f9853f4d73"><a name="a10688aa1cfc04dadb7e3e8f9853f4d73"></a><a name="a10688aa1cfc04dadb7e3e8f9853f4d73"></a>clusterId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a994aa2776362487a907e658e92a33fe1"><a name="a994aa2776362487a907e658e92a33fe1"></a><a name="a994aa2776362487a907e658e92a33fe1"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a3e206f5cfc65472aaf87ad696521fe24"><a name="a3e206f5cfc65472aaf87ad696521fe24"></a><a name="a3e206f5cfc65472aaf87ad696521fe24"></a>Cluster ID</p>
</td>
</tr>
<tr id="r2f6706375f2a4447bb47dab13101adad"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a76f14b78f12f4ba29bfc15856a02a92b"><a name="a76f14b78f12f4ba29bfc15856a02a92b"></a><a name="a76f14b78f12f4ba29bfc15856a02a92b"></a>clusterName</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ad2b55a223c034651b8305882f6b282cf"><a name="ad2b55a223c034651b8305882f6b282cf"></a><a name="ad2b55a223c034651b8305882f6b282cf"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a70dadc69e617478c85fd9d19995a5ab2"><a name="a70dadc69e617478c85fd9d19995a5ab2"></a><a name="a70dadc69e617478c85fd9d19995a5ab2"></a>Cluster name</p>
</td>
</tr>
<tr id="rbad05444fc3e4d79af8b212864801a08"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a8f39287aed4841c2a1efcc1da669d3d2"><a name="a8f39287aed4841c2a1efcc1da669d3d2"></a><a name="a8f39287aed4841c2a1efcc1da669d3d2"></a>masterNodeNum</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a078665add1a24d4abdf674b963233e49"><a name="a078665add1a24d4abdf674b963233e49"></a><a name="a078665add1a24d4abdf674b963233e49"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ac03ba58e57c842baaceae31dc68f478a"><a name="ac03ba58e57c842baaceae31dc68f478a"></a><a name="ac03ba58e57c842baaceae31dc68f478a"></a>Number of Master nodes deployed in a cluster</p>
</td>
</tr>
<tr id="r9bdb4a8b3c974732ade219dc74796025"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a69e8a4e9721f4c158f4c4387e491ef38"><a name="a69e8a4e9721f4c158f4c4387e491ef38"></a><a name="a69e8a4e9721f4c158f4c4387e491ef38"></a>coreNodeNum</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a6b9c52d136a946d68b6a1ff7d036f698"><a name="a6b9c52d136a946d68b6a1ff7d036f698"></a><a name="a6b9c52d136a946d68b6a1ff7d036f698"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a62ba541462c54c30b6c99a4bacc28345"><a name="a62ba541462c54c30b6c99a4bacc28345"></a><a name="a62ba541462c54c30b6c99a4bacc28345"></a>Number of Core nodes deployed in a cluster</p>
</td>
</tr>
<tr id="row794912352334"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p12949735123317"><a name="p12949735123317"></a><a name="p12949735123317"></a>totalNodeNum</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p7949635133317"><a name="p7949635133317"></a><a name="p7949635133317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p0951143583314"><a name="p0951143583314"></a><a name="p0951143583314"></a>Total number of nodes deployed in a cluster</p>
</td>
</tr>
<tr id="r50c49d9666914c4caa1b5e9243112de3"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a5cbbc8f8834b480493821018e3741915"><a name="a5cbbc8f8834b480493821018e3741915"></a><a name="a5cbbc8f8834b480493821018e3741915"></a>clusterState</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a4927886d6676430a8779b7c274df2428"><a name="a4927886d6676430a8779b7c274df2428"></a><a name="a4927886d6676430a8779b7c274df2428"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><div class="p" id="a2eaba0f58bd9429aadfa792a1916d377"><a name="a2eaba0f58bd9429aadfa792a1916d377"></a><a name="a2eaba0f58bd9429aadfa792a1916d377"></a>Cluster status. Valid values include:<a name="u1ed2f3245f86457aa9c63b6da1cc146a"></a><a name="u1ed2f3245f86457aa9c63b6da1cc146a"></a><ul id="u1ed2f3245f86457aa9c63b6da1cc146a"><li><strong id="b12881132018155"><a name="b12881132018155"></a><a name="b12881132018155"></a>starting</strong>: The cluster is being started.</li><li><strong id="b12419152341516"><a name="b12419152341516"></a><a name="b12419152341516"></a>running</strong>: The cluster is running.</li><li><strong id="b1317972751514"><a name="b1317972751514"></a><a name="b1317972751514"></a>terminated</strong>: The cluster has been terminated.</li><li><strong id="b1029515301157"><a name="b1029515301157"></a><a name="b1029515301157"></a>failed</strong>: The cluster fails.</li><li><strong id="b1235534121514"><a name="b1235534121514"></a><a name="b1235534121514"></a>abnormal</strong>: The cluster is abnormal.</li><li><strong id="b10329143719158"><a name="b10329143719158"></a><a name="b10329143719158"></a>terminating</strong>: The cluster is being terminated.</li><li><strong id="b1168619464153"><a name="b1168619464153"></a><a name="b1168619464153"></a>frozen</strong>: The cluster has been frozen.</li><li><strong id="b24465071516"><a name="b24465071516"></a><a name="b24465071516"></a>scaling-out</strong>: The cluster is being scaled out.</li><li><strong id="b9899175321520"><a name="b9899175321520"></a><a name="b9899175321520"></a>scaling-in</strong>: The cluster is being scaled in.</li></ul>
</div>
</td>
</tr>
<tr id="rbe381b9e76714c369f347dd34cbdbeff"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110581853_p194253911742"><a name="en-us_topic_0110581853_p194253911742"></a><a name="en-us_topic_0110581853_p194253911742"></a>createAt</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ae25215c7c5f94d78a899d3803d023767"><a name="ae25215c7c5f94d78a899d3803d023767"></a><a name="ae25215c7c5f94d78a899d3803d023767"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581853_p943072211742"><a name="en-us_topic_0110581853_p943072211742"></a><a name="en-us_topic_0110581853_p943072211742"></a>Cluster creation time, which is a 10-bit timestamp</p>
</td>
</tr>
<tr id="rb59d4223e23a492792ee9ea8fbed03c4"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a0bdb9c8ecf7849ff85900a4da14f4746"><a name="a0bdb9c8ecf7849ff85900a4da14f4746"></a><a name="a0bdb9c8ecf7849ff85900a4da14f4746"></a>updateAt</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a1a974e614b0246ce8390224ee388eff4"><a name="a1a974e614b0246ce8390224ee388eff4"></a><a name="a1a974e614b0246ce8390224ee388eff4"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a50d3a7e81dc44a85a9a4833aeccdabe7"><a name="a50d3a7e81dc44a85a9a4833aeccdabe7"></a><a name="a50d3a7e81dc44a85a9a4833aeccdabe7"></a>Cluster update time, which is a 10-bit timestamp</p>
</td>
</tr>
<tr id="rd4365d22198a474aa1fb3b3d98d4c148"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a569d0715799b4da09b73d456d3f28ac5"><a name="a569d0715799b4da09b73d456d3f28ac5"></a><a name="a569d0715799b4da09b73d456d3f28ac5"></a>billingType</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="afabff1ae31c74b66b8618a0836fab006"><a name="afabff1ae31c74b66b8618a0836fab006"></a><a name="afabff1ae31c74b66b8618a0836fab006"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581853_p700268211742"><a name="en-us_topic_0110581853_p700268211742"></a><a name="en-us_topic_0110581853_p700268211742"></a>Cluster billing mode</p>
</td>
</tr>
<tr id="r9e2a2070cfc34e48bc63451adc72ce90"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110581853_p468189111742"><a name="en-us_topic_0110581853_p468189111742"></a><a name="en-us_topic_0110581853_p468189111742"></a>dataCenter</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="aed469aee879041f3a87af33f6ace3ef6"><a name="aed469aee879041f3a87af33f6ace3ef6"></a><a name="aed469aee879041f3a87af33f6ace3ef6"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a31955df039e248488c755efc6dd13804"><a name="a31955df039e248488c755efc6dd13804"></a><a name="a31955df039e248488c755efc6dd13804"></a>Cluster work region</p>
</td>
</tr>
<tr id="r4c404f4483074ead8f224c25e111a7f4"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aba4b15fad5a84c3ab8dc0c25ea95fa3f"><a name="aba4b15fad5a84c3ab8dc0c25ea95fa3f"></a><a name="aba4b15fad5a84c3ab8dc0c25ea95fa3f"></a>vpc</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a06d6511757a942ac8606824c72ded378"><a name="a06d6511757a942ac8606824c72ded378"></a><a name="a06d6511757a942ac8606824c72ded378"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581853_p183315311742"><a name="en-us_topic_0110581853_p183315311742"></a><a name="en-us_topic_0110581853_p183315311742"></a>VPC name</p>
</td>
</tr>
<tr id="r1b6dba20cb9a49ccb4e8000eda2a80d3"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="acfea4c3bcbec4febaac1eff43f8d988e"><a name="acfea4c3bcbec4febaac1eff43f8d988e"></a><a name="acfea4c3bcbec4febaac1eff43f8d988e"></a>fee</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ad8d7a80b7d4646f1a26ec31e370f9ca2"><a name="ad8d7a80b7d4646f1a26ec31e370f9ca2"></a><a name="ad8d7a80b7d4646f1a26ec31e370f9ca2"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a31641f551eda4b3eb330aedb94e8a44d"><a name="a31641f551eda4b3eb330aedb94e8a44d"></a><a name="a31641f551eda4b3eb330aedb94e8a44d"></a>Cluster creation fee, which is automatically calculated</p>
</td>
</tr>
<tr id="r952dc10813274c0da7294880b7d15409"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a4dde3961044b4bd6b74abfe792575b69"><a name="a4dde3961044b4bd6b74abfe792575b69"></a><a name="a4dde3961044b4bd6b74abfe792575b69"></a>hadoopVersion</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ae994d645bf2a42c88ad4c1659ebab242"><a name="ae994d645bf2a42c88ad4c1659ebab242"></a><a name="ae994d645bf2a42c88ad4c1659ebab242"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ac38a4a01b4cb4a6189e5d37adc06c2a7"><a name="ac38a4a01b4cb4a6189e5d37adc06c2a7"></a><a name="ac38a4a01b4cb4a6189e5d37adc06c2a7"></a>Hadoop version</p>
</td>
</tr>
<tr id="r0499999ee19c41ffb518baa7cf445516"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110581853_p950109411742"><a name="en-us_topic_0110581853_p950109411742"></a><a name="en-us_topic_0110581853_p950109411742"></a>masterNodeSize</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a68f1249250734d67b9312f7c6c4b02f5"><a name="a68f1249250734d67b9312f7c6c4b02f5"></a><a name="a68f1249250734d67b9312f7c6c4b02f5"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581853_p11129511742"><a name="en-us_topic_0110581853_p11129511742"></a><a name="en-us_topic_0110581853_p11129511742"></a>Instance specifications of a Master node </p>
</td>
</tr>
<tr id="r72ac4942735d453a9ef618d0e285d2c7"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a712372353ced490f8ac73a7c3e742e51"><a name="a712372353ced490f8ac73a7c3e742e51"></a><a name="a712372353ced490f8ac73a7c3e742e51"></a>coreNodeSize</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a2d83ef236f794b5ba00f6e23b9dd1878"><a name="a2d83ef236f794b5ba00f6e23b9dd1878"></a><a name="a2d83ef236f794b5ba00f6e23b9dd1878"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a125ebf44fed5475fad4ef3bd57dd7ca1"><a name="a125ebf44fed5475fad4ef3bd57dd7ca1"></a><a name="a125ebf44fed5475fad4ef3bd57dd7ca1"></a>Instance specifications of a Core node </p>
</td>
</tr>
<tr id="r05078a2c310f4e7890b576046cb6ed4b"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a808715b073c24e0392fd9a73cf9b423f"><a name="a808715b073c24e0392fd9a73cf9b423f"></a><a name="a808715b073c24e0392fd9a73cf9b423f"></a>componentList</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a59483ee1753f4157bda78a201824f145"><a name="a59483ee1753f4157bda78a201824f145"></a><a name="a59483ee1753f4157bda78a201824f145"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a0d15541bd57d44fe8414980b1e778224"><a name="a0d15541bd57d44fe8414980b1e778224"></a><a name="a0d15541bd57d44fe8414980b1e778224"></a>Component list. For details, see <a href="#t0bc8fb7b4f444931b3c1b0ed022c2f79">Table 3</a>.</p>
</td>
</tr>
<tr id="r96c72486496b465486df085990187b68"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a4bf26128d1e44439b2754b14b9feef2e"><a name="a4bf26128d1e44439b2754b14b9feef2e"></a><a name="a4bf26128d1e44439b2754b14b9feef2e"></a>externalIp</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a7664da3520d1424fa89428bb92dc77e8"><a name="a7664da3520d1424fa89428bb92dc77e8"></a><a name="a7664da3520d1424fa89428bb92dc77e8"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581853_p434661411742"><a name="en-us_topic_0110581853_p434661411742"></a><a name="en-us_topic_0110581853_p434661411742"></a>External IP address</p>
</td>
</tr>
<tr id="r724638bc55824c07a23ac0f3df45603f"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a7564fdb21cf24086b455d177162c6fd8"><a name="a7564fdb21cf24086b455d177162c6fd8"></a><a name="a7564fdb21cf24086b455d177162c6fd8"></a>externalAlternateIp</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ac546888eb0cb4b7b84f526ddec86e0ba"><a name="ac546888eb0cb4b7b84f526ddec86e0ba"></a><a name="ac546888eb0cb4b7b84f526ddec86e0ba"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a9f5ec2c8beaa4a9fb338ad9b80c548cb"><a name="a9f5ec2c8beaa4a9fb338ad9b80c548cb"></a><a name="a9f5ec2c8beaa4a9fb338ad9b80c548cb"></a>Backup external IP address</p>
</td>
</tr>
<tr id="r983c7292e20143a69151897eb7ea8dcf"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a12ed59f355854cf6a87711b9cd554cd3"><a name="a12ed59f355854cf6a87711b9cd554cd3"></a><a name="a12ed59f355854cf6a87711b9cd554cd3"></a>internalIp</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a01ac4f6f0bd84d6a9726298cf9da1e73"><a name="a01ac4f6f0bd84d6a9726298cf9da1e73"></a><a name="a01ac4f6f0bd84d6a9726298cf9da1e73"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aa998e2baa1834e3f86189078ab7b6134"><a name="aa998e2baa1834e3f86189078ab7b6134"></a><a name="aa998e2baa1834e3f86189078ab7b6134"></a>Internal IP address</p>
</td>
</tr>
<tr id="rd8b0fd5835124b959dbcdb9da6af6fcf"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="af6e4c55bcd6244e1a7c416a8eff2a457"><a name="af6e4c55bcd6244e1a7c416a8eff2a457"></a><a name="af6e4c55bcd6244e1a7c416a8eff2a457"></a>deploymentId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0110581853_p450335811742"><a name="en-us_topic_0110581853_p450335811742"></a><a name="en-us_topic_0110581853_p450335811742"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a715970957e9d440299b155c4a721d615"><a name="a715970957e9d440299b155c4a721d615"></a><a name="a715970957e9d440299b155c4a721d615"></a>Cluster deployment ID</p>
</td>
</tr>
<tr id="r1a1d4789bb30486485d431a0a2f7a181"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a6de594917417462e9e2154c2c2ec4301"><a name="a6de594917417462e9e2154c2c2ec4301"></a><a name="a6de594917417462e9e2154c2c2ec4301"></a>remark</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="af00330ed16d74212abcb3ad30da2f150"><a name="af00330ed16d74212abcb3ad30da2f150"></a><a name="af00330ed16d74212abcb3ad30da2f150"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a3c34d749dfa54cec944cc6032532dd9d"><a name="a3c34d749dfa54cec944cc6032532dd9d"></a><a name="a3c34d749dfa54cec944cc6032532dd9d"></a>Cluster remarks</p>
</td>
</tr>
<tr id="r4148cc94f55c42499072ff2c70f0ae05"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="acc61073f9e29433f94e3f7d61a4bdaa0"><a name="acc61073f9e29433f94e3f7d61a4bdaa0"></a><a name="acc61073f9e29433f94e3f7d61a4bdaa0"></a>orderId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a0db4206b4b3545329d34b0d06f3dbafb"><a name="a0db4206b4b3545329d34b0d06f3dbafb"></a><a name="a0db4206b4b3545329d34b0d06f3dbafb"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581853_p841024011742"><a name="en-us_topic_0110581853_p841024011742"></a><a name="en-us_topic_0110581853_p841024011742"></a>Cluster creation order ID</p>
</td>
</tr>
<tr id="r2afac8c1ebed45e8becf4143dbeb5a4f"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aa6520c6bf37a4064a0544095eb3fe019"><a name="aa6520c6bf37a4064a0544095eb3fe019"></a><a name="aa6520c6bf37a4064a0544095eb3fe019"></a>azId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="abe3a88fc438b442aacd2753fe22ea146"><a name="abe3a88fc438b442aacd2753fe22ea146"></a><a name="abe3a88fc438b442aacd2753fe22ea146"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="abde40229be674bf7bdc56e3498c4c42a"><a name="abde40229be674bf7bdc56e3498c4c42a"></a><a name="abde40229be674bf7bdc56e3498c4c42a"></a>AZ ID</p>
</td>
</tr>
<tr id="rb8f9a585daff41afb9de9bd68e2c04b0"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a73e62ee1a7b248d2801382a8597d6849"><a name="a73e62ee1a7b248d2801382a8597d6849"></a><a name="a73e62ee1a7b248d2801382a8597d6849"></a>masterNodeProductId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a8821636803c0497a8549fa323794e3b6"><a name="a8821636803c0497a8549fa323794e3b6"></a><a name="a8821636803c0497a8549fa323794e3b6"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a6d5c06a0cb654aeb89bf0ae1ce4a8348"><a name="a6d5c06a0cb654aeb89bf0ae1ce4a8348"></a><a name="a6d5c06a0cb654aeb89bf0ae1ce4a8348"></a>Product ID of a Master node</p>
</td>
</tr>
<tr id="rec4b4d403241412e8c019af91031fa32"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110581853_p620458511742"><a name="en-us_topic_0110581853_p620458511742"></a><a name="en-us_topic_0110581853_p620458511742"></a>masterNodeSpecId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a752181e9de954373923e7de2b4886011"><a name="a752181e9de954373923e7de2b4886011"></a><a name="a752181e9de954373923e7de2b4886011"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aefd4b4ca595a456a82f9836657857efc"><a name="aefd4b4ca595a456a82f9836657857efc"></a><a name="aefd4b4ca595a456a82f9836657857efc"></a>Specification ID of a Master node</p>
</td>
</tr>
<tr id="r1f82f5ae3a8b4dcc887f108dc989e370"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a4ecc3f39fd354b6bbfd2c2ac7765dee4"><a name="a4ecc3f39fd354b6bbfd2c2ac7765dee4"></a><a name="a4ecc3f39fd354b6bbfd2c2ac7765dee4"></a>coreNodeProductId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a8db4017ba32f42e2b0ee052ab27419ef"><a name="a8db4017ba32f42e2b0ee052ab27419ef"></a><a name="a8db4017ba32f42e2b0ee052ab27419ef"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a08b8fe45ec8e449a88afd827b407a5fb"><a name="a08b8fe45ec8e449a88afd827b407a5fb"></a><a name="a08b8fe45ec8e449a88afd827b407a5fb"></a>Product ID of a Core node</p>
</td>
</tr>
<tr id="r7fa1b491dfce45238afe316c826fcc5a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a86e713f9f1af48b996788e1d4c915271"><a name="a86e713f9f1af48b996788e1d4c915271"></a><a name="a86e713f9f1af48b996788e1d4c915271"></a>coreNodeSpecId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a27f48a51dca74a3c907a61e3da0de595"><a name="a27f48a51dca74a3c907a61e3da0de595"></a><a name="a27f48a51dca74a3c907a61e3da0de595"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a5fa634aaba544c02bb4ef13537593db3"><a name="a5fa634aaba544c02bb4ef13537593db3"></a><a name="a5fa634aaba544c02bb4ef13537593db3"></a>Specification ID of a Core node</p>
</td>
</tr>
<tr id="r52cad3e3d7eb4b8c95ac1e6a34f626b1"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110581853_p197913411742"><a name="en-us_topic_0110581853_p197913411742"></a><a name="en-us_topic_0110581853_p197913411742"></a>azName</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a0f70c0cb28f84bb18c91c7f8290c4551"><a name="a0f70c0cb28f84bb18c91c7f8290c4551"></a><a name="a0f70c0cb28f84bb18c91c7f8290c4551"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a34c51fb753d64a5d8245e99637706f43"><a name="a34c51fb753d64a5d8245e99637706f43"></a><a name="a34c51fb753d64a5d8245e99637706f43"></a>AZ name</p>
</td>
</tr>
<tr id="r2a461bc22fa14a74914001854dc7cb8a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110581853_p221812011742"><a name="en-us_topic_0110581853_p221812011742"></a><a name="en-us_topic_0110581853_p221812011742"></a>instanceId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a5f5f45f5cae74887be5edc976a10da9f"><a name="a5f5f45f5cae74887be5edc976a10da9f"></a><a name="a5f5f45f5cae74887be5edc976a10da9f"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a941b52f2fb4d4e93bc290b06260c758f"><a name="a941b52f2fb4d4e93bc290b06260c758f"></a><a name="a941b52f2fb4d4e93bc290b06260c758f"></a>Instance ID</p>
</td>
</tr>
<tr id="r0b38d37b1785490a8c8809d98a15ecc3"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="acf6511845a0f48a2935081415adfb72a"><a name="acf6511845a0f48a2935081415adfb72a"></a><a name="acf6511845a0f48a2935081415adfb72a"></a>vnc</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a06c0c261fe0e4b99bb66c0f2db4d740c"><a name="a06c0c261fe0e4b99bb66c0f2db4d740c"></a><a name="a06c0c261fe0e4b99bb66c0f2db4d740c"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581853_p887680911742"><a name="en-us_topic_0110581853_p887680911742"></a><a name="en-us_topic_0110581853_p887680911742"></a>URI for remotely logging in to an ECS</p>
</td>
</tr>
<tr id="rcf5f88cf52574ff49c92039bc3f6fc52"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a9ea4142a6652403e884aea248620c43b"><a name="a9ea4142a6652403e884aea248620c43b"></a><a name="a9ea4142a6652403e884aea248620c43b"></a>tenantId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0110581853_p632170911742"><a name="en-us_topic_0110581853_p632170911742"></a><a name="en-us_topic_0110581853_p632170911742"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a770697e4b07b449783e725f7f1e215df"><a name="a770697e4b07b449783e725f7f1e215df"></a><a name="a770697e4b07b449783e725f7f1e215df"></a>Project ID</p>
</td>
</tr>
<tr id="rc8245a38fae94be6a71e2e799c0a53de"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a60b968a5325942ba9851f8a23659109d"><a name="a60b968a5325942ba9851f8a23659109d"></a><a name="a60b968a5325942ba9851f8a23659109d"></a>volumeSize</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ad9c420cbdf024be8bb83a6e21ac0f282"><a name="ad9c420cbdf024be8bb83a6e21ac0f282"></a><a name="ad9c420cbdf024be8bb83a6e21ac0f282"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a3e578559a4d94847a589e89449fdda9e"><a name="a3e578559a4d94847a589e89449fdda9e"></a><a name="a3e578559a4d94847a589e89449fdda9e"></a>Disk storage space</p>
</td>
</tr>
<tr id="row19792184225320"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p127921542135317"><a name="p127921542135317"></a><a name="p127921542135317"></a>subnetId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1679413427538"><a name="p1679413427538"></a><a name="p1679413427538"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p179474217532"><a name="p179474217532"></a><a name="p179474217532"></a>Subnet ID</p>
</td>
</tr>
<tr id="r7630bd9ee29d431ca30647c3f1cf0440"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a964c6bc005994dc3aa3d79f71cf0bc0b"><a name="a964c6bc005994dc3aa3d79f71cf0bc0b"></a><a name="a964c6bc005994dc3aa3d79f71cf0bc0b"></a>subnetName</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a1f81e99a483043f091891d9407b7051c"><a name="a1f81e99a483043f091891d9407b7051c"></a><a name="a1f81e99a483043f091891d9407b7051c"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581853_p675001311742"><a name="en-us_topic_0110581853_p675001311742"></a><a name="en-us_topic_0110581853_p675001311742"></a>Subnet name</p>
</td>
</tr>
<tr id="r37357716378c4795aeb7f8c85f30e439"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a4e26647863d14ed8b19fc3990898d719"><a name="a4e26647863d14ed8b19fc3990898d719"></a><a name="a4e26647863d14ed8b19fc3990898d719"></a>securityGroupsId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="acedd54e069ff43109769ce3ce9fcfa5e"><a name="acedd54e069ff43109769ce3ce9fcfa5e"></a><a name="acedd54e069ff43109769ce3ce9fcfa5e"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a3134202a084346c9ad38bde9bba97ddb"><a name="a3134202a084346c9ad38bde9bba97ddb"></a><a name="a3134202a084346c9ad38bde9bba97ddb"></a>Security group ID</p>
</td>
</tr>
<tr id="rfbe1ca753396446d88cdfa97d2dc0bfc"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a662d07db4f68404d98b78c92735efab5"><a name="a662d07db4f68404d98b78c92735efab5"></a><a name="a662d07db4f68404d98b78c92735efab5"></a>slaveSecurityGroupsId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0110581853_p335596211742"><a name="en-us_topic_0110581853_p335596211742"></a><a name="en-us_topic_0110581853_p335596211742"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581853_p339752011742"><a name="en-us_topic_0110581853_p339752011742"></a><a name="en-us_topic_0110581853_p339752011742"></a>Security group ID of a non-Master node. Currently, one MRS cluster uses only one security group. Therefore, this field has been discarded. This field returns the same value as <strong id="b8977195717443"><a name="b8977195717443"></a><a name="b8977195717443"></a>securityGroupsId</strong> does for compatibility consideration.</p>
</td>
</tr>
<tr id="row15246511027"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p199385353416"><a name="p199385353416"></a><a name="p199385353416"></a>bootstrap_scripts</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p241241133713"><a name="p241241133713"></a><a name="p241241133713"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p14160173618352"><a name="p14160173618352"></a><a name="p14160173618352"></a>Bootstrap action script information. For more parameter description, see <a href="#table1258382865010">Table 5</a>.</p>
<p id="p12412410370"><a name="p12412410370"></a><a name="p12412410370"></a>MRS 1.7.2 or later supports this parameter.</p>
</td>
</tr>
<tr id="r4e4bc96c9c734b73a8cdbb6ff0a854eb"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ae732bf7f74b8486aa18747a766482618"><a name="ae732bf7f74b8486aa18747a766482618"></a><a name="ae732bf7f74b8486aa18747a766482618"></a>stageDesc</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a82537f9fb6bd4725b3546474a581c4f6"><a name="a82537f9fb6bd4725b3546474a581c4f6"></a><a name="a82537f9fb6bd4725b3546474a581c4f6"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="acf4e438fc5ca4bb5a7fe7dc73393331d"><a name="acf4e438fc5ca4bb5a7fe7dc73393331d"></a><a name="acf4e438fc5ca4bb5a7fe7dc73393331d"></a>Cluster operation progress description.</p>
<div class="p" id="a818d39a3292948508ce11cc2678ff7f4"><a name="a818d39a3292948508ce11cc2678ff7f4"></a><a name="a818d39a3292948508ce11cc2678ff7f4"></a>The cluster installation progress includes:<a name="ub1cafa16e10d4a0981f5f722a4b30147"></a><a name="ub1cafa16e10d4a0981f5f722a4b30147"></a><ul id="ub1cafa16e10d4a0981f5f722a4b30147"><li>Verifying cluster parameters: Cluster parameters are being verified.</li><li>Applying for cluster resources: Cluster resources are being applied for.</li><li>Creating VMs: The VMs are being created.</li><li>Initializing VMs: The VMs are being initialized.</li><li>Installing MRS Manager: MRS Manager is being installed.</li><li>Deploying the cluster: The cluster is being deployed.</li><li>Cluster installation failed: Failed to install the cluster.</li></ul>
</div>
<div class="p" id="a2cfa8e32e44c441ba23de0b460f9f4e4"><a name="a2cfa8e32e44c441ba23de0b460f9f4e4"></a><a name="a2cfa8e32e44c441ba23de0b460f9f4e4"></a>The cluster scale-out progress includes:<a name="ufe258da9ad3a48d4942791399c0ccf86"></a><a name="ufe258da9ad3a48d4942791399c0ccf86"></a><ul id="ufe258da9ad3a48d4942791399c0ccf86"><li>Preparing for scale-out: Cluster scale-out is being prepared.</li><li>Creating VMs: The VMs are being created.</li><li>Initializing VMs: The VMs are being initialized.</li><li>Adding nodes to the cluster: The nodes are being added to the cluster.</li><li>Scale-out failed: Failed to scale out the cluster.</li></ul>
</div>
<div class="p" id="a0de8520663024d38874448ff1b548357"><a name="a0de8520663024d38874448ff1b548357"></a><a name="a0de8520663024d38874448ff1b548357"></a>The cluster scale-in progress includes:<a name="ue6c02feb34da4acd8371c66455699885"></a><a name="ue6c02feb34da4acd8371c66455699885"></a><ul id="ue6c02feb34da4acd8371c66455699885"><li>Preparing for scale-in: Cluster scale-in is being prepared.</li><li>Decommissioning instance: The instance is being decommissioned.</li><li>Deleting VMs: The VMs are being deleted.</li><li>Deleting nodes from the cluster: The nodes are being deleted from the cluster.</li><li>Scale-in failed: Failed to scale in the cluster.</li></ul>
</div>
<p id="a09e704768abc4dec9abdff3449e3e38a"><a name="a09e704768abc4dec9abdff3449e3e38a"></a><a name="a09e704768abc4dec9abdff3449e3e38a"></a>If the cluster installation, scale-out, or scale-in fails, <strong id="b1572620134619"><a name="b1572620134619"></a><a name="b1572620134619"></a>stageDesc</strong> will display the failure cause. For details, see <a href="resizing-a-cluster.md#table101661350414">Table 6</a>.</p>
</td>
</tr>
<tr id="rcbe6465f55224482bb4d3d1ff83dca7b"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110581853_p323403095641"><a name="en-us_topic_0110581853_p323403095641"></a><a name="en-us_topic_0110581853_p323403095641"></a>mrsManagerFinish</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a6fa38020fdb0448cadf21ca3a4fb69e4"><a name="a6fa38020fdb0448cadf21ca3a4fb69e4"></a><a name="a6fa38020fdb0448cadf21ca3a4fb69e4"></a>boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a8178f77fe0b54ef288d2ea36b33b70f3"><a name="a8178f77fe0b54ef288d2ea36b33b70f3"></a><a name="a8178f77fe0b54ef288d2ea36b33b70f3"></a>Whether MRS Manager installation is finished during cluster creation.</p>
<a name="ue62bf4e186224b7192b3a2e73f97e14e"></a><a name="ue62bf4e186224b7192b3a2e73f97e14e"></a><ul id="ue62bf4e186224b7192b3a2e73f97e14e"><li><strong id="b1194328161613"><a name="b1194328161613"></a><a name="b1194328161613"></a>true</strong>: MRS Manager installation is finished.</li><li><strong id="b203481111191612"><a name="b203481111191612"></a><a name="b203481111191612"></a>false</strong>: MRS Manager installation is not finished.</li></ul>
</td>
</tr>
<tr id="r40988b13f4f548a3983578f8e03f3f62"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="af4b0d84df98042f68275cf832c802d77"><a name="af4b0d84df98042f68275cf832c802d77"></a><a name="af4b0d84df98042f68275cf832c802d77"></a>safeMode</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a78cfbe87380a4db9b27b125b549cf8d6"><a name="a78cfbe87380a4db9b27b125b549cf8d6"></a><a name="a78cfbe87380a4db9b27b125b549cf8d6"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a8abdffe887b641f1932f73e277c323fd"><a name="a8abdffe887b641f1932f73e277c323fd"></a><a name="a8abdffe887b641f1932f73e277c323fd"></a>Running mode of an MRS cluster</p>
<a name="ubd370c44676647059633eea4b757b10a"></a><a name="ubd370c44676647059633eea4b757b10a"></a><ul id="ubd370c44676647059633eea4b757b10a"><li><strong id="b2771111618168"><a name="b2771111618168"></a><a name="b2771111618168"></a>0</strong>: Normal cluster</li><li><strong id="b6919269168"><a name="b6919269168"></a><a name="b6919269168"></a>1</strong>: Security cluster</li></ul>
</td>
</tr>
<tr id="rfb8116715b5d4def9f3968d50bbe47f4"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110581853_p348827911742"><a name="en-us_topic_0110581853_p348827911742"></a><a name="en-us_topic_0110581853_p348827911742"></a>clusterVersion</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0110581853_p247795811742"><a name="en-us_topic_0110581853_p247795811742"></a><a name="en-us_topic_0110581853_p247795811742"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a8024d729f4b3453abe8284d1efcb7bc1"><a name="a8024d729f4b3453abe8284d1efcb7bc1"></a><a name="a8024d729f4b3453abe8284d1efcb7bc1"></a>Cluster version</p>
</td>
</tr>
<tr id="r88cfab3a9b664db08318dbb0e7e717cd"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ab02619d914a44207b325edc8574325aa"><a name="ab02619d914a44207b325edc8574325aa"></a><a name="ab02619d914a44207b325edc8574325aa"></a>nodePublicCertName</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a8685108f65374ac49263514c2cc6b643"><a name="a8685108f65374ac49263514c2cc6b643"></a><a name="a8685108f65374ac49263514c2cc6b643"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a8dec9af3799c4fc39d40cb8d22648fad"><a name="a8dec9af3799c4fc39d40cb8d22648fad"></a><a name="a8dec9af3799c4fc39d40cb8d22648fad"></a>Name of the key file</p>
</td>
</tr>
<tr id="r097ea2a0c5a24a5d95f67306c52f8614"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a64ebadcd51744596a3c5477488c1aec0"><a name="a64ebadcd51744596a3c5477488c1aec0"></a><a name="a64ebadcd51744596a3c5477488c1aec0"></a>masterNodeIp</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ade16183ea33d4f91b272a4fa0145cd0d"><a name="ade16183ea33d4f91b272a4fa0145cd0d"></a><a name="ade16183ea33d4f91b272a4fa0145cd0d"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a54ef7ba2c0de4c479053489a1f6d38ce"><a name="a54ef7ba2c0de4c479053489a1f6d38ce"></a><a name="a54ef7ba2c0de4c479053489a1f6d38ce"></a>IP address of a Master node</p>
</td>
</tr>
<tr id="rd02278de90cc4a40852de6c2a6d8658e"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a6a639410c87245f1bd7728fd2264fd18"><a name="a6a639410c87245f1bd7728fd2264fd18"></a><a name="a6a639410c87245f1bd7728fd2264fd18"></a>privateIpFirst</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a56ea13797b5442bd87fc7a7ba62c6dd9"><a name="a56ea13797b5442bd87fc7a7ba62c6dd9"></a><a name="a56ea13797b5442bd87fc7a7ba62c6dd9"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ad27d84dcc9184551b35afab327b806f1"><a name="ad27d84dcc9184551b35afab327b806f1"></a><a name="ad27d84dcc9184551b35afab327b806f1"></a>Preferred private IP address</p>
</td>
</tr>
<tr id="r89ac793c38d64f48ad51264479c61474"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a024f4d0a395b4b218aa5fd23527fed79"><a name="a024f4d0a395b4b218aa5fd23527fed79"></a><a name="a024f4d0a395b4b218aa5fd23527fed79"></a>errorInfo</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a504a860cf5ab4dc9ae638c8837ef074a"><a name="a504a860cf5ab4dc9ae638c8837ef074a"></a><a name="a504a860cf5ab4dc9ae638c8837ef074a"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ab44397ceee3c4bf29bc472f788e55819"><a name="ab44397ceee3c4bf29bc472f788e55819"></a><a name="ab44397ceee3c4bf29bc472f788e55819"></a>Error message</p>
</td>
</tr>
<tr id="r79aa93c23a524b988ffd5c9188507b89"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110581853_p32874175319"><a name="en-us_topic_0110581853_p32874175319"></a><a name="en-us_topic_0110581853_p32874175319"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0110581853_p192871817631"><a name="en-us_topic_0110581853_p192871817631"></a><a name="en-us_topic_0110581853_p192871817631"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581853_p182871317532"><a name="en-us_topic_0110581853_p182871317532"></a><a name="en-us_topic_0110581853_p182871317532"></a>Tag information</p>
</td>
</tr>
<tr id="r682a2c86c21b428f9b9bb1f39b18bc5a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a932f2cc4f94c4b4fa9ccc4af6fa7ebed"><a name="a932f2cc4f94c4b4fa9ccc4af6fa7ebed"></a><a name="a932f2cc4f94c4b4fa9ccc4af6fa7ebed"></a>chargingStartTime</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a9144c58fcde34675b5a71e2dfea11219"><a name="a9144c58fcde34675b5a71e2dfea11219"></a><a name="a9144c58fcde34675b5a71e2dfea11219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581853_p205723511742"><a name="en-us_topic_0110581853_p205723511742"></a><a name="en-us_topic_0110581853_p205723511742"></a>Start time of billing</p>
</td>
</tr>
<tr id="row19341104210552"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1534113428553"><a name="p1534113428553"></a><a name="p1534113428553"></a>clusterType</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p153411442175516"><a name="p153411442175516"></a><a name="p153411442175516"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p173411542185510"><a name="p173411542185510"></a><a name="p173411542185510"></a>Cluster type</p>
</td>
</tr>
<tr id="r52e4788c45b54b63aa0911accf339639"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a30977e22b7ad45988bd08d4970acd8ac"><a name="a30977e22b7ad45988bd08d4970acd8ac"></a><a name="a30977e22b7ad45988bd08d4970acd8ac"></a>logCollection</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="aeb231e3f17c643f3bdf77fac1d1da1b1"><a name="aeb231e3f17c643f3bdf77fac1d1da1b1"></a><a name="aeb231e3f17c643f3bdf77fac1d1da1b1"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a98c0af5c94244b5a87f0bd309cd5433b"><a name="a98c0af5c94244b5a87f0bd309cd5433b"></a><a name="a98c0af5c94244b5a87f0bd309cd5433b"></a>Whether to collect logs when cluster installation fails</p>
<a name="uc5ff600ee21e4af98acce88059e8e2f1"></a><a name="uc5ff600ee21e4af98acce88059e8e2f1"></a><ul id="uc5ff600ee21e4af98acce88059e8e2f1"><li><strong id="b12428939171615"><a name="b12428939171615"></a><a name="b12428939171615"></a>0</strong>: Do not collect.</li><li><strong id="b1228054212167"><a name="b1228054212167"></a><a name="b1228054212167"></a>1</strong>: Collect.</li></ul>
</td>
</tr>
<tr id="r5f2faae6eb954649a6871b86fb156cbc"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110581853_p277116811651"><a name="en-us_topic_0110581853_p277116811651"></a><a name="en-us_topic_0110581853_p277116811651"></a>taskNodeGroups</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1271014583511"><a name="p1271014583511"></a><a name="p1271014583511"></a>List&lt;NodeGroup&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aed14af3415d14d8c8e4493ee144f165a"><a name="aed14af3415d14d8c8e4493ee144f165a"></a><a name="aed14af3415d14d8c8e4493ee144f165a"></a>List of Task nodes. For more parameter description, see <a href="#t985f9eb1ce0c4e0186e16ed2a6c7e731">Table 4</a>.</p>
</td>
</tr>
<tr id="row1994189113517"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1799416963519"><a name="p1799416963519"></a><a name="p1799416963519"></a>nodeGroups</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p599412915359"><a name="p599412915359"></a><a name="p599412915359"></a>List&lt;NodeGroup&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p999419915356"><a name="p999419915356"></a><a name="p999419915356"></a>List of Master, Core and Task nodes. For more parameter description, </p>
<p id="p7652181263617"><a name="p7652181263617"></a><a name="p7652181263617"></a>see <a href="#t985f9eb1ce0c4e0186e16ed2a6c7e731">Table 4</a>.</p>
</td>
</tr>
<tr id="r3b0b2f1bd6ac4c24be668a240d157cc3"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ad10725d40d5345b2815bd59027b71778"><a name="ad10725d40d5345b2815bd59027b71778"></a><a name="ad10725d40d5345b2815bd59027b71778"></a>masterDataVolumeType</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a8d385713cda742c59e39fd5de10e41e3"><a name="a8d385713cda742c59e39fd5de10e41e3"></a><a name="a8d385713cda742c59e39fd5de10e41e3"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a775d72e0ec46401699b121f19d923737"><a name="a775d72e0ec46401699b121f19d923737"></a><a name="a775d72e0ec46401699b121f19d923737"></a>Data disk storage type of the Master node. Currently, SATA, SAS, and SSD are supported.</p>
</td>
</tr>
<tr id="ree38f8953d2a4d44b2298c0beaaae766"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a9b957867014145558822659146103ad0"><a name="a9b957867014145558822659146103ad0"></a><a name="a9b957867014145558822659146103ad0"></a>masterDataVolumeSize</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="acf3a345c5fbd4090b854311772592ad5"><a name="acf3a345c5fbd4090b854311772592ad5"></a><a name="acf3a345c5fbd4090b854311772592ad5"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aedb1d96fee394755903c6602b5422b00"><a name="aedb1d96fee394755903c6602b5422b00"></a><a name="aedb1d96fee394755903c6602b5422b00"></a>Data disk storage space of the Master node. To increase data storage capacity, you can add disks at the same time when creating a cluster.</p>
<p id="acad9924248be44b584fec6f03babed24"><a name="acad9924248be44b584fec6f03babed24"></a><a name="acad9924248be44b584fec6f03babed24"></a>Value range: 100 GB to 32,000 GB</p>
</td>
</tr>
<tr id="r2a93b9f022494539bcd07422ebd820db"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a7b56861d6aad4dbea1fecac41b0c2398"><a name="a7b56861d6aad4dbea1fecac41b0c2398"></a><a name="a7b56861d6aad4dbea1fecac41b0c2398"></a>masterDataVolumeCount</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ab036d51adb8343dca43bee91ad9cf125"><a name="ab036d51adb8343dca43bee91ad9cf125"></a><a name="ab036d51adb8343dca43bee91ad9cf125"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aa0844421037c4286b6f845bb608e46f8"><a name="aa0844421037c4286b6f845bb608e46f8"></a><a name="aa0844421037c4286b6f845bb608e46f8"></a>Number of data disks of the Master node.</p>
<p id="a269dbeb8a2a644e089e61b7961da9635"><a name="a269dbeb8a2a644e089e61b7961da9635"></a><a name="a269dbeb8a2a644e089e61b7961da9635"></a>The value can be set to <strong id="b1529331311498"><a name="b1529331311498"></a><a name="b1529331311498"></a>1</strong> only.</p>
</td>
</tr>
<tr id="r86b5bcdc8fbb4cb3aa4fc7f78aded7bb"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a895848ea14f4414b838e4499c9b15c64"><a name="a895848ea14f4414b838e4499c9b15c64"></a><a name="a895848ea14f4414b838e4499c9b15c64"></a>coreDataVolumeType</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="aee2277799dc04fedbe605590717c7693"><a name="aee2277799dc04fedbe605590717c7693"></a><a name="aee2277799dc04fedbe605590717c7693"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110581853_p690620211638"><a name="en-us_topic_0110581853_p690620211638"></a><a name="en-us_topic_0110581853_p690620211638"></a>Data disk storage type of the Core node. Currently, SATA, SAS, and SSD are supported.</p>
</td>
</tr>
<tr id="re1db6d88dac04be0898a6ccdc14bedc1"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110581853_p145693711638"><a name="en-us_topic_0110581853_p145693711638"></a><a name="en-us_topic_0110581853_p145693711638"></a>coreDataVolumeSize</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a9e24583e9b3e45f29410d713fe538184"><a name="a9e24583e9b3e45f29410d713fe538184"></a><a name="a9e24583e9b3e45f29410d713fe538184"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a931fe7fd83a24796b2396aee0146ffd7"><a name="a931fe7fd83a24796b2396aee0146ffd7"></a><a name="a931fe7fd83a24796b2396aee0146ffd7"></a>Data disk storage space of the Core node. To increase data storage capacity, you can add disks at the same time when creating a cluster.</p>
<p id="a70c5d9ebb52a4d568298ab0ee3fc091d"><a name="a70c5d9ebb52a4d568298ab0ee3fc091d"></a><a name="a70c5d9ebb52a4d568298ab0ee3fc091d"></a>Value range: 100 GB to 32,000 GB</p>
</td>
</tr>
<tr id="r09d2bf7f4607482e96879228b19c4da0"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a1e0f1a36c4194b0a870922f162b5c36a"><a name="a1e0f1a36c4194b0a870922f162b5c36a"></a><a name="a1e0f1a36c4194b0a870922f162b5c36a"></a>coreDataVolumeCount</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="afc4acf9f9abb40aebd96745e3212b3bf"><a name="afc4acf9f9abb40aebd96745e3212b3bf"></a><a name="afc4acf9f9abb40aebd96745e3212b3bf"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a4cb5dab822fa46cb8c7d2cd966cded81"><a name="a4cb5dab822fa46cb8c7d2cd966cded81"></a><a name="a4cb5dab822fa46cb8c7d2cd966cded81"></a>Number of data disks of the Core node.</p>
<p id="ad9da3f1a22b3400d821e2247ac002a57"><a name="ad9da3f1a22b3400d821e2247ac002a57"></a><a name="ad9da3f1a22b3400d821e2247ac002a57"></a>Value range: 1 to 10</p>
</td>
</tr>
<tr id="row14751048102918"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1675114832918"><a name="p1675114832918"></a><a name="p1675114832918"></a>scale</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p6751184819296"><a name="p6751184819296"></a><a name="p6751184819296"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p147511482293"><a name="p147511482293"></a><a name="p147511482293"></a>Node change status. If this parameter is left blank, the cluster nodes are not changed.</p>
<p id="p17246183715315"><a name="p17246183715315"></a><a name="p17246183715315"></a>Possible values are as follows:</p>
<a name="ul15504745113118"></a><a name="ul15504745113118"></a><ul id="ul15504745113118"><li><strong id="b914776191715"><a name="b914776191715"></a><a name="b914776191715"></a>scaling-out</strong>: The cluster is being scaled out.</li><li><strong id="b1360359161720"><a name="b1360359161720"></a><a name="b1360359161720"></a>scaling-in</strong>: The cluster is being scaled in.</li><li><strong id="b1023018139179"><a name="b1023018139179"></a><a name="b1023018139179"></a>scaling-error</strong>: The cluster is in the running state and fails to be scaled in or out or the specifications fail to be scaled up for the last time.</li><li><strong id="b20621181761714"><a name="b20621181761714"></a><a name="b20621181761714"></a>scaling-up</strong>: The Master node specifications are being scaled up.</li><li><strong id="b530213229170"><a name="b530213229170"></a><a name="b530213229170"></a>scaling_up_first</strong>: The standby Master node specifications are being scaled up.</li><li><strong id="b52887255171"><a name="b52887255171"></a><a name="b52887255171"></a>scaled_up_first</strong>: The standby Master node specifications have been scaled up successfully.</li><li><strong id="b013432831716"><a name="b013432831716"></a><a name="b013432831716"></a>scaled-up-success</strong>: The Master node specifications have been scaled up successfully.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  3** **componentList**  parameter description

<a name="t0bc8fb7b4f444931b3c1b0ed022c2f79"></a>
<table><thead align="left"><tr id="en-us_topic_0172486178_r5cdd583aca4b4755881b19b62f09ccec"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="en-us_topic_0172486178_ac254da0dab1441ec92a6b33f1a6eb0b3"><a name="en-us_topic_0172486178_ac254da0dab1441ec92a6b33f1a6eb0b3"></a><a name="en-us_topic_0172486178_ac254da0dab1441ec92a6b33f1a6eb0b3"></a><strong id="en-us_topic_0172486178_b8888954155013"><a name="en-us_topic_0172486178_b8888954155013"></a><a name="en-us_topic_0172486178_b8888954155013"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0172486178_a8b1273cf6c0140e6b474ce7c8d105e6c"><a name="en-us_topic_0172486178_a8b1273cf6c0140e6b474ce7c8d105e6c"></a><a name="en-us_topic_0172486178_a8b1273cf6c0140e6b474ce7c8d105e6c"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="en-us_topic_0172486178_en-us_topic_0110581913_p949969815937"><a name="en-us_topic_0172486178_en-us_topic_0110581913_p949969815937"></a><a name="en-us_topic_0172486178_en-us_topic_0110581913_p949969815937"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0172486178_r39314b8086f442f48eda8af464423342"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_aed175543b6454ef9ad425f18d592120e"><a name="en-us_topic_0172486178_aed175543b6454ef9ad425f18d592120e"></a><a name="en-us_topic_0172486178_aed175543b6454ef9ad425f18d592120e"></a>componentId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_a69d7a7e94eb344b49a7baf4aabe6e2c6"><a name="en-us_topic_0172486178_a69d7a7e94eb344b49a7baf4aabe6e2c6"></a><a name="en-us_topic_0172486178_a69d7a7e94eb344b49a7baf4aabe6e2c6"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_a2cbc5a24356749c3ac36314ab4c3f090"><a name="en-us_topic_0172486178_a2cbc5a24356749c3ac36314ab4c3f090"></a><a name="en-us_topic_0172486178_a2cbc5a24356749c3ac36314ab4c3f090"></a>Component ID</p>
<a name="en-us_topic_0172486178_ul193151412181318"></a><a name="en-us_topic_0172486178_ul193151412181318"></a><ul id="en-us_topic_0172486178_ul193151412181318"><li>Component IDs of MRS 2.1.0 are as follows: <a name="en-us_topic_0172486178_ul23161412191313"></a><a name="en-us_topic_0172486178_ul23161412191313"></a><ul id="en-us_topic_0172486178_ul23161412191313"><li>MRS 2.1.0_001: Hadoop</li><li>MRS 2.1.0_002: Spark</li><li>MRS 2.1.0_003: HBase</li><li>MRS 2.1.0_004: Hive</li><li>MRS 2.1.0_005: Hue</li><li>MRS 2.1.0_006: Kafka</li><li>MRS 2.1.0_007: Storm</li><li>MRS 2.1.0_008: Loader</li><li>MRS 2.1.0_009: Flume</li><li>MRS 2.1.0_010: Tez</li><li>MRS 2.1.0_011: Presto</li><li>MRS 2.1.0_014: Flink</li></ul>
</li></ul>
<a name="en-us_topic_0172486178_ul157259529017"></a><a name="en-us_topic_0172486178_ul157259529017"></a><ul id="en-us_topic_0172486178_ul157259529017"><li>Component IDs of MRS 1.9.2 are as follows: <a name="en-us_topic_0172486178_ul918122913275"></a><a name="en-us_topic_0172486178_ul918122913275"></a><ul id="en-us_topic_0172486178_ul918122913275"><li>MRS 1.9.2_001: Hadoop</li><li>MRS 1.9.2_002: Spark</li><li>MRS 1.9.2_003: HBase</li><li>MRS 1.9.2_004: Hive</li><li>MRS 1.9.2_005: Hue</li><li>MRS 1.9.2_006: Kafka</li><li>MRS 1.9.2_007: Storm</li><li>MRS 1.9.2_008: Loader</li><li>MRS 1.9.2_009: Flume</li><li>MRS 1.9.2_010: Presto</li><li>MRS 1.9.2_011: KafkaManager</li><li>MRS 1.9.2_012: Flink</li><li>MRS 1.9.2_013: OpenTSDB</li><li>MRS 1.9.2_015: Alluxio</li><li>MRS 1.9.2_16: Ranger</li><li>MRS 1.9.2_17: Tez</li></ul>
</li><li>Component IDs of MRS 1.7.2 and MRS 1.6.3 are as follows:<a name="en-us_topic_0172486178_ul1379931812111"></a><a name="en-us_topic_0172486178_ul1379931812111"></a><ul id="en-us_topic_0172486178_ul1379931812111"><li>MRS 1.7.2_001: Hadoop</li><li>MRS 1.7.2_002: Spark</li><li>MRS 1.7.2_003: HBase</li><li>MRS 1.7.2_004: Hive</li><li>MRS 1.7.2_005: Hue</li><li>MRS 1.7.2_006: Kafka</li><li>MRS 1.7.2_007: Storm</li><li>MRS 1.7.2_008: Loader</li><li>MRS 1.7.2_009: Flume</li></ul>
</li></ul>
<p id="en-us_topic_0172486178_p666562343819"><a name="en-us_topic_0172486178_p666562343819"></a><a name="en-us_topic_0172486178_p666562343819"></a>For example, the <strong id="en-us_topic_0172486178_b1084011143113"><a name="en-us_topic_0172486178_b1084011143113"></a><a name="en-us_topic_0172486178_b1084011143113"></a>component_id</strong> of Hadoop is MRS 2.1.0_001, MRS 1.9.2_001, MRS 1.7.2_001, or MRS 1.6.3_001.</p>
</td>
</tr>
<tr id="en-us_topic_0172486178_r2786a9524cff4d728bb1e6924db9604f"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_ae2fc48462fa9475699eee62f3dd0c571"><a name="en-us_topic_0172486178_ae2fc48462fa9475699eee62f3dd0c571"></a><a name="en-us_topic_0172486178_ae2fc48462fa9475699eee62f3dd0c571"></a>componentName</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_a93a9337114124ee3bc25fd02a9e3b3ae"><a name="en-us_topic_0172486178_a93a9337114124ee3bc25fd02a9e3b3ae"></a><a name="en-us_topic_0172486178_a93a9337114124ee3bc25fd02a9e3b3ae"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_en-us_topic_0110581913_p601825815950"><a name="en-us_topic_0172486178_en-us_topic_0110581913_p601825815950"></a><a name="en-us_topic_0172486178_en-us_topic_0110581913_p601825815950"></a>Component name</p>
<a name="en-us_topic_0172486178_ul4211784545"></a><a name="en-us_topic_0172486178_ul4211784545"></a><ul id="en-us_topic_0172486178_ul4211784545"><li>MRS 2.1.0 or later support the following components: Presto, Hadoop, Spark, HBase, Hive, Tez, Hue, Loader, Flink, Flume, Kafka, and Storm</li><li>MRS 1.9.2 supports the following components: Presto, Hadoop, Spark, HBase, OpenTSDB, Hive, Hue, Loader, Tez, Flink, Alluxio, Ranger, Flume, Kafka, KafkaManager, and Storm</li><li>MRS 1.7.2 and MRS 1.6.3 support the following components: Hadoop, Spark, HBase, Hive, Hue, Loader, Flume, Kafka, and Storm</li></ul>
</td>
</tr>
<tr id="en-us_topic_0172486178_rdeb58819b19a47c4b396fe25d0ac3d36"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_ad027a7c5fda74a5dac59c2e7bf7e8550"><a name="en-us_topic_0172486178_ad027a7c5fda74a5dac59c2e7bf7e8550"></a><a name="en-us_topic_0172486178_ad027a7c5fda74a5dac59c2e7bf7e8550"></a>componentVersion</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_a5f3a3feb65b946c38297b7f2c19908fd"><a name="en-us_topic_0172486178_a5f3a3feb65b946c38297b7f2c19908fd"></a><a name="en-us_topic_0172486178_a5f3a3feb65b946c38297b7f2c19908fd"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_a87f565dffa3b48f9a22328317768b405"><a name="en-us_topic_0172486178_a87f565dffa3b48f9a22328317768b405"></a><a name="en-us_topic_0172486178_a87f565dffa3b48f9a22328317768b405"></a>Component version</p>
<a name="en-us_topic_0172486178_ul31291258111712"></a><a name="en-us_topic_0172486178_ul31291258111712"></a><ul id="en-us_topic_0172486178_ul31291258111712"><li>MRS 2.1.0 supports the following component versions:<div class="p" id="en-us_topic_0172486178_p623832344416"><a name="en-us_topic_0172486178_p623832344416"></a><a name="en-us_topic_0172486178_p623832344416"></a>Component versions of an analysis cluster:<a name="en-us_topic_0172486178_ul8238122314418"></a><a name="en-us_topic_0172486178_ul8238122314418"></a><ul id="en-us_topic_0172486178_ul8238122314418"><li>Presto: 308</li><li>Hadoop: 3.1.1</li><li>Spark: 2.3.2</li><li>HBase: 2.1.1</li><li>Hive: 3.1.0</li><li>Tez: 0.9.1</li><li>Hue: <span id="en-us_topic_0172486178_text79788306250"><a name="en-us_topic_0172486178_text79788306250"></a><a name="en-us_topic_0172486178_text79788306250"></a>3.11.0</span></li><li>Loader: <span id="en-us_topic_0172486178_text4978130112511"><a name="en-us_topic_0172486178_text4978130112511"></a><a name="en-us_topic_0172486178_text4978130112511"></a>2.0.0</span></li><li>Flink: 1.7.0</li></ul>
</div>
<div class="p" id="en-us_topic_0172486178_p18239182310441"><a name="en-us_topic_0172486178_p18239182310441"></a><a name="en-us_topic_0172486178_p18239182310441"></a>Component versions of a streaming cluster:<a name="en-us_topic_0172486178_ul023912237441"></a><a name="en-us_topic_0172486178_ul023912237441"></a><ul id="en-us_topic_0172486178_ul023912237441"><li>Kafka: 1.1.0</li><li>Storm: 1.2.1</li><li>Flume: <span id="en-us_topic_0172486178_text497918307257"><a name="en-us_topic_0172486178_text497918307257"></a><a name="en-us_topic_0172486178_text497918307257"></a>1.6.0</span></li></ul>
</div>
</li><li>MRS 1.9.2 supports the following component versions:<div class="p" id="en-us_topic_0172486178_p3990164033612"><a name="en-us_topic_0172486178_p3990164033612"></a><a name="en-us_topic_0172486178_p3990164033612"></a>Component versions of an analysis cluster:<a name="en-us_topic_0172486178_ul2099020407363"></a><a name="en-us_topic_0172486178_ul2099020407363"></a><ul id="en-us_topic_0172486178_ul2099020407363"><li>Presto: 0.216</li><li>Hadoop: 2.8.3</li><li>Spark: 2.2.2</li><li>HBase: 1.3.1</li><li>OpenTSDB: 2.3.0</li><li>Hive: 2.3.3</li><li>Hue: <span id="en-us_topic_0172486178_text2796102174115"><a name="en-us_topic_0172486178_text2796102174115"></a><a name="en-us_topic_0172486178_text2796102174115"></a>3.11.0</span></li><li>Loader: <span id="en-us_topic_0172486178_text1181562310410"><a name="en-us_topic_0172486178_text1181562310410"></a><a name="en-us_topic_0172486178_text1181562310410"></a>2.0.0</span></li><li>Tez: 0.9.1</li><li>Flink: 1.7.0</li><li>Alluxio: 2.0.1</li><li>Ranger: 1.0.1</li></ul>
</div>
<div class="p" id="en-us_topic_0172486178_p19991174063615"><a name="en-us_topic_0172486178_p19991174063615"></a><a name="en-us_topic_0172486178_p19991174063615"></a>Component versions of a streaming cluster:<a name="en-us_topic_0172486178_ul39911540123610"></a><a name="en-us_topic_0172486178_ul39911540123610"></a><ul id="en-us_topic_0172486178_ul39911540123610"><li>Kafka: 1.1.0</li><li>KafkaManager: 1.3.3.1</li><li>Storm: 1.2.1</li><li>Flume: <span id="en-us_topic_0172486178_text859319741"><a name="en-us_topic_0172486178_text859319741"></a><a name="en-us_topic_0172486178_text859319741"></a>1.6.0</span></li></ul>
</div>
</li><li>MRS 1.7.2 supports the following component versions:<div class="p" id="en-us_topic_0172486178_p31541581173"><a name="en-us_topic_0172486178_p31541581173"></a><a name="en-us_topic_0172486178_p31541581173"></a>Component versions of an analysis cluster:<a name="en-us_topic_0172486178_ul17160158111712"></a><a name="en-us_topic_0172486178_ul17160158111712"></a><ul id="en-us_topic_0172486178_ul17160158111712"><li>Hadoop: 2.8.3</li><li>Spark: 2.2.1</li><li>HBase: <span id="en-us_topic_0172486178_text682075583020"><a name="en-us_topic_0172486178_text682075583020"></a><a name="en-us_topic_0172486178_text682075583020"></a>1.3.1</span></li><li>Hive: <span id="en-us_topic_0172486178_text16419155793011"><a name="en-us_topic_0172486178_text16419155793011"></a><a name="en-us_topic_0172486178_text16419155793011"></a>1.2.1</span></li><li>Hue: <span id="en-us_topic_0172486178_text1416119361586"><a name="en-us_topic_0172486178_text1416119361586"></a><a name="en-us_topic_0172486178_text1416119361586"></a>3.11.0</span></li><li>Loader: <span id="en-us_topic_0172486178_text1438898961"><a name="en-us_topic_0172486178_text1438898961"></a><a name="en-us_topic_0172486178_text1438898961"></a>2.0.0</span></li></ul>
</div>
<div class="p" id="en-us_topic_0172486178_p132551058131720"><a name="en-us_topic_0172486178_p132551058131720"></a><a name="en-us_topic_0172486178_p132551058131720"></a>Component versions of a streaming cluster:<a name="en-us_topic_0172486178_ul1226119585179"></a><a name="en-us_topic_0172486178_ul1226119585179"></a><ul id="en-us_topic_0172486178_ul1226119585179"><li>Kafka: 0.10.2.0</li><li>Storm: <span id="en-us_topic_0172486178_text02971058101711"><a name="en-us_topic_0172486178_text02971058101711"></a><a name="en-us_topic_0172486178_text02971058101711"></a>1.0.2</span></li><li>Flume: <span id="en-us_topic_0172486178_text999318377582"><a name="en-us_topic_0172486178_text999318377582"></a><a name="en-us_topic_0172486178_text999318377582"></a>1.6.0</span></li></ul>
</div>
</li></ul>
<a name="en-us_topic_0172486178_u6738a612b0cf455592b3bcd33ff9c354"></a><a name="en-us_topic_0172486178_u6738a612b0cf455592b3bcd33ff9c354"></a><ul id="en-us_topic_0172486178_u6738a612b0cf455592b3bcd33ff9c354"><li>MRS 1.6.3 supports the following component versions:<div class="p" id="en-us_topic_0172486178_ae323927123e541b8a490aaebcf7632df"><a name="en-us_topic_0172486178_ae323927123e541b8a490aaebcf7632df"></a><a name="en-us_topic_0172486178_ae323927123e541b8a490aaebcf7632df"></a>Component versions of an analysis cluster:<a name="en-us_topic_0172486178_u04a4ea3e8b3f4048bf440a213250110d"></a><a name="en-us_topic_0172486178_u04a4ea3e8b3f4048bf440a213250110d"></a><ul id="en-us_topic_0172486178_u04a4ea3e8b3f4048bf440a213250110d"><li>Hadoop: <span id="en-us_topic_0172486178_t0f87b3845ded40438cdf1016322a128b"><a name="en-us_topic_0172486178_t0f87b3845ded40438cdf1016322a128b"></a><a name="en-us_topic_0172486178_t0f87b3845ded40438cdf1016322a128b"></a>2.7.2</span></li><li>Spark: 2.1.0</li><li>HBase: <span id="en-us_topic_0172486178_t855985d1b3a54c7b8880dcc78fb9571c"><a name="en-us_topic_0172486178_t855985d1b3a54c7b8880dcc78fb9571c"></a><a name="en-us_topic_0172486178_t855985d1b3a54c7b8880dcc78fb9571c"></a>1.3.1</span></li><li>Hive: <span id="en-us_topic_0172486178_t94e4a14080954d8689219835533c7696"><a name="en-us_topic_0172486178_t94e4a14080954d8689219835533c7696"></a><a name="en-us_topic_0172486178_t94e4a14080954d8689219835533c7696"></a>1.2.1</span></li><li>Hue: <span id="en-us_topic_0172486178_teddc07a7bf2b4ecc8d497039dab5ef6e"><a name="en-us_topic_0172486178_teddc07a7bf2b4ecc8d497039dab5ef6e"></a><a name="en-us_topic_0172486178_teddc07a7bf2b4ecc8d497039dab5ef6e"></a>3.11.0</span></li><li>Loader: <span id="en-us_topic_0172486178_tde62c720d17042dea0cc702abdaefea7"><a name="en-us_topic_0172486178_tde62c720d17042dea0cc702abdaefea7"></a><a name="en-us_topic_0172486178_tde62c720d17042dea0cc702abdaefea7"></a>2.0.0</span></li></ul>
</div>
<div class="p" id="en-us_topic_0172486178_af8e44931e7644cf8a13b9ee363c297e7"><a name="en-us_topic_0172486178_af8e44931e7644cf8a13b9ee363c297e7"></a><a name="en-us_topic_0172486178_af8e44931e7644cf8a13b9ee363c297e7"></a>Component versions of a streaming cluster:<a name="en-us_topic_0172486178_u5afd4973364e44c4b228bf66ffe35503"></a><a name="en-us_topic_0172486178_u5afd4973364e44c4b228bf66ffe35503"></a><ul id="en-us_topic_0172486178_u5afd4973364e44c4b228bf66ffe35503"><li>Kafka: <span id="en-us_topic_0172486178_tee4cc20227124a9c991e3e95d41a3dd9"><a name="en-us_topic_0172486178_tee4cc20227124a9c991e3e95d41a3dd9"></a><a name="en-us_topic_0172486178_tee4cc20227124a9c991e3e95d41a3dd9"></a>0.10.0.0</span></li><li>Storm: <span id="en-us_topic_0172486178_text198413291333"><a name="en-us_topic_0172486178_text198413291333"></a><a name="en-us_topic_0172486178_text198413291333"></a>1.0.2</span></li><li>Flume: <span id="en-us_topic_0172486178_tb130c3fba76444bf9f7722679fd50e95"><a name="en-us_topic_0172486178_tb130c3fba76444bf9f7722679fd50e95"></a><a name="en-us_topic_0172486178_tb130c3fba76444bf9f7722679fd50e95"></a>1.6.0</span></li></ul>
</div>
</li></ul>
</td>
</tr>
<tr id="en-us_topic_0172486178_rff3b68eefb0f4fbd8a889ae3aafdd8cb"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_ac4efd0130b414871bbda101ed18b829a"><a name="en-us_topic_0172486178_ac4efd0130b414871bbda101ed18b829a"></a><a name="en-us_topic_0172486178_ac4efd0130b414871bbda101ed18b829a"></a>componentDesc</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_a4d6168334a7d49eaa98687dd37b6e759"><a name="en-us_topic_0172486178_a4d6168334a7d49eaa98687dd37b6e759"></a><a name="en-us_topic_0172486178_a4d6168334a7d49eaa98687dd37b6e759"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_abd24f96372cf4ce680ba21c7bc5cbe40"><a name="en-us_topic_0172486178_abd24f96372cf4ce680ba21c7bc5cbe40"></a><a name="en-us_topic_0172486178_abd24f96372cf4ce680ba21c7bc5cbe40"></a>Component description</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **NodeGroup**  parameter description

<a name="t985f9eb1ce0c4e0186e16ed2a6c7e731"></a>
<table><thead align="left"><tr id="en-us_topic_0172486178_rb71a09c44d4845bb9e005db6c92bac3d"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="en-us_topic_0172486178_a94285558ebf148e393ca16fc271aa713"><a name="en-us_topic_0172486178_a94285558ebf148e393ca16fc271aa713"></a><a name="en-us_topic_0172486178_a94285558ebf148e393ca16fc271aa713"></a><strong id="en-us_topic_0172486178_b990316783414"><a name="en-us_topic_0172486178_b990316783414"></a><a name="en-us_topic_0172486178_b990316783414"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0172486178_aa72743b5263a4616b05119a37403b12a"><a name="en-us_topic_0172486178_aa72743b5263a4616b05119a37403b12a"></a><a name="en-us_topic_0172486178_aa72743b5263a4616b05119a37403b12a"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="en-us_topic_0172486178_ad9f74d87937e492daff9830ae1eaa065"><a name="en-us_topic_0172486178_ad9f74d87937e492daff9830ae1eaa065"></a><a name="en-us_topic_0172486178_ad9f74d87937e492daff9830ae1eaa065"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0172486178_r772c2a2c36894025883ba35bf6a9652f"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_a21ea093161dc4b28b54210d0214483e5"><a name="en-us_topic_0172486178_a21ea093161dc4b28b54210d0214483e5"></a><a name="en-us_topic_0172486178_a21ea093161dc4b28b54210d0214483e5"></a>groupName</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_ab11033caf61a4fa4a86a15439fb5daff"><a name="en-us_topic_0172486178_ab11033caf61a4fa4a86a15439fb5daff"></a><a name="en-us_topic_0172486178_ab11033caf61a4fa4a86a15439fb5daff"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_af8330597bc564ca8b62a4c22f87c0b5b"><a name="en-us_topic_0172486178_af8330597bc564ca8b62a4c22f87c0b5b"></a><a name="en-us_topic_0172486178_af8330597bc564ca8b62a4c22f87c0b5b"></a>Node group name</p>
</td>
</tr>
<tr id="en-us_topic_0172486178_r685acdcd63804970be9df9ccb752824c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_a9a6835b784d045deb7520c63ee38ad2e"><a name="en-us_topic_0172486178_a9a6835b784d045deb7520c63ee38ad2e"></a><a name="en-us_topic_0172486178_a9a6835b784d045deb7520c63ee38ad2e"></a>nodeNum</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_a92ccc56708e54ecf9a23c77eb3efc231"><a name="en-us_topic_0172486178_a92ccc56708e54ecf9a23c77eb3efc231"></a><a name="en-us_topic_0172486178_a92ccc56708e54ecf9a23c77eb3efc231"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_en-us_topic_0110581913_p604125417392"><a name="en-us_topic_0172486178_en-us_topic_0110581913_p604125417392"></a><a name="en-us_topic_0172486178_en-us_topic_0110581913_p604125417392"></a>Number of nodes. The value ranges from 0 to 500. The minimum number of Master and Core nodes is 1 and the total number of Core and Task nodes cannot exceed 500.</p>
</td>
</tr>
<tr id="en-us_topic_0172486178_r3ff0d41b7fa44f67a30507227df1df19"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_en-us_topic_0110581913_p425651111412"><a name="en-us_topic_0172486178_en-us_topic_0110581913_p425651111412"></a><a name="en-us_topic_0172486178_en-us_topic_0110581913_p425651111412"></a>nodeSize</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_en-us_topic_0110581913_p60006581181"><a name="en-us_topic_0172486178_en-us_topic_0110581913_p60006581181"></a><a name="en-us_topic_0172486178_en-us_topic_0110581913_p60006581181"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_abfaa8eeb949c4ee5a98200fc6528e42e"><a name="en-us_topic_0172486178_abfaa8eeb949c4ee5a98200fc6528e42e"></a><a name="en-us_topic_0172486178_abfaa8eeb949c4ee5a98200fc6528e42e"></a>Instance specifications of a node </p>
</td>
</tr>
<tr id="en-us_topic_0172486178_rfb678198b0ba4844a39f0cf9366168ea"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_af8a5b305e2754841a9490a5bb1984d86"><a name="en-us_topic_0172486178_af8a5b305e2754841a9490a5bb1984d86"></a><a name="en-us_topic_0172486178_af8a5b305e2754841a9490a5bb1984d86"></a>nodeSpecId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_a397e7084c91744e386c50135480aff85"><a name="en-us_topic_0172486178_a397e7084c91744e386c50135480aff85"></a><a name="en-us_topic_0172486178_a397e7084c91744e386c50135480aff85"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_aa8db59e414e645cc9cb8ec2dc4d7479e"><a name="en-us_topic_0172486178_aa8db59e414e645cc9cb8ec2dc4d7479e"></a><a name="en-us_topic_0172486178_aa8db59e414e645cc9cb8ec2dc4d7479e"></a>Instance specification ID of a node</p>
</td>
</tr>
<tr id="en-us_topic_0172486178_r5e6ec48632bc4a20b39222b03003e2ea"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_aac6c899a4c9d4d958226d208be51f5a2"><a name="en-us_topic_0172486178_aac6c899a4c9d4d958226d208be51f5a2"></a><a name="en-us_topic_0172486178_aac6c899a4c9d4d958226d208be51f5a2"></a>nodeProductId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_a6134c6e5eeef4805b21a92ddb0b4f43a"><a name="en-us_topic_0172486178_a6134c6e5eeef4805b21a92ddb0b4f43a"></a><a name="en-us_topic_0172486178_a6134c6e5eeef4805b21a92ddb0b4f43a"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_a5bc3f61bd74a49eda19d271c1ea45d1d"><a name="en-us_topic_0172486178_a5bc3f61bd74a49eda19d271c1ea45d1d"></a><a name="en-us_topic_0172486178_a5bc3f61bd74a49eda19d271c1ea45d1d"></a>Instance product ID of a node</p>
</td>
</tr>
<tr id="en-us_topic_0172486178_r44088dff65db49e7adcfe1689612064a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_aac3e491b249443f0818bc7fb586d81ee"><a name="en-us_topic_0172486178_aac3e491b249443f0818bc7fb586d81ee"></a><a name="en-us_topic_0172486178_aac3e491b249443f0818bc7fb586d81ee"></a>vmProductId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_af0c4b33732e445548b7bc7be8368e8ae"><a name="en-us_topic_0172486178_af0c4b33732e445548b7bc7be8368e8ae"></a><a name="en-us_topic_0172486178_af0c4b33732e445548b7bc7be8368e8ae"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_a2de7baded5a74a2d97517286b00261f5"><a name="en-us_topic_0172486178_a2de7baded5a74a2d97517286b00261f5"></a><a name="en-us_topic_0172486178_a2de7baded5a74a2d97517286b00261f5"></a>VM product ID of a node</p>
</td>
</tr>
<tr id="en-us_topic_0172486178_r001eacc59c634fc0b761167070eb116f"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_ad5e229de9769478f9fdef9c0d30d0052"><a name="en-us_topic_0172486178_ad5e229de9769478f9fdef9c0d30d0052"></a><a name="en-us_topic_0172486178_ad5e229de9769478f9fdef9c0d30d0052"></a>vmSpecCode</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_ad0294285f7e442999ce6cfbb45361b44"><a name="en-us_topic_0172486178_ad0294285f7e442999ce6cfbb45361b44"></a><a name="en-us_topic_0172486178_ad0294285f7e442999ce6cfbb45361b44"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_a003c6b4040ee4c01b2fb5f51c6367d9d"><a name="en-us_topic_0172486178_a003c6b4040ee4c01b2fb5f51c6367d9d"></a><a name="en-us_topic_0172486178_a003c6b4040ee4c01b2fb5f51c6367d9d"></a>VM specifications of a node</p>
</td>
</tr>
<tr id="en-us_topic_0172486178_r62dc652909934b839ed5ab0dbab7d55e"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_ab908078805b747188f065a8d46f3210d"><a name="en-us_topic_0172486178_ab908078805b747188f065a8d46f3210d"></a><a name="en-us_topic_0172486178_ab908078805b747188f065a8d46f3210d"></a>rootVolumeSize</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_ab21d0fc2d1074e8baf95bbb736e93e67"><a name="en-us_topic_0172486178_ab21d0fc2d1074e8baf95bbb736e93e67"></a><a name="en-us_topic_0172486178_ab21d0fc2d1074e8baf95bbb736e93e67"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_en-us_topic_0110581913_p200757511847"><a name="en-us_topic_0172486178_en-us_topic_0110581913_p200757511847"></a><a name="en-us_topic_0172486178_en-us_topic_0110581913_p200757511847"></a>System disk size of a node. This parameter is not configurable and its default value is <strong id="en-us_topic_0172486178_b84235270620266"><a name="en-us_topic_0172486178_b84235270620266"></a><a name="en-us_topic_0172486178_b84235270620266"></a>40 GB</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0172486178_ra1145762730546c595def5fe555b451a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_a445d8504e2df46e38e3e20862d5a4517"><a name="en-us_topic_0172486178_a445d8504e2df46e38e3e20862d5a4517"></a><a name="en-us_topic_0172486178_a445d8504e2df46e38e3e20862d5a4517"></a>rootVolumeProductId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_ac05728f1dbff41daa43670cb6c2a7be8"><a name="en-us_topic_0172486178_ac05728f1dbff41daa43670cb6c2a7be8"></a><a name="en-us_topic_0172486178_ac05728f1dbff41daa43670cb6c2a7be8"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_a1b1f30e9690f4527b4c1f1cb19d16d38"><a name="en-us_topic_0172486178_a1b1f30e9690f4527b4c1f1cb19d16d38"></a><a name="en-us_topic_0172486178_a1b1f30e9690f4527b4c1f1cb19d16d38"></a>System disk product ID of a node</p>
</td>
</tr>
<tr id="en-us_topic_0172486178_ra94f567604e94dce8d62dbd7c32a9295"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_a4164ec2b2020429c9c3933749379ab98"><a name="en-us_topic_0172486178_a4164ec2b2020429c9c3933749379ab98"></a><a name="en-us_topic_0172486178_a4164ec2b2020429c9c3933749379ab98"></a>rootVolumeType</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_a4ce29b1d4bc74f038b1c756d56fe9251"><a name="en-us_topic_0172486178_a4ce29b1d4bc74f038b1c756d56fe9251"></a><a name="en-us_topic_0172486178_a4ce29b1d4bc74f038b1c756d56fe9251"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_a46f150f4f39142538cd1a3fed0bc1ee7"><a name="en-us_topic_0172486178_a46f150f4f39142538cd1a3fed0bc1ee7"></a><a name="en-us_topic_0172486178_a46f150f4f39142538cd1a3fed0bc1ee7"></a>System disk type of a node</p>
</td>
</tr>
<tr id="en-us_topic_0172486178_rbd0491d62d7849878ad92ffc473c5bbb"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_a14cdc064b9ff4bd3b2ff31b606ce189e"><a name="en-us_topic_0172486178_a14cdc064b9ff4bd3b2ff31b606ce189e"></a><a name="en-us_topic_0172486178_a14cdc064b9ff4bd3b2ff31b606ce189e"></a>rootVolumeResourceSpecCode</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_a4d00b1aa898b459ea05525398eb34fcf"><a name="en-us_topic_0172486178_a4d00b1aa898b459ea05525398eb34fcf"></a><a name="en-us_topic_0172486178_a4d00b1aa898b459ea05525398eb34fcf"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_ad44fb03082fd4d8399f5a1590c2da2aa"><a name="en-us_topic_0172486178_ad44fb03082fd4d8399f5a1590c2da2aa"></a><a name="en-us_topic_0172486178_ad44fb03082fd4d8399f5a1590c2da2aa"></a>System disk product specifications of a node</p>
</td>
</tr>
<tr id="en-us_topic_0172486178_rccf420005b74474987f58a8c0508808d"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_ae1c0d77a20e44534b3aae6cfb00c72e4"><a name="en-us_topic_0172486178_ae1c0d77a20e44534b3aae6cfb00c72e4"></a><a name="en-us_topic_0172486178_ae1c0d77a20e44534b3aae6cfb00c72e4"></a>rootVolumeResourceType</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_a2ae3d79db3734c23964156fe2daf9add"><a name="en-us_topic_0172486178_a2ae3d79db3734c23964156fe2daf9add"></a><a name="en-us_topic_0172486178_a2ae3d79db3734c23964156fe2daf9add"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_a2621e2f95d0c4ad587cf61a7eb27e5cc"><a name="en-us_topic_0172486178_a2621e2f95d0c4ad587cf61a7eb27e5cc"></a><a name="en-us_topic_0172486178_a2621e2f95d0c4ad587cf61a7eb27e5cc"></a>System disk product type of a node</p>
</td>
</tr>
<tr id="en-us_topic_0172486178_rc4b398e9fe8c47ed9eab7783efcf874a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_aa3da3db1c5844bfe80e0afb2325570b4"><a name="en-us_topic_0172486178_aa3da3db1c5844bfe80e0afb2325570b4"></a><a name="en-us_topic_0172486178_aa3da3db1c5844bfe80e0afb2325570b4"></a>dataVolumeType</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_ade6cdf58add24c5e93acd30a43d77c58"><a name="en-us_topic_0172486178_ade6cdf58add24c5e93acd30a43d77c58"></a><a name="en-us_topic_0172486178_ade6cdf58add24c5e93acd30a43d77c58"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_aa790158b0b444a67a47b75fa6ac4d09b"><a name="en-us_topic_0172486178_aa790158b0b444a67a47b75fa6ac4d09b"></a><a name="en-us_topic_0172486178_aa790158b0b444a67a47b75fa6ac4d09b"></a>Data disk storage type of a node. Currently, SATA, SAS, and SSD are supported.</p>
<a name="en-us_topic_0172486178_u9f5e1d8806514426a6e9c525d6c02ae4"></a><a name="en-us_topic_0172486178_u9f5e1d8806514426a6e9c525d6c02ae4"></a><ul id="en-us_topic_0172486178_u9f5e1d8806514426a6e9c525d6c02ae4"><li>SATA: Common I/O</li><li>SAS: High I/O</li><li>SSD: Ultra-high I/O</li></ul>
</td>
</tr>
<tr id="en-us_topic_0172486178_r88ceb6f16ec2420c9b3d352c6c2ce247"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_a5e309b28f6e54d6590c66cf9700b157d"><a name="en-us_topic_0172486178_a5e309b28f6e54d6590c66cf9700b157d"></a><a name="en-us_topic_0172486178_a5e309b28f6e54d6590c66cf9700b157d"></a>dataVolumeCount</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_a1b6b88569b804f2f92d6afc483561f7d"><a name="en-us_topic_0172486178_a1b6b88569b804f2f92d6afc483561f7d"></a><a name="en-us_topic_0172486178_a1b6b88569b804f2f92d6afc483561f7d"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_a2d988c7551df4a81854d7b9a4dbfdef9"><a name="en-us_topic_0172486178_a2d988c7551df4a81854d7b9a4dbfdef9"></a><a name="en-us_topic_0172486178_a2d988c7551df4a81854d7b9a4dbfdef9"></a>Number of data disks of a node</p>
</td>
</tr>
<tr id="en-us_topic_0172486178_racc1050d22de4f54aabbd2c2ced25c2c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_aab3c5eac8ee74fd9a48c935f4b0b8d86"><a name="en-us_topic_0172486178_aab3c5eac8ee74fd9a48c935f4b0b8d86"></a><a name="en-us_topic_0172486178_aab3c5eac8ee74fd9a48c935f4b0b8d86"></a>dataVolumeSize</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_a5bd2105a280041f189c918e86c6131c4"><a name="en-us_topic_0172486178_a5bd2105a280041f189c918e86c6131c4"></a><a name="en-us_topic_0172486178_a5bd2105a280041f189c918e86c6131c4"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_a506ed75cabee4f2faba58f6c4d481fa9"><a name="en-us_topic_0172486178_a506ed75cabee4f2faba58f6c4d481fa9"></a><a name="en-us_topic_0172486178_a506ed75cabee4f2faba58f6c4d481fa9"></a>Data disk storage space of a node</p>
</td>
</tr>
<tr id="en-us_topic_0172486178_r52a96e7d17ce4f3a9eadc7d7cc31880e"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_ac4a609c326424822bcd0243aa38a0155"><a name="en-us_topic_0172486178_ac4a609c326424822bcd0243aa38a0155"></a><a name="en-us_topic_0172486178_ac4a609c326424822bcd0243aa38a0155"></a>dataVolumeProductId</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_ad2f91538b2c44b48979ad38a8620f059"><a name="en-us_topic_0172486178_ad2f91538b2c44b48979ad38a8620f059"></a><a name="en-us_topic_0172486178_ad2f91538b2c44b48979ad38a8620f059"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_a3cc4de2d5a564fe7a1be33a103c850fe"><a name="en-us_topic_0172486178_a3cc4de2d5a564fe7a1be33a103c850fe"></a><a name="en-us_topic_0172486178_a3cc4de2d5a564fe7a1be33a103c850fe"></a>Data disk product ID of a node</p>
</td>
</tr>
<tr id="en-us_topic_0172486178_r1cb3bcf5b93f4e588020e361de63a209"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_abef89f6ae16646a3a6ee31b211851f90"><a name="en-us_topic_0172486178_abef89f6ae16646a3a6ee31b211851f90"></a><a name="en-us_topic_0172486178_abef89f6ae16646a3a6ee31b211851f90"></a>dataVolumeResourceSpecCode</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_a78420bba01144cf48c60043c1b2f2370"><a name="en-us_topic_0172486178_a78420bba01144cf48c60043c1b2f2370"></a><a name="en-us_topic_0172486178_a78420bba01144cf48c60043c1b2f2370"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_a7dadecb9771948ecbeecdbe5a3eee6bb"><a name="en-us_topic_0172486178_a7dadecb9771948ecbeecdbe5a3eee6bb"></a><a name="en-us_topic_0172486178_a7dadecb9771948ecbeecdbe5a3eee6bb"></a>Data disk product specifications of a node</p>
</td>
</tr>
<tr id="en-us_topic_0172486178_r0a2a9426d6274990a3f406be65b77b34"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0172486178_a1baaf1591f2448ab8ec85a9278681587"><a name="en-us_topic_0172486178_a1baaf1591f2448ab8ec85a9278681587"></a><a name="en-us_topic_0172486178_a1baaf1591f2448ab8ec85a9278681587"></a>dataVolumeResourceType</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0172486178_a54bab5459e034e66bd296b444e31e957"><a name="en-us_topic_0172486178_a54bab5459e034e66bd296b444e31e957"></a><a name="en-us_topic_0172486178_a54bab5459e034e66bd296b444e31e957"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0172486178_a13c8af6c0a6247869bcf6ca3c57348b3"><a name="en-us_topic_0172486178_a13c8af6c0a6247869bcf6ca3c57348b3"></a><a name="en-us_topic_0172486178_a13c8af6c0a6247869bcf6ca3c57348b3"></a>Data disk product type of a node</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **bootstrap\_scripts**  parameter description

<a name="table1258382865010"></a>
<table><thead align="left"><tr id="row16585132875017"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p2058552815010"><a name="p2058552815010"></a><a name="p2058552815010"></a><strong id="b4454134410215"><a name="b4454134410215"></a><a name="b4454134410215"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p145856289503"><a name="p145856289503"></a><a name="p145856289503"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p35851281504"><a name="p35851281504"></a><a name="p35851281504"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19585182815014"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p0223193618537"><a name="p0223193618537"></a><a name="p0223193618537"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1422373615314"><a name="p1422373615314"></a><a name="p1422373615314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p27361059145112"><a name="p27361059145112"></a><a name="p27361059145112"></a>Name of a bootstrap action script. It must be unique in a cluster.</p>
<p id="p1768234115215"><a name="p1768234115215"></a><a name="p1768234115215"></a>The value can contain only digits, letters, spaces, hyphens (-), and underscores (_) and cannot start with a space.</p>
<p id="p35651138195212"><a name="p35651138195212"></a><a name="p35651138195212"></a>The value can contain 1 to 64 characters.</p>
</td>
</tr>
<tr id="row55851328175016"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p132232362536"><a name="p132232362536"></a><a name="p132232362536"></a>uri</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p16223183655320"><a name="p16223183655320"></a><a name="p16223183655320"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p13373112592717"><a name="p13373112592717"></a><a name="p13373112592717"></a>Path of the shell script. Set this parameter to an OBS bucket path or a local VM path.</p>
<a name="ul129121753017"></a><a name="ul129121753017"></a><ul id="ul129121753017"><li>OBS bucket path: Enter a script path manually. For example, enter the path of the public sample script provided by MRS. Example: <strong id="b415132882317"><a name="b415132882317"></a><a name="b415132882317"></a>s3a://bootstrap/presto/presto-install.sh</strong>. If <strong id="b19154132816233"><a name="b19154132816233"></a><a name="b19154132816233"></a>dualroles</strong> is installed, the parameter of the <strong id="b41561528152315"><a name="b41561528152315"></a><a name="b41561528152315"></a>presto-install.sh</strong> script is <strong id="b18161202817231"><a name="b18161202817231"></a><a name="b18161202817231"></a>dualroles</strong>. If <strong id="b16163628172317"><a name="b16163628172317"></a><a name="b16163628172317"></a>worker</strong> is installed, the parameter of the <strong id="b141651728172317"><a name="b141651728172317"></a><a name="b141651728172317"></a>presto-install.sh</strong> script is <strong id="b3167122842316"><a name="b3167122842316"></a><a name="b3167122842316"></a>worker</strong>. Based on the Presto usage habit, you are advised to install <strong id="b1855303911230"><a name="b1855303911230"></a><a name="b1855303911230"></a>dualroles</strong> on the active Master nodes and <strong id="b13555539132315"><a name="b13555539132315"></a><a name="b13555539132315"></a>worker</strong> on the Core nodes.</li><li>Local VM path: Enter a script path. The script path must start with a slash (/) and end with <strong id="b1165514161242"><a name="b1165514161242"></a><a name="b1165514161242"></a>.sh</strong>.</li></ul>
</td>
</tr>
<tr id="row11585122835019"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p32231936175317"><a name="p32231936175317"></a><a name="p32231936175317"></a>parameters</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p322373685317"><a name="p322373685317"></a><a name="p322373685317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p28581637172215"><a name="p28581637172215"></a><a name="p28581637172215"></a>Bootstrap action script parameters</p>
</td>
</tr>
<tr id="row2058516287502"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1922313367533"><a name="p1922313367533"></a><a name="p1922313367533"></a>nodes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1822313612539"><a name="p1822313612539"></a><a name="p1822313612539"></a>Array String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p12585928145012"><a name="p12585928145012"></a><a name="p12585928145012"></a>Type of a node where the bootstrap action script is executed. The value can be Master, Core, or Task.</p>
</td>
</tr>
<tr id="row4757171219539"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p19223203615313"><a name="p19223203615313"></a><a name="p19223203615313"></a>active_master</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p152231536145317"><a name="p152231536145317"></a><a name="p152231536145317"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p207581812185316"><a name="p207581812185316"></a><a name="p207581812185316"></a>Whether the bootstrap action script runs only on active Master nodes.</p>
<p id="p1919931141119"><a name="p1919931141119"></a><a name="p1919931141119"></a>The default value is <strong id="b18180193218241"><a name="b18180193218241"></a><a name="b18180193218241"></a>false</strong>, indicating that the bootstrap action script can run on all Master nodes.</p>
</td>
</tr>
<tr id="row12296121585317"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1622473605319"><a name="p1622473605319"></a><a name="p1622473605319"></a>before_component_start</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p12224173635317"><a name="p12224173635317"></a><a name="p12224173635317"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p11296615135311"><a name="p11296615135311"></a><a name="p11296615135311"></a>Time when the bootstrap action script is executed. Currently, the following two options are available: <strong id="b183212038112413"><a name="b183212038112413"></a><a name="b183212038112413"></a>Before component start</strong> and <strong id="b3322138162415"><a name="b3322138162415"></a><a name="b3322138162415"></a>After component start</strong></p>
<p id="p172869585132"><a name="p172869585132"></a><a name="p172869585132"></a>The default value is <strong id="b1355134014246"><a name="b1355134014246"></a><a name="b1355134014246"></a>false</strong>, indicating that the bootstrap action script is executed after the component is started.</p>
</td>
</tr>
<tr id="row1193251913537"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p132241936165315"><a name="p132241936165315"></a><a name="p132241936165315"></a>fail_action</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p3224113655314"><a name="p3224113655314"></a><a name="p3224113655314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4700154617299"><a name="p4700154617299"></a><a name="p4700154617299"></a>Whether to continue executing subsequent scripts and creating a cluster after the bootstrap action script fails to be executed.</p>
<a name="ul18391113413191"></a><a name="ul18391113413191"></a><ul id="ul18391113413191"><li><strong id="b1543720171819"><a name="b1543720171819"></a><a name="b1543720171819"></a>continue</strong>: Continue to execute subsequent scripts.</li><li><strong id="b13979629181"><a name="b13979629181"></a><a name="b13979629181"></a>errorout</strong>: Stop the action.</li></ul>
<div class="p" id="p1190163315446"><a name="p1190163315446"></a><a name="p1190163315446"></a>The default value is <strong id="b458704811244"><a name="b458704811244"></a><a name="b458704811244"></a>errorout</strong>, indicating that the action is stopped.<div class="note" id="note796819345579"><a name="note796819345579"></a><a name="note796819345579"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p6994625143710"><a name="p6994625143710"></a><a name="p6994625143710"></a>You are advised to set this parameter to <strong id="b3691195952413"><a name="b3691195952413"></a><a name="b3691195952413"></a>continue</strong> in the commissioning phase so that the cluster can continue to be installed and started no matter whether the bootstrap action is successful.</p>
</div></div>
</div>
</td>
</tr>
<tr id="row1721772714517"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p17217202764511"><a name="p17217202764511"></a><a name="p17217202764511"></a>start_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p32181327144511"><a name="p32181327144511"></a><a name="p32181327144511"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p021852712452"><a name="p021852712452"></a><a name="p021852712452"></a>Execution time of one boot operation script.</p>
</td>
</tr>
<tr id="row7534624194520"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p85351124154513"><a name="p85351124154513"></a><a name="p85351124154513"></a>state</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p545746588"><a name="p545746588"></a><a name="p545746588"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p8535122494514"><a name="p8535122494514"></a><a name="p8535122494514"></a>Running state of one bootstrap action script</p>
<a name="ul5571711145820"></a><a name="ul5571711145820"></a><ul id="ul5571711145820"><li><strong id="b81041118191814"><a name="b81041118191814"></a><a name="b81041118191814"></a>PENDING</strong></li><li><strong id="b9479142318189"><a name="b9479142318189"></a><a name="b9479142318189"></a>IN_PROGRESS</strong></li><li><strong id="b1791811279187"><a name="b1791811279187"></a><a name="b1791811279187"></a>SUCCESS</strong></li><li><strong id="b1125113212188"><a name="b1125113212188"></a><a name="b1125113212188"></a>FAILURE</strong></li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section88101461162"></a>

-   Example request

    None.

-   Example response

    ```
    {
        "cluster":{
            "clusterId":"bdb064ff-2855-4624-90d5-e9a6376abd6e",
            "clusterName":"c17022001",
            "masterNodeNum":"2",
            "coreNodeNum":"3",
            "clusterState":"scaling-in",
            "stageDesc": null,
            "createAt":"1487570757",
            "updateAt":"1487668974",
            "billingType":"Metered",
            "dataCenter":"eu-de",
            "vpc": "vpc-autotest",        
            "vpcId": "e2978efd-ca12-4058-9332-1ca0bfbab592",        
            "duration":"0",
            "fee":"0",
            "hadoopVersion":"",
            "masterNodeSize":"s1.8xlarge.linux.mrs",
            "coreNodeSize":"c2.2xlarge.linux.mrs",
            "componentList":[
                {
                    "componentId":"MRS 2.1.0_001",
                    "componentName":"Hadoop",
                    "componentVersion": "3.1.1",
                    "componentDesc":"A framework that allows for the distributed processing of large data sets across clusters."
                },
                {
                    "componentId":"MRS 2.1.0_002",
                    "componentName":"Spark",
                    "componentVersion": "2.3.2",
                    "componentDesc":"A fast and general engine for large-scale data processing."
                },
                {
                    "componentId":"MRS 2.1.0_004",
                    "componentName":"Hive",
                    "componentVersion":"3.1.0",
                    "componentDesc":"A data warehouse infrastructure that provides data summarization and ad hoc querying."
                },
                {
                    "componentId":"MRS 2.1.0_003",
                    "componentName":"HBase",
                    "componentVersion":"2.1.1",
                    "componentDesc":"A scalable, distributed database that supports structured data storage for large tables."
                }
    ,
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
            "externalIp":"100.XXX.XXX.XXX",
            "externalAlternateIp":"100.XXX.XXX.XXX",
            "internalIp":"192.XXX.XXX.XXX",
            "deploymentId":"4ac46ca7-a488-4b91-82c2-e4d7aa9c40c2",
            "remark":"",
            "orderId":"null",
            "azId":"null",
            "masterNodeProductId":"b35cf2d2348a445ca74b32289a160882",
            "masterNodeSpecId":"8ab05e503b4c42abb304e2489560063b",
            "coreNodeProductId":"dc970349d128460e960a0c2b826c427c",
            "coreNodeSpecId":"cdc6035a249a40249312f5ef72a23cd7",
            "azName":"eu-de-01",
            "instanceId":"4ac46ca7-a488-4b91-82c2-e4d7aa9c40c2",
            "vnc":null,
            "tenantId":"3f99e3319a8943ceb15c584f3325d064",
            "volumeSize":100,
            "volumeType":"SATA",
            "subnetId": "6b96eec3-4f8d-4c83-93e2-6ec625001d7c",
            "subnetName":"subnet-ftest",
            "securityGroupsId":"930e34e2-195d-401f-af07-0b64ea6603f8",
            "slaveSecurityGroupsId":"2ef3343e-3477-4a0d-80fe-4d874e4f81b8",
            "bootstrapScripts": [
             {
    	"name": "test1-success",
    	"uri": "s3a://bootscript/script/simple/basic_success.sh",
    	"parameters": "",
    	"nodes": ["master", "core"],
    	"active_master": true,
    	"fail_action": "errorout",
    	"before_component_start": true,
    	"state": "SUCCESS",
    	"start_time": 1527681083
              }
                ],
            "stageDesc": "Installing MRS Manager",
            "mrsManagerFinish": false, 
            "safeMode":1,
            "clusterVersion":"MRS 2.1.0",
            "nodePublicCertName":"myp",
            "masterNodeIp":"192.XXX.XXX.XXX",
            "privateIpFirst":"192.XXX.XXX.XXX",
            "errorInfo":null,
            "tags":"k1=v1,k2=v2,k3=v3",
            "clusterType": 0,
            "logCollection": 1,
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
                     "dataVolumeResourceType": ""
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
                     "dataVolumeResourceType": ""
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
                     "dataVolumeResourceType": ""
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
                   "AutoScalingPolicy": null
                   }
                ],
             "masterDataVolumeType": "SATA",
             "masterDataVolumeSize": 200,
             "masterDataVolumeCount": 1,
             "coreDataVolumeType": "SATA",
             "coreDataVolumeSize": 100,
             "coreDataVolumeCount": 1,
          }
      }
    ```


## Status Code<a name="s430f1e763f4141caad0f2317ab21b17a"></a>

[Table 6](#te1408c9f77054f128c7aa7ade589dc24)  describes the status code of this API.

**Table  6**  Status code

<a name="te1408c9f77054f128c7aa7ade589dc24"></a>
<table><thead align="left"><tr id="r2a5859ed39a74bd4ae3156fdfc840527"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="a75c8eefea05f4c2b9564cd558bc9abf2"><a name="a75c8eefea05f4c2b9564cd558bc9abf2"></a><a name="a75c8eefea05f4c2b9564cd558bc9abf2"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="ac95e194beee64d8fa440bf9d7ebd4524"><a name="ac95e194beee64d8fa440bf9d7ebd4524"></a><a name="ac95e194beee64d8fa440bf9d7ebd4524"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r10bd7e45b8f14e18b317cc52b61e5c78"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="a6793fcfaa1994df6a0ecc85acb284462"><a name="a6793fcfaa1994df6a0ecc85acb284462"></a><a name="a6793fcfaa1994df6a0ecc85acb284462"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="a8987a51998ac40519a175e9e5e7a2182"><a name="a8987a51998ac40519a175e9e5e7a2182"></a><a name="a8987a51998ac40519a175e9e5e7a2182"></a>Cluster details have been queried successfully.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

