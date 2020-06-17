# Querying the Host Configuration<a name="EN-US_TOPIC_0171212559"></a>

## Function<a name="section66578044"></a>

This API is used to query the host configuration for a specified event type in a specified period of time. You can specify the dimension of data to be queried.

>![](/images/icon-notice.gif) **NOTICE:**   
>This API is provided for SAP Monitor in the HANA scenario to query the host configuration. In other scenarios, the host configuration cannot be queried with this API.  

## URI<a name="section5658454014325"></a>

GET /V1.0/\{project\_id\}/event-data

-   Parameter description

    **Table  1**  Parameter description

    <a name="table75058417558"></a>
    <table><thead align="left"><tr id="row6325008217558"><th class="cellrowborder" valign="top" width="18.3%" id="mcps1.2.4.1.1"><p id="p2298303317558"><a name="p2298303317558"></a><a name="p2298303317558"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.4.1.2"><p id="p4968641317558"><a name="p4968641317558"></a><a name="p4968641317558"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.34%" id="mcps1.2.4.1.3"><p id="p6517651717558"><a name="p6517651717558"></a><a name="p6517651717558"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4480653817558"><td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.1 "><p id="p545094717558"><a name="p545094717558"></a><a name="p545094717558"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p3887356117558"><a name="p3887356117558"></a><a name="p3887356117558"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.34%" headers="mcps1.2.4.1.3 "><p id="p6175070717558"><a name="p6175070717558"></a><a name="p6175070717558"></a>Specifies the project ID.</p>
    <p id="p131101257568"><a name="p131101257568"></a><a name="p131101257568"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameters that are used to query the host configuration

    <a name="table35416756"></a>
    <table><thead align="left"><tr id="row27598891"><th class="cellrowborder" valign="top" width="18.61%" id="mcps1.1.5.1.1"><p id="p20917673"><a name="p20917673"></a><a name="p20917673"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.1%" id="mcps1.1.5.1.2"><p id="p16609919"><a name="p16609919"></a><a name="p16609919"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.54%" id="mcps1.1.5.1.3"><p id="p29058925163547"><a name="p29058925163547"></a><a name="p29058925163547"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.75%" id="mcps1.1.5.1.4"><p id="p3226198"><a name="p3226198"></a><a name="p3226198"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59995477"><td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.1.5.1.1 "><p id="p3900147595641"><a name="p3900147595641"></a><a name="p3900147595641"></a>namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.1.5.1.2 "><p id="p500289695641"><a name="p500289695641"></a><a name="p500289695641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.3 "><p id="p667393162913"><a name="p667393162913"></a><a name="p667393162913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.75%" headers="mcps1.1.5.1.4 "><p id="p12933146104119"><a name="p12933146104119"></a><a name="p12933146104119"></a>Query the namespace of a service. For example, see <a href="ecs-metrics.md#en-us_topic_0022067719_section24282572112133">Namespace</a> for ECS namespace.</p>
    <p id="p1529914911223"><a name="p1529914911223"></a><a name="p1529914911223"></a>The value must be in the <strong id="b1127311121319"><a name="b1127311121319"></a><a name="b1127311121319"></a>service.item</strong> format and can contain 3 to 32 characters. <strong id="b1627421161313"><a name="b1627421161313"></a><a name="b1627421161313"></a>service</strong> and <strong id="b4274121115131"><a name="b4274121115131"></a><a name="b4274121115131"></a>item</strong> must be a string that starts with a letter and contains only uppercase letters, lowercase letters, digits, and underscores (_).</p>
    </td>
    </tr>
    <tr id="row14620943"><td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.1.5.1.1 "><p id="p36641520143355"><a name="p36641520143355"></a><a name="p36641520143355"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.1.5.1.2 "><p id="p2566588195641"><a name="p2566588195641"></a><a name="p2566588195641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.3 "><p id="p66435433163547"><a name="p66435433163547"></a><a name="p66435433163547"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.75%" headers="mcps1.1.5.1.4 "><p id="p15720316165828"><a name="p15720316165828"></a><a name="p15720316165828"></a>Specifies the event type.</p>
    <p id="p7013114145729"><a name="p7013114145729"></a><a name="p7013114145729"></a>It can contain only letters, underscores (_), and hyphens (-). It must start with a letter and cannot exceed 64 characters, for example, <strong id="b842352706165359"><a name="b842352706165359"></a><a name="b842352706165359"></a>instance_host_info</strong>.</p>
    </td>
    </tr>
    <tr id="row55056607"><td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.1.5.1.1 "><p id="p2518324095641"><a name="p2518324095641"></a><a name="p2518324095641"></a>from</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.1.5.1.2 "><p id="p2657653695641"><a name="p2657653695641"></a><a name="p2657653695641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.3 "><p id="p829483813299"><a name="p829483813299"></a><a name="p829483813299"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.75%" headers="mcps1.1.5.1.4 "><p id="p50729725153619"><a name="p50729725153619"></a><a name="p50729725153619"></a>Specifies the start time of the query.</p>
    <p id="p58158650145729"><a name="p58158650145729"></a><a name="p58158650145729"></a>The value is a UNIX timestamp and the unit is ms.</p>
    </td>
    </tr>
    <tr id="row6114302"><td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.1.5.1.1 "><p id="p4423458695641"><a name="p4423458695641"></a><a name="p4423458695641"></a>to</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.1.5.1.2 "><p id="p2623169995641"><a name="p2623169995641"></a><a name="p2623169995641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.3 "><p id="p141569412294"><a name="p141569412294"></a><a name="p141569412294"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.75%" headers="mcps1.1.5.1.4 "><p id="p37722762154851"><a name="p37722762154851"></a><a name="p37722762154851"></a>Specifies the end time of the query.</p>
    <p id="p12358701154859"><a name="p12358701154859"></a><a name="p12358701154859"></a>The value is a UNIX timestamp and the unit is ms.</p>
    <p id="p4386413145729"><a name="p4386413145729"></a><a name="p4386413145729"></a>The value of parameter <strong id="b10781660165741"><a name="b10781660165741"></a><a name="b10781660165741"></a>from</strong> must be earlier than that of parameter <strong id="b29926084165741"><a name="b29926084165741"></a><a name="b29926084165741"></a>to</strong>.</p>
    </td>
    </tr>
    <tr id="row6189824095632"><td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.1.5.1.1 "><p id="p6296468095641"><a name="p6296468095641"></a><a name="p6296468095641"></a>dim</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.1.5.1.2 "><p id="p6697434595641"><a name="p6697434595641"></a><a name="p6697434595641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.3 "><p id="p59844053163547"><a name="p59844053163547"></a><a name="p59844053163547"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.75%" headers="mcps1.1.5.1.4 "><p id="p132891013125316"><a name="p132891013125316"></a><a name="p132891013125316"></a>Specifies the monitoring dimension. For example, the <a href="ecs-metrics.md">monitoring dimension</a> of an ECS is <strong id="b217332219423"><a name="b217332219423"></a><a name="b217332219423"></a>instance_id</strong>.</p>
    <p id="p3156446135916"><a name="p3156446135916"></a><a name="p3156446135916"></a>Specifies the metric dimension. A maximum of three dimensions are supported, and the dimensions are numbered from 0 in <strong id="b11496656104410"><a name="b11496656104410"></a><a name="b11496656104410"></a>dim.{i}=key,value</strong> format. The <strong id="b155373012228"><a name="b155373012228"></a><a name="b155373012228"></a>key</strong> cannot exceed 32 characters and the <strong id="b13618115172216"><a name="b13618115172216"></a><a name="b13618115172216"></a>value</strong> cannot exceed 256 characters.</p>
    <p id="p5621290395641"><a name="p5621290395641"></a><a name="p5621290395641"></a>Example: <strong id="b1344110556214"><a name="b1344110556214"></a><a name="b1344110556214"></a>dim.0=instance_id,i-12345</strong></p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example: Query the configuration information about the ECS whose  **ID**  is  **33328f02-3814-422e-b688-bfdba93d4051**  and  **type**  is  **instance\_host\_info**.

    ```
    GET https://{Cloud Eye endpoint}/V1.0/{project_id}/event-data?namespace=SYS.ECS&dim.0=instance_id,33328f02-3814-422e-b688-bfdba93d4051&type=instance_host_info&from=1450234543422&to=1450320943422
    ```


