# Error Codes<a name="dcs-api-0312044"></a>

## Failure Responses<a name="section129721954152018"></a>

If an error occurs in API calling, HTTP status code 4xx or 5xx is returned.  **FailMessage**  is used as the response body to describe the cause of an error.

## Response Message \(v1.0\)<a name="section495413418434"></a>

**Table  1**  FailMessage parameter description

<a name="table42315565438"></a>
<table><thead align="left"><tr id="row6232175612437"><th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.5.1.1"><p id="p11232165614435"><a name="p11232165614435"></a><a name="p11232165614435"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.5.1.2"><p id="p122324563434"><a name="p122324563434"></a><a name="p122324563434"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.3"><p id="p623225644310"><a name="p623225644310"></a><a name="p623225644310"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.5.1.4"><p id="p823245617437"><a name="p823245617437"></a><a name="p823245617437"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12232105616432"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.1 "><p id="p523219564433"><a name="p523219564433"></a><a name="p523219564433"></a>error</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p223235616432"><a name="p223235616432"></a><a name="p223235616432"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p423235613430"><a name="p423235613430"></a><a name="p423235613430"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p2232195684319"><a name="p2232195684319"></a><a name="p2232195684319"></a>Error description. For details, see <a href="#table9232115644314">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Failure response parameter description

<a name="table9232115644314"></a>
<table><thead align="left"><tr id="row1223225620433"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p6232175674315"><a name="p6232175674315"></a><a name="p6232175674315"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.2"><p id="p10232656174320"><a name="p10232656174320"></a><a name="p10232656174320"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p1823265634313"><a name="p1823265634313"></a><a name="p1823265634313"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1723275634310"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p623255619434"><a name="p623255619434"></a><a name="p623255619434"></a>code</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p19232856194320"><a name="p19232856194320"></a><a name="p19232856194320"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1123211562431"><a name="p1123211562431"></a><a name="p1123211562431"></a>Error code. For details, see <a href="#table4581796">Table 4</a>.</p>
</td>
</tr>
<tr id="row623255619430"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1623215634316"><a name="p1623215634316"></a><a name="p1623215634316"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p823355613434"><a name="p823355613434"></a><a name="p823355613434"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p15233105614316"><a name="p15233105614316"></a><a name="p15233105614316"></a>Error information.</p>
</td>
</tr>
</tbody>
</table>

## Example Response \(v1.0\)<a name="section185402425431"></a>

```
{
    "error": {
        "code": "111404022",
        "message": "This DCS instance does not exist."
    }
}
```

## Response \(v2\)<a name="section1249454813445"></a>

**Table  3**  Failure response parameter description

<a name="table1562494813443"></a>
<table><thead align="left"><tr id="row5646148164415"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p1165464874416"><a name="p1165464874416"></a><a name="p1165464874416"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.2"><p id="p1766014485443"><a name="p1766014485443"></a><a name="p1766014485443"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p1866618486449"><a name="p1866618486449"></a><a name="p1866618486449"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6675648194417"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p206811748104411"><a name="p206811748104411"></a><a name="p206811748104411"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p7688164817449"><a name="p7688164817449"></a><a name="p7688164817449"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p26942487445"><a name="p26942487445"></a><a name="p26942487445"></a>Error code. For details, see <a href="#table4581796">Table 4</a>.</p>
</td>
</tr>
<tr id="row1703548114415"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p117081748194410"><a name="p117081748194410"></a><a name="p117081748194410"></a>error_msg</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p187161948204410"><a name="p187161948204410"></a><a name="p187161948204410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p17724148114416"><a name="p17724148114416"></a><a name="p17724148114416"></a>Detailed error information.</p>
</td>
</tr>
</tbody>
</table>

## Example Response \(v2\)<a name="section197301448134411"></a>

```
{
        "error_code": "DCS.8001",
        "error_msg": "fail to get order id."
}
```

## Error Code<a name="section20348152412118"></a>

