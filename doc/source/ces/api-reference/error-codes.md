# Error Codes<a name="EN-US_TOPIC_0171212582"></a>

## Function<a name="section25523120121746"></a>

If an error occurs during API calling, the system returns error information. This section describes the error codes contained in the error information for Cloud Eye APIs.

## Example Response<a name="section3667181464912"></a>

```
{
    "code": 400,
    "element": "Bad Request",
    "message": "The system received a request which cannot be recognized",
    "details": {
        "details": "Some content in message body is not correct",
        "code": "ces.0014"
    }
}
```

## Glossary<a name="section30376965111542"></a>

<a name="table38187127111748"></a>
<table><thead align="left"><tr id="row53839319111748"><th class="cellrowborder" valign="top" width="21.19%" id="mcps1.1.3.1.1"><p id="p66017579111748"><a name="p66017579111748"></a><a name="p66017579111748"></a>Glossary</p>
</th>
<th class="cellrowborder" valign="top" width="78.81%" id="mcps1.1.3.1.2"><p id="p9760230111748"><a name="p9760230111748"></a><a name="p9760230111748"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1668748111748"><td class="cellrowborder" valign="top" width="21.19%" headers="mcps1.1.3.1.1 "><p id="p950866111748"><a name="p950866111748"></a><a name="p950866111748"></a>Cloud Eye</p>
</td>
<td class="cellrowborder" valign="top" width="78.81%" headers="mcps1.1.3.1.2 "><p id="p9911321111748"><a name="p9911321111748"></a><a name="p9911321111748"></a>Cloud Eye</p>
</td>
</tr>
<tr id="row22093028111748"><td class="cellrowborder" valign="top" width="21.19%" headers="mcps1.1.3.1.1 "><p id="p44704847111748"><a name="p44704847111748"></a><a name="p44704847111748"></a>Built-in metric</p>
</td>
<td class="cellrowborder" valign="top" width="78.81%" headers="mcps1.1.3.1.2 "><p id="p64322830111748"><a name="p64322830111748"></a><a name="p64322830111748"></a>Each service has its own built-in metrics and dimensions. For example, an ECS (SYS.ECS) supports <strong id="b842352706195535"><a name="b842352706195535"></a><a name="b842352706195535"></a>cpu_util</strong>.</p>
</td>
</tr>
<tr id="row42034561111748"><td class="cellrowborder" valign="top" width="21.19%" headers="mcps1.1.3.1.1 "><p id="p49356250111748"><a name="p49356250111748"></a><a name="p49356250111748"></a>Metric</p>
</td>
<td class="cellrowborder" valign="top" width="78.81%" headers="mcps1.1.3.1.2 "><p id="p38433275111748"><a name="p38433275111748"></a><a name="p38433275111748"></a>A metric consists of the namespace, dimension (optional), and metric name. A metric name solely does not identify any object.</p>
</td>
</tr>
</tbody>
</table>

## Error Code Description<a name="section4609164142111"></a>

