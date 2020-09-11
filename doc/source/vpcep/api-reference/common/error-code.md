# Error Code<a name="vpcep_08_0002"></a>

## Function<a name="section6144247617754"></a>

If an error occurs during API calling, a customized error message will be returned. This section describes the meaning of each status code returned by VPCEP.

## Error Code Structure Format<a name="section2995295617754"></a>

```
STATUS CODE 400
```

```
{
        "error_code": "EndPoint.0002",
        "error_msg": "Parameter error."
}
```

## Error Code Description<a name="section484824318239"></a>

>![](/images/icon-note.gif) **NOTE:** 
>An error code returned by an API does not correspond to an error message.

**Table  1**  Error code description

<a name="table198011511195617"></a>
<table><thead align="left"><tr id="row98010111569"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.7.1.1"><p id="p118011911135620"><a name="p118011911135620"></a><a name="p118011911135620"></a><strong id="b13975433699"><a name="b13975433699"></a><a name="b13975433699"></a>Category</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.7.1.2"><p id="p5801121110567"><a name="p5801121110567"></a><a name="p5801121110567"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.7.1.3"><p id="p1080111155617"><a name="p1080111155617"></a><a name="p1080111155617"></a><strong id="b10145115411590"><a name="b10145115411590"></a><a name="b10145115411590"></a>HTTP Response Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="22%" id="mcps1.2.7.1.4"><p id="p780121111563"><a name="p780121111563"></a><a name="p780121111563"></a><strong id="b558101618108"><a name="b558101618108"></a><a name="b558101618108"></a>Error Message</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.7.1.5"><p id="p1180191117568"><a name="p1180191117568"></a><a name="p1180191117568"></a><strong id="b174781731112211"><a name="b174781731112211"></a><a name="b174781731112211"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.7.1.6"><p id="p78018116565"><a name="p78018116565"></a><a name="p78018116565"></a><strong id="b1372035911104"><a name="b1372035911104"></a><a name="b1372035911104"></a>Solution</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row9801131185620"><td class="cellrowborder" rowspan="22" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p1680191119567"><a name="p1680191119567"></a><a name="p1680191119567"></a>SYSTEM ERROR: 0xxx</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.7.1.2 "><p id="p4801131115615"><a name="p4801131115615"></a><a name="p4801131115615"></a>EndPoint.0001</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.3 "><p id="p080121125615"><a name="p080121125615"></a><a name="p080121125615"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.4 "><p id="p128011611115617"><a name="p128011611115617"></a><a name="p128011611115617"></a>System error. Please retry.</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p15802611195616"><a name="p15802611195616"></a><a name="p15802611195616"></a>System error. Please retry.</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.7.1.6 "><p id="p380214111567"><a name="p380214111567"></a><a name="p380214111567"></a>Try again. If the fault persists, contact customer service.</p>
</td>
</tr>
<tr id="row280251195613"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1880211110568"><a name="p1880211110568"></a><a name="p1880211110568"></a>EndPoint.0002</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p88021811115613"><a name="p88021811115613"></a><a name="p88021811115613"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p128021211195615"><a name="p128021211195615"></a><a name="p128021211195615"></a>Parameter error.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p780251113562"><a name="p780251113562"></a><a name="p780251113562"></a>Parameter error.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p28021113566"><a name="p28021113566"></a><a name="p28021113566"></a>Check whether the parameter is correct.</p>
</td>
</tr>
<tr id="row1380251119568"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p178021211105611"><a name="p178021211105611"></a><a name="p178021211105611"></a>EndPoint.0003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p480211105619"><a name="p480211105619"></a><a name="p480211105619"></a>401</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1802911155616"><a name="p1802911155616"></a><a name="p1802911155616"></a>Authentication failed or authentication information is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p10802101165616"><a name="p10802101165616"></a><a name="p10802101165616"></a>Authentication failed or authentication information is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1802101112564"><a name="p1802101112564"></a><a name="p1802101112564"></a>Check whether the permission is enabled.</p>
</td>
</tr>
<tr id="row1180251185613"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1880211115612"><a name="p1880211115612"></a><a name="p1880211115612"></a>EndPoint.0004</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p2802181111561"><a name="p2802181111561"></a><a name="p2802181111561"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p158020112566"><a name="p158020112566"></a><a name="p158020112566"></a>Authentication information is incorrect or you have no permissions.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1680281115618"><a name="p1680281115618"></a><a name="p1680281115618"></a>Authentication information is incorrect or you have no permissions.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p17802611165619"><a name="p17802611165619"></a><a name="p17802611165619"></a>Check whether the permission is enabled.</p>
</td>
</tr>
<tr id="row380217119560"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p128024117569"><a name="p128024117569"></a><a name="p128024117569"></a>EndPoint.0005</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p3802161145619"><a name="p3802161145619"></a><a name="p3802161145619"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p118021011145619"><a name="p118021011145619"></a><a name="p118021011145619"></a>The requested resource does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p14802101195611"><a name="p14802101195611"></a><a name="p14802101195611"></a>The requested resource is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p19802311185613"><a name="p19802311185613"></a><a name="p19802311185613"></a>Check whether input parameters are correct.</p>
</td>
</tr>
<tr id="row8802811175617"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p58021811205613"><a name="p58021811205613"></a><a name="p58021811205613"></a>EndPoint.0006</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p4802171112567"><a name="p4802171112567"></a><a name="p4802171112567"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p2080201145618"><a name="p2080201145618"></a><a name="p2080201145618"></a>Invalid limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p180321117568"><a name="p180321117568"></a><a name="p180321117568"></a>Invalid limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p188038115565"><a name="p188038115565"></a><a name="p188038115565"></a>Enter a correct limit.</p>
</td>
</tr>
<tr id="row188034111568"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p680318113565"><a name="p680318113565"></a><a name="p680318113565"></a>EndPoint.0007</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p080341111564"><a name="p080341111564"></a><a name="p080341111564"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p15803511195619"><a name="p15803511195619"></a><a name="p15803511195619"></a>Invalid action.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p08031411155615"><a name="p08031411155615"></a><a name="p08031411155615"></a>Invalid action.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p118031711145615"><a name="p118031711145615"></a><a name="p118031711145615"></a>Enter a correct action.</p>
</td>
</tr>
<tr id="row17803101155612"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p58031211145613"><a name="p58031211145613"></a><a name="p58031211145613"></a>EndPoint.0009</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p28035113564"><a name="p28035113564"></a><a name="p28035113564"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p880431105619"><a name="p880431105619"></a><a name="p880431105619"></a>The remote address does not match.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p128047116563"><a name="p128047116563"></a><a name="p128047116563"></a>The remote address does not match.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1280491114566"><a name="p1280491114566"></a><a name="p1280491114566"></a>Check whether you have the access permission.</p>
</td>
</tr>
<tr id="row38041611105610"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p88042011185612"><a name="p88042011185612"></a><a name="p88042011185612"></a>EndPoint.0010</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p78046117568"><a name="p78046117568"></a><a name="p78046117568"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p4804311105614"><a name="p4804311105614"></a><a name="p4804311105614"></a>Invalid offset.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1880471112564"><a name="p1880471112564"></a><a name="p1880471112564"></a>Invalid offset.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p17804211175614"><a name="p17804211175614"></a><a name="p17804211175614"></a>Enter a correct offset.</p>
</td>
</tr>
<tr id="row48041811155613"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p2804311175610"><a name="p2804311175610"></a><a name="p2804311175610"></a>EndPoint.0011</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1880441145610"><a name="p1880441145610"></a><a name="p1880441145610"></a>504</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p380417112569"><a name="p380417112569"></a><a name="p380417112569"></a>The request body is null.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p15804111111562"><a name="p15804111111562"></a><a name="p15804111111562"></a>The request body is null.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p080551114563"><a name="p080551114563"></a><a name="p080551114563"></a>Enter the request body again.</p>
</td>
</tr>
<tr id="row580531175618"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p19805111105615"><a name="p19805111105615"></a><a name="p19805111105615"></a>EndPoint.0012</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p158056113568"><a name="p158056113568"></a><a name="p158056113568"></a>504</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p780513118567"><a name="p780513118567"></a><a name="p780513118567"></a>The request header is null.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p08051611155620"><a name="p08051611155620"></a><a name="p08051611155620"></a>The request header is null.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1380513116565"><a name="p1380513116565"></a><a name="p1380513116565"></a>Enter a request header.</p>
</td>
</tr>
<tr id="row480516119567"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p3805171185618"><a name="p3805171185618"></a><a name="p3805171185618"></a>EndPoint.0013</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p48051711145619"><a name="p48051711145619"></a><a name="p48051711145619"></a>504</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p780551114561"><a name="p780551114561"></a><a name="p780551114561"></a>The request timed out.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p8805411195612"><a name="p8805411195612"></a><a name="p8805411195612"></a>The request timed out.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p7805161110563"><a name="p7805161110563"></a><a name="p7805161110563"></a>Contact customer service if the problem persists after a retry.</p>
</td>
</tr>
<tr id="row10805911195619"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1980510111568"><a name="p1980510111568"></a><a name="p1980510111568"></a>EndPoint.0014</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p48066118560"><a name="p48066118560"></a><a name="p48066118560"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1480621125615"><a name="p1480621125615"></a><a name="p1480621125615"></a>Invalid project ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p5806181113562"><a name="p5806181113562"></a><a name="p5806181113562"></a>Invalid project ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p580610114564"><a name="p580610114564"></a><a name="p580610114564"></a>Enter a correct project ID.</p>
</td>
</tr>
<tr id="row8806171175620"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p10806151105611"><a name="p10806151105611"></a><a name="p10806151105611"></a>EndPoint.0015</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1980618114566"><a name="p1980618114566"></a><a name="p1980618114566"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p88068114568"><a name="p88068114568"></a><a name="p88068114568"></a>Invalid specification.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p12806101165616"><a name="p12806101165616"></a><a name="p12806101165616"></a>Invalid specification.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p980610115567"><a name="p980610115567"></a><a name="p980610115567"></a>Enter a correct specification.</p>
</td>
</tr>
<tr id="row1780661195610"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1806151116562"><a name="p1806151116562"></a><a name="p1806151116562"></a>EndPoint.0016</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p2806311165615"><a name="p2806311165615"></a><a name="p2806311165615"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p19806111145610"><a name="p19806111145610"></a><a name="p19806111145610"></a>The number of batch operated resources exceeded the limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1080611119566"><a name="p1080611119566"></a><a name="p1080611119566"></a>The number of batch operated resources exceeded the limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p68061011135617"><a name="p68061011135617"></a><a name="p68061011135617"></a>Reduce the number of resources to be batch operated.</p>
</td>
</tr>
<tr id="row14806611145613"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p180731125615"><a name="p180731125615"></a><a name="p180731125615"></a>EndPoint.0017</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p98071311195619"><a name="p98071311195619"></a><a name="p98071311195619"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p08071115562"><a name="p08071115562"></a><a name="p08071115562"></a>Invalid sort_key.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p19807181105619"><a name="p19807181105619"></a><a name="p19807181105619"></a>Invalid sort key.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p9807171111565"><a name="p9807171111565"></a><a name="p9807171111565"></a>Enter a correct sort key.</p>
</td>
</tr>
<tr id="row178071711175612"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p08071011175617"><a name="p08071011175617"></a><a name="p08071011175617"></a>EndPoint.0018</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p380718115569"><a name="p380718115569"></a><a name="p380718115569"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p20807111155610"><a name="p20807111155610"></a><a name="p20807111155610"></a>Invalid sort_dir.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p78071311115617"><a name="p78071311115617"></a><a name="p78071311115617"></a>Invalid sort DIR. </p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p15807181145610"><a name="p15807181145610"></a><a name="p15807181145610"></a>Enter a correct sort DIR.</p>
</td>
</tr>
<tr id="row68078115568"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p8807131125615"><a name="p8807131125615"></a><a name="p8807131125615"></a>EndPoint.0019</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p380771117567"><a name="p380771117567"></a><a name="p380771117567"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1280710115563"><a name="p1280710115563"></a><a name="p1280710115563"></a>Invalid status.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p180714116568"><a name="p180714116568"></a><a name="p180714116568"></a>Invalid status.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p480741195613"><a name="p480741195613"></a><a name="p480741195613"></a>Enter a correct status.</p>
</td>
</tr>
<tr id="row1980716119563"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p19807191117564"><a name="p19807191117564"></a><a name="p19807191117564"></a>EndPoint.0020</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p198071911155610"><a name="p198071911155610"></a><a name="p198071911155610"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p10807211185616"><a name="p10807211185616"></a><a name="p10807211185616"></a>Invalid VPC ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p98081011145617"><a name="p98081011145617"></a><a name="p98081011145617"></a>Invalid VPC ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p68081011135610"><a name="p68081011135610"></a><a name="p68081011135610"></a>Enter a correct VPC ID.</p>
</td>
</tr>
<tr id="row1280813116569"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p98084117562"><a name="p98084117562"></a><a name="p98084117562"></a>EndPoint.0021</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p13808411175618"><a name="p13808411175618"></a><a name="p13808411175618"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p17808121195611"><a name="p17808121195611"></a><a name="p17808121195611"></a>Invalid marker_id.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p880841145619"><a name="p880841145619"></a><a name="p880841145619"></a>Invalid marker ID. </p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p280851118560"><a name="p280851118560"></a><a name="p280851118560"></a>Enter a correct marker ID. </p>
</td>
</tr>
<tr id="row158085111560"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p158081811145618"><a name="p158081811145618"></a><a name="p158081811145618"></a>EndPoint.0022</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p880812116564"><a name="p880812116564"></a><a name="p880812116564"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p108081411195615"><a name="p108081411195615"></a><a name="p108081411195615"></a>The number of requests exceeded the limit. Please try later.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p118081111145611"><a name="p118081111145611"></a><a name="p118081111145611"></a>The number of requests exceeded the limit. Please try later.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p20808121114567"><a name="p20808121114567"></a><a name="p20808121114567"></a>Try again later.</p>
</td>
</tr>
<tr id="row19808111118568"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p88083118567"><a name="p88083118567"></a><a name="p88083118567"></a>EndPoint.0023</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p2808161175617"><a name="p2808161175617"></a><a name="p2808161175617"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p10809911165618"><a name="p10809911165618"></a><a name="p10809911165618"></a>Invalid subnet_id.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1780941155620"><a name="p1780941155620"></a><a name="p1780941155620"></a>Invalid subnet ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1809141112569"><a name="p1809141112569"></a><a name="p1809141112569"></a>Enter a correct subnet ID.</p>
</td>
</tr>
<tr id="row1580916112565"><td class="cellrowborder" rowspan="5" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p10809191105618"><a name="p10809191105618"></a><a name="p10809191105618"></a>ENDPOINT ERROR: 1xxx</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.7.1.2 "><p id="p580911135610"><a name="p580911135610"></a><a name="p580911135610"></a>EndPoint.1003</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.3 "><p id="p88091011195614"><a name="p88091011195614"></a><a name="p88091011195614"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.4 "><p id="p8809181110566"><a name="p8809181110566"></a><a name="p8809181110566"></a>Invalid service name.</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p17809411185616"><a name="p17809411185616"></a><a name="p17809411185616"></a>Invalid service name.</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.7.1.6 "><p id="p108091011195616"><a name="p108091011195616"></a><a name="p108091011195616"></a>Enter a correct service name.</p>
</td>
</tr>
<tr id="row480971155617"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p480901112563"><a name="p480901112563"></a><a name="p480901112563"></a>EndPoint.1004</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p148095117566"><a name="p148095117566"></a><a name="p148095117566"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1880971125619"><a name="p1880971125619"></a><a name="p1880971125619"></a>Invalid request.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p2809131115615"><a name="p2809131115615"></a><a name="p2809131115615"></a>Invalid request.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p780916114569"><a name="p780916114569"></a><a name="p780916114569"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row1880911165619"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p98090116564"><a name="p98090116564"></a><a name="p98090116564"></a>EndPoint.1008</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p17809111115612"><a name="p17809111115612"></a><a name="p17809111115612"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1780910111567"><a name="p1780910111567"></a><a name="p1780910111567"></a>Failed to obtain the token.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p108091311205612"><a name="p108091311205612"></a><a name="p108091311205612"></a>Failed to obtain the token.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1680912117566"><a name="p1680912117566"></a><a name="p1680912117566"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row380961113564"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p118094111567"><a name="p118094111567"></a><a name="p118094111567"></a>Endpoint.1018</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p78091211175618"><a name="p78091211175618"></a><a name="p78091211175618"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1881013112563"><a name="p1881013112563"></a><a name="p1881013112563"></a>Quota exceeded.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p12810411155614"><a name="p12810411155614"></a><a name="p12810411155614"></a>Quota exceeded.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p6810611165612"><a name="p6810611165612"></a><a name="p6810611165612"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row178101011115614"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1481071114563"><a name="p1481071114563"></a><a name="p1481071114563"></a>EndPoint.1019</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p18810101119568"><a name="p18810101119568"></a><a name="p18810101119568"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p48101111155620"><a name="p48101111155620"></a><a name="p48101111155620"></a>Invalid route table ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p11810311195615"><a name="p11810311195615"></a><a name="p11810311195615"></a>Invalid route table ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p20810201118565"><a name="p20810201118565"></a><a name="p20810201118565"></a>Enter a correct route table ID.</p>
</td>
</tr>
<tr id="row4810011155612"><td class="cellrowborder" rowspan="37" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p168101311115610"><a name="p168101311115610"></a><a name="p168101311115610"></a>ENDPOINT ERROR: 2xxx</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.7.1.2 "><p id="p9810131145616"><a name="p9810131145616"></a><a name="p9810131145616"></a>EndPoint.2001</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.3 "><p id="p11810201117569"><a name="p11810201117569"></a><a name="p11810201117569"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.4 "><p id="p78101211155611"><a name="p78101211155611"></a><a name="p78101211155611"></a>The VPC does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p4810191110562"><a name="p4810191110562"></a><a name="p4810191110562"></a>The VPC does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.7.1.6 "><p id="p13810211125612"><a name="p13810211125612"></a><a name="p13810211125612"></a>Enter a correct VPC ID for the current tenant.</p>
</td>
</tr>
<tr id="row15810131185614"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p18102111560"><a name="p18102111560"></a><a name="p18102111560"></a>EndPoint.2002</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p4810151117568"><a name="p4810151117568"></a><a name="p4810151117568"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p781010114569"><a name="p781010114569"></a><a name="p781010114569"></a>The request input parameter is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p58103114564"><a name="p58103114564"></a><a name="p58103114564"></a>The request input parameter is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p14810211175615"><a name="p14810211175615"></a><a name="p14810211175615"></a>Please input a correct parameter.</p>
</td>
</tr>
<tr id="row08101111195616"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p9811811105616"><a name="p9811811105616"></a><a name="p9811811105616"></a>EndPoint.2003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p4811111145614"><a name="p4811111145614"></a><a name="p4811111145614"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p7811191125611"><a name="p7811191125611"></a><a name="p7811191125611"></a>The endpoint service does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p681181113568"><a name="p681181113568"></a><a name="p681181113568"></a>The VPC endpoint service does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1081131110563"><a name="p1081131110563"></a><a name="p1081131110563"></a>Enter a VPC endpoint service.</p>
</td>
</tr>
<tr id="row16811181115561"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p28111011155617"><a name="p28111011155617"></a><a name="p28111011155617"></a>EndPoint.2004</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p16811161111561"><a name="p16811161111561"></a><a name="p16811161111561"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1181121117566"><a name="p1181121117566"></a><a name="p1181121117566"></a>The endpoint service is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1811311195619"><a name="p1811311195619"></a><a name="p1811311195619"></a>The VPC endpoint service is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p48111911175612"><a name="p48111911175612"></a><a name="p48111911175612"></a>Try again later. If the fault persists, contact customer service.</p>
</td>
</tr>
<tr id="row108116119565"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p28111711145614"><a name="p28111711145614"></a><a name="p28111711145614"></a>EndPoint.2006</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p5811161112566"><a name="p5811161112566"></a><a name="p5811161112566"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p981101165610"><a name="p981101165610"></a><a name="p981101165610"></a>The requested endpoint does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1811511205616"><a name="p1811511205616"></a><a name="p1811511205616"></a>The requested VPC endpoint does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p181121110566"><a name="p181121110566"></a><a name="p181121110566"></a>Enter a correct VPC endpoint.</p>
</td>
</tr>
<tr id="row1481111110562"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p9811141105611"><a name="p9811141105611"></a><a name="p9811141105611"></a>EndPoint.2007</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p3811611195610"><a name="p3811611195610"></a><a name="p3811611195610"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p3811121155612"><a name="p3811121155612"></a><a name="p3811121155612"></a>The endpoint information does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p16811111119562"><a name="p16811111119562"></a><a name="p16811111119562"></a>The VPC endpoint information is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p11811211195614"><a name="p11811211195614"></a><a name="p11811211195614"></a>Enter a correct VPC endpoint and check whether the endpoint is deleted.</p>
</td>
</tr>
<tr id="row5812121175620"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p20812101165614"><a name="p20812101165614"></a><a name="p20812101165614"></a>EndPoint.2008</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p581241165615"><a name="p581241165615"></a><a name="p581241165615"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p6812181135610"><a name="p6812181135610"></a><a name="p6812181135610"></a>The endpoint has been deleted.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p168121411125618"><a name="p168121411125618"></a><a name="p168121411125618"></a>The VPC endpoint has been deleted.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1981241125613"><a name="p1981241125613"></a><a name="p1981241125613"></a>Check whether the VPC endpoint is deleted.</p>
</td>
</tr>
<tr id="row2081211114561"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p2812511135620"><a name="p2812511135620"></a><a name="p2812511135620"></a>EndPoint.2009</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p48121411135611"><a name="p48121411135611"></a><a name="p48121411135611"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1181241111566"><a name="p1181241111566"></a><a name="p1181241111566"></a>The specification information does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1881241135612"><a name="p1881241135612"></a><a name="p1881241135612"></a>The specification is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p681281145612"><a name="p681281145612"></a><a name="p681281145612"></a>Enter a correct specification.</p>
</td>
</tr>
<tr id="row1781271175612"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p28124112561"><a name="p28124112561"></a><a name="p28124112561"></a>EndPoint.2010</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p9812181116567"><a name="p9812181116567"></a><a name="p9812181116567"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p28121911105614"><a name="p28121911105614"></a><a name="p28121911105614"></a>The input parameter subnet ID is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p15812911185611"><a name="p15812911185611"></a><a name="p15812911185611"></a>The input parameter <strong id="b1494755122613"><a name="b1494755122613"></a><a name="b1494755122613"></a>subnet_id</strong> is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1181271165610"><a name="p1181271165610"></a><a name="p1181271165610"></a>Enter a valid subnet ID.</p>
</td>
</tr>
<tr id="row481271112569"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1081211110569"><a name="p1081211110569"></a><a name="p1081211110569"></a>EndPoint.2011</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p981216111565"><a name="p981216111565"></a><a name="p981216111565"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p168121211185618"><a name="p168121211185618"></a><a name="p168121211185618"></a>The input parameter VPC ID is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1281341116562"><a name="p1281341116562"></a><a name="p1281341116562"></a>The input parameter <strong id="b5010401271"><a name="b5010401271"></a><a name="b5010401271"></a>vpc_id</strong> is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p16813111155617"><a name="p16813111155617"></a><a name="p16813111155617"></a>Enter a valid VPC ID.</p>
</td>
</tr>
<tr id="row28131311165610"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p68131911105613"><a name="p68131911105613"></a><a name="p68131911105613"></a>EndPoint.2012</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p12813211175612"><a name="p12813211175612"></a><a name="p12813211175612"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p98131611185619"><a name="p98131611185619"></a><a name="p98131611185619"></a>You have no permission to connect to the VPC endpoint service.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p16813911105616"><a name="p16813911105616"></a><a name="p16813911105616"></a>You have no permission to connect to the VPC endpoint service.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1881313119564"><a name="p1881313119564"></a><a name="p1881313119564"></a>Check whether you have the access permission.</p>
</td>
</tr>
<tr id="row3813101119563"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p168137116568"><a name="p168137116568"></a><a name="p168137116568"></a>EndPoint.2013</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1381314111567"><a name="p1381314111567"></a><a name="p1381314111567"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1081321112561"><a name="p1081321112561"></a><a name="p1081321112561"></a>The endpoint does not belong to the endpoint service.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p19813311175616"><a name="p19813311175616"></a><a name="p19813311175616"></a>The VPC endpoint does not belong to the VPC endpoint service.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p17813181115615"><a name="p17813181115615"></a><a name="p17813181115615"></a>Check whether the VPC endpoint is correct.</p>
</td>
</tr>
<tr id="row681331125618"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p2081371185615"><a name="p2081371185615"></a><a name="p2081371185615"></a>EndPoint.2014</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p281331112566"><a name="p281331112566"></a><a name="p281331112566"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1813101145619"><a name="p1813101145619"></a><a name="p1813101145619"></a>The endpoint has been connected to the endpoint service.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p98131114561"><a name="p98131114561"></a><a name="p98131114561"></a>The VPC endpoint has connected to the VPC endpoint service.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p681371115566"><a name="p681371115566"></a><a name="p681371115566"></a>Connected. You do not need to connect again.</p>
</td>
</tr>
<tr id="row68131811115611"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p381331105610"><a name="p381331105610"></a><a name="p381331105610"></a>EndPoint.2015</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p28144117563"><a name="p28144117563"></a><a name="p28144117563"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p48146110566"><a name="p48146110566"></a><a name="p48146110566"></a>The endpoint has been frozen.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p12814111115619"><a name="p12814111115619"></a><a name="p12814111115619"></a>The VPC endpoint has been frozen.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p4814711125617"><a name="p4814711125617"></a><a name="p4814711125617"></a>Contact customer service to confirm the freezing reason.</p>
</td>
</tr>
<tr id="row78143115567"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1814121165616"><a name="p1814121165616"></a><a name="p1814121165616"></a>EndPoint.2016</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p9814101118569"><a name="p9814101118569"></a><a name="p9814101118569"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p2814161117565"><a name="p2814161117565"></a><a name="p2814161117565"></a>The endpoint pool IP address does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p13814191145612"><a name="p13814191145612"></a><a name="p13814191145612"></a>The VPC endpoint pool IP address does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1681412116563"><a name="p1681412116563"></a><a name="p1681412116563"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row7814011125614"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p781421110563"><a name="p781421110563"></a><a name="p781421110563"></a>EndPoint.2017</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p17814101117561"><a name="p17814101117561"></a><a name="p17814101117561"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p7814131120567"><a name="p7814131120567"></a><a name="p7814131120567"></a>Invalid endpoint ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p10814811115610"><a name="p10814811115610"></a><a name="p10814811115610"></a>The ID of the VPC endpoint is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p58141111165616"><a name="p58141111165616"></a><a name="p58141111165616"></a>Enter a correct VPC endpoint ID.</p>
</td>
</tr>
<tr id="row3814161165615"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p128144113566"><a name="p128144113566"></a><a name="p128144113566"></a>EndPoint.2018</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1081451115611"><a name="p1081451115611"></a><a name="p1081451115611"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p11814141113566"><a name="p11814141113566"></a><a name="p11814141113566"></a>The endpoint is being deleted.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1581481185611"><a name="p1581481185611"></a><a name="p1581481185611"></a>The VPC endpoint is being deleted.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1381561113563"><a name="p1381561113563"></a><a name="p1381561113563"></a>Select an available VPC endpoint.</p>
</td>
</tr>
<tr id="row20815411175616"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p9815411165616"><a name="p9815411165616"></a><a name="p9815411165616"></a>EndPoint.2019</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p12815311195612"><a name="p12815311195612"></a><a name="p12815311195612"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p881541125619"><a name="p881541125619"></a><a name="p881541125619"></a>The endpoint is being created.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p581510113565"><a name="p581510113565"></a><a name="p581510113565"></a>The VPC endpoint is being created.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p188154115560"><a name="p188154115560"></a><a name="p188154115560"></a>Try again later.</p>
</td>
</tr>
<tr id="row10815161112565"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1081513113562"><a name="p1081513113562"></a><a name="p1081513113562"></a>EndPoint.2020</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p18151311185620"><a name="p18151311185620"></a><a name="p18151311185620"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p981513116568"><a name="p981513116568"></a><a name="p981513116568"></a>qrMac or sgMac does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1981514119569"><a name="p1981514119569"></a><a name="p1981514119569"></a><strong id="b1926312448615"><a name="b1926312448615"></a><a name="b1926312448615"></a>qrMac</strong> or <strong id="b150714612614"><a name="b150714612614"></a><a name="b150714612614"></a>sgMac</strong> is not found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p13815161119564"><a name="p13815161119564"></a><a name="p13815161119564"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row9815511135613"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p381512117567"><a name="p381512117567"></a><a name="p381512117567"></a>EndPoint.2021</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p19815311195613"><a name="p19815311195613"></a><a name="p19815311195613"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p4815131112564"><a name="p4815131112564"></a><a name="p4815131112564"></a>Failed to query the VPC.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p198151711165613"><a name="p198151711165613"></a><a name="p198151711165613"></a>Failed to query the VPC.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p10815111115615"><a name="p10815111115615"></a><a name="p10815111115615"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row5815101114560"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p7815191117560"><a name="p7815191117560"></a><a name="p7815191117560"></a>EndPoint.2022</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p281613115568"><a name="p281613115568"></a><a name="p281613115568"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p148164118567"><a name="p148164118567"></a><a name="p148164118567"></a>Failed to create an endpoint.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p11816911155612"><a name="p11816911155612"></a><a name="p11816911155612"></a>Failed to create a VPC endpoint.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p158162117561"><a name="p158162117561"></a><a name="p158162117561"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row1481610111565"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p10816191117568"><a name="p10816191117568"></a><a name="p10816191117568"></a>EndPoint.2023</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1381681110566"><a name="p1381681110566"></a><a name="p1381681110566"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p18161311155616"><a name="p18161311155616"></a><a name="p18161311155616"></a>CIDR is not found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p2816151125616"><a name="p2816151125616"></a><a name="p2816151125616"></a>CIDR is not found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p13816411145617"><a name="p13816411145617"></a><a name="p13816411145617"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row481611110563"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1981613118560"><a name="p1981613118560"></a><a name="p1981613118560"></a>EndPoint.2024</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p881691175615"><a name="p881691175615"></a><a name="p881691175615"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1481691155612"><a name="p1481691155612"></a><a name="p1481691155612"></a>shadowVpc or shadowPort does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p11816141155616"><a name="p11816141155616"></a><a name="p11816141155616"></a><strong id="b95414331562"><a name="b95414331562"></a><a name="b95414331562"></a>shadowVpc</strong> or <strong id="b65893361068"><a name="b65893361068"></a><a name="b65893361068"></a>shadowPort</strong> is null.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1881610112562"><a name="p1881610112562"></a><a name="p1881610112562"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row2816121119566"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p081612116562"><a name="p081612116562"></a><a name="p081612116562"></a>EndPoint.2025</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p11816131111569"><a name="p11816131111569"></a><a name="p11816131111569"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1681611120561"><a name="p1681611120561"></a><a name="p1681611120561"></a>The endpoint port does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p18817711195618"><a name="p18817711195618"></a><a name="p18817711195618"></a>The VPC endpoint port is not found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p881761114563"><a name="p881761114563"></a><a name="p881761114563"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row1481716113562"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p17817161112563"><a name="p17817161112563"></a><a name="p17817161112563"></a>EndPoint.2026</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p981741185618"><a name="p981741185618"></a><a name="p981741185618"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p081741119563"><a name="p081741119563"></a><a name="p081741119563"></a>VNI is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1981711185619"><a name="p1981711185619"></a><a name="p1981711185619"></a>VNI is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p158175112567"><a name="p158175112567"></a><a name="p158175112567"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row1817311145618"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p68171511135613"><a name="p68171511135613"></a><a name="p68171511135613"></a>EndPoint.2027</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1581713112565"><a name="p1581713112565"></a><a name="p1581713112565"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p19817211165615"><a name="p19817211165615"></a><a name="p19817211165615"></a>Invalid action.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p081711115616"><a name="p081711115616"></a><a name="p081711115616"></a>Invalid action.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1481721125610"><a name="p1481721125610"></a><a name="p1481721125610"></a>Enter a valid action.</p>
</td>
</tr>
<tr id="row1281761135613"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p6817131145617"><a name="p6817131145617"></a><a name="p6817131145617"></a>EndPoint.2028</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p8817121114561"><a name="p8817121114561"></a><a name="p8817121114561"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p481771114564"><a name="p481771114564"></a><a name="p481771114564"></a>The endpoint service port or protocol is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p3817191155610"><a name="p3817191155610"></a><a name="p3817191155610"></a>The VPC endpoint service port or protocol is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p17818711145611"><a name="p17818711145611"></a><a name="p17818711145611"></a>Enter a valid port number or protocol.</p>
</td>
</tr>
<tr id="row14818121120562"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p181812115562"><a name="p181812115562"></a><a name="p181812115562"></a>EndPoint.2029</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p2818411165618"><a name="p2818411165618"></a><a name="p2818411165618"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p8818311105619"><a name="p8818311105619"></a><a name="p8818311105619"></a>The requested endpoint service ID is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p188181811135620"><a name="p188181811135620"></a><a name="p188181811135620"></a>The ID of the requested VPC endpoint service is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1681851115615"><a name="p1681851115615"></a><a name="p1681851115615"></a>Enter a valid VPC endpoint service ID.</p>
</td>
</tr>
<tr id="row8818111135612"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p128181611135619"><a name="p128181611135619"></a><a name="p128181611135619"></a>EndPoint.2030</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p118181211175610"><a name="p118181211175610"></a><a name="p118181211175610"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p081811113564"><a name="p081811113564"></a><a name="p081811113564"></a>markerId is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p14818141185617"><a name="p14818141185617"></a><a name="p14818141185617"></a><strong id="b378204016620"><a name="b378204016620"></a><a name="b378204016620"></a>markerId</strong> is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p10818151111569"><a name="p10818151111569"></a><a name="p10818151111569"></a>Enter a valid marker ID.</p>
</td>
</tr>
<tr id="row148180114560"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p18818311105615"><a name="p18818311105615"></a><a name="p18818311105615"></a>EndPoint.2031</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p10818121117566"><a name="p10818121117566"></a><a name="p10818121117566"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p20819211115615"><a name="p20819211115615"></a><a name="p20819211115615"></a>Only one endpoint is allowed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p8819011195619"><a name="p8819011195619"></a><a name="p8819011195619"></a>Only one VPC endpoint is allowed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p7819611155613"><a name="p7819611155613"></a><a name="p7819611155613"></a>A VPC endpoint service allows accepting or rejecting only one VPC endpoint.</p>
</td>
</tr>
<tr id="row48191011185613"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p581919111564"><a name="p581919111564"></a><a name="p581919111564"></a>EndPoint.2033</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p15819161105610"><a name="p15819161105610"></a><a name="p15819161105610"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p138191411155613"><a name="p138191411155613"></a><a name="p138191411155613"></a>The entered parameter enable_dns is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1781941119562"><a name="p1781941119562"></a><a name="p1781941119562"></a>Invalid parameter <strong id="b19391155205720"><a name="b19391155205720"></a><a name="b19391155205720"></a>enable_dns</strong>.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p16820811195613"><a name="p16820811195613"></a><a name="p16820811195613"></a>Enter a valid parameter.</p>
</td>
</tr>
<tr id="row7820911175610"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p782061114561"><a name="p782061114561"></a><a name="p782061114561"></a>EndPoint.2034</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p20820161117566"><a name="p20820161117566"></a><a name="p20820161117566"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p98201111175611"><a name="p98201111175611"></a><a name="p98201111175611"></a>The entered parameter enable_dns is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p3820121165617"><a name="p3820121165617"></a><a name="p3820121165617"></a>The entered parameter <strong id="b1588474624118"><a name="b1588474624118"></a><a name="b1588474624118"></a>enable_dns</strong> is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1582019114567"><a name="p1582019114567"></a><a name="p1582019114567"></a>Enter a valid parameter.</p>
</td>
</tr>
<tr id="row1882001118560"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p88206111563"><a name="p88206111563"></a><a name="p88206111563"></a>EndPoint.2035</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p16820201116568"><a name="p16820201116568"></a><a name="p16820201116568"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p18201611105613"><a name="p18201611105613"></a><a name="p18201611105613"></a>The system parameter dns.enable is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p882081175613"><a name="p882081175613"></a><a name="p882081175613"></a>System parameter <strong id="b1649111597416"><a name="b1649111597416"></a><a name="b1649111597416"></a>dns.enable</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p148208117569"><a name="p148208117569"></a><a name="p148208117569"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row982041117564"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p0821101165613"><a name="p0821101165613"></a><a name="p0821101165613"></a>EndPoint.2037</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p20821311155618"><a name="p20821311155618"></a><a name="p20821311155618"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p6821131155616"><a name="p6821131155616"></a><a name="p6821131155616"></a>The current network does not belong to the VPC.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p4821171135610"><a name="p4821171135610"></a><a name="p4821171135610"></a>The current network does not belong to the VPC.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1782161145612"><a name="p1782161145612"></a><a name="p1782161145612"></a>Check whether the parameter is correct.</p>
</td>
</tr>
<tr id="row1782119117564"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1821511115618"><a name="p1821511115618"></a><a name="p1821511115618"></a>EndPoint.2038</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p782131115565"><a name="p782131115565"></a><a name="p782131115565"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p882141111567"><a name="p882141111567"></a><a name="p882141111567"></a>The pool does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p782111155619"><a name="p782111155619"></a><a name="p782111155619"></a>The resource pool is not found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p08215113567"><a name="p08215113567"></a><a name="p08215113567"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row128211611175616"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p88213119563"><a name="p88213119563"></a><a name="p88213119563"></a>EndPoint.2039</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p17821131145616"><a name="p17821131145616"></a><a name="p17821131145616"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p14821121145615"><a name="p14821121145615"></a><a name="p14821121145615"></a>The route table is being used by another VPC endpoint.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p208229116563"><a name="p208229116563"></a><a name="p208229116563"></a>The route table is being used by another VPC endpoint.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p11822181118560"><a name="p11822181118560"></a><a name="p11822181118560"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row138222011165614"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p138221011175612"><a name="p138221011175612"></a><a name="p138221011175612"></a>EndPoint.2040</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p188221311105610"><a name="p188221311105610"></a><a name="p188221311105610"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p168221511195616"><a name="p168221511195616"></a><a name="p168221511195616"></a>The VPC endpoint has no route table bound.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p6822131115615"><a name="p6822131115615"></a><a name="p6822131115615"></a>The VPC endpoint has no route table associated.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p68221311185613"><a name="p68221311185613"></a><a name="p68221311185613"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row682212116565"><td class="cellrowborder" rowspan="53" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p13822181113563"><a name="p13822181113563"></a><a name="p13822181113563"></a>ENDPOINT_SERVICE ERR0R: 3xxx</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.7.1.2 "><p id="p17822151155616"><a name="p17822151155616"></a><a name="p17822151155616"></a>EndPoint.3001</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.3 "><p id="p5822141185612"><a name="p5822141185612"></a><a name="p5822141185612"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.4 "><p id="p16822101135619"><a name="p16822101135619"></a><a name="p16822101135619"></a>Failed to create a port.</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p282221135618"><a name="p282221135618"></a><a name="p282221135618"></a>Failed to create a port.</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.7.1.6 "><p id="p282241125616"><a name="p282241125616"></a><a name="p282241125616"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row118224110566"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1823131145610"><a name="p1823131145610"></a><a name="p1823131145610"></a>EndPoint.3002</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p782311175610"><a name="p782311175610"></a><a name="p782311175610"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p14823111145610"><a name="p14823111145610"></a><a name="p14823111145610"></a>Invalid permission.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p6823911145611"><a name="p6823911145611"></a><a name="p6823911145611"></a>Invalid permission.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p782310119569"><a name="p782310119569"></a><a name="p782310119569"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row18233118568"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1582321120569"><a name="p1582321120569"></a><a name="p1582321120569"></a>EndPoint.3003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p13823511195617"><a name="p13823511195617"></a><a name="p13823511195617"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1482341118563"><a name="p1482341118563"></a><a name="p1482341118563"></a>Invalid port ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p11823121114565"><a name="p11823121114565"></a><a name="p11823121114565"></a>Invalid port ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p138231911145616"><a name="p138231911145616"></a><a name="p138231911145616"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row3823101185611"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p48236117566"><a name="p48236117566"></a><a name="p48236117566"></a>EndPoint.3004</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1182391195617"><a name="p1182391195617"></a><a name="p1182391195617"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p282461105612"><a name="p282461105612"></a><a name="p282461105612"></a>Invalid port.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p11824711145612"><a name="p11824711145612"></a><a name="p11824711145612"></a>Invalid port.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p782471125613"><a name="p782471125613"></a><a name="p782471125613"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row2824141185617"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p16824131120565"><a name="p16824131120565"></a><a name="p16824131120565"></a>EndPoint.3005</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p20824811145614"><a name="p20824811145614"></a><a name="p20824811145614"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p38248113565"><a name="p38248113565"></a><a name="p38248113565"></a>Failed to delete the endpoint service.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p6824311185616"><a name="p6824311185616"></a><a name="p6824311185616"></a>Failed to delete the VPC endpoint service.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p148241611115619"><a name="p148241611115619"></a><a name="p148241611115619"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row13824411205617"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p082421145611"><a name="p082421145611"></a><a name="p082421145611"></a>EndPoint.3006</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p2824711115613"><a name="p2824711115613"></a><a name="p2824711115613"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1082431155615"><a name="p1082431155615"></a><a name="p1082431155615"></a>The endpoint service is being used.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1782441135613"><a name="p1782441135613"></a><a name="p1782441135613"></a>The VPC endpoint service is being used.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1082421114567"><a name="p1082421114567"></a><a name="p1082421114567"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row282521195611"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p4825101111563"><a name="p4825101111563"></a><a name="p4825101111563"></a>EndPoint.3008</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p3825411125619"><a name="p3825411125619"></a><a name="p3825411125619"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1582571115611"><a name="p1582571115611"></a><a name="p1582571115611"></a>The port does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p2825811195620"><a name="p2825811195620"></a><a name="p2825811195620"></a>The port is not found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p982511111564"><a name="p982511111564"></a><a name="p982511111564"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row3825131185612"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1382581185615"><a name="p1382581185615"></a><a name="p1382581185615"></a>EndPoint.3009</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p482591114567"><a name="p482591114567"></a><a name="p482591114567"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p16825121125616"><a name="p16825121125616"></a><a name="p16825121125616"></a>Invalid CIDR.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p682516117561"><a name="p682516117561"></a><a name="p682516117561"></a>Invalid CIDR.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p682571105620"><a name="p682571105620"></a><a name="p682571105620"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row17825611175612"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1082518116569"><a name="p1082518116569"></a><a name="p1082518116569"></a>EndPoint.3010</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1782513113566"><a name="p1782513113566"></a><a name="p1782513113566"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p882681195616"><a name="p882681195616"></a><a name="p882681195616"></a>Invalid IP address.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p168261411115616"><a name="p168261411115616"></a><a name="p168261411115616"></a>Invalid IP address.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p13826191165612"><a name="p13826191165612"></a><a name="p13826191165612"></a>Enter a correct IP address.</p>
</td>
</tr>
<tr id="row1682614113561"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p188269113568"><a name="p188269113568"></a><a name="p188269113568"></a>EndPoint.3011</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p88265111561"><a name="p88265111561"></a><a name="p88265111561"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1982611113566"><a name="p1982611113566"></a><a name="p1982611113566"></a>Parameter IP is not required to create an endpoint service (interface).</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p4826171113567"><a name="p4826171113567"></a><a name="p4826171113567"></a>Parameter <strong id="b4135201470"><a name="b4135201470"></a><a name="b4135201470"></a>ip</strong> is not required to create a VPC endpoint service (interface).</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1482621125616"><a name="p1482621125616"></a><a name="p1482621125616"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row13826111116560"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p17826131175614"><a name="p17826131175614"></a><a name="p17826131175614"></a>EndPoint.3013</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p282681155612"><a name="p282681155612"></a><a name="p282681155612"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p148267111562"><a name="p148267111562"></a><a name="p148267111562"></a>endpointService interface vlan can't have vpcId.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p382681119566"><a name="p382681119566"></a><a name="p382681119566"></a>The request for accessing the VLAN VPC endpoint service cannot contain VPC ID information.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1982619119560"><a name="p1982619119560"></a><a name="p1982619119560"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row1826151114560"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p18827191117563"><a name="p18827191117563"></a><a name="p18827191117563"></a>EndPoint.3014</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p0827511105619"><a name="p0827511105619"></a><a name="p0827511105619"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p18271611105616"><a name="p18271611105616"></a><a name="p18271611105616"></a>endpointService interface can't have cidr.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1582781135617"><a name="p1582781135617"></a><a name="p1582781135617"></a>The request for accessing the VPC endpoint service (interface) cannot contain CIDR.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p2827111111565"><a name="p2827111111565"></a><a name="p2827111111565"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row1782711111567"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1382791111566"><a name="p1382791111566"></a><a name="p1382791111566"></a>EndPoint.3015</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p8827101115561"><a name="p8827101115561"></a><a name="p8827101115561"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p0827191115613"><a name="p0827191115613"></a><a name="p0827191115613"></a>endpointService gateway vlan can't have portId.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p7827181110562"><a name="p7827181110562"></a><a name="p7827181110562"></a>The request for accessing the VLAN VPC endpoint service (gateway) cannot contain the port ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1827121116563"><a name="p1827121116563"></a><a name="p1827121116563"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row1827311135619"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p178277115566"><a name="p178277115566"></a><a name="p178277115566"></a>EndPoint.3016</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p16827711195611"><a name="p16827711195611"></a><a name="p16827711195611"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p6827011125611"><a name="p6827011125611"></a><a name="p6827011125611"></a>endpointService gateway vlan can't have ip.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p138278113560"><a name="p138278113560"></a><a name="p138278113560"></a>The request for accessing the VLAN VPC endpoint service cannot contain IP address information.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p782814110564"><a name="p782814110564"></a><a name="p782814110564"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row582871118562"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p7828141145611"><a name="p7828141145611"></a><a name="p7828141145611"></a>EndPoint.3017</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p5828811125613"><a name="p5828811125613"></a><a name="p5828811125613"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p9828181110561"><a name="p9828181110561"></a><a name="p9828181110561"></a>Invalid CIDRs.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p11828011175612"><a name="p11828011175612"></a><a name="p11828011175612"></a>Invalid CIDRs.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p14828211175613"><a name="p14828211175613"></a><a name="p14828211175613"></a>Enter correct CIDRs.</p>
</td>
</tr>
<tr id="row9828121117566"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1482813110568"><a name="p1482813110568"></a><a name="p1482813110568"></a>EndPoint.3018</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p188281811145619"><a name="p188281811145619"></a><a name="p188281811145619"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1828201175613"><a name="p1828201175613"></a><a name="p1828201175613"></a>endpointService gateway vlan can't have vpcId.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p14828511165619"><a name="p14828511165619"></a><a name="p14828511165619"></a>The request for accessing the VLAN VPC endpoint service cannot contain VPC ID information.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p7830511105619"><a name="p7830511105619"></a><a name="p7830511105619"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row1083011165619"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p08302011205618"><a name="p08302011205618"></a><a name="p08302011205618"></a>EndPoint.3021</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p88307112567"><a name="p88307112567"></a><a name="p88307112567"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1583001116563"><a name="p1583001116563"></a><a name="p1583001116563"></a>Invalid serverType.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p16830151165616"><a name="p16830151165616"></a><a name="p16830151165616"></a>Invalid parameter <strong id="b1460911117593"><a name="b1460911117593"></a><a name="b1460911117593"></a>serverType</strong>.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p583017112568"><a name="p583017112568"></a><a name="p583017112568"></a>Enter a valid parameter.</p>
</td>
</tr>
<tr id="row1983071135615"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p083015114568"><a name="p083015114568"></a><a name="p083015114568"></a>EndPoint.3022</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p5830171165616"><a name="p5830171165616"></a><a name="p5830171165616"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p983013111563"><a name="p983013111563"></a><a name="p983013111563"></a>Failed to create a network.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p98302011145617"><a name="p98302011145617"></a><a name="p98302011145617"></a>Failed to create a network.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p5830131112561"><a name="p5830131112561"></a><a name="p5830131112561"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row8830151115569"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p19831151119561"><a name="p19831151119561"></a><a name="p19831151119561"></a>EndPoint.3023</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1483131118567"><a name="p1483131118567"></a><a name="p1483131118567"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1831191114568"><a name="p1831191114568"></a><a name="p1831191114568"></a>Failed to create a subnet.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p583171113568"><a name="p583171113568"></a><a name="p583171113568"></a>Failed to create a subnet.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p683117114568"><a name="p683117114568"></a><a name="p683117114568"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row58312118568"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p28314119561"><a name="p28314119561"></a><a name="p28314119561"></a>EndPoint.3035</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p5831211125614"><a name="p5831211125614"></a><a name="p5831211125614"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p3831211135616"><a name="p3831211135616"></a><a name="p3831211135616"></a>Invalid action.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1583120116563"><a name="p1583120116563"></a><a name="p1583120116563"></a>Invalid action.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1283118114563"><a name="p1283118114563"></a><a name="p1283118114563"></a>Enter a correct action.</p>
</td>
</tr>
<tr id="row198311811175614"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p783191185620"><a name="p783191185620"></a><a name="p783191185620"></a>EndPoint.3036</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p283131115618"><a name="p283131115618"></a><a name="p283131115618"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p183111119567"><a name="p183111119567"></a><a name="p183111119567"></a>Invalid permissions.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p19832111113567"><a name="p19832111113567"></a><a name="p19832111113567"></a>The permission list cannot be empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p3832181125620"><a name="p3832181125620"></a><a name="p3832181125620"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row6832101125616"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p8832911195618"><a name="p8832911195618"></a><a name="p8832911195618"></a>EndPoint.3040</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p283221145618"><a name="p283221145618"></a><a name="p283221145618"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p13832121115615"><a name="p13832121115615"></a><a name="p13832121115615"></a>Failed to add a rollback task.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p118321411115613"><a name="p118321411115613"></a><a name="p118321411115613"></a>Failed to add a rollback task.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p083271111565"><a name="p083271111565"></a><a name="p083271111565"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row20832181185617"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1383212112568"><a name="p1383212112568"></a><a name="p1383212112568"></a>EndPoint.3042</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p2832111185618"><a name="p2832111185618"></a><a name="p2832111185618"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p118321115562"><a name="p118321115562"></a><a name="p118321115562"></a>The port ID does not belong to the current VPC.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p10832111135617"><a name="p10832111135617"></a><a name="p10832111135617"></a>The port ID does not belong to the current VPC.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p3832311135610"><a name="p3832311135610"></a><a name="p3832311135610"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row98321311185611"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p158329114561"><a name="p158329114561"></a><a name="p158329114561"></a>EndPoint.3043</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1683351112560"><a name="p1683351112560"></a><a name="p1683351112560"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p6833511175618"><a name="p6833511175618"></a><a name="p6833511175618"></a>The service port is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p983315118562"><a name="p983315118562"></a><a name="p983315118562"></a>Invalid service port.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p9833181185611"><a name="p9833181185611"></a><a name="p9833181185611"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row108331111135613"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1683351105611"><a name="p1683351105611"></a><a name="p1683351105611"></a>EndPoint.3044</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1983301185617"><a name="p1983301185617"></a><a name="p1983301185617"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p88331611205618"><a name="p88331611205618"></a><a name="p88331611205618"></a>The parameter ports conflicted with ports in an existing endpoint service.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1983317111565"><a name="p1983317111565"></a><a name="p1983317111565"></a>This port conflicted with the port of an existing endpoint service.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p6833181185615"><a name="p6833181185615"></a><a name="p6833181185615"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row1083331125615"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p6833311115616"><a name="p6833311115616"></a><a name="p6833311115616"></a>EndPoint.3045</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p18833131117567"><a name="p18833131117567"></a><a name="p18833131117567"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p583371118569"><a name="p583371118569"></a><a name="p583371118569"></a>Other properties cannot be modified in the current endpoint service state.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p2834611155620"><a name="p2834611155620"></a><a name="p2834611155620"></a>Modifying other properties in the current endpoint service state is not supported.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p383414113566"><a name="p383414113566"></a><a name="p383414113566"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row9834211165613"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1683412111569"><a name="p1683412111569"></a><a name="p1683412111569"></a>EndPoint.3046</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p9834161119561"><a name="p9834161119561"></a><a name="p9834161119561"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p208342115569"><a name="p208342115569"></a><a name="p208342115569"></a>The IP address conflicted with an existing endpoint service.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p15834151165615"><a name="p15834151165615"></a><a name="p15834151165615"></a>The IP address conflicted with an existing VPC endpoint service.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1683421112564"><a name="p1683421112564"></a><a name="p1683421112564"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row18352011175615"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p383521125613"><a name="p383521125613"></a><a name="p383521125613"></a>EndPoint.3048</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p148351311165610"><a name="p148351311165610"></a><a name="p148351311165610"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p13835311115614"><a name="p13835311115614"></a><a name="p13835311115614"></a>Invalid netType.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p14835611185617"><a name="p14835611185617"></a><a name="p14835611185617"></a>Invalid <strong id="b197921111773"><a name="b197921111773"></a><a name="b197921111773"></a>netType</strong>.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p68361711135610"><a name="p68361711135610"></a><a name="p68361711135610"></a>Enter a valid value.</p>
</td>
</tr>
<tr id="row1183617118566"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p783618115569"><a name="p783618115569"></a><a name="p783618115569"></a>EndPoint.3049</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p168361711105615"><a name="p168361711105615"></a><a name="p168361711105615"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p18836611115612"><a name="p18836611115612"></a><a name="p18836611115612"></a>The maximum number of whitelist records has been reached.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p148362011125616"><a name="p148362011125616"></a><a name="p148362011125616"></a>The maximum number of whitelist records has been reached.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1583613112563"><a name="p1583613112563"></a><a name="p1583613112563"></a>Delete invalid whitelist records or add an authorized account ID named *.</p>
</td>
</tr>
<tr id="row16836011195616"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p16836111119565"><a name="p16836111119565"></a><a name="p16836111119565"></a>EndPoint.3051</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p15836411135619"><a name="p15836411135619"></a><a name="p15836411135619"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p10836141115612"><a name="p10836141115612"></a><a name="p10836141115612"></a>Endpoint service vip port id is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p98369113565"><a name="p98369113565"></a><a name="p98369113565"></a>Invalid parameter <strong id="b184664541040"><a name="b184664541040"></a><a name="b184664541040"></a>vip_port_id</strong>.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p17837101110561"><a name="p17837101110561"></a><a name="p17837101110561"></a>Enter a correct value.</p>
</td>
</tr>
<tr id="row88371011105610"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p783781110562"><a name="p783781110562"></a><a name="p783781110562"></a>EndPoint.3052</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p14837151112569"><a name="p14837151112569"></a><a name="p14837151112569"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p19837161175614"><a name="p19837161175614"></a><a name="p19837161175614"></a>portId and ip cannot be modified at the same time.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p9837151117563"><a name="p9837151117563"></a><a name="p9837151117563"></a><strong id="b24471913123112"><a name="b24471913123112"></a><a name="b24471913123112"></a>portId</strong> and <strong id="b1452521793117"><a name="b1452521793117"></a><a name="b1452521793117"></a>ip</strong> cannot be modified at the same time.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p883781117566"><a name="p883781117566"></a><a name="p883781117566"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row18371311205615"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p16837511185616"><a name="p16837511185616"></a><a name="p16837511185616"></a>EndPoint.3053</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p48372112563"><a name="p48372112563"></a><a name="p48372112563"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p483711118564"><a name="p483711118564"></a><a name="p483711118564"></a>vipPortId and ip cannot be modified at the same time.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p16838211155614"><a name="p16838211155614"></a><a name="p16838211155614"></a><strong id="b17579281885"><a name="b17579281885"></a><a name="b17579281885"></a>vipPortId</strong> and <strong id="b571913307812"><a name="b571913307812"></a><a name="b571913307812"></a>ip</strong> cannot be modified at the same time.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p9838121105620"><a name="p9838121105620"></a><a name="p9838121105620"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row083851175618"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p138387114565"><a name="p138387114565"></a><a name="p138387114565"></a>EndPoint.3054</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p58385117562"><a name="p58385117562"></a><a name="p58385117562"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p198381114565"><a name="p198381114565"></a><a name="p198381114565"></a>portId or vipPortId cannot be modified.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p583881120569"><a name="p583881120569"></a><a name="p583881120569"></a><strong id="b839118361382"><a name="b839118361382"></a><a name="b839118361382"></a>portId</strong> or <strong id="b17225539185"><a name="b17225539185"></a><a name="b17225539185"></a>vipPortId</strong> cannot be modified.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p68381611125615"><a name="p68381611125615"></a><a name="p68381611125615"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row198384111563"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p19838511125617"><a name="p19838511125617"></a><a name="p19838511125617"></a>EndPoint.3055</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p12838191111562"><a name="p12838191111562"></a><a name="p12838191111562"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p128381113565"><a name="p128381113565"></a><a name="p128381113565"></a>ip cannot be modified.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1883881135610"><a name="p1883881135610"></a><a name="p1883881135610"></a><strong id="b694334312810"><a name="b694334312810"></a><a name="b694334312810"></a>ip</strong> cannot be modified.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1183921112562"><a name="p1183921112562"></a><a name="p1183921112562"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row28394111567"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1383931155610"><a name="p1383931155610"></a><a name="p1383931155610"></a>EndPoint.3056</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p88392011145614"><a name="p88392011145614"></a><a name="p88392011145614"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p583951110563"><a name="p583951110563"></a><a name="p583951110563"></a>The maximum of VPC endpoint services using the same IP address has been reached.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p2839311185618"><a name="p2839311185618"></a><a name="p2839311185618"></a>The maximum of VPC endpoint services supported by a backend resource has been reached.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p2839191125613"><a name="p2839191125613"></a><a name="p2839191125613"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row138391911155614"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1183901110565"><a name="p1183901110565"></a><a name="p1183901110565"></a>EndPoint.3057</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1784051115560"><a name="p1784051115560"></a><a name="p1784051115560"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p38401411175614"><a name="p38401411175614"></a><a name="p38401411175614"></a>cidr cannot be modified.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p38405117564"><a name="p38405117564"></a><a name="p38405117564"></a>CIDR cannot be modified.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p884061185615"><a name="p884061185615"></a><a name="p884061185615"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row15840151185620"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p184011110564"><a name="p184011110564"></a><a name="p184011110564"></a>EndPoint.3058</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p128401111135619"><a name="p128401111135619"></a><a name="p128401111135619"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p4840811115613"><a name="p4840811115613"></a><a name="p4840811115613"></a>The domain name is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p13840311175617"><a name="p13840311175617"></a><a name="p13840311175617"></a>Invalid domain name.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p138401611125617"><a name="p138401611125617"></a><a name="p138401611125617"></a>Enter a correct domain name.</p>
</td>
</tr>
<tr id="row13840101115619"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p984012118562"><a name="p984012118562"></a><a name="p984012118562"></a>EndPoint.3059</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p20841511205610"><a name="p20841511205610"></a><a name="p20841511205610"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p4841201113567"><a name="p4841201113567"></a><a name="p4841201113567"></a>The domain name already exists.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p18841171185619"><a name="p18841171185619"></a><a name="p18841171185619"></a>The domain name already exists.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p10841121110561"><a name="p10841121110561"></a><a name="p10841121110561"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row1384112111562"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p78411411165618"><a name="p78411411165618"></a><a name="p78411411165618"></a>EndPoint.3060</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p5841111115612"><a name="p5841111115612"></a><a name="p5841111115612"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p10841191175611"><a name="p10841191175611"></a><a name="p10841191175611"></a>You have no permission to add domain names.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p384161111563"><a name="p384161111563"></a><a name="p384161111563"></a>You have no permission to add domain names.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1984181118564"><a name="p1984181118564"></a><a name="p1984181118564"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row1184191175614"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p128411811175616"><a name="p128411811175616"></a><a name="p128411811175616"></a>EndPoint.3061</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p198419117564"><a name="p198419117564"></a><a name="p198419117564"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p184131114563"><a name="p184131114563"></a><a name="p184131114563"></a>The maximum number of domain names has reached.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p784212112567"><a name="p784212112567"></a><a name="p784212112567"></a>The maximum number of domain names has been reached.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p10842911115612"><a name="p10842911115612"></a><a name="p10842911115612"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row1084231110567"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p38421911105618"><a name="p38421911105618"></a><a name="p38421911105618"></a>EndPoint.3062</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p10842151155611"><a name="p10842151155611"></a><a name="p10842151155611"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p98421411105614"><a name="p98421411105614"></a><a name="p98421411105614"></a>Invalid endpoint service ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p148421911185616"><a name="p148421911185616"></a><a name="p148421911185616"></a>Invalid VPC endpoint service ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p48421211135616"><a name="p48421211135616"></a><a name="p48421211135616"></a>Enter a correct parameter.</p>
</td>
</tr>
<tr id="row18842131112562"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p19842311155614"><a name="p19842311155614"></a><a name="p19842311155614"></a>EndPoint.3063</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1684221119560"><a name="p1684221119560"></a><a name="p1684221119560"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p13842911175620"><a name="p13842911175620"></a><a name="p13842911175620"></a>Invalid port ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p0842171135618"><a name="p0842171135618"></a><a name="p0842171135618"></a>Invalid port ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p13843171135617"><a name="p13843171135617"></a><a name="p13843171135617"></a>Enter a correct port ID.</p>
</td>
</tr>
<tr id="row1184311110563"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1984321155614"><a name="p1984321155614"></a><a name="p1984321155614"></a>EndPoint.3066</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p18843151111560"><a name="p18843151111560"></a><a name="p18843151111560"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p12843101117569"><a name="p12843101117569"></a><a name="p12843101117569"></a>The tag cannot be empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p8843151155616"><a name="p8843151155616"></a><a name="p8843151155616"></a>The tag cannot be empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p4843511125611"><a name="p4843511125611"></a><a name="p4843511125611"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row3843211195612"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p19843181118566"><a name="p19843181118566"></a><a name="p19843181118566"></a>EndPoint.3067</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p684391115610"><a name="p684391115610"></a><a name="p684391115610"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p12843011115617"><a name="p12843011115617"></a><a name="p12843011115617"></a>The tag key cannot be duplicated.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p3843191115568"><a name="p3843191115568"></a><a name="p3843191115568"></a>The tag key cannot be duplicated.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p7843161111569"><a name="p7843161111569"></a><a name="p7843161111569"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row1684320116568"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p13844911185619"><a name="p13844911185619"></a><a name="p13844911185619"></a>EndPoint.3068</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p58441811105612"><a name="p58441811105612"></a><a name="p58441811105612"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p198442011195620"><a name="p198442011195620"></a><a name="p198442011195620"></a>Tag keys and values should meet relevant requirements.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p138446113563"><a name="p138446113563"></a><a name="p138446113563"></a>Tag keys and values must meet relevant requirements.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1844911175620"><a name="p1844911175620"></a><a name="p1844911175620"></a>Enter a correct request body.</p>
</td>
</tr>
<tr id="row1784415116566"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p784461175613"><a name="p784461175613"></a><a name="p784461175613"></a>EndPoint.3069</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p13844101115612"><a name="p13844101115612"></a><a name="p13844101115612"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p118448112567"><a name="p118448112567"></a><a name="p118448112567"></a>The maximum number of tags has been reached.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p2084418112567"><a name="p2084418112567"></a><a name="p2084418112567"></a>The maximum number of tags has been reached.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1784410116563"><a name="p1784410116563"></a><a name="p1784410116563"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row08447113565"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p28443113562"><a name="p28443113562"></a><a name="p28443113562"></a>EndPoint.3070</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p184513110562"><a name="p184513110562"></a><a name="p184513110562"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p11845191175616"><a name="p11845191175616"></a><a name="p11845191175616"></a>Invalid resource type.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p208474113563"><a name="p208474113563"></a><a name="p208474113563"></a>Incorrect resource type.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p10847311185618"><a name="p10847311185618"></a><a name="p10847311185618"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row14847141165617"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p10847411135610"><a name="p10847411135610"></a><a name="p10847411135610"></a>EndPoint.3071</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p78481611195613"><a name="p78481611195613"></a><a name="p78481611195613"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p168481511155613"><a name="p168481511155613"></a><a name="p168481511155613"></a>The tag value cannot be duplicated.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p384817119567"><a name="p384817119567"></a><a name="p384817119567"></a>Tag values cannot be duplicated.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1084831119560"><a name="p1084831119560"></a><a name="p1084831119560"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row15848011145620"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p28487114567"><a name="p28487114567"></a><a name="p28487114567"></a>EndPoint.3072</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p284814116560"><a name="p284814116560"></a><a name="p284814116560"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p20848811195612"><a name="p20848811195612"></a><a name="p20848811195612"></a>The tag key size is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p17848181114566"><a name="p17848181114566"></a><a name="p17848181114566"></a>The tag key size is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p9848131117567"><a name="p9848131117567"></a><a name="p9848131117567"></a>Enter a correct tag key.</p>
</td>
</tr>
<tr id="row2848141115562"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p58481611105617"><a name="p58481611105617"></a><a name="p58481611105617"></a>EndPoint.3073</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p3848711185610"><a name="p3848711185610"></a><a name="p3848711185610"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1284914118565"><a name="p1284914118565"></a><a name="p1284914118565"></a>The tag value size is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p178494118562"><a name="p178494118562"></a><a name="p178494118562"></a>The tag value size is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p128491811105616"><a name="p128491811105616"></a><a name="p128491811105616"></a>Enter a correct tag value.</p>
</td>
</tr>
<tr id="row16849511185613"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p148498117566"><a name="p148498117566"></a><a name="p148498117566"></a>EndPoint.3074</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p38491611205613"><a name="p38491611205613"></a><a name="p38491611205613"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p13849171115564"><a name="p13849171115564"></a><a name="p13849171115564"></a>The maximum of ports has been reached.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1984981114567"><a name="p1984981114567"></a><a name="p1984981114567"></a>The maximum of port mappings has been reached.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p48504117569"><a name="p48504117569"></a><a name="p48504117569"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row178501211205615"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p13850201135617"><a name="p13850201135617"></a><a name="p13850201135617"></a>EndPoint.3075</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p7850131111568"><a name="p7850131111568"></a><a name="p7850131111568"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1685081118567"><a name="p1685081118567"></a><a name="p1685081118567"></a>The protocol is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p10850911105617"><a name="p10850911105617"></a><a name="p10850911105617"></a>Invalid protocol.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p10851111145610"><a name="p10851111145610"></a><a name="p10851111145610"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row0851711125613"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p188511911195616"><a name="p188511911195616"></a><a name="p188511911195616"></a>EndPoint.3076</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p5851911125615"><a name="p5851911125615"></a><a name="p5851911125615"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p98518115564"><a name="p98518115564"></a><a name="p98518115564"></a>Invalid service name.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p108511011175614"><a name="p108511011175614"></a><a name="p108511011175614"></a>Invalid service name.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1385161145611"><a name="p1385161145611"></a><a name="p1385161145611"></a>Enter a valid service name.</p>
</td>
</tr>
<tr id="row2085161165617"><td class="cellrowborder" rowspan="27" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p18851201115565"><a name="p18851201115565"></a><a name="p18851201115565"></a>NEUTRON ERR0R: 4xxx</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.7.1.2 "><p id="p188511111135619"><a name="p188511111135619"></a><a name="p188511111135619"></a>EndPoint.4001</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.3 "><p id="p18512011195612"><a name="p18512011195612"></a><a name="p18512011195612"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.4 "><p id="p1885251125614"><a name="p1885251125614"></a><a name="p1885251125614"></a>Failed to query the subnet.</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p15852141111569"><a name="p15852141111569"></a><a name="p15852141111569"></a>Failed to query the subnet.</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.7.1.6 "><p id="p585214114561"><a name="p585214114561"></a><a name="p585214114561"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row2852111155619"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p285213119566"><a name="p285213119566"></a><a name="p285213119566"></a>EndPoint.4002</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p188523117567"><a name="p188523117567"></a><a name="p188523117567"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p208521911115616"><a name="p208521911115616"></a><a name="p208521911115616"></a>Failed to create a subnet.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p138521711135616"><a name="p138521711135616"></a><a name="p138521711135616"></a>Failed to create a subnet.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1985281119568"><a name="p1985281119568"></a><a name="p1985281119568"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row3852151185616"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1685311145615"><a name="p1685311145615"></a><a name="p1685311145615"></a>EndPoint.4003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p178531511165619"><a name="p178531511165619"></a><a name="p178531511165619"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p885313115568"><a name="p885313115568"></a><a name="p885313115568"></a>Failed to delete the subnet.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p78531011125616"><a name="p78531011125616"></a><a name="p78531011125616"></a>Failed to delete the subnet.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1685311175618"><a name="p1685311175618"></a><a name="p1685311175618"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row138533112562"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p6853101175615"><a name="p6853101175615"></a><a name="p6853101175615"></a>EndPoint.4004</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p17853011115620"><a name="p17853011115620"></a><a name="p17853011115620"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1785371110566"><a name="p1785371110566"></a><a name="p1785371110566"></a>The subnet is not found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p485320110563"><a name="p485320110563"></a><a name="p485320110563"></a>The subnet does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p108549110567"><a name="p108549110567"></a><a name="p108549110567"></a>Check the entered subnet ID. If the fault persists, contact customer service.</p>
</td>
</tr>
<tr id="row385491185611"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1085401165616"><a name="p1085401165616"></a><a name="p1085401165616"></a>EndPoint.4005</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p985441115617"><a name="p985441115617"></a><a name="p985441115617"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p15854121120566"><a name="p15854121120566"></a><a name="p15854121120566"></a>Failed to query the network.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p485421112560"><a name="p485421112560"></a><a name="p485421112560"></a>Failed to query the network.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1385471120566"><a name="p1385471120566"></a><a name="p1385471120566"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row19854911145615"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1885451112561"><a name="p1885451112561"></a><a name="p1885451112561"></a>EndPoint.4006</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1785411155616"><a name="p1785411155616"></a><a name="p1785411155616"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p985581115561"><a name="p985581115561"></a><a name="p985581115561"></a>Failed to create a network.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p138551011105619"><a name="p138551011105619"></a><a name="p138551011105619"></a>Failed to create a network.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p78551611145620"><a name="p78551611145620"></a><a name="p78551611145620"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row4855111165611"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p985511111560"><a name="p985511111560"></a><a name="p985511111560"></a>EndPoint.4007</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p58551311105616"><a name="p58551311105616"></a><a name="p58551311105616"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p58551911165612"><a name="p58551911165612"></a><a name="p58551911165612"></a>Failed to delete the network.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p118551011135620"><a name="p118551011135620"></a><a name="p118551011135620"></a>Failed to delete the network.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p98551711175610"><a name="p98551711175610"></a><a name="p98551711175610"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row1685512111561"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p168559119561"><a name="p168559119561"></a><a name="p168559119561"></a>EndPoint.4008</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1855311125616"><a name="p1855311125616"></a><a name="p1855311125616"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p8856191155617"><a name="p8856191155617"></a><a name="p8856191155617"></a>Network is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p168561113568"><a name="p168561113568"></a><a name="p168561113568"></a>Network is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p18856161115569"><a name="p18856161115569"></a><a name="p18856161115569"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row1185616119561"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p0856131135611"><a name="p0856131135611"></a><a name="p0856131135611"></a>EndPoint.4009</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1085614116562"><a name="p1085614116562"></a><a name="p1085614116562"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p785681105618"><a name="p785681105618"></a><a name="p785681105618"></a>Failed to query the port.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p985691135611"><a name="p985691135611"></a><a name="p985691135611"></a>Failed to query the port.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p17856161105612"><a name="p17856161105612"></a><a name="p17856161105612"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row12856911135611"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1885661112568"><a name="p1885661112568"></a><a name="p1885661112568"></a>EndPoint.4010</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p68573119564"><a name="p68573119564"></a><a name="p68573119564"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p985716112563"><a name="p985716112563"></a><a name="p985716112563"></a>Failed to create a port.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p2857111114568"><a name="p2857111114568"></a><a name="p2857111114568"></a>Failed to create a port.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p14857411115620"><a name="p14857411115620"></a><a name="p14857411115620"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row1485721175614"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p88571511135615"><a name="p88571511135615"></a><a name="p88571511135615"></a>EndPoint.4011</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1185716116566"><a name="p1185716116566"></a><a name="p1185716116566"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p11859011195619"><a name="p11859011195619"></a><a name="p11859011195619"></a>Failed to delete the port.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p5859121112561"><a name="p5859121112561"></a><a name="p5859121112561"></a>Failed to delete the port.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p48591011205613"><a name="p48591011205613"></a><a name="p48591011205613"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row188591811105615"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p138593111563"><a name="p138593111563"></a><a name="p138593111563"></a>EndPoint.4012</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p585941113564"><a name="p585941113564"></a><a name="p585941113564"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1185991116565"><a name="p1185991116565"></a><a name="p1185991116565"></a>The port is not found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p685951112563"><a name="p685951112563"></a><a name="p685951112563"></a>The port is not found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p17859101110564"><a name="p17859101110564"></a><a name="p17859101110564"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row188595119569"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1386031113565"><a name="p1386031113565"></a><a name="p1386031113565"></a>EndPoint.4013</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1086010115562"><a name="p1086010115562"></a><a name="p1086010115562"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p786011113562"><a name="p786011113562"></a><a name="p786011113562"></a>Failed to query the proxy.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p138601311205616"><a name="p138601311205616"></a><a name="p138601311205616"></a>Failed to query the proxy.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p148601911185611"><a name="p148601911185611"></a><a name="p148601911185611"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row68602112566"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p986014115565"><a name="p986014115565"></a><a name="p986014115565"></a>EndPoint.4014</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p13860511115618"><a name="p13860511115618"></a><a name="p13860511115618"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p78604114561"><a name="p78604114561"></a><a name="p78604114561"></a>Failed to query the router.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p18861131116567"><a name="p18861131116567"></a><a name="p18861131116567"></a>Failed to query the route.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p20861111195611"><a name="p20861111195611"></a><a name="p20861111195611"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row886121155620"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p178611511115617"><a name="p178611511115617"></a><a name="p178611511115617"></a>EndPoint.4015</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p3861711125611"><a name="p3861711125611"></a><a name="p3861711125611"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1086115113568"><a name="p1086115113568"></a><a name="p1086115113568"></a>The router is not found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1986151120561"><a name="p1986151120561"></a><a name="p1986151120561"></a>The route is not found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p18861151111563"><a name="p18861151111563"></a><a name="p18861151111563"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row178611911165617"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p14861111110564"><a name="p14861111110564"></a><a name="p14861111110564"></a>EndPoint.4016</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1862181115610"><a name="p1862181115610"></a><a name="p1862181115610"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p5862161112562"><a name="p5862161112562"></a><a name="p5862161112562"></a>Failed to add an interface router.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p10862161118562"><a name="p10862161118562"></a><a name="p10862161118562"></a>Failed to add an interface route.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p7862181165619"><a name="p7862181165619"></a><a name="p7862181165619"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row158621011115616"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p986291117565"><a name="p986291117565"></a><a name="p986291117565"></a>EndPoint.4017</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p12862911125614"><a name="p12862911125614"></a><a name="p12862911125614"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p98621011155617"><a name="p98621011155617"></a><a name="p98621011155617"></a>Failed to delete the interface router.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1186214112564"><a name="p1186214112564"></a><a name="p1186214112564"></a>Failed to delete the interface route.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p19863161175618"><a name="p19863161175618"></a><a name="p19863161175618"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row186331195618"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p48637117564"><a name="p48637117564"></a><a name="p48637117564"></a>EndPoint.4018</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p178631211125620"><a name="p178631211125620"></a><a name="p178631211125620"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p11863151115564"><a name="p11863151115564"></a><a name="p11863151115564"></a>Failed to add an extension router.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p20863141112563"><a name="p20863141112563"></a><a name="p20863141112563"></a>Failed to add the extended route.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p486313113562"><a name="p486313113562"></a><a name="p486313113562"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row108631211105619"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p4863181185611"><a name="p4863181185611"></a><a name="p4863181185611"></a>EndPoint.4019</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p108631011185614"><a name="p108631011185614"></a><a name="p108631011185614"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1686351165618"><a name="p1686351165618"></a><a name="p1686351165618"></a>Failed to delete the extension router.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p12863101145610"><a name="p12863101145610"></a><a name="p12863101145610"></a>Failed to delete the extended route.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p10864131165615"><a name="p10864131165615"></a><a name="p10864131165615"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row9864211195612"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p386491195614"><a name="p386491195614"></a><a name="p386491195614"></a>EndPoint.4020</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p8864101113569"><a name="p8864101113569"></a><a name="p8864101113569"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p5864121135611"><a name="p5864121135611"></a><a name="p5864121135611"></a>Failed to query Neutron L3 Agent.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p128641211165612"><a name="p128641211165612"></a><a name="p128641211165612"></a>Failed to query Neutron L3 Agent.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1686412114560"><a name="p1686412114560"></a><a name="p1686412114560"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row1086419118566"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p686419113567"><a name="p686419113567"></a><a name="p686419113567"></a>EndPoint.4021</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p14864111185620"><a name="p14864111185620"></a><a name="p14864111185620"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1486418118563"><a name="p1486418118563"></a><a name="p1486418118563"></a>Neutron L3 Agent is not found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1286581155618"><a name="p1286581155618"></a><a name="p1286581155618"></a>Neutron L3 Agent is not found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p2086591155617"><a name="p2086591155617"></a><a name="p2086591155617"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row1186541185618"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p12865191110565"><a name="p12865191110565"></a><a name="p12865191110565"></a>EndPoint.4025</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p686518114568"><a name="p686518114568"></a><a name="p686518114568"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1486511114567"><a name="p1486511114567"></a><a name="p1486511114567"></a>The specification is being used.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1386521119565"><a name="p1386521119565"></a><a name="p1386521119565"></a>The specification is being used.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p28651611175614"><a name="p28651611175614"></a><a name="p28651611175614"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row168651411185612"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p15865181118562"><a name="p15865181118562"></a><a name="p15865181118562"></a>EndPoint.4026</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p14866161114568"><a name="p14866161114568"></a><a name="p14866161114568"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p386611105619"><a name="p386611105619"></a><a name="p386611105619"></a>Failed to query the default route table of the VPC.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p2086671135616"><a name="p2086671135616"></a><a name="p2086671135616"></a>Failed to query the default route table of the VPC.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p14866141120563"><a name="p14866141120563"></a><a name="p14866141120563"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row148661411155617"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p13866121185615"><a name="p13866121185615"></a><a name="p13866121185615"></a>EndPoint.4027</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p38666117569"><a name="p38666117569"></a><a name="p38666117569"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p5866711105613"><a name="p5866711105613"></a><a name="p5866711105613"></a>Failed to query route tables of the VPC.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p98661311135614"><a name="p98661311135614"></a><a name="p98661311135614"></a>Failed to query route tables of the VPC.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p18661311175614"><a name="p18661311175614"></a><a name="p18661311175614"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row1866171125610"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p28671911175618"><a name="p28671911175618"></a><a name="p28671911175618"></a>EndPoint.4028</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p11867141145619"><a name="p11867141145619"></a><a name="p11867141145619"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p11867181185617"><a name="p11867181185617"></a><a name="p11867181185617"></a>Failed to add routes to the VPC's route table.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p15867171115616"><a name="p15867171115616"></a><a name="p15867171115616"></a>Failed to add routes to the VPC's route table.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p5867141135620"><a name="p5867141135620"></a><a name="p5867141135620"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row1886701114561"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p486711125616"><a name="p486711125616"></a><a name="p486711125616"></a>EndPoint.4029</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p5867911115613"><a name="p5867911115613"></a><a name="p5867911115613"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p19868911175614"><a name="p19868911175614"></a><a name="p19868911175614"></a>Failed to remove routes from the VPC's route table.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p68681111195614"><a name="p68681111195614"></a><a name="p68681111195614"></a>Failed to remove routes from the VPC's route table.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p38682118567"><a name="p38682118567"></a><a name="p38682118567"></a>Contact customer service.</p>
</td>
</tr>
<tr id="row13868611125615"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1286891175620"><a name="p1286891175620"></a><a name="p1286891175620"></a>EndPoint.4030</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p28683119564"><a name="p28683119564"></a><a name="p28683119564"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p486811120564"><a name="p486811120564"></a><a name="p486811120564"></a>The route table is not found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p138681011205616"><a name="p138681011205616"></a><a name="p138681011205616"></a>The route table is not found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p20868511205612"><a name="p20868511205612"></a><a name="p20868511205612"></a>Contact customer service.</p>
</td>
</tr>
</tbody>
</table>