[Table 4](#table4581796)  lists common DCS error codes.

**Table  4**  Error codes

<a name="table4581796"></a>
<table><thead align="left"><tr id="row32073719"><th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.4.1.1"><p id="p49387472"><a name="p49387472"></a><a name="p49387472"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.4.1.2"><p id="p40962311"><a name="p40962311"></a><a name="p40962311"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="69.69696969696969%" id="mcps1.2.4.1.3"><p id="p29612923"><a name="p29612923"></a><a name="p29612923"></a>Error Message</p>
</th>
</tr>
</thead>
<tbody><tr id="row49836563"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p15519212619"><a name="p15519212619"></a><a name="p15519212619"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p16520201216113"><a name="p16520201216113"></a><a name="p16520201216113"></a>111400002</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1052018121413"><a name="p1052018121413"></a><a name="p1052018121413"></a>Invalid project ID format.</p>
</td>
</tr>
<tr id="row22891915"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p155206125118"><a name="p155206125118"></a><a name="p155206125118"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p115201212710"><a name="p115201212710"></a><a name="p115201212710"></a>111400004</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p252018121111"><a name="p252018121111"></a><a name="p252018121111"></a>Empty request body.</p>
</td>
</tr>
<tr id="row56688054"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p75201212416"><a name="p75201212416"></a><a name="p75201212416"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p185208128119"><a name="p185208128119"></a><a name="p185208128119"></a>111400005</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1452015121515"><a name="p1452015121515"></a><a name="p1452015121515"></a>The message body contains invalid characters or is not in JSON format.</p>
</td>
</tr>
<tr id="row17540457"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1552001213113"><a name="p1552001213113"></a><a name="p1552001213113"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p135201121213"><a name="p135201121213"></a><a name="p135201121213"></a>111400007</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p7520181210118"><a name="p7520181210118"></a><a name="p7520181210118"></a>The selected cache engine edition is not supported.</p>
</td>
</tr>
<tr id="row55822426"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p13520181216116"><a name="p13520181216116"></a><a name="p13520181216116"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p2520012918"><a name="p2520012918"></a><a name="p2520012918"></a>111400008</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p352019121713"><a name="p352019121713"></a><a name="p352019121713"></a>The selected cache engine version is not supported.</p>
</td>
</tr>
<tr id="row22680839"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p752010123114"><a name="p752010123114"></a><a name="p752010123114"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p135201612514"><a name="p135201612514"></a><a name="p135201612514"></a>111400009</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p135203121718"><a name="p135203121718"></a><a name="p135203121718"></a>Invalid product ID in the request.</p>
</td>
</tr>
<tr id="row96701341261"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p205201712416"><a name="p205201712416"></a><a name="p205201712416"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p7520912112"><a name="p7520912112"></a><a name="p7520912112"></a>111400010</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p452014121412"><a name="p452014121412"></a><a name="p452014121412"></a>Invalid DCS instance name. The name must be 4 to 64 characters long. Only letters, digits, underscores (_), and hyphens (-) are allowed.</p>
</td>
</tr>
<tr id="row1748744216613"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p75201912216"><a name="p75201912216"></a><a name="p75201912216"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p852017121818"><a name="p852017121818"></a><a name="p852017121818"></a>111400011</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p25203121615"><a name="p25203121615"></a><a name="p25203121615"></a>DCS instance description cannot exceed 1024 characters.</p>
</td>
</tr>
<tr id="row379804220615"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1352010128115"><a name="p1352010128115"></a><a name="p1352010128115"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1352015123114"><a name="p1352015123114"></a><a name="p1352015123114"></a>111400012</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p0520812316"><a name="p0520812316"></a><a name="p0520812316"></a>Invalid capacity parameter in the request.</p>
</td>
</tr>
<tr id="row581443666"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p105209128115"><a name="p105209128115"></a><a name="p105209128115"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p16520912913"><a name="p16520912913"></a><a name="p16520912913"></a>111400013</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1952011120117"><a name="p1952011120117"></a><a name="p1952011120117"></a>Invalid <strong id="b314004310326"><a name="b314004310326"></a><a name="b314004310326"></a>vpc_id</strong> in the request.</p>
</td>
</tr>
<tr id="row1219634313614"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p652015121911"><a name="p652015121911"></a><a name="p652015121911"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p155201712715"><a name="p155201712715"></a><a name="p155201712715"></a>111400014</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p16520612215"><a name="p16520612215"></a><a name="p16520612215"></a>Invalid <strong id="b5613103818320"><a name="b5613103818320"></a><a name="b5613103818320"></a>security_group_id</strong> in the request.</p>
</td>
</tr>
<tr id="row237215432613"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p9520712713"><a name="p9520712713"></a><a name="p9520712713"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p175201812613"><a name="p175201812613"></a><a name="p175201812613"></a>111400016</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p95205121415"><a name="p95205121415"></a><a name="p95205121415"></a>Invalid <strong id="b13463114733211"><a name="b13463114733211"></a><a name="b13463114733211"></a>subnet_id</strong> in the request.</p>
</td>
</tr>
<tr id="row011174551"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p4143111010515"><a name="p4143111010515"></a><a name="p4143111010515"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p01445102515"><a name="p01445102515"></a><a name="p01445102515"></a>111400017</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p71442101251"><a name="p71442101251"></a><a name="p71442101251"></a>A background task associated with this instance is running.</p>
</td>
</tr>
<tr id="row13576104317613"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p2521161218120"><a name="p2521161218120"></a><a name="p2521161218120"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p852121216114"><a name="p852121216114"></a><a name="p852121216114"></a>111400018</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p115214121815"><a name="p115214121815"></a><a name="p115214121815"></a>This subnet must exist in the VPC.</p>
</td>
</tr>
<tr id="row67561243862"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p752111121919"><a name="p752111121919"></a><a name="p752111121919"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p145212012214"><a name="p145212012214"></a><a name="p145212012214"></a>111400019</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p145211212513"><a name="p145211212513"></a><a name="p145211212513"></a>The password does not meet complexity requirements.</p>
</td>
</tr>
<tr id="row99408434616"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p85211112713"><a name="p85211112713"></a><a name="p85211112713"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p552119121017"><a name="p552119121017"></a><a name="p552119121017"></a>111400020</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p55213121912"><a name="p55213121912"></a><a name="p55213121912"></a>DHCP must be enabled for this subnet.</p>
</td>
</tr>
<tr id="row11925153113810"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p692583193810"><a name="p692583193810"></a><a name="p692583193810"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1392514315384"><a name="p1392514315384"></a><a name="p1392514315384"></a>111400021</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p192512317381"><a name="p192512317381"></a><a name="p192512317381"></a>Invalid <strong id="b689601693317"><a name="b689601693317"></a><a name="b689601693317"></a>isAutoRenew</strong> in the request. It must be either <strong id="b638614236331"><a name="b638614236331"></a><a name="b638614236331"></a>0</strong> or <strong id="b093543113336"><a name="b093543113336"></a><a name="b093543113336"></a>1</strong>.</p>
</td>
</tr>
<tr id="row776812509254"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p157941954172520"><a name="p157941954172520"></a><a name="p157941954172520"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p27996540250"><a name="p27996540250"></a><a name="p27996540250"></a>111400022</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p3804175411256"><a name="p3804175411256"></a><a name="p3804175411256"></a>The cache engine does not match the product ID.</p>
</td>
</tr>
<tr id="row161661244666"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1552113126118"><a name="p1552113126118"></a><a name="p1552113126118"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p452116125111"><a name="p452116125111"></a><a name="p452116125111"></a>111400026</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1752161210116"><a name="p1752161210116"></a><a name="p1752161210116"></a>This operation is not allowed when the DCS instance is in the current state.</p>
</td>
</tr>
<tr id="row718133317369"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p918114332369"><a name="p918114332369"></a><a name="p918114332369"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p14182733173615"><a name="p14182733173615"></a><a name="p14182733173615"></a>111400027</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p818293310368"><a name="p818293310368"></a><a name="p818293310368"></a>The current node does not support this operation.</p>
</td>
</tr>
<tr id="row196918375222"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p8846528224"><a name="p8846528224"></a><a name="p8846528224"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p284352182215"><a name="p284352182215"></a><a name="p284352182215"></a>111400035</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1784175252218"><a name="p1784175252218"></a><a name="p1784175252218"></a>DCS instance quota of the tenant is insufficient.</p>
</td>
</tr>
<tr id="row14492338162216"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p984352162219"><a name="p984352162219"></a><a name="p984352162219"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p58415210226"><a name="p58415210226"></a><a name="p58415210226"></a>111400036</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p198465218224"><a name="p198465218224"></a><a name="p198465218224"></a>Memory quota of the tenant is insufficient.</p>
</td>
</tr>
<tr id="row92344175353"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1831772093518"><a name="p1831772093518"></a><a name="p1831772093518"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p4317202012354"><a name="p4317202012354"></a><a name="p4317202012354"></a>111400037</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p667111426352"><a name="p667111426352"></a><a name="p667111426352"></a>The <strong id="b18268920133414"><a name="b18268920133414"></a><a name="b18268920133414"></a>instanceParams</strong> parameter in the request contains invalid characters or is not in JSON format.</p>
</td>
</tr>
<tr id="row994015178359"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p183171520173519"><a name="p183171520173519"></a><a name="p183171520173519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p18318152013515"><a name="p18318152013515"></a><a name="p18318152013515"></a>111400038</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p2067119429358"><a name="p2067119429358"></a><a name="p2067119429358"></a>The <strong id="b197661724123419"><a name="b197661724123419"></a><a name="b197661724123419"></a>periodNum</strong> parameter in the request must be an integer.</p>
</td>
</tr>
<tr id="row141931525203717"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p2194625143710"><a name="p2194625143710"></a><a name="p2194625143710"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p161945252372"><a name="p161945252372"></a><a name="p161945252372"></a>111400039</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p111948250377"><a name="p111948250377"></a><a name="p111948250377"></a>Your quota has been reached.</p>
</td>
</tr>
<tr id="row93833441068"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p145211121120"><a name="p145211121120"></a><a name="p145211121120"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1521212710"><a name="p1521212710"></a><a name="p1521212710"></a>111400042</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p8521912413"><a name="p8521912413"></a><a name="p8521912413"></a>This AZ does not exist.</p>
</td>
</tr>
<tr id="row127971244564"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p14521101211119"><a name="p14521101211119"></a><a name="p14521101211119"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1852171215111"><a name="p1852171215111"></a><a name="p1852171215111"></a>111400046</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p175215121717"><a name="p175215121717"></a><a name="p175215121717"></a>This security group does not exist.</p>
</td>
</tr>
<tr id="row109521474383"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p595384718381"><a name="p595384718381"></a><a name="p595384718381"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p18953154763820"><a name="p18953154763820"></a><a name="p18953154763820"></a>111400047</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1595315475385"><a name="p1595315475385"></a><a name="p1595315475385"></a>The <strong id="b1479511103517"><a name="b1479511103517"></a><a name="b1479511103517"></a>periodType</strong> parameter in the request must be either <strong id="b362671473514"><a name="b362671473514"></a><a name="b362671473514"></a>2</strong> or <strong id="b17263151611355"><a name="b17263151611355"></a><a name="b17263151611355"></a>3</strong>.</p>
</td>
</tr>
<tr id="row4992134412617"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p55215121711"><a name="p55215121711"></a><a name="p55215121711"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p135218121014"><a name="p135218121014"></a><a name="p135218121014"></a>111400048</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p105211612116"><a name="p105211612116"></a><a name="p105211612116"></a>The security group must have both outbound and inbound rules with protocols set to <strong id="b1846312823519"><a name="b1846312823519"></a><a name="b1846312823519"></a>ANY</strong>.</p>
</td>
</tr>
<tr id="row181874451613"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p175218121018"><a name="p175218121018"></a><a name="p175218121018"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1352110121012"><a name="p1352110121012"></a><a name="p1352110121012"></a>111400051</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p85211012214"><a name="p85211012214"></a><a name="p85211012214"></a>The package for upgrading the DCS instance to the target version was not found.</p>
</td>
</tr>
<tr id="row63799451666"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p85213127111"><a name="p85213127111"></a><a name="p85213127111"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p4521151211112"><a name="p4521151211112"></a><a name="p4521151211112"></a>111400052</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p185211912913"><a name="p185211912913"></a><a name="p185211912913"></a>The DCS instance to be upgraded must be in the <strong id="b779710496356"><a name="b779710496356"></a><a name="b779710496356"></a>Running</strong> state.</p>
</td>
</tr>
<tr id="row4583104510611"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p55211121215"><a name="p55211121215"></a><a name="p55211121215"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p3521412012"><a name="p3521412012"></a><a name="p3521412012"></a>111400053</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1852191210112"><a name="p1852191210112"></a><a name="p1852191210112"></a>The <strong id="b8274957143520"><a name="b8274957143520"></a><a name="b8274957143520"></a>targetVersion</strong> parameter in the request cannot be the same as the source version.</p>
</td>
</tr>
<tr id="row18766194510619"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p195221812311"><a name="p195221812311"></a><a name="p195221812311"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1352217124112"><a name="p1352217124112"></a><a name="p1352217124112"></a>111400054</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1252221210110"><a name="p1252221210110"></a><a name="p1252221210110"></a>The DCS quota in the selected AZ has been reached.</p>
</td>
</tr>
<tr id="row182381885116"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p0239480119"><a name="p0239480119"></a><a name="p0239480119"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p18239681217"><a name="p18239681217"></a><a name="p18239681217"></a>111400060</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p18239881516"><a name="p18239881516"></a><a name="p18239881516"></a>This instance name already exists.</p>
</td>
</tr>
<tr id="row119461245868"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1152219128119"><a name="p1152219128119"></a><a name="p1152219128119"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p15228121315"><a name="p15228121315"></a><a name="p15228121315"></a>111400061</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p185221312313"><a name="p185221312313"></a><a name="p185221312313"></a>Invalid instance ID format.</p>
</td>
</tr>
<tr id="row64813145414"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1648151410411"><a name="p1648151410411"></a><a name="p1648151410411"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p154817149411"><a name="p154817149411"></a><a name="p154817149411"></a>111400062</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p2048141464117"><a name="p2048141464117"></a><a name="p2048141464117"></a>Invalid parameter <strong id="b1669214283715"><a name="b1669214283715"></a><a name="b1669214283715"></a>{0}</strong> in the request.</p>
</td>
</tr>
<tr id="row1372764217496"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p17281742184915"><a name="p17281742184915"></a><a name="p17281742184915"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p12729642194917"><a name="p12729642194917"></a><a name="p12729642194917"></a>111400063</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p9729154254912"><a name="p9729154254912"></a><a name="p9729154254912"></a>Invalid parameter <strong id="b2835105418367"><a name="b2835105418367"></a><a name="b2835105418367"></a>{0}</strong> in the request.</p>
</td>
</tr>
<tr id="row151252461166"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p452218129112"><a name="p452218129112"></a><a name="p452218129112"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p15522612416"><a name="p15522612416"></a><a name="p15522612416"></a>111400064</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p11522151210115"><a name="p11522151210115"></a><a name="p11522151210115"></a>The <strong id="b1490902312362"><a name="b1490902312362"></a><a name="b1490902312362"></a>action</strong> parameter in the request must be <strong id="b955052673613"><a name="b955052673613"></a><a name="b955052673613"></a>start</strong>, <strong id="b318152817367"><a name="b318152817367"></a><a name="b318152817367"></a>stop</strong>, or <strong id="b4184129133620"><a name="b4184129133620"></a><a name="b4184129133620"></a>restart</strong>.</p>
</td>
</tr>
<tr id="row1829017463617"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p14522912918"><a name="p14522912918"></a><a name="p14522912918"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1852214125112"><a name="p1852214125112"></a><a name="p1852214125112"></a>111400065</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p125220121219"><a name="p125220121219"></a><a name="p125220121219"></a>The <strong id="b1120519332360"><a name="b1120519332360"></a><a name="b1120519332360"></a>instances</strong> parameter in the request cannot be a null value or left unspecified.</p>
</td>
</tr>
<tr id="row54421146465"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p19522121212116"><a name="p19522121212116"></a><a name="p19522121212116"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p55220121418"><a name="p55220121418"></a><a name="p55220121418"></a>111400066</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p55225122015"><a name="p55225122015"></a><a name="p55225122015"></a>Invalid configuration parameter <strong id="b1827011215376"><a name="b1827011215376"></a><a name="b1827011215376"></a>{0}</strong>.</p>
</td>
</tr>
<tr id="row1762517461961"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p352219126111"><a name="p352219126111"></a><a name="p352219126111"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1252213121119"><a name="p1252213121119"></a><a name="p1252213121119"></a>111400067</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p11522912218"><a name="p11522912218"></a><a name="p11522912218"></a>The <strong id="b1893632193820"><a name="b1893632193820"></a><a name="b1893632193820"></a>available_zones</strong> parameter in the request must be an array that contains only one AZ ID.</p>
</td>
</tr>
<tr id="row579915464610"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p14522111214111"><a name="p14522111214111"></a><a name="p14522111214111"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p105225121217"><a name="p105225121217"></a><a name="p105225121217"></a>111400068</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1452281211118"><a name="p1452281211118"></a><a name="p1452281211118"></a>This VPC does not exist.</p>
</td>
</tr>
<tr id="row168082441751"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p7911146552"><a name="p7911146552"></a><a name="p7911146552"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p19119460516"><a name="p19119460516"></a><a name="p19119460516"></a>111400070</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1291112467516"><a name="p1291112467516"></a><a name="p1291112467516"></a>Invalid task ID format.</p>
</td>
</tr>
<tr id="row18947144715224"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p0947134713229"><a name="p0947134713229"></a><a name="p0947134713229"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1594714712212"><a name="p1594714712212"></a><a name="p1594714712212"></a>111400072</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p11947184718223"><a name="p11947184718223"></a><a name="p11947184718223"></a>The value of the instance backup parameter <strong id="b1517132273812"><a name="b1517132273812"></a><a name="b1517132273812"></a>saveDays</strong> in the request must be between 1 and 7.</p>
</td>
</tr>
<tr id="row149531024142310"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1895382432314"><a name="p1895382432314"></a><a name="p1895382432314"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p8953182420238"><a name="p8953182420238"></a><a name="p8953182420238"></a>111400073</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p695320240234"><a name="p695320240234"></a><a name="p695320240234"></a>The value of the instance backup parameter <strong id="b136752919381"><a name="b136752919381"></a><a name="b136752919381"></a>backupType</strong> in the request must be either auto or manual.</p>
</td>
</tr>
<tr id="row942715278238"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p8427427122316"><a name="p8427427122316"></a><a name="p8427427122316"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p242762720233"><a name="p242762720233"></a><a name="p242762720233"></a>111400074</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p2427427202317"><a name="p2427427202317"></a><a name="p2427427202317"></a>The value of the instance backup parameter <strong id="b1325312344382"><a name="b1325312344382"></a><a name="b1325312344382"></a>periodType</strong> in the request must be weekly.</p>
</td>
</tr>
<tr id="row053219348247"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p553243415243"><a name="p553243415243"></a><a name="p553243415243"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1653210344243"><a name="p1653210344243"></a><a name="p1653210344243"></a>111400075</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p17532153415245"><a name="p17532153415245"></a><a name="p17532153415245"></a>The value of the instance backup parameter <strong id="b8223193943811"><a name="b8223193943811"></a><a name="b8223193943811"></a>backupAt</strong> in the request cannot be null or undefined.</p>
</td>
</tr>
<tr id="row1370512597246"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p197051259152413"><a name="p197051259152413"></a><a name="p197051259152413"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p10705185972413"><a name="p10705185972413"></a><a name="p10705185972413"></a>111400076</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1270545992411"><a name="p1270545992411"></a><a name="p1270545992411"></a>The value of the instance backup parameter <strong id="b1954164543816"><a name="b1954164543816"></a><a name="b1954164543816"></a>beginAt</strong> in the request must be in the 00:00–00:00 format.</p>
</td>
</tr>
<tr id="row168671214259"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p10867723252"><a name="p10867723252"></a><a name="p10867723252"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p9867429257"><a name="p9867429257"></a><a name="p9867429257"></a>111400080</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p286716292512"><a name="p286716292512"></a><a name="p286716292512"></a>Invalid password for accessing the selected DCS instance.</p>
</td>
</tr>
<tr id="row101350652513"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p213596132520"><a name="p213596132520"></a><a name="p213596132520"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1013519612253"><a name="p1013519612253"></a><a name="p1013519612253"></a>111400086</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1313596182518"><a name="p1313596182518"></a><a name="p1313596182518"></a>This operation is allowed only for master/standby DCS instances.</p>
</td>
</tr>
<tr id="row3259488255"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p32596892513"><a name="p32596892513"></a><a name="p32596892513"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p825918832516"><a name="p825918832516"></a><a name="p825918832516"></a>111400087</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p725958192513"><a name="p725958192513"></a><a name="p725958192513"></a>The restore operation is allowed only when the backup task is in the <strong id="b3167102114397"><a name="b3167102114397"></a><a name="b3167102114397"></a>Succeeded</strong> state.</p>
</td>
</tr>
<tr id="row49611443615"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p33896571819"><a name="p33896571819"></a><a name="p33896571819"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p538913571218"><a name="p538913571218"></a><a name="p538913571218"></a>111400094</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p33893575111"><a name="p33893575111"></a><a name="p33893575111"></a>The system does not support the background task function.</p>
</td>
</tr>
<tr id="row291810135270"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p189181113192713"><a name="p189181113192713"></a><a name="p189181113192713"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1091831315273"><a name="p1091831315273"></a><a name="p1091831315273"></a>111400095</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p6918141312715"><a name="p6918141312715"></a><a name="p6918141312715"></a>Backup and restoration are not supported.</p>
</td>
</tr>
<tr id="row1865193216273"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p2065113326277"><a name="p2065113326277"></a><a name="p2065113326277"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p156519327271"><a name="p156519327271"></a><a name="p156519327271"></a>111400096</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1465143262710"><a name="p1465143262710"></a><a name="p1465143262710"></a>Backing up the DCS instance... Please try again later.</p>
</td>
</tr>
<tr id="row207251115142720"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p7726101502718"><a name="p7726101502718"></a><a name="p7726101502718"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p12726121520277"><a name="p12726121520277"></a><a name="p12726121520277"></a>111400097</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p8726715162713"><a name="p8726715162713"></a><a name="p8726715162713"></a>Restoring the DCS instance... Please try again later.</p>
</td>
</tr>
<tr id="row35911817152711"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p65917170278"><a name="p65917170278"></a><a name="p65917170278"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1591181732717"><a name="p1591181732717"></a><a name="p1591181732717"></a>111400098</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p145911817112718"><a name="p145911817112718"></a><a name="p145911817112718"></a>The value of the <strong id="b13901574020"><a name="b13901574020"></a><a name="b13901574020"></a>remark</strong> parameter cannot exceed 128 characters long.</p>
</td>
</tr>
<tr id="row13569161915273"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p256911911275"><a name="p256911911275"></a><a name="p256911911275"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p35691819172714"><a name="p35691819172714"></a><a name="p35691819172714"></a>111400099</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p356916197274"><a name="p356916197274"></a><a name="p356916197274"></a>DCS instances in the <strong id="b1147113124017"><a name="b1147113124017"></a><a name="b1147113124017"></a>Creating</strong>, <strong id="b17963143510402"><a name="b17963143510402"></a><a name="b17963143510402"></a>Restarting</strong>, or <strong id="b916963994011"><a name="b916963994011"></a><a name="b916963994011"></a>Deleting</strong> state cannot be deleted.</p>
</td>
</tr>
<tr id="row144972162711"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1949221172719"><a name="p1949221172719"></a><a name="p1949221172719"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1149182182715"><a name="p1149182182715"></a><a name="p1149182182715"></a>111400100</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p44952112715"><a name="p44952112715"></a><a name="p44952112715"></a>The number of instance IDs in an instances array cannot exceed 50.</p>
</td>
</tr>
<tr id="row18291722921"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1655915304214"><a name="p1655915304214"></a><a name="p1655915304214"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p165596301429"><a name="p165596301429"></a><a name="p165596301429"></a>111400102</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1455912308217"><a name="p1455912308217"></a><a name="p1455912308217"></a>Scale-up is not supported.</p>
</td>
</tr>
<tr id="row2018619237215"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1355913305214"><a name="p1355913305214"></a><a name="p1355913305214"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p105593301526"><a name="p105593301526"></a><a name="p105593301526"></a>111400103</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p165596302026"><a name="p165596302026"></a><a name="p165596302026"></a>The capacity to which the DCS instance is scaled up must be greater than the original capacity.</p>
</td>
</tr>
<tr id="row20420165251812"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p3331140121917"><a name="p3331140121917"></a><a name="p3331140121917"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p933480131914"><a name="p933480131914"></a><a name="p933480131914"></a>111400105</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p18337150121919"><a name="p18337150121919"></a><a name="p18337150121919"></a>The value of <strong id="b1643989134112"><a name="b1643989134112"></a><a name="b1643989134112"></a>reserved-memory</strong> cannot be greater than the free memory size of this DCS instance.</p>
</td>
</tr>
<tr id="row97797231020"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1255918306211"><a name="p1255918306211"></a><a name="p1255918306211"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p8559133016218"><a name="p8559133016218"></a><a name="p8559133016218"></a>111400106</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p16559133017220"><a name="p16559133017220"></a><a name="p16559133017220"></a>Invalid maintenance time window.</p>
</td>
</tr>
<tr id="row1060219167525"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1797715216525"><a name="p1797715216525"></a><a name="p1797715216525"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1497702119520"><a name="p1497702119520"></a><a name="p1497702119520"></a>111400111</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p99776216526"><a name="p99776216526"></a><a name="p99776216526"></a>Restarting the DCS instance... Please try again later.</p>
</td>
</tr>
<tr id="row1240451711526"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p189771121155218"><a name="p189771121155218"></a><a name="p189771121155218"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1977921105217"><a name="p1977921105217"></a><a name="p1977921105217"></a>111400113</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p8978112155212"><a name="p8978112155212"></a><a name="p8978112155212"></a>Scaling up the DCS instance... Please try again later.</p>
</td>
</tr>
<tr id="row1581559521"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p99781221105219"><a name="p99781221105219"></a><a name="p99781221105219"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p197818216524"><a name="p197818216524"></a><a name="p197818216524"></a>111400114</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p8978102155216"><a name="p8978102155216"></a><a name="p8978102155216"></a>Modifying instance configuration... Please try again later.</p>
</td>
</tr>
<tr id="row12328710115211"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p139784214529"><a name="p139784214529"></a><a name="p139784214529"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p397882112524"><a name="p397882112524"></a><a name="p397882112524"></a>111400115</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p13978102135215"><a name="p13978102135215"></a><a name="p13978102135215"></a>Changing instance password... Please try again later.</p>
</td>
</tr>
<tr id="row3860111018524"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p2978162116526"><a name="p2978162116526"></a><a name="p2978162116526"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p18978102155216"><a name="p18978102155216"></a><a name="p18978102155216"></a>111400116</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p497832135210"><a name="p497832135210"></a><a name="p497832135210"></a>Upgrading the DCS instance... Please try again later.</p>
</td>
</tr>
<tr id="row1623621118520"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p4978521115219"><a name="p4978521115219"></a><a name="p4978521115219"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1097810214524"><a name="p1097810214524"></a><a name="p1097810214524"></a>111400117</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p18978162113522"><a name="p18978162113522"></a><a name="p18978162113522"></a>Rolling back the DCS instance... Please try again later.</p>
</td>
</tr>
<tr id="row241514117523"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p10978132115217"><a name="p10978132115217"></a><a name="p10978132115217"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p17978521115213"><a name="p17978521115213"></a><a name="p17978521115213"></a>111400118</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1497942195215"><a name="p1497942195215"></a><a name="p1497942195215"></a>Creating the DCS instance... Please try again later.</p>
</td>
</tr>
<tr id="row7343204120554"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p14344841135513"><a name="p14344841135513"></a><a name="p14344841135513"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p5666125117550"><a name="p5666125117550"></a><a name="p5666125117550"></a>111400119</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p73441341145514"><a name="p73441341145514"></a><a name="p73441341145514"></a>This DCS instance does not exist.</p>
</td>
</tr>
<tr id="row559514361719"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p51821343465"><a name="p51821343465"></a><a name="p51821343465"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p55969391711"><a name="p55969391711"></a><a name="p55969391711"></a>111400800</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p359614361717"><a name="p359614361717"></a><a name="p359614361717"></a>Invalid parameter <strong id="b1154083433719"><a name="b1154083433719"></a><a name="b1154083433719"></a>{0}</strong> in the request.</p>
</td>
</tr>
<tr id="row109761461867"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p952231212110"><a name="p952231212110"></a><a name="p952231212110"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p18522151219116"><a name="p18522151219116"></a><a name="p18522151219116"></a>111401001</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1852221212119"><a name="p1852221212119"></a><a name="p1852221212119"></a>Invalid token.</p>
</td>
</tr>
<tr id="row103468235526"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p15347323185213"><a name="p15347323185213"></a><a name="p15347323185213"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p9347192320527"><a name="p9347192320527"></a><a name="p9347192320527"></a>111401002</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p73471723115211"><a name="p73471723115211"></a><a name="p73471723115211"></a>Expired token.</p>
</td>
</tr>
<tr id="row91552047961"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p12522212218"><a name="p12522212218"></a><a name="p12522212218"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p952271217114"><a name="p952271217114"></a><a name="p952271217114"></a>111401003</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p652261210113"><a name="p652261210113"></a><a name="p652261210113"></a>Missing token.</p>
</td>
</tr>
<tr id="row1334334717616"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p65221212613"><a name="p65221212613"></a><a name="p65221212613"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1552271217116"><a name="p1552271217116"></a><a name="p1552271217116"></a>111401004</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p852251211118"><a name="p852251211118"></a><a name="p852251211118"></a>Project ID does not match the token.</p>
</td>
</tr>
<tr id="row85358472614"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p13522181211114"><a name="p13522181211114"></a><a name="p13522181211114"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p45228122112"><a name="p45228122112"></a><a name="p45228122112"></a>111403002</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p9522912113"><a name="p9522912113"></a><a name="p9522912113"></a>This tenant has read permissions only and cannot perform this operation.</p>
</td>
</tr>
<tr id="row6727154714618"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p145228127115"><a name="p145228127115"></a><a name="p145228127115"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p85225127118"><a name="p85225127118"></a><a name="p85225127118"></a>111403003</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p105221121119"><a name="p105221121119"></a><a name="p105221121119"></a>This role does not have the permissions to perform this operation.</p>
</td>
</tr>
<tr id="row1091711475616"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p9522712516"><a name="p9522712516"></a><a name="p9522712516"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p65225120117"><a name="p65225120117"></a><a name="p65225120117"></a>111404001</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1252291214115"><a name="p1252291214115"></a><a name="p1252291214115"></a>The requested URL does not exist.</p>
</td>
</tr>
<tr id="row29174811618"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p05221912617"><a name="p05221912617"></a><a name="p05221912617"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p10523171218119"><a name="p10523171218119"></a><a name="p10523171218119"></a>111404022</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p165232123114"><a name="p165232123114"></a><a name="p165232123114"></a>This DCS instance does not exist.</p>
</td>
</tr>
<tr id="row24421348667"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p330905575610"><a name="p330905575610"></a><a name="p330905575610"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p230912557567"><a name="p230912557567"></a><a name="p230912557567"></a>111405001</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p193091755105617"><a name="p193091755105617"></a><a name="p193091755105617"></a>This request method is not allowed.</p>
</td>
</tr>
<tr id="row18130184474218"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p16429154634214"><a name="p16429154634214"></a><a name="p16429154634214"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p4436194634210"><a name="p4436194634210"></a><a name="p4436194634210"></a>111400069</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p104404460421"><a name="p104404460421"></a><a name="p104404460421"></a>Another user is modifying configuration parameters of the DCS instance. Try again later.</p>
</td>
</tr>
<tr id="row1155539192318"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p13155143910230"><a name="p13155143910230"></a><a name="p13155143910230"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1115513920234"><a name="p1115513920234"></a><a name="p1115513920234"></a>111400101</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p7155439192312"><a name="p7155439192312"></a><a name="p7155439192312"></a>Failed to delete the instance backup files.</p>
</td>
</tr>
<tr id="row1419454332314"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p10194043112315"><a name="p10194043112315"></a><a name="p10194043112315"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1219464320235"><a name="p1219464320235"></a><a name="p1219464320235"></a>111400842</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p12194643162319"><a name="p12194643162319"></a><a name="p12194643162319"></a>Job execution failed.</p>
</td>
</tr>
<tr id="row1321125316583"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p630918559562"><a name="p630918559562"></a><a name="p630918559562"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1330918556565"><a name="p1330918556565"></a><a name="p1330918556565"></a>111500000</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1530995555614"><a name="p1530995555614"></a><a name="p1530995555614"></a>Internal service error.</p>
</td>
</tr>
<tr id="row203211453165815"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p143101555185617"><a name="p143101555185617"></a><a name="p143101555185617"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1331065515566"><a name="p1331065515566"></a><a name="p1331065515566"></a>111500006</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p93101055115614"><a name="p93101055115614"></a><a name="p93101055115614"></a>Internal service error.</p>
</td>
</tr>
<tr id="row6894757145818"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1131155555616"><a name="p1131155555616"></a><a name="p1131155555616"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p3311655115611"><a name="p3311655115611"></a><a name="p3311655115611"></a>111500017</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p8311955165616"><a name="p8311955165616"></a><a name="p8311955165616"></a>Internal service error.</p>
</td>
</tr>
<tr id="row118801444175415"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p0881164419541"><a name="p0881164419541"></a><a name="p0881164419541"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p19881134415416"><a name="p19881134415416"></a><a name="p19881134415416"></a>111500020</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1988119447547"><a name="p1988119447547"></a><a name="p1988119447547"></a>Failed to add a port for the ECS.</p>
</td>
</tr>
<tr id="row78954577584"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p131125513561"><a name="p131125513561"></a><a name="p131125513561"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p17311655195611"><a name="p17311655195611"></a><a name="p17311655195611"></a>111500023</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p173111855125615"><a name="p173111855125615"></a><a name="p173111855125615"></a>Internal service error.</p>
</td>
</tr>
<tr id="row48957574586"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1731195595615"><a name="p1731195595615"></a><a name="p1731195595615"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p9311205595612"><a name="p9311205595612"></a><a name="p9311205595612"></a>111500024</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p143111556564"><a name="p143111556564"></a><a name="p143111556564"></a>Internal service error.</p>
</td>
</tr>
<tr id="row118953579581"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p10312655185616"><a name="p10312655185616"></a><a name="p10312655185616"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p8312555185615"><a name="p8312555185615"></a><a name="p8312555185615"></a>111500025</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p113129552564"><a name="p113129552564"></a><a name="p113129552564"></a>Internal service error.</p>
</td>
</tr>
<tr id="row194740536530"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p14745534530"><a name="p14745534530"></a><a name="p14745534530"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p84742537531"><a name="p84742537531"></a><a name="p84742537531"></a>111500031</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p16474145315319"><a name="p16474145315319"></a><a name="p16474145315319"></a>Failed to create the DCS instance.</p>
</td>
</tr>
<tr id="row10348205334912"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p735095314499"><a name="p735095314499"></a><a name="p735095314499"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p113501953174914"><a name="p113501953174914"></a><a name="p113501953174914"></a>111500032</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p7350953194919"><a name="p7350953194919"></a><a name="p7350953194919"></a>Internal service error.</p>
</td>
</tr>
<tr id="row20166731912"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p20312135565616"><a name="p20312135565616"></a><a name="p20312135565616"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p103121155135611"><a name="p103121155135611"></a><a name="p103121155135611"></a>111500041</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p11312655115612"><a name="p11312655115612"></a><a name="p11312655115612"></a>No resource tenant available.</p>
</td>
</tr>
<tr id="row952973112535"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p15291831145311"><a name="p15291831145311"></a><a name="p15291831145311"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p17529113115530"><a name="p17529113115530"></a><a name="p17529113115530"></a>111500044</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p9529231145314"><a name="p9529231145314"></a><a name="p9529231145314"></a>Failed to update the status of the DCS instance.</p>
</td>
</tr>
<tr id="row459443616"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p631314554566"><a name="p631314554566"></a><a name="p631314554566"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p4313155205611"><a name="p4313155205611"></a><a name="p4313155205611"></a>111500051</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1631395555619"><a name="p1631395555619"></a><a name="p1631395555619"></a>Internal service error.</p>
</td>
</tr>
<tr id="row1611644314"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p103132551567"><a name="p103132551567"></a><a name="p103132551567"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p19313145519562"><a name="p19313145519562"></a><a name="p19313145519562"></a>111500052</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p8313105595615"><a name="p8313105595615"></a><a name="p8313105595615"></a>Internal service error.</p>
</td>
</tr>
<tr id="row960816412110"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1131315552565"><a name="p1131315552565"></a><a name="p1131315552565"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p12313955195617"><a name="p12313955195617"></a><a name="p12313955195617"></a>111500053</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p23145554564"><a name="p23145554564"></a><a name="p23145554564"></a>Internal service error.</p>
</td>
</tr>
<tr id="row12143651813"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p19314355115617"><a name="p19314355115617"></a><a name="p19314355115617"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p12314555155613"><a name="p12314555155613"></a><a name="p12314555155613"></a>111500054</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p173141855195611"><a name="p173141855195611"></a><a name="p173141855195611"></a>Internal service error.</p>
</td>
</tr>
<tr id="row15487114772010"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p63141558567"><a name="p63141558567"></a><a name="p63141558567"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1231485515615"><a name="p1231485515615"></a><a name="p1231485515615"></a>111500070</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p93151155115615"><a name="p93151155115615"></a><a name="p93151155115615"></a>Internal service error.</p>
</td>
</tr>
<tr id="row18284155382114"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p17316175519569"><a name="p17316175519569"></a><a name="p17316175519569"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p5316145510564"><a name="p5316145510564"></a><a name="p5316145510564"></a>111500071</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p33160551561"><a name="p33160551561"></a><a name="p33160551561"></a>Internal service error.</p>
</td>
</tr>
<tr id="row980012225568"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p88001622115615"><a name="p88001622115615"></a><a name="p88001622115615"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1780052265615"><a name="p1780052265615"></a><a name="p1780052265615"></a>111500077</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p191311481713"><a name="p191311481713"></a><a name="p191311481713"></a>Internal service error.</p>
</td>
</tr>
<tr id="row15126162516568"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p148871124155910"><a name="p148871124155910"></a><a name="p148871124155910"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p71271525105612"><a name="p71271525105612"></a><a name="p71271525105612"></a>111500078</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1792716482111"><a name="p1792716482111"></a><a name="p1792716482111"></a>Internal service error.</p>
</td>
</tr>
<tr id="row174811527185615"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1791542475917"><a name="p1791542475917"></a><a name="p1791542475917"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p74821327125610"><a name="p74821327125610"></a><a name="p74821327125610"></a>111500079</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p119392489115"><a name="p119392489115"></a><a name="p119392489115"></a>Internal service error.</p>
</td>
</tr>
<tr id="row9876172985617"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p16935424145912"><a name="p16935424145912"></a><a name="p16935424145912"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p138775291567"><a name="p138775291567"></a><a name="p138775291567"></a>111500081</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p6947948719"><a name="p6947948719"></a><a name="p6947948719"></a>Internal service error.</p>
</td>
</tr>
<tr id="row1140513217568"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1095402411593"><a name="p1095402411593"></a><a name="p1095402411593"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p194057321565"><a name="p194057321565"></a><a name="p194057321565"></a>111500082</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p69621481112"><a name="p69621481112"></a><a name="p69621481112"></a>Internal service error.</p>
</td>
</tr>
<tr id="row1412016351564"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p097011245593"><a name="p097011245593"></a><a name="p097011245593"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p012073514567"><a name="p012073514567"></a><a name="p012073514567"></a>111500083</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p197110482019"><a name="p197110482019"></a><a name="p197110482019"></a>Internal service error.</p>
</td>
</tr>
<tr id="row9809113719564"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p109941124105914"><a name="p109941124105914"></a><a name="p109941124105914"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p128096375568"><a name="p128096375568"></a><a name="p128096375568"></a>111500084</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p15980184815112"><a name="p15980184815112"></a><a name="p15980184815112"></a>Internal service error.</p>
</td>
</tr>
<tr id="row20497124010566"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p99152515918"><a name="p99152515918"></a><a name="p99152515918"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p54973408567"><a name="p54973408567"></a><a name="p54973408567"></a>111500085</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p098894813113"><a name="p098894813113"></a><a name="p098894813113"></a>Internal service error.</p>
</td>
</tr>
<tr id="row1136710439569"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p930325195916"><a name="p930325195916"></a><a name="p930325195916"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p103687437566"><a name="p103687437566"></a><a name="p103687437566"></a>111500088</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p49963481618"><a name="p49963481618"></a><a name="p49963481618"></a>Internal service error.</p>
</td>
</tr>
<tr id="row4298546175618"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p13451625135917"><a name="p13451625135917"></a><a name="p13451625135917"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p229994612567"><a name="p229994612567"></a><a name="p229994612567"></a>111500089</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1679497111"><a name="p1679497111"></a><a name="p1679497111"></a>Internal service error.</p>
</td>
</tr>
<tr id="row851716491566"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p18612253593"><a name="p18612253593"></a><a name="p18612253593"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p105171849145616"><a name="p105171849145616"></a><a name="p105171849145616"></a>111500090</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p8171491311"><a name="p8171491311"></a><a name="p8171491311"></a>Internal service error.</p>
</td>
</tr>
<tr id="row6939154825718"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p279132517596"><a name="p279132517596"></a><a name="p279132517596"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p69391948115715"><a name="p69391948115715"></a><a name="p69391948115715"></a>111500091</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p11261549614"><a name="p11261549614"></a><a name="p11261549614"></a>Internal service error.</p>
</td>
</tr>
<tr id="row185727535579"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1393112517596"><a name="p1393112517596"></a><a name="p1393112517596"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p7572185325718"><a name="p7572185325718"></a><a name="p7572185325718"></a>111500092</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p15354495117"><a name="p15354495117"></a><a name="p15354495117"></a>Internal service error.</p>
</td>
</tr>
<tr id="row159318562579"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p14109112516592"><a name="p14109112516592"></a><a name="p14109112516592"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p159485620574"><a name="p159485620574"></a><a name="p159485620574"></a>111500093</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p4531449716"><a name="p4531449716"></a><a name="p4531449716"></a>Internal service error.</p>
</td>
</tr>
<tr id="row8285520263"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p731695512560"><a name="p731695512560"></a><a name="p731695512560"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1431610552563"><a name="p1431610552563"></a><a name="p1431610552563"></a>111500094</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p203161556565"><a name="p203161556565"></a><a name="p203161556565"></a>Internal service error.</p>
</td>
</tr>
<tr id="row98671314584"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p208673385819"><a name="p208673385819"></a><a name="p208673385819"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1786814318580"><a name="p1786814318580"></a><a name="p1786814318580"></a>111500095</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1486818317582"><a name="p1486818317582"></a><a name="p1486818317582"></a>Internal service error.</p>
</td>
</tr>
<tr id="row11994144920210"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1994204911217"><a name="p1994204911217"></a><a name="p1994204911217"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p1199417491122"><a name="p1199417491122"></a><a name="p1199417491122"></a>111500104</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1899418494217"><a name="p1899418494217"></a><a name="p1899418494217"></a>Internal service error.</p>
</td>
</tr>
<tr id="row1021316391584"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p431675525613"><a name="p431675525613"></a><a name="p431675525613"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p14316155535614"><a name="p14316155535614"></a><a name="p14316155535614"></a>111500106</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1331711557562"><a name="p1331711557562"></a><a name="p1331711557562"></a>Internal service error.</p>
</td>
</tr>
<tr id="row121813321828"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p6182193214212"><a name="p6182193214212"></a><a name="p6182193214212"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p19182123218218"><a name="p19182123218218"></a><a name="p19182123218218"></a>111500801</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p2018218321221"><a name="p2018218321221"></a><a name="p2018218321221"></a>Internal service error.</p>
</td>
</tr>
<tr id="row134595653515"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p3346155616353"><a name="p3346155616353"></a><a name="p3346155616353"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p17347956143511"><a name="p17347956143511"></a><a name="p17347956143511"></a>111500802</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p43471656113511"><a name="p43471656113511"></a><a name="p43471656113511"></a>Internal service error.</p>
</td>
</tr>
<tr id="row4660133310320"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p866020330315"><a name="p866020330315"></a><a name="p866020330315"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p96601331637"><a name="p96601331637"></a><a name="p96601331637"></a>111500810</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p7660433831"><a name="p7660433831"></a><a name="p7660433831"></a>Internal service error.</p>
</td>
</tr>
<tr id="row0349184214312"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p1734911428319"><a name="p1734911428319"></a><a name="p1734911428319"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p3349124212316"><a name="p3349124212316"></a><a name="p3349124212316"></a>111500814</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p3349542135"><a name="p3349542135"></a><a name="p3349542135"></a>Internal service error.</p>
</td>
</tr>
<tr id="row289241516227"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p13765112917223"><a name="p13765112917223"></a><a name="p13765112917223"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p2770129202214"><a name="p2770129202214"></a><a name="p2770129202214"></a>111500815</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p197751929112216"><a name="p197751929112216"></a><a name="p197751929112216"></a>Internal service error.</p>
</td>
</tr>
<tr id="row538010511139"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p438095113316"><a name="p438095113316"></a><a name="p438095113316"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p17380165116319"><a name="p17380165116319"></a><a name="p17380165116319"></a>111500816</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p5380451137"><a name="p5380451137"></a><a name="p5380451137"></a>Internal service error.</p>
</td>
</tr>
<tr id="row658419615420"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.4.1.1 "><p id="p9584869419"><a name="p9584869419"></a><a name="p9584869419"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="p2584116841"><a name="p2584116841"></a><a name="p2584116841"></a>111500820</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p165844612412"><a name="p165844612412"></a><a name="p165844612412"></a>Internal service error.</p>
</td>
</tr>
</tbody>
</table>

