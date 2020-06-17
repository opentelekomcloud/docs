# Adding Monitoring Data<a name="EN-US_TOPIC_0171212551"></a>

## Function<a name="section66578044"></a>

This API is used to add one or more pieces of custom metric monitoring data to solve the problem that the system metrics cannot meet specific service requirements.

## URI<a name="section62331491"></a>

POST /V1.0/\{project\_id\}/metric-data

-   Parameter description

    **Table  1**  Parameter description

    <a name="table75058417558"></a>
    <table><thead align="left"><tr id="row6325008217558"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.1"><p id="p2298303317558"><a name="p2298303317558"></a><a name="p2298303317558"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.2"><p id="p4968641317558"><a name="p4968641317558"></a><a name="p4968641317558"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="p6517651717558"><a name="p6517651717558"></a><a name="p6517651717558"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4480653817558"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p545094717558"><a name="p545094717558"></a><a name="p545094717558"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p3887356117558"><a name="p3887356117558"></a><a name="p3887356117558"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p6175070717558"><a name="p6175070717558"></a><a name="p6175070717558"></a>Specifies the project ID.</p>
    <p id="p92930451060"><a name="p92930451060"></a><a name="p92930451060"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example

    ```
    POST https://{Cloud Eye endpoint}/V1.0/{project_id}/metric-data
    ```


## Request<a name="section24112512"></a>

>![](/images/icon-notice.gif) **NOTICE:**   
>1.  The size of a POST request cannot exceed 512 KB. Otherwise, the request will be denied.  
>2.  The period for sending POST requests must be shorter than the minimum aggregation period. Otherwise, the aggregated data will be noncontinuous. For example, if the aggregation period is 5 minutes and the POST request sending period is 7 minutes, the data will be aggregated every 10 minutes, rather than 5 minutes.  
>3.  Timestamp \(collect\_time\) in the POST request body value must be within the period that starts from three days before the current time to 10 minutes after the current time. If it is not in this range, you are not allowed to insert the metric data.  

