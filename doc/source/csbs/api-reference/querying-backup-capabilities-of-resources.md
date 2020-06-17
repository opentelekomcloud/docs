# Querying Backup Capabilities of Resources<a name="EN-US_TOPIC_0059304220"></a>

## Function<a name="section47598139"></a>

This API is used to query whether resources can be backed up.

## URI<a name="section25730074"></a>

-   URI format

    POST https://\{endpoint\}/v1/\{project\_id\}/providers/\{provider\_id\}/resources/action

-   Parameter description

    **Table  1**  Parameter description

    <a name="table5845406"></a>
    <table><thead align="left"><tr id="row39295133"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.5.1.1"><p id="p28789191"><a name="p28789191"></a><a name="p28789191"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="p50223154"><a name="p50223154"></a><a name="p50223154"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p41543686"><a name="p41543686"></a><a name="p41543686"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p9595369"><a name="p9595369"></a><a name="p9595369"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39027462"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p7107843"><a name="p7107843"></a><a name="p7107843"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p38864392"><a name="p38864392"></a><a name="p38864392"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p61008062"><a name="p61008062"></a><a name="p61008062"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row48809652"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p61267771"><a name="p61267771"></a><a name="p61267771"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p63742381"><a name="p63742381"></a><a name="p63742381"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p62859252"><a name="p62859252"></a><a name="p62859252"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p58434680"><a name="p58434680"></a><a name="p58434680"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b969994520325"><a name="b969994520325"></a><a name="b969994520325"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section30244080"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table64107605"></a>
    <table><thead align="left"><tr id="row61408832"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.5.1.1"><p id="p8059500"><a name="p8059500"></a><a name="p8059500"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="p48839760"><a name="p48839760"></a><a name="p48839760"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p63706517"><a name="p63706517"></a><a name="p63706517"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p59954275"><a name="p59954275"></a><a name="p59954275"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row24458081"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p34947511"><a name="p34947511"></a><a name="p34947511"></a>check_protectable</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p12176142"><a name="p12176142"></a><a name="p12176142"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p46743437"><a name="p46743437"></a><a name="p46743437"></a>List&lt;protectable_param&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p28122077"><a name="p28122077"></a><a name="p28122077"></a>Query parameter list</p>
    <p id="p1839218833611"><a name="p1839218833611"></a><a name="p1839218833611"></a>For details, see <a href="#table63295782">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **protectable\_param**

    **Table  3**  Parameter description of field  **protectable\_param**

    <a name="table63295782"></a>
    <table><thead align="left"><tr id="row55065844"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.5.1.1"><p id="p31148418"><a name="p31148418"></a><a name="p31148418"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p39993940"><a name="p39993940"></a><a name="p39993940"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p18283731"><a name="p18283731"></a><a name="p18283731"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p4587238"><a name="p4587238"></a><a name="p4587238"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row36022006"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.5.1.1 "><p id="p32101354"><a name="p32101354"></a><a name="p32101354"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p50072875"><a name="p50072875"></a><a name="p50072875"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p29371040"><a name="p29371040"></a><a name="p29371040"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p30244017"><a name="p30244017"></a><a name="p30244017"></a>ID of the resource (server, or EVS disk) to be checked</p>
    <p id="p1454191714455"><a name="p1454191714455"></a><a name="p1454191714455"></a>For details about how to obtain the server ID, see the <a href="https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0020805967.html" target="_blank" rel="noopener noreferrer">Elastic Cloud Server API Reference</a>. For details about how to obtain the disk ID, see the <a href="https://docs.otc.t-systems.com/en-us/api/evs/en-us_topic_0020806013.html" target="_blank" rel="noopener noreferrer">Elastic Volume Service API Reference</a>.</p>
    </td>
    </tr>
    <tr id="row3760704"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.5.1.1 "><p id="p36181640"><a name="p36181640"></a><a name="p36181640"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p45031712"><a name="p45031712"></a><a name="p45031712"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p23690032"><a name="p23690032"></a><a name="p23690032"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p39844449"><a name="p39844449"></a><a name="p39844449"></a>Type of the resource to be checked, for example, <strong id="b842352706105620"><a name="b842352706105620"></a><a name="b842352706105620"></a>OS::Nova::Server</strong> for an ECS</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{endpoint}/v1/{project_id}/providers/{provider_id}/resources/action
    {
      "check_protectable" : [ {
        "resource_id" : "6507cb66-90dc-4a12-a573-c9f3398f899d",
        "resource_type" : "OS::Nova::Server"
      } ]
    }
    ```


## Response<a name="section3761270"></a>

-   Parameter description

    **Table  4**  Parameter description

    <a name="table65316081"></a>
    <table><thead align="left"><tr id="row11761497"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p13157206"><a name="p13157206"></a><a name="p13157206"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p22434190"><a name="p22434190"></a><a name="p22434190"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p5230105"><a name="p5230105"></a><a name="p5230105"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20985336"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p22090644"><a name="p22090644"></a><a name="p22090644"></a>protectable</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p48677920"><a name="p48677920"></a><a name="p48677920"></a>List&lt;check_resp&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p50597473"><a name="p50597473"></a><a name="p50597473"></a>Check result list</p>
    <p id="p9555135383613"><a name="p9555135383613"></a><a name="p9555135383613"></a>For details, see <a href="#table4754687">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **check\_resp**

    **Table  5**  Parameter description of field  **check\_resp**

    <a name="table4754687"></a>
    <table><thead align="left"><tr id="row7236400"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p49277517"><a name="p49277517"></a><a name="p49277517"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p46392904"><a name="p46392904"></a><a name="p46392904"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p66837750"><a name="p66837750"></a><a name="p66837750"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45148709"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p33166845"><a name="p33166845"></a><a name="p33166845"></a>result</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p40734917"><a name="p40734917"></a><a name="p40734917"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p11193990"><a name="p11193990"></a><a name="p11193990"></a>Whether backup or restoration is supported</p>
    <p id="p2979184717222"><a name="p2979184717222"></a><a name="p2979184717222"></a><strong id="b344552882519"><a name="b344552882519"></a><a name="b344552882519"></a>true</strong>: yes</p>
    <p id="p1097918474229"><a name="p1097918474229"></a><a name="p1097918474229"></a><strong id="b201961734192515"><a name="b201961734192515"></a><a name="b201961734192515"></a>false</strong>: no</p>
    </td>
    </tr>
    <tr id="row33637050"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p40246543"><a name="p40246543"></a><a name="p40246543"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p51299710"><a name="p51299710"></a><a name="p51299710"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p61635816"><a name="p61635816"></a><a name="p61635816"></a>Resource type</p>
    <p id="p207361518182320"><a name="p207361518182320"></a><a name="p207361518182320"></a>Possible values are <strong id="b1917481160"><a name="b1917481160"></a><a name="b1917481160"></a>OS::Nova::Server</strong> (ECS) and <strong id="b1635870371"><a name="b1635870371"></a><a name="b1635870371"></a>OS::Ironic::BareMetalServer</strong> (BMS).</p>
    </td>
    </tr>
    <tr id="row17851434"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p36680054"><a name="p36680054"></a><a name="p36680054"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p5450975"><a name="p5450975"></a><a name="p5450975"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p38875853"><a name="p38875853"></a><a name="p38875853"></a>Error code. If an error occurs, a value is returned.</p>
    </td>
    </tr>
    <tr id="row14338358"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p20556355"><a name="p20556355"></a><a name="p20556355"></a>error_msg</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p48542107"><a name="p48542107"></a><a name="p48542107"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p39596598"><a name="p39596598"></a><a name="p39596598"></a>Error message, which will be returned if the VM is associated with a backup policy. If an error occurs, a value is returned.</p>
    </td>
    </tr>
    <tr id="row20825063"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p9108560"><a name="p9108560"></a><a name="p9108560"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p34373930"><a name="p34373930"></a><a name="p34373930"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p32824940"><a name="p32824940"></a><a name="p32824940"></a>Resource ID</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "protectable" : [ {
        "resource_id" : "6507cb66-90dc-4a12-a573-c9f3398f899d",
        "resource_type" : "OS::Nova::Server",
        "result" : true
      } ]
    }
    ```