## Request<a name="section18441583143655"></a>

None

## Response<a name="section64339306143726"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table15437449143726"></a>
    <table><thead align="left"><tr id="row46953322143726"><th class="cellrowborder" valign="top" width="15.14848515148485%" id="mcps1.2.4.1.1"><p id="p45122727143726"><a name="p45122727143726"></a><a name="p45122727143726"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="11.0988901109889%" id="mcps1.2.4.1.2"><p id="p33014498143726"><a name="p33014498143726"></a><a name="p33014498143726"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="73.75262473752625%" id="mcps1.2.4.1.3"><p id="p56928688143726"><a name="p56928688143726"></a><a name="p56928688143726"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row47821055143726"><td class="cellrowborder" valign="top" width="15.14848515148485%" headers="mcps1.2.4.1.1 "><p id="p48300279143726"><a name="p48300279143726"></a><a name="p48300279143726"></a>datapoints</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.0988901109889%" headers="mcps1.2.4.1.2 "><p id="p10076671143726"><a name="p10076671143726"></a><a name="p10076671143726"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.75262473752625%" headers="mcps1.2.4.1.3 "><p id="p42007541165934"><a name="p42007541165934"></a><a name="p42007541165934"></a>Specifies the configuration list.</p>
    <p id="p32310501145729"><a name="p32310501145729"></a><a name="p32310501145729"></a>If the corresponding configuration information does not exist, <strong id="b842352706165623"><a name="b842352706165623"></a><a name="b842352706165623"></a>datapoints</strong> is an empty array and is <strong id="b842352706163912"><a name="b842352706163912"></a><a name="b842352706163912"></a>[]</strong>.</p>
    <p id="p240834211342"><a name="p240834211342"></a><a name="p240834211342"></a>For details, see <a href="#table19905142618343">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **datapoints**  field data structure description

    <a name="table19905142618343"></a>
    <table><thead align="left"><tr id="row19041926183419"><th class="cellrowborder" valign="top" width="15.14848515148485%" id="mcps1.2.4.1.1"><p id="p16904192643414"><a name="p16904192643414"></a><a name="p16904192643414"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="11.0988901109889%" id="mcps1.2.4.1.2"><p id="p2090442673410"><a name="p2090442673410"></a><a name="p2090442673410"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="73.75262473752625%" id="mcps1.2.4.1.3"><p id="p15904202633412"><a name="p15904202633412"></a><a name="p15904202633412"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5905102618348"><td class="cellrowborder" valign="top" width="15.14848515148485%" headers="mcps1.2.4.1.1 "><p id="p990432693415"><a name="p990432693415"></a><a name="p990432693415"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.0988901109889%" headers="mcps1.2.4.1.2 "><p id="p3904102610348"><a name="p3904102610348"></a><a name="p3904102610348"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.75262473752625%" headers="mcps1.2.4.1.3 "><p id="p10905182613411"><a name="p10905182613411"></a><a name="p10905182613411"></a>Specifies the event type, for example, <strong id="b842352706164014"><a name="b842352706164014"></a><a name="b842352706164014"></a>instance_host_info</strong>.</p>
    </td>
    </tr>
    <tr id="row1490522663419"><td class="cellrowborder" valign="top" width="15.14848515148485%" headers="mcps1.2.4.1.1 "><p id="p1990562611342"><a name="p1990562611342"></a><a name="p1990562611342"></a>timestamp</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.0988901109889%" headers="mcps1.2.4.1.2 "><p id="p12905326113411"><a name="p12905326113411"></a><a name="p12905326113411"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.75262473752625%" headers="mcps1.2.4.1.3 "><p id="p49053264343"><a name="p49053264343"></a><a name="p49053264343"></a>Specifies the time when the event is reported. It is a UNIX timestamp and the unit is ms.</p>
    </td>
    </tr>
    <tr id="row11905426153410"><td class="cellrowborder" valign="top" width="15.14848515148485%" headers="mcps1.2.4.1.1 "><p id="p1090517264343"><a name="p1090517264343"></a><a name="p1090517264343"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.0988901109889%" headers="mcps1.2.4.1.2 "><p id="p2905126193416"><a name="p2905126193416"></a><a name="p2905126193416"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.75262473752625%" headers="mcps1.2.4.1.3 "><p id="p1090513263348"><a name="p1090513263348"></a><a name="p1090513263348"></a>Specifies the host configuration information.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "datapoints": [
            {
                "type": "instance_host_info",
                "timestamp": 1450231200000,
                "value": "xxx"
            },
            {
                "type": "instance_host_info",
                "timestamp": 1450231800000,
                "value": "xxx"
            }
        ]
    }
    ```


## Returned Values<a name="section6956456"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0171212608_table46793998"></a>
    <table><thead align="left"><tr id="en-us_topic_0171212608_row65573909"><th class="cellrowborder" valign="top" width="33.08%" id="mcps1.1.3.1.1"><p id="en-us_topic_0171212608_p1849030182924"><a name="en-us_topic_0171212608_p1849030182924"></a><a name="en-us_topic_0171212608_p1849030182924"></a><strong id="en-us_topic_0171212608_b842352706181143"><a name="en-us_topic_0171212608_b842352706181143"></a><a name="en-us_topic_0171212608_b842352706181143"></a>Returned Values</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="66.92%" id="mcps1.1.3.1.2"><p id="en-us_topic_0171212608_p15553712182924"><a name="en-us_topic_0171212608_p15553712182924"></a><a name="en-us_topic_0171212608_p15553712182924"></a><strong id="en-us_topic_0171212608_b842352706181147"><a name="en-us_topic_0171212608_b842352706181147"></a><a name="en-us_topic_0171212608_b842352706181147"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0171212608_row37564172"><td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0171212608_p581987519168"><a name="en-us_topic_0171212608_p581987519168"></a><a name="en-us_topic_0171212608_p581987519168"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.92%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0171212608_p164784039168"><a name="en-us_topic_0171212608_p164784039168"></a><a name="en-us_topic_0171212608_p164784039168"></a>Request error</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171212608_row66248115"><td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0171212608_p2691669168"><a name="en-us_topic_0171212608_p2691669168"></a><a name="en-us_topic_0171212608_p2691669168"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.92%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0171212608_p218024949168"><a name="en-us_topic_0171212608_p218024949168"></a><a name="en-us_topic_0171212608_p218024949168"></a>The authentication information is not provided or is incorrect.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171212608_row44282627"><td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0171212608_p563264059168"><a name="en-us_topic_0171212608_p563264059168"></a><a name="en-us_topic_0171212608_p563264059168"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.92%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0171212608_p661449719168"><a name="en-us_topic_0171212608_p661449719168"></a><a name="en-us_topic_0171212608_p661449719168"></a>You are forbidden to access the page requested.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171212608_row1815156"><td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0171212608_p355199299168"><a name="en-us_topic_0171212608_p355199299168"></a><a name="en-us_topic_0171212608_p355199299168"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.92%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0171212608_p585420329168"><a name="en-us_topic_0171212608_p585420329168"></a><a name="en-us_topic_0171212608_p585420329168"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171212608_row25675773"><td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0171212608_p630127129168"><a name="en-us_topic_0171212608_p630127129168"></a><a name="en-us_topic_0171212608_p630127129168"></a>429 Too Many Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.92%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0171212608_p37560249168"><a name="en-us_topic_0171212608_p37560249168"></a><a name="en-us_topic_0171212608_p37560249168"></a>Concurrent requests are excessive.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171212608_row47530006"><td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0171212608_p537873819168"><a name="en-us_topic_0171212608_p537873819168"></a><a name="en-us_topic_0171212608_p537873819168"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.92%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0171212608_p618106189168"><a name="en-us_topic_0171212608_p618106189168"></a><a name="en-us_topic_0171212608_p618106189168"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171212608_row20561848"><td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0171212608_p298930079168"><a name="en-us_topic_0171212608_p298930079168"></a><a name="en-us_topic_0171212608_p298930079168"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.92%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0171212608_p54144829168"><a name="en-us_topic_0171212608_p54144829168"></a><a name="en-us_topic_0171212608_p54144829168"></a>The service is currently unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section134757259472"></a>

For details, see  [Error Codes](error-codes.md).