-   Request parameters

    **Table  2**  Request parameters

    <a name="table124974516419"></a>
    <table><thead align="left"><tr id="row1825013456412"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="p925017459411"><a name="p925017459411"></a><a name="p925017459411"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p52506451146"><a name="p52506451146"></a><a name="p52506451146"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p42501745342"><a name="p42501745342"></a><a name="p42501745342"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.2.5.1.4"><p id="p32500450417"><a name="p32500450417"></a><a name="p32500450417"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row142508450418"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p1825054519412"><a name="p1825054519412"></a><a name="p1825054519412"></a>metric</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p925020451849"><a name="p925020451849"></a><a name="p925020451849"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p49891519102019"><a name="p49891519102019"></a><a name="p49891519102019"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p62501845547"><a name="p62501845547"></a><a name="p62501845547"></a>Specifies the metric data.</p>
    <p id="p757315414114"><a name="p757315414114"></a><a name="p757315414114"></a>For details, see <a href="#table1358724013016">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row6252445249"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p325211451143"><a name="p325211451143"></a><a name="p325211451143"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p725217453412"><a name="p725217453412"></a><a name="p725217453412"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p198667263364"><a name="p198667263364"></a><a name="p198667263364"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p92521245643"><a name="p92521245643"></a><a name="p92521245643"></a>Specifies the data validity period. The unit is second. The value range is 0–604,800 seconds. If the validity period expires, the data will be automatically deleted.</p>
    </td>
    </tr>
    <tr id="row14252545341"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p16252145748"><a name="p16252145748"></a><a name="p16252145748"></a>collect_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p6252134510413"><a name="p6252134510413"></a><a name="p6252134510413"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p132525451649"><a name="p132525451649"></a><a name="p132525451649"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p142520451146"><a name="p142520451146"></a><a name="p142520451146"></a>Specifies the time when the data was collected.</p>
    <p id="p11252045643"><a name="p11252045643"></a><a name="p11252045643"></a>The time is UNIX timestamp (ms) format.</p>
    <div class="note" id="note72522451848"><a name="note72522451848"></a><a name="note72522451848"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p62525452414"><a name="p62525452414"></a><a name="p62525452414"></a>Since there is a latency between the client and the server, the data timestamp to be inserted should be within the period that starts from three days before the current time plus 20s to 10 minutes after the current time minus 20s. In this way, the timestamp will be inserted to the database without being affected by the latency.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row82526458420"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p11252945941"><a name="p11252945941"></a><a name="p11252945941"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p32521245843"><a name="p32521245843"></a><a name="p32521245843"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p107881698215"><a name="p107881698215"></a><a name="p107881698215"></a>Integer or Float</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p112529450419"><a name="p112529450419"></a><a name="p112529450419"></a>Specifies the monitoring metric data to be added.</p>
    <p id="p14689184267"><a name="p14689184267"></a><a name="p14689184267"></a>The value can be an integer or a floating point number.</p>
    </td>
    </tr>
    <tr id="row72524454419"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p1925212451441"><a name="p1925212451441"></a><a name="p1925212451441"></a>unit</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p1925234516418"><a name="p1925234516418"></a><a name="p1925234516418"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p92521045346"><a name="p92521045346"></a><a name="p92521045346"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p2252545548"><a name="p2252545548"></a><a name="p2252545548"></a>Specifies the data unit.</p>
    <p id="p5929525131315"><a name="p5929525131315"></a><a name="p5929525131315"></a>Enter a maximum of 32 characters.</p>
    </td>
    </tr>
    <tr id="row32534451641"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p14253114513412"><a name="p14253114513412"></a><a name="p14253114513412"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p1225314513411"><a name="p1225314513411"></a><a name="p1225314513411"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p42536458417"><a name="p42536458417"></a><a name="p42536458417"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p1620828161212"><a name="p1620828161212"></a><a name="p1620828161212"></a>The value can be any of the following:</p>
    <a name="ul1019119128130"></a><a name="ul1019119128130"></a><ul id="ul1019119128130"><li>int</li><li>float</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **metric**  field data structure description

    <a name="table1358724013016"></a>
    <table><thead align="left"><tr id="row9586104013016"><th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.1"><p id="p1858674016307"><a name="p1858674016307"></a><a name="p1858674016307"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.2"><p id="p15871112813714"><a name="p15871112813714"></a><a name="p15871112813714"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="p1958684013306"><a name="p1958684013306"></a><a name="p1958684013306"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.57575757575757%" id="mcps1.2.5.1.4"><p id="p16586840173017"><a name="p16586840173017"></a><a name="p16586840173017"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row058694020301"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.1 "><p id="p1458611403306"><a name="p1458611403306"></a><a name="p1458611403306"></a>namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p1787192893717"><a name="p1787192893717"></a><a name="p1787192893717"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p19586174017307"><a name="p19586174017307"></a><a name="p19586174017307"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.57575757575757%" headers="mcps1.2.5.1.4 "><p id="p12933146104119"><a name="p12933146104119"></a><a name="p12933146104119"></a>Specifies the customized namespace. For example, see <a href="ecs-metrics.md#en-us_topic_0022067719_section24282572112133">Namespace</a> for the customized namespace of an ECS.</p>
    <p id="p17148866184830"><a name="p17148866184830"></a><a name="p17148866184830"></a>The value must be in the <strong id="b1914217271041"><a name="b1914217271041"></a><a name="b1914217271041"></a>service.item</strong> format and can contain 3 to 32 characters. <strong id="b181444271645"><a name="b181444271645"></a><a name="b181444271645"></a>service</strong> and <strong id="b19145112711415"><a name="b19145112711415"></a><a name="b19145112711415"></a>item</strong> must be a string that starts with a letter and contains only uppercase letters, lowercase letters, digits, and underscores (_). In addition, <strong id="b842352706142346"><a name="b842352706142346"></a><a name="b842352706142346"></a>service</strong> cannot start with <strong id="b842352706195554"><a name="b842352706195554"></a><a name="b842352706195554"></a>SYS</strong> and <strong id="b1439514211911"><a name="b1439514211911"></a><a name="b1439514211911"></a>AGT</strong>.</p>
    <p id="p1767864611103"><a name="p1767864611103"></a><a name="p1767864611103"></a><strong id="b84235270618543"><a name="b84235270618543"></a><a name="b84235270618543"></a>namespace</strong> cannot be <strong id="b842352706185412"><a name="b842352706185412"></a><a name="b842352706185412"></a>SERVICE.BMS</strong>.</p>
    </td>
    </tr>
    <tr id="row35879403303"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.1 "><p id="p75865406307"><a name="p75865406307"></a><a name="p75865406307"></a>dimensions</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p687112817373"><a name="p687112817373"></a><a name="p687112817373"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p1396413334224"><a name="p1396413334224"></a><a name="p1396413334224"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.57575757575757%" headers="mcps1.2.5.1.4 "><p id="p55861740143019"><a name="p55861740143019"></a><a name="p55861740143019"></a>Specifies the list of the metric dimensions.</p>
    <p id="p9586154053018"><a name="p9586154053018"></a><a name="p9586154053018"></a>For details, see <a href="#table15589124016303">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row15171713175610"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.1 "><p id="p13623999153639"><a name="p13623999153639"></a><a name="p13623999153639"></a>metric_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p1627183516576"><a name="p1627183516576"></a><a name="p1627183516576"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p136841954153011"><a name="p136841954153011"></a><a name="p136841954153011"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.57575757575757%" headers="mcps1.2.5.1.4 "><p id="p686919215492"><a name="p686919215492"></a><a name="p686919215492"></a>Specifies the metric ID. For example, if the <a href="ecs-metrics.md">monitoring metric</a> of an ECS is CPU usage, <strong id="b1181918246126"><a name="b1181918246126"></a><a name="b1181918246126"></a>metric_name</strong> is <strong id="b1482272421216"><a name="b1482272421216"></a><a name="b1482272421216"></a>cpu_util</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **dimensions**  field data structure description

    <a name="table15589124016303"></a>
    <table><thead align="left"><tr id="row95871840183019"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="p155871640123019"><a name="p155871640123019"></a><a name="p155871640123019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p2844544133711"><a name="p2844544133711"></a><a name="p2844544133711"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p758714013304"><a name="p758714013304"></a><a name="p758714013304"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="p1958714018307"><a name="p1958714018307"></a><a name="p1958714018307"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3588194053014"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p9588164019308"><a name="p9588164019308"></a><a name="p9588164019308"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p18844174473710"><a name="p18844174473710"></a><a name="p18844174473710"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p858811407301"><a name="p858811407301"></a><a name="p858811407301"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p19551520125012"><a name="p19551520125012"></a><a name="p19551520125012"></a>Specifies the monitoring dimension. For example, the monitoring dimension of an ECS is <strong id="b8659197317"><a name="b8659197317"></a><a name="b8659197317"></a>instance_id</strong>, which is listed in the <strong id="b12651352193114"><a name="b12651352193114"></a><a name="b12651352193114"></a>key</strong> column in <a href="ecs-metrics.md#en-us_topic_0022067719_section36963297112133">Dimension</a>.</p>
    <p id="p3963077184830"><a name="p3963077184830"></a><a name="p3963077184830"></a>The value can be a string of 1 to 32 characters and must start with a letter and contain only uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row6589124015301"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p19588184023011"><a name="p19588184023011"></a><a name="p19588184023011"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p198441544173718"><a name="p198441544173718"></a><a name="p198441544173718"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p1118310411206"><a name="p1118310411206"></a><a name="p1118310411206"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p11371113251615"><a name="p11371113251615"></a><a name="p11371113251615"></a>Specifies the dimension value, for example, an ECS ID.</p>
    <p id="p91691546145115"><a name="p91691546145115"></a><a name="p91691546145115"></a>The value can be a string of 1 to 256 characters and must start with a letter or a digit and contain only uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    [
        {
            "metric": {
                "namespace": "MINE.APP",
                "dimensions": [
                    {
                        "name": "instance_id",
                        "value": "33328f02-3814-422e-b688-bfdba93d4050"
                    }
                ],
                "metric_name": "cpu_util"
            },
            "ttl": 172800,
            "collect_time": 1463598260000,
            "type": "int",
            "value": 60,
            "unit": "%"
        },
        {
            "metric": {
                "namespace": "MINE.APP",
                "dimensions": [
                    {
                        "name": "instance_id",
                        "value": "33328f02-3814-422e-b688-bfdba93d4050"
                    }
                ],
                "metric_name": "cpu_util"
            },
            "ttl": 172800,
            "collect_time": 1463598270000,
            "type": "int",
            "value": 70,
            "unit": "%"
        }
    ]
    ```


## Response<a name="section15686020"></a>

The response has no message body.

## Returned Values<a name="section6956456"></a>

-   Normal

    201

-   Abnormal

    <a name="table46793998"></a>
    <table><thead align="left"><tr id="row65573909"><th class="cellrowborder" valign="top" width="32.519999999999996%" id="mcps1.1.3.1.1"><p id="p1849030182924"><a name="p1849030182924"></a><a name="p1849030182924"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="67.47999999999999%" id="mcps1.1.3.1.2"><p id="p15553712182924"><a name="p15553712182924"></a><a name="p15553712182924"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37564172"><td class="cellrowborder" valign="top" width="32.519999999999996%" headers="mcps1.1.3.1.1 "><p id="p581987519168"><a name="p581987519168"></a><a name="p581987519168"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.47999999999999%" headers="mcps1.1.3.1.2 "><p id="p164784039168"><a name="p164784039168"></a><a name="p164784039168"></a>Request error</p>
    </td>
    </tr>
    <tr id="row66248115"><td class="cellrowborder" valign="top" width="32.519999999999996%" headers="mcps1.1.3.1.1 "><p id="p2691669168"><a name="p2691669168"></a><a name="p2691669168"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.47999999999999%" headers="mcps1.1.3.1.2 "><p id="p218024949168"><a name="p218024949168"></a><a name="p218024949168"></a>The authentication information is not provided or is incorrect.</p>
    </td>
    </tr>
    <tr id="row44282627"><td class="cellrowborder" valign="top" width="32.519999999999996%" headers="mcps1.1.3.1.1 "><p id="p563264059168"><a name="p563264059168"></a><a name="p563264059168"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.47999999999999%" headers="mcps1.1.3.1.2 "><p id="p661449719168"><a name="p661449719168"></a><a name="p661449719168"></a>You are forbidden to access the page requested.</p>
    </td>
    </tr>
    <tr id="row1815156"><td class="cellrowborder" valign="top" width="32.519999999999996%" headers="mcps1.1.3.1.1 "><p id="p355199299168"><a name="p355199299168"></a><a name="p355199299168"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.47999999999999%" headers="mcps1.1.3.1.2 "><p id="p585420329168"><a name="p585420329168"></a><a name="p585420329168"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row25675773"><td class="cellrowborder" valign="top" width="32.519999999999996%" headers="mcps1.1.3.1.1 "><p id="p630127129168"><a name="p630127129168"></a><a name="p630127129168"></a>429 Too Many Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.47999999999999%" headers="mcps1.1.3.1.2 "><p id="p37560249168"><a name="p37560249168"></a><a name="p37560249168"></a>Concurrent requests are excessive.</p>
    </td>
    </tr>
    <tr id="row47530006"><td class="cellrowborder" valign="top" width="32.519999999999996%" headers="mcps1.1.3.1.1 "><p id="p537873819168"><a name="p537873819168"></a><a name="p537873819168"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.47999999999999%" headers="mcps1.1.3.1.2 "><p id="p618106189168"><a name="p618106189168"></a><a name="p618106189168"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row20561848"><td class="cellrowborder" valign="top" width="32.519999999999996%" headers="mcps1.1.3.1.1 "><p id="p298930079168"><a name="p298930079168"></a><a name="p298930079168"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.47999999999999%" headers="mcps1.1.3.1.2 "><p id="p54144829168"><a name="p54144829168"></a><a name="p54144829168"></a>The service is currently unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section172711834720"></a>

For details, see  [Error Codes](error-codes.md).

