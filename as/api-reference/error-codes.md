# Error Codes<a name="EN-US_TOPIC_0043063042"></a>

## Description<a name="section24124960164955"></a>

This section provides the meanings of error codes returned by AS APIs.

## Returned Body Format<a name="section4573701164955"></a>

\{"error":\{"code":"AS.0001","message":"System error."\}\}

## Error Code Description<a name="section45893865164955"></a>

<a name="table26415567164955"></a>
<table><thead align="left"><tr id="row1545304164955"><th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.1.6.1.1"><p id="p6284392610354"><a name="p6284392610354"></a><a name="p6284392610354"></a>HTTP Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.1.6.1.2"><p id="p58060822164955"><a name="p58060822164955"></a><a name="p58060822164955"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.1.6.1.3"><p id="p5306116164955"><a name="p5306116164955"></a><a name="p5306116164955"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.1.6.1.4"><p id="p5040809173036"><a name="p5040809173036"></a><a name="p5040809173036"></a>Error Message</p>
</th>
<th class="cellrowborder" valign="top" width="34.343434343434346%" id="mcps1.1.6.1.5"><p id="p25790345103515"><a name="p25790345103515"></a><a name="p25790345103515"></a>Solution</p>
</th>
</tr>
</thead>
<tbody><tr id="row27142218164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p4287735410374"><a name="p4287735410374"></a><a name="p4287735410374"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p51036049164955"><a name="p51036049164955"></a><a name="p51036049164955"></a>AS.0001</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p40279296164955"><a name="p40279296164955"></a><a name="p40279296164955"></a>A system error occurs.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p55191899173036"><a name="p55191899173036"></a><a name="p55191899173036"></a>System error.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p5020800311042"><a name="p5020800311042"></a><a name="p5020800311042"></a>Try again later or contact technical support.</p>
</td>
</tr>
<tr id="row26969351164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p5196964910374"><a name="p5196964910374"></a><a name="p5196964910374"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p37033798164955"><a name="p37033798164955"></a><a name="p37033798164955"></a>AS.0002</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p46947650164955"><a name="p46947650164955"></a><a name="p46947650164955"></a>The message body is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p36685269173036"><a name="p36685269173036"></a><a name="p36685269173036"></a>Request body is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p2730398011042"><a name="p2730398011042"></a><a name="p2730398011042"></a>Enter a valid message body.</p>
</td>
</tr>
<tr id="row31213038164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1511305210374"><a name="p1511305210374"></a><a name="p1511305210374"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p45228113164955"><a name="p45228113164955"></a><a name="p45228113164955"></a>AS.0005</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p39598574164955"><a name="p39598574164955"></a><a name="p39598574164955"></a>The header in the request carries no or an empty token.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p58777598173036"><a name="p58777598173036"></a><a name="p58777598173036"></a>The token of the header in the request is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4189352211042"><a name="p4189352211042"></a><a name="p4189352211042"></a>Enter a valid token.</p>
</td>
</tr>
<tr id="row20842849164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1156183910374"><a name="p1156183910374"></a><a name="p1156183910374"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p10549189164955"><a name="p10549189164955"></a><a name="p10549189164955"></a>AS.0006</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p49177974164955"><a name="p49177974164955"></a><a name="p49177974164955"></a>The header in the request carries an incorrect, invalid, or expired token.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p33414429173036"><a name="p33414429173036"></a><a name="p33414429173036"></a>The token of the header in the request is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p584510211042"><a name="p584510211042"></a><a name="p584510211042"></a>Enter a valid token.</p>
</td>
</tr>
<tr id="row39948582164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p3997329310374"><a name="p3997329310374"></a><a name="p3997329310374"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p14609716164955"><a name="p14609716164955"></a><a name="p14609716164955"></a>AS.0007</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p42536387164955"><a name="p42536387164955"></a><a name="p42536387164955"></a>The requested resources are not found.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p4694203171112"><a name="p4694203171112"></a><a name="p4694203171112"></a>The requested resource [%s] could not be found.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p14508347439"><a name="p14508347439"></a><a name="p14508347439"></a>Use the correct URL parameter.</p>
</td>
</tr>
<tr id="row47283171164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1528367910374"><a name="p1528367910374"></a><a name="p1528367910374"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p4731605164955"><a name="p4731605164955"></a><a name="p4731605164955"></a>AS.0008</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p47715740164955"><a name="p47715740164955"></a><a name="p47715740164955"></a>The <strong id="b842352706185959"><a name="b842352706185959"></a><a name="b842352706185959"></a>project id</strong> value carried in the URL is different from that resolved from the token.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p53967930173036"><a name="p53967930173036"></a><a name="p53967930173036"></a>Incorrect ProjectID.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p5932175911042"><a name="p5932175911042"></a><a name="p5932175911042"></a>Check whether the parameter in the URL matches that in the token.</p>
</td>
</tr>
<tr id="row9644045164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p173084110374"><a name="p173084110374"></a><a name="p173084110374"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p42970152164955"><a name="p42970152164955"></a><a name="p42970152164955"></a>AS.0011</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p58030292164955"><a name="p58030292164955"></a><a name="p58030292164955"></a>You do not have the rights to perform the operation.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p16827031173036"><a name="p16827031173036"></a><a name="p16827031173036"></a>You do not have the rights to perform the operation.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p2745395311042"><a name="p2745395311042"></a><a name="p2745395311042"></a>Check whether te_admin, as_adm, or other required roles exist.</p>
</td>
</tr>
<tr id="row60762273153240"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1001485210383"><a name="p1001485210383"></a><a name="p1001485210383"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p22797109153240"><a name="p22797109153240"></a><a name="p22797109153240"></a>AS.0022</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p34626541153240"><a name="p34626541153240"></a><a name="p34626541153240"></a>The request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p64952194173036"><a name="p64952194173036"></a><a name="p64952194173036"></a>Request body error</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p263540911042"><a name="p263540911042"></a><a name="p263540911042"></a>Check whether the request body is in standard JSON format or whether an unsupported parameter exists.</p>
</td>
</tr>
<tr id="row48813578143217"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p25538210143224"><a name="p25538210143224"></a><a name="p25538210143224"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p55329100143224"><a name="p55329100143224"></a><a name="p55329100143224"></a>AS.0026</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p52472098143224"><a name="p52472098143224"></a><a name="p52472098143224"></a>No scaling action is allowed in the cooldown period.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p22381582143224"><a name="p22381582143224"></a><a name="p22381582143224"></a>Scaling action is not allowed in the cooling duration.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p968821143224"><a name="p968821143224"></a><a name="p968821143224"></a>Try again later.</p>
</td>
</tr>
<tr id="row176889287502"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1689102812503"><a name="p1689102812503"></a><a name="p1689102812503"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p20689132816501"><a name="p20689132816501"></a><a name="p20689132816501"></a>AS.0031</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p96895288503"><a name="p96895288503"></a><a name="p96895288503"></a>Fine-grained authentication failed because no authentication item is specified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p36891728125011"><a name="p36891728125011"></a><a name="p36891728125011"></a>Policy doesn't allow [%s] to be performed.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1568916283507"><a name="p1568916283507"></a><a name="p1568916283507"></a>Add the required authorization item.</p>
</td>
</tr>
<tr id="row34504214556"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1545216211557"><a name="p1545216211557"></a><a name="p1545216211557"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p1445218225514"><a name="p1445218225514"></a><a name="p1445218225514"></a>AS.0033</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p17452172135510"><a name="p17452172135510"></a><a name="p17452172135510"></a>Invalid API ID.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p345216285518"><a name="p345216285518"></a><a name="p345216285518"></a>The api version is illegal, only v1 and v2.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p845272135512"><a name="p845272135512"></a><a name="p845272135512"></a>Enter a correct API ID.</p>
</td>
</tr>
<tr id="row329718231433"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1629782310436"><a name="p1629782310436"></a><a name="p1629782310436"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p19297172324315"><a name="p19297172324315"></a><a name="p19297172324315"></a>AS.0034</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p1081143214276"><a name="p1081143214276"></a><a name="p1081143214276"></a>Failed to trigger the AS policy because a scaling action in the AS group is in progress.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p1229782334315"><a name="p1229782334315"></a><a name="p1229782334315"></a>Failed to execute the policy because the AS group is in active state.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p2029719238430"><a name="p2029719238430"></a><a name="p2029719238430"></a>An AS policy can be automatically triggered only when there is no in-progress scaling action in the AS group. Try again later.</p>
</td>
</tr>
<tr id="row7428484164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p5306980810383"><a name="p5306980810383"></a><a name="p5306980810383"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p64836351164955"><a name="p64836351164955"></a><a name="p64836351164955"></a>AS.1001</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p17253091164955"><a name="p17253091164955"></a><a name="p17253091164955"></a>The <strong>start number</strong> value is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p38400933173036"><a name="p38400933173036"></a><a name="p38400933173036"></a>The value of parameter Start number is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p616142118510"><a name="p616142118510"></a><a name="p616142118510"></a>Enter a valid <strong id="b151111837854"><a name="b151111837854"></a><a name="b151111837854"></a>start number</strong> value.</p>
</td>
</tr>
<tr id="row21060091164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p3318496110383"><a name="p3318496110383"></a><a name="p3318496110383"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p28145806164955"><a name="p28145806164955"></a><a name="p28145806164955"></a>AS.1002</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p65217822164955"><a name="p65217822164955"></a><a name="p65217822164955"></a>The <strong>limit</strong> value is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p9884531173036"><a name="p9884531173036"></a><a name="p9884531173036"></a>The value of parameter Limit is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p6500546155119"><a name="p6500546155119"></a><a name="p6500546155119"></a>Enter a valid <strong id="b197661171663"><a name="b197661171663"></a><a name="b197661171663"></a>limit</strong> value.</p>
</td>
</tr>
<tr id="row50089488164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p564352810440"><a name="p564352810440"></a><a name="p564352810440"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p30716709164955"><a name="p30716709164955"></a><a name="p30716709164955"></a>AS.1003</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p5025515164955"><a name="p5025515164955"></a><a name="p5025515164955"></a>The AS configuration ID is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p25174709173036"><a name="p25174709173036"></a><a name="p25174709173036"></a>The AS configuration ID is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p5383018811042"><a name="p5383018811042"></a><a name="p5383018811042"></a>Add an AS configuration ID.</p>
</td>
</tr>
<tr id="row45229640164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p2049143710440"><a name="p2049143710440"></a><a name="p2049143710440"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p39722201164955"><a name="p39722201164955"></a><a name="p39722201164955"></a>AS.1004</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p63381744164955"><a name="p63381744164955"></a><a name="p63381744164955"></a>The AS configuration does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p31643263173036"><a name="p31643263173036"></a><a name="p31643263173036"></a>The AS configuration does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p5063117211042"><a name="p5063117211042"></a><a name="p5063117211042"></a>Use a correct AS configuration ID.</p>
</td>
</tr>
<tr id="row33564784164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p4008993710440"><a name="p4008993710440"></a><a name="p4008993710440"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p34392968164955"><a name="p34392968164955"></a><a name="p34392968164955"></a>AS.1006</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p34367000164955"><a name="p34367000164955"></a><a name="p34367000164955"></a>The AS configuration is being used by an AS group and cannot be deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p49598957173036"><a name="p49598957173036"></a><a name="p49598957173036"></a>The AS configuration is in use.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p060811315523"><a name="p060811315523"></a><a name="p060811315523"></a>Change this AS configuration for the AS group to another one and delete the AS configuration.</p>
</td>
</tr>
<tr id="row40867549164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p3320843910440"><a name="p3320843910440"></a><a name="p3320843910440"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p21937173164955"><a name="p21937173164955"></a><a name="p21937173164955"></a>AS.1007</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p32080602164955"><a name="p32080602164955"></a><a name="p32080602164955"></a>The AS configuration name is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p53071073173036"><a name="p53071073173036"></a><a name="p53071073173036"></a>The AS configuration name is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4757422211042"><a name="p4757422211042"></a><a name="p4757422211042"></a>Add an AS configuration name.</p>
</td>
</tr>
<tr id="row20289964164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p4976132210440"><a name="p4976132210440"></a><a name="p4976132210440"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p32874415164955"><a name="p32874415164955"></a><a name="p32874415164955"></a>AS.1008</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p45581938164955"><a name="p45581938164955"></a><a name="p45581938164955"></a>The AS configuration name is too long.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p34106565173036"><a name="p34106565173036"></a><a name="p34106565173036"></a>The AS configuration name is too long.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p5343417411042"><a name="p5343417411042"></a><a name="p5343417411042"></a>Use an AS configuration name of proper length.</p>
</td>
</tr>
<tr id="row7584259164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p3721772610440"><a name="p3721772610440"></a><a name="p3721772610440"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p10345225164955"><a name="p10345225164955"></a><a name="p10345225164955"></a>AS.1009</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p32656933164955"><a name="p32656933164955"></a><a name="p32656933164955"></a>The AS group ID is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p33406798173036"><a name="p33406798173036"></a><a name="p33406798173036"></a>The AS group ID is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p3037237611042"><a name="p3037237611042"></a><a name="p3037237611042"></a>Add an AS group ID.</p>
</td>
</tr>
<tr id="row8535681164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p3012882510440"><a name="p3012882510440"></a><a name="p3012882510440"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p20301566164955"><a name="p20301566164955"></a><a name="p20301566164955"></a>AS.1011</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p33814168164955"><a name="p33814168164955"></a><a name="p33814168164955"></a>The <strong id="b16033132278"><a name="b16033132278"></a><a name="b16033132278"></a>instance_config</strong> field is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p25447168173036"><a name="p25447168173036"></a><a name="p25447168173036"></a>The instance configuration information is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p3516207511042"><a name="p3516207511042"></a><a name="p3516207511042"></a>Enter a valid <strong id="b135702027182719"><a name="b135702027182719"></a><a name="b135702027182719"></a>instance_config</strong> value.</p>
</td>
</tr>
<tr id="row25181088164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1931518310440"><a name="p1931518310440"></a><a name="p1931518310440"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p26402236164955"><a name="p26402236164955"></a><a name="p26402236164955"></a>AS.1014</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p58206332164955"><a name="p58206332164955"></a><a name="p58206332164955"></a>The image ID is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p28939704173036"><a name="p28939704173036"></a><a name="p28939704173036"></a>The image ID in the AS configuration is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p6467597011042"><a name="p6467597011042"></a><a name="p6467597011042"></a>Add an image ID.</p>
</td>
</tr>
<tr id="row54094941164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p43572206104438"><a name="p43572206104438"></a><a name="p43572206104438"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p19614095164955"><a name="p19614095164955"></a><a name="p19614095164955"></a>AS.1015</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p45237849164955"><a name="p45237849164955"></a><a name="p45237849164955"></a>The image in the AS configuration does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p24861103173036"><a name="p24861103173036"></a><a name="p24861103173036"></a>The image in the AS configuration does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p3836020711042"><a name="p3836020711042"></a><a name="p3836020711042"></a>Use a correct image ID. </p>
</td>
</tr>
<tr id="row4487463164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p21645617104438"><a name="p21645617104438"></a><a name="p21645617104438"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p27940233164955"><a name="p27940233164955"></a><a name="p27940233164955"></a>AS.1016</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p48566424164955"><a name="p48566424164955"></a><a name="p48566424164955"></a>The flavor ID is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p4351298173036"><a name="p4351298173036"></a><a name="p4351298173036"></a>The specification ID in the AS configuration cannot be null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4730357111042"><a name="p4730357111042"></a><a name="p4730357111042"></a>Add a flavor ID.</p>
</td>
</tr>
<tr id="row34444635164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p9071993104438"><a name="p9071993104438"></a><a name="p9071993104438"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p38552088164955"><a name="p38552088164955"></a><a name="p38552088164955"></a>AS.1017</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p35711413164955"><a name="p35711413164955"></a><a name="p35711413164955"></a>The flavor of the AS configuration does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p17979794173036"><a name="p17979794173036"></a><a name="p17979794173036"></a>The specification [%s] in the AS configuration does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p5745642711042"><a name="p5745642711042"></a><a name="p5745642711042"></a>Use a correct flavor ID.</p>
</td>
</tr>
<tr id="row52967263164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p36814682104438"><a name="p36814682104438"></a><a name="p36814682104438"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p62489904164955"><a name="p62489904164955"></a><a name="p62489904164955"></a>AS.1018</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p28517429164955"><a name="p28517429164955"></a><a name="p28517429164955"></a>The flavor and image do not match.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p21041996173036"><a name="p21041996173036"></a><a name="p21041996173036"></a>The specification [%s] and image is not match.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p92691444154514"><a name="p92691444154514"></a><a name="p92691444154514"></a>Check whether the flavor matches the image. If not, modify the configuration.</p>
</td>
</tr>
<tr id="row39695358201718"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p61466477104438"><a name="p61466477104438"></a><a name="p61466477104438"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p61207391201718"><a name="p61207391201718"></a><a name="p61207391201718"></a>AS.1019</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p58851633201718"><a name="p58851633201718"></a><a name="p58851633201718"></a>The flavor and disk do not match.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p38794594173036"><a name="p38794594173036"></a><a name="p38794594173036"></a>The disk of this type is not applicable to the ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p3373443911042"><a name="p3373443911042"></a><a name="p3373443911042"></a>Check whether the flavor matches the disk type. If not, change the resources.</p>
</td>
</tr>
<tr id="row6730222164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p5711522310457"><a name="p5711522310457"></a><a name="p5711522310457"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p8277111164955"><a name="p8277111164955"></a><a name="p8277111164955"></a>AS.1021</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p66466289164955"><a name="p66466289164955"></a><a name="p66466289164955"></a>The image in the AS configuration is not activated.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p54283350173036"><a name="p54283350173036"></a><a name="p54283350173036"></a>The image in the AS configuration is not activated.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p6682329211042"><a name="p6682329211042"></a><a name="p6682329211042"></a>Use a correct image ID. </p>
</td>
</tr>
<tr id="row344587479011"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p2950230910457"><a name="p2950230910457"></a><a name="p2950230910457"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p396951319011"><a name="p396951319011"></a><a name="p396951319011"></a>AS.1022</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p611890239011"><a name="p611890239011"></a><a name="p611890239011"></a>The image in the AS configuration is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p45441859173036"><a name="p45441859173036"></a><a name="p45441859173036"></a>The image in the AS configuration is not available.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p6025385611042"><a name="p6025385611042"></a><a name="p6025385611042"></a>Use a correct image ID. </p>
</td>
</tr>
<tr id="row26749458164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p3234742010457"><a name="p3234742010457"></a><a name="p3234742010457"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p19222494164955"><a name="p19222494164955"></a><a name="p19222494164955"></a>AS.1023</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p13518178164955"><a name="p13518178164955"></a><a name="p13518178164955"></a>The AS configuration name is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p42445351173036"><a name="p42445351173036"></a><a name="p42445351173036"></a>Invalid AS configuration name.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p3586448211042"><a name="p3586448211042"></a><a name="p3586448211042"></a>Use a valid AS configuration name.</p>
</td>
</tr>
<tr id="row54554745164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p2605813310457"><a name="p2605813310457"></a><a name="p2605813310457"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p56858245164955"><a name="p56858245164955"></a><a name="p56858245164955"></a>AS.1024</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p42115166164955"><a name="p42115166164955"></a><a name="p42115166164955"></a>The number of AS configurations exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p5474975173036"><a name="p5474975173036"></a><a name="p5474975173036"></a>The number of AS configurations exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p3985928311042"><a name="p3985928311042"></a><a name="p3985928311042"></a>Delete idle AS configurations or apply for a higher quota.</p>
</td>
</tr>
<tr id="row43492179164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p457106110457"><a name="p457106110457"></a><a name="p457106110457"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p33205577164955"><a name="p33205577164955"></a><a name="p33205577164955"></a>AS.1025</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p5297216164955"><a name="p5297216164955"></a><a name="p5297216164955"></a>The user login mode in the AS configuration is not unique.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p31833868173036"><a name="p31833868173036"></a><a name="p31833868173036"></a>The user login mode in the AS configuration is not unique.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p6638836711042"><a name="p6638836711042"></a><a name="p6638836711042"></a>Use account-and-password or key-pair login mode only.</p>
</td>
</tr>
<tr id="row47674947164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p4396951010457"><a name="p4396951010457"></a><a name="p4396951010457"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p36465502164955"><a name="p36465502164955"></a><a name="p36465502164955"></a>AS.1026</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p915661164955"><a name="p915661164955"></a><a name="p915661164955"></a>The user login mode in the AS configuration is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p54332251173036"><a name="p54332251173036"></a><a name="p54332251173036"></a>The user login mode in the AS configuration is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1544312491102"><a name="p1544312491102"></a><a name="p1544312491102"></a>Enter a valid <strong id="b1199616526304"><a name="b1199616526304"></a><a name="b1199616526304"></a>key_name</strong> value.</p>
</td>
</tr>
<tr id="row8240952164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p4284489110457"><a name="p4284489110457"></a><a name="p4284489110457"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p63537345164955"><a name="p63537345164955"></a><a name="p63537345164955"></a>AS.1027</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p46251282164955"><a name="p46251282164955"></a><a name="p46251282164955"></a>The user AS configuration is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p13981630173036"><a name="p13981630173036"></a><a name="p13981630173036"></a>The scaling config personality is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p2204767811042"><a name="p2204767811042"></a><a name="p2204767811042"></a>Enter a valid <strong id="b1129105511304"><a name="b1129105511304"></a><a name="b1129105511304"></a>personality</strong> value.</p>
</td>
</tr>
<tr id="row13608357164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p38369144104546"><a name="p38369144104546"></a><a name="p38369144104546"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p28535158164955"><a name="p28535158164955"></a><a name="p28535158164955"></a>AS.1028</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p29646500164955"><a name="p29646500164955"></a><a name="p29646500164955"></a>The disk in the AS configuration is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p59170160173036"><a name="p59170160173036"></a><a name="p59170160173036"></a>The disk in the AS configuration is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p3373908611042"><a name="p3373908611042"></a><a name="p3373908611042"></a>Enter a valid <strong id="b656455733010"><a name="b656455733010"></a><a name="b656455733010"></a>disk</strong> value.</p>
</td>
</tr>
<tr id="row65491913164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p53819111104546"><a name="p53819111104546"></a><a name="p53819111104546"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p3244749164955"><a name="p3244749164955"></a><a name="p3244749164955"></a>AS.1029</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p61498080164955"><a name="p61498080164955"></a><a name="p61498080164955"></a>The number of system disks in the AS configuration is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p51156340173036"><a name="p51156340173036"></a><a name="p51156340173036"></a>The number of system disks in the AS configuration is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p3394973311042"><a name="p3394973311042"></a><a name="p3394973311042"></a>Ensure that there is only one system disk.</p>
</td>
</tr>
<tr id="row16611816164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p42555754104546"><a name="p42555754104546"></a><a name="p42555754104546"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p3379864164955"><a name="p3379864164955"></a><a name="p3379864164955"></a>AS.1030</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p5333548164955"><a name="p5333548164955"></a><a name="p5333548164955"></a>The size of the system disk in the AS configuration is smaller than the requirement.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p47552854173036"><a name="p47552854173036"></a><a name="p47552854173036"></a>The size of the system disk in the AS configuration is less than the specification required.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p5329370211042"><a name="p5329370211042"></a><a name="p5329370211042"></a>Use a proper system disk size.</p>
</td>
</tr>
<tr id="row48001935164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p18849852104546"><a name="p18849852104546"></a><a name="p18849852104546"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p62951541164955"><a name="p62951541164955"></a><a name="p62951541164955"></a>AS.1031</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p65910067164955"><a name="p65910067164955"></a><a name="p65910067164955"></a>The size of the disk in the AS configuration is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p37856743173036"><a name="p37856743173036"></a><a name="p37856743173036"></a>The size of the disk in the AS configuration is not correct.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p6218578811042"><a name="p6218578811042"></a><a name="p6218578811042"></a>Use a proper disk size.</p>
</td>
</tr>
<tr id="row56319699164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p51334240104546"><a name="p51334240104546"></a><a name="p51334240104546"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p65601802164955"><a name="p65601802164955"></a><a name="p65601802164955"></a>AS.1032</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p12145708164955"><a name="p12145708164955"></a><a name="p12145708164955"></a>The number of disks in the AS configuration exceeds 24.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p8631533173911"><a name="p8631533173911"></a><a name="p8631533173911"></a>The ECS type [%s] in the AS configuration do not support 24 disks.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p3495689111042"><a name="p3495689111042"></a><a name="p3495689111042"></a>Ensure that the number of disks does not exceed the limit.</p>
</td>
</tr>
<tr id="row42202514164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p43024226104546"><a name="p43024226104546"></a><a name="p43024226104546"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p62960450164955"><a name="p62960450164955"></a><a name="p62960450164955"></a>AS.1033</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p66631699164955"><a name="p66631699164955"></a><a name="p66631699164955"></a>The <strong>volumeType</strong> of the disk in the AS configuration is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p59243342173036"><a name="p59243342173036"></a><a name="p59243342173036"></a>Parameter volumeType in the AS configuration is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4931430011042"><a name="p4931430011042"></a><a name="p4931430011042"></a>Use a valid <strong id="b1650403917320"><a name="b1650403917320"></a><a name="b1650403917320"></a>volume_type</strong> value.</p>
</td>
</tr>
<tr id="row62814383164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p24821267104546"><a name="p24821267104546"></a><a name="p24821267104546"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p54800276164955"><a name="p54800276164955"></a><a name="p54800276164955"></a>AS.1034</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p9637357164955"><a name="p9637357164955"></a><a name="p9637357164955"></a>The <strong>diskType</strong> in the AS configuration is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p37397234173036"><a name="p37397234173036"></a><a name="p37397234173036"></a>Parameter diskType in the AS configuration is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4688307611042"><a name="p4688307611042"></a><a name="p4688307611042"></a>Use a valid <strong id="b1463064314326"><a name="b1463064314326"></a><a name="b1463064314326"></a>disk_type</strong> value.</p>
</td>
</tr>
<tr id="row19627353164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p42419535104546"><a name="p42419535104546"></a><a name="p42419535104546"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p46311740164955"><a name="p46311740164955"></a><a name="p46311740164955"></a>AS.1035</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p60263431164955"><a name="p60263431164955"></a><a name="p60263431164955"></a>The password in the AS configuration fails to meet the complexity requirements.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p16385122173036"><a name="p16385122173036"></a><a name="p16385122173036"></a>Parameter adminPass in the AS configuration is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1935100511042"><a name="p1935100511042"></a><a name="p1935100511042"></a>Use passwords that meet complexity requirements.</p>
</td>
</tr>
<tr id="row5499971164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p53764282104546"><a name="p53764282104546"></a><a name="p53764282104546"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p42844543164955"><a name="p42844543164955"></a><a name="p42844543164955"></a>AS.1036</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p47855926164955"><a name="p47855926164955"></a><a name="p47855926164955"></a>The memory of 32-bit OS exceeds 4 GB.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p185489114013"><a name="p185489114013"></a><a name="p185489114013"></a>32-bit operating system (OS) does not support the specification [%s] with 4G memory.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1402143411042"><a name="p1402143411042"></a><a name="p1402143411042"></a>Change the image or the policy.</p>
</td>
</tr>
<tr id="row55424671152313"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p2585470104546"><a name="p2585470104546"></a><a name="p2585470104546"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p60213357152313"><a name="p60213357152313"></a><a name="p60213357152313"></a>AS.1038</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p45443752152313"><a name="p45443752152313"></a><a name="p45443752152313"></a>Deleting AS configurations in batches fails.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p15164506173036"><a name="p15164506173036"></a><a name="p15164506173036"></a>Batch deleting the AS configuration failed.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p2107823011042"><a name="p2107823011042"></a><a name="p2107823011042"></a>If this error code is returned, use parameter <strong id="b11128225335"><a name="b11128225335"></a><a name="b11128225335"></a>Message</strong> to obtain the configuration ID and the failure cause.</p>
</td>
</tr>
<tr id="row6256512215237"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p5759758104546"><a name="p5759758104546"></a><a name="p5759758104546"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p3461016015237"><a name="p3461016015237"></a><a name="p3461016015237"></a>AS.1039</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p5195958615237"><a name="p5195958615237"></a><a name="p5195958615237"></a>The number of AS configurations to be deleted in batches exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p49071600173036"><a name="p49071600173036"></a><a name="p49071600173036"></a>The number of AS configurations is beyond the maximum limit.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p6520888411042"><a name="p6520888411042"></a><a name="p6520888411042"></a>Delete a maximum of 50 AS configurations at a time.</p>
</td>
</tr>
<tr id="row1446242771614"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p19274140121614"><a name="p19274140121614"></a><a name="p19274140121614"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p14274124015167"><a name="p14274124015167"></a><a name="p14274124015167"></a>AS.1040</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p5274540121615"><a name="p5274540121615"></a><a name="p5274540121615"></a>The AS configuration list is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p12631638201316"><a name="p12631638201316"></a><a name="p12631638201316"></a>The list of AS config to be deleted is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1226363817132"><a name="p1226363817132"></a><a name="p1226363817132"></a>Add the IDs of the AS configurations to be deleted in batches.</p>
</td>
</tr>
<tr id="row1436533115133"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p82628383134"><a name="p82628383134"></a><a name="p82628383134"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p12628385130"><a name="p12628385130"></a><a name="p12628385130"></a>AS.1041</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p182631738141318"><a name="p182631738141318"></a><a name="p182631738141318"></a>The <strong id="b26621657163313"><a name="b26621657163313"></a><a name="b26621657163313"></a>eip</strong> field in the <strong id="b46631457143318"><a name="b46631457143318"></a><a name="b46631457143318"></a>public_ip</strong> field is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p2865111101418"><a name="p2865111101418"></a><a name="p2865111101418"></a>The eip info of scaling config is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1994119482151"><a name="p1994119482151"></a><a name="p1994119482151"></a>Ensure that the <strong id="b10981577342"><a name="b10981577342"></a><a name="b10981577342"></a>eip</strong> field is not empty when specifying the <strong id="b1992763412"><a name="b1992763412"></a><a name="b1992763412"></a>public_ip</strong> field.</p>
</td>
</tr>
<tr id="row165231611185510"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p145361014135510"><a name="p145361014135510"></a><a name="p145361014135510"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p165551314135514"><a name="p165551314135514"></a><a name="p165551314135514"></a>AS.1042</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p17573121418559"><a name="p17573121418559"></a><a name="p17573121418559"></a>The bandwidth size is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p1588181415517"><a name="p1588181415517"></a><a name="p1588181415517"></a>The bandwidth size of eip is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p960317146556"><a name="p960317146556"></a><a name="p960317146556"></a>Enter a valid bandwidth.</p>
</td>
</tr>
<tr id="row09094192177"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p158126101719"><a name="p158126101719"></a><a name="p158126101719"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p17810266177"><a name="p17810266177"></a><a name="p17810266177"></a>AS.1043</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p662733151712"><a name="p662733151712"></a><a name="p662733151712"></a>The EIP type is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p116261531191712"><a name="p116261531191712"></a><a name="p116261531191712"></a>The eip type of scaling config is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p20605831171719"><a name="p20605831171719"></a><a name="p20605831171719"></a>Use a valid EIP type.</p>
</td>
</tr>
<tr id="row6782754132418"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p729318292516"><a name="p729318292516"></a><a name="p729318292516"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p82933272519"><a name="p82933272519"></a><a name="p82933272519"></a>AS.1044</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p191053714253"><a name="p191053714253"></a><a name="p191053714253"></a>The bandwidth billing model of the AS configuration is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p510447112514"><a name="p510447112514"></a><a name="p510447112514"></a>The bandwidth charging mode of eip is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p410397142512"><a name="p410397142512"></a><a name="p410397142512"></a>Use a valid bandwidth billing model.</p>
</td>
</tr>
<tr id="row15847191485118"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p78481514105114"><a name="p78481514105114"></a><a name="p78481514105114"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p7848214145112"><a name="p7848214145112"></a><a name="p7848214145112"></a>AS.1045</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p0848141411519"><a name="p0848141411519"></a><a name="p0848141411519"></a>The bandwidth type is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p78481914175116"><a name="p78481914175116"></a><a name="p78481914175116"></a>The bandwidth type of eip is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p28481814135118"><a name="p28481814135118"></a><a name="p28481814135118"></a>Use a valid bandwidth.</p>
</td>
</tr>
<tr id="row102279581257"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p152271258154"><a name="p152271258154"></a><a name="p152271258154"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p75972262063"><a name="p75972262063"></a><a name="p75972262063"></a>AS.1046</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p72272581952"><a name="p72272581952"></a><a name="p72272581952"></a>The bandwidth size is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p1322719583510"><a name="p1322719583510"></a><a name="p1322719583510"></a>The bandwidth size of eip is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p72272581513"><a name="p72272581513"></a><a name="p72272581513"></a>Add the bandwidth value of the AS configuration.</p>
</td>
</tr>
<tr id="row34739717135821"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p10345517104645"><a name="p10345517104645"></a><a name="p10345517104645"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p62453698135821"><a name="p62453698135821"></a><a name="p62453698135821"></a>AS.1049</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p25584796135821"><a name="p25584796135821"></a><a name="p25584796135821"></a>Parameter <strong id="b84235270616830"><a name="b84235270616830"></a><a name="b84235270616830"></a>userdata</strong> in the AS configuration is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p4172527173036"><a name="p4172527173036"></a><a name="p4172527173036"></a>Parameter userdata in the AS configuration is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p2420105511042"><a name="p2420105511042"></a><a name="p2420105511042"></a>Use a valid <strong id="b1071914357406"><a name="b1071914357406"></a><a name="b1071914357406"></a>userdata</strong>.</p>
</td>
</tr>
<tr id="row4862426114011"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p25689377104645"><a name="p25689377104645"></a><a name="p25689377104645"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p4625105714011"><a name="p4625105714011"></a><a name="p4625105714011"></a>AS.1050</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p5534809714011"><a name="p5534809714011"></a><a name="p5534809714011"></a>The user login mode in the AS configuration is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p21873520173036"><a name="p21873520173036"></a><a name="p21873520173036"></a>The user login mode in the AS configuration is illegal.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p6004727511042"><a name="p6004727511042"></a><a name="p6004727511042"></a>Use a valid login mode.</p>
</td>
</tr>
<tr id="row5936170614048"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p4182789104645"><a name="p4182789104645"></a><a name="p4182789104645"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p4356888214048"><a name="p4356888214048"></a><a name="p4356888214048"></a>AS.1052</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p3941856714048"><a name="p3941856714048"></a><a name="p3941856714048"></a>The <strong id="b8423527061690"><a name="b8423527061690"></a><a name="b8423527061690"></a>metadata</strong> in the AS configuration is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p40995928173036"><a name="p40995928173036"></a><a name="p40995928173036"></a>Parameter metadata in the AS configuration is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1948427311042"><a name="p1948427311042"></a><a name="p1948427311042"></a>Use a valid <strong id="b372011863185133"><a name="b372011863185133"></a><a name="b372011863185133"></a>metadata</strong>, whose maximum length is 512 bytes and the <strong id="b869442758185514"><a name="b869442758185514"></a><a name="b869442758185514"></a>key</strong> value cannot contain spaces, $, or periods(.).</p>
</td>
</tr>
<tr id="row9130979155136"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p29354894104645"><a name="p29354894104645"></a><a name="p29354894104645"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p1411798155136"><a name="p1411798155136"></a><a name="p1411798155136"></a>AS.1053</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p47246851155136"><a name="p47246851155136"></a><a name="p47246851155136"></a>The data image in the AS configuration is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p22587409173036"><a name="p22587409173036"></a><a name="p22587409173036"></a>The data image is not available.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4645704195613"><a name="p4645704195613"></a><a name="p4645704195613"></a>Use a valid data image.</p>
</td>
</tr>
<tr id="row50821955155140"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p59099510104645"><a name="p59099510104645"></a><a name="p59099510104645"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p22937714155140"><a name="p22937714155140"></a><a name="p22937714155140"></a>AS.1054</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p46015541155140"><a name="p46015541155140"></a><a name="p46015541155140"></a>The size of the data disk in the AS configuration is smaller than what the data image requires.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p24549710173036"><a name="p24549710173036"></a><a name="p24549710173036"></a>The size of the data disk in the AS configuration is less than the data image required.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1558944512569"><a name="p1558944512569"></a><a name="p1558944512569"></a>Use a proper data disk.</p>
</td>
</tr>
<tr id="row13893503155230"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p66761536104645"><a name="p66761536104645"></a><a name="p66761536104645"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p51631940155230"><a name="p51631940155230"></a><a name="p51631940155230"></a>AS.1055</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p21437626155230"><a name="p21437626155230"></a><a name="p21437626155230"></a>A data disk image cannot be used to create a system disk.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p45780938173036"><a name="p45780938173036"></a><a name="p45780938173036"></a>The system disk is not support to data image.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p44447217195613"><a name="p44447217195613"></a><a name="p44447217195613"></a>Refer to the error code description.</p>
</td>
</tr>
<tr id="row63191809155212"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p33311140104711"><a name="p33311140104711"></a><a name="p33311140104711"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p18262924155212"><a name="p18262924155212"></a><a name="p18262924155212"></a>AS.1056</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p2901888155212"><a name="p2901888155212"></a><a name="p2901888155212"></a>The data image in the AS configuration does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p21198600173036"><a name="p21198600173036"></a><a name="p21198600173036"></a>The data image in the AS configuration does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p66080536195613"><a name="p66080536195613"></a><a name="p66080536195613"></a>Use a valid data image ID.</p>
</td>
</tr>
<tr id="row60148552155234"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p57521351104711"><a name="p57521351104711"></a><a name="p57521351104711"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p40194548155234"><a name="p40194548155234"></a><a name="p40194548155234"></a>AS.1057</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p34532952155234"><a name="p34532952155234"></a><a name="p34532952155234"></a>The selected DSS device is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p69931823165813"><a name="p69931823165813"></a><a name="p69931823165813"></a>The DSS of the disk in the AS configuration is not available.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p27795966195613"><a name="p27795966195613"></a><a name="p27795966195613"></a>Use a correct DSS device.</p>
</td>
</tr>
<tr id="row3102048155227"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p57133789104711"><a name="p57133789104711"></a><a name="p57133789104711"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p49939316155227"><a name="p49939316155227"></a><a name="p49939316155227"></a>AS.1058</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p18552789155227"><a name="p18552789155227"></a><a name="p18552789155227"></a>The selected DSS device does not support the disk type.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p39098175173036"><a name="p39098175173036"></a><a name="p39098175173036"></a>The type of dss in the AS configuration is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p48628945195613"><a name="p48628945195613"></a><a name="p48628945195613"></a>Change the DSS device or disk type.</p>
</td>
</tr>
<tr id="row1760394115528"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p43037220104711"><a name="p43037220104711"></a><a name="p43037220104711"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p1663308715528"><a name="p1663308715528"></a><a name="p1663308715528"></a>AS.1059</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p510278915528"><a name="p510278915528"></a><a name="p510278915528"></a>The storage space on the selected DSS device is insufficient.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p48411365173036"><a name="p48411365173036"></a><a name="p48411365173036"></a>The capacity of dss in the AS configuration is not enough.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p58235720195613"><a name="p58235720195613"></a><a name="p58235720195613"></a>Change the DSS device.</p>
</td>
</tr>
<tr id="row17727518155220"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p34293916104711"><a name="p34293916104711"></a><a name="p34293916104711"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p26642866155220"><a name="p26642866155220"></a><a name="p26642866155220"></a>AS.1060</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p10588501155220"><a name="p10588501155220"></a><a name="p10588501155220"></a>You can use either DSS or EVS disks in an AS configuration.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p59732010173036"><a name="p59732010173036"></a><a name="p59732010173036"></a>DSS and EVS are used together in the AS configuration.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p20542051195613"><a name="p20542051195613"></a><a name="p20542051195613"></a>Refer to the error code description.</p>
</td>
</tr>
<tr id="row18044691155224"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p35767505104711"><a name="p35767505104711"></a><a name="p35767505104711"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p52333876155224"><a name="p52333876155224"></a><a name="p52333876155224"></a>AS.1061</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p11185565155224"><a name="p11185565155224"></a><a name="p11185565155224"></a>The selected DSS devices must be in the same AZ.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p58091704173036"><a name="p58091704173036"></a><a name="p58091704173036"></a>The DSS does not belong to the same AZ in the AS configuration.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p32258636195633"><a name="p32258636195633"></a><a name="p32258636195633"></a>Change DSS devices so that they are in the same AZ.</p>
</td>
</tr>
<tr id="row62357829171212"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p17819395171212"><a name="p17819395171212"></a><a name="p17819395171212"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p34084930171212"><a name="p34084930171212"></a><a name="p34084930171212"></a>AS.1062</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p9415978171212"><a name="p9415978171212"></a><a name="p9415978171212"></a>The number of disks with snapshot IDs in the AS configuration is different from that of EVS disks specified in the full-ECS image.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p24496738171212"><a name="p24496738171212"></a><a name="p24496738171212"></a>The number of EVS disks with snapshot IDs in the AS configuration is different from that of EVS disks specified in the full-ECS image.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p38078738171212"><a name="p38078738171212"></a><a name="p38078738171212"></a>Refer to the error code description.</p>
</td>
</tr>
<tr id="row40133793171216"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p29611797171216"><a name="p29611797171216"></a><a name="p29611797171216"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p49745386171216"><a name="p49745386171216"></a><a name="p49745386171216"></a>AS.1063</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p2844488171216"><a name="p2844488171216"></a><a name="p2844488171216"></a>The disk data backup in a full-ECS image is used to restore the disk in DSS.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p29076950171216"><a name="p29076950171216"></a><a name="p29076950171216"></a>The disk data backup in a full-ECS image cannot be used to restore the disk in DSS.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p6422716171216"><a name="p6422716171216"></a><a name="p6422716171216"></a>Refer to the error code description.</p>
</td>
</tr>
<tr id="row12435259171219"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p623097171219"><a name="p623097171219"></a><a name="p623097171219"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p50470907171219"><a name="p50470907171219"></a><a name="p50470907171219"></a>AS.1064</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p61611690171219"><a name="p61611690171219"></a><a name="p61611690171219"></a>Your selected data disk will recover from the disk backup in the full-ECS image, and data mirroring is unavailable now.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p24490989171219"><a name="p24490989171219"></a><a name="p24490989171219"></a>The data disk you have selected will be restored using the disk data backup in the full-ECS image. Then, data mirroring will be unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p37613101171219"><a name="p37613101171219"></a><a name="p37613101171219"></a>Refer to the error code description.</p>
</td>
</tr>
<tr id="row18780559171228"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p44830283171228"><a name="p44830283171228"></a><a name="p44830283171228"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p7374332171228"><a name="p7374332171228"></a><a name="p7374332171228"></a>AS.1065</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p60450058171228"><a name="p60450058171228"></a><a name="p60450058171228"></a>The VMs in the AS configuration do not belong to the same AZ.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p64616540171228"><a name="p64616540171228"></a><a name="p64616540171228"></a>ECS resources specified in the AS configuration belong to different AZs.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p66557275171228"><a name="p66557275171228"></a><a name="p66557275171228"></a>Use ECS resources (specifications, images, disk) in the same AZ.</p>
</td>
</tr>
<tr id="row17333839171223"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p61863685171223"><a name="p61863685171223"></a><a name="p61863685171223"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p44902588171223"><a name="p44902588171223"></a><a name="p44902588171223"></a>AS.1066</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p13231003171223"><a name="p13231003171223"></a><a name="p13231003171223"></a>The AS configuration contains EVS disks with invalid snapshot IDs.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p65078347171223"><a name="p65078347171223"></a><a name="p65078347171223"></a>The AS configuration contains EVS disks with invalid snapshot IDs.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p36854772171223"><a name="p36854772171223"></a><a name="p36854772171223"></a>Use a correct snapshot ID. </p>
</td>
</tr>
<tr id="row64831959151819"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p18483185915188"><a name="p18483185915188"></a><a name="p18483185915188"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p151181115151913"><a name="p151181115151913"></a><a name="p151181115151913"></a>AS.1067</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p348395941818"><a name="p348395941818"></a><a name="p348395941818"></a>Parameter <strong id="b158651356114219"><a name="b158651356114219"></a><a name="b158651356114219"></a>offset</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p6483959101816"><a name="p6483959101816"></a><a name="p6483959101816"></a>The value of parameter Offset number is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p14636194317578"><a name="p14636194317578"></a><a name="p14636194317578"></a>Use a valid <strong id="b12616161161310"><a name="b12616161161310"></a><a name="b12616161161310"></a>offset</strong> value.</p>
</td>
</tr>
<tr id="row44491256142614"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p2583133320271"><a name="p2583133320271"></a><a name="p2583133320271"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p960073313272"><a name="p960073313272"></a><a name="p960073313272"></a>AS.1074</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p13365171413201"><a name="p13365171413201"></a><a name="p13365171413201"></a>Parameter <strong id="b195731624518"><a name="b195731624518"></a><a name="b195731624518"></a>marker</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p24491556162616"><a name="p24491556162616"></a><a name="p24491556162616"></a>The value of parameter Marker is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p11449165610262"><a name="p11449165610262"></a><a name="p11449165610262"></a>Use a valid <strong id="b20842172054610"><a name="b20842172054610"></a><a name="b20842172054610"></a>marker</strong> value.</p>
</td>
</tr>
<tr id="row1882150152712"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p11935123413271"><a name="p11935123413271"></a><a name="p11935123413271"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p4948133417274"><a name="p4948133417274"></a><a name="p4948133417274"></a>AS.1075</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p088210015274"><a name="p088210015274"></a><a name="p088210015274"></a>Image ID in the AS configuration is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p1288220192718"><a name="p1288220192718"></a><a name="p1288220192718"></a>The image ID is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p388270162711"><a name="p388270162711"></a><a name="p388270162711"></a>Use a correct image ID. </p>
</td>
</tr>
<tr id="row451093514415"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p10127439184115"><a name="p10127439184115"></a><a name="p10127439184115"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p10127153917418"><a name="p10127153917418"></a><a name="p10127153917418"></a>AS.1085</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p18127173934117"><a name="p18127173934117"></a><a name="p18127173934117"></a>The priority policy used in multi-flavor AS configuration is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p81271239204110"><a name="p81271239204110"></a><a name="p81271239204110"></a>Invalid multi flavor priority policy.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p41272391417"><a name="p41272391417"></a><a name="p41272391417"></a>Use a valid <strong id="b1113616590507"><a name="b1113616590507"></a><a name="b1113616590507"></a>multi_flavor_priority_policy</strong> value.</p>
</td>
</tr>
<tr id="row1917708174220"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p7458102664215"><a name="p7458102664215"></a><a name="p7458102664215"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p245862684220"><a name="p245862684220"></a><a name="p245862684220"></a>AS.1086</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p1245882644217"><a name="p1245882644217"></a><a name="p1245882644217"></a>The AS configuration is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p8458126164212"><a name="p8458126164212"></a><a name="p8458126164212"></a>AS configuration is not available for AS group</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4458122612425"><a name="p4458122612425"></a><a name="p4458122612425"></a>Replace the AS configuration in the AS group.</p>
</td>
</tr>
<tr id="row1368651574214"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1523910318429"><a name="p1523910318429"></a><a name="p1523910318429"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p142391531124216"><a name="p142391531124216"></a><a name="p142391531124216"></a>AS.1087</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p92398318425"><a name="p92398318425"></a><a name="p92398318425"></a>The number of flavors in the AS configuration reaches the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p20239931174217"><a name="p20239931174217"></a><a name="p20239931174217"></a>The number of flavors in the AS config exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1239931204218"><a name="p1239931204218"></a><a name="p1239931204218"></a>Ensure that the number of flavors in the AS configuration does not exceed the upper limit.</p>
</td>
</tr>
<tr id="row893418122426"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p44801386425"><a name="p44801386425"></a><a name="p44801386425"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p17480173834213"><a name="p17480173834213"></a><a name="p17480173834213"></a>AS.1088</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p848043874219"><a name="p848043874219"></a><a name="p848043874219"></a>The image in the AS configuration is not available in the AZ of the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p14480838194214"><a name="p14480838194214"></a><a name="p14480838194214"></a>The image in the AS configuration you selected is unavailable for the AZ [%s] in AS group</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p948073844217"><a name="p948073844217"></a><a name="p948073844217"></a>Change another AS configuration or AZ for the AS group.</p>
</td>
</tr>
<tr id="row15179123772913"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p44951741122917"><a name="p44951741122917"></a><a name="p44951741122917"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p349554113298"><a name="p349554113298"></a><a name="p349554113298"></a>AS.1090</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p1880610110309"><a name="p1880610110309"></a><a name="p1880610110309"></a>The selected flavor is incompatible with the image architecture.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p0357912103019"><a name="p0357912103019"></a><a name="p0357912103019"></a>Flavor {0} in the AS configuration is incompatible with the image architecture.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1649512413293"><a name="p1649512413293"></a><a name="p1649512413293"></a>Ensure that the selected flavor is compatible with the image architecture.</p>
</td>
</tr>
<tr id="row28498644164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p36088124104728"><a name="p36088124104728"></a><a name="p36088124104728"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p26688852164955"><a name="p26688852164955"></a><a name="p26688852164955"></a>AS.2002</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p14313421164955"><a name="p14313421164955"></a><a name="p14313421164955"></a>The AS group name is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p3159170173036"><a name="p3159170173036"></a><a name="p3159170173036"></a>The name of the AS group is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p37199673195633"><a name="p37199673195633"></a><a name="p37199673195633"></a>Add an AS group name.</p>
</td>
</tr>
<tr id="row61711926164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1567857104728"><a name="p1567857104728"></a><a name="p1567857104728"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p32610070164955"><a name="p32610070164955"></a><a name="p32610070164955"></a>AS.2003</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p24169986164955"><a name="p24169986164955"></a><a name="p24169986164955"></a>The AS group name is too long.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p21333635173036"><a name="p21333635173036"></a><a name="p21333635173036"></a>The AS group name is too long.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p65031837195633"><a name="p65031837195633"></a><a name="p65031837195633"></a>Use an AS group name of proper length.</p>
</td>
</tr>
<tr id="row16203289164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p2117430104728"><a name="p2117430104728"></a><a name="p2117430104728"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p37398019164955"><a name="p37398019164955"></a><a name="p37398019164955"></a>AS.2004</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p9340718164955"><a name="p9340718164955"></a><a name="p9340718164955"></a>The maximum or minimum number of instances is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p50072446173036"><a name="p50072446173036"></a><a name="p50072446173036"></a>Invalid min or max number of instances in the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p336712175820"><a name="p336712175820"></a><a name="p336712175820"></a>Enter correct maximum/minimum number of instances for the AS group.</p>
</td>
</tr>
<tr id="row16957603164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p103271104728"><a name="p103271104728"></a><a name="p103271104728"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p31388626164955"><a name="p31388626164955"></a><a name="p31388626164955"></a>AS.2005</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p59450773164955"><a name="p59450773164955"></a><a name="p59450773164955"></a>The expected number of instances in the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p62700222173036"><a name="p62700222173036"></a><a name="p62700222173036"></a>The expected number cannot be less than the minimum number of instances or greater than the maximum number of instances.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p8917114825810"><a name="p8917114825810"></a><a name="p8917114825810"></a>Enter a valid number of expected instances for the AS group.</p>
</td>
</tr>
<tr id="row65294914164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p8176038104728"><a name="p8176038104728"></a><a name="p8176038104728"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p54396671164955"><a name="p54396671164955"></a><a name="p54396671164955"></a>AS.2006</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p44054212164955"><a name="p44054212164955"></a><a name="p44054212164955"></a>The cooldown period in the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p7325911173036"><a name="p7325911173036"></a><a name="p7325911173036"></a>Invalid cooldown period of the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p9101195211595"><a name="p9101195211595"></a><a name="p9101195211595"></a>Enter a valid cooldown period for the AS group.</p>
</td>
</tr>
<tr id="row60943594164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p54751773104728"><a name="p54751773104728"></a><a name="p54751773104728"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p37484047164955"><a name="p37484047164955"></a><a name="p37484047164955"></a>AS.2007</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p16308944164955"><a name="p16308944164955"></a><a name="p16308944164955"></a>The AS group does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p38988898173036"><a name="p38988898173036"></a><a name="p38988898173036"></a>The AS group does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p11283991195633"><a name="p11283991195633"></a><a name="p11283991195633"></a>Use a correct AS group ID.</p>
</td>
</tr>
<tr id="row12562775164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p51377985104728"><a name="p51377985104728"></a><a name="p51377985104728"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p10951887164955"><a name="p10951887164955"></a><a name="p10951887164955"></a>AS.2008</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p14687639164955"><a name="p14687639164955"></a><a name="p14687639164955"></a>The execution action of the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p35857604173036"><a name="p35857604173036"></a><a name="p35857604173036"></a>Invalid execution action of the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p141119183013"><a name="p141119183013"></a><a name="p141119183013"></a>Use a correct scaling action for the AS group.</p>
</td>
</tr>
<tr id="row65079888164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p738594510483"><a name="p738594510483"></a><a name="p738594510483"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p36979604164955"><a name="p36979604164955"></a><a name="p36979604164955"></a>AS.2009</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p42557948164955"><a name="p42557948164955"></a><a name="p42557948164955"></a>The AS group ID is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p34845415173036"><a name="p34845415173036"></a><a name="p34845415173036"></a>The AS group ID is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p67048654195640"><a name="p67048654195640"></a><a name="p67048654195640"></a>Add an AS group ID.</p>
</td>
</tr>
<tr id="row36956356104417"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1564496810483"><a name="p1564496810483"></a><a name="p1564496810483"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p40674877104417"><a name="p40674877104417"></a><a name="p40674877104417"></a>AS.2010</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p6330710104417"><a name="p6330710104417"></a><a name="p6330710104417"></a>The expected number of instances in the AS group cannot be smaller than the number of instances for which instance protection has been configured.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p35156989173036"><a name="p35156989173036"></a><a name="p35156989173036"></a>The expected number of instances in the AS group cannot be smaller than the number of instances for which instance protection has been configured.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p729184520016"><a name="p729184520016"></a><a name="p729184520016"></a>Ensure that the number of expected instances is no less than the protected instances, or change the expected number of instances after canceling instance protection.</p>
</td>
</tr>
<tr id="row51778985141828"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p6378414710483"><a name="p6378414710483"></a><a name="p6378414710483"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p33348219141828"><a name="p33348219141828"></a><a name="p33348219141828"></a>AS.2011</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p16851234141828"><a name="p16851234141828"></a><a name="p16851234141828"></a>The AZ in the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p60968516173036"><a name="p60968516173036"></a><a name="p60968516173036"></a>Invalid AZ in AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p2208324511042"><a name="p2208324511042"></a><a name="p2208324511042"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row61517544164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p5930943510483"><a name="p5930943510483"></a><a name="p5930943510483"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p16865164164955"><a name="p16865164164955"></a><a name="p16865164164955"></a>AS.2012</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p23901073164955"><a name="p23901073164955"></a><a name="p23901073164955"></a>The VPC of the AS group does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p19980220173036"><a name="p19980220173036"></a><a name="p19980220173036"></a>The VPC of the AS group does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p5966773611042"><a name="p5966773611042"></a><a name="p5966773611042"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row13783071164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1847034910483"><a name="p1847034910483"></a><a name="p1847034910483"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p42687000164955"><a name="p42687000164955"></a><a name="p42687000164955"></a>AS.2013</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p35094981164955"><a name="p35094981164955"></a><a name="p35094981164955"></a>Parameter <strong id="b842352706152923"><a name="b842352706152923"></a><a name="b842352706152923"></a>networks</strong> in the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p5745810410028"><a name="p5745810410028"></a><a name="p5745810410028"></a>Parameter <strong id="b842352706152934"><a name="b842352706152934"></a><a name="b842352706152934"></a>networks</strong> in the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1123633411042"><a name="p1123633411042"></a><a name="p1123633411042"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row47419379164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p4311212310483"><a name="p4311212310483"></a><a name="p4311212310483"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p15764490164955"><a name="p15764490164955"></a><a name="p15764490164955"></a>AS.2014</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p1855305164955"><a name="p1855305164955"></a><a name="p1855305164955"></a>The security group of the AS group does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p8199606173036"><a name="p8199606173036"></a><a name="p8199606173036"></a>The security group of the AS group does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p400613611042"><a name="p400613611042"></a><a name="p400613611042"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row37393475143929"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p5963483104829"><a name="p5963483104829"></a><a name="p5963483104829"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p8972616143929"><a name="p8972616143929"></a><a name="p8972616143929"></a>AS.2015</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p1229639171416"><a name="p1229639171416"></a><a name="p1229639171416"></a>The load balancer listener of the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p172968961410"><a name="p172968961410"></a><a name="p172968961410"></a>Parameter listenerId in the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p112963971417"><a name="p112963971417"></a><a name="p112963971417"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row62102541145334"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p52412495104829"><a name="p52412495104829"></a><a name="p52412495104829"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p19729846145345"><a name="p19729846145345"></a><a name="p19729846145345"></a>AS.2016</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p54613709145345"><a name="p54613709145345"></a><a name="p54613709145345"></a>The VPC to which the ELB listener in the AS group belongs is different from the VPC in the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p27437094173036"><a name="p27437094173036"></a><a name="p27437094173036"></a>The listener of the AS group does not belong to the vpc.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p6352076811042"><a name="p6352076811042"></a><a name="p6352076811042"></a>Change the VPC ID or ELB listener ID.</p>
</td>
</tr>
<tr id="row16697752164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p23765866104829"><a name="p23765866104829"></a><a name="p23765866104829"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p10340647164955"><a name="p10340647164955"></a><a name="p10340647164955"></a>AS.2017</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p32286067164955"><a name="p32286067164955"></a><a name="p32286067164955"></a>The VPC ID in the AS group is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p28801421173036"><a name="p28801421173036"></a><a name="p28801421173036"></a>The ID of the VPC in the AS group is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p152396411042"><a name="p152396411042"></a><a name="p152396411042"></a>Add a VPC ID.</p>
</td>
</tr>
<tr id="row22139147164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p11230064104829"><a name="p11230064104829"></a><a name="p11230064104829"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p48440444164955"><a name="p48440444164955"></a><a name="p48440444164955"></a>AS.2018</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p31361886164955"><a name="p31361886164955"></a><a name="p31361886164955"></a>No AS is configured in the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p58270672173036"><a name="p58270672173036"></a><a name="p58270672173036"></a>No AS configuration is in the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p3722794411042"><a name="p3722794411042"></a><a name="p3722794411042"></a>Enable the AS group after adding an AS configuration to the AS group.</p>
</td>
</tr>
<tr id="row6616152154523"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p66146275154523"><a name="p66146275154523"></a><a name="p66146275154523"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p56248063154523"><a name="p56248063154523"></a><a name="p56248063154523"></a>AS.2019</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p59799251154523"><a name="p59799251154523"></a><a name="p59799251154523"></a>The value of the parameter that specifies whether to forcibly delete an AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p11901192154523"><a name="p11901192154523"></a><a name="p11901192154523"></a>The value of the parameter that specifies whether to forcibly delete an AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p24472518154523"><a name="p24472518154523"></a><a name="p24472518154523"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row13821520164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p66544170104829"><a name="p66544170104829"></a><a name="p66544170104829"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p45801374164955"><a name="p45801374164955"></a><a name="p45801374164955"></a>AS.2020</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p18923824164955"><a name="p18923824164955"></a><a name="p18923824164955"></a>The AS group status is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p66518388173036"><a name="p66518388173036"></a><a name="p66518388173036"></a>The scaling group status is illegal.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p2719071311042"><a name="p2719071311042"></a><a name="p2719071311042"></a>You are not allowed to perform the operation when the AS group is in the current status.</p>
</td>
</tr>
<tr id="row36096695164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p58100396104829"><a name="p58100396104829"></a><a name="p58100396104829"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p38151146164955"><a name="p38151146164955"></a><a name="p38151146164955"></a>AS.2021</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p3235159164955"><a name="p3235159164955"></a><a name="p3235159164955"></a>Deleting the AS group fails because there are instances in it.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p39305170173036"><a name="p39305170173036"></a><a name="p39305170173036"></a>The current number of instances in the AS group is not 0.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p2491543311042"><a name="p2491543311042"></a><a name="p2491543311042"></a>Before deleting the AS group, deleting its instances.</p>
</td>
</tr>
<tr id="row29116434164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p9496082104829"><a name="p9496082104829"></a><a name="p9496082104829"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p9620934164955"><a name="p9620934164955"></a><a name="p9620934164955"></a>AS.2022</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p41098183164955"><a name="p41098183164955"></a><a name="p41098183164955"></a>The AS group name contains invalid characters.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p65093391173036"><a name="p65093391173036"></a><a name="p65093391173036"></a>The AS group name contains invalid characters.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4395794711042"><a name="p4395794711042"></a><a name="p4395794711042"></a>Use a correct AS group name.</p>
</td>
</tr>
<tr id="row34339327164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p17919758104853"><a name="p17919758104853"></a><a name="p17919758104853"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p30022109164955"><a name="p30022109164955"></a><a name="p30022109164955"></a>AS.2023</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p15871804164955"><a name="p15871804164955"></a><a name="p15871804164955"></a>The number of AS groups exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p7115477173036"><a name="p7115477173036"></a><a name="p7115477173036"></a>The number of AS groups exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p3441593111042"><a name="p3441593111042"></a><a name="p3441593111042"></a>Delete idle AS groups or apply for a higher quota.</p>
</td>
</tr>
<tr id="row8628516164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p44384411104853"><a name="p44384411104853"></a><a name="p44384411104853"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p27821158164955"><a name="p27821158164955"></a><a name="p27821158164955"></a>AS.2024</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p38921341164955"><a name="p38921341164955"></a><a name="p38921341164955"></a>The number of subnets in the AS group exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p19800343173036"><a name="p19800343173036"></a><a name="p19800343173036"></a>The number of subnets in the AS group exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p32252451529"><a name="p32252451529"></a><a name="p32252451529"></a>Ensure that the number of subnets does not exceed the upper limit.</p>
</td>
</tr>
<tr id="row14747756164955"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p9763650104853"><a name="p9763650104853"></a><a name="p9763650104853"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p53717597164955"><a name="p53717597164955"></a><a name="p53717597164955"></a>AS.2025</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p56158102164955"><a name="p56158102164955"></a><a name="p56158102164955"></a>The number of security groups in the AS group exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p6044368173036"><a name="p6044368173036"></a><a name="p6044368173036"></a>The number of security groups in the AS group exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p5290818111042"><a name="p5290818111042"></a><a name="p5290818111042"></a>Ensure that the number of security groups does not exceed the upper limit.</p>
</td>
</tr>
<tr id="row63576353143535"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p4161871104853"><a name="p4161871104853"></a><a name="p4161871104853"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p49410992143535"><a name="p49410992143535"></a><a name="p49410992143535"></a>AS.2026</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p42867411143535"><a name="p42867411143535"></a><a name="p42867411143535"></a>There are ELB listeners of different types in the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p44268227173036"><a name="p44268227173036"></a><a name="p44268227173036"></a>The type of listeners in the AS group is not unique.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4957617311042"><a name="p4957617311042"></a><a name="p4957617311042"></a><strong id="b1934719550195032"><a name="b1934719550195032"></a><a name="b1934719550195032"></a>lb_listener_id</strong> is alternative to <strong id="b84235270610186"><a name="b84235270610186"></a><a name="b84235270610186"></a>lbaas_listeners</strong>.</p>
</td>
</tr>
<tr id="row433963639308"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p14105171104853"><a name="p14105171104853"></a><a name="p14105171104853"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p3757514593014"><a name="p3757514593014"></a><a name="p3757514593014"></a>AS.2027</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p2368790893014"><a name="p2368790893014"></a><a name="p2368790893014"></a>The VPC to which some subnets in the AS group belong is different with the VPC in the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p59283003173036"><a name="p59283003173036"></a><a name="p59283003173036"></a>The subnet of the AS group does not belong to the vpc.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p3646193511042"><a name="p3646193511042"></a><a name="p3646193511042"></a>Change the VPC ID or subnet.</p>
</td>
</tr>
<tr id="row11408906112223"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p15013867104853"><a name="p15013867104853"></a><a name="p15013867104853"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p51706204112223"><a name="p51706204112223"></a><a name="p51706204112223"></a>AS.2028</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p27453019112223"><a name="p27453019112223"></a><a name="p27453019112223"></a>The new expected number of instances is the same as the original number.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p66310092173036"><a name="p66310092173036"></a><a name="p66310092173036"></a>The modified expected number of instances is the same as the original number.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p564097311042"><a name="p564097311042"></a><a name="p564097311042"></a>Refer to the error code description.</p>
</td>
</tr>
<tr id="row7788117112224"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p6364280104853"><a name="p6364280104853"></a><a name="p6364280104853"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p26857746112224"><a name="p26857746112224"></a><a name="p26857746112224"></a>AS.2029</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p27993836112224"><a name="p27993836112224"></a><a name="p27993836112224"></a>The health check method for instances in the AS group is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p21675023173036"><a name="p21675023173036"></a><a name="p21675023173036"></a>Invalid health check method of the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1862905811042"><a name="p1862905811042"></a><a name="p1862905811042"></a>Use a valid <strong id="b112692034248"><a name="b112692034248"></a><a name="b112692034248"></a>health_periodic_audit_method</strong> value.</p>
</td>
</tr>
<tr id="row49556462112224"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p9049063104853"><a name="p9049063104853"></a><a name="p9049063104853"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p54650522112224"><a name="p54650522112224"></a><a name="p54650522112224"></a>AS.2030</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p64616129112224"><a name="p64616129112224"></a><a name="p64616129112224"></a>You are not allowed to modify the load balancer, AZ, subnet, or security group information when there are instances in the AS group, the AS group is scaling, or the AS group is in <strong id="b699315151472"><a name="b699315151472"></a><a name="b699315151472"></a>Inservice</strong> state.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p30509161173036"><a name="p30509161173036"></a><a name="p30509161173036"></a>You are not allowed to modify the lb, AZ, subnet, and security information when the number of instances in the AS group is not 0, the AS group is scaling, or the AS group is in Inservice status.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p2459323311042"><a name="p2459323311042"></a><a name="p2459323311042"></a>Check the number of instances in the AS group and the status of the AS group, or try again later.</p>
</td>
</tr>
<tr id="row20653682112224"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p60068124104921"><a name="p60068124104921"></a><a name="p60068124104921"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p62335566112224"><a name="p62335566112224"></a><a name="p62335566112224"></a>AS.2031</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p16016119112224"><a name="p16016119112224"></a><a name="p16016119112224"></a>The health check period of the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p28144580173036"><a name="p28144580173036"></a><a name="p28144580173036"></a>Invalid health check period of the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1040077411042"><a name="p1040077411042"></a><a name="p1040077411042"></a>Use a valid <strong id="b107842371941"><a name="b107842371941"></a><a name="b107842371941"></a>health_periodic_audit_time</strong> value.</p>
</td>
</tr>
<tr id="row49045923112224"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p34683525104921"><a name="p34683525104921"></a><a name="p34683525104921"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p13296787112224"><a name="p13296787112224"></a><a name="p13296787112224"></a>AS.2032</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p3297935112224"><a name="p3297935112224"></a><a name="p3297935112224"></a>The instance removal policy for the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p49195346173036"><a name="p49195346173036"></a><a name="p49195346173036"></a>Invalid instance removal policy.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p6597157011042"><a name="p6597157011042"></a><a name="p6597157011042"></a>Use a valid <strong id="b1381612391243"><a name="b1381612391243"></a><a name="b1381612391243"></a>instance_terminate_policy</strong> value.</p>
</td>
</tr>
<tr id="row49436199112225"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p51356896104921"><a name="p51356896104921"></a><a name="p51356896104921"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p44909198112225"><a name="p44909198112225"></a><a name="p44909198112225"></a>AS.2033</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p13766450112225"><a name="p13766450112225"></a><a name="p13766450112225"></a>You are not allowed to perform the operation when the AS group is in the current status.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p27274577173036"><a name="p27274577173036"></a><a name="p27274577173036"></a>You are not allowed to perform the operation when the AS group is in current [%s] status.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4332830611042"><a name="p4332830611042"></a><a name="p4332830611042"></a>Refer to the error code description.</p>
</td>
</tr>
<tr id="row33118350112225"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p59540370104921"><a name="p59540370104921"></a><a name="p59540370104921"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p4274779113942"><a name="p4274779113942"></a><a name="p4274779113942"></a>AS.2034</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p10712781113942"><a name="p10712781113942"></a><a name="p10712781113942"></a>The notification method for the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p18942913173036"><a name="p18942913173036"></a><a name="p18942913173036"></a>Invalid notification method of the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4516906311042"><a name="p4516906311042"></a><a name="p4516906311042"></a>Use a valid notification method.</p>
</td>
</tr>
<tr id="row7022220112225"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p52603781104921"><a name="p52603781104921"></a><a name="p52603781104921"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p27327022113956"><a name="p27327022113956"></a><a name="p27327022113956"></a>AS.2035</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p66005135113956"><a name="p66005135113956"></a><a name="p66005135113956"></a>The number of ECSs in the AS group is greater than the upper limit because some ECSs are manually added.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p52066606173036"><a name="p52066606173036"></a><a name="p52066606173036"></a>The number of instances manually added to the AS group exceeds the maximum number of the instances required in the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1286713441044"><a name="p1286713441044"></a><a name="p1286713441044"></a>Add a proper number of ECSs or increase the maximum number of instances in the AS group.</p>
</td>
</tr>
<tr id="row19147386112227"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p28995051104921"><a name="p28995051104921"></a><a name="p28995051104921"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p61592371114022"><a name="p61592371114022"></a><a name="p61592371114022"></a>AS.2036</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p65317475112227"><a name="p65317475112227"></a><a name="p65317475112227"></a>The number of ECSs in the AS group is smaller than the lower limit because some ECSs are manually deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p40047979173036"><a name="p40047979173036"></a><a name="p40047979173036"></a>The number of instances manually deleted is less than the minimum number of the instances required in the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p14913625859"><a name="p14913625859"></a><a name="p14913625859"></a>Delete a proper number of ECSs or decrease the minimum number of instances in the AS group.</p>
</td>
</tr>
<tr id="row18986414152922"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p65209602104921"><a name="p65209602104921"></a><a name="p65209602104921"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p46019644152922"><a name="p46019644152922"></a><a name="p46019644152922"></a>AS.2037</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p64209894152922"><a name="p64209894152922"></a><a name="p64209894152922"></a>The number of ELB listeners in the AS group reaches the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p2621524173036"><a name="p2621524173036"></a><a name="p2621524173036"></a>The number of listeners in the AS group exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4899600311042"><a name="p4899600311042"></a><a name="p4899600311042"></a>Select a proper number of load balancer listeners.</p>
</td>
</tr>
<tr id="row14454372101229"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p24724170104921"><a name="p24724170104921"></a><a name="p24724170104921"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p29953444101229"><a name="p29953444101229"></a><a name="p29953444101229"></a>AS.2038</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p10309872101229"><a name="p10309872101229"></a><a name="p10309872101229"></a>The ECSs of this type in the AZ of the AS group have been sold out.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p05281019114811"><a name="p05281019114811"></a><a name="p05281019114811"></a>The type [%s] of ECS in the AZ you selected has been sold out.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1617092711042"><a name="p1617092711042"></a><a name="p1617092711042"></a>Refer to the error code description. Change the AZ of the AS group or change the AS configuration for the AS group.</p>
</td>
</tr>
<tr id="row52432846143621"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p47469079104953"><a name="p47469079104953"></a><a name="p47469079104953"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p19202159143621"><a name="p19202159143621"></a><a name="p19202159143621"></a>AS.2039</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p11871085143621"><a name="p11871085143621"></a><a name="p11871085143621"></a>Parameter <strong id="b842352706161719"><a name="b842352706161719"></a><a name="b842352706161719"></a>protocolPort</strong> of the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p5569594173036"><a name="p5569594173036"></a><a name="p5569594173036"></a>Parameter <strong id="b20787523338"><a name="b20787523338"></a><a name="b20787523338"></a>protocolPort</strong> of the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4455509711042"><a name="p4455509711042"></a><a name="p4455509711042"></a>Use a valid <strong id="b25155632193030"><a name="b25155632193030"></a><a name="b25155632193030"></a>protocolPort</strong>.</p>
</td>
</tr>
<tr id="row50220297143629"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p43893655104953"><a name="p43893655104953"></a><a name="p43893655104953"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p41312260143629"><a name="p41312260143629"></a><a name="p41312260143629"></a>AS.2040</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p57958739143629"><a name="p57958739143629"></a><a name="p57958739143629"></a>Parameter <strong id="b1978780229161736"><a name="b1978780229161736"></a><a name="b1978780229161736"></a>weight</strong> of the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p33702870173036"><a name="p33702870173036"></a><a name="p33702870173036"></a>Parameter <strong id="b1792381366165057"><a name="b1792381366165057"></a><a name="b1792381366165057"></a>weight</strong> of the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p6708440211042"><a name="p6708440211042"></a><a name="p6708440211042"></a>Use a valid <strong id="b841336913"><a name="b841336913"></a><a name="b841336913"></a>weight</strong>.</p>
</td>
</tr>
<tr id="row13743590195610"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p54655380104953"><a name="p54655380104953"></a><a name="p54655380104953"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p39489026195610"><a name="p39489026195610"></a><a name="p39489026195610"></a>AS.2042</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p44494571195610"><a name="p44494571195610"></a><a name="p44494571195610"></a>The load balancer pool in the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p1468851110912"><a name="p1468851110912"></a><a name="p1468851110912"></a>Parameter pool of lbaas in the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4927637411042"><a name="p4927637411042"></a><a name="p4927637411042"></a>Use a valid <strong id="b1740449063"><a name="b1740449063"></a><a name="b1740449063"></a>pool</strong>.</p>
</td>
</tr>
<tr id="row12875298195615"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p48216033104953"><a name="p48216033104953"></a><a name="p48216033104953"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p36266213195615"><a name="p36266213195615"></a><a name="p36266213195615"></a>AS.2043</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p51882149195615"><a name="p51882149195615"></a><a name="p51882149195615"></a>Storage resources of this type are sold out or do not exist in the AZ specified for this AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p1397414512489"><a name="p1397414512489"></a><a name="p1397414512489"></a>There is not avalid volume in the AZ [%s] you selected.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p33332091201957"><a name="p33332091201957"></a><a name="p33332091201957"></a>Refer to the error code description. Change the AZ of the AS group or change the AS configuration for the AS group.</p>
</td>
</tr>
<tr id="row759372115443"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1111169315443"><a name="p1111169315443"></a><a name="p1111169315443"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p2763194115443"><a name="p2763194115443"></a><a name="p2763194115443"></a>AS.2044</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p2359476215443"><a name="p2359476215443"></a><a name="p2359476215443"></a>The AZ in the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p3212755515443"><a name="p3212755515443"></a><a name="p3212755515443"></a>The AZ in the AS group is not available.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p5219516115443"><a name="p5219516115443"></a><a name="p5219516115443"></a>Refer to the error code description. Change the AZ of the AS group.</p>
</td>
</tr>
<tr id="row61934319103631"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p66360076103638"><a name="p66360076103638"></a><a name="p66360076103638"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p6457086103638"><a name="p6457086103638"></a><a name="p6457086103638"></a>AS.2045</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p21826760103631"><a name="p21826760103631"></a><a name="p21826760103631"></a>The minimum or maximum number of instances in the AS group exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p23137118103631"><a name="p23137118103631"></a><a name="p23137118103631"></a>The min or max number of instances in the AS group exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p729911512068"><a name="p729911512068"></a><a name="p729911512068"></a>Enter proper maximum and minimum numbers of instances for the AS group.</p>
</td>
</tr>
<tr id="row14556425104152"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p38219776104152"><a name="p38219776104152"></a><a name="p38219776104152"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p8794143104152"><a name="p8794143104152"></a><a name="p8794143104152"></a>AS.2046</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p41237007104152"><a name="p41237007104152"></a><a name="p41237007104152"></a>The grace period for the instance health check is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p51863288104152"><a name="p51863288104152"></a><a name="p51863288104152"></a>Invalid health check grace period of the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p40176769104152"><a name="p40176769104152"></a><a name="p40176769104152"></a>Use a valid <strong id="b1553102317717"><a name="b1553102317717"></a><a name="b1553102317717"></a>health_periodic_audit_grace_period</strong> value.</p>
</td>
</tr>
<tr id="row184621040172815"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p7463940132812"><a name="p7463940132812"></a><a name="p7463940132812"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p154638408285"><a name="p154638408285"></a><a name="p154638408285"></a>AS.2047</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p194631540192816"><a name="p194631540192816"></a><a name="p194631540192816"></a>Failed to modify load balancer parameters because a scaling action is ongoing.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p8493914131119"><a name="p8493914131119"></a><a name="p8493914131119"></a>The AS group is in active status.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p13463840132811"><a name="p13463840132811"></a><a name="p13463840132811"></a>Wait until the scaling action is complete and modify the load balancer parameters again.</p>
</td>
</tr>
<tr id="row912612684920"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p20791588493"><a name="p20791588493"></a><a name="p20791588493"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p157948114920"><a name="p157948114920"></a><a name="p157948114920"></a>AS.2053</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p87915844919"><a name="p87915844919"></a><a name="p87915844919"></a>The priority policy used for multiple AZs in the AS group is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p1479108164911"><a name="p1479108164911"></a><a name="p1479108164911"></a>Invalid multi az priority policy.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p127918834916"><a name="p127918834916"></a><a name="p127918834916"></a>Change the priority policy used for multiple AZs in the AS group.</p>
</td>
</tr>
<tr id="row1648153715918"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p5648143765919"><a name="p5648143765919"></a><a name="p5648143765919"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p1764813379596"><a name="p1764813379596"></a><a name="p1764813379596"></a>AS.2054</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p1464923710594"><a name="p1464923710594"></a><a name="p1464923710594"></a>Failed to change the AZ because a scaling action is ongoing.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p19649123715915"><a name="p19649123715915"></a><a name="p19649123715915"></a>The AS group is in active status.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p9188118419"><a name="p9188118419"></a><a name="p9188118419"></a>Wait until the scaling action is complete and change the AZ again.</p>
</td>
</tr>
<tr id="row56766952112227"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1069985104953"><a name="p1069985104953"></a><a name="p1069985104953"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p27792162114022"><a name="p27792162114022"></a><a name="p27792162114022"></a>AS.3002</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p60886158112227"><a name="p60886158112227"></a><a name="p60886158112227"></a>The AS policy type is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p64564307173036"><a name="p64564307173036"></a><a name="p64564307173036"></a>Invalid AS policy type.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p534576201957"><a name="p534576201957"></a><a name="p534576201957"></a>Use a valid <strong id="b9849841118"><a name="b9849841118"></a><a name="b9849841118"></a>scaling_policy_type</strong> value.</p>
</td>
</tr>
<tr id="row54066752112227"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p41821664104953"><a name="p41821664104953"></a><a name="p41821664104953"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p60718354114022"><a name="p60718354114022"></a><a name="p60718354114022"></a>AS.3003</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p61616925112227"><a name="p61616925112227"></a><a name="p61616925112227"></a>When the AS policy is scheduled or periodic, parameter <strong id="b1523751310118"><a name="b1523751310118"></a><a name="b1523751310118"></a>scheduled_policy</strong> is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p24066721173036"><a name="p24066721173036"></a><a name="p24066721173036"></a>The information about the AS policy is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p20595268201957"><a name="p20595268201957"></a><a name="p20595268201957"></a>Use a valid <strong id="b2075162711115"><a name="b2075162711115"></a><a name="b2075162711115"></a>scheduled_policy</strong> value.</p>
</td>
</tr>
<tr id="row44482860112228"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p20569484104953"><a name="p20569484104953"></a><a name="p20569484104953"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p38938953114022"><a name="p38938953114022"></a><a name="p38938953114022"></a>AS.3004</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p62707491112228"><a name="p62707491112228"></a><a name="p62707491112228"></a>The period type is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p64195431032"><a name="p64195431032"></a><a name="p64195431032"></a>Invalid recurrence type in the AS policy.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p23846769201957"><a name="p23846769201957"></a><a name="p23846769201957"></a>Use a valid <strong id="b0947113811116"><a name="b0947113811116"></a><a name="b0947113811116"></a>recurrence_type</strong> value.</p>
</td>
</tr>
<tr id="row3259482112228"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p4577052010519"><a name="p4577052010519"></a><a name="p4577052010519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p66556426114022"><a name="p66556426114022"></a><a name="p66556426114022"></a>AS.3005</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p44843893112228"><a name="p44843893112228"></a><a name="p44843893112228"></a>The end time is not specified for a periodic AS policy.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p32504377173036"><a name="p32504377173036"></a><a name="p32504377173036"></a>The end time of the scaling action triggered periodically is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p34424085201957"><a name="p34424085201957"></a><a name="p34424085201957"></a>Enter a valid <strong id="b4101182912139"><a name="b4101182912139"></a><a name="b4101182912139"></a>end_time</strong> value.</p>
</td>
</tr>
<tr id="row28481294112228"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1360439110519"><a name="p1360439110519"></a><a name="p1360439110519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p67035168114022"><a name="p67035168114022"></a><a name="p67035168114022"></a>AS.3006</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p25887631114356"><a name="p25887631114356"></a><a name="p25887631114356"></a>The format of the end time for the periodically triggered scaling action is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p6262434173036"><a name="p6262434173036"></a><a name="p6262434173036"></a>The format of the end time for the scaling action triggered periodically is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p2387679411042"><a name="p2387679411042"></a><a name="p2387679411042"></a>Use a correct format for the end time.</p>
</td>
</tr>
<tr id="row59062974112228"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p5259805510519"><a name="p5259805510519"></a><a name="p5259805510519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p13385119114022"><a name="p13385119114022"></a><a name="p13385119114022"></a>AS.3007</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p25596201112228"><a name="p25596201112228"></a><a name="p25596201112228"></a>The end time of the scaling action triggered periodically must be later than the current time.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p1912170173036"><a name="p1912170173036"></a><a name="p1912170173036"></a>The end time of the scaling action triggered periodically must be later than the current time.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4419117688"><a name="p4419117688"></a><a name="p4419117688"></a>Ensure that the end time is later than the current time.</p>
</td>
</tr>
<tr id="row7089341112229"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p2482090010519"><a name="p2482090010519"></a><a name="p2482090010519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p26966688114022"><a name="p26966688114022"></a><a name="p26966688114022"></a>AS.3008</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p6729712112229"><a name="p6729712112229"></a><a name="p6729712112229"></a>The triggering time is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p51795220173036"><a name="p51795220173036"></a><a name="p51795220173036"></a>Parameter lanchTime in the AS policy is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p2921611511042"><a name="p2921611511042"></a><a name="p2921611511042"></a>Enter a valid <strong id="b1757115431416"><a name="b1757115431416"></a><a name="b1757115431416"></a>launch_time</strong> value.</p>
</td>
</tr>
<tr id="row39415837112229"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p4215204910519"><a name="p4215204910519"></a><a name="p4215204910519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p62927880114022"><a name="p62927880114022"></a><a name="p62927880114022"></a>AS.3009</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p36857268112229"><a name="p36857268112229"></a><a name="p36857268112229"></a>The triggering time format is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p43534508173036"><a name="p43534508173036"></a><a name="p43534508173036"></a>The format of parameter lanchTime is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p2503832411042"><a name="p2503832411042"></a><a name="p2503832411042"></a>Use a correct triggering time format.</p>
</td>
</tr>
<tr id="row30010565112229"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p6009354610519"><a name="p6009354610519"></a><a name="p6009354610519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p39070785114022"><a name="p39070785114022"></a><a name="p39070785114022"></a>AS.3010</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p1911232112229"><a name="p1911232112229"></a><a name="p1911232112229"></a>The triggering time of the scaling action triggered at a scheduled time must be later than the current time.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p36731871316"><a name="p36731871316"></a><a name="p36731871316"></a>The triggering time of the scheduled policy must be later than the current time.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p16241944783"><a name="p16241944783"></a><a name="p16241944783"></a>Ensure that the triggering time of the scheduled policy is later than the current time.</p>
</td>
</tr>
<tr id="row44690612112229"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p5321604910519"><a name="p5321604910519"></a><a name="p5321604910519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p28444158114022"><a name="p28444158114022"></a><a name="p28444158114022"></a>AS.3011</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p16483859112229"><a name="p16483859112229"></a><a name="p16483859112229"></a>The AS policy type is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p40409334173036"><a name="p40409334173036"></a><a name="p40409334173036"></a>The AS policy type is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p62616444202314"><a name="p62616444202314"></a><a name="p62616444202314"></a>Enter a valid <strong id="b155111635101313"><a name="b155111635101313"></a><a name="b155111635101313"></a>scaling_policy_type</strong> value.</p>
</td>
</tr>
<tr id="row4078060112230"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p557643210519"><a name="p557643210519"></a><a name="p557643210519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p66261242114022"><a name="p66261242114022"></a><a name="p66261242114022"></a>AS.3012</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p46826671112230"><a name="p46826671112230"></a><a name="p46826671112230"></a>The cooldown period in the AS policy is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p64722214173036"><a name="p64722214173036"></a><a name="p64722214173036"></a>Invalid cooldown period in the AS policy.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p37606415202314"><a name="p37606415202314"></a><a name="p37606415202314"></a>Enter a valid <strong id="b17546165441518"><a name="b17546165441518"></a><a name="b17546165441518"></a>cool_down_time</strong> value.</p>
</td>
</tr>
<tr id="row46407276112230"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p5838877105141"><a name="p5838877105141"></a><a name="p5838877105141"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p53172408114022"><a name="p53172408114022"></a><a name="p53172408114022"></a>AS.3013</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p5222290112230"><a name="p5222290112230"></a><a name="p5222290112230"></a>The AS policy name is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p4963264173036"><a name="p4963264173036"></a><a name="p4963264173036"></a>The AS policy name is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p56269026202314"><a name="p56269026202314"></a><a name="p56269026202314"></a>Enter a valid <strong id="b9901726151718"><a name="b9901726151718"></a><a name="b9901726151718"></a>scaling_policy_name</strong> value.</p>
</td>
</tr>
<tr id="row17916979112230"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p28683449105141"><a name="p28683449105141"></a><a name="p28683449105141"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p40871235114022"><a name="p40871235114022"></a><a name="p40871235114022"></a>AS.3014</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p45682878112230"><a name="p45682878112230"></a><a name="p45682878112230"></a>The length of the AS policy name is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p61450166173036"><a name="p61450166173036"></a><a name="p61450166173036"></a>The length of the AS policy name is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p42824987202314"><a name="p42824987202314"></a><a name="p42824987202314"></a>Enter a valid <strong id="b789119296173"><a name="b789119296173"></a><a name="b789119296173"></a>scaling_policy_name</strong> value.</p>
</td>
</tr>
<tr id="row36984131112230"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p39377743105141"><a name="p39377743105141"></a><a name="p39377743105141"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p65904111114022"><a name="p65904111114022"></a><a name="p65904111114022"></a>AS.3015</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p54342194112230"><a name="p54342194112230"></a><a name="p54342194112230"></a>The execution action in the AS policy is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p35559171173036"><a name="p35559171173036"></a><a name="p35559171173036"></a>The action in the AS policy is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p42531241202314"><a name="p42531241202314"></a><a name="p42531241202314"></a>Enter a valid <strong id="b41751559173"><a name="b41751559173"></a><a name="b41751559173"></a>scaling_policy_action</strong> value.</p>
</td>
</tr>
<tr id="row51624858112230"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p50890244105141"><a name="p50890244105141"></a><a name="p50890244105141"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p61259285114022"><a name="p61259285114022"></a><a name="p61259285114022"></a>AS.3016</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p12262893112230"><a name="p12262893112230"></a><a name="p12262893112230"></a>The operation to perform the execution action in the AS policy is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p18614634173036"><a name="p18614634173036"></a><a name="p18614634173036"></a>The operation to perform the action in the AS policy is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p138621031595"><a name="p138621031595"></a><a name="p138621031595"></a>Enter a valid <strong id="b3135612121816"><a name="b3135612121816"></a><a name="b3135612121816"></a>operation</strong> value.</p>
</td>
</tr>
<tr id="row975162112231"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p54895234105141"><a name="p54895234105141"></a><a name="p54895234105141"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p30624730114022"><a name="p30624730114022"></a><a name="p30624730114022"></a>AS.3017</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p22699505112231"><a name="p22699505112231"></a><a name="p22699505112231"></a>The operation to perform the action in the AS policy action is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p14078263173036"><a name="p14078263173036"></a><a name="p14078263173036"></a>The operation to perform the action in the AS policy action is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p42705128202314"><a name="p42705128202314"></a><a name="p42705128202314"></a>Enter a valid <strong id="b28073541914"><a name="b28073541914"></a><a name="b28073541914"></a>operation</strong> value.</p>
</td>
</tr>
<tr id="row43880482112231"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p21742780105141"><a name="p21742780105141"></a><a name="p21742780105141"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p45285608114022"><a name="p45285608114022"></a><a name="p45285608114022"></a>AS.3018</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p2817085112231"><a name="p2817085112231"></a><a name="p2817085112231"></a>The number of instances to which the AS policy applies is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p62506491173036"><a name="p62506491173036"></a><a name="p62506491173036"></a>The number of instances which action in the AS policy operates on is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1592913311042"><a name="p1592913311042"></a><a name="p1592913311042"></a>Enter a valid <strong id="b11136144632020"><a name="b11136144632020"></a><a name="b11136144632020"></a>instance_number</strong> value.</p>
</td>
</tr>
<tr id="row49287761112231"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p12794797105141"><a name="p12794797105141"></a><a name="p12794797105141"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p62756146114022"><a name="p62756146114022"></a><a name="p62756146114022"></a>AS.3019</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p46498512112231"><a name="p46498512112231"></a><a name="p46498512112231"></a>The AS group ID in the AS policy is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p313683173036"><a name="p313683173036"></a><a name="p313683173036"></a>The AS group ID in the AS policy cannot be null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p38485140202725"><a name="p38485140202725"></a><a name="p38485140202725"></a>Add an AS group ID.</p>
</td>
</tr>
<tr id="row26161609112232"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p5707034105217"><a name="p5707034105217"></a><a name="p5707034105217"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p48094131114022"><a name="p48094131114022"></a><a name="p48094131114022"></a>AS.3020</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p48954284112232"><a name="p48954284112232"></a><a name="p48954284112232"></a>The AS policy does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p27348384173036"><a name="p27348384173036"></a><a name="p27348384173036"></a>The AS policy does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p64324907202725"><a name="p64324907202725"></a><a name="p64324907202725"></a>Use a correct AS policy ID.</p>
</td>
</tr>
<tr id="row27185015112232"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p66787561105217"><a name="p66787561105217"></a><a name="p66787561105217"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p29794606114022"><a name="p29794606114022"></a><a name="p29794606114022"></a>AS.3021</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p52634650112232"><a name="p52634650112232"></a><a name="p52634650112232"></a>The AS policy ID is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p5639887173036"><a name="p5639887173036"></a><a name="p5639887173036"></a>The AS policy ID cannot be null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p66514883202725"><a name="p66514883202725"></a><a name="p66514883202725"></a>Add an AS policy ID.</p>
</td>
</tr>
<tr id="row7722120112232"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p34206174105217"><a name="p34206174105217"></a><a name="p34206174105217"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p44104942114022"><a name="p44104942114022"></a><a name="p44104942114022"></a>AS.3022</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p64747517112232"><a name="p64747517112232"></a><a name="p64747517112232"></a>The action of the AS policy request body is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p17837330173036"><a name="p17837330173036"></a><a name="p17837330173036"></a>The action of the AS policy request body is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p54342265202725"><a name="p54342265202725"></a><a name="p54342265202725"></a>Use a valid <strong id="b19192171213236"><a name="b19192171213236"></a><a name="b19192171213236"></a>action</strong> value.</p>
</td>
</tr>
<tr id="row32453419112232"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p38912394105217"><a name="p38912394105217"></a><a name="p38912394105217"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p7357319114022"><a name="p7357319114022"></a><a name="p7357319114022"></a>AS.3023</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p57565873112232"><a name="p57565873112232"></a><a name="p57565873112232"></a>The period type of the AS policy is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p51403172173036"><a name="p51403172173036"></a><a name="p51403172173036"></a>The period type of the AS policy is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4079990202725"><a name="p4079990202725"></a><a name="p4079990202725"></a>Use a valid <strong id="b35281814122310"><a name="b35281814122310"></a><a name="b35281814122310"></a>recurrence_type</strong> value.</p>
</td>
</tr>
<tr id="row378013112232"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p47195018105217"><a name="p47195018105217"></a><a name="p47195018105217"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p61885330114022"><a name="p61885330114022"></a><a name="p61885330114022"></a>AS.3024</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p64227482112232"><a name="p64227482112232"></a><a name="p64227482112232"></a>The value of the periodically triggered tasks of the AS policy is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p26166664173036"><a name="p26166664173036"></a><a name="p26166664173036"></a>The value of the period type of the AS policy is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p6678184202725"><a name="p6678184202725"></a><a name="p6678184202725"></a>Add a valid <strong id="b15352152532511"><a name="b15352152532511"></a><a name="b15352152532511"></a>recurrence_value</strong> value.</p>
</td>
</tr>
<tr id="row45438673112232"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p45429823105217"><a name="p45429823105217"></a><a name="p45429823105217"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p17249396114022"><a name="p17249396114022"></a><a name="p17249396114022"></a>AS.3025</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p25560497112232"><a name="p25560497112232"></a><a name="p25560497112232"></a>The period type of the AS policy is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p16581194173036"><a name="p16581194173036"></a><a name="p16581194173036"></a>The value of period type of the AS policy is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p48388998202725"><a name="p48388998202725"></a><a name="p48388998202725"></a>Use a valid <strong id="b67558352611"><a name="b67558352611"></a><a name="b67558352611"></a>recurrence_type</strong> value.</p>
</td>
</tr>
<tr id="row29893452112233"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p31319988105251"><a name="p31319988105251"></a><a name="p31319988105251"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p25452311114022"><a name="p25452311114022"></a><a name="p25452311114022"></a>AS.3026</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p38842897112233"><a name="p38842897112233"></a><a name="p38842897112233"></a>The alarm ID in the AS policy is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p8094907173036"><a name="p8094907173036"></a><a name="p8094907173036"></a>The alarm ID in the AS policy is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1692880202725"><a name="p1692880202725"></a><a name="p1692880202725"></a>Add an alarm ID.</p>
</td>
</tr>
<tr id="row30520336112233"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p15258006105251"><a name="p15258006105251"></a><a name="p15258006105251"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p32688301114022"><a name="p32688301114022"></a><a name="p32688301114022"></a>AS.3027</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p58185657112233"><a name="p58185657112233"></a><a name="p58185657112233"></a>The AS group must be in service when the AS policy is performed.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p62716343173036"><a name="p62716343173036"></a><a name="p62716343173036"></a>The AS policy must be in the inservice status when the AS policy is performed.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p46926697202734"><a name="p46926697202734"></a><a name="p46926697202734"></a>Enable the AS group and try again.</p>
</td>
</tr>
<tr id="row55448348112233"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p50123815105251"><a name="p50123815105251"></a><a name="p50123815105251"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p6125428114022"><a name="p6125428114022"></a><a name="p6125428114022"></a>AS.3028</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p66568360112233"><a name="p66568360112233"></a><a name="p66568360112233"></a>The format of the start time for the periodically triggered scaling action is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p19078370173036"><a name="p19078370173036"></a><a name="p19078370173036"></a>The format of the start time for the scaling action triggered periodically is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p53482891202734"><a name="p53482891202734"></a><a name="p53482891202734"></a>Use a correct format for the start time.</p>
</td>
</tr>
<tr id="row45728906112233"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p33039427105251"><a name="p33039427105251"></a><a name="p33039427105251"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p36252012114022"><a name="p36252012114022"></a><a name="p36252012114022"></a>AS.3029</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p50730198112233"><a name="p50730198112233"></a><a name="p50730198112233"></a>The start time of the periodically triggered scaling action must be earlier than the end time.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p16597350173036"><a name="p16597350173036"></a><a name="p16597350173036"></a>The start time of the scaling action triggered periodically must be earlier than the end time.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p3553178920317"><a name="p3553178920317"></a><a name="p3553178920317"></a>Ensure that the start time of the periodic policy is earlier than the end time.</p>
</td>
</tr>
<tr id="row4714756112233"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p60769678105251"><a name="p60769678105251"></a><a name="p60769678105251"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p53933345114022"><a name="p53933345114022"></a><a name="p53933345114022"></a>AS.3030</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p63442019112233"><a name="p63442019112233"></a><a name="p63442019112233"></a>The alarm rule in the AS policy does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p189369137579"><a name="p189369137579"></a><a name="p189369137579"></a>The alarm in the AS policy does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1657339120317"><a name="p1657339120317"></a><a name="p1657339120317"></a>Modify the alarm rule used by the AS policy.</p>
</td>
</tr>
<tr id="row4492113112233"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p9245490105251"><a name="p9245490105251"></a><a name="p9245490105251"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p58723430114022"><a name="p58723430114022"></a><a name="p58723430114022"></a>AS.3031</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p11966210112233"><a name="p11966210112233"></a><a name="p11966210112233"></a>The AS policy name is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p58975053173036"><a name="p58975053173036"></a><a name="p58975053173036"></a>Invalid AS policy name.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1052687820317"><a name="p1052687820317"></a><a name="p1052687820317"></a>Enter a valid <strong id="b111623815271"><a name="b111623815271"></a><a name="b111623815271"></a>scaling_policy_name</strong> value.</p>
</td>
</tr>
<tr id="row58011824112234"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p29076130105251"><a name="p29076130105251"></a><a name="p29076130105251"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p61034775114022"><a name="p61034775114022"></a><a name="p61034775114022"></a>AS.3032</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p41212403112234"><a name="p41212403112234"></a><a name="p41212403112234"></a>The number of AS policies exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p43140974173036"><a name="p43140974173036"></a><a name="p43140974173036"></a>The number of AS policies exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4269598520317"><a name="p4269598520317"></a><a name="p4269598520317"></a>Delete idle AS policies or apply for a higher quota.</p>
</td>
</tr>
<tr id="row30407009152833"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p57206873105251"><a name="p57206873105251"></a><a name="p57206873105251"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p47048696152833"><a name="p47048696152833"></a><a name="p47048696152833"></a>AS.3033</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p52847994152833"><a name="p52847994152833"></a><a name="p52847994152833"></a>The triggering time of the periodic policy falls outside the effective time range of the policy.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p16161013325"><a name="p16161013325"></a><a name="p16161013325"></a>The triggering time of the periodic policy is not included in the effective time of the policy.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p29769692203142"><a name="p29769692203142"></a><a name="p29769692203142"></a>Ensure that the triggering time of the periodic policy is within the range from the start time to the end time.</p>
</td>
</tr>
<tr id="row4292539115340"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p27053092105317"><a name="p27053092105317"></a><a name="p27053092105317"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p2963180915340"><a name="p2963180915340"></a><a name="p2963180915340"></a>AS.3034</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p4870198915340"><a name="p4870198915340"></a><a name="p4870198915340"></a>The alarm ID in the AS policy is being used by another AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p11701443173036"><a name="p11701443173036"></a><a name="p11701443173036"></a>The alarm ID in the AS policy is being used by another AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p55755377203142"><a name="p55755377203142"></a><a name="p55755377203142"></a>Refer to the error code description. An alarm ID can be used only by the AS policy in one AS group at a time.</p>
</td>
</tr>
<tr id="row55597684173212"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p58806940105317"><a name="p58806940105317"></a><a name="p58806940105317"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p4348400173227"><a name="p4348400173227"></a><a name="p4348400173227"></a>AS.3035</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p16676080173227"><a name="p16676080173227"></a><a name="p16676080173227"></a>The percentage of instances to which the AS policy applies is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p7526436173036"><a name="p7526436173036"></a><a name="p7526436173036"></a>The percentage of instances which action in the AS policy operates on is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4629531675"><a name="p4629531675"></a><a name="p4629531675"></a>Use a valid <strong id="b15776296291"><a name="b15776296291"></a><a name="b15776296291"></a>instance_percentage</strong> value.</p>
</td>
</tr>
<tr id="row53327903173217"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p54804177105317"><a name="p54804177105317"></a><a name="p54804177105317"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p10158051173227"><a name="p10158051173227"></a><a name="p10158051173227"></a>AS.3036</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p17495789173227"><a name="p17495789173227"></a><a name="p17495789173227"></a>The action in the AS policy operates is not unique.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p50954476173036"><a name="p50954476173036"></a><a name="p50954476173036"></a>The action in the AS policy operates is not unique.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p193136101095"><a name="p193136101095"></a><a name="p193136101095"></a>Select one from <strong id="b1822049153111"><a name="b1822049153111"></a><a name="b1822049153111"></a>instance_percentage</strong> or <strong id="b48334919313"><a name="b48334919313"></a><a name="b48334919313"></a>instance_number</strong>.</p>
</td>
</tr>
<tr id="row19376028101015"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p25954453101015"><a name="p25954453101015"></a><a name="p25954453101015"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p21935918101015"><a name="p21935918101015"></a><a name="p21935918101015"></a>AS.3037</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p31978895101015"><a name="p31978895101015"></a><a name="p31978895101015"></a>The resource type in the AS policy is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p40153697101015"><a name="p40153697101015"></a><a name="p40153697101015"></a>The scaling resource type in the AS policy is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1218012421486"><a name="p1218012421486"></a><a name="p1218012421486"></a>Use a valid <strong id="b19622135012326"><a name="b19622135012326"></a><a name="b19622135012326"></a>scaling_resource_type</strong> value.</p>
</td>
</tr>
<tr id="row46623563101025"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p18412284101025"><a name="p18412284101025"></a><a name="p18412284101025"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p15000074101025"><a name="p15000074101025"></a><a name="p15000074101025"></a>AS.3038</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p7046492101025"><a name="p7046492101025"></a><a name="p7046492101025"></a>The AS policy is being executed and cannot be executed again.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p33895003101025"><a name="p33895003101025"></a><a name="p33895003101025"></a>The AS policy is in executing status.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p494164914918"><a name="p494164914918"></a><a name="p494164914918"></a>Try again later.</p>
</td>
</tr>
<tr id="row30966484101028"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p25257286101028"><a name="p25257286101028"></a><a name="p25257286101028"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p32574309101028"><a name="p32574309101028"></a><a name="p32574309101028"></a>AS.3040</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p21273368101028"><a name="p21273368101028"></a><a name="p21273368101028"></a>The number of modifications to scaling resources in the AS policy has reached the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p45421256101028"><a name="p45421256101028"></a><a name="p45421256101028"></a>The adjustment by policy reached the limit</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p55243100101028"><a name="p55243100101028"></a><a name="p55243100101028"></a>Refer to the error code description.</p>
</td>
</tr>
<tr id="row31952379101035"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p38005883101035"><a name="p38005883101035"></a><a name="p38005883101035"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p58577692101035"><a name="p58577692101035"></a><a name="p58577692101035"></a>AS.3041</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p47172613101035"><a name="p47172613101035"></a><a name="p47172613101035"></a>The scaling resource ID in the AS policy is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p62885343101035"><a name="p62885343101035"></a><a name="p62885343101035"></a>The scaling resource ID in the AS policy is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p60548050101035"><a name="p60548050101035"></a><a name="p60548050101035"></a>Enter a valid AS resource ID in the AS policy.</p>
</td>
</tr>
<tr id="row13507962101022"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p20403113101022"><a name="p20403113101022"></a><a name="p20403113101022"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p42039445101022"><a name="p42039445101022"></a><a name="p42039445101022"></a>AS.3042</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p49751845101022"><a name="p49751845101022"></a><a name="p49751845101022"></a>The scaling resource in the AS policy does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p3367617101022"><a name="p3367617101022"></a><a name="p3367617101022"></a>The scaling resource in the AS policy does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p2122102031117"><a name="p2122102031117"></a><a name="p2122102031117"></a>Enter a valid AS resource ID in the AS policy.</p>
</td>
</tr>
<tr id="row42888858101019"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p51445482101019"><a name="p51445482101019"></a><a name="p51445482101019"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p6334494101019"><a name="p6334494101019"></a><a name="p6334494101019"></a>AS.3043</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p43331999101019"><a name="p43331999101019"></a><a name="p43331999101019"></a>The value of parameter <strong id="b842352706173219"><a name="b842352706173219"></a><a name="b842352706173219"></a>limits</strong> in the AS policy is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p20230996101019"><a name="p20230996101019"></a><a name="p20230996101019"></a>The limit which action in the AS policy operates on is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p28097957101019"><a name="p28097957101019"></a><a name="p28097957101019"></a>Use a valid <strong id="b842352706194651"><a name="b842352706194651"></a><a name="b842352706194651"></a>limits</strong> value in the AS policy.</p>
</td>
</tr>
<tr id="row6871419185318"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p2087212192534"><a name="p2087212192534"></a><a name="p2087212192534"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p587251916531"><a name="p587251916531"></a><a name="p587251916531"></a>AS.3045</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p387291975316"><a name="p387291975316"></a><a name="p387291975316"></a>Failed to delete policies in batches.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p88721319195313"><a name="p88721319195313"></a><a name="p88721319195313"></a>Failed to delete policies in a batch.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p188722019105313"><a name="p188722019105313"></a><a name="p188722019105313"></a>If this error code is returned, use parameter <strong id="b17105608103135_1"><a name="b17105608103135_1"></a><a name="b17105608103135_1"></a>Message</strong> to obtain the policy ID and the failure cause.</p>
</td>
</tr>
<tr id="row05918445531"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1851482112541"><a name="p1851482112541"></a><a name="p1851482112541"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p153062112543"><a name="p153062112543"></a><a name="p153062112543"></a>AS.3046</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p1359844165315"><a name="p1359844165315"></a><a name="p1359844165315"></a>Failed to enable policies in batches.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p75915445530"><a name="p75915445530"></a><a name="p75915445530"></a>Failed to resume policies in a batch.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p75914475312"><a name="p75914475312"></a><a name="p75914475312"></a>If this error code is returned, use parameter <strong id="b104931967"><a name="b104931967"></a><a name="b104931967"></a>Message</strong> to obtain the policy ID and the failure cause.</p>
</td>
</tr>
<tr id="row7451133835312"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p12541927175410"><a name="p12541927175410"></a><a name="p12541927175410"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p12559172715411"><a name="p12559172715411"></a><a name="p12559172715411"></a>AS.3047</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p144511138165317"><a name="p144511138165317"></a><a name="p144511138165317"></a>Failed to disable policies in batches.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p8451163816532"><a name="p8451163816532"></a><a name="p8451163816532"></a>Failed to pause policies in a batch.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p845116386536"><a name="p845116386536"></a><a name="p845116386536"></a>If this error code is returned, use parameter <strong id="b17165194872317"><a name="b17165194872317"></a><a name="b17165194872317"></a>Message</strong> to obtain the policy ID and the failure cause.</p>
</td>
</tr>
<tr id="row55291135115316"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1661033013549"><a name="p1661033013549"></a><a name="p1661033013549"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p1962653015547"><a name="p1962653015547"></a><a name="p1962653015547"></a>AS.3048</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p1152917359538"><a name="p1152917359538"></a><a name="p1152917359538"></a>The value of the parameter that specifies whether to forcibly delete the policy is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p10529735205315"><a name="p10529735205315"></a><a name="p10529735205315"></a>The value of the parameter that specifies whether to forcibly delete the policy is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p14686255101311"><a name="p14686255101311"></a><a name="p14686255101311"></a>Use a valid <strong id="b8435151593317"><a name="b8435151593317"></a><a name="b8435151593317"></a>force_delete</strong> value.</p>
</td>
</tr>
<tr id="row17247113525413"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p0694163813547"><a name="p0694163813547"></a><a name="p0694163813547"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p19713173865420"><a name="p19713173865420"></a><a name="p19713173865420"></a>AS.3049</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p2247435115413"><a name="p2247435115413"></a><a name="p2247435115413"></a>The list of AS policies on which a batch operation is to be performed is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p3247235165413"><a name="p3247235165413"></a><a name="p3247235165413"></a>The list of AS policies to be batched is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p14317114175112"><a name="p14317114175112"></a><a name="p14317114175112"></a>Add the IDs of the AS policies to be operated in batches.</p>
</td>
</tr>
<tr id="row896062016214"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p59601820621"><a name="p59601820621"></a><a name="p59601820621"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p2067912251827"><a name="p2067912251827"></a><a name="p2067912251827"></a>AS.3050</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p44264545416"><a name="p44264545416"></a><a name="p44264545416"></a>The format of the alarm ID in the AS policy is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p9960142010210"><a name="p9960142010210"></a><a name="p9960142010210"></a>The alarm ID in the AS policy is illegal.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1596020202216"><a name="p1596020202216"></a><a name="p1596020202216"></a>Use an alarm ID in correct format.</p>
</td>
</tr>
<tr id="row1275317188244"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p17753018132412"><a name="p17753018132412"></a><a name="p17753018132412"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p1075311842410"><a name="p1075311842410"></a><a name="p1075311842410"></a>AS.3054</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p642312618194"><a name="p642312618194"></a><a name="p642312618194"></a>The scaling resource type in the AS policy cannot be left blank.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p27517545180"><a name="p27517545180"></a><a name="p27517545180"></a>The scaling resource type in the AS policy is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p975319183246"><a name="p975319183246"></a><a name="p975319183246"></a>Use a valid <strong id="b10998192219347"><a name="b10998192219347"></a><a name="b10998192219347"></a>scaling_resource_type</strong> value.</p>
</td>
</tr>
<tr id="row145745437168"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p07380508169"><a name="p07380508169"></a><a name="p07380508169"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p1375945031619"><a name="p1375945031619"></a><a name="p1375945031619"></a>AS.3055</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p10188253203119"><a name="p10188253203119"></a><a name="p10188253203119"></a>The scaling resource ID in the scaling policy is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p18808650171616"><a name="p18808650171616"></a><a name="p18808650171616"></a>The scaling resource ID in the AS policy is format wrong.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1750345773114"><a name="p1750345773114"></a><a name="p1750345773114"></a>Enter a valid AS resource ID in the AS policy.</p>
</td>
</tr>
<tr id="row18283114652719"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p132832460271"><a name="p132832460271"></a><a name="p132832460271"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p14283546182712"><a name="p14283546182712"></a><a name="p14283546182712"></a>AS.3056</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p102832467278"><a name="p102832467278"></a><a name="p102832467278"></a>The value of the alarm rule used for deleting the scaling policy is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p928364682716"><a name="p928364682716"></a><a name="p928364682716"></a>The value of the parameter that specifies whether to delete the alarm in the AS policy is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p6283746172715"><a name="p6283746172715"></a><a name="p6283746172715"></a>Use a valid <strong id="b835812319406"><a name="b835812319406"></a><a name="b835812319406"></a>delete_alarm</strong> value.</p>
</td>
</tr>
<tr id="row299417357314"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p799514358316"><a name="p799514358316"></a><a name="p799514358316"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p139958354318"><a name="p139958354318"></a><a name="p139958354318"></a>AS.3057</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p11797929183218"><a name="p11797929183218"></a><a name="p11797929183218"></a>The <strong id="b1389212516457"><a name="b1389212516457"></a><a name="b1389212516457"></a>sort_by</strong> value in the request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p699623518310"><a name="p699623518310"></a><a name="p699623518310"></a>The value of parameter sort_by in the request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p599653517316"><a name="p599653517316"></a><a name="p599653517316"></a>Use a valid <strong id="b453418239491"><a name="b453418239491"></a><a name="b453418239491"></a>sort_by</strong> value.</p>
</td>
</tr>
<tr id="row13578307322"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p357819016327"><a name="p357819016327"></a><a name="p357819016327"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p85783019327"><a name="p85783019327"></a><a name="p85783019327"></a>AS.3058</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p73132319326"><a name="p73132319326"></a><a name="p73132319326"></a>The <strong id="b18801733105011"><a name="b18801733105011"></a><a name="b18801733105011"></a>order</strong> value in the request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p165787073217"><a name="p165787073217"></a><a name="p165787073217"></a>The value of parameter order in the request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p125780043211"><a name="p125780043211"></a><a name="p125780043211"></a>Use a valid <strong id="b5557548115017"><a name="b5557548115017"></a><a name="b5557548115017"></a>order</strong> value.</p>
</td>
</tr>
<tr id="row16778849112234"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p22471318105317"><a name="p22471318105317"></a><a name="p22471318105317"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p1174486114022"><a name="p1174486114022"></a><a name="p1174486114022"></a>AS.4000</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p27492982112234"><a name="p27492982112234"></a><a name="p27492982112234"></a>The <strong id="b4860776310291"><a name="b4860776310291"></a><a name="b4860776310291"></a>start_number</strong> value in the instance request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p34611589173036"><a name="p34611589173036"></a><a name="p34611589173036"></a>The value of parameter start_number in the request for the instance is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p75992147210"><a name="p75992147210"></a><a name="p75992147210"></a>Use a valid <strong id="b432711128145"><a name="b432711128145"></a><a name="b432711128145"></a>start_number</strong> value.</p>
</td>
</tr>
<tr id="row15251876112234"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p7028679105317"><a name="p7028679105317"></a><a name="p7028679105317"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p50894029114022"><a name="p50894029114022"></a><a name="p50894029114022"></a>AS.4001</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p8242634112234"><a name="p8242634112234"></a><a name="p8242634112234"></a>The <strong id="b11504718102914"><a name="b11504718102914"></a><a name="b11504718102914"></a>limit</strong> value in the instance request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p66024610173036"><a name="p66024610173036"></a><a name="p66024610173036"></a>The value of parameter limit in the request for the instance is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p149982271623"><a name="p149982271623"></a><a name="p149982271623"></a>Use a valid <strong id="b748193316148"><a name="b748193316148"></a><a name="b748193316148"></a>limit</strong> value.</p>
</td>
</tr>
<tr id="row17044959112234"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p23633670105317"><a name="p23633670105317"></a><a name="p23633670105317"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p20271676114022"><a name="p20271676114022"></a><a name="p20271676114022"></a>AS.4003</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p28613098112234"><a name="p28613098112234"></a><a name="p28613098112234"></a>The <strong>life_cycle_state</strong> value in the instance request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p14885374173036"><a name="p14885374173036"></a><a name="p14885374173036"></a>The value of parameter life_cycle_state in the instance request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p63296063203333"><a name="p63296063203333"></a><a name="p63296063203333"></a>Use a valid <strong>life_cycle_state</strong> value.</p>
</td>
</tr>
<tr id="row62308696112234"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p24415284105356"><a name="p24415284105356"></a><a name="p24415284105356"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p14102386114022"><a name="p14102386114022"></a><a name="p14102386114022"></a>AS.4004</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p47267125112234"><a name="p47267125112234"></a><a name="p47267125112234"></a>The <strong id="b3577853102946"><a name="b3577853102946"></a><a name="b3577853102946"></a>health_status</strong> value in the instance request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p46910748173036"><a name="p46910748173036"></a><a name="p46910748173036"></a>The value of parameter health_status in the request for the instance is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p65030484203333"><a name="p65030484203333"></a><a name="p65030484203333"></a>Use a valid <strong>health_status</strong> value.</p>
</td>
</tr>
<tr id="row35649107115840"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p14893145105356"><a name="p14893145105356"></a><a name="p14893145105356"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p40761235115947"><a name="p40761235115947"></a><a name="p40761235115947"></a>AS.4005</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p19405330115840"><a name="p19405330115840"></a><a name="p19405330115840"></a>The <strong id="b35610086102958"><a name="b35610086102958"></a><a name="b35610086102958"></a>scaling_group_id</strong> in the instance request does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p39523847173036"><a name="p39523847173036"></a><a name="p39523847173036"></a>Parameter scaling_group_id in the request for the instance does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p8960836203354"><a name="p8960836203354"></a><a name="p8960836203354"></a>Use a correct <strong>scaling_group_id</strong>.</p>
</td>
</tr>
<tr id="row25572498115842"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p52576160105356"><a name="p52576160105356"></a><a name="p52576160105356"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p52822553115947"><a name="p52822553115947"></a><a name="p52822553115947"></a>AS.4006</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p9005439115842"><a name="p9005439115842"></a><a name="p9005439115842"></a>The instance does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p23182355173036"><a name="p23182355173036"></a><a name="p23182355173036"></a>The instance does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p23948143203354"><a name="p23948143203354"></a><a name="p23948143203354"></a>Use a correct instance ID.</p>
</td>
</tr>
<tr id="row43184896115842"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p8859707105356"><a name="p8859707105356"></a><a name="p8859707105356"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p54262590115947"><a name="p54262590115947"></a><a name="p54262590115947"></a>AS.4007</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p2478963115842"><a name="p2478963115842"></a><a name="p2478963115842"></a>The value of the parameter that specifies whether to delete the instance is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p55612057173036"><a name="p55612057173036"></a><a name="p55612057173036"></a>The value of the parameter that specifies whether to delete the instance is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p21278784203354"><a name="p21278784203354"></a><a name="p21278784203354"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row25924595184553"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p16275813105356"><a name="p16275813105356"></a><a name="p16275813105356"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p629840618468"><a name="p629840618468"></a><a name="p629840618468"></a>AS.4008</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p4040886818468"><a name="p4040886818468"></a><a name="p4040886818468"></a>The start time format of the log about the expected number of the instances is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p7436222173036"><a name="p7436222173036"></a><a name="p7436222173036"></a>The start time format of the log about the expected number of the instances is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p55996582203354"><a name="p55996582203354"></a><a name="p55996582203354"></a>Use a correct format.</p>
</td>
</tr>
<tr id="row66937130184555"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p53908001105356"><a name="p53908001105356"></a><a name="p53908001105356"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p6438272818468"><a name="p6438272818468"></a><a name="p6438272818468"></a>AS.4009</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p4761849718468"><a name="p4761849718468"></a><a name="p4761849718468"></a>The end time format of the log about expected number of the instances is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p52297004173036"><a name="p52297004173036"></a><a name="p52297004173036"></a>The end time format of the log about expected number of the instances is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p22616856203354"><a name="p22616856203354"></a><a name="p22616856203354"></a>Use a correct format.</p>
</td>
</tr>
<tr id="row25913833184556"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p40247803105356"><a name="p40247803105356"></a><a name="p40247803105356"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p1860170618468"><a name="p1860170618468"></a><a name="p1860170618468"></a>AS.4010</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p3034319018468"><a name="p3034319018468"></a><a name="p3034319018468"></a>The <strong>start_number</strong> in the request for the log about the expected number of instances is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p6681302173036"><a name="p6681302173036"></a><a name="p6681302173036"></a>Parameter start_number in the request for the log about the expected number of instances is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p10169171313"><a name="p10169171313"></a><a name="p10169171313"></a>Use a valid <strong id="b185842291517"><a name="b185842291517"></a><a name="b185842291517"></a>start_number</strong> value.</p>
</td>
</tr>
<tr id="row962224184557"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p14074820105356"><a name="p14074820105356"></a><a name="p14074820105356"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p4136984718468"><a name="p4136984718468"></a><a name="p4136984718468"></a>AS.4011</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p6262333018468"><a name="p6262333018468"></a><a name="p6262333018468"></a>The value of <strong>limit</strong> in the request for the log about the expected number of instances is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p38831031173036"><a name="p38831031173036"></a><a name="p38831031173036"></a>The value of parameter limit in the request for the log about the expected number of instances is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p10291226035"><a name="p10291226035"></a><a name="p10291226035"></a>Use a valid <strong id="b149591146141518"><a name="b149591146141518"></a><a name="b149591146141518"></a>limit</strong> value.</p>
</td>
</tr>
<tr id="row32554367184558"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p22606030105444"><a name="p22606030105444"></a><a name="p22606030105444"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p1838051818468"><a name="p1838051818468"></a><a name="p1838051818468"></a>AS.4012</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p1242698518468"><a name="p1242698518468"></a><a name="p1242698518468"></a>The <strong>logId</strong> in the request for the log about the expected number of instances is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p54989970173036"><a name="p54989970173036"></a><a name="p54989970173036"></a>The value of parameter logId in the request for the log about the expected number of instances is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p13823528137"><a name="p13823528137"></a><a name="p13823528137"></a>Use a valid <strong id="b17001441121618"><a name="b17001441121618"></a><a name="b17001441121618"></a>logId</strong> value.</p>
</td>
</tr>
<tr id="row65654154115842"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p38124863105444"><a name="p38124863105444"></a><a name="p38124863105444"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p30307500115947"><a name="p30307500115947"></a><a name="p30307500115947"></a>AS.4013</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p52218842115842"><a name="p52218842115842"></a><a name="p52218842115842"></a>The list of instances to be deleted is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p23696562173036"><a name="p23696562173036"></a><a name="p23696562173036"></a>The list of instances to be deleted is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p3890656611042"><a name="p3890656611042"></a><a name="p3890656611042"></a>Add instances to be deleted.</p>
</td>
</tr>
<tr id="row25466015115842"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p9955774105444"><a name="p9955774105444"></a><a name="p9955774105444"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p15351382115947"><a name="p15351382115947"></a><a name="p15351382115947"></a>AS.4014</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p48565314115842"><a name="p48565314115842"></a><a name="p48565314115842"></a>The instances do not belong to the same AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p27816107173036"><a name="p27816107173036"></a><a name="p27816107173036"></a>The instances do not belong to the same AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4294650811042"><a name="p4294650811042"></a><a name="p4294650811042"></a>Select instances in the same AS group.</p>
</td>
</tr>
<tr id="row636161115842"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p10002037105444"><a name="p10002037105444"></a><a name="p10002037105444"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p51086135115947"><a name="p51086135115947"></a><a name="p51086135115947"></a>AS.4015</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p13108814115842"><a name="p13108814115842"></a><a name="p13108814115842"></a>The instance is not in <strong id="b65909870101744"><a name="b65909870101744"></a><a name="b65909870101744"></a>inservice</strong> state.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p11065110173036"><a name="p11065110173036"></a><a name="p11065110173036"></a>The instance is not in the inservice status.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p10383145393716"><a name="p10383145393716"></a><a name="p10383145393716"></a>Select an <strong id="b842352706194944"><a name="b842352706194944"></a><a name="b842352706194944"></a>inservice</strong> instance.</p>
</td>
</tr>
<tr id="row10132970115843"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p43728345105444"><a name="p43728345105444"></a><a name="p43728345105444"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p63481874115947"><a name="p63481874115947"></a><a name="p63481874115947"></a>AS.4016</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p44645846115843"><a name="p44645846115843"></a><a name="p44645846115843"></a>The instance cannot be deleted because it is charged by month or year.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p13401944173036"><a name="p13401944173036"></a><a name="p13401944173036"></a>Failed to delete the instance because the instance is charged by month or year.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p62704453203724"><a name="p62704453203724"></a><a name="p62704453203724"></a>Refer to the error code description.</p>
</td>
</tr>
<tr id="row33011049115843"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1253732105444"><a name="p1253732105444"></a><a name="p1253732105444"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p40279090115947"><a name="p40279090115947"></a><a name="p40279090115947"></a>AS.4017</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p25188681115843"><a name="p25188681115843"></a><a name="p25188681115843"></a>The requested instance is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p39232091173036"><a name="p39232091173036"></a><a name="p39232091173036"></a>The requested instance is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p68829241386"><a name="p68829241386"></a><a name="p68829241386"></a>Enter a valid instance.</p>
</td>
</tr>
<tr id="row35686145115843"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p41556058105444"><a name="p41556058105444"></a><a name="p41556058105444"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p36883499115947"><a name="p36883499115947"></a><a name="p36883499115947"></a>AS.4018</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p61084749115843"><a name="p61084749115843"></a><a name="p61084749115843"></a>The value of the request body action of the batch instance operation is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p11818321173036"><a name="p11818321173036"></a><a name="p11818321173036"></a>The action of the body in the request to operate the instance is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p54771728203724"><a name="p54771728203724"></a><a name="p54771728203724"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row47910281115843"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p28268676105444"><a name="p28268676105444"></a><a name="p28268676105444"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p44525206115947"><a name="p44525206115947"></a><a name="p44525206115947"></a>AS.4019</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p1440111115843"><a name="p1440111115843"></a><a name="p1440111115843"></a>The list of instances to be added to the AS group is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p25622136173036"><a name="p25622136173036"></a><a name="p25622136173036"></a>The list of instances to be added to the AS group is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p16699114164013"><a name="p16699114164013"></a><a name="p16699114164013"></a>Enter a valid instance.</p>
</td>
</tr>
<tr id="row54118695115843"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p5443830105444"><a name="p5443830105444"></a><a name="p5443830105444"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p45294296115947"><a name="p45294296115947"></a><a name="p45294296115947"></a>AS.4020</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p66872781115843"><a name="p66872781115843"></a><a name="p66872781115843"></a>The AZ to which the instance belongs is different from the AZ to which the AS group belongs.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p22272976173036"><a name="p22272976173036"></a><a name="p22272976173036"></a>The AZ to which the instance belongs is not within the AZ in the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1911172112418"><a name="p1911172112418"></a><a name="p1911172112418"></a>Select a proper instance for the AZ.</p>
</td>
</tr>
<tr id="row3008667115843"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p9129676105444"><a name="p9129676105444"></a><a name="p9129676105444"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p1980891115947"><a name="p1980891115947"></a><a name="p1980891115947"></a>AS.4021</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p9863207115843"><a name="p9863207115843"></a><a name="p9863207115843"></a>The VPC to which the instance belongs is different from the VPC in the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p63763429173036"><a name="p63763429173036"></a><a name="p63763429173036"></a>The VPC to which the instance belongs is different from the VPC in the AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p58632047154119"><a name="p58632047154119"></a><a name="p58632047154119"></a>Select a proper instance for the VPC.</p>
</td>
</tr>
<tr id="row56047273115844"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p11756520105444"><a name="p11756520105444"></a><a name="p11756520105444"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p34783441115947"><a name="p34783441115947"></a><a name="p34783441115947"></a>AS.4022</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p36694565115844"><a name="p36694565115844"></a><a name="p36694565115844"></a>The number of instances added to the AS group exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p44206218173036"><a name="p44206218173036"></a><a name="p44206218173036"></a>The number of instances added to the AS group exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p13541848134211"><a name="p13541848134211"></a><a name="p13541848134211"></a>Add a proper number of instances.</p>
</td>
</tr>
<tr id="row984878115844"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p47677364105444"><a name="p47677364105444"></a><a name="p47677364105444"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p57087480115947"><a name="p57087480115947"></a><a name="p57087480115947"></a>AS.4023</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p19337727115844"><a name="p19337727115844"></a><a name="p19337727115844"></a>The added instance already exists.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p14078875173036"><a name="p14078875173036"></a><a name="p14078875173036"></a>The added instance has already existed.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p51671313203748"><a name="p51671313203748"></a><a name="p51671313203748"></a>Select another valid instance.</p>
</td>
</tr>
<tr id="row23721093115844"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p61516261105444"><a name="p61516261105444"></a><a name="p61516261105444"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p9277264115947"><a name="p9277264115947"></a><a name="p9277264115947"></a>AS.4024</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p8635979115844"><a name="p8635979115844"></a><a name="p8635979115844"></a>The added instance is not in the active state.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p62952890173036"><a name="p62952890173036"></a><a name="p62952890173036"></a>The instance is not in the active status.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p13526192413431"><a name="p13526192413431"></a><a name="p13526192413431"></a>Select an <strong id="b797771990"><a name="b797771990"></a><a name="b797771990"></a>active</strong> instance.</p>
</td>
</tr>
<tr id="row52793879115844"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p5034255410559"><a name="p5034255410559"></a><a name="p5034255410559"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p31654922115947"><a name="p31654922115947"></a><a name="p31654922115947"></a>AS.4026</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p31799178115844"><a name="p31799178115844"></a><a name="p31799178115844"></a>The number of instances deleted exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p57302801173036"><a name="p57302801173036"></a><a name="p57302801173036"></a>The number of instances deleted exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p101971694447"><a name="p101971694447"></a><a name="p101971694447"></a>Delete a proper number of instances.</p>
</td>
</tr>
<tr id="row27154546115845"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p5828213410559"><a name="p5828213410559"></a><a name="p5828213410559"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p58098459115947"><a name="p58098459115947"></a><a name="p58098459115947"></a>AS.4027</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p54051262115845"><a name="p54051262115845"></a><a name="p54051262115845"></a>The instance has already been added to another AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p32029205173036"><a name="p32029205173036"></a><a name="p32029205173036"></a>The added instance has already existed in other AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p934912017459"><a name="p934912017459"></a><a name="p934912017459"></a>Select another valid instance.</p>
</td>
</tr>
<tr id="row13154205472519"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p171741829261"><a name="p171741829261"></a><a name="p171741829261"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p117519272614"><a name="p117519272614"></a><a name="p117519272614"></a>AS.4028</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p4175152192611"><a name="p4175152192611"></a><a name="p4175152192611"></a>The instance ID cannot be left blank.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p26221539152614"><a name="p26221539152614"></a><a name="p26221539152614"></a>The AS instance ID cannot be null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p19835643172611"><a name="p19835643172611"></a><a name="p19835643172611"></a>Use a correct instance ID.</p>
</td>
</tr>
<tr id="row59555326184648"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p2380850310559"><a name="p2380850310559"></a><a name="p2380850310559"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p45805498184650"><a name="p45805498184650"></a><a name="p45805498184650"></a>AS.4029</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p3388049019137"><a name="p3388049019137"></a><a name="p3388049019137"></a>Failed to batch add instances.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p6709462173036"><a name="p6709462173036"></a><a name="p6709462173036"></a>Failed to add instances in a batch.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p43261936203832"><a name="p43261936203832"></a><a name="p43261936203832"></a>If this error code is returned, use parameter <strong id="b1895814628"><a name="b1895814628"></a><a name="b1895814628"></a>Message</strong> to obtain the instance ID and the failure cause.</p>
</td>
</tr>
<tr id="row59978491184648"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p4231234510559"><a name="p4231234510559"></a><a name="p4231234510559"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p13230999184650"><a name="p13230999184650"></a><a name="p13230999184650"></a>AS.4030</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p33271843191310"><a name="p33271843191310"></a><a name="p33271843191310"></a>Failed to delete ECSs in batches.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p59359648173036"><a name="p59359648173036"></a><a name="p59359648173036"></a>Failed to delete instances in a batch.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p5613706811042"><a name="p5613706811042"></a><a name="p5613706811042"></a>If this error code is returned, use parameter <strong id="b1303991816"><a name="b1303991816"></a><a name="b1303991816"></a>Message</strong> to obtain the instance ID and the failure cause.</p>
</td>
</tr>
<tr id="row3770707104551"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p5421010561"><a name="p5421010561"></a><a name="p5421010561"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p36991827104551"><a name="p36991827104551"></a><a name="p36991827104551"></a>AS.4032</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p43548020104551"><a name="p43548020104551"></a><a name="p43548020104551"></a>The list of instances is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p55075250173036"><a name="p55075250173036"></a><a name="p55075250173036"></a>The list of instances is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4755057203838"><a name="p4755057203838"></a><a name="p4755057203838"></a>Refer to the error code description.</p>
</td>
</tr>
<tr id="row1770677610462"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p3951934210561"><a name="p3951934210561"></a><a name="p3951934210561"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p2496273410462"><a name="p2496273410462"></a><a name="p2496273410462"></a>AS.4033</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p871561010462"><a name="p871561010462"></a><a name="p871561010462"></a>Failed to set instance protection in a batch.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p18757160173036"><a name="p18757160173036"></a><a name="p18757160173036"></a>Failed to set instance protection in a batch.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p48823388203838"><a name="p48823388203838"></a><a name="p48823388203838"></a>If this error code is returned, use parameter <strong id="b1028311042"><a name="b1028311042"></a><a name="b1028311042"></a>Message</strong> to obtain the instance ID and the failure cause.</p>
</td>
</tr>
<tr id="row19247125713422"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p3248145704211"><a name="p3248145704211"></a><a name="p3248145704211"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p0248757144215"><a name="p0248757144215"></a><a name="p0248757144215"></a>AS.4043</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p14248105716429"><a name="p14248105716429"></a><a name="p14248105716429"></a>The number of instances for batch operations exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p192480574424"><a name="p192480574424"></a><a name="p192480574424"></a>The number of instances exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p5248155714424"><a name="p5248155714424"></a><a name="p5248155714424"></a>Ensure that the number of instances for batch operations is no more than 10 at a time.</p>
</td>
</tr>
<tr id="row26023119174720"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p2939172310561"><a name="p2939172310561"></a><a name="p2939172310561"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p27497907174720"><a name="p27497907174720"></a><a name="p27497907174720"></a>AS.7012</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p12737958174720"><a name="p12737958174720"></a><a name="p12737958174720"></a>The ELB listener does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p64864033173036"><a name="p64864033173036"></a><a name="p64864033173036"></a>The ELB listener is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p41574405203942"><a name="p41574405203942"></a><a name="p41574405203942"></a>Modify the ELB listener information.</p>
</td>
</tr>
<tr id="row451383520181"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1883902110561"><a name="p1883902110561"></a><a name="p1883902110561"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p3007634120181"><a name="p3007634120181"></a><a name="p3007634120181"></a>AS.7019</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p2026457620181"><a name="p2026457620181"></a><a name="p2026457620181"></a>Private IP addresses in the subnet are insufficient.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p41240337173036"><a name="p41240337173036"></a><a name="p41240337173036"></a>The number of private IP addresses in the subnet is insufficient.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p50247206203942"><a name="p50247206203942"></a><a name="p50247206203942"></a>Modify the subnet information and enable the AS group.</p>
</td>
</tr>
<tr id="row29405392153842"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p4343874910561"><a name="p4343874910561"></a><a name="p4343874910561"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p63357528153847"><a name="p63357528153847"></a><a name="p63357528153847"></a>AS.7022</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p31686154153847"><a name="p31686154153847"></a><a name="p31686154153847"></a>The SSH key of the AS configuration does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p66544035173036"><a name="p66544035173036"></a><a name="p66544035173036"></a>The key pair does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p15642270203939"><a name="p15642270203939"></a><a name="p15642270203939"></a>Replace the AS configuration in the AS group.</p>
</td>
</tr>
<tr id="row33917172105115"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p61711135105723"><a name="p61711135105723"></a><a name="p61711135105723"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p62936427105115"><a name="p62936427105115"></a><a name="p62936427105115"></a>AS.7044</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p64685855105115"><a name="p64685855105115"></a><a name="p64685855105115"></a>The tag of this resource is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p45144849173036"><a name="p45144849173036"></a><a name="p45144849173036"></a>The tag of this resource is null</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p76307909158"><a name="p76307909158"></a><a name="p76307909158"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row13193203105120"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p24479140105723"><a name="p24479140105723"></a><a name="p24479140105723"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p62016511105120"><a name="p62016511105120"></a><a name="p62016511105120"></a>AS.7045</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p57281455105120"><a name="p57281455105120"></a><a name="p57281455105120"></a>The number of tags exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p27252029173036"><a name="p27252029173036"></a><a name="p27252029173036"></a>The number of tags exceeded.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p433095649158"><a name="p433095649158"></a><a name="p433095649158"></a>Add a maximum of 10 tags.</p>
</td>
</tr>
<tr id="row92888464112"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p3975135813115"><a name="p3975135813115"></a><a name="p3975135813115"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p18975195814118"><a name="p18975195814118"></a><a name="p18975195814118"></a>AS.7046</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p1297615583117"><a name="p1297615583117"></a><a name="p1297615583117"></a>The tag is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p18993173211910"><a name="p18993173211910"></a><a name="p18993173211910"></a>The tags in the resource is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1433122810417"><a name="p1433122810417"></a><a name="p1433122810417"></a>Use a valid tag.</p>
</td>
</tr>
<tr id="row9864098105155"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p61444192105723"><a name="p61444192105723"></a><a name="p61444192105723"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p60794470105155"><a name="p60794470105155"></a><a name="p60794470105155"></a>AS.7047</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p25405067105155"><a name="p25405067105155"></a><a name="p25405067105155"></a>The tag value is too long.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p2505717173036"><a name="p2505717173036"></a><a name="p2505717173036"></a>The value of tag in the resource is too long.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p598793589158"><a name="p598793589158"></a><a name="p598793589158"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row26814411105158"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p31204080105723"><a name="p31204080105723"></a><a name="p31204080105723"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p24483712105158"><a name="p24483712105158"></a><a name="p24483712105158"></a>AS.7048</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p37023678105158"><a name="p37023678105158"></a><a name="p37023678105158"></a>The resource type in this operation with tag is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p14728628173036"><a name="p14728628173036"></a><a name="p14728628173036"></a>The resource type in this operation with tag is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p614826999158"><a name="p614826999158"></a><a name="p614826999158"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row1534337110523"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p64978357105723"><a name="p64978357105723"></a><a name="p64978357105723"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p3485350410523"><a name="p3485350410523"></a><a name="p3485350410523"></a>AS.7049</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p456155310523"><a name="p456155310523"></a><a name="p456155310523"></a>The action in this operation with tag is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p66860733173036"><a name="p66860733173036"></a><a name="p66860733173036"></a>The action in this operation with tag is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p6405691891611"><a name="p6405691891611"></a><a name="p6405691891611"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row5951705110527"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p57473692105723"><a name="p57473692105723"></a><a name="p57473692105723"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p5615186610527"><a name="p5615186610527"></a><a name="p5615186610527"></a>AS.7050</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p5200733010527"><a name="p5200733010527"></a><a name="p5200733010527"></a>The key of tag is duplicate.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p20439515173036"><a name="p20439515173036"></a><a name="p20439515173036"></a>The key of tag cannot be duplicate.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p5473638291611"><a name="p5473638291611"></a><a name="p5473638291611"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row7668103114111"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p7668143114117"><a name="p7668143114117"></a><a name="p7668143114117"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p126685315111"><a name="p126685315111"></a><a name="p126685315111"></a>AS.7052</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p56686318118"><a name="p56686318118"></a><a name="p56686318118"></a>The <strong id="b979291912114"><a name="b979291912114"></a><a name="b979291912114"></a>matches</strong> value is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p066833111117"><a name="p066833111117"></a><a name="p066833111117"></a>The matches in the resource is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1466893112110"><a name="p1466893112110"></a><a name="p1466893112110"></a>Use a valid <strong id="b464223931812"><a name="b464223931812"></a><a name="b464223931812"></a>matches</strong> value.</p>
</td>
</tr>
<tr id="row18475121755719"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p0645132245718"><a name="p0645132245718"></a><a name="p0645132245718"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p5646152214576"><a name="p5646152214576"></a><a name="p5646152214576"></a>AS.7054</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p156461822145712"><a name="p156461822145712"></a><a name="p156461822145712"></a>A key in the tag has duplicate values.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p263116393581"><a name="p263116393581"></a><a name="p263116393581"></a>The value of tag cannot be duplicate.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1864652235710"><a name="p1864652235710"></a><a name="p1864652235710"></a>Check and change the duplicate values in the tag.</p>
</td>
</tr>
<tr id="row1180123013595"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1215905035914"><a name="p1215905035914"></a><a name="p1215905035914"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p115965019593"><a name="p115965019593"></a><a name="p115965019593"></a>AS.7059</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p1716045016594"><a name="p1716045016594"></a><a name="p1716045016594"></a>The selected enterprise project does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p181606509592"><a name="p181606509592"></a><a name="p181606509592"></a>The enterprise project does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p0105921656"><a name="p0105921656"></a><a name="p0105921656"></a>Use an existing enterprise project.</p>
</td>
</tr>
<tr id="row16686153505915"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p1825965275911"><a name="p1825965275911"></a><a name="p1825965275911"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p226015214596"><a name="p226015214596"></a><a name="p226015214596"></a>AS.7060</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p32603521594"><a name="p32603521594"></a><a name="p32603521594"></a>The enterprise project is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p209020461724"><a name="p209020461724"></a><a name="p209020461724"></a>The enterprise project is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p107891252151220"><a name="p107891252151220"></a><a name="p107891252151220"></a>Use an available enterprise project.</p>
</td>
</tr>
<tr id="row163971628461"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p93979284619"><a name="p93979284619"></a><a name="p93979284619"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p450715501974"><a name="p450715501974"></a><a name="p450715501974"></a>AS.7061</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p1939715285616"><a name="p1939715285616"></a><a name="p1939715285616"></a>The value of the tag is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p1239772812611"><a name="p1239772812611"></a><a name="p1239772812611"></a>The value of scaling tag is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p133971328566"><a name="p133971328566"></a><a name="p133971328566"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row1342912331466"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p17429733265"><a name="p17429733265"></a><a name="p17429733265"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p104291433566"><a name="p104291433566"></a><a name="p104291433566"></a>AS.7062</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p134294338620"><a name="p134294338620"></a><a name="p134294338620"></a>The key of the tag is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p1442910331661"><a name="p1442910331661"></a><a name="p1442910331661"></a>The key of scaling tag is null.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p11429933963"><a name="p11429933963"></a><a name="p11429933963"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row839710360618"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p93976361262"><a name="p93976361262"></a><a name="p93976361262"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p53973361160"><a name="p53973361160"></a><a name="p53973361160"></a>AS.7063</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p1239710362064"><a name="p1239710362064"></a><a name="p1239710362064"></a>The tag key is too long.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p163976361761"><a name="p163976361761"></a><a name="p163976361761"></a>The key of scaling tag is too long.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p11397113619612"><a name="p11397113619612"></a><a name="p11397113619612"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row199314035920"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p203131566014"><a name="p203131566014"></a><a name="p203131566014"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p153141366010"><a name="p153141366010"></a><a name="p153141366010"></a>AS.7065</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p13314261102"><a name="p13314261102"></a><a name="p13314261102"></a>The request parameter <strong id="b611412611343"><a name="b611412611343"></a><a name="b611412611343"></a>enterprise_project_id</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p5380548636"><a name="p5380548636"></a><a name="p5380548636"></a>The value of parameter enterprise_project_id in the request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1131496601"><a name="p1131496601"></a><a name="p1131496601"></a>Use a valid <strong id="b3366612113410"><a name="b3366612113410"></a><a name="b3366612113410"></a>enterprise_project_id</strong>.</p>
</td>
</tr>
<tr id="row59547105115847"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p61116610105748"><a name="p61116610105748"></a><a name="p61116610105748"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p13194531115947"><a name="p13194531115947"></a><a name="p13194531115947"></a>AS.7111</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p47861034115847"><a name="p47861034115847"></a><a name="p47861034115847"></a>The ECS quota is insufficient.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p2239266173036"><a name="p2239266173036"></a><a name="p2239266173036"></a>Insufficient instance quota.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p3019396311042"><a name="p3019396311042"></a><a name="p3019396311042"></a>Release idle ECSs or apply for a higher ECS quota.</p>
</td>
</tr>
<tr id="row10653656115847"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p60832406105748"><a name="p60832406105748"></a><a name="p60832406105748"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p22246243115947"><a name="p22246243115947"></a><a name="p22246243115947"></a>AS.7112</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p38310835115847"><a name="p38310835115847"></a><a name="p38310835115847"></a>The disk capacity quota is insufficient.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p21812395173036"><a name="p21812395173036"></a><a name="p21812395173036"></a>Insufficient volume quota.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p6680112611042"><a name="p6680112611042"></a><a name="p6680112611042"></a>Release idle ECSs or increase the upper limit of disks.</p>
</td>
</tr>
<tr id="row6261694172736"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p54973860105748"><a name="p54973860105748"></a><a name="p54973860105748"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p37435207172736"><a name="p37435207172736"></a><a name="p37435207172736"></a>AS.7113</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p12352961172736"><a name="p12352961172736"></a><a name="p12352961172736"></a>The EIP quota is insufficient.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p63544667173036"><a name="p63544667173036"></a><a name="p63544667173036"></a>Insufficient elastic ip quota.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4409511611042"><a name="p4409511611042"></a><a name="p4409511611042"></a>Release idle EIPs or increase the upper limit of EIPs.</p>
</td>
</tr>
<tr id="row25881807173537"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p11952657105748"><a name="p11952657105748"></a><a name="p11952657105748"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p16051597173537"><a name="p16051597173537"></a><a name="p16051597173537"></a>AS.7114</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p25110947173537"><a name="p25110947173537"></a><a name="p25110947173537"></a>The ECS memory quota is insufficient.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p18946460173036"><a name="p18946460173036"></a><a name="p18946460173036"></a>Insufficient ram quota.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p19376611042"><a name="p19376611042"></a><a name="p19376611042"></a>Release idle ECSs or apply for a higher ECS memory quota.</p>
</td>
</tr>
<tr id="row3538771173543"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p56443783105748"><a name="p56443783105748"></a><a name="p56443783105748"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p18205014173543"><a name="p18205014173543"></a><a name="p18205014173543"></a>AS.7115</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p65320001173543"><a name="p65320001173543"></a><a name="p65320001173543"></a>The ECS vCPU quota is insufficient.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p54652449173036"><a name="p54652449173036"></a><a name="p54652449173036"></a>Insufficient cpu quota.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p703796011042"><a name="p703796011042"></a><a name="p703796011042"></a>Release idle ECSs or increase the upper limit of ECS vCPUs.</p>
</td>
</tr>
<tr id="row2361633115847"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p9784313105748"><a name="p9784313105748"></a><a name="p9784313105748"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p44275106115947"><a name="p44275106115947"></a><a name="p44275106115947"></a>AS.9001</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p59635405115847"><a name="p59635405115847"></a><a name="p59635405115847"></a>The format of the start time of the scaling log is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p46079141173036"><a name="p46079141173036"></a><a name="p46079141173036"></a>The format of the start time of the scaling activity log is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p3039975811042"><a name="p3039975811042"></a><a name="p3039975811042"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row28186363115847"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p19224674105748"><a name="p19224674105748"></a><a name="p19224674105748"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p64298045115947"><a name="p64298045115947"></a><a name="p64298045115947"></a>AS.9002</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p45812666115847"><a name="p45812666115847"></a><a name="p45812666115847"></a>The format of the end time for the scaling log is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p37261995173036"><a name="p37261995173036"></a><a name="p37261995173036"></a>The format of the end time for the scaling action log is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p1549871411042"><a name="p1549871411042"></a><a name="p1549871411042"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row1330856115847"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p56143749105748"><a name="p56143749105748"></a><a name="p56143749105748"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p31287893115947"><a name="p31287893115947"></a><a name="p31287893115947"></a>AS.9003</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p7598009115847"><a name="p7598009115847"></a><a name="p7598009115847"></a>The <strong>start_number</strong> in the request for the scaling log is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p4921144781317"><a name="p4921144781317"></a><a name="p4921144781317"></a>The value of parameter start_number in the request for the scaling activity log is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p2427336611042"><a name="p2427336611042"></a><a name="p2427336611042"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row60673383115847"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p4967993710580"><a name="p4967993710580"></a><a name="p4967993710580"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p58969751115947"><a name="p58969751115947"></a><a name="p58969751115947"></a>AS.9004</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p55396362115847"><a name="p55396362115847"></a><a name="p55396362115847"></a>The <strong>limit</strong> in the request for the scaling log is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p1428658173036"><a name="p1428658173036"></a><a name="p1428658173036"></a>The value of parameter limit in the request for the scaling activity log is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p4565317511042"><a name="p4565317511042"></a><a name="p4565317511042"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row56768632115847"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p4499702710580"><a name="p4499702710580"></a><a name="p4499702710580"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p39276021115947"><a name="p39276021115947"></a><a name="p39276021115947"></a>AS.9005</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p4801005115847"><a name="p4801005115847"></a><a name="p4801005115847"></a>The <strong>logId</strong> in the request for the scaling log is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p34858848173036"><a name="p34858848173036"></a><a name="p34858848173036"></a>The value of parameter log_id in the request for the scaling log is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p6227743111042"><a name="p6227743111042"></a><a name="p6227743111042"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row17365573102628"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p2485077810286"><a name="p2485077810286"></a><a name="p2485077810286"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p6675602210286"><a name="p6675602210286"></a><a name="p6675602210286"></a>AS.9007</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p34128148102628"><a name="p34128148102628"></a><a name="p34128148102628"></a>The time format of the AS policy execution log is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p12916599102628"><a name="p12916599102628"></a><a name="p12916599102628"></a>The format of the execute time in the request is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p39611607102628"><a name="p39611607102628"></a><a name="p39611607102628"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row65091720102652"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p6651628110288"><a name="p6651628110288"></a><a name="p6651628110288"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p1910967910288"><a name="p1910967910288"></a><a name="p1910967910288"></a>AS.9008</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p4028196102652"><a name="p4028196102652"></a><a name="p4028196102652"></a>Parameter <strong>start_number</strong> in the AS policy execution log is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p57848446102652"><a name="p57848446102652"></a><a name="p57848446102652"></a>The value of parameter start_number in the request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p55212569102652"><a name="p55212569102652"></a><a name="p55212569102652"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row34052163102633"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p4915265210288"><a name="p4915265210288"></a><a name="p4915265210288"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p2194184510288"><a name="p2194184510288"></a><a name="p2194184510288"></a>AS.9009</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p5580482102633"><a name="p5580482102633"></a><a name="p5580482102633"></a>Parameter <strong>limit</strong> in the AS policy execution log is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p49365912102633"><a name="p49365912102633"></a><a name="p49365912102633"></a>The value of parameter limit in the request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p39215942102633"><a name="p39215942102633"></a><a name="p39215942102633"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row14415490102637"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p2464504210289"><a name="p2464504210289"></a><a name="p2464504210289"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p5009141710289"><a name="p5009141710289"></a><a name="p5009141710289"></a>AS.9010</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p35950732102637"><a name="p35950732102637"></a><a name="p35950732102637"></a>Parameter <strong>logId</strong> in the AS policy execution log is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p8464052191420"><a name="p8464052191420"></a><a name="p8464052191420"></a>The value of parameter log_id in the request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p52209079102637"><a name="p52209079102637"></a><a name="p52209079102637"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row57188228102641"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p2994317410289"><a name="p2994317410289"></a><a name="p2994317410289"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p947805210289"><a name="p947805210289"></a><a name="p947805210289"></a>AS.9011</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p41407093102641"><a name="p41407093102641"></a><a name="p41407093102641"></a>The resource ID in the AS policy execution log is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p127721303159"><a name="p127721303159"></a><a name="p127721303159"></a>The value of parameter scaling_resource_id in the request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p15259301102641"><a name="p15259301102641"></a><a name="p15259301102641"></a>Use a valid value.</p>
</td>
</tr>
<tr id="row4829171214155"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p18293126151"><a name="p18293126151"></a><a name="p18293126151"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p1982991213156"><a name="p1982991213156"></a><a name="p1982991213156"></a>AS.9012</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p882931216151"><a name="p882931216151"></a><a name="p882931216151"></a>The <strong id="b18647185916349"><a name="b18647185916349"></a><a name="b18647185916349"></a>type</strong> in the request for the scaling action log is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p10829712121515"><a name="p10829712121515"></a><a name="p10829712121515"></a>The value of parameter type in the request for the scaling activity log is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p67691839151518"><a name="p67691839151518"></a><a name="p67691839151518"></a>Use a valid <strong id="b1587092003412"><a name="b1587092003412"></a><a name="b1587092003412"></a>type</strong> value.</p>
</td>
</tr>
<tr id="row99081722121514"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="p16908142213153"><a name="p16908142213153"></a><a name="p16908142213153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.2 "><p id="p139081622131515"><a name="p139081622131515"></a><a name="p139081622131515"></a>AS.9013</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.6.1.3 "><p id="p159081822111519"><a name="p159081822111519"></a><a name="p159081822111519"></a>The <strong id="b171041955153514"><a name="b171041955153514"></a><a name="b171041955153514"></a>status</strong> in the request for the scaling action log is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.6.1.4 "><p id="p59081522131511"><a name="p59081522131511"></a><a name="p59081522131511"></a>The value of parameter status in the request for the scaling activity log is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.6.1.5 "><p id="p19129841101516"><a name="p19129841101516"></a><a name="p19129841101516"></a>Use a valid <strong id="b11759185312341"><a name="b11759185312341"></a><a name="b11759185312341"></a>status</strong> value.</p>
</td>
</tr>
</tbody>
</table>

