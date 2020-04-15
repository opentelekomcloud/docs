# Data Structure for Creating ECSs<a name="EN-US_TOPIC_0167957246"></a>

## Contents<a name="section1235152713529"></a>

-   [publicip Field Description](#section1846944811410)
-   [security\_groups Field Description](#section332191084315)
-   [eip Field Description](#section1840318312449)
-   [bandwidth Field Description](#section172789339448)
-   [extendparam Field Description for Creating Disks](#section1361484104817)
-   [extendparam Field Description for Creating ECSs](#section1373711413505)
-   [metadata Field Description for Creating Disks](#section1228814491353)
-   [metadata Field Description for Creating ECSs](#section1574435185018)
-   [os:scheduler\_hints Field Description](#section16585034175117)
-   [binding:profile Field Description](#section681114217434)
-   [extra\_dhcp\_opts Field Description](#section12781010134512)

## **publicip**  Field Description<a name="section1846944811410"></a>

This field is used by the following APIs:

-   Creating ECSs: /v1/\{project\_id\}/cloudservers

**Table  1** **publicip**  field description

<a name="table2785183710710"></a>
<table><thead align="left"><tr id="en-us_topic_0020212668_row7093323"><th class="cellrowborder" valign="top" width="18.42%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020212668_p655704815421"><a name="en-us_topic_0020212668_p655704815421"></a><a name="en-us_topic_0020212668_p655704815421"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.54%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020212668_p165571448114214"><a name="en-us_topic_0020212668_p165571448114214"></a><a name="en-us_topic_0020212668_p165571448114214"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.48%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020212668_p45727487425"><a name="en-us_topic_0020212668_p45727487425"></a><a name="en-us_topic_0020212668_p45727487425"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.56%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020212668_p13572124817427"><a name="en-us_topic_0020212668_p13572124817427"></a><a name="en-us_topic_0020212668_p13572124817427"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020212668_row38559395"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p21035367101953"><a name="en-us_topic_0020212668_p21035367101953"></a><a name="en-us_topic_0020212668_p21035367101953"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p37294877102020"><a name="en-us_topic_0020212668_p37294877102020"></a><a name="en-us_topic_0020212668_p37294877102020"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p37223744101953"><a name="en-us_topic_0020212668_p37223744101953"></a><a name="en-us_topic_0020212668_p37223744101953"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.56%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020212668_p36517316174333"><a name="en-us_topic_0020212668_p36517316174333"></a><a name="en-us_topic_0020212668_p36517316174333"></a>Specifies the ID of the existing EIP assigned to the ECS to be created. The value is in UUID format.</p>
<p id="en-us_topic_0020212668_p60220392174333"><a name="en-us_topic_0020212668_p60220392174333"></a><a name="en-us_topic_0020212668_p60220392174333"></a>Constraints: Only EIPs in <strong id="b1283288101211"><a name="b1283288101211"></a><a name="b1283288101211"></a>DOWN</strong> state can be assigned.</p>
</td>
</tr>
<tr id="en-us_topic_0020212668_row4762671410201"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p2598724810201"><a name="en-us_topic_0020212668_p2598724810201"></a><a name="en-us_topic_0020212668_p2598724810201"></a>eip</p>
</td>
<td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p2459235410201"><a name="en-us_topic_0020212668_p2459235410201"></a><a name="en-us_topic_0020212668_p2459235410201"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p4582368110201"><a name="en-us_topic_0020212668_p4582368110201"></a><a name="en-us_topic_0020212668_p4582368110201"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="47.56%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020212668_p2073067610201"><a name="en-us_topic_0020212668_p2073067610201"></a><a name="en-us_topic_0020212668_p2073067610201"></a>Specifies an EIP that will be automatically assigned to an ECS.</p>
<p id="en-us_topic_0020212668_p19810844172712"><a name="en-us_topic_0020212668_p19810844172712"></a><a name="en-us_topic_0020212668_p19810844172712"></a>For details, see <a href="#table020717438159">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Either  **id**  or  **eip**  in the  **publicip**  field can be configured.  

## **security\_groups**  Field Description<a name="section332191084315"></a>

This field is used by the following APIs:

-   Creating ECSs: /v1/\{project\_id\}/cloudservers

**Table  2** **security\_groups**  field description

<a name="table1698566599"></a>
<table><thead align="left"><tr id="en-us_topic_0020212668_row51142457"><th class="cellrowborder" valign="top" width="18.7981201879812%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020212668_p17968192484320"><a name="en-us_topic_0020212668_p17968192484320"></a><a name="en-us_topic_0020212668_p17968192484320"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.168383161683835%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020212668_p19832247434"><a name="en-us_topic_0020212668_p19832247434"></a><a name="en-us_topic_0020212668_p19832247434"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.66823317668233%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020212668_p99833249439"><a name="en-us_topic_0020212668_p99833249439"></a><a name="en-us_topic_0020212668_p99833249439"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.36526347365263%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020212668_p13999172414438"><a name="en-us_topic_0020212668_p13999172414438"></a><a name="en-us_topic_0020212668_p13999172414438"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020212668_row34524340"><td class="cellrowborder" valign="top" width="18.7981201879812%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p45008187"><a name="en-us_topic_0020212668_p45008187"></a><a name="en-us_topic_0020212668_p45008187"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.168383161683835%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p21784493"><a name="en-us_topic_0020212668_p21784493"></a><a name="en-us_topic_0020212668_p21784493"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.66823317668233%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p19713524"><a name="en-us_topic_0020212668_p19713524"></a><a name="en-us_topic_0020212668_p19713524"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.36526347365263%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020212668_p3313237174650"><a name="en-us_topic_0020212668_p3313237174650"></a><a name="en-us_topic_0020212668_p3313237174650"></a>Specifies the ID of the security group to which an ECS is to be added. The configuration will take effect on the NICs of the ECS. You need to specify the ID of an existing security group in UUID format. Otherwise, the default security group will be used at the underlying layer.</p>
</td>
</tr>
</tbody>
</table>

## **eip**  Field Description<a name="section1840318312449"></a>

This field is used by the following APIs:

-   Creating ECSs: /v1/\{project\_id\}/cloudservers

**Table  3** **eip**  field description

<a name="table020717438159"></a>
<table><thead align="left"><tr id="row142051643161515"><th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.5.1.1"><p id="p220520436158"><a name="p220520436158"></a><a name="p220520436158"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.2"><p id="p1920514312151"><a name="p1920514312151"></a><a name="p1920514312151"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.3"><p id="p520584317151"><a name="p520584317151"></a><a name="p520584317151"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.504950495049506%" id="mcps1.2.5.1.4"><p id="p920514331510"><a name="p920514331510"></a><a name="p920514331510"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6206174311511"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.1 "><p id="p22055434158"><a name="p22055434158"></a><a name="p22055434158"></a>iptype</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p9205194311515"><a name="p9205194311515"></a><a name="p9205194311515"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p8206104311514"><a name="p8206104311514"></a><a name="p8206104311514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="p142060437155"><a name="p142060437155"></a><a name="p142060437155"></a>Specifies the EIP type.</p>
<p id="p102068433158"><a name="p102068433158"></a><a name="p102068433158"></a>For details about the enumerated values, see the <strong id="b08876115150"><a name="b08876115150"></a><a name="b08876115150"></a>publicip</strong> field in "Assigning an EIP" in <em id="i68884113159"><a name="i68884113159"></a><a name="i68884113159"></a>Virtual Private Cloud API Reference</em>.</p>
</td>
</tr>
<tr id="row52079430153"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.1 "><p id="p1320604312157"><a name="p1320604312157"></a><a name="p1320604312157"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p1720634381517"><a name="p1720634381517"></a><a name="p1720634381517"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p152067435153"><a name="p152067435153"></a><a name="p152067435153"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="p920618437151"><a name="p920618437151"></a><a name="p920618437151"></a>Specifies the EIP bandwidth.</p>
<p id="p172071043111520"><a name="p172071043111520"></a><a name="p172071043111520"></a>For details, see <a href="data-structure-for-creating-ecss.md#section172789339448">bandwidth Field Description</a>.</p>
</td>
</tr>
</tbody>
</table>

## **bandwidth**  Field Description<a name="section172789339448"></a>

This field is used by the following APIs:

-   Creating ECSs: /v1/\{project\_id\}/cloudservers

**Table  4** **bandwidth**  field description

<a name="table16301415102451"></a>
<table><thead align="left"><tr id="en-us_topic_0020212668_row17791119102758"><th class="cellrowborder" valign="top" width="19.09%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020212668_p940919329434"><a name="en-us_topic_0020212668_p940919329434"></a><a name="en-us_topic_0020212668_p940919329434"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.950000000000001%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020212668_p1542583214315"><a name="en-us_topic_0020212668_p1542583214315"></a><a name="en-us_topic_0020212668_p1542583214315"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.96%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020212668_p20425183274314"><a name="en-us_topic_0020212668_p20425183274314"></a><a name="en-us_topic_0020212668_p20425183274314"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020212668_p15440183294320"><a name="en-us_topic_0020212668_p15440183294320"></a><a name="en-us_topic_0020212668_p15440183294320"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020212668_row5196896102758"><td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p18295456102758"><a name="en-us_topic_0020212668_p18295456102758"></a><a name="en-us_topic_0020212668_p18295456102758"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p5536985102758"><a name="en-us_topic_0020212668_p5536985102758"></a><a name="en-us_topic_0020212668_p5536985102758"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.96%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p45842610102758"><a name="en-us_topic_0020212668_p45842610102758"></a><a name="en-us_topic_0020212668_p45842610102758"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p1875653414718"><a name="p1875653414718"></a><a name="p1875653414718"></a>Specifies the bandwidth size.</p>
<p id="en-us_topic_0020212668_p11589040111711"><a name="en-us_topic_0020212668_p11589040111711"></a><a name="en-us_topic_0020212668_p11589040111711"></a>Specifies the bandwidth (Mbit/s). The value ranges from 1 to 1000.</p>
</td>
</tr>
<tr id="en-us_topic_0020212668_row66157294102758"><td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p57140623102758"><a name="en-us_topic_0020212668_p57140623102758"></a><a name="en-us_topic_0020212668_p57140623102758"></a>sharetype</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p64987789102758"><a name="en-us_topic_0020212668_p64987789102758"></a><a name="en-us_topic_0020212668_p64987789102758"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.96%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p29519567102758"><a name="en-us_topic_0020212668_p29519567102758"></a><a name="en-us_topic_0020212668_p29519567102758"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020212668_p44928433102758"><a name="en-us_topic_0020212668_p44928433102758"></a><a name="en-us_topic_0020212668_p44928433102758"></a>Specifies the bandwidth sharing type.</p>
<p id="en-us_topic_0020212668_p226836615358"><a name="en-us_topic_0020212668_p226836615358"></a><a name="en-us_topic_0020212668_p226836615358"></a>Enumerated values: <strong id="b842352706114517"><a name="b842352706114517"></a><a name="b842352706114517"></a>PER</strong> (indicates exclusive bandwidth) and <strong id="b842352706114521"><a name="b842352706114521"></a><a name="b842352706114521"></a>WHOLE</strong> (indicates sharing)</p>
</td>
</tr>
<tr id="en-us_topic_0020212668_row66831921141019"><td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p44676503141019"><a name="en-us_topic_0020212668_p44676503141019"></a><a name="en-us_topic_0020212668_p44676503141019"></a>chargemode</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p62027027141019"><a name="en-us_topic_0020212668_p62027027141019"></a><a name="en-us_topic_0020212668_p62027027141019"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.96%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p58133258141019"><a name="en-us_topic_0020212668_p58133258141019"></a><a name="en-us_topic_0020212668_p58133258141019"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020212668_p11173478141019"><a name="en-us_topic_0020212668_p11173478141019"></a><a name="en-us_topic_0020212668_p11173478141019"></a>Specifies the bandwidth billing mode.</p>
<a name="en-us_topic_0020212668_ul23956879141348"></a><a name="en-us_topic_0020212668_ul23956879141348"></a><ul id="en-us_topic_0020212668_ul23956879141348"><li>If the field value is <strong id="b16182133682513"><a name="b16182133682513"></a><a name="b16182133682513"></a>traffic</strong>, the ECS is billed by traffic.</li><li>If the field value is others, creating the ECS will fail.</li></ul>
</td>
</tr>
</tbody>
</table>

## **extendparam**  Field Description for Creating Disks<a name="section1361484104817"></a>

This field is used by the following APIs:

-   Creating ECSs: /v1/\{project\_id\}/cloudservers

**Table  5** **extendparam**  field description for creating disks

<a name="table7562101331712"></a>
<table><thead align="left"><tr id="en-us_topic_0020212668_row4999061312178"><th class="cellrowborder" valign="top" width="18.988101189881014%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020212668_p159171369431"><a name="en-us_topic_0020212668_p159171369431"></a><a name="en-us_topic_0020212668_p159171369431"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.978402159784022%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020212668_p19933936124315"><a name="en-us_topic_0020212668_p19933936124315"></a><a name="en-us_topic_0020212668_p19933936124315"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.66823317668233%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020212668_p59331136154317"><a name="en-us_topic_0020212668_p59331136154317"></a><a name="en-us_topic_0020212668_p59331136154317"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.36526347365263%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020212668_p1294943624317"><a name="en-us_topic_0020212668_p1294943624317"></a><a name="en-us_topic_0020212668_p1294943624317"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020212668_row98284261548"><td class="cellrowborder" valign="top" width="18.988101189881014%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p158291026105416"><a name="en-us_topic_0020212668_p158291026105416"></a><a name="en-us_topic_0020212668_p158291026105416"></a>snapshotId</p>
</td>
<td class="cellrowborder" valign="top" width="15.978402159784022%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p9829182612547"><a name="en-us_topic_0020212668_p9829182612547"></a><a name="en-us_topic_0020212668_p9829182612547"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.66823317668233%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p1082942655420"><a name="en-us_topic_0020212668_p1082942655420"></a><a name="en-us_topic_0020212668_p1082942655420"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.36526347365263%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020212668_p165161345194219"><a name="en-us_topic_0020212668_p165161345194219"></a><a name="en-us_topic_0020212668_p165161345194219"></a>Specifies the snapshot ID or ID of the original data disk contained in the full-ECS image.</p>
<p id="en-us_topic_0020212668_p12838424153912"><a name="en-us_topic_0020212668_p12838424153912"></a><a name="en-us_topic_0020212668_p12838424153912"></a><strong id="b1778912241786"><a name="b1778912241786"></a><a name="b1778912241786"></a>Application scenarios:</strong></p>
<p id="en-us_topic_0020212668_p8101134111396"><a name="en-us_topic_0020212668_p8101134111396"></a><a name="en-us_topic_0020212668_p8101134111396"></a>This parameter is used if an ECS is created using a full-ECS image, and the image contains one or more data disks.</p>
<p id="en-us_topic_0020212668_p10347156194311"><a name="en-us_topic_0020212668_p10347156194311"></a><a name="en-us_topic_0020212668_p10347156194311"></a>When an ECS is created using a full-ECS image, the system automatically restores data from the data disk (if any) in the image. However, the disk type will be restored to the default settings: common I/O, VBD, and non-shared. The <strong id="b842352706185910"><a name="b842352706185910"></a><a name="b842352706185910"></a>snapshotId</strong> parameter allows you to specify the disk type for the original data disk after restoration.</p>
<div class="note" id="en-us_topic_0020212668_note20821102313353"><a name="en-us_topic_0020212668_note20821102313353"></a><a name="en-us_topic_0020212668_note20821102313353"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0020212668_ul18479202511419"></a><a name="en-us_topic_0020212668_ul18479202511419"></a><ul id="en-us_topic_0020212668_ul18479202511419"><li>You are advised to set <strong id="b84235270619219"><a name="b84235270619219"></a><a name="b84235270619219"></a>snapshotId</strong> for each original data disk. Otherwise, the original data disks without <strong id="b28325701419242"><a name="b28325701419242"></a><a name="b28325701419242"></a>snapshotId</strong> specified will use the default settings.</li><li>If you are required to change a disk size, ensure that the changed disk size is greater than or equal to the size of the original data disk. Otherwise, restoring data of the original data disk will fail.</li></ul>
</div></div>
<p id="en-us_topic_0020212668_p18951356175713"><a name="en-us_topic_0020212668_p18951356175713"></a><a name="en-us_topic_0020212668_p18951356175713"></a><strong id="b198571395918"><a name="b198571395918"></a><a name="b198571395918"></a>Working rules:</strong></p>
<p id="en-us_topic_0020212668_p916611325812"><a name="en-us_topic_0020212668_p916611325812"></a><a name="en-us_topic_0020212668_p916611325812"></a><strong id="b84235270619443"><a name="b84235270619443"></a><a name="b84235270619443"></a>snapshotId</strong> uniquely identifies an original data disk contained in a full-ECS image. You can use <strong id="b132452214819538"><a name="b132452214819538"></a><a name="b132452214819538"></a>snapshotId</strong> to obtain the information of the original data disk for data restoration.</p>
<p id="p29793189319"><a name="p29793189319"></a><a name="p29793189319"></a><strong id="b1045712161101"><a name="b1045712161101"></a><a name="b1045712161101"></a>Obtaining snapshotId through the management console:</strong></p>
<p id="en-us_topic_0020212668_p179131302432"><a name="en-us_topic_0020212668_p179131302432"></a><a name="en-us_topic_0020212668_p179131302432"></a>Log in to the management console, choose <strong id="b842352706145529"><a name="b842352706145529"></a><a name="b842352706145529"></a>Elastic Volume Service</strong> &gt; <strong id="b842352706145535"><a name="b842352706145535"></a><a name="b842352706145535"></a>Snapshot</strong>. Then, use the name of the original data disk to find the snapshot ID or the original disk ID.</p>
<p id="p93941230183116"><a name="p93941230183116"></a><a name="p93941230183116"></a><strong id="b1265110520118"><a name="b1265110520118"></a><a name="b1265110520118"></a>Obtaining snapshotId through the API:</strong></p>
<div class="p" id="p525262911283"><a name="p525262911283"></a><a name="p525262911283"></a>If you have obtained the full-ECS image ID, obtain the Cloud Backup and Recovery (CBR) or Cloud Server Backup Service (CSBS) backup ID associated with the full-ECS image ID by following the instructions provided in the API for querying image details.<a name="ul610116235288"></a><a name="ul610116235288"></a><ul id="ul610116235288"><li>If CBR backup is used, use the CBR backup ID to obtain the backup. The <strong id="b1296018611123"><a name="b1296018611123"></a><a name="b1296018611123"></a>resource_id</strong> or <strong id="b196116619127"><a name="b196116619127"></a><a name="b196116619127"></a>snapshot_id</strong> contained in the children field in the response is the desired <strong id="b1496217619127"><a name="b1496217619127"></a><a name="b1496217619127"></a>snapshotId</strong>. For details, see the API for "Querying a Specified Backup" in <em id="i17588183611215"><a name="i17588183611215"></a><a name="i17588183611215"></a>Cloud Backup and Recovery User Guide</em>.</li><li>If CSBS backup is used, use the CSBS backup ID to obtain the backup. The <strong id="b5644103615138"><a name="b5644103615138"></a><a name="b5644103615138"></a>source_volume_id</strong> or <strong id="b4645136141320"><a name="b4645136141320"></a><a name="b4645136141320"></a>snapshot_id</strong> contained in the <strong id="b364503631312"><a name="b364503631312"></a><a name="b364503631312"></a>volume_backups</strong> field in the response is the desired <strong id="b156451736171318"><a name="b156451736171318"></a><a name="b156451736171318"></a>snapshotId</strong>. For details, see the API for "Querying a Single Backup" in <em id="i1034939181416"><a name="i1034939181416"></a><a name="i1034939181416"></a>Cloud Server Backup Service User Guide</em>.</li></ul>
</div>
</td>
</tr>
</tbody>
</table>

## **extendparam**  Field Description for Creating ECSs<a name="section1373711413505"></a>

This field is used by the following APIs:

-   Creating ECSs: /v1/\{project\_id\}/cloudservers

**Table  6** **extendparam**  field description for creating ECSs \(for V1 APIs\)

<a name="table1137234112314"></a>
<table><thead align="left"><tr id="en-us_topic_0020212668_row908051512314"><th class="cellrowborder" valign="top" width="22.040000000000003%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020212668_p11836154112432"><a name="en-us_topic_0020212668_p11836154112432"></a><a name="en-us_topic_0020212668_p11836154112432"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.959999999999999%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020212668_p585210410437"><a name="en-us_topic_0020212668_p585210410437"></a><a name="en-us_topic_0020212668_p585210410437"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020212668_p18852134118436"><a name="en-us_topic_0020212668_p18852134118436"></a><a name="en-us_topic_0020212668_p18852134118436"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020212668_p78681541114315"><a name="en-us_topic_0020212668_p78681541114315"></a><a name="en-us_topic_0020212668_p78681541114315"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020212668_row30217817123156"><td class="cellrowborder" valign="top" width="22.040000000000003%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p3524901123156"><a name="en-us_topic_0020212668_p3524901123156"></a><a name="en-us_topic_0020212668_p3524901123156"></a>regionID</p>
</td>
<td class="cellrowborder" valign="top" width="12.959999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p17081589123156"><a name="en-us_topic_0020212668_p17081589123156"></a><a name="en-us_topic_0020212668_p17081589123156"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p41431486123156"><a name="en-us_topic_0020212668_p41431486123156"></a><a name="en-us_topic_0020212668_p41431486123156"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020212668_p507175123156"><a name="en-us_topic_0020212668_p507175123156"></a><a name="en-us_topic_0020212668_p507175123156"></a>Specifies the ID of the region where the ECS resides.</p>
</td>
</tr>
<tr id="en-us_topic_0020212668_row18799174141220"><td class="cellrowborder" valign="top" width="22.040000000000003%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p3800114111212"><a name="en-us_topic_0020212668_p3800114111212"></a><a name="en-us_topic_0020212668_p3800114111212"></a>support_auto_recovery</p>
</td>
<td class="cellrowborder" valign="top" width="12.959999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p08002401211"><a name="en-us_topic_0020212668_p08002401211"></a><a name="en-us_topic_0020212668_p08002401211"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p12800844124"><a name="en-us_topic_0020212668_p12800844124"></a><a name="en-us_topic_0020212668_p12800844124"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020212668_p73643317120"><a name="en-us_topic_0020212668_p73643317120"></a><a name="en-us_topic_0020212668_p73643317120"></a>Specifies whether automatic recovery is enabled on the ECS.</p>
<a name="en-us_topic_0020212668_ul20360154114125"></a><a name="en-us_topic_0020212668_ul20360154114125"></a><ul id="en-us_topic_0020212668_ul20360154114125"><li><strong id="b193101667377"><a name="b193101667377"></a><a name="b193101667377"></a>true</strong>: enables this function.</li><li><strong id="b84235270691530"><a name="b84235270691530"></a><a name="b84235270691530"></a>false</strong>: disables this function.</li></ul>
<div class="note" id="en-us_topic_0020212668_note968019464617"><a name="en-us_topic_0020212668_note968019464617"></a><a name="en-us_topic_0020212668_note968019464617"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0020212668_p86801749463"><a name="en-us_topic_0020212668_p86801749463"></a><a name="en-us_topic_0020212668_p86801749463"></a>This parameter is of boolean type. If a non-boolean character is imported, the parameter value is set to <strong id="b41512011113711"><a name="b41512011113711"></a><a name="b41512011113711"></a>false</strong>.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## **metadata**  Field Description for Creating Disks<a name="section1228814491353"></a>

This field is used by the following APIs:

-   Creating ECSs: /v1/\{project\_id\}/cloudservers

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   When you create an ECS, both  **root\_volume**  and  **data\_volume**  contain the  **metadata**  field.  

**Table  7** **metadata**  field description for creating disks

<a name="table1028814491351"></a>
<table><thead align="left"><tr id="row14289749355"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.1"><p id="p142893491958"><a name="p142893491958"></a><a name="p142893491958"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.2"><p id="p1128918494518"><a name="p1128918494518"></a><a name="p1128918494518"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="p202891549251"><a name="p202891549251"></a><a name="p202891549251"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.46464646464647%" id="mcps1.2.5.1.4"><p id="p328918491518"><a name="p328918491518"></a><a name="p328918491518"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10289249156"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p1562408795622"><a name="p1562408795622"></a><a name="p1562408795622"></a>__system__encrypted</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p5759155095622"><a name="p5759155095622"></a><a name="p5759155095622"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p3440400295622"><a name="p3440400295622"></a><a name="p3440400295622"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p729227516614"><a name="p729227516614"></a><a name="p729227516614"></a>Specifies encryption in <strong id="b2039276207171318"><a name="b2039276207171318"></a><a name="b2039276207171318"></a>metadata</strong>. The value can be <strong id="b815044561171318"><a name="b815044561171318"></a><a name="b815044561171318"></a>0</strong> (encryption disabled) or <strong id="b1102444237171318"><a name="b1102444237171318"></a><a name="b1102444237171318"></a>1</strong> (encryption enabled).</p>
<p id="p3526077895622"><a name="p3526077895622"></a><a name="p3526077895622"></a>If this parameter does not exist, the disk will not be encrypted by default.</p>
</td>
</tr>
<tr id="row428914491452"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p241272995622"><a name="p241272995622"></a><a name="p241272995622"></a>__system__cmkid</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p683657101711"><a name="p683657101711"></a><a name="p683657101711"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p5933737595622"><a name="p5933737595622"></a><a name="p5933737595622"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p20670814113715"><a name="p20670814113715"></a><a name="p20670814113715"></a>Specifies the CMK ID, which indicates encryption in <strong id="b18651112211379"><a name="b18651112211379"></a><a name="b18651112211379"></a>metadata</strong>. This parameter is used with <strong id="b891155174413"><a name="b891155174413"></a><a name="b891155174413"></a>__system__encrypted</strong>.</p>
<div class="note" id="note153392271895"><a name="note153392271895"></a><a name="note153392271895"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p35971634891"><a name="p35971634891"></a><a name="p35971634891"></a>For details about how to obtain the CMK ID, see "Querying the List of CMKs" in <em id="i185111076413"><a name="i185111076413"></a><a name="i185111076413"></a>Key Management Service API Reference</em>.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## **metadata**  Field Description for Creating ECSs<a name="section1574435185018"></a>

This field is used by the following APIs:

-   Creating ECSs: /v1/\{project\_id\}/cloudservers

**Table  8** **metadata**  field description

<a name="table2373623012315"></a>
<table><thead align="left"><tr id="en-us_topic_0020212668_row4787810512315"><th class="cellrowborder" valign="top" width="21.617838216178384%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020212668_p135337462439"><a name="en-us_topic_0020212668_p135337462439"></a><a name="en-us_topic_0020212668_p135337462439"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.448655134486554%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020212668_p1853324694312"><a name="en-us_topic_0020212668_p1853324694312"></a><a name="en-us_topic_0020212668_p1853324694312"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.58834116588341%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020212668_p2054974617431"><a name="en-us_topic_0020212668_p2054974617431"></a><a name="en-us_topic_0020212668_p2054974617431"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.34516548345165%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020212668_p75495461436"><a name="en-us_topic_0020212668_p75495461436"></a><a name="en-us_topic_0020212668_p75495461436"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020212668_row5207191472520"><td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p374219816268"><a name="en-us_topic_0020212668_p374219816268"></a><a name="en-us_topic_0020212668_p374219816268"></a>User-defined field key-value pair</p>
</td>
<td class="cellrowborder" valign="top" width="13.448655134486554%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p19742188182614"><a name="en-us_topic_0020212668_p19742188182614"></a><a name="en-us_topic_0020212668_p19742188182614"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.58834116588341%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p27421685267"><a name="en-us_topic_0020212668_p27421685267"></a><a name="en-us_topic_0020212668_p27421685267"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.34516548345165%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020212668_p19742380265"><a name="en-us_topic_0020212668_p19742380265"></a><a name="en-us_topic_0020212668_p19742380265"></a>Specifies the user-defined field key-value pair.</p>
<div class="note" id="en-us_topic_0020212668_note4876141782613"><a name="en-us_topic_0020212668_note4876141782613"></a><a name="en-us_topic_0020212668_note4876141782613"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0020212668_ul49971332368"></a><a name="en-us_topic_0020212668_ul49971332368"></a><ul id="en-us_topic_0020212668_ul49971332368"><li>A maximum of 10 key-value pairs can be injected.</li><li>A metadata key consists of 1 to 255 characters and contains only uppercase letters, lowercase letters, digits, hyphens (-), underscores (_), colons (:), and decimal points (.).</li><li>A metadata value consists of a maximum of 255 characters.</li></ul>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0020212668_row1137835517246"><td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p3877115254"><a name="en-us_topic_0020212668_p3877115254"></a><a name="en-us_topic_0020212668_p3877115254"></a>admin_pass</p>
</td>
<td class="cellrowborder" valign="top" width="13.448655134486554%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p28712114258"><a name="en-us_topic_0020212668_p28712114258"></a><a name="en-us_topic_0020212668_p28712114258"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.58834116588341%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p587610259"><a name="en-us_topic_0020212668_p587610259"></a><a name="en-us_topic_0020212668_p587610259"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.34516548345165%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020212668_p1587815251"><a name="en-us_topic_0020212668_p1587815251"></a><a name="en-us_topic_0020212668_p1587815251"></a>Specifies the password of user <strong id="b8423527061197"><a name="b8423527061197"></a><a name="b8423527061197"></a>Administrator</strong> for logging in to a Windows ECS. For details, see <a href="creating-an-ecs.md#section61372619">Function</a>.</p>
<p id="en-us_topic_0020212668_p3871619258"><a name="en-us_topic_0020212668_p3871619258"></a><a name="en-us_topic_0020212668_p3871619258"></a>Example: <strong id="en-us_topic_0057972661_b84235270620046"><a name="en-us_topic_0057972661_b84235270620046"></a><a name="en-us_topic_0057972661_b84235270620046"></a>cloud.1234</strong></p>
<div class="note" id="en-us_topic_0020212668_note178716152516"><a name="en-us_topic_0020212668_note178716152516"></a><a name="en-us_topic_0020212668_note178716152516"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0020212668_p158717113250"><a name="en-us_topic_0020212668_p158717113250"></a><a name="en-us_topic_0020212668_p158717113250"></a>This parameter is mandatory when a Windows ECS using password authentication is created.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0020212668_row123659618318"><td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p1585813419425"><a name="en-us_topic_0020212668_p1585813419425"></a><a name="en-us_topic_0020212668_p1585813419425"></a>op_svc_userid</p>
</td>
<td class="cellrowborder" valign="top" width="13.448655134486554%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p30970240152124"><a name="en-us_topic_0020212668_p30970240152124"></a><a name="en-us_topic_0020212668_p30970240152124"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.58834116588341%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p25561503152124"><a name="en-us_topic_0020212668_p25561503152124"></a><a name="en-us_topic_0020212668_p25561503152124"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.34516548345165%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020212668_p57215887152124"><a name="en-us_topic_0020212668_p57215887152124"></a><a name="en-us_topic_0020212668_p57215887152124"></a>Specifies the user ID.</p>
</td>
</tr>
<tr id="row188201635161913"><td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.2.5.1.1 "><p id="p482163517190"><a name="p482163517190"></a><a name="p482163517190"></a>agency_name</p>
</td>
<td class="cellrowborder" valign="top" width="13.448655134486554%" headers="mcps1.2.5.1.2 "><p id="p3821143561911"><a name="p3821143561911"></a><a name="p3821143561911"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.58834116588341%" headers="mcps1.2.5.1.3 "><p id="p38217353191"><a name="p38217353191"></a><a name="p38217353191"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.34516548345165%" headers="mcps1.2.5.1.4 "><p id="p0842044134818"><a name="p0842044134818"></a><a name="p0842044134818"></a>Specifies the IAM agency name.</p>
<p id="p9821153514191"><a name="p9821153514191"></a><a name="p9821153514191"></a>An agency is created by a tenant administrator on Identity and Access Management (IAM) to provide temporary credentials for ECSs to access cloud services.</p>
</td>
</tr>
</tbody>
</table>

## **os:scheduler\_hints**  Field Description<a name="section16585034175117"></a>

This field is used by the following APIs:

-   Creating ECSs: /v1/\{project\_id\}/cloudservers
-   Creating ECSs \(native API\): /v2.1/\{project\_id\}/servers

    **Table  9** **os:scheduler\_hints**  field description

    <a name="table24430409172542"></a>
    <table><thead align="left"><tr id="en-us_topic_0020212668_row5164550172542"><th class="cellrowborder" valign="top" width="22.747725227477254%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020212668_p1649754984312"><a name="en-us_topic_0020212668_p1649754984312"></a><a name="en-us_topic_0020212668_p1649754984312"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.418558144185582%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020212668_p10512194974320"><a name="en-us_topic_0020212668_p10512194974320"></a><a name="en-us_topic_0020212668_p10512194974320"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.468453154684534%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020212668_p13512164915435"><a name="en-us_topic_0020212668_p13512164915435"></a><a name="en-us_topic_0020212668_p13512164915435"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.36526347365263%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020212668_p15528949104315"><a name="en-us_topic_0020212668_p15528949104315"></a><a name="en-us_topic_0020212668_p15528949104315"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020212668_row16191828172542"><td class="cellrowborder" valign="top" width="22.747725227477254%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p4448806918565"><a name="en-us_topic_0020212668_p4448806918565"></a><a name="en-us_topic_0020212668_p4448806918565"></a>group</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.418558144185582%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p1252936172542"><a name="en-us_topic_0020212668_p1252936172542"></a><a name="en-us_topic_0020212668_p1252936172542"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.468453154684534%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p34378991172542"><a name="en-us_topic_0020212668_p34378991172542"></a><a name="en-us_topic_0020212668_p34378991172542"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.36526347365263%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020212668_p33234878172542"><a name="en-us_topic_0020212668_p33234878172542"></a><a name="en-us_topic_0020212668_p33234878172542"></a>Specifies an ECS group ID, which is in UUID format.</p>
    <p id="en-us_topic_0020212668_p1295251611495"><a name="en-us_topic_0020212668_p1295251611495"></a><a name="en-us_topic_0020212668_p1295251611495"></a>Obtain the parameter value from the console or by performing operations provided in <a href="querying-ecs-groups(openstack).md">Querying ECS Groups</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020212668_row4670511154836"><td class="cellrowborder" valign="top" width="22.747725227477254%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p9464792154850"><a name="en-us_topic_0020212668_p9464792154850"></a><a name="en-us_topic_0020212668_p9464792154850"></a>tenancy</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.418558144185582%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p28450689154850"><a name="en-us_topic_0020212668_p28450689154850"></a><a name="en-us_topic_0020212668_p28450689154850"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.468453154684534%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p22804507154850"><a name="en-us_topic_0020212668_p22804507154850"></a><a name="en-us_topic_0020212668_p22804507154850"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.36526347365263%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020212668_p35225806154850"><a name="en-us_topic_0020212668_p35225806154850"></a><a name="en-us_topic_0020212668_p35225806154850"></a>Creates ECSs on a dedicated or shared host.</p>
    <p id="en-us_topic_0020212668_p48596800154850"><a name="en-us_topic_0020212668_p48596800154850"></a><a name="en-us_topic_0020212668_p48596800154850"></a>The value of this parameter can be <strong id="b84235270693435"><a name="b84235270693435"></a><a name="b84235270693435"></a>dedicated</strong> or <strong id="b84235270693438"><a name="b84235270693438"></a><a name="b84235270693438"></a>shared</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020212668_row35777762154842"><td class="cellrowborder" valign="top" width="22.747725227477254%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p60695964154850"><a name="en-us_topic_0020212668_p60695964154850"></a><a name="en-us_topic_0020212668_p60695964154850"></a>dedicated_host_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.418558144185582%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p17426056154850"><a name="en-us_topic_0020212668_p17426056154850"></a><a name="en-us_topic_0020212668_p17426056154850"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.468453154684534%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p2224428154850"><a name="en-us_topic_0020212668_p2224428154850"></a><a name="en-us_topic_0020212668_p2224428154850"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.36526347365263%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020212668_p45961009154850"><a name="en-us_topic_0020212668_p45961009154850"></a><a name="en-us_topic_0020212668_p45961009154850"></a>Specifies the dedicated host ID.</p>
    <div class="note" id="en-us_topic_0020212668_note104335662920"><a name="en-us_topic_0020212668_note104335662920"></a><a name="en-us_topic_0020212668_note104335662920"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0020212668_p238416346291"><a name="en-us_topic_0020212668_p238416346291"></a><a name="en-us_topic_0020212668_p238416346291"></a>A DeH ID takes effect only when <strong id="b842352706191448"><a name="b842352706191448"></a><a name="b842352706191448"></a>tenancy</strong> is set to <strong id="b842352706191453"><a name="b842352706191453"></a><a name="b842352706191453"></a>dedicated</strong>.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


## **binding:profile**  Field Description<a name="section681114217434"></a>

This field is used by the following APIs:

-   Creating ECSs: /v1/\{project\_id\}/cloudservers

**Table  10** **binding:profile**  field description

<a name="table42451440577"></a>
<table><thead align="left"><tr id="en-us_topic_0020212668_row527424465711"><th class="cellrowborder" valign="top" width="22.747725227477254%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020212668_p327225311433"><a name="en-us_topic_0020212668_p327225311433"></a><a name="en-us_topic_0020212668_p327225311433"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.84851514848515%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020212668_p12881953184318"><a name="en-us_topic_0020212668_p12881953184318"></a><a name="en-us_topic_0020212668_p12881953184318"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.038496150384962%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020212668_p828865316433"><a name="en-us_topic_0020212668_p828865316433"></a><a name="en-us_topic_0020212668_p828865316433"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.36526347365263%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020212668_p1530345324320"><a name="en-us_topic_0020212668_p1530345324320"></a><a name="en-us_topic_0020212668_p1530345324320"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020212668_row4319184413579"><td class="cellrowborder" valign="top" width="22.747725227477254%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p5943195315816"><a name="en-us_topic_0020212668_p5943195315816"></a><a name="en-us_topic_0020212668_p5943195315816"></a>disable_security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="14.84851514848515%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p1933114417571"><a name="en-us_topic_0020212668_p1933114417571"></a><a name="en-us_topic_0020212668_p1933114417571"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.038496150384962%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p11337144105712"><a name="en-us_topic_0020212668_p11337144105712"></a><a name="en-us_topic_0020212668_p11337144105712"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="47.36526347365263%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020212668_p20347144419574"><a name="en-us_topic_0020212668_p20347144419574"></a><a name="en-us_topic_0020212668_p20347144419574"></a>Indicates that a HANA ECS NIC is not added to a security group.</p>
<div class="note" id="en-us_topic_0020212668_note12688551006"><a name="en-us_topic_0020212668_note12688551006"></a><a name="en-us_topic_0020212668_note12688551006"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0020212668_ul11762133368"></a><a name="en-us_topic_0020212668_ul11762133368"></a><ul id="en-us_topic_0020212668_ul11762133368"><li>A primary HANA ECS NIC must be added to a security group.</li><li>At most one HANA ECS NIC is allowed not to add to any security group.</li></ul>
</div></div>
</td>
</tr>
</tbody>
</table>

## **extra\_dhcp\_opts**  Field Description<a name="section12781010134512"></a>

This field is used by the following APIs:

-   Creating ECSs: /v1/\{project\_id\}/cloudservers

**Table  11** **extra\_dhcp\_opts**  field description

<a name="table93959401279"></a>
<table><thead align="left"><tr id="en-us_topic_0020212668_row1142718406718"><th class="cellrowborder" valign="top" width="22.747725227477254%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020212668_p83691007441"><a name="en-us_topic_0020212668_p83691007441"></a><a name="en-us_topic_0020212668_p83691007441"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.84851514848515%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020212668_p136919015446"><a name="en-us_topic_0020212668_p136919015446"></a><a name="en-us_topic_0020212668_p136919015446"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.038496150384962%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020212668_p1338616034416"><a name="en-us_topic_0020212668_p1338616034416"></a><a name="en-us_topic_0020212668_p1338616034416"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.36526347365263%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020212668_p73861404449"><a name="en-us_topic_0020212668_p73861404449"></a><a name="en-us_topic_0020212668_p73861404449"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020212668_row15468840872"><td class="cellrowborder" valign="top" width="22.747725227477254%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p147617408712"><a name="en-us_topic_0020212668_p147617408712"></a><a name="en-us_topic_0020212668_p147617408712"></a>opt_value</p>
</td>
<td class="cellrowborder" valign="top" width="14.84851514848515%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p5483104013713"><a name="en-us_topic_0020212668_p5483104013713"></a><a name="en-us_topic_0020212668_p5483104013713"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.038496150384962%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p34905405716"><a name="en-us_topic_0020212668_p34905405716"></a><a name="en-us_topic_0020212668_p34905405716"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="47.36526347365263%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020212668_p1850016404713"><a name="en-us_topic_0020212668_p1850016404713"></a><a name="en-us_topic_0020212668_p1850016404713"></a>Specifies the NIC MTU, which ranges from 1280 to 8888.</p>
</td>
</tr>
<tr id="en-us_topic_0020212668_row1350416401775"><td class="cellrowborder" valign="top" width="22.747725227477254%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020212668_p1651164016710"><a name="en-us_topic_0020212668_p1651164016710"></a><a name="en-us_topic_0020212668_p1651164016710"></a>opt_name</p>
</td>
<td class="cellrowborder" valign="top" width="14.84851514848515%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020212668_p85191040476"><a name="en-us_topic_0020212668_p85191040476"></a><a name="en-us_topic_0020212668_p85191040476"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.038496150384962%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020212668_p14526154019715"><a name="en-us_topic_0020212668_p14526154019715"></a><a name="en-us_topic_0020212668_p14526154019715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.36526347365263%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020212668_p135322401179"><a name="en-us_topic_0020212668_p135322401179"></a><a name="en-us_topic_0020212668_p135322401179"></a>Set the parameter value to <strong id="b1598982315913"><a name="b1598982315913"></a><a name="b1598982315913"></a>26</strong>.</p>
</td>
</tr>
</tbody>
</table>

