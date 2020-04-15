# Supported Resources<a name="EN-US_TOPIC_0076468642"></a>

RTS supports 44 types of resources, including compute, storage, and network resources.  [Table 1](#table421015631013)  describes resource types supported by RTS. You can also log in to the RTS management console and view those resource types on the  **Resource Types**  page.

For details about resource types, see  [Resource Type Reference](resource-type-reference.md).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>OSE is the abbreviation of OpenStack Extension. In  [Table 1](#table421015631013),  **OSE**  indicates an extended resource type except for default resource types of OpenStack Heat, or a user-defined resource type.  

**Table  1**  Resource types supported by RTS

<a name="table421015631013"></a>
<table><thead align="left"><tr id="row921185681013"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.6.1.1"><p id="p058132791111"><a name="p058132791111"></a><a name="p058132791111"></a>Resource Type</p>
</th>
<th class="cellrowborder" valign="top" width="22%" id="mcps1.2.6.1.2"><p id="p13588102751110"><a name="p13588102751110"></a><a name="p13588102751110"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.6.1.3"><p id="p195948272116"><a name="p195948272116"></a><a name="p195948272116"></a>Supported by RTS</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.6.1.4"><p id="p196011127101110"><a name="p196011127101110"></a><a name="p196011127101110"></a>Supported by Heat</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.5"><p id="p1860852781115"><a name="p1860852781115"></a><a name="p1860852781115"></a>Dependent Service</p>
</th>
</tr>
</thead>
<tbody><tr id="row921225618103"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p16221827151117"><a name="p16221827151117"></a><a name="p16221827151117"></a><a href="os-cinder-volume.md">OS::Cinder::Volume</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p17629527151112"><a name="p17629527151112"></a><a name="p17629527151112"></a>Resource for providing Cinder volumes</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p156352273118"><a name="p156352273118"></a><a name="p156352273118"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p15642192721118"><a name="p15642192721118"></a><a name="p15642192721118"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p264872718114"><a name="p264872718114"></a><a name="p264872718114"></a>EVS</p>
</td>
</tr>
<tr id="row1521295620102"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p17657027121120"><a name="p17657027121120"></a><a name="p17657027121120"></a><a href="os-cinder-volumeattachment.md">OS::Cinder::VolumeAttachment</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p1066882741115"><a name="p1066882741115"></a><a name="p1066882741115"></a>Resoure for associating volumes with instances</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p1679152714113"><a name="p1679152714113"></a><a name="p1679152714113"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p5685327201118"><a name="p5685327201118"></a><a name="p5685327201118"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p136921327141115"><a name="p136921327141115"></a><a name="p136921327141115"></a>EVS</p>
</td>
</tr>
<tr id="row8212105615102"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p117011274112"><a name="p117011274112"></a><a name="p117011274112"></a><a href="os-heat-autoscalinggroup.md">OS::Heat::AutoScalingGroup</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p4709162713118"><a name="p4709162713118"></a><a name="p4709162713118"></a>Auto Scaling (AS) group that can scale any resources</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p12715112731112"><a name="p12715112731112"></a><a name="p12715112731112"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p16724122711117"><a name="p16724122711117"></a><a name="p16724122711117"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p1672922721116"><a name="p1672922721116"></a><a name="p1672922721116"></a>RTS</p>
</td>
</tr>
<tr id="row1721313566101"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p8740142713110"><a name="p8740142713110"></a><a name="p8740142713110"></a><a href="os-heat-cloudconfig.md">OS::Heat::CloudConfig</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p97485275111"><a name="p97485275111"></a><a name="p97485275111"></a>Configuration resource for representing <strong id="b3106190134711"><a name="b3106190134711"></a><a name="b3106190134711"></a>cloud-init cloud-config</strong></p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p97587271115"><a name="p97587271115"></a><a name="p97587271115"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p4765327161112"><a name="p4765327161112"></a><a name="p4765327161112"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p13771162720116"><a name="p13771162720116"></a><a name="p13771162720116"></a>RTS</p>
</td>
</tr>
<tr id="row1921319562102"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p4784627181116"><a name="p4784627181116"></a><a name="p4784627181116"></a><a href="os-heat-multipartmime.md">OS::Heat::MultipartMime</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p9943122364218"><a name="p9943122364218"></a><a name="p9943122364218"></a>Resource that assembles a collection of software configurations as a multi-part mime</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p1379892715115"><a name="p1379892715115"></a><a name="p1379892715115"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p1380711273119"><a name="p1380711273119"></a><a name="p1380711273119"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p1481412718111"><a name="p1481412718111"></a><a name="p1481412718111"></a>RTS</p>
</td>
</tr>
<tr id="row8213556101010"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p18825162717118"><a name="p18825162717118"></a><a name="p18825162717118"></a><a href="os-heat-randomstring.md">OS::Heat::RandomString</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p883192720111"><a name="p883192720111"></a><a name="p883192720111"></a>Resource for generating a random string</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p1283910272117"><a name="p1283910272117"></a><a name="p1283910272117"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p884482715112"><a name="p884482715112"></a><a name="p884482715112"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p585172716114"><a name="p585172716114"></a><a name="p585172716114"></a>RTS</p>
</td>
</tr>
<tr id="row172131656171011"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p188612027151110"><a name="p188612027151110"></a><a name="p188612027151110"></a><a href="os-heat-resourcegroup.md">OS::Heat::ResourceGroup</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p178687275115"><a name="p178687275115"></a><a name="p178687275115"></a>Creating one or more identically configured nested resources</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p98748278115"><a name="p98748278115"></a><a name="p98748278115"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p14883162713115"><a name="p14883162713115"></a><a name="p14883162713115"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p58891027121118"><a name="p58891027121118"></a><a name="p58891027121118"></a>RTS</p>
</td>
</tr>
<tr id="row1221365631011"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p20898132791113"><a name="p20898132791113"></a><a name="p20898132791113"></a><a href="os-heat-scalingpolicy.md">OS::Heat::ScalingPolicy</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p290410271118"><a name="p290410271118"></a><a name="p290410271118"></a>Resource for creating OS::Heat::AutoScalingGroup</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p791112741116"><a name="p791112741116"></a><a name="p791112741116"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p10917327191111"><a name="p10917327191111"></a><a name="p10917327191111"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p14924102781115"><a name="p14924102781115"></a><a name="p14924102781115"></a>RTS</p>
</td>
</tr>
<tr id="row9214456111015"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p13822410101211"><a name="p13822410101211"></a><a name="p13822410101211"></a><a href="os-heat-softwarecomponent.md">OS::Heat::SoftwareComponent</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p10830010181216"><a name="p10830010181216"></a><a name="p10830010181216"></a>Resource for describing and storing a software component</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p18840161020120"><a name="p18840161020120"></a><a name="p18840161020120"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p48473104121"><a name="p48473104121"></a><a name="p48473104121"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p48541310111220"><a name="p48541310111220"></a><a name="p48541310111220"></a>RTS</p>
</td>
</tr>
<tr id="row821415610102"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p1786441051211"><a name="p1786441051211"></a><a name="p1786441051211"></a><a href="os-heat-softwareconfig.md">OS::Heat::SoftwareConfig</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p9871510121214"><a name="p9871510121214"></a><a name="p9871510121214"></a>Resource for describing and storing a software configuration</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p3878111021214"><a name="p3878111021214"></a><a name="p3878111021214"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p9885110181219"><a name="p9885110181219"></a><a name="p9885110181219"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p1889112105123"><a name="p1889112105123"></a><a name="p1889112105123"></a>RTS</p>
</td>
</tr>
<tr id="row158251939121419"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p798813387565"><a name="p798813387565"></a><a name="p798813387565"></a><a href="os-heat-softwaredeployment.md">OS::Heat::SoftwareDeployment</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p189889386565"><a name="p189889386565"></a><a name="p189889386565"></a>Resource for describing and storing a software deployment</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p18988338155616"><a name="p18988338155616"></a><a name="p18988338155616"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p1998863820568"><a name="p1998863820568"></a><a name="p1998863820568"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p1598813865619"><a name="p1598813865619"></a><a name="p1598813865619"></a>RTS</p>
</td>
</tr>
<tr id="row16214195691013"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p28996104123"><a name="p28996104123"></a><a name="p28996104123"></a><a href="os-heat-structuredconfig.md">OS::Heat::StructuredConfig</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p1890512108128"><a name="p1890512108128"></a><a name="p1890512108128"></a>Resource that has the same logic with OS::Heat::SoftwareConfig</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p1791301031215"><a name="p1791301031215"></a><a name="p1791301031215"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p20919910121211"><a name="p20919910121211"></a><a name="p20919910121211"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p119256102123"><a name="p119256102123"></a><a name="p119256102123"></a>RTS</p>
</td>
</tr>
<tr id="row7214105621017"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p11936131041219"><a name="p11936131041219"></a><a name="p11936131041219"></a><a href="os-heat-waitcondition.md">OS::Heat::WaitCondition</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p2943111016129"><a name="p2943111016129"></a><a name="p2943111016129"></a>Resource for handling signals received by WaitConditionHandle</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p149511910181219"><a name="p149511910181219"></a><a name="p149511910181219"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p169591510131211"><a name="p169591510131211"></a><a name="p169591510131211"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p1196715104124"><a name="p1196715104124"></a><a name="p1196715104124"></a>RTS</p>
</td>
</tr>
<tr id="row421515566104"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p149776100124"><a name="p149776100124"></a><a name="p149776100124"></a><a href="os-heat-waitconditionhandle.md">OS::Heat::WaitConditionHandle</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p1798351020125"><a name="p1798351020125"></a><a name="p1798351020125"></a>Resource for creating instance signals</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p399031041214"><a name="p399031041214"></a><a name="p399031041214"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p99961610151217"><a name="p99961610151217"></a><a name="p99961610151217"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p22171141216"><a name="p22171141216"></a><a name="p22171141216"></a>RTS</p>
</td>
</tr>
<tr id="row82151456181019"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p1813141110126"><a name="p1813141110126"></a><a name="p1813141110126"></a><a href="os-neutron-floatingip.md">OS::Neutron::FloatingIP</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p19241111141215"><a name="p19241111141215"></a><a name="p19241111141215"></a>Resource for creating a floating IP address for Neutron</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p183201113125"><a name="p183201113125"></a><a name="p183201113125"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p23816111125"><a name="p23816111125"></a><a name="p23816111125"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p44661118124"><a name="p44661118124"></a><a name="p44661118124"></a>VPC</p>
</td>
</tr>
<tr id="row721515601020"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p1358811131215"><a name="p1358811131215"></a><a name="p1358811131215"></a><a href="os-neutron-floatingipassociation.md">OS::Neutron::FloatingIPAssociation</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p5621111151212"><a name="p5621111151212"></a><a name="p5621111151212"></a>Resource for associating floating IP addresses and ports</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p26861112124"><a name="p26861112124"></a><a name="p26861112124"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p575151116126"><a name="p575151116126"></a><a name="p575151116126"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p5831211161215"><a name="p5831211161215"></a><a name="p5831211161215"></a>VPC</p>
</td>
</tr>
<tr id="row4215856151010"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p19221182216143"><a name="p19221182216143"></a><a name="p19221182216143"></a><a href="os-neutron-net.md">OS::Neutron::Net</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p182283227148"><a name="p182283227148"></a><a name="p182283227148"></a>Resource for creating Neutron networks</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p323782218149"><a name="p323782218149"></a><a name="p323782218149"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p1724419227148"><a name="p1724419227148"></a><a name="p1724419227148"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p17252922171417"><a name="p17252922171417"></a><a name="p17252922171417"></a>VPC</p>
</td>
</tr>
<tr id="row821545661016"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p1126213221142"><a name="p1126213221142"></a><a name="p1126213221142"></a><a href="os-neutron-port.md">OS::Neutron::Port</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p13269182217147"><a name="p13269182217147"></a><a name="p13269182217147"></a>Resource for creating Neutron network ports</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p227914228142"><a name="p227914228142"></a><a name="p227914228142"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p32855228149"><a name="p32855228149"></a><a name="p32855228149"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p629192281417"><a name="p629192281417"></a><a name="p629192281417"></a>VPC</p>
</td>
</tr>
<tr id="row82159564105"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p0302422141411"><a name="p0302422141411"></a><a name="p0302422141411"></a><a href="os-neutron-router.md">OS::Neutron::Router</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p1331019229148"><a name="p1331019229148"></a><a name="p1331019229148"></a>Resource for implementing Neutron routers</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p331952211144"><a name="p331952211144"></a><a name="p331952211144"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p14327152219147"><a name="p14327152219147"></a><a name="p14327152219147"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p43361022131418"><a name="p43361022131418"></a><a name="p43361022131418"></a>VPC</p>
</td>
</tr>
<tr id="row1221513566106"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p7386202291410"><a name="p7386202291410"></a><a name="p7386202291410"></a><a href="os-neutron-routerinterface.md">OS::Neutron::RouterInterface</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p839362216149"><a name="p839362216149"></a><a name="p839362216149"></a>Resource for creating Neutron router interfaces</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p20399122241417"><a name="p20399122241417"></a><a name="p20399122241417"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p1407722181410"><a name="p1407722181410"></a><a name="p1407722181410"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p1241392251410"><a name="p1241392251410"></a><a name="p1241392251410"></a>VPC</p>
</td>
</tr>
<tr id="row32151568103"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p1342611225143"><a name="p1342611225143"></a><a name="p1342611225143"></a><a href="os-neutron-securitygroup.md">OS::Neutron::SecurityGroup</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p5434192220141"><a name="p5434192220141"></a><a name="p5434192220141"></a>Resource for creating Neutron security groups</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p14421822171414"><a name="p14421822171414"></a><a name="p14421822171414"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p644872261412"><a name="p644872261412"></a><a name="p644872261412"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p545511223146"><a name="p545511223146"></a><a name="p545511223146"></a>VPC</p>
</td>
</tr>
<tr id="row1521611565109"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p144697228148"><a name="p144697228148"></a><a name="p144697228148"></a><a href="os-neutron-subnet.md">OS::Neutron::Subnet</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p94761622121413"><a name="p94761622121413"></a><a name="p94761622121413"></a>Resource for creating Neutron subnets</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p34831422141411"><a name="p34831422141411"></a><a name="p34831422141411"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p15489192215149"><a name="p15489192215149"></a><a name="p15489192215149"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p44961522161411"><a name="p44961522161411"></a><a name="p44961522161411"></a>VPC</p>
</td>
</tr>
<tr id="row1321618562107"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p551172201420"><a name="p551172201420"></a><a name="p551172201420"></a><a href="os-nova-keypair.md">OS::Nova::KeyPair</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p1952062215145"><a name="p1952062215145"></a><a name="p1952062215145"></a>Resource for creating Nova key pairs</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p9527152271418"><a name="p9527152271418"></a><a name="p9527152271418"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p5534192219145"><a name="p5534192219145"></a><a name="p5534192219145"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p054218223146"><a name="p054218223146"></a><a name="p054218223146"></a>ECS</p>
</td>
</tr>
<tr id="row17216456121018"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p1552102218147"><a name="p1552102218147"></a><a name="p1552102218147"></a><a href="os-nova-server.md">OS::Nova::Server</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p1156142201411"><a name="p1156142201411"></a><a name="p1156142201411"></a>Resource for creating Nova instances</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p1656952218147"><a name="p1656952218147"></a><a name="p1656952218147"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p15575522161418"><a name="p15575522161418"></a><a name="p15575522161418"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p1958592221418"><a name="p1958592221418"></a><a name="p1958592221418"></a>ECS</p>
</td>
</tr>
<tr id="row15216175616106"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p12596122111414"><a name="p12596122111414"></a><a name="p12596122111414"></a><a href="os-nova-servergroup.md">OS::Nova::ServerGroup</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p96031922131412"><a name="p96031922131412"></a><a name="p96031922131412"></a>Resource for creating a Nova server group</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p9612152231412"><a name="p9612152231412"></a><a name="p9612152231412"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p13619722201415"><a name="p13619722201415"></a><a name="p13619722201415"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p462642219149"><a name="p462642219149"></a><a name="p462642219149"></a>ECS</p>
</td>
</tr>
<tr id="row16216205612108"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p563882231415"><a name="p563882231415"></a><a name="p563882231415"></a><a href="ose-as-scalingconfig.md">OSE::AS::ScalingConfig</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p464418227145"><a name="p464418227145"></a><a name="p464418227145"></a>Resource for creating an AS configuration</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p16501422101412"><a name="p16501422101412"></a><a name="p16501422101412"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p14658142220147"><a name="p14658142220147"></a><a name="p14658142220147"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p1866511227146"><a name="p1866511227146"></a><a name="p1866511227146"></a>AS</p>
</td>
</tr>
<tr id="row4216165651014"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p136766226140"><a name="p136766226140"></a><a name="p136766226140"></a><a href="ose-as-scalinggroup.md">OSE::AS::ScalingGroup</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p868422261417"><a name="p868422261417"></a><a name="p868422261417"></a>Resource for creating an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p1569032217143"><a name="p1569032217143"></a><a name="p1569032217143"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p8696102217148"><a name="p8696102217148"></a><a name="p8696102217148"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p10704192291413"><a name="p10704192291413"></a><a name="p10704192291413"></a>AS</p>
</td>
</tr>
<tr id="row221605641017"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p8715172220148"><a name="p8715172220148"></a><a name="p8715172220148"></a><a href="ose-as-scalingpolicy.md">OSE::AS::ScalingPolicy</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p872232210144"><a name="p872232210144"></a><a name="p872232210144"></a>Resource for creating an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p1073122271419"><a name="p1073122271419"></a><a name="p1073122271419"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p20737132291410"><a name="p20737132291410"></a><a name="p20737132291410"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p13744122216149"><a name="p13744122216149"></a><a name="p13744122216149"></a>AS</p>
</td>
</tr>
<tr id="row16218956111015"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p8754142215146"><a name="p8754142215146"></a><a name="p8754142215146"></a><a href="ose-ces-alarm.md">OSE::CES::Alarm</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p18761422151411"><a name="p18761422151411"></a><a name="p18761422151411"></a>Resource for creating a Cloud Eye alarm</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p47694222141"><a name="p47694222141"></a><a name="p47694222141"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p97751122181414"><a name="p97751122181414"></a><a name="p97751122181414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p1278214227147"><a name="p1278214227147"></a><a name="p1278214227147"></a>Cloud Eye</p>
</td>
</tr>
<tr id="row139022522210"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p158180577211"><a name="p158180577211"></a><a name="p158180577211"></a><a href="ose-elb-loadbalancer.md">OSE::ELB::LoadBalancer</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p1282120572218"><a name="p1282120572218"></a><a name="p1282120572218"></a>Resource for creating load balancers</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p28265571217"><a name="p28265571217"></a><a name="p28265571217"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p198283571727"><a name="p198283571727"></a><a name="p198283571727"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p08301657529"><a name="p08301657529"></a><a name="p08301657529"></a>ELB</p>
</td>
</tr>
<tr id="row22060341312"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p127581203419"><a name="p127581203419"></a><a name="p127581203419"></a><a href="ose-elb-listener.md">OSE::ELB::Listener</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p37644019414"><a name="p37644019414"></a><a name="p37644019414"></a>Resource for creating classic load balancer listeners</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p77661001341"><a name="p77661001341"></a><a name="p77661001341"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p137691401044"><a name="p137691401044"></a><a name="p137691401044"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p37721902049"><a name="p37721902049"></a><a name="p37721902049"></a>ELB</p>
</td>
</tr>
<tr id="row197934411131"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p1573869941"><a name="p1573869941"></a><a name="p1573869941"></a><a href="ose-elb-healthcheck.md">OSE::ELB::HealthCheck</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p1674611916415"><a name="p1674611916415"></a><a name="p1674611916415"></a>Resource for creating health checks for classic load balancers</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p6748129947"><a name="p6748129947"></a><a name="p6748129947"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p7751191448"><a name="p7751191448"></a><a name="p7751191448"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p275316917418"><a name="p275316917418"></a><a name="p275316917418"></a>ELB</p>
</td>
</tr>
<tr id="row189914497318"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p106893171441"><a name="p106893171441"></a><a name="p106893171441"></a><a href="ose-elb-member.md">OSE::ELB::Member</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p36931174412"><a name="p36931174412"></a><a name="p36931174412"></a>Resource for creating backend servers for classic load balancers</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p069510178420"><a name="p069510178420"></a><a name="p069510178420"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p2696017842"><a name="p2696017842"></a><a name="p2696017842"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p186991171347"><a name="p186991171347"></a><a name="p186991171347"></a>ELB</p>
</td>
</tr>
<tr id="row1576681081311"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p1279132291418"><a name="p1279132291418"></a><a name="p1279132291418"></a><a href="ose-elb-certificate.md">OSE::ELB::Certificate</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p1580013222148"><a name="p1580013222148"></a><a name="p1580013222148"></a>Resource for creating certificates for classic load balancers</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p1280732211417"><a name="p1280732211417"></a><a name="p1280732211417"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p11813102210147"><a name="p11813102210147"></a><a name="p11813102210147"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p182012227144"><a name="p182012227144"></a><a name="p182012227144"></a>ELB</p>
</td>
</tr>
<tr id="row1876871013130"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p1380515528411"><a name="p1380515528411"></a><a name="p1380515528411"></a><a href="os-neutron-lbaas-healthmonitor.md">OS::Neutron::LBaaS::HealthMonitor</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p28056521243"><a name="p28056521243"></a><a name="p28056521243"></a>Resource for handling enhanced load balancer listeners</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p12805125218418"><a name="p12805125218418"></a><a name="p12805125218418"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p78044527412"><a name="p78044527412"></a><a name="p78044527412"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p480416525416"><a name="p480416525416"></a><a name="p480416525416"></a>ELB</p>
</td>
</tr>
<tr id="row276961010136"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p1380314529416"><a name="p1380314529416"></a><a name="p1380314529416"></a><a href="os-neutron-lbaas-listener.md">OS::Neutron::LBaaS::Listener</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p128039521846"><a name="p128039521846"></a><a name="p128039521846"></a>Resource for creating enhanced load balancer listeners</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p980319521942"><a name="p980319521942"></a><a name="p980319521942"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p1980217525413"><a name="p1980217525413"></a><a name="p1980217525413"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p0802165210416"><a name="p0802165210416"></a><a name="p0802165210416"></a>ELB</p>
</td>
</tr>
<tr id="row6769141091316"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p6801165211412"><a name="p6801165211412"></a><a name="p6801165211412"></a><a href="os-neutron-lbaas-loadbalancer.md">OS::Neutron::LBaaS::LoadBalancer</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p1780013521349"><a name="p1780013521349"></a><a name="p1780013521349"></a>Resource for creating enhanced load balancers</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p188000521047"><a name="p188000521047"></a><a name="p188000521047"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p187991552849"><a name="p187991552849"></a><a name="p187991552849"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p4798052440"><a name="p4798052440"></a><a name="p4798052440"></a>ELB</p>
</td>
</tr>
<tr id="row207691110151317"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p14798115217414"><a name="p14798115217414"></a><a name="p14798115217414"></a><a href="os-neutron-lbaas-pool.md">OS::Neutron::LBaaS::Pool</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p2798352341"><a name="p2798352341"></a><a name="p2798352341"></a>Resource for creating backend server groups for enhanced load balancers</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p19797252346"><a name="p19797252346"></a><a name="p19797252346"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p187975521145"><a name="p187975521145"></a><a name="p187975521145"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p1279575210418"><a name="p1279575210418"></a><a name="p1279575210418"></a>ELB</p>
</td>
</tr>
<tr id="row15894802615"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p2894001165"><a name="p2894001165"></a><a name="p2894001165"></a><a href="os-neutron-lbaas-poolmember.md">OS::Neutron::LBaaS::PoolMember</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p18894309612"><a name="p18894309612"></a><a name="p18894309612"></a>Resource for creating backend servers for enhanced load balancers</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p1689414013618"><a name="p1689414013618"></a><a name="p1689414013618"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p18895110869"><a name="p18895110869"></a><a name="p18895110869"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p138951101760"><a name="p138951101760"></a><a name="p138951101760"></a>ELB</p>
</td>
</tr>
<tr id="row1729311105916"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p2067219221808"><a name="p2067219221808"></a><a name="p2067219221808"></a><a href="ose-rds-instance.md">OSE::RDS::Instance</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p11672192214014"><a name="p11672192214014"></a><a name="p11672192214014"></a>Resource for creating an RDS DB instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p15672162212017"><a name="p15672162212017"></a><a name="p15672162212017"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p1067215225018"><a name="p1067215225018"></a><a name="p1067215225018"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p1672522601"><a name="p1672522601"></a><a name="p1672522601"></a>RDS</p>
</td>
</tr>
<tr id="row3294191113599"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p1267219221908"><a name="p1267219221908"></a><a name="p1267219221908"></a><a href="ose-vpc-vpc.md">OSE::VPC::Vpc</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p176727221204"><a name="p176727221204"></a><a name="p176727221204"></a>Resource for creating a VPC</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p7672722002"><a name="p7672722002"></a><a name="p7672722002"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p126727229019"><a name="p126727229019"></a><a name="p126727229019"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p206725228018"><a name="p206725228018"></a><a name="p206725228018"></a>VPC</p>
</td>
</tr>
<tr id="row103093179596"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p1867262213011"><a name="p1867262213011"></a><a name="p1867262213011"></a><a href="ose-vpc-subnet.md">OSE::VPC::Subnet</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p11672822102"><a name="p11672822102"></a><a name="p11672822102"></a>Resource for creating a VPC subnet</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p567216223014"><a name="p567216223014"></a><a name="p567216223014"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p176729222000"><a name="p176729222000"></a><a name="p176729222000"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p196722221501"><a name="p196722221501"></a><a name="p196722221501"></a>VPC</p>
</td>
</tr>
<tr id="row9311201755919"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p67731282014"><a name="p67731282014"></a><a name="p67731282014"></a><a href="ose-sfs-share.md">OSE::SFS::Share</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p877314281601"><a name="p877314281601"></a><a name="p877314281601"></a>Resource for creating a file share</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p1577342817019"><a name="p1577342817019"></a><a name="p1577342817019"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p13773162819010"><a name="p13773162819010"></a><a name="p13773162819010"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p5773112812012"><a name="p5773112812012"></a><a name="p5773112812012"></a>SFS</p>
</td>
</tr>
<tr id="row361142318592"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.1 "><p id="p20773528103"><a name="p20773528103"></a><a name="p20773528103"></a><a href="ose-sfs-shareaccessrule.md">OSE::SFS::ShareAccessRule</a></p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p4773112820018"><a name="p4773112820018"></a><a name="p4773112820018"></a>Resource for creating rules for accessing file shares</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.6.1.3 "><p id="p5773028407"><a name="p5773028407"></a><a name="p5773028407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.4 "><p id="p1677319281706"><a name="p1677319281706"></a><a name="p1677319281706"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p167731128604"><a name="p167731128604"></a><a name="p167731128604"></a>SFS</p>
</td>
</tr>
</tbody>
</table>

