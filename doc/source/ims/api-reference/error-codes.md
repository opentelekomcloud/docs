# Error Codes<a name="EN-US_TOPIC_0022473689"></a>

## Function Description<a name="section6144247617754"></a>

If the returned status code is  **400**, a customized error message will be returned. This section describes the meaning of each status code.

## Response Format<a name="section2995295617754"></a>

```
STATUS CODE 400
```

```
{
    "error": {
        "message": "The imagetype is invalid.",
        "code": "IMG.0024"
    }
}
```

## Error Message Description<a name="section3932856217754"></a>

**Table  1**  Error code description

<a name="table22139774114422"></a>
<table><thead align="left"><tr id="row25421928114422"><th class="cellrowborder" valign="top" width="11.65%" id="mcps1.2.6.1.1"><p id="p55374399114435"><a name="p55374399114435"></a><a name="p55374399114435"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="11.12%" id="mcps1.2.6.1.2"><p id="p56141312114435"><a name="p56141312114435"></a><a name="p56141312114435"></a><strong id="b38375206162752"><a name="b38375206162752"></a><a name="b38375206162752"></a>Error Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="22.7%" id="mcps1.2.6.1.3"><p id="p51152455114435"><a name="p51152455114435"></a><a name="p51152455114435"></a><strong id="b40144794162610"><a name="b40144794162610"></a><a name="b40144794162610"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.87%" id="mcps1.2.6.1.4"><p id="p83051937597"><a name="p83051937597"></a><a name="p83051937597"></a>Error Message</p>
</th>
<th class="cellrowborder" valign="top" width="30.659999999999997%" id="mcps1.2.6.1.5"><p id="p1399911370354"><a name="p1399911370354"></a><a name="p1399911370354"></a><strong id="b84235270616428"><a name="b84235270616428"></a><a name="b84235270616428"></a>Handling Measure</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row51213039114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p2635184316189"><a name="p2635184316189"></a><a name="p2635184316189"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p66927757114454"><a name="p66927757114454"></a><a name="p66927757114454"></a>IMG.0001</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p37268087115557"><a name="p37268087115557"></a><a name="p37268087115557"></a>The request message format is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1224712610386"><a name="p1224712610386"></a><a name="p1224712610386"></a>The request message format is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p268962613517"><a name="p268962613517"></a><a name="p268962613517"></a>Use the correct format.</p>
</td>
</tr>
<tr id="row4966389114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p12650144312184"><a name="p12650144312184"></a><a name="p12650144312184"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p2190726114454"><a name="p2190726114454"></a><a name="p2190726114454"></a>IMG.0002</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p56454858115557"><a name="p56454858115557"></a><a name="p56454858115557"></a>The image name contains more than 128 characters.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p19261626153818"><a name="p19261626153818"></a><a name="p19261626153818"></a>The image name contains more than 128 characters.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p168913265354"><a name="p168913265354"></a><a name="p168913265354"></a>Reduce the length of the image name.</p>
</td>
</tr>
<tr id="row34443751114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p3650243121816"><a name="p3650243121816"></a><a name="p3650243121816"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p53535690114454"><a name="p53535690114454"></a><a name="p53535690114454"></a>IMG.0003</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p17858010115557"><a name="p17858010115557"></a><a name="p17858010115557"></a>The image name format is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p162741426153819"><a name="p162741426153819"></a><a name="p162741426153819"></a>The image name format is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1689132693510"><a name="p1689132693510"></a><a name="p1689132693510"></a>Check whether the image name is valid.</p>
</td>
</tr>
<tr id="row62203740114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p2667143141818"><a name="p2667143141818"></a><a name="p2667143141818"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p37268733114454"><a name="p37268733114454"></a><a name="p37268733114454"></a>IMG.0004</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p66479188115557"><a name="p66479188115557"></a><a name="p66479188115557"></a>The image name contains more than 1024 characters.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p928811267387"><a name="p928811267387"></a><a name="p928811267387"></a>The description contains more than 1024 characters.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p66891026193514"><a name="p66891026193514"></a><a name="p66891026193514"></a>Reduce the length of the image description to within 1024 characters.</p>
</td>
</tr>
<tr id="row1802929114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p186678439187"><a name="p186678439187"></a><a name="p186678439187"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p56925769114454"><a name="p56925769114454"></a><a name="p56925769114454"></a>IMG.0005</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p10728746115557"><a name="p10728746115557"></a><a name="p10728746115557"></a>The <span id="text1857818111321"><a name="text1857818111321"></a><a name="text1857818111321"></a></span><span id="text19578410323"><a name="text19578410323"></a><a name="text19578410323"></a>ECS</span> does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p630172612384"><a name="p630172612384"></a><a name="p630172612384"></a>The ECS does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p8689132613356"><a name="p8689132613356"></a><a name="p8689132613356"></a>Check whether the <span id="text260296163218"><a name="text260296163218"></a><a name="text260296163218"></a></span><span id="text5602106183210"><a name="text5602106183210"></a><a name="text5602106183210"></a>ECS</span> exists.</p>
</td>
</tr>
<tr id="row139214114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p19682134391817"><a name="p19682134391817"></a><a name="p19682134391817"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p25607969114454"><a name="p25607969114454"></a><a name="p25607969114454"></a>IMG.0006</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p36628055115557"><a name="p36628055115557"></a><a name="p36628055115557"></a>The system disk of the <span id="text14496193173211"><a name="text14496193173211"></a><a name="text14496193173211"></a></span><span id="text2049613323211"><a name="text2049613323211"></a><a name="text2049613323211"></a>ECS</span> cannot be used to create an image.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p3315182617384"><a name="p3315182617384"></a><a name="p3315182617384"></a>The ECS system disk cannot be used to create an image.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p168942616352"><a name="p168942616352"></a><a name="p168942616352"></a>Check the system disk status of the <span id="text115715297531"><a name="text115715297531"></a><a name="text115715297531"></a></span><span id="text3488314534"><a name="text3488314534"></a><a name="text3488314534"></a>ECS</span>.</p>
</td>
</tr>
<tr id="row5245923114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p968220434185"><a name="p968220434185"></a><a name="p968220434185"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p11945472114454"><a name="p11945472114454"></a><a name="p11945472114454"></a>IMG.0007</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p59633566115557"><a name="p59633566115557"></a><a name="p59633566115557"></a>The message body is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p103281926143814"><a name="p103281926143814"></a><a name="p103281926143814"></a>The request body is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p12689162612354"><a name="p12689162612354"></a><a name="p12689162612354"></a>Check whether the message body is valid.</p>
</td>
</tr>
<tr id="row23041829114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1569864331812"><a name="p1569864331812"></a><a name="p1569864331812"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p51205929114454"><a name="p51205929114454"></a><a name="p51205929114454"></a>IMG.0008</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p53435211115557"><a name="p53435211115557"></a><a name="p53435211115557"></a>The <span id="text379743353213"><a name="text379743353213"></a><a name="text379743353213"></a></span><span id="text77971333183215"><a name="text77971333183215"></a><a name="text77971333183215"></a>ECS</span> cannot be used to create an image because it is not in the <strong id="b477438103716"><a name="b477438103716"></a><a name="b477438103716"></a>Stopped</strong> state.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1434212265385"><a name="p1434212265385"></a><a name="p1434212265385"></a>The ECS cannot be used to create images because it is not in stopped state.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p10689122613510"><a name="p10689122613510"></a><a name="p10689122613510"></a>Stop the <span id="text16637104112320"><a name="text16637104112320"></a><a name="text16637104112320"></a></span><span id="text763774112328"><a name="text763774112328"></a><a name="text763774112328"></a>ECS</span> and try again.</p>
</td>
</tr>
<tr id="row33462421114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p19698144316189"><a name="p19698144316189"></a><a name="p19698144316189"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p16594279114454"><a name="p16594279114454"></a><a name="p16594279114454"></a>IMG.0009</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p31127791115557"><a name="p31127791115557"></a><a name="p31127791115557"></a>The image name already exists.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p11355112615383"><a name="p11355112615383"></a><a name="p11355112615383"></a>The image name already exists.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p20689132618352"><a name="p20689132618352"></a><a name="p20689132618352"></a>Change another image name.</p>
</td>
</tr>
<tr id="row50049977114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p12713443191815"><a name="p12713443191815"></a><a name="p12713443191815"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p17634510114454"><a name="p17634510114454"></a><a name="p17634510114454"></a>IMG.0010</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p9364007115557"><a name="p9364007115557"></a><a name="p9364007115557"></a>The <span id="text92651346133212"><a name="text92651346133212"></a><a name="text92651346133212"></a></span><span id="text1026594653210"><a name="text1026594653210"></a><a name="text1026594653210"></a>ECS</span> cannot be used to create an image because it has in-progress tasks.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1136911261388"><a name="p1136911261388"></a><a name="p1136911261388"></a>The ECS cannot be used to create an image because it has in-progress tasks.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p106894266354"><a name="p106894266354"></a><a name="p106894266354"></a>Try again after the tasks are complete.</p>
</td>
</tr>
<tr id="row38768736114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p171310434189"><a name="p171310434189"></a><a name="p171310434189"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p37764983114454"><a name="p37764983114454"></a><a name="p37764983114454"></a>IMG.0011</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p48365908115557"><a name="p48365908115557"></a><a name="p48365908115557"></a><strong id="b84235270614571"><a name="b84235270614571"></a><a name="b84235270614571"></a>forceCreate</strong> must be set to <strong id="b84235270614575"><a name="b84235270614575"></a><a name="b84235270614575"></a>true</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p238232615384"><a name="p238232615384"></a><a name="p238232615384"></a><strong id="b495140235"><a name="b495140235"></a><a name="b495140235"></a>forceCreate</strong> must be set to <strong id="b2021405215"><a name="b2021405215"></a><a name="b2021405215"></a>true</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1668942653519"><a name="p1668942653519"></a><a name="p1668942653519"></a>Set <strong id="b842352706144656"><a name="b842352706144656"></a><a name="b842352706144656"></a>forceCreate</strong> to <strong id="b842352706144659"><a name="b842352706144659"></a><a name="b842352706144659"></a>true</strong>.</p>
</td>
</tr>
<tr id="row21066849114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1772904311186"><a name="p1772904311186"></a><a name="p1772904311186"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p16038983114454"><a name="p16038983114454"></a><a name="p16038983114454"></a>IMG.0012</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p26593891115557"><a name="p26593891115557"></a><a name="p26593891115557"></a>The <span id="text18211115493213"><a name="text18211115493213"></a><a name="text18211115493213"></a></span><span id="text162111954163214"><a name="text162111954163214"></a><a name="text162111954163214"></a>ECS</span> ID is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p64051526133813"><a name="p64051526133813"></a><a name="p64051526133813"></a>The ECS ID is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1568913260354"><a name="p1568913260354"></a><a name="p1568913260354"></a>Enter a valid <span id="text184275589321"><a name="text184275589321"></a><a name="text184275589321"></a></span><span id="text242719587325"><a name="text242719587325"></a><a name="text242719587325"></a>ECS</span> ID.</p>
</td>
</tr>
<tr id="row7548763114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p9729443101819"><a name="p9729443101819"></a><a name="p9729443101819"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p15476648114454"><a name="p15476648114454"></a><a name="p15476648114454"></a>IMG.0013</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p59594118115557"><a name="p59594118115557"></a><a name="p59594118115557"></a>The image name is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p14418192693813"><a name="p14418192693813"></a><a name="p14418192693813"></a>The image name is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p17689026193512"><a name="p17689026193512"></a><a name="p17689026193512"></a>Enter a valid image name.</p>
</td>
</tr>
<tr id="row61393014114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p474584314181"><a name="p474584314181"></a><a name="p474584314181"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p8187469114454"><a name="p8187469114454"></a><a name="p8187469114454"></a>IMG.0014</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p24677368115557"><a name="p24677368115557"></a><a name="p24677368115557"></a>An exception occurred when IaaS OpenStack was executing the task.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1343242653810"><a name="p1343242653810"></a><a name="p1343242653810"></a>An exception occurred when IaaS OpenStack was executing the task.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p8689122643513"><a name="p8689122643513"></a><a name="p8689122643513"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row8707615114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1913515015185"><a name="p1913515015185"></a><a name="p1913515015185"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p63085041114454"><a name="p63085041114454"></a><a name="p63085041114454"></a>IMG.0015</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p4626108115557"><a name="p4626108115557"></a><a name="p4626108115557"></a>The number of private images has reached the quota.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p114461526143813"><a name="p114461526143813"></a><a name="p114461526143813"></a>The number of private images has reached the maximum allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p2689526193510"><a name="p2689526193510"></a><a name="p2689526193510"></a>Increase the quota or delete existing images.</p>
</td>
</tr>
<tr id="row24324047114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1415185017181"><a name="p1415185017181"></a><a name="p1415185017181"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p19423255114454"><a name="p19423255114454"></a><a name="p19423255114454"></a>IMG.0016</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p16990046115557"><a name="p16990046115557"></a><a name="p16990046115557"></a>An error occurred when the request body was deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p124592261384"><a name="p124592261384"></a><a name="p124592261384"></a>An error occurred when the request body was deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p6689226103517"><a name="p6689226103517"></a><a name="p6689226103517"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row28772803114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p7151205071817"><a name="p7151205071817"></a><a name="p7151205071817"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p66691786114454"><a name="p66691786114454"></a><a name="p66691786114454"></a>IMG.0017</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p37712559115557"><a name="p37712559115557"></a><a name="p37712559115557"></a>The URL format is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p11474426143815"><a name="p11474426143815"></a><a name="p11474426143815"></a>The URL format is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1568952633511"><a name="p1568952633511"></a><a name="p1568952633511"></a>Check whether the URL format is valid.</p>
</td>
</tr>
<tr id="row19704516114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p8167650161815"><a name="p8167650161815"></a><a name="p8167650161815"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p31495006114454"><a name="p31495006114454"></a><a name="p31495006114454"></a>IMG.0018</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p44930443115557"><a name="p44930443115557"></a><a name="p44930443115557"></a>An error occurred when the job was submitted.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p8486026153813"><a name="p8486026153813"></a><a name="p8486026153813"></a>An error occurred when the job was submitted.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p2068919269358"><a name="p2068919269358"></a><a name="p2068919269358"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row14646240114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p6182145021815"><a name="p6182145021815"></a><a name="p6182145021815"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p8628012114454"><a name="p8628012114454"></a><a name="p8628012114454"></a>IMG.0019</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p5168022115557"><a name="p5168022115557"></a><a name="p5168022115557"></a>The backup ID is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p050022610383"><a name="p050022610383"></a><a name="p050022610383"></a>The backup ID is not specified.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p11689112623511"><a name="p11689112623511"></a><a name="p11689112623511"></a>Check whether the current backup ID is valid.</p>
</td>
</tr>
<tr id="row55157294114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p11182105012185"><a name="p11182105012185"></a><a name="p11182105012185"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p48696921114454"><a name="p48696921114454"></a><a name="p48696921114454"></a>IMG.0020</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p9392122115557"><a name="p9392122115557"></a><a name="p9392122115557"></a>The backup does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p95132269384"><a name="p95132269384"></a><a name="p95132269384"></a>The backup does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1968912683512"><a name="p1968912683512"></a><a name="p1968912683512"></a>Check whether the backup file exists.</p>
</td>
</tr>
<tr id="row16528014114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1721315014181"><a name="p1721315014181"></a><a name="p1721315014181"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p66575503114454"><a name="p66575503114454"></a><a name="p66575503114454"></a>IMG.0021</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p1753130115557"><a name="p1753130115557"></a><a name="p1753130115557"></a>The source type is unknown.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p17526162612389"><a name="p17526162612389"></a><a name="p17526162612389"></a>The resource type is unknown.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p2068917260354"><a name="p2068917260354"></a><a name="p2068917260354"></a>Select a correct source type.</p>
</td>
</tr>
<tr id="row12103525114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p102297504182"><a name="p102297504182"></a><a name="p102297504182"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p13833153114454"><a name="p13833153114454"></a><a name="p13833153114454"></a>IMG.0022</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p2963617115557"><a name="p2963617115557"></a><a name="p2963617115557"></a>A disk in the current state cannot be used to create images.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p7540122663818"><a name="p7540122663818"></a><a name="p7540122663818"></a>The disk in the current state cannot be used to create images.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p06892268357"><a name="p06892268357"></a><a name="p06892268357"></a>Check the disk status.</p>
</td>
</tr>
<tr id="row63486051114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1722925011818"><a name="p1722925011818"></a><a name="p1722925011818"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p18039018114454"><a name="p18039018114454"></a><a name="p18039018114454"></a>IMG.0023</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p12993442115557"><a name="p12993442115557"></a><a name="p12993442115557"></a>An exception occurred during job query.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1552426153817"><a name="p1552426153817"></a><a name="p1552426153817"></a>An exception occurred during task query.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p86890269353"><a name="p86890269353"></a><a name="p86890269353"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row46226496114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p12451450201813"><a name="p12451450201813"></a><a name="p12451450201813"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p64215757114454"><a name="p64215757114454"></a><a name="p64215757114454"></a>IMG.0024</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p9869816115557"><a name="p9869816115557"></a><a name="p9869816115557"></a>The image type in the request is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1256718260382"><a name="p1256718260382"></a><a name="p1256718260382"></a>The image type in the request is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p7689152673514"><a name="p7689152673514"></a><a name="p7689152673514"></a>Select either BMS or ECS.</p>
</td>
</tr>
<tr id="row16514170114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1727614505189"><a name="p1727614505189"></a><a name="p1727614505189"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p38408885114454"><a name="p38408885114454"></a><a name="p38408885114454"></a>IMG.0025</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p14448055115557"><a name="p14448055115557"></a><a name="p14448055115557"></a>The user type in the request is incorrect. </p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p19579026143817"><a name="p19579026143817"></a><a name="p19579026143817"></a>The user type in the request is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p76893268351"><a name="p76893268351"></a><a name="p76893268351"></a>Check whether the user type is valid.</p>
</td>
</tr>
<tr id="row34026264114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p6276175091816"><a name="p6276175091816"></a><a name="p6276175091816"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p15681334114454"><a name="p15681334114454"></a><a name="p15681334114454"></a>IMG.0026</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p63649528115557"><a name="p63649528115557"></a><a name="p63649528115557"></a>The operator does not have the rights to perform the operation.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p16593152693815"><a name="p16593152693815"></a><a name="p16593152693815"></a>The role is invalid,maybe need to apply for permission or real-name authentication.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p2689122618351"><a name="p2689122618351"></a><a name="p2689122618351"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row54962793114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p19291050191812"><a name="p19291050191812"></a><a name="p19291050191812"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p23185641114454"><a name="p23185641114454"></a><a name="p23185641114454"></a>IMG.0027</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p28281504115557"><a name="p28281504115557"></a><a name="p28281504115557"></a>The image ID in the request does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1760642616389"><a name="p1760642616389"></a><a name="p1760642616389"></a>The image ID in the request does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1068912261353"><a name="p1068912261353"></a><a name="p1068912261353"></a>Use a valid image ID.</p>
</td>
</tr>
<tr id="row50943684114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1849420579188"><a name="p1849420579188"></a><a name="p1849420579188"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p58007859114454"><a name="p58007859114454"></a><a name="p58007859114454"></a>IMG.0028</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p14795545115557"><a name="p14795545115557"></a><a name="p14795545115557"></a>The image in the request is protected.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p9618132653810"><a name="p9618132653810"></a><a name="p9618132653810"></a>The image in the request is protected.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p136891266358"><a name="p136891266358"></a><a name="p136891266358"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row44696136114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p7526155714182"><a name="p7526155714182"></a><a name="p7526155714182"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p9145086114454"><a name="p9145086114454"></a><a name="p9145086114454"></a>IMG.0029</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p48534294115557"><a name="p48534294115557"></a><a name="p48534294115557"></a>The backup in the request has already been used to create an image.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p76331626143816"><a name="p76331626143816"></a><a name="p76331626143816"></a>The backup in the request has already been used to create an image.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p5689192618356"><a name="p5689192618356"></a><a name="p5689192618356"></a>Select another backup that has not been used.</p>
</td>
</tr>
<tr id="row49715868114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1054215771814"><a name="p1054215771814"></a><a name="p1054215771814"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p22990204114454"><a name="p22990204114454"></a><a name="p22990204114454"></a>IMG.0030</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p15129170115557"><a name="p15129170115557"></a><a name="p15129170115557"></a>The project ID and token in the request are invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p14647126103820"><a name="p14647126103820"></a><a name="p14647126103820"></a>The project ID and token in the request are invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p156891326163517"><a name="p156891326163517"></a><a name="p156891326163517"></a>Enter a correct project ID and token.</p>
</td>
</tr>
<tr id="row4141232114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p2054216576185"><a name="p2054216576185"></a><a name="p2054216576185"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p49752299114454"><a name="p49752299114454"></a><a name="p49752299114454"></a>IMG.0031</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p23311440115557"><a name="p23311440115557"></a><a name="p23311440115557"></a>The resource ID in the request is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p5661132610381"><a name="p5661132610381"></a><a name="p5661132610381"></a>The resource ID in the request is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p176891926173513"><a name="p176891926173513"></a><a name="p176891926173513"></a>Use a valid image ID.</p>
</td>
</tr>
<tr id="row3021433114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p2557145714183"><a name="p2557145714183"></a><a name="p2557145714183"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p30639435114454"><a name="p30639435114454"></a><a name="p30639435114454"></a>IMG.0032</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p15497499115557"><a name="p15497499115557"></a><a name="p15497499115557"></a>The backup is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1567492643814"><a name="p1567492643814"></a><a name="p1567492643814"></a>The backup is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p8689152623518"><a name="p8689152623518"></a><a name="p8689152623518"></a>Check whether the backup is available.</p>
</td>
</tr>
<tr id="row468664114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p15573125731810"><a name="p15573125731810"></a><a name="p15573125731810"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p56005416114454"><a name="p56005416114454"></a><a name="p56005416114454"></a>IMG.0033</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p23388167115557"><a name="p23388167115557"></a><a name="p23388167115557"></a>The backup is not a system disk backup.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p96901326133816"><a name="p96901326133816"></a><a name="p96901326133816"></a>The backup is not a system disk backup.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p14689026153519"><a name="p14689026153519"></a><a name="p14689026153519"></a>Check whether the backup is a system disk backup.</p>
</td>
</tr>
<tr id="row38032051114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p19588165714189"><a name="p19588165714189"></a><a name="p19588165714189"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p25759317114454"><a name="p25759317114454"></a><a name="p25759317114454"></a>IMG.0034</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p4322413115557"><a name="p4322413115557"></a><a name="p4322413115557"></a>The number of images cannot be modified.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p127011026143818"><a name="p127011026143818"></a><a name="p127011026143818"></a>The number of images cannot be modified.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p10689726133519"><a name="p10689726133519"></a><a name="p10689726133519"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row31126009114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p45881257101810"><a name="p45881257101810"></a><a name="p45881257101810"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p55169710114454"><a name="p55169710114454"></a><a name="p55169710114454"></a>IMG.0035</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p64031858115557"><a name="p64031858115557"></a><a name="p64031858115557"></a>An attribute conflict occurred during the modification.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1171412266381"><a name="p1171412266381"></a><a name="p1171412266381"></a>An attribute conflict occurred during the modification.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1368912264353"><a name="p1368912264353"></a><a name="p1368912264353"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row31766561114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p106031157191816"><a name="p106031157191816"></a><a name="p106031157191816"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p20509397114454"><a name="p20509397114454"></a><a name="p20509397114454"></a>IMG.0036</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p38564288115557"><a name="p38564288115557"></a><a name="p38564288115557"></a>An error occurred when the value of <strong id="b84235270616410"><a name="b84235270616410"></a><a name="b84235270616410"></a>asumeToken</strong> was obtained. </p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p177291826133819"><a name="p177291826133819"></a><a name="p177291826133819"></a>An error occurred when the value of <strong id="b639544844"><a name="b639544844"></a><a name="b639544844"></a>asumeToken</strong> was obtained.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p15689142643517"><a name="p15689142643517"></a><a name="p15689142643517"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row51680394114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p3620135720186"><a name="p3620135720186"></a><a name="p3620135720186"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p53182708114454"><a name="p53182708114454"></a><a name="p53182708114454"></a>IMG.0037</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p61860938115557"><a name="p61860938115557"></a><a name="p61860938115557"></a>An error occurred in the AK/SK was obtained.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p117455262387"><a name="p117455262387"></a><a name="p117455262387"></a>An error occurred in the AK/SK was obtained.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p66891326163515"><a name="p66891326163515"></a><a name="p66891326163515"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row23580700114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1862085751814"><a name="p1862085751814"></a><a name="p1862085751814"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p48380288114454"><a name="p48380288114454"></a><a name="p48380288114454"></a>IMG.0038</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p66576139115557"><a name="p66576139115557"></a><a name="p66576139115557"></a>An error occurred when the bucket was created.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p28176265385"><a name="p28176265385"></a><a name="p28176265385"></a>An error occurred when the bucket was created.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p16689202613353"><a name="p16689202613353"></a><a name="p16689202613353"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row50879748114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p266717572181"><a name="p266717572181"></a><a name="p266717572181"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p37076979114454"><a name="p37076979114454"></a><a name="p37076979114454"></a>IMG.0039</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p14296774115557"><a name="p14296774115557"></a><a name="p14296774115557"></a>An error occurred when read and write permissions of the bucket were granted to a specified user.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1082982612386"><a name="p1082982612386"></a><a name="p1082982612386"></a>An error occurred when read and write permissions of the bucket was granted to a specified user.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1268972618354"><a name="p1268972618354"></a><a name="p1268972618354"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row58050683114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1068225715180"><a name="p1068225715180"></a><a name="p1068225715180"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p51355025114454"><a name="p51355025114454"></a><a name="p51355025114454"></a>IMG.0040</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p20474566115557"><a name="p20474566115557"></a><a name="p20474566115557"></a>An error occurred in the object storage address was obtained.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p684402612387"><a name="p684402612387"></a><a name="p684402612387"></a>An error occurred in the object storage address was obtained.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1068910265353"><a name="p1068910265353"></a><a name="p1068910265353"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row15122046114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p3698157141817"><a name="p3698157141817"></a><a name="p3698157141817"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p58176035114454"><a name="p58176035114454"></a><a name="p58176035114454"></a>IMG.0041</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p27791263115557"><a name="p27791263115557"></a><a name="p27791263115557"></a>The authorized account is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p685722615384"><a name="p685722615384"></a><a name="p685722615384"></a>The authorized account is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p8689142663519"><a name="p8689142663519"></a><a name="p8689142663519"></a>Use a valid account.</p>
</td>
</tr>
<tr id="row26054550114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p9713115771816"><a name="p9713115771816"></a><a name="p9713115771816"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p64636605114454"><a name="p64636605114454"></a><a name="p64636605114454"></a>IMG.0042</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p60062698115557"><a name="p60062698115557"></a><a name="p60062698115557"></a>The image is not a marketplace image.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p187014265389"><a name="p187014265389"></a><a name="p187014265389"></a>The image is not a Marketplace image.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p136896267350"><a name="p136896267350"></a><a name="p136896267350"></a>Check the operations that can be performed on the image.</p>
</td>
</tr>
<tr id="row35563665114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1871335761812"><a name="p1871335761812"></a><a name="p1871335761812"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p9663099114454"><a name="p9663099114454"></a><a name="p9663099114454"></a>IMG.0043</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p30727948115557"><a name="p30727948115557"></a><a name="p30727948115557"></a>The image has already been published in the Marketplace by others.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p12883182614386"><a name="p12883182614386"></a><a name="p12883182614386"></a>The image has already been published in Marketplace by others.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p19689152663514"><a name="p19689152663514"></a><a name="p19689152663514"></a>Use a compliant image file.</p>
</td>
</tr>
<tr id="row13134918114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1448137161916"><a name="p1448137161916"></a><a name="p1448137161916"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p65077567114454"><a name="p65077567114454"></a><a name="p65077567114454"></a>IMG.0044</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p53422575115557"><a name="p53422575115557"></a><a name="p53422575115557"></a>The image is not the one being published in the Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p889716268388"><a name="p889716268388"></a><a name="p889716268388"></a>The image is not the one being published to Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1168915269352"><a name="p1168915269352"></a><a name="p1168915269352"></a>Check whether the image has been published in the Marketplace.</p>
</td>
</tr>
<tr id="row14180181114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1946318715196"><a name="p1946318715196"></a><a name="p1946318715196"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p62688371114454"><a name="p62688371114454"></a><a name="p62688371114454"></a>IMG.0045</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p21916101115557"><a name="p21916101115557"></a><a name="p21916101115557"></a>Failed to generate the image product code.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p10910172620389"><a name="p10910172620389"></a><a name="p10910172620389"></a>Failed to generate the image product code.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p4689132603514"><a name="p4689132603514"></a><a name="p4689132603514"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row62002659114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p44633761911"><a name="p44633761911"></a><a name="p44633761911"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p65795532114454"><a name="p65795532114454"></a><a name="p65795532114454"></a>IMG.0046</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p4928716115557"><a name="p4928716115557"></a><a name="p4928716115557"></a>The image is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p19234261388"><a name="p19234261388"></a><a name="p19234261388"></a>The image is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p468911264355"><a name="p468911264355"></a><a name="p468911264355"></a>Check the image status.</p>
</td>
</tr>
<tr id="row44094305114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p2047957171918"><a name="p2047957171918"></a><a name="p2047957171918"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p49214468114454"><a name="p49214468114454"></a><a name="p49214468114454"></a>IMG.0047</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p36264196115557"><a name="p36264196115557"></a><a name="p36264196115557"></a>This operation can be performed only by the image owner.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p20937132663816"><a name="p20937132663816"></a><a name="p20937132663816"></a>This operation can be performed only by the image owner.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p86899268353"><a name="p86899268353"></a><a name="p86899268353"></a>Check whether you have the permission to operate the image.</p>
</td>
</tr>
<tr id="row9260100114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1749516711920"><a name="p1749516711920"></a><a name="p1749516711920"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p41214366114454"><a name="p41214366114454"></a><a name="p41214366114454"></a>IMG.0048</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p62815481115557"><a name="p62815481115557"></a><a name="p62815481115557"></a>The operation on the marketplace image is unknown.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p11949122613817"><a name="p11949122613817"></a><a name="p11949122613817"></a>The operation on the Marketplace image is unknown.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p468992612357"><a name="p468992612357"></a><a name="p468992612357"></a>Perform a correct operation.</p>
</td>
</tr>
<tr id="row64846285114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p349515781911"><a name="p349515781911"></a><a name="p349515781911"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p47611302114454"><a name="p47611302114454"></a><a name="p47611302114454"></a>IMG.0049</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p24240766115557"><a name="p24240766115557"></a><a name="p24240766115557"></a>The image has been published in the Marketplace or is being published to Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1696442683819"><a name="p1696442683819"></a><a name="p1696442683819"></a>The image has been published in Marketplace or is being published in Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1968912617351"><a name="p1968912617351"></a><a name="p1968912617351"></a>Do not release the image repeatedly.</p>
</td>
</tr>
<tr id="row64810946114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p145101771914"><a name="p145101771914"></a><a name="p145101771914"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p13356653114454"><a name="p13356653114454"></a><a name="p13356653114454"></a>IMG.0050</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p21887855115557"><a name="p21887855115557"></a><a name="p21887855115557"></a>Image release to Marketplace cannot be set to <strong id="b842352706182712"><a name="b842352706182712"></a><a name="b842352706182712"></a>Failed</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p2978192643815"><a name="p2978192643815"></a><a name="p2978192643815"></a>Failing to publish the image in Marketplace cannot be set.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p10689142613354"><a name="p10689142613354"></a><a name="p10689142613354"></a>Check the operations supported by the image.</p>
</td>
</tr>
<tr id="row18916402114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1451013711192"><a name="p1451013711192"></a><a name="p1451013711192"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p6215248114454"><a name="p6215248114454"></a><a name="p6215248114454"></a>IMG.0051</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p51445870115557"><a name="p51445870115557"></a><a name="p51445870115557"></a>An image created using a CSBS backup cannot be published in the Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p2990142619387"><a name="p2990142619387"></a><a name="p2990142619387"></a>The image created using a CSBS backup cannot be published in Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p6689162615357"><a name="p6689162615357"></a><a name="p6689162615357"></a>Select an image that can be published.</p>
</td>
</tr>
<tr id="row59349300114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1452614761916"><a name="p1452614761916"></a><a name="p1452614761916"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p34622064114454"><a name="p34622064114454"></a><a name="p34622064114454"></a>IMG.0052</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p57293221115557"><a name="p57293221115557"></a><a name="p57293221115557"></a>A shared image cannot be published in the Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p14422793813"><a name="p14422793813"></a><a name="p14422793813"></a>A shared image cannot be published in Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p10689112663518"><a name="p10689112663518"></a><a name="p10689112663518"></a>Select an image that can be published.</p>
</td>
</tr>
<tr id="row66476199114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p152647111913"><a name="p152647111913"></a><a name="p152647111913"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p6552442114454"><a name="p6552442114454"></a><a name="p6552442114454"></a>IMG.0053</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p25045385115557"><a name="p25045385115557"></a><a name="p25045385115557"></a>An error occurred when the domain information of the shadow account was obtained.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p41782713810"><a name="p41782713810"></a><a name="p41782713810"></a>An error occurred when the domain information of the shadow account was obtained.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p8689102673510"><a name="p8689102673510"></a><a name="p8689102673510"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row58438130114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p145421575196"><a name="p145421575196"></a><a name="p145421575196"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p12001376114454"><a name="p12001376114454"></a><a name="p12001376114454"></a>IMG.0054</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p4475284115557"><a name="p4475284115557"></a><a name="p4475284115557"></a>The image description format is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p330127163815"><a name="p330127163815"></a><a name="p330127163815"></a>The image description format is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p16891426133518"><a name="p16891426133518"></a><a name="p16891426133518"></a>Check the image description. It can contain no more than 1024 characters that consist of only letters and digits. Spaces and angle brackets (&lt; &gt;) are not allowed.</p>
</td>
</tr>
<tr id="row21080517114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p654267131918"><a name="p654267131918"></a><a name="p654267131918"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p24851229114454"><a name="p24851229114454"></a><a name="p24851229114454"></a>IMG.0055</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p41257226115557"><a name="p41257226115557"></a><a name="p41257226115557"></a>The memory or disk size is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p14416271381"><a name="p14416271381"></a><a name="p14416271381"></a>The memory or disk size is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p19690192673515"><a name="p19690192673515"></a><a name="p19690192673515"></a>Check the memory (MB) or disk size (GB) supported by the image.</p>
</td>
</tr>
<tr id="row16911318114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1555718741915"><a name="p1555718741915"></a><a name="p1555718741915"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p64262004114454"><a name="p64262004114454"></a><a name="p64262004114454"></a>IMG.0056</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p11746740115557"><a name="p11746740115557"></a><a name="p11746740115557"></a>The OS type is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p20573275381"><a name="p20573275381"></a><a name="p20573275381"></a>The OS type is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p18690142617356"><a name="p18690142617356"></a><a name="p18690142617356"></a>Select Windows or Linux.</p>
</td>
</tr>
<tr id="row63082147114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p15574713198"><a name="p15574713198"></a><a name="p15574713198"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p5014449114454"><a name="p5014449114454"></a><a name="p5014449114454"></a>IMG.0057</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p40548006115557"><a name="p40548006115557"></a><a name="p40548006115557"></a>The image file does not exist, is empty, or in the incorrect format.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p6704275386"><a name="p6704275386"></a><a name="p6704275386"></a>The image file does not exist, is empty, or in the incorrect format.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1469010261353"><a name="p1469010261353"></a><a name="p1469010261353"></a>Select a valid image file.</p>
</td>
</tr>
<tr id="row48036149114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p11573371198"><a name="p11573371198"></a><a name="p11573371198"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p31654757114454"><a name="p31654757114454"></a><a name="p31654757114454"></a>IMG.0058</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p31596796115557"><a name="p31596796115557"></a><a name="p31596796115557"></a>The region of the bucket where the image file is stored is inconsistent with that of the user.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1784152710386"><a name="p1784152710386"></a><a name="p1784152710386"></a>The region of the bucket where the image file is stored is inconsistent with that of the user.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p19690102693514"><a name="p19690102693514"></a><a name="p19690102693514"></a>Ensure that the bucket where the image is stored is in region as the user.</p>
</td>
</tr>
<tr id="row31210202114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p6573167181918"><a name="p6573167181918"></a><a name="p6573167181918"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p57977901114454"><a name="p57977901114454"></a><a name="p57977901114454"></a>IMG.0059</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p15724184115557"><a name="p15724184115557"></a><a name="p15724184115557"></a>The size of the image file exceeds the maximum allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1897192753814"><a name="p1897192753814"></a><a name="p1897192753814"></a>The size of the image file exceeds the maximum allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p8690926143516"><a name="p8690926143516"></a><a name="p8690926143516"></a>Check whether the size of the image file is less than or equal to 128 GB.</p>
</td>
</tr>
<tr id="row4580585114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p10792101211917"><a name="p10792101211917"></a><a name="p10792101211917"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p54414442114454"><a name="p54414442114454"></a><a name="p54414442114454"></a>IMG.0060</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p54423268115557"><a name="p54423268115557"></a><a name="p54423268115557"></a>The number of tasks exceeds the flow control limit.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1011252763814"><a name="p1011252763814"></a><a name="p1011252763814"></a>The number of tasks exceeds the flow control limit.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p669082615356"><a name="p669082615356"></a><a name="p669082615356"></a>Wait for a while and then try again.</p>
</td>
</tr>
<tr id="row36959873114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p188071312171912"><a name="p188071312171912"></a><a name="p188071312171912"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p6790153114454"><a name="p6790153114454"></a><a name="p6790153114454"></a>IMG.0061</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p13224341115557"><a name="p13224341115557"></a><a name="p13224341115557"></a>Unknown system error.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1124727163816"><a name="p1124727163816"></a><a name="p1124727163816"></a>Unknown system error.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p14690142663518"><a name="p14690142663518"></a><a name="p14690142663518"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row30108234114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1380712126195"><a name="p1380712126195"></a><a name="p1380712126195"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p51074876114454"><a name="p51074876114454"></a><a name="p51074876114454"></a>IMG.0062</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p43977573115557"><a name="p43977573115557"></a><a name="p43977573115557"></a>The image name is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p19138192719386"><a name="p19138192719386"></a><a name="p19138192719386"></a>The image name is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p369062663517"><a name="p369062663517"></a><a name="p369062663517"></a>Check whether the image name is valid.</p>
</td>
</tr>
<tr id="row54556209114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p188231512131910"><a name="p188231512131910"></a><a name="p188231512131910"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p55274302114454"><a name="p55274302114454"></a><a name="p55274302114454"></a>IMG.0063</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p48723159115557"><a name="p48723159115557"></a><a name="p48723159115557"></a>The <span id="text3312016347"><a name="text3312016347"></a><a name="text3312016347"></a></span><span id="text637093413"><a name="text637093413"></a><a name="text637093413"></a>ECS</span> type does not support image creation.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p15151122773814"><a name="p15151122773814"></a><a name="p15151122773814"></a>The VM type does not support image creation.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1551875545110"><a name="p1551875545110"></a><a name="p1551875545110"></a>Select an <span id="text1378162183417"><a name="text1378162183417"></a><a name="text1378162183417"></a></span><span id="text33785219347"><a name="text33785219347"></a><a name="text33785219347"></a>ECS</span> that supports image creation.</p>
</td>
</tr>
<tr id="row56225071114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p12823101212199"><a name="p12823101212199"></a><a name="p12823101212199"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p29648146114454"><a name="p29648146114454"></a><a name="p29648146114454"></a>IMG.0064</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p18594551115557"><a name="p18594551115557"></a><a name="p18594551115557"></a>Failed to obtain tenant information from IAM.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p5163172710380"><a name="p5163172710380"></a><a name="p5163172710380"></a>Failed to obtain tenant information from IAM.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1369019264354"><a name="p1369019264354"></a><a name="p1369019264354"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row39957250114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p17823181281918"><a name="p17823181281918"></a><a name="p17823181281918"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p4444740114454"><a name="p4444740114454"></a><a name="p4444740114454"></a>IMG.0065</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p66546198115557"><a name="p66546198115557"></a><a name="p66546198115557"></a>Failed to obtain the tenant domain from IAM.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1617612712384"><a name="p1617612712384"></a><a name="p1617612712384"></a>Failed to obtain the tenant domain from IAM.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1969018266350"><a name="p1969018266350"></a><a name="p1969018266350"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row55095792114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p6838312161918"><a name="p6838312161918"></a><a name="p6838312161918"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p18989989114454"><a name="p18989989114454"></a><a name="p18989989114454"></a>IMG.0066</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p59579025115557"><a name="p59579025115557"></a><a name="p59579025115557"></a>The image ID is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p5189227123814"><a name="p5189227123814"></a><a name="p5189227123814"></a>The image ID is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1569022616357"><a name="p1569022616357"></a><a name="p1569022616357"></a>Enter a correct image ID.</p>
</td>
</tr>
<tr id="row60375690114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p18541612191912"><a name="p18541612191912"></a><a name="p18541612191912"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p19276305114454"><a name="p19276305114454"></a><a name="p19276305114454"></a>IMG.0067</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p13674377115557"><a name="p13674377115557"></a><a name="p13674377115557"></a>The project ID is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p182011527113811"><a name="p182011527113811"></a><a name="p182011527113811"></a>The project ID is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p7690152683513"><a name="p7690152683513"></a><a name="p7690152683513"></a>Enter a correct project ID.</p>
</td>
</tr>
<tr id="row46364007114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p285421214190"><a name="p285421214190"></a><a name="p285421214190"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p26674476114454"><a name="p26674476114454"></a><a name="p26674476114454"></a>IMG.0068</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p36509611115557"><a name="p36509611115557"></a><a name="p36509611115557"></a>The specified bucket name is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p621402713817"><a name="p621402713817"></a><a name="p621402713817"></a>The specified bucket name is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p12690192616358"><a name="p12690192616358"></a><a name="p12690192616358"></a>Check whether the specified bucket name is empty and enter a correct bucket name.</p>
</td>
</tr>
<tr id="row58404580114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p20870171219194"><a name="p20870171219194"></a><a name="p20870171219194"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p51231776114454"><a name="p51231776114454"></a><a name="p51231776114454"></a>IMG.0069</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p40396777115557"><a name="p40396777115557"></a><a name="p40396777115557"></a>The specified bucket cannot be accessed.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p32296276382"><a name="p32296276382"></a><a name="p32296276382"></a>The specified bucket cannot be accessed.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1069042683514"><a name="p1069042683514"></a><a name="p1069042683514"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row6849769114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p587014129193"><a name="p587014129193"></a><a name="p587014129193"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p35436640114454"><a name="p35436640114454"></a><a name="p35436640114454"></a>IMG.0070</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p55568446115557"><a name="p55568446115557"></a><a name="p55568446115557"></a>The image file already exists.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p12240182723811"><a name="p12240182723811"></a><a name="p12240182723811"></a>The image file already exists. Confirm the file in the corresponding directory of the OBS bucket or in the OBS bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p206901526133516"><a name="p206901526133516"></a><a name="p206901526133516"></a>Check whether the file exists in the corresponding directory of the OBS bucket or in the OBS bucket.</p>
</td>
</tr>
<tr id="row24071846114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1988511215192"><a name="p1988511215192"></a><a name="p1988511215192"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p63507047114454"><a name="p63507047114454"></a><a name="p63507047114454"></a>IMG.0071</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p42752621115557"><a name="p42752621115557"></a><a name="p42752621115557"></a>The image cannot be exported.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1525372711387"><a name="p1525372711387"></a><a name="p1525372711387"></a>The image cannot be exported.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p9690132643510"><a name="p9690132643510"></a><a name="p9690132643510"></a>Select another image.</p>
</td>
</tr>
<tr id="row41113168114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p15885121214194"><a name="p15885121214194"></a><a name="p15885121214194"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p58630264114454"><a name="p58630264114454"></a><a name="p58630264114454"></a>IMG.0072</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p28148418115557"><a name="p28148418115557"></a><a name="p28148418115557"></a>The specified image format is not supported.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1426652711380"><a name="p1426652711380"></a><a name="p1426652711380"></a>The specified image format is not supported.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1469011264351"><a name="p1469011264351"></a><a name="p1469011264351"></a>Check the image format. Only VHD, RAW, ZVHD, and QCOW2 are supported. The default format is VHD.</p>
</td>
</tr>
<tr id="row14359784114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p2667201718193"><a name="p2667201718193"></a><a name="p2667201718193"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p60225374114454"><a name="p60225374114454"></a><a name="p60225374114454"></a>IMG.0073</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p51993294115557"><a name="p51993294115557"></a><a name="p51993294115557"></a>The name of the exported file is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p627816271383"><a name="p627816271383"></a><a name="p627816271383"></a>The name of the exported file is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p86901626113515"><a name="p86901626113515"></a><a name="p86901626113515"></a>Enter a correct file name.</p>
</td>
</tr>
<tr id="row38510580114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p12682171711196"><a name="p12682171711196"></a><a name="p12682171711196"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p15101229114454"><a name="p15101229114454"></a><a name="p15101229114454"></a>IMG.0074</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p53712430115557"><a name="p53712430115557"></a><a name="p53712430115557"></a>The file name length exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p11292627203812"><a name="p11292627203812"></a><a name="p11292627203812"></a>The file name length exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p136901026163512"><a name="p136901026163512"></a><a name="p136901026163512"></a>Reduce the length of the file name.</p>
</td>
</tr>
<tr id="row4985155114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p668217178194"><a name="p668217178194"></a><a name="p668217178194"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p2942462114454"><a name="p2942462114454"></a><a name="p2942462114454"></a>IMG.0075</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p31893827115557"><a name="p31893827115557"></a><a name="p31893827115557"></a>The file name contains invalid characters.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p19304162713386"><a name="p19304162713386"></a><a name="p19304162713386"></a>The file name contains invalid characters.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p23657106585"><a name="p23657106585"></a><a name="p23657106585"></a>Ensure that the image file name meets the following requirements:</p>
<a name="ul5327123613427"></a><a name="ul5327123613427"></a><ul id="ul5327123613427"><li>The name cannot start or end with space.</li><li>The name contains 1 to 128 characters.</li><li>The name contains the following four types of characters:</li><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-), periods (.), underscores (_), and space</li></ul>
</td>
</tr>
<tr id="row64024748114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p2698101710198"><a name="p2698101710198"></a><a name="p2698101710198"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p64680630114454"><a name="p64680630114454"></a><a name="p64680630114454"></a>IMG.0076</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p30933498115557"><a name="p30933498115557"></a><a name="p30933498115557"></a>You cannot share an image with yourself.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p2318142715386"><a name="p2318142715386"></a><a name="p2318142715386"></a>You cannot share an image with yourself.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p17690102619358"><a name="p17690102619358"></a><a name="p17690102619358"></a>Do not share images with yourself.</p>
</td>
</tr>
<tr id="row37386190114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1271301761910"><a name="p1271301761910"></a><a name="p1271301761910"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p41757119114454"><a name="p41757119114454"></a><a name="p41757119114454"></a>IMG.0077</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p1942149115557"><a name="p1942149115557"></a><a name="p1942149115557"></a>The public image cannot be exported.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p93299275380"><a name="p93299275380"></a><a name="p93299275380"></a>The public image cannot be exported.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p66904269357"><a name="p66904269357"></a><a name="p66904269357"></a>Select another image.</p>
</td>
</tr>
<tr id="row54183889114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1071361712191"><a name="p1071361712191"></a><a name="p1071361712191"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p40624588114454"><a name="p40624588114454"></a><a name="p40624588114454"></a>IMG.0078</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p6540831115557"><a name="p6540831115557"></a><a name="p6540831115557"></a>A marketplace image or private image created from a marketplace image cannot be exported.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p7342142713383"><a name="p7342142713383"></a><a name="p7342142713383"></a>The Marketplace image or private image created from a Marketplace image cannot be exported.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p146904260358"><a name="p146904260358"></a><a name="p146904260358"></a>Select another image.</p>
</td>
</tr>
<tr id="row58509602114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p672931771920"><a name="p672931771920"></a><a name="p672931771920"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p20315800114454"><a name="p20315800114454"></a><a name="p20315800114454"></a>IMG.0079</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p3536843115557"><a name="p3536843115557"></a><a name="p3536843115557"></a>A system disk image created from a charged image cannot be exported.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p23551827163820"><a name="p23551827163820"></a><a name="p23551827163820"></a>The system disk image created from a charged image cannot be exported.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p15690172603511"><a name="p15690172603511"></a><a name="p15690172603511"></a>Select another image.</p>
</td>
</tr>
<tr id="row15019322114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p4729191721919"><a name="p4729191721919"></a><a name="p4729191721919"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p46268326114454"><a name="p46268326114454"></a><a name="p46268326114454"></a>IMG.0080</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p28222229115557"><a name="p28222229115557"></a><a name="p28222229115557"></a>The image created from a CSBS backup cannot be exported.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p736816275388"><a name="p736816275388"></a><a name="p736816275388"></a>The image created from a CSBS backup cannot be exported.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1769019260352"><a name="p1769019260352"></a><a name="p1769019260352"></a>Export the image after the backup is created.</p>
</td>
</tr>
<tr id="row229974114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1774581717194"><a name="p1774581717194"></a><a name="p1774581717194"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p40960257114454"><a name="p40960257114454"></a><a name="p40960257114454"></a>IMG.0081</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p38692558115557"><a name="p38692558115557"></a><a name="p38692558115557"></a>The image cannot be exported because it is created from an image file.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1038112793817"><a name="p1038112793817"></a><a name="p1038112793817"></a>The image cannot be exported because it is created from an image file.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p3585105211419"><a name="p3585105211419"></a><a name="p3585105211419"></a>Select another image.</p>
</td>
</tr>
<tr id="row48351551114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p14745121719191"><a name="p14745121719191"></a><a name="p14745121719191"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p63692285114454"><a name="p63692285114454"></a><a name="p63692285114454"></a>IMG.0082</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p21152210115557"><a name="p21152210115557"></a><a name="p21152210115557"></a>The image cannot be published in the Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p13394827113820"><a name="p13394827113820"></a><a name="p13394827113820"></a>The image cannot be published in Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1577031212421"><a name="p1577031212421"></a><a name="p1577031212421"></a>Check whether the image can be published.</p>
</td>
</tr>
<tr id="row27949312114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p113382248196"><a name="p113382248196"></a><a name="p113382248196"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p27652480114454"><a name="p27652480114454"></a><a name="p27652480114454"></a>IMG.0086</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p48245512115557"><a name="p48245512115557"></a><a name="p48245512115557"></a>No image was found.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p74456274383"><a name="p74456274383"></a><a name="p74456274383"></a>No image was found.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p3690526113513"><a name="p3690526113513"></a><a name="p3690526113513"></a>Check whether the image exists.</p>
</td>
</tr>
<tr id="row39058342114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1733892491913"><a name="p1733892491913"></a><a name="p1733892491913"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p25998801114454"><a name="p25998801114454"></a><a name="p25998801114454"></a>IMG.0087</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p5933809115557"><a name="p5933809115557"></a><a name="p5933809115557"></a>The token is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p15458132715387"><a name="p15458132715387"></a><a name="p15458132715387"></a>The token is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p16690192693518"><a name="p16690192693518"></a><a name="p16690192693518"></a>Enter a correct token.</p>
</td>
</tr>
<tr id="row6215659114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p103546241197"><a name="p103546241197"></a><a name="p103546241197"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p28426396114454"><a name="p28426396114454"></a><a name="p28426396114454"></a>IMG.0088</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p30779887115557"><a name="p30779887115557"></a><a name="p30779887115557"></a>The number of shared images has reached the quota.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p144721827123813"><a name="p144721827123813"></a><a name="p144721827123813"></a>The number of shared images has reached the maximum allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p186901926113512"><a name="p186901926113512"></a><a name="p186901926113512"></a>Increase the quota.</p>
</td>
</tr>
<tr id="row12851533114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p137092451919"><a name="p137092451919"></a><a name="p137092451919"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p53312812114454"><a name="p53312812114454"></a><a name="p53312812114454"></a>IMG.0089</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p24177686115557"><a name="p24177686115557"></a><a name="p24177686115557"></a>A public image or marketplace image cannot be shared.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p2048382763817"><a name="p2048382763817"></a><a name="p2048382763817"></a>The public image or Marketplace image cannot be shared.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p186909265359"><a name="p186909265359"></a><a name="p186909265359"></a>Check the constraints of image sharing.</p>
</td>
</tr>
<tr id="row53982163114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p18385152461916"><a name="p18385152461916"></a><a name="p18385152461916"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p9008149114454"><a name="p9008149114454"></a><a name="p9008149114454"></a>IMG.0090</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p43010943115557"><a name="p43010943115557"></a><a name="p43010943115557"></a>An image being created cannot be deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p5496182713383"><a name="p5496182713383"></a><a name="p5496182713383"></a>The image being created cannot be deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p16907268356"><a name="p16907268356"></a><a name="p16907268356"></a>Delete the image after the image is created.</p>
</td>
</tr>
<tr id="row33741772114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p2401172414197"><a name="p2401172414197"></a><a name="p2401172414197"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p57380848114454"><a name="p57380848114454"></a><a name="p57380848114454"></a>IMG.0091</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p15138575115557"><a name="p15138575115557"></a><a name="p15138575115557"></a>A protected image cannot be deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p135092279384"><a name="p135092279384"></a><a name="p135092279384"></a>The protected image cannot be deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p0690142663510"><a name="p0690142663510"></a><a name="p0690142663510"></a>Remove the image from Marketplace.</p>
</td>
</tr>
<tr id="row37797775114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1040192481913"><a name="p1040192481913"></a><a name="p1040192481913"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p21816354114454"><a name="p21816354114454"></a><a name="p21816354114454"></a>IMG.0092</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p30167856115557"><a name="p30167856115557"></a><a name="p30167856115557"></a>The image can only be deleted by the owner.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p15231427133816"><a name="p15231427133816"></a><a name="p15231427133816"></a>The image can only be deleted by the owner.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p12690162643510"><a name="p12690162643510"></a><a name="p12690162643510"></a>Ask the image owner to delete the image.</p>
</td>
</tr>
<tr id="row11637563114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p194171224121918"><a name="p194171224121918"></a><a name="p194171224121918"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p66430357114454"><a name="p66430357114454"></a><a name="p66430357114454"></a>IMG.0093</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p47768725115557"><a name="p47768725115557"></a><a name="p47768725115557"></a>A marketplace image cannot be deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p75352274381"><a name="p75352274381"></a><a name="p75352274381"></a>The Marketplace image cannot be deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p106901826173512"><a name="p106901826173512"></a><a name="p106901826173512"></a>Do not delete marketplace images.</p>
</td>
</tr>
<tr id="row24183114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p104321424151910"><a name="p104321424151910"></a><a name="p104321424151910"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p42239355114454"><a name="p42239355114454"></a><a name="p42239355114454"></a>IMG.0094</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p61009145115557"><a name="p61009145115557"></a><a name="p61009145115557"></a>The public image cannot be deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1854932716385"><a name="p1854932716385"></a><a name="p1854932716385"></a>The public image cannot be deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p369032618356"><a name="p369032618356"></a><a name="p369032618356"></a>Do not delete public images.</p>
</td>
</tr>
<tr id="row41712691114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p104324246196"><a name="p104324246196"></a><a name="p104324246196"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p56630802114454"><a name="p56630802114454"></a><a name="p56630802114454"></a>IMG.0095</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p49598943115557"><a name="p49598943115557"></a><a name="p49598943115557"></a>The key does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1056219274384"><a name="p1056219274384"></a><a name="p1056219274384"></a>The KMS key does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p19690122663519"><a name="p19690122663519"></a><a name="p19690122663519"></a>Check whether the key exists.</p>
</td>
</tr>
<tr id="row17316964114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p114481324141913"><a name="p114481324141913"></a><a name="p114481324141913"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p11903322114454"><a name="p11903322114454"></a><a name="p11903322114454"></a>IMG.0096</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p53060946115557"><a name="p53060946115557"></a><a name="p53060946115557"></a>The specified KMS key ID must be different from the image key ID.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1757572713387"><a name="p1757572713387"></a><a name="p1757572713387"></a>The specified KMS key ID must be different from the image key ID.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p9690182617351"><a name="p9690182617351"></a><a name="p9690182617351"></a>Check whether the specified KMS key ID is the same as the image key ID.</p>
</td>
</tr>
<tr id="row8034251114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p146362410191"><a name="p146362410191"></a><a name="p146362410191"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p20478431114454"><a name="p20478431114454"></a><a name="p20478431114454"></a>IMG.0097</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p26724518115557"><a name="p26724518115557"></a><a name="p26724518115557"></a>The key is not enabled.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p95873271382"><a name="p95873271382"></a><a name="p95873271382"></a>The key is not enabled.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p176901926163520"><a name="p176901926163520"></a><a name="p176901926163520"></a>Enable the key.</p>
</td>
</tr>
<tr id="row34235822114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p12463132421914"><a name="p12463132421914"></a><a name="p12463132421914"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p30608756114454"><a name="p30608756114454"></a><a name="p30608756114454"></a>IMG.0098</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p20603188115557"><a name="p20603188115557"></a><a name="p20603188115557"></a>The encrypted image cannot be shared or published in the Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p36005274386"><a name="p36005274386"></a><a name="p36005274386"></a>The encrypted image cannot be shared or published in Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p16909268357"><a name="p16909268357"></a><a name="p16909268357"></a>Copy the image to a non-encrypted image and then share or release the non-encrypted image.</p>
</td>
</tr>
<tr id="row28181404114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p2479224161912"><a name="p2479224161912"></a><a name="p2479224161912"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p33640949114454"><a name="p33640949114454"></a><a name="p33640949114454"></a>IMG.0099</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p54447905115557"><a name="p54447905115557"></a><a name="p54447905115557"></a>You do not have the permission to access the key.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p261292763817"><a name="p261292763817"></a><a name="p261292763817"></a>You do not have the permission to access the key.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p66907265354"><a name="p66907265354"></a><a name="p66907265354"></a>Check whether you have the permission to access the key.</p>
</td>
</tr>
<tr id="row13295404114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p94791524131912"><a name="p94791524131912"></a><a name="p94791524131912"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p29516804114454"><a name="p29516804114454"></a><a name="p29516804114454"></a>IMG.0100</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p31184407115557"><a name="p31184407115557"></a><a name="p31184407115557"></a>You do not have OBT permission for KMS.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p362512277386"><a name="p362512277386"></a><a name="p362512277386"></a>You do not have OBT permission of KMS.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p36901226183510"><a name="p36901226183510"></a><a name="p36901226183510"></a>Check whether you have the OBT permission of KMS.</p>
</td>
</tr>
<tr id="row20763069114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p10275193413199"><a name="p10275193413199"></a><a name="p10275193413199"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p42913739114454"><a name="p42913739114454"></a><a name="p42913739114454"></a>IMG.0101</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p50636809115557"><a name="p50636809115557"></a><a name="p50636809115557"></a>The original key does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p106391272386"><a name="p106391272386"></a><a name="p106391272386"></a>The original key does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p169062683514"><a name="p169062683514"></a><a name="p169062683514"></a>Check whether the key is valid.</p>
</td>
</tr>
<tr id="row12959287114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1027523411915"><a name="p1027523411915"></a><a name="p1027523411915"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p11385791114454"><a name="p11385791114454"></a><a name="p11385791114454"></a>IMG.0102</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p4358642115557"><a name="p4358642115557"></a><a name="p4358642115557"></a>The original key is not enabled.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p15651102733814"><a name="p15651102733814"></a><a name="p15651102733814"></a>The original key is not enabled.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p2690926163511"><a name="p2690926163511"></a><a name="p2690926163511"></a>Enable the original key.</p>
</td>
</tr>
<tr id="row41574599114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p7292123416191"><a name="p7292123416191"></a><a name="p7292123416191"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p45851994114454"><a name="p45851994114454"></a><a name="p45851994114454"></a>IMG.0103</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p23333525115557"><a name="p23333525115557"></a><a name="p23333525115557"></a>You do not have the permission to access the original key.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1166452711387"><a name="p1166452711387"></a><a name="p1166452711387"></a>You do not have the permission to access the original key.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1169252617358"><a name="p1169252617358"></a><a name="p1169252617358"></a>Check whether you have the permission to access the key.</p>
</td>
</tr>
<tr id="row22623185114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p10354234111912"><a name="p10354234111912"></a><a name="p10354234111912"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p65963290114454"><a name="p65963290114454"></a><a name="p65963290114454"></a>IMG.0105</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p16145022115557"><a name="p16145022115557"></a><a name="p16145022115557"></a>The operation is not supported.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p136921027153812"><a name="p136921027153812"></a><a name="p136921027153812"></a>The operation is not supported.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p19692926113518"><a name="p19692926113518"></a><a name="p19692926113518"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row484561114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p83851234161918"><a name="p83851234161918"></a><a name="p83851234161918"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p37292060114454"><a name="p37292060114454"></a><a name="p37292060114454"></a>IMG.0106</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p25669873115557"><a name="p25669873115557"></a><a name="p25669873115557"></a>The image owner is another tenant.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1170522715384"><a name="p1170522715384"></a><a name="p1170522715384"></a>The image owner is another tenant.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1069232633512"><a name="p1069232633512"></a><a name="p1069232633512"></a>Confirm the image owner.</p>
</td>
</tr>
<tr id="row39668340114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1938518349197"><a name="p1938518349197"></a><a name="p1938518349197"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p6822402114454"><a name="p6822402114454"></a><a name="p6822402114454"></a>IMG.0107</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p57073659115557"><a name="p57073659115557"></a><a name="p57073659115557"></a>A marketplace image cannot be shared.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p97205279389"><a name="p97205279389"></a><a name="p97205279389"></a>The Marketplace image cannot be shared.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p18692172623517"><a name="p18692172623517"></a><a name="p18692172623517"></a>Check the constraints of image sharing.</p>
</td>
</tr>
<tr id="row49578385114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1141611346196"><a name="p1141611346196"></a><a name="p1141611346196"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p7475374114454"><a name="p7475374114454"></a><a name="p7475374114454"></a>IMG.0108</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p66310790115557"><a name="p66310790115557"></a><a name="p66310790115557"></a>The tenant ID was not found in the current region.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p8733127143812"><a name="p8733127143812"></a><a name="p8733127143812"></a>The tenant ID was not found in the current region.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p569272617351"><a name="p569272617351"></a><a name="p569272617351"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row27719880114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p19432133416195"><a name="p19432133416195"></a><a name="p19432133416195"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p13729674114454"><a name="p13729674114454"></a><a name="p13729674114454"></a>IMG.0109</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p22183876115557"><a name="p22183876115557"></a><a name="p22183876115557"></a>The bucket name contains invalid characters.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p16747112773820"><a name="p16747112773820"></a><a name="p16747112773820"></a>The bucket name contains invalid characters.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p6692202633513"><a name="p6692202633513"></a><a name="p6692202633513"></a>Check whether the bucket name is valid.</p>
</td>
</tr>
<tr id="row35937854114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p16448183410190"><a name="p16448183410190"></a><a name="p16448183410190"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p9712203114454"><a name="p9712203114454"></a><a name="p9712203114454"></a>IMG.0110</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p65918963115557"><a name="p65918963115557"></a><a name="p65918963115557"></a>The system disk is unavailable and cannot be used to create images.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p9760927163812"><a name="p9760927163812"></a><a name="p9760927163812"></a>The system disk is unavailable and cannot be used to create images.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p10692326173514"><a name="p10692326173514"></a><a name="p10692326173514"></a>Create an image when the system disk is available.</p>
</td>
</tr>
<tr id="row19808100114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p16463163413197"><a name="p16463163413197"></a><a name="p16463163413197"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p33765803114454"><a name="p33765803114454"></a><a name="p33765803114454"></a>IMG.0111</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p4977427115557"><a name="p4977427115557"></a><a name="p4977427115557"></a>The size of the system disk exceeds the maximum allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p14776132713383"><a name="p14776132713383"></a><a name="p14776132713383"></a>The size of the system disk exceeds the maximum allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1769242616355"><a name="p1769242616355"></a><a name="p1769242616355"></a>Ensure that the <span id="text979074435420"><a name="text979074435420"></a><a name="text979074435420"></a></span><span id="text13450144685418"><a name="text13450144685418"></a><a name="text13450144685418"></a>ECS</span> system disk size is greater than or equal to the system disk size of the image and smaller than 1024 GB.</p>
</td>
</tr>
<tr id="row52710063114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1447918345196"><a name="p1447918345196"></a><a name="p1447918345196"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p53426733114454"><a name="p53426733114454"></a><a name="p53426733114454"></a>IMG.0112</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p4665776115557"><a name="p4665776115557"></a><a name="p4665776115557"></a>Failed to add the tenant.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p37892270380"><a name="p37892270380"></a><a name="p37892270380"></a>Failed to add the tenant.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p6692226163519"><a name="p6692226163519"></a><a name="p6692226163519"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row46572384114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p749553414193"><a name="p749553414193"></a><a name="p749553414193"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p24947933114454"><a name="p24947933114454"></a><a name="p24947933114454"></a>IMG.0113</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p45907869115557"><a name="p45907869115557"></a><a name="p45907869115557"></a>Failed to delete the tenant.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p8805152716385"><a name="p8805152716385"></a><a name="p8805152716385"></a>Failed to delete the tenant.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p369272693518"><a name="p369272693518"></a><a name="p369272693518"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row19707709114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p951063451919"><a name="p951063451919"></a><a name="p951063451919"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p541196114454"><a name="p541196114454"></a><a name="p541196114454"></a>IMG.0114</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p46622902115557"><a name="p46622902115557"></a><a name="p46622902115557"></a>Failed to query the tenant details.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p138191427103810"><a name="p138191427103810"></a><a name="p138191427103810"></a>Failed to query the tenant details.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1169232610357"><a name="p1169232610357"></a><a name="p1169232610357"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row50562645114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p91571142191916"><a name="p91571142191916"></a><a name="p91571142191916"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p58988055114454"><a name="p58988055114454"></a><a name="p58988055114454"></a>IMG.0115</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p31010717115557"><a name="p31010717115557"></a><a name="p31010717115557"></a>The image tag is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p283562763812"><a name="p283562763812"></a><a name="p283562763812"></a>The image tag is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p16921326103511"><a name="p16921326103511"></a><a name="p16921326103511"></a>Check the validity of the image tag.</p>
</td>
</tr>
<tr id="row22465727114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p18173042111917"><a name="p18173042111917"></a><a name="p18173042111917"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p52619295114454"><a name="p52619295114454"></a><a name="p52619295114454"></a>IMG.0116</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p58234492115557"><a name="p58234492115557"></a><a name="p58234492115557"></a>The number of image tags exceeds the quota.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p19852227163811"><a name="p19852227163811"></a><a name="p19852227163811"></a>The number of image tags exceeds the quota.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1069213261354"><a name="p1069213261354"></a><a name="p1069213261354"></a>Delete tags that are unnecessary or not in use.</p>
</td>
</tr>
<tr id="row43318874114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p16187194214191"><a name="p16187194214191"></a><a name="p16187194214191"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p40305361114454"><a name="p40305361114454"></a><a name="p40305361114454"></a>IMG.0117</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p40143304115557"><a name="p40143304115557"></a><a name="p40143304115557"></a>The image type can only be BMS or ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p686882712383"><a name="p686882712383"></a><a name="p686882712383"></a>The image source can only be BMS or ECS.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p18692132603519"><a name="p18692132603519"></a><a name="p18692132603519"></a>Select a correct image type.</p>
</td>
</tr>
<tr id="row54953101114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p518794271913"><a name="p518794271913"></a><a name="p518794271913"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p56035103114454"><a name="p56035103114454"></a><a name="p56035103114454"></a>IMG.0118</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p5004539115557"><a name="p5004539115557"></a><a name="p5004539115557"></a>The BMS image does not support KMS encryption.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p3885527153812"><a name="p3885527153812"></a><a name="p3885527153812"></a>The BMS image does not support KMS encryption.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1269292611354"><a name="p1269292611354"></a><a name="p1269292611354"></a>Modify the BMS image configuration.</p>
</td>
</tr>
<tr id="row3485192114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p92031242161914"><a name="p92031242161914"></a><a name="p92031242161914"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p47401220114454"><a name="p47401220114454"></a><a name="p47401220114454"></a>IMG.0119</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p24430937115557"><a name="p24430937115557"></a><a name="p24430937115557"></a>The <span id="text1559184263519"><a name="text1559184263519"></a><a name="text1559184263519"></a></span><span id="text15984217359"><a name="text15984217359"></a><a name="text15984217359"></a>ECS</span> does not have a system disk.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p11898027183811"><a name="p11898027183811"></a><a name="p11898027183811"></a>The VM does not have a system disk.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p46921926103515"><a name="p46921926103515"></a><a name="p46921926103515"></a>Attach a system disk to the <span id="text8709944143515"><a name="text8709944143515"></a><a name="text8709944143515"></a></span><span id="text1370994417358"><a name="text1370994417358"></a><a name="text1370994417358"></a>ECS</span>.</p>
</td>
</tr>
<tr id="row60899457114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1820313423197"><a name="p1820313423197"></a><a name="p1820313423197"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p61533763114454"><a name="p61533763114454"></a><a name="p61533763114454"></a>IMG.0120</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p26304171115557"><a name="p26304171115557"></a><a name="p26304171115557"></a>The specified data disk ID is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p19642272383"><a name="p19642272383"></a><a name="p19642272383"></a>The specified data disk ID is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1769232623519"><a name="p1769232623519"></a><a name="p1769232623519"></a>Check whether the current data disk ID is valid.</p>
</td>
</tr>
<tr id="row29236342114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p9219194221917"><a name="p9219194221917"></a><a name="p9219194221917"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p29392680114454"><a name="p29392680114454"></a><a name="p29392680114454"></a>IMG.0121</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p49714693115557"><a name="p49714693115557"></a><a name="p49714693115557"></a>The object cannot be found.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p2978142711389"><a name="p2978142711389"></a><a name="p2978142711389"></a>The object cannot be found.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1669282615356"><a name="p1669282615356"></a><a name="p1669282615356"></a>Check whether the object exists.</p>
</td>
</tr>
<tr id="row36233968114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p7219842141912"><a name="p7219842141912"></a><a name="p7219842141912"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p19536196114454"><a name="p19536196114454"></a><a name="p19536196114454"></a>IMG.0122</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p3225219115557"><a name="p3225219115557"></a><a name="p3225219115557"></a>The OS type is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p12991152716381"><a name="p12991152716381"></a><a name="p12991152716381"></a>The OS type is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p269262617351"><a name="p269262617351"></a><a name="p269262617351"></a>Select Windows or Linux.</p>
</td>
</tr>
<tr id="row58723645114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p10235204291914"><a name="p10235204291914"></a><a name="p10235204291914"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p14808116114454"><a name="p14808116114454"></a><a name="p14808116114454"></a>IMG.0123</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p2374663115557"><a name="p2374663115557"></a><a name="p2374663115557"></a>The image file address in the request is duplicate.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p44528183810"><a name="p44528183810"></a><a name="p44528183810"></a>The image file address in the request is duplicate.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p2692152613354"><a name="p2692152613354"></a><a name="p2692152613354"></a>Delete the duplicate image file address.</p>
</td>
</tr>
<tr id="row30631604114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p523564201917"><a name="p523564201917"></a><a name="p523564201917"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p57698393114454"><a name="p57698393114454"></a><a name="p57698393114454"></a>IMG.0124</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p53407739115557"><a name="p53407739115557"></a><a name="p53407739115557"></a>The data disk image cannot be published in the Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p818162843810"><a name="p818162843810"></a><a name="p818162843810"></a>The data disk image cannot be published in Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1692122673519"><a name="p1692122673519"></a><a name="p1692122673519"></a>Select another image.</p>
</td>
</tr>
<tr id="row28768037114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p14251342101919"><a name="p14251342101919"></a><a name="p14251342101919"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p44161083114454"><a name="p44161083114454"></a><a name="p44161083114454"></a>IMG.0126</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p39714572115557"><a name="p39714572115557"></a><a name="p39714572115557"></a>The <span id="text464175318354"><a name="text464175318354"></a><a name="text464175318354"></a></span><span id="text206411653163512"><a name="text206411653163512"></a><a name="text206411653163512"></a>ECS</span> in the current status cannot be used to create a full-ECS image.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p941142815383"><a name="p941142815383"></a><a name="p941142815383"></a>The VM in the current stage cannot be used to create a full-ECS image.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p19692192663513"><a name="p19692192663513"></a><a name="p19692192663513"></a>Check the <span id="text8138358103512"><a name="text8138358103512"></a><a name="text8138358103512"></a></span><span id="text7138105873511"><a name="text7138105873511"></a><a name="text7138105873511"></a>ECS</span> status. Ensure that the <span id="text19131851368"><a name="text19131851368"></a><a name="text19131851368"></a></span><span id="text5133573611"><a name="text5133573611"></a><a name="text5133573611"></a>ECS</span> is in the <strong id="b623322013562"><a name="b623322013562"></a><a name="b623322013562"></a>Running</strong> or <strong id="b1972371345614"><a name="b1972371345614"></a><a name="b1972371345614"></a>Stopped</strong> state.</p>
</td>
</tr>
<tr id="row38322868114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1426694221915"><a name="p1426694221915"></a><a name="p1426694221915"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p48284005114454"><a name="p48284005114454"></a><a name="p48284005114454"></a>IMG.0127</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p28003174115557"><a name="p28003174115557"></a><a name="p28003174115557"></a>The CSBS backup does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p55513288382"><a name="p55513288382"></a><a name="p55513288382"></a>The CSBS backup does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p869232619353"><a name="p869232619353"></a><a name="p869232619353"></a>Check whether the CSBS backup exists.</p>
</td>
</tr>
<tr id="row35817498114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1576614871915"><a name="p1576614871915"></a><a name="p1576614871915"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p33995297114454"><a name="p33995297114454"></a><a name="p33995297114454"></a>IMG.0128</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p13219886115557"><a name="p13219886115557"></a><a name="p13219886115557"></a>A full-ECS image cannot be exported.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p36762814389"><a name="p36762814389"></a><a name="p36762814389"></a>The full-ECS image cannot be exported.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p106929269352"><a name="p106929269352"></a><a name="p106929269352"></a>Check the constraints on image export.</p>
</td>
</tr>
<tr id="row19879189114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p197812487199"><a name="p197812487199"></a><a name="p197812487199"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p19401211114454"><a name="p19401211114454"></a><a name="p19401211114454"></a>IMG.0129</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p40729525115557"><a name="p40729525115557"></a><a name="p40729525115557"></a>A full-ECS image cannot be published in the Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p118062883819"><a name="p118062883819"></a><a name="p118062883819"></a>The full-ECS image cannot be published in Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p96921126123518"><a name="p96921126123518"></a><a name="p96921126123518"></a>Select another image.</p>
</td>
</tr>
<tr id="row29027819114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p187811482195"><a name="p187811482195"></a><a name="p187811482195"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p50621380114454"><a name="p50621380114454"></a><a name="p50621380114454"></a>IMG.0130</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p29706328115557"><a name="p29706328115557"></a><a name="p29706328115557"></a>A full-ECS image cannot be exported or replicated.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p99310286382"><a name="p99310286382"></a><a name="p99310286382"></a>The full-ECS image cannot be exported or replicated.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p869212633517"><a name="p869212633517"></a><a name="p869212633517"></a>Check the constraints on full-ECS images.</p>
</td>
</tr>
<tr id="row50246957114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p57971648141911"><a name="p57971648141911"></a><a name="p57971648141911"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p60219992114454"><a name="p60219992114454"></a><a name="p60219992114454"></a>IMG.0131</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p46859064115557"><a name="p46859064115557"></a><a name="p46859064115557"></a>A full-ECS image cannot be published in the Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p8106328123814"><a name="p8106328123814"></a><a name="p8106328123814"></a>The full-ECS image cannot be published in Marketplace.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p118061471547"><a name="p118061471547"></a><a name="p118061471547"></a>Check the constraints on full-ECS images.</p>
</td>
</tr>
<tr id="row49575282114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p16797948161910"><a name="p16797948161910"></a><a name="p16797948161910"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p11177819114454"><a name="p11177819114454"></a><a name="p11177819114454"></a>IMG.0132</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p1846530115557"><a name="p1846530115557"></a><a name="p1846530115557"></a>A CSBS backup in the current state cannot be used to create a full-ECS image.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p3118328193817"><a name="p3118328193817"></a><a name="p3118328193817"></a>The CSBS backup in the current state cannot be used to create a full-ECS image.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p569282693518"><a name="p569282693518"></a><a name="p569282693518"></a>Wait until the CSBS backup becomes available.</p>
</td>
</tr>
<tr id="row13040919114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p13813144812192"><a name="p13813144812192"></a><a name="p13813144812192"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p28457975114454"><a name="p28457975114454"></a><a name="p28457975114454"></a>IMG.0133</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p3943592115557"><a name="p3943592115557"></a><a name="p3943592115557"></a>You are not allowed to access the CSBS backup.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p91311328103810"><a name="p91311328103810"></a><a name="p91311328103810"></a>You are not allowed to access the CSBS backup.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1669252613520"><a name="p1669252613520"></a><a name="p1669252613520"></a>Apply for the permissions.</p>
</td>
</tr>
<tr id="row46201860114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p381364831912"><a name="p381364831912"></a><a name="p381364831912"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p9225119114454"><a name="p9225119114454"></a><a name="p9225119114454"></a>IMG.0134</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p56306725115557"><a name="p56306725115557"></a><a name="p56306725115557"></a>The CSBS backup has been registered as an image.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p81441128133814"><a name="p81441128133814"></a><a name="p81441128133814"></a>The CSBS backup has been registered as an image.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1569212615359"><a name="p1569212615359"></a><a name="p1569212615359"></a>A CSBS backup can be used to create only one full-ECS image. Select another CSBS backup.</p>
</td>
</tr>
<tr id="row27202409114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p158131348151915"><a name="p158131348151915"></a><a name="p158131348151915"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p14225614114454"><a name="p14225614114454"></a><a name="p14225614114454"></a>IMG.0135</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p44087100115557"><a name="p44087100115557"></a><a name="p44087100115557"></a>A full-ECS image cannot be shared.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p16156162893814"><a name="p16156162893814"></a><a name="p16156162893814"></a>The full-ECS image cannot be shared.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p136922268356"><a name="p136922268356"></a><a name="p136922268356"></a>Check the constraints of image sharing.</p>
</td>
</tr>
<tr id="row30050171114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1482824810198"><a name="p1482824810198"></a><a name="p1482824810198"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p35707847114454"><a name="p35707847114454"></a><a name="p35707847114454"></a>IMG.0136</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p61459513115557"><a name="p61459513115557"></a><a name="p61459513115557"></a>Failed to create a full-ECS image because a backup is being created for the <span id="text144614815516"><a name="text144614815516"></a><a name="text144614815516"></a></span><span id="text5471148185519"><a name="text5471148185519"></a><a name="text5471148185519"></a>ECS</span>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p11701428153814"><a name="p11701428153814"></a><a name="p11701428153814"></a>Failed to create a full-ECS image because the ECS is being backed up.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p127112413619"><a name="p127112413619"></a><a name="p127112413619"></a>Wait until the CSBS backup becomes available.</p>
</td>
</tr>
<tr id="row39748411114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p784414814190"><a name="p784414814190"></a><a name="p784414814190"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p59890517114454"><a name="p59890517114454"></a><a name="p59890517114454"></a>IMG.0137</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p42372781115557"><a name="p42372781115557"></a><a name="p42372781115557"></a>Failed to obtain the <span id="text179281510561"><a name="text179281510561"></a><a name="text179281510561"></a></span><span id="text199283514567"><a name="text199283514567"></a><a name="text199283514567"></a>ECS</span> information.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p20185128143810"><a name="p20185128143810"></a><a name="p20185128143810"></a>Failed to obtain the VM information.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p169218268351"><a name="p169218268351"></a><a name="p169218268351"></a>Check whether the <span id="text167487810563"><a name="text167487810563"></a><a name="text167487810563"></a></span><span id="text117487819561"><a name="text117487819561"></a><a name="text117487819561"></a>ECS</span> ID is correct and whether you have the permission to perform operations on the <span id="text13947151025619"><a name="text13947151025619"></a><a name="text13947151025619"></a></span><span id="text1294712104560"><a name="text1294712104560"></a><a name="text1294712104560"></a>ECS</span>.</p>
</td>
</tr>
<tr id="row34758191114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p58441348201912"><a name="p58441348201912"></a><a name="p58441348201912"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p39425932114454"><a name="p39425932114454"></a><a name="p39425932114454"></a>IMG.0138</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p19680309115557"><a name="p19680309115557"></a><a name="p19680309115557"></a>Failed to obtain the OS type information.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1220015283386"><a name="p1220015283386"></a><a name="p1220015283386"></a>Failed to obtain the OS type information.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1692026113510"><a name="p1692026113510"></a><a name="p1692026113510"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row39310374114422"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p384444841916"><a name="p384444841916"></a><a name="p384444841916"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p18910853114454"><a name="p18910853114454"></a><a name="p18910853114454"></a>IMG.0139</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p52757298115557"><a name="p52757298115557"></a><a name="p52757298115557"></a>Other disks on the <span id="text1478961312561"><a name="text1478961312561"></a><a name="text1478961312561"></a></span><span id="text3789161305615"><a name="text3789161305615"></a><a name="text3789161305615"></a>ECS</span> are being used to created ECSs.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p182141128163812"><a name="p182141128163812"></a><a name="p182141128163812"></a>Other disks on the VM are being used to created VMs.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p2692152612358"><a name="p2692152612358"></a><a name="p2692152612358"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row1283753011453"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p686024815191"><a name="p686024815191"></a><a name="p686024815191"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p541330311453"><a name="p541330311453"></a><a name="p541330311453"></a>IMG.0140</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p6691729115557"><a name="p6691729115557"></a><a name="p6691729115557"></a>The disks in the request are from different ECSs.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p72301928103810"><a name="p72301928103810"></a><a name="p72301928103810"></a>The disks in the request come from different ECSs.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p18692192614359"><a name="p18692192614359"></a><a name="p18692192614359"></a>Ensure that the ECS to which the disks are attached is the same.</p>
</td>
</tr>
<tr id="row1966532131817"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1886014881918"><a name="p1886014881918"></a><a name="p1886014881918"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p1066516215183"><a name="p1066516215183"></a><a name="p1066516215183"></a>IMG.0141</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p126659281813"><a name="p126659281813"></a><a name="p126659281813"></a>The value of <strong id="b842352706163246"><a name="b842352706163246"></a><a name="b842352706163246"></a>hw_firmware_type</strong> is not <strong id="b842352706163251"><a name="b842352706163251"></a><a name="b842352706163251"></a>uefi</strong> or <strong id="b84235270616331"><a name="b84235270616331"></a><a name="b84235270616331"></a>bios</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p2024152893812"><a name="p2024152893812"></a><a name="p2024152893812"></a>The value of <strong id="b1565029575"><a name="b1565029575"></a><a name="b1565029575"></a>hw_firmware_type</strong> is not <strong id="b1228460325"><a name="b1228460325"></a><a name="b1228460325"></a>uefi</strong> or <strong id="b1745692462"><a name="b1745692462"></a><a name="b1745692462"></a>bios</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p2069202603512"><a name="p2069202603512"></a><a name="p2069202603512"></a>Set <strong id="b84235270617416"><a name="b84235270617416"></a><a name="b84235270617416"></a>hw_firmware_type</strong> to <strong id="b84235270617419"><a name="b84235270617419"></a><a name="b84235270617419"></a>uefi</strong> or <strong id="b842352706174119"><a name="b842352706174119"></a><a name="b842352706174119"></a>bios</strong>.</p>
</td>
</tr>
<tr id="row77553918310"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p983737337"><a name="p983737337"></a><a name="p983737337"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p779465315317"><a name="p779465315317"></a><a name="p779465315317"></a>IMG.0144</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p1575519913311"><a name="p1575519913311"></a><a name="p1575519913311"></a>The image does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p16294102813384"><a name="p16294102813384"></a><a name="p16294102813384"></a>The image does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1369216267358"><a name="p1369216267358"></a><a name="p1369216267358"></a>Check whether the image exists.</p>
</td>
</tr>
<tr id="row8802172214310"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p19997377314"><a name="p19997377314"></a><a name="p19997377314"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p1480885314310"><a name="p1480885314310"></a><a name="p1480885314310"></a>IMG.0145</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p0802322138"><a name="p0802322138"></a><a name="p0802322138"></a>The project name is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p16307328123811"><a name="p16307328123811"></a><a name="p16307328123811"></a>The project name is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p186921826143520"><a name="p186921826143520"></a><a name="p186921826143520"></a>Enter a correct project name.</p>
</td>
</tr>
<tr id="row68808291236"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p31307371432"><a name="p31307371432"></a><a name="p31307371432"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p195896161046"><a name="p195896161046"></a><a name="p195896161046"></a>IMG.0148</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p78805291231"><a name="p78805291231"></a><a name="p78805291231"></a>The image is being exported.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p193461328163812"><a name="p193461328163812"></a><a name="p193461328163812"></a>The image is being exported.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p18692192683514"><a name="p18692192683514"></a><a name="p18692192683514"></a>Wait until the image is exported.</p>
</td>
</tr>
<tr id="row118807291132"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p32866391130"><a name="p32866391130"></a><a name="p32866391130"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p788072911313"><a name="p788072911313"></a><a name="p788072911313"></a>IMG.0153</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p1088019291739"><a name="p1088019291739"></a><a name="p1088019291739"></a>DESS or DSS disks cannot be used to create images.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p34091528143818"><a name="p34091528143818"></a><a name="p34091528143818"></a>DESS or DSS disks cannot be used to create images.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p5452185331418"><a name="p5452185331418"></a><a name="p5452185331418"></a>Select another <span id="text181451212175714"><a name="text181451212175714"></a><a name="text181451212175714"></a></span><span id="text16146201218572"><a name="text16146201218572"></a><a name="text16146201218572"></a>ECS</span>.</p>
</td>
</tr>
<tr id="row1845952944319"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p4302739839"><a name="p4302739839"></a><a name="p4302739839"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p18740145284315"><a name="p18740145284315"></a><a name="p18740145284315"></a>IMG.0154</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p67357413449"><a name="p67357413449"></a><a name="p67357413449"></a>Failed to communicate with EPS.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p134231281388"><a name="p134231281388"></a><a name="p134231281388"></a>Failed to communicate with Enterprise Project Management Service (EPS).</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1869322615359"><a name="p1869322615359"></a><a name="p1869322615359"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row1521123310535"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p621283317530"><a name="p621283317530"></a><a name="p621283317530"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p1521213335531"><a name="p1521213335531"></a><a name="p1521213335531"></a>IMG.0160</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p8658182792413"><a name="p8658182792413"></a><a name="p8658182792413"></a>Only images smaller than 128 GB can be exported.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p20177541192418"><a name="p20177541192418"></a><a name="p20177541192418"></a>Only images less than 128 GB can be exported.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1221210333532"><a name="p1221210333532"></a><a name="p1221210333532"></a>Images larger than 128 GB cannot be exported.</p>
</td>
</tr>
<tr id="row4320317125414"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p4320417155410"><a name="p4320417155410"></a><a name="p4320417155410"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p153201917165420"><a name="p153201917165420"></a><a name="p153201917165420"></a>IMG.0165</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p56841730291"><a name="p56841730291"></a><a name="p56841730291"></a>You do not have permission to access the CSBS backup.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1864159132912"><a name="p1864159132912"></a><a name="p1864159132912"></a>You do not have permission to access the CSBS backup.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p132071710544"><a name="p132071710544"></a><a name="p132071710544"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row84042194541"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p16404101905414"><a name="p16404101905414"></a><a name="p16404101905414"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p13404171935417"><a name="p13404171935417"></a><a name="p13404171935417"></a>IMG.0166</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p202381522102915"><a name="p202381522102915"></a><a name="p202381522102915"></a>OS version information must be contained when an ISO file is used to create an image.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1654311329295"><a name="p1654311329295"></a><a name="p1654311329295"></a>OS information must be contained in the ISO files used to create images.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p15404151975413"><a name="p15404151975413"></a><a name="p15404151975413"></a>OS version information must be contained when an ISO file is used to create an image.</p>
</td>
</tr>
<tr id="row5606101355411"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1760641335411"><a name="p1760641335411"></a><a name="p1760641335411"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p12607131385412"><a name="p12607131385412"></a><a name="p12607131385412"></a>IMG.0167</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p10885339142919"><a name="p10885339142919"></a><a name="p10885339142919"></a>The ISO image does not support this function.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1356804862915"><a name="p1356804862915"></a><a name="p1356804862915"></a>This operation cannot be performed for ISO images.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p10607141316547"><a name="p10607141316547"></a><a name="p10607141316547"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row5106776545"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p111073745420"><a name="p111073745420"></a><a name="p111073745420"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p4107167155416"><a name="p4107167155416"></a><a name="p4107167155416"></a>IMG.0168</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p11446953112918"><a name="p11446953112918"></a><a name="p11446953112918"></a>Data disk images cannot be updated.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p2294110163015"><a name="p2294110163015"></a><a name="p2294110163015"></a>Data disk images cannot be updated.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1310717745413"><a name="p1310717745413"></a><a name="p1310717745413"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row7866104595317"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p15788456155313"><a name="p15788456155313"></a><a name="p15788456155313"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p97881456145312"><a name="p97881456145312"></a><a name="p97881456145312"></a>IMG.0169</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p1763810143014"><a name="p1763810143014"></a><a name="p1763810143014"></a>Failed to update the image because the OS versions are different.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p4996841301"><a name="p4996841301"></a><a name="p4996841301"></a>Failed to update the image because the OS versions are different.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p8788856165312"><a name="p8788856165312"></a><a name="p8788856165312"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row517095125414"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p3170255548"><a name="p3170255548"></a><a name="p3170255548"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p1017015195412"><a name="p1017015195412"></a><a name="p1017015195412"></a>IMG.0170</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p17414102493016"><a name="p17414102493016"></a><a name="p17414102493016"></a>Failed to update the image because the image formats are different.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p18996134603016"><a name="p18996134603016"></a><a name="p18996134603016"></a>Failed to update the image because the image formats are different.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1917015575417"><a name="p1917015575417"></a><a name="p1917015575417"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row4296183145413"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p32961334544"><a name="p32961334544"></a><a name="p32961334544"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p102964385415"><a name="p102964385415"></a><a name="p102964385415"></a>IMG.0171</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p27031329303"><a name="p27031329303"></a><a name="p27031329303"></a>Failed to update the image because the minimum disk space is less than that of the source image.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p12263452103018"><a name="p12263452103018"></a><a name="p12263452103018"></a>Failed to update the image because the minimum disk space is less than that of the source image.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p829617317549"><a name="p829617317549"></a><a name="p829617317549"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row078201135420"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p97831125412"><a name="p97831125412"></a><a name="p97831125412"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p17786175410"><a name="p17786175410"></a><a name="p17786175410"></a>IMG.0172</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p1376163743014"><a name="p1376163743014"></a><a name="p1376163743014"></a>Failed to update the image because the minimum memory is less than that of the source image.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1651335716303"><a name="p1651335716303"></a><a name="p1651335716303"></a>Failed to update the image because the minimum memory is less than that of the source image.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p20791318543"><a name="p20791318543"></a><a name="p20791318543"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row63451964913"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p834576890"><a name="p834576890"></a><a name="p834576890"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p94803582092"><a name="p94803582092"></a><a name="p94803582092"></a>IMG.0173</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p839124273012"><a name="p839124273012"></a><a name="p839124273012"></a>Failed to update the image because the image environment types are different.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p138100210315"><a name="p138100210315"></a><a name="p138100210315"></a>Failed to update the image because the image environment types are different.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p93468615918"><a name="p93468615918"></a><a name="p93468615918"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row1059121211920"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1959112121395"><a name="p1959112121395"></a><a name="p1959112121395"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p2760205919918"><a name="p2760205919918"></a><a name="p2760205919918"></a>IMG.0174</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p1586312215329"><a name="p1586312215329"></a><a name="p1586312215329"></a>Failed to update the image because the name of the source image is different from that of the target image.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p699611603115"><a name="p699611603115"></a><a name="p699611603115"></a>Failed to update the image because the name of the source image is different from that of the target image.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1459110125914"><a name="p1459110125914"></a><a name="p1459110125914"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row1172151813913"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p2721218299"><a name="p2721218299"></a><a name="p2721218299"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p1259414018106"><a name="p1259414018106"></a><a name="p1259414018106"></a>IMG.0175</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p543131017325"><a name="p543131017325"></a><a name="p543131017325"></a>The folder name and image file name cannot contain spaces.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p17372142415317"><a name="p17372142415317"></a><a name="p17372142415317"></a>The folder name and image file name cannot contain spaces.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p3721118696"><a name="p3721118696"></a><a name="p3721118696"></a>Check whether the file name is valid.</p>
</td>
</tr>
<tr id="row9818121610920"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1181812167917"><a name="p1181812167917"></a><a name="p1181812167917"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p839512120106"><a name="p839512120106"></a><a name="p839512120106"></a>IMG.0176</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p1971361420328"><a name="p1971361420328"></a><a name="p1971361420328"></a>Failed to delete the full-ECS backup.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1411942923119"><a name="p1411942923119"></a><a name="p1411942923119"></a>Failed to delete the full-ECS backup.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p5818121619914"><a name="p5818121619914"></a><a name="p5818121619914"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row1726614198"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1572731411917"><a name="p1572731411917"></a><a name="p1572731411917"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p1918116251019"><a name="p1918116251019"></a><a name="p1918116251019"></a>IMG.0177</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p18610919133210"><a name="p18610919133210"></a><a name="p18610919133210"></a>The source and target tenants reside in different regions.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p171957347314"><a name="p171957347314"></a><a name="p171957347314"></a>The source and target tenants reside in different regions.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1572711140917"><a name="p1572711140917"></a><a name="p1572711140917"></a>Check whether the source and target tenants reside in the same region.</p>
</td>
</tr>
<tr id="row1360761010910"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p060731016916"><a name="p060731016916"></a><a name="p060731016916"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p935934100"><a name="p935934100"></a><a name="p935934100"></a>IMG.0178</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p15705194723219"><a name="p15705194723219"></a><a name="p15705194723219"></a>The target tenant is the same as the source tenant.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p205411439113113"><a name="p205411439113113"></a><a name="p205411439113113"></a>The target tenant is the same as the source tenant.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p17607310796"><a name="p17607310796"></a><a name="p17607310796"></a>The target tenant cannot be the same as the source tenant. Please check.</p>
</td>
</tr>
<tr id="row95701184917"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p195701381195"><a name="p195701381195"></a><a name="p195701381195"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p199011381015"><a name="p199011381015"></a><a name="p199011381015"></a>IMG.0179</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p122912539327"><a name="p122912539327"></a><a name="p122912539327"></a>The token of the source image agency is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p11213124520314"><a name="p11213124520314"></a><a name="p11213124520314"></a>The token of the source image agency is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p16570387915"><a name="p16570387915"></a><a name="p16570387915"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row6219162819262"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p6219142832617"><a name="p6219142832617"></a><a name="p6219142832617"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p7917191722718"><a name="p7917191722718"></a><a name="p7917191722718"></a>IMG.0181</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p1233215323315"><a name="p1233215323315"></a><a name="p1233215323315"></a>Failed to obtain ECSs that can be protected.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p20459175619316"><a name="p20459175619316"></a><a name="p20459175619316"></a>Failed to obtain ECSs that can be protected.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p521932818267"><a name="p521932818267"></a><a name="p521932818267"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row157198520272"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p10719135162714"><a name="p10719135162714"></a><a name="p10719135162714"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p74031223112717"><a name="p74031223112717"></a><a name="p74031223112717"></a>IMG.0186</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p7343121223418"><a name="p7343121223418"></a><a name="p7343121223418"></a>The ECS is associated with the CSBS service.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p1371020221355"><a name="p1371020221355"></a><a name="p1371020221355"></a>The ECS is associated with the CSBS service.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1657164515404"><a name="p1657164515404"></a><a name="p1657164515404"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row1492851162714"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1392810192715"><a name="p1392810192715"></a><a name="p1392810192715"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p15353122717276"><a name="p15353122717276"></a><a name="p15353122717276"></a>IMG.0187</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p1777316160345"><a name="p1777316160345"></a><a name="p1777316160345"></a>KMS access traffic has reached the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p16474122816355"><a name="p16474122816355"></a><a name="p16474122816355"></a>KMS access traffic has reached the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p741434754016"><a name="p741434754016"></a><a name="p741434754016"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row82741530172612"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p14274930162619"><a name="p14274930162619"></a><a name="p14274930162619"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p1750223282719"><a name="p1750223282719"></a><a name="p1750223282719"></a>IMG.0191</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p101340514365"><a name="p101340514365"></a><a name="p101340514365"></a>Failed to query ECS flavors.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p4158555113514"><a name="p4158555113514"></a><a name="p4158555113514"></a>Failed to query ECS flavors.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p22982334110"><a name="p22982334110"></a><a name="p22982334110"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row12151657142612"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p172161157172616"><a name="p172161157172616"></a><a name="p172161157172616"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p12475193319277"><a name="p12475193319277"></a><a name="p12475193319277"></a>IMG.0192</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p131781691369"><a name="p131781691369"></a><a name="p131781691369"></a>The flavor used to query images is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p173831658153617"><a name="p173831658153617"></a><a name="p173831658153617"></a>The flavor used to query images is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p13892643413"><a name="p13892643413"></a><a name="p13892643413"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row1284315113347"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p7843151123420"><a name="p7843151123420"></a><a name="p7843151123420"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p188437117341"><a name="p188437117341"></a><a name="p188437117341"></a>IMG.0194</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p5500191933615"><a name="p5500191933615"></a><a name="p5500191933615"></a>The maximum number of images that can be imported at one time has been reached.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p158214603717"><a name="p158214603717"></a><a name="p158214603717"></a>The maximum number of images that can be imported at one time has been reached.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p129765440411"><a name="p129765440411"></a><a name="p129765440411"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row1395911833417"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p7959287346"><a name="p7959287346"></a><a name="p7959287346"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p995913813414"><a name="p995913813414"></a><a name="p995913813414"></a>IMG.0195</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p06112513618"><a name="p06112513618"></a><a name="p06112513618"></a>Full-ECS images created from CBR backups must contain the OS version.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p107991310113718"><a name="p107991310113718"></a><a name="p107991310113718"></a>Full-ECS images created from CBR backups must contain an OS.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p159591481346"><a name="p159591481346"></a><a name="p159591481346"></a>Specify the OS version.</p>
</td>
</tr>
<tr id="row11360165819332"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p1036015585336"><a name="p1036015585336"></a><a name="p1036015585336"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p1536016588338"><a name="p1536016588338"></a><a name="p1536016588338"></a>IMG.0196</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p19587112913367"><a name="p19587112913367"></a><a name="p19587112913367"></a>The image cannot be replicated because it is not accepted by the recipient.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p9310181413712"><a name="p9310181413712"></a><a name="p9310181413712"></a>The image cannot be replicated because it is not accepted by the recipient.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p036055823310"><a name="p036055823310"></a><a name="p036055823310"></a>Accept the shared image.</p>
</td>
</tr>
<tr id="row1978117383411"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p77811333342"><a name="p77811333342"></a><a name="p77811333342"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p178114311340"><a name="p178114311340"></a><a name="p178114311340"></a>IMG.0197</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p197653917361"><a name="p197653917361"></a><a name="p197653917361"></a>Failed to replicate the shared image because it is encrypted using KMS.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p18360121823713"><a name="p18360121823713"></a><a name="p18360121823713"></a>Failed to replicate the shared image because it is encrypted using KMS.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p1078163163410"><a name="p1078163163410"></a><a name="p1078163163410"></a>Shared encrypted images cannot be replicated.</p>
</td>
</tr>
<tr id="row72043123415"><td class="cellrowborder" valign="top" width="11.65%" headers="mcps1.2.6.1.1 "><p id="p12041318349"><a name="p12041318349"></a><a name="p12041318349"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.12%" headers="mcps1.2.6.1.2 "><p id="p11204101163413"><a name="p11204101163413"></a><a name="p11204101163413"></a>IMG.0198</p>
</td>
<td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.2.6.1.3 "><p id="p1085285217368"><a name="p1085285217368"></a><a name="p1085285217368"></a>Backup ID does not match the backup type or the backup does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="23.87%" headers="mcps1.2.6.1.4 "><p id="p99481421183719"><a name="p99481421183719"></a><a name="p99481421183719"></a>Backup id is not match with backup type or not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="30.659999999999997%" headers="mcps1.2.6.1.5 "><p id="p192041316344"><a name="p192041316344"></a><a name="p192041316344"></a>Check whether the backup ID and backup type match.</p>
</td>
</tr>
</tbody>
</table>