## Status Codes<a name="section33851438"></a>

-   Normal

    <a name="table30872487"></a>
    <table><thead align="left"><tr id="row44342955"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p35009634"><a name="p35009634"></a><a name="p35009634"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p17208068"><a name="p17208068"></a><a name="p17208068"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51676283"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p25029423"><a name="p25029423"></a><a name="p25029423"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p14117383"><a name="p14117383"></a><a name="p14117383"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table2657388"></a>
    <table><thead align="left"><tr id="row15598548"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p55522847"><a name="p55522847"></a><a name="p55522847"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p1056763"><a name="p1056763"></a><a name="p1056763"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18488975"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p21212036"><a name="p21212036"></a><a name="p21212036"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p40453378"><a name="p40453378"></a><a name="p40453378"></a>Invalid request parameters.</p>
    </td>
    </tr>
    <tr id="row28536083"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p29721392"><a name="p29721392"></a><a name="p29721392"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p58622570"><a name="p58622570"></a><a name="p58622570"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row57841085"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p54616300"><a name="p54616300"></a><a name="p54616300"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p61844204"><a name="p61844204"></a><a name="p61844204"></a>No operation permission.</p>
    </td>
    </tr>
    <tr id="row19726930"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p54377486"><a name="p54377486"></a><a name="p54377486"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p42500206"><a name="p42500206"></a><a name="p42500206"></a>Requested object not found.</p>
    </td>
    </tr>
    <tr id="row46957535"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p45463985"><a name="p45463985"></a><a name="p45463985"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p58704155"><a name="p58704155"></a><a name="p58704155"></a>Service internal error.</p>
    </td>
    </tr>
    <tr id="row58575353"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p46983163"><a name="p46983163"></a><a name="p46983163"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p47539882"><a name="p47539882"></a><a name="p47539882"></a>Service unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

