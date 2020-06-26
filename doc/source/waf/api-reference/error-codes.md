# Error Codes<a name="EN-US_TOPIC_0193630654"></a>

## Function Description<a name="section59067588"></a>

A customized message is returned when errors, such as 400 or 500, occur in an extended public cloud API. This section describes the meaning of each error code.

## Response Format<a name="section171114175308"></a>

-   HTTP status code

    ```
    400
    ```

-   Response body example

    ```
    {
    "error_code": "11000000",
    "error_msg": "hx error."
    }
    ```


## Error Code Description<a name="section220145853014"></a>

<a name="table10546806"></a>
<table><thead align="left"><tr id="row6204869"><th class="cellrowborder" valign="top" width="33.77%" id="mcps1.1.3.1.1"><p id="p42178345"><a name="p42178345"></a><a name="p42178345"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="66.23%" id="mcps1.1.3.1.2"><p id="p61002824"><a name="p61002824"></a><a name="p61002824"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row42281744"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p164949490128"><a name="p164949490128"></a><a name="p164949490128"></a>WAF.1001</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p166413761313"><a name="p166413761313"></a><a name="p166413761313"></a>Invalid request</p>
</td>
</tr>
<tr id="row46127541"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p19494749181216"><a name="p19494749181216"></a><a name="p19494749181216"></a>WAF.1002</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p665103713135"><a name="p665103713135"></a><a name="p665103713135"></a>Invalid page number or page size</p>
</td>
</tr>
<tr id="row37744207"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p84941949131214"><a name="p84941949131214"></a><a name="p84941949131214"></a>WAF.1003</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p56513781320"><a name="p56513781320"></a><a name="p56513781320"></a>Invalid ID</p>
</td>
</tr>
<tr id="row5210793"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p1549474981216"><a name="p1549474981216"></a><a name="p1549474981216"></a>WAF.1004</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p1651637121319"><a name="p1651637121319"></a><a name="p1651637121319"></a>Invalid name</p>
</td>
</tr>
<tr id="row65138754"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p154941749191211"><a name="p154941749191211"></a><a name="p154941749191211"></a>WAF.1005</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p4616841366"><a name="p4616841366"></a><a name="p4616841366"></a>Invalid path</p>
</td>
</tr>
<tr id="row523123621116"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p16240361117"><a name="p16240361117"></a><a name="p16240361117"></a>WAF.1006</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p102418368112"><a name="p102418368112"></a><a name="p102418368112"></a>Invalid rate limiting mode</p>
</td>
</tr>
<tr id="row9219164541315"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p7219174518135"><a name="p7219174518135"></a><a name="p7219174518135"></a>WAF.1007</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p15219154518133"><a name="p15219154518133"></a><a name="p15219154518133"></a>Invalid user identifier</p>
</td>
</tr>
<tr id="row2898057141419"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p1189835721419"><a name="p1189835721419"></a><a name="p1189835721419"></a>WAF.1008</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p11898357141410"><a name="p11898357141410"></a><a name="p11898357141410"></a>Invalid protective action</p>
</td>
</tr>
<tr id="row1331122611168"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p4311112691610"><a name="p4311112691610"></a><a name="p4311112691610"></a>WAF.1009</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p03111526191610"><a name="p03111526191610"></a><a name="p03111526191610"></a>Invalid CC attack protection rule</p>
</td>
</tr>
<tr id="row450505720168"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p1150516571164"><a name="p1150516571164"></a><a name="p1150516571164"></a>WAF.1012</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p15053579166"><a name="p15053579166"></a><a name="p15053579166"></a>Invalid Referer</p>
</td>
</tr>
<tr id="row14566944201"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p165669415206"><a name="p165669415206"></a><a name="p165669415206"></a>WAF.1013</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p962414345205"><a name="p962414345205"></a><a name="p962414345205"></a>Invalid type</p>
</td>
</tr>
<tr id="row18489618192113"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p20489191872114"><a name="p20489191872114"></a><a name="p20489191872114"></a>WAF.1014</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p8489181852117"><a name="p8489181852117"></a><a name="p8489181852117"></a>Invalid logic</p>
</td>
</tr>
<tr id="row20407759112111"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p929491120222"><a name="p929491120222"></a><a name="p929491120222"></a>WAF.1015</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p1482912113220"><a name="p1482912113220"></a><a name="p1482912113220"></a>Invalid subfield</p>
</td>
</tr>
<tr id="row109701387220"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p20970168132214"><a name="p20970168132214"></a><a name="p20970168132214"></a>WAF.1016</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p1097018822212"><a name="p1097018822212"></a><a name="p1097018822212"></a>Invalid content</p>
</td>
</tr>
<tr id="row158173517229"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p18817165172214"><a name="p18817165172214"></a><a name="p18817165172214"></a>WAF.1018</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p15817054222"><a name="p15817054222"></a><a name="p15817054222"></a>Invalid precise protection rule</p>
</td>
</tr>
<tr id="row61377352212"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p1213720342218"><a name="p1213720342218"></a><a name="p1213720342218"></a>WAF.1019</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p1013717312228"><a name="p1013717312228"></a><a name="p1013717312228"></a>Invalid data masking rule</p>
</td>
</tr>
<tr id="row146218512253"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p362113516256"><a name="p362113516256"></a><a name="p362113516256"></a>WAF.1020</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p36211457251"><a name="p36211457251"></a><a name="p36211457251"></a>Invalid User-Agent</p>
</td>
</tr>
<tr id="row1970461382512"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p2704111372511"><a name="p2704111372511"></a><a name="p2704111372511"></a>WAF.1021</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p37042013202520"><a name="p37042013202520"></a><a name="p37042013202520"></a>Invalid IP address</p>
</td>
</tr>
<tr id="row1840181112250"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p1440171172516"><a name="p1440171172516"></a><a name="p1440171172516"></a>WAF.1022</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p440171192513"><a name="p440171192513"></a><a name="p440171192513"></a>Invalid false alarm masking rule</p>
</td>
</tr>
<tr id="row4434118192515"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p124341892516"><a name="p124341892516"></a><a name="p124341892516"></a>WAF.1023</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p124347811252"><a name="p124347811252"></a><a name="p124347811252"></a>Invalid number</p>
</td>
</tr>
<tr id="row11860151918278"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p386012198273"><a name="p386012198273"></a><a name="p386012198273"></a>WAF.1025</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p18860519192712"><a name="p18860519192712"></a><a name="p18860519192712"></a>Invalid time</p>
</td>
</tr>
<tr id="row4343429142713"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p334316291279"><a name="p334316291279"></a><a name="p334316291279"></a>WAF.1029</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p18343202915274"><a name="p18343202915274"></a><a name="p18343202915274"></a>Invalid protection level</p>
</td>
</tr>
<tr id="row1462202642711"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p19621826152711"><a name="p19621826152711"></a><a name="p19621826152711"></a>WAF.1030</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p1362132662717"><a name="p1362132662717"></a><a name="p1362132662717"></a>Invalid priority</p>
</td>
</tr>
<tr id="row85881722162711"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p097819370293"><a name="p097819370293"></a><a name="p097819370293"></a>WAF.1031</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p3588152292716"><a name="p3588152292716"></a><a name="p3588152292716"></a>Invalid attack type</p>
</td>
</tr>
<tr id="row33790110"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p1849418491124"><a name="p1849418491124"></a><a name="p1849418491124"></a>WAF.1600</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p665133718135"><a name="p665133718135"></a><a name="p665133718135"></a>Invalid domain name</p>
</td>
</tr>
<tr id="row58612362"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p20494184921211"><a name="p20494184921211"></a><a name="p20494184921211"></a>WAF.1601</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p965193751315"><a name="p965193751315"></a><a name="p965193751315"></a>Invalid protocol</p>
</td>
</tr>
<tr id="row63076700"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p19494164931210"><a name="p19494164931210"></a><a name="p19494164931210"></a>WAF.1602</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p106563711135"><a name="p106563711135"></a><a name="p106563711135"></a>Invalid server address</p>
</td>
</tr>
<tr id="row6997551"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p1849414491123"><a name="p1849414491123"></a><a name="p1849414491123"></a>WAF.1603</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p126820375132"><a name="p126820375132"></a><a name="p126820375132"></a>Invalid port</p>
</td>
</tr>
<tr id="row9132841"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p1649434921211"><a name="p1649434921211"></a><a name="p1649434921211"></a>WAF.1604</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p06812374138"><a name="p06812374138"></a><a name="p06812374138"></a>Invalid protection status or connection status</p>
</td>
</tr>
<tr id="row65452216"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p18494134941216"><a name="p18494134941216"></a><a name="p18494134941216"></a>WAF.1605</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p36813771317"><a name="p36813771317"></a><a name="p36813771317"></a>Invalid certificate content format</p>
</td>
</tr>
<tr id="row21337296"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p16494134911216"><a name="p16494134911216"></a><a name="p16494134911216"></a>WAF.1606</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p77010374133"><a name="p77010374133"></a><a name="p77010374133"></a>Invalid private key format</p>
</td>
</tr>
<tr id="row846795123417"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p662112153345"><a name="p662112153345"></a><a name="p662112153345"></a>WAF.2001</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p174676513418"><a name="p174676513418"></a><a name="p174676513418"></a>IDs do not match.</p>
</td>
</tr>
<tr id="row11518161311343"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p5518181311345"><a name="p5518181311345"></a><a name="p5518181311345"></a>WAF.2002</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p1865592711352"><a name="p1865592711352"></a><a name="p1865592711352"></a>The protective action cannot be set to block.</p>
</td>
</tr>
<tr id="row2321311183415"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p932411153414"><a name="p932411153414"></a><a name="p932411153414"></a>WAF.2004</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p19321311153417"><a name="p19321311153417"></a><a name="p19321311153417"></a>The user identifier is unavailable in a CC attack protection rule.</p>
</td>
</tr>
<tr id="row182612793417"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p10826107153419"><a name="p10826107153419"></a><a name="p10826107153419"></a>WAF.2005</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p7716161119402"><a name="p7716161119402"></a><a name="p7716161119402"></a>The condition list in the precise protection rule is empty.</p>
</td>
</tr>
<tr id="row82212919409"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p82953194114"><a name="p82953194114"></a><a name="p82953194114"></a>WAF.2006</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p1423911624115"><a name="p1423911624115"></a><a name="p1423911624115"></a>Subfields cannot be set for conditions in the precise protection rule.</p>
</td>
</tr>
<tr id="row11269134134010"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p10764114428"><a name="p10764114428"></a><a name="p10764114428"></a>WAF.2007</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p16269133474011"><a name="p16269133474011"></a><a name="p16269133474011"></a>The precise protection rule contains duplicate conditions.</p>
</td>
</tr>
<tr id="row197406311404"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p2627105454215"><a name="p2627105454215"></a><a name="p2627105454215"></a>WAF.2008</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p580152114434"><a name="p580152114434"></a><a name="p580152114434"></a>Wildcard domains are not supported.</p>
</td>
</tr>
<tr id="row44182573"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p144941649181216"><a name="p144941649181216"></a><a name="p144941649181216"></a>WAF.3001</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p117073717139"><a name="p117073717139"></a><a name="p117073717139"></a>The requested resource was not found.</p>
</td>
</tr>
<tr id="row12608918"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p114941149131217"><a name="p114941149131217"></a><a name="p114941149131217"></a>WAF.3002</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p1870437161316"><a name="p1870437161316"></a><a name="p1870437161316"></a>The number of resources exceeds the maximum limit allowed.</p>
</td>
</tr>
<tr id="row38311703"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p74941049181216"><a name="p74941049181216"></a><a name="p74941049181216"></a>WAF.3003</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p97093718132"><a name="p97093718132"></a><a name="p97093718132"></a>The resource is in use.</p>
</td>
</tr>
<tr id="row27999558"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p7494184961216"><a name="p7494184961216"></a><a name="p7494184961216"></a>WAF.3004</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p1270163751310"><a name="p1270163751310"></a><a name="p1270163751310"></a>The system is busy.</p>
</td>
</tr>
<tr id="row45931522"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p1549418499122"><a name="p1549418499122"></a><a name="p1549418499122"></a>WAF.3005</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p17018374131"><a name="p17018374131"></a><a name="p17018374131"></a>The domain name already exists.</p>
</td>
</tr>
<tr id="row5754878"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p749464912122"><a name="p749464912122"></a><a name="p749464912122"></a>WAF.3006</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p370237141319"><a name="p370237141319"></a><a name="p370237141319"></a>The rule name already exists.</p>
</td>
</tr>
<tr id="row47645920"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p1149484920123"><a name="p1149484920123"></a><a name="p1149484920123"></a>WAF.3007</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p2070123712139"><a name="p2070123712139"></a><a name="p2070123712139"></a>Rules conflict with each other.</p>
</td>
</tr>
<tr id="row39047789"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p1349404921216"><a name="p1349404921216"></a><a name="p1349404921216"></a>WAF.3008</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p157093713139"><a name="p157093713139"></a><a name="p157093713139"></a>The rule already exists.</p>
</td>
</tr>
<tr id="row18572019194418"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p1285711192440"><a name="p1285711192440"></a><a name="p1285711192440"></a>WAF.3010</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p33191351184514"><a name="p33191351184514"></a><a name="p33191351184514"></a>The policy has been bound to the domain name.</p>
</td>
</tr>
<tr id="row810113624718"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p121012610473"><a name="p121012610473"></a><a name="p121012610473"></a>WAF.4000</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p310112619477"><a name="p310112619477"></a><a name="p310112619477"></a>The API cannot be found.</p>
</td>
</tr>
<tr id="row1157172474719"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p1815762434717"><a name="p1815762434717"></a><a name="p1815762434717"></a>WAF.4001</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p18658422473"><a name="p18658422473"></a><a name="p18658422473"></a>The method is not allowed.</p>
</td>
</tr>
<tr id="row61902708"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p54941149181214"><a name="p54941149181214"></a><a name="p54941149181214"></a>WAF.5000</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p1570193718133"><a name="p1570193718133"></a><a name="p1570193718133"></a>Internal error</p>
</td>
</tr>
<tr id="row81075834818"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p3107888486"><a name="p3107888486"></a><a name="p3107888486"></a>WAF.5001</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p134191018164811"><a name="p134191018164811"></a><a name="p134191018164811"></a>Failed to access data.</p>
</td>
</tr>
<tr id="row1859113244816"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p168611232164816"><a name="p168611232164816"></a><a name="p168611232164816"></a>WAF.5002</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p18861193254815"><a name="p18861193254815"></a><a name="p18861193254815"></a>HTTP request failed.</p>
</td>
</tr>
<tr id="row0957105111483"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p5957115115482"><a name="p5957115115482"></a><a name="p5957115115482"></a>WAF.5003</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p1195765174810"><a name="p1195765174810"></a><a name="p1195765174810"></a>Elasticsearch request failed.</p>
</td>
</tr>
<tr id="row1859944114916"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p148596440498"><a name="p148596440498"></a><a name="p148596440498"></a>WAF.6000</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p2085934414919"><a name="p2085934414919"></a><a name="p2085934414919"></a>Connection failed.</p>
</td>
</tr>
<tr id="row79351412145018"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p89357122504"><a name="p89357122504"></a><a name="p89357122504"></a>WAF.6001</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p1593541225010"><a name="p1593541225010"></a><a name="p1593541225010"></a>The request is not permitted.</p>
</td>
</tr>
<tr id="row8821191875010"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p982101825010"><a name="p982101825010"></a><a name="p982101825010"></a>WAF.6002</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p98211718205010"><a name="p98211718205010"></a><a name="p98211718205010"></a>Failed to read obtained data.</p>
</td>
</tr>
<tr id="row2010715295211"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p41071422529"><a name="p41071422529"></a><a name="p41071422529"></a>WAF.6003</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p810742175215"><a name="p810742175215"></a><a name="p810742175215"></a>Failed to export data.</p>
</td>
</tr>
<tr id="row05621315195014"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p956220151501"><a name="p956220151501"></a><a name="p956220151501"></a>WAF.6004</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p145622015175018"><a name="p145622015175018"></a><a name="p145622015175018"></a>Failed to import data.</p>
</td>
</tr>
<tr id="row37051858195218"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p1370518581527"><a name="p1370518581527"></a><a name="p1370518581527"></a>WAF.7001</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p1470665817525"><a name="p1470665817525"></a><a name="p1470665817525"></a>The data exceeds the valid length.</p>
</td>
</tr>
<tr id="row146256456531"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p56251245105316"><a name="p56251245105316"></a><a name="p56251245105316"></a>WAF.9001</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p2062519459534"><a name="p2062519459534"></a><a name="p2062519459534"></a>IAM authentication failed.</p>
</td>
</tr>
<tr id="row8554114915533"><td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.1.3.1.1 "><p id="p8554184916534"><a name="p8554184916534"></a><a name="p8554184916534"></a>WAF.9002</p>
</td>
<td class="cellrowborder" valign="top" width="66.23%" headers="mcps1.1.3.1.2 "><p id="p2554549175317"><a name="p2554549175317"></a><a name="p2554549175317"></a>No permission</p>
</td>
</tr>
</tbody>
</table>