<a name="table33042642142158"></a>
<table><thead align="left"><tr id="row21006729142158"><th class="cellrowborder" valign="top" width="14.78%" id="mcps1.1.7.1.1"><p id="p13084746142158"><a name="p13084746142158"></a><a name="p13084746142158"></a>Module</p>
</th>
<th class="cellrowborder" valign="top" width="9.78%" id="mcps1.1.7.1.2"><p id="p575417119349"><a name="p575417119349"></a><a name="p575417119349"></a>HTTP Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="12.55%" id="mcps1.1.7.1.3"><p id="p53231512142158"><a name="p53231512142158"></a><a name="p53231512142158"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="21.97%" id="mcps1.1.7.1.4"><p id="p16785255142158"><a name="p16785255142158"></a><a name="p16785255142158"></a>Error Code Description</p>
</th>
<th class="cellrowborder" valign="top" width="21.22%" id="mcps1.1.7.1.5"><p id="p172825543512"><a name="p172825543512"></a><a name="p172825543512"></a>Error Message</p>
</th>
<th class="cellrowborder" valign="top" width="19.7%" id="mcps1.1.7.1.6"><p id="p1688910019359"><a name="p1688910019359"></a><a name="p1688910019359"></a>Measure</p>
</th>
</tr>
</thead>
<tbody><tr id="row353022183618"><td class="cellrowborder" valign="top" width="14.78%" headers="mcps1.1.7.1.1 "><p id="p155301522365"><a name="p155301522365"></a><a name="p155301522365"></a>Cloud Eye</p>
</td>
<td class="cellrowborder" valign="top" width="9.78%" headers="mcps1.1.7.1.2 "><p id="p56004024717"><a name="p56004024717"></a><a name="p56004024717"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="12.55%" headers="mcps1.1.7.1.3 "><p id="p44512649143226"><a name="p44512649143226"></a><a name="p44512649143226"></a>ces.0007</p>
</td>
<td class="cellrowborder" valign="top" width="21.97%" headers="mcps1.1.7.1.4 "><p id="p48754816143226"><a name="p48754816143226"></a><a name="p48754816143226"></a>Internal service error</p>
</td>
<td class="cellrowborder" valign="top" width="21.22%" headers="mcps1.1.7.1.5 "><p id="p1493810734818"><a name="p1493810734818"></a><a name="p1493810734818"></a>Internal service error.</p>
</td>
<td class="cellrowborder" valign="top" width="19.7%" headers="mcps1.1.7.1.6 "><p id="p15960427204811"><a name="p15960427204811"></a><a name="p15960427204811"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row16849575142158"><td class="cellrowborder" rowspan="14" valign="top" width="14.78%" headers="mcps1.1.7.1.1 "><p id="p22638297142158"><a name="p22638297142158"></a><a name="p22638297142158"></a>API</p>
</td>
<td class="cellrowborder" valign="top" width="9.78%" headers="mcps1.1.7.1.2 "><p id="p660124018474"><a name="p660124018474"></a><a name="p660124018474"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12.55%" headers="mcps1.1.7.1.3 "><p id="p21762784142158"><a name="p21762784142158"></a><a name="p21762784142158"></a>ces.0001</p>
</td>
<td class="cellrowborder" valign="top" width="21.97%" headers="mcps1.1.7.1.4 "><p id="p22687134142618"><a name="p22687134142618"></a><a name="p22687134142618"></a>The request content cannot be empty.</p>
</td>
<td class="cellrowborder" valign="top" width="21.22%" headers="mcps1.1.7.1.5 "><p id="p1293817134819"><a name="p1293817134819"></a><a name="p1293817134819"></a>The content must be specified.</p>
</td>
<td class="cellrowborder" valign="top" width="19.7%" headers="mcps1.1.7.1.6 "><p id="p896019272481"><a name="p896019272481"></a><a name="p896019272481"></a>Specify the request content.</p>
</td>
</tr>
<tr id="row1056340914255"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p560104016472"><a name="p560104016472"></a><a name="p560104016472"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p5018127414255"><a name="p5018127414255"></a><a name="p5018127414255"></a>ces.0003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p3815136914255"><a name="p3815136914255"></a><a name="p3815136914255"></a>The project ID is left blank or is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p109393734816"><a name="p109393734816"></a><a name="p109393734816"></a>The tenant ID is left blank or incorrect.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p6960627204818"><a name="p6960627204818"></a><a name="p6960627204818"></a>Add or use the correct tenant ID.</p>
</td>
</tr>
<tr id="row32855085143145"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p360640174712"><a name="p360640174712"></a><a name="p360640174712"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p8547270143145"><a name="p8547270143145"></a><a name="p8547270143145"></a>ces.0004</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1745194611813"><a name="p1745194611813"></a><a name="p1745194611813"></a>The API version is not specified.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p199391079485"><a name="p199391079485"></a><a name="p199391079485"></a>The API version must be specified.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p1896092714813"><a name="p1896092714813"></a><a name="p1896092714813"></a>Specify the API version in the request URL.</p>
</td>
</tr>
<tr id="row12253599143223"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p860144024711"><a name="p860144024711"></a><a name="p860144024711"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p66557662143223"><a name="p66557662143223"></a><a name="p66557662143223"></a>ces.0005</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p22461505143223"><a name="p22461505143223"></a><a name="p22461505143223"></a>The API version is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p893917134811"><a name="p893917134811"></a><a name="p893917134811"></a>The API version is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p1960627124812"><a name="p1960627124812"></a><a name="p1960627124812"></a>Use the correct API version.</p>
</td>
</tr>
<tr id="row65348213143230"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p206084013471"><a name="p206084013471"></a><a name="p206084013471"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p58204324143230"><a name="p58204324143230"></a><a name="p58204324143230"></a>ces.0006</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p16929774143230"><a name="p16929774143230"></a><a name="p16929774143230"></a>The paging address is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p29395784810"><a name="p29395784810"></a><a name="p29395784810"></a>The paging address is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p1960627204814"><a name="p1960627204814"></a><a name="p1960627204814"></a>Use the correct paging information.</p>
</td>
</tr>
<tr id="row13209931143347"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p2606407470"><a name="p2606407470"></a><a name="p2606407470"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p32816955143347"><a name="p32816955143347"></a><a name="p32816955143347"></a>ces.0009</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p8532158153917"><a name="p8532158153917"></a><a name="p8532158153917"></a>System metrics cannot be added.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1893910774816"><a name="p1893910774816"></a><a name="p1893910774816"></a>Adding SYS metric is not allowed</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p16960172716481"><a name="p16960172716481"></a><a name="p16960172716481"></a>Use correct rights to add metrics.</p>
</td>
</tr>
<tr id="row1156884234019"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p166115407477"><a name="p166115407477"></a><a name="p166115407477"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p143906054119"><a name="p143906054119"></a><a name="p143906054119"></a>ces.0010</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p16391110124112"><a name="p16391110124112"></a><a name="p16391110124112"></a>System metrics cannot be deleted.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p18939177134819"><a name="p18939177134819"></a><a name="p18939177134819"></a>Deleting SYS metric is not allowed</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p1396052718485"><a name="p1396052718485"></a><a name="p1396052718485"></a>Use correct rights to delete metrics.</p>
</td>
</tr>
<tr id="row49855628143351"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p9614409470"><a name="p9614409470"></a><a name="p9614409470"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p14174132143351"><a name="p14174132143351"></a><a name="p14174132143351"></a>ces.0011</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p7254053143351"><a name="p7254053143351"></a><a name="p7254053143351"></a>The request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p3939478482"><a name="p3939478482"></a><a name="p3939478482"></a>The request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p18961827144813"><a name="p18961827144813"></a><a name="p18961827144813"></a>Check the request.</p>
</td>
</tr>
<tr id="row28605787143358"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p961124017477"><a name="p961124017477"></a><a name="p961124017477"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p46188056143358"><a name="p46188056143358"></a><a name="p46188056143358"></a>ces.0013</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p50245041143358"><a name="p50245041143358"></a><a name="p50245041143358"></a>The URL parameter is invalid or does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p20939117184818"><a name="p20939117184818"></a><a name="p20939117184818"></a>The URL parameter is invalid or does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p49611827194811"><a name="p49611827194811"></a><a name="p49611827194811"></a>Check the URL parameter.</p>
</td>
</tr>
<tr id="row35555210422"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p5611640174720"><a name="p5611640174720"></a><a name="p5611640174720"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p78637141424"><a name="p78637141424"></a><a name="p78637141424"></a>ces.0014</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1686421419422"><a name="p1686421419422"></a><a name="p1686421419422"></a>Some content in the message body is correct.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1893912710480"><a name="p1893912710480"></a><a name="p1893912710480"></a>Some content in message body is not correct.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p1396192718489"><a name="p1396192718489"></a><a name="p1396192718489"></a>Check the request body parameters.</p>
</td>
</tr>
<tr id="row8263357143623"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p1361840204719"><a name="p1361840204719"></a><a name="p1361840204719"></a>401</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p59038500143623"><a name="p59038500143623"></a><a name="p59038500143623"></a>ces.0015</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p17389180143623"><a name="p17389180143623"></a><a name="p17389180143623"></a>Authentication fails or invalid authentication information is not provided.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p29392717485"><a name="p29392717485"></a><a name="p29392717485"></a>Authentication fails or the authentication information is not provided.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p13961427144813"><a name="p13961427144813"></a><a name="p13961427144813"></a>Check whether the user name or password (or AK or SK) for obtaining the token is correct.</p>
</td>
</tr>
<tr id="row46563482143714"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p661164018475"><a name="p661164018475"></a><a name="p661164018475"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p23456691143714"><a name="p23456691143714"></a><a name="p23456691143714"></a>ces.0016</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p20943847143714"><a name="p20943847143714"></a><a name="p20943847143714"></a>The requested resource does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p593917717487"><a name="p593917717487"></a><a name="p593917717487"></a>The requested resource does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p396132712488"><a name="p396132712488"></a><a name="p396132712488"></a>Check whether the requested resource exists.</p>
</td>
</tr>
<tr id="row52300053143723"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p661134010479"><a name="p661134010479"></a><a name="p661134010479"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p13027446143723"><a name="p13027446143723"></a><a name="p13027446143723"></a>ces.0017</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p48590207143723"><a name="p48590207143723"></a><a name="p48590207143723"></a>The authentication information is incorrect or the service invoker does not have sufficient rights.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p12939076484"><a name="p12939076484"></a><a name="p12939076484"></a>The authentication information is incorrect or the service invoker does not have sufficient rights.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p1696114279488"><a name="p1696114279488"></a><a name="p1696114279488"></a>Check whether the user name or password (or AK or SK) or the user rights for obtaining the token are correct.</p>
</td>
</tr>
<tr id="row59921212143928"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p196118400478"><a name="p196118400478"></a><a name="p196118400478"></a>429</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p19351246143928"><a name="p19351246143928"></a><a name="p19351246143928"></a>ces.0020</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p23947055143928"><a name="p23947055143928"></a><a name="p23947055143928"></a>The number of requests exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p129401272483"><a name="p129401272483"></a><a name="p129401272483"></a>The number of requests exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p1796122712488"><a name="p1796122712488"></a><a name="p1796122712488"></a>Reduce the numbers of requests.</p>
</td>
</tr>
<tr id="row15706154718422"><td class="cellrowborder" valign="top" width="14.78%" headers="mcps1.1.7.1.1 "><p id="p28791253164214"><a name="p28791253164214"></a><a name="p28791253164214"></a>Cassandra</p>
</td>
<td class="cellrowborder" valign="top" width="9.78%" headers="mcps1.1.7.1.2 "><p id="p1287919535426"><a name="p1287919535426"></a><a name="p1287919535426"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="12.55%" headers="mcps1.1.7.1.3 "><p id="p17880195319429"><a name="p17880195319429"></a><a name="p17880195319429"></a>ces.0008</p>
</td>
<td class="cellrowborder" valign="top" width="21.97%" headers="mcps1.1.7.1.4 "><p id="p1788015536421"><a name="p1788015536421"></a><a name="p1788015536421"></a>Database error</p>
</td>
<td class="cellrowborder" valign="top" width="21.22%" headers="mcps1.1.7.1.5 "><p id="p1888015318426"><a name="p1888015318426"></a><a name="p1888015318426"></a>Database error.</p>
</td>
<td class="cellrowborder" valign="top" width="19.7%" headers="mcps1.1.7.1.6 "><p id="p588016539425"><a name="p588016539425"></a><a name="p588016539425"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row985164210391"><td class="cellrowborder" valign="top" width="14.78%" headers="mcps1.1.7.1.1 "><p id="p789393516460"><a name="p789393516460"></a><a name="p789393516460"></a>Kafka</p>
</td>
<td class="cellrowborder" valign="top" width="9.78%" headers="mcps1.1.7.1.2 "><p id="p1589316357461"><a name="p1589316357461"></a><a name="p1589316357461"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="12.55%" headers="mcps1.1.7.1.3 "><p id="p1289373516465"><a name="p1289373516465"></a><a name="p1289373516465"></a>ces.0012</p>
</td>
<td class="cellrowborder" valign="top" width="21.97%" headers="mcps1.1.7.1.4 "><p id="p789311354464"><a name="p789311354464"></a><a name="p789311354464"></a>The message queue is abnormal or is not ready.</p>
</td>
<td class="cellrowborder" valign="top" width="21.22%" headers="mcps1.1.7.1.5 "><p id="p18893123514616"><a name="p18893123514616"></a><a name="p18893123514616"></a>The message queue is abnormal or is not ready.</p>
</td>
<td class="cellrowborder" valign="top" width="19.7%" headers="mcps1.1.7.1.6 "><p id="p089316357463"><a name="p089316357463"></a><a name="p089316357463"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row44741232174314"><td class="cellrowborder" valign="top" width="14.78%" headers="mcps1.1.7.1.1 "><p id="p18156145954318"><a name="p18156145954318"></a><a name="p18156145954318"></a>Zookeeper</p>
</td>
<td class="cellrowborder" valign="top" width="9.78%" headers="mcps1.1.7.1.2 "><p id="p7156145917436"><a name="p7156145917436"></a><a name="p7156145917436"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="12.55%" headers="mcps1.1.7.1.3 "><p id="p315685964317"><a name="p315685964317"></a><a name="p315685964317"></a>ces.0021</p>
</td>
<td class="cellrowborder" valign="top" width="21.97%" headers="mcps1.1.7.1.4 "><p id="p6156459184319"><a name="p6156459184319"></a><a name="p6156459184319"></a>Internal locking error</p>
</td>
<td class="cellrowborder" valign="top" width="21.22%" headers="mcps1.1.7.1.5 "><p id="p12156659204311"><a name="p12156659204311"></a><a name="p12156659204311"></a>Internal locking error</p>
</td>
<td class="cellrowborder" valign="top" width="19.7%" headers="mcps1.1.7.1.6 "><p id="p71568590430"><a name="p71568590430"></a><a name="p71568590430"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row1235124616434"><td class="cellrowborder" valign="top" width="14.78%" headers="mcps1.1.7.1.1 "><p id="p1031718161466"><a name="p1031718161466"></a><a name="p1031718161466"></a>Blueflood</p>
</td>
<td class="cellrowborder" valign="top" width="9.78%" headers="mcps1.1.7.1.2 "><p id="p5317181614618"><a name="p5317181614618"></a><a name="p5317181614618"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="12.55%" headers="mcps1.1.7.1.3 "><p id="p10317151634612"><a name="p10317151634612"></a><a name="p10317151634612"></a>ces.0019</p>
</td>
<td class="cellrowborder" valign="top" width="21.97%" headers="mcps1.1.7.1.4 "><p id="p1731731617466"><a name="p1731731617466"></a><a name="p1731731617466"></a>The metric processing engine is abnormal.</p>
</td>
<td class="cellrowborder" valign="top" width="21.22%" headers="mcps1.1.7.1.5 "><p id="p031731613469"><a name="p031731613469"></a><a name="p031731613469"></a>The metric processing engine is abnormal.</p>
</td>
<td class="cellrowborder" valign="top" width="19.7%" headers="mcps1.1.7.1.6 "><p id="p931761674617"><a name="p931761674617"></a><a name="p931761674617"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row595818424432"><td class="cellrowborder" rowspan="3" valign="top" width="14.78%" headers="mcps1.1.7.1.1 "><p id="p665612310453"><a name="p665612310453"></a><a name="p665612310453"></a>Alarm</p>
</td>
<td class="cellrowborder" valign="top" width="9.78%" headers="mcps1.1.7.1.2 "><p id="p1075512112340"><a name="p1075512112340"></a><a name="p1075512112340"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="12.55%" headers="mcps1.1.7.1.3 "><p id="p45368459142158"><a name="p45368459142158"></a><a name="p45368459142158"></a>ces.0002</p>
</td>
<td class="cellrowborder" valign="top" width="21.97%" headers="mcps1.1.7.1.4 "><p id="p50966590142158"><a name="p50966590142158"></a><a name="p50966590142158"></a>The alarm ID cannot be left blank.</p>
</td>
<td class="cellrowborder" valign="top" width="21.22%" headers="mcps1.1.7.1.5 "><p id="p11159145984513"><a name="p11159145984513"></a><a name="p11159145984513"></a>The alarm ID must be specified.</p>
</td>
<td class="cellrowborder" valign="top" width="19.7%" headers="mcps1.1.7.1.6 "><p id="p91596595458"><a name="p91596595458"></a><a name="p91596595458"></a>Specify the alarm ID.</p>
</td>
</tr>
<tr id="row171871058154410"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p185951010154516"><a name="p185951010154516"></a><a name="p185951010154516"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p55951010184512"><a name="p55951010184512"></a><a name="p55951010184512"></a>ces.0018</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1259591044517"><a name="p1259591044517"></a><a name="p1259591044517"></a>The number of alarm rules created exceeds the quota.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1459531034512"><a name="p1459531034512"></a><a name="p1459531034512"></a>The number of alarms exceeds the quota</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p1459511108456"><a name="p1459511108456"></a><a name="p1459511108456"></a>Apply for a higher alarm quota.</p>
</td>
</tr>
<tr id="row290655114420"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p55951010194519"><a name="p55951010194519"></a><a name="p55951010194519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p18595310134513"><a name="p18595310134513"></a><a name="p18595310134513"></a>ces.0028</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p959513109453"><a name="p959513109453"></a><a name="p959513109453"></a>The metric and notification type do not match when an alarm rule is created.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p19596810174518"><a name="p19596810174518"></a><a name="p19596810174518"></a>The metric does not support the alarm action type.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p1359619106454"><a name="p1359619106454"></a><a name="p1359619106454"></a>Modify the metric or notification type according to the parameter description to make them match.</p>
</td>
</tr>
</tbody>
</table>

