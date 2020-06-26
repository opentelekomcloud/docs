# Changing the Name of a Protected Instance<a name="sdrs_05_0505"></a>

## Function<a name="section136351762416"></a>

This API is used to change the name of a protected instance.

## Constraints and Limitations<a name="section1981616408367"></a>

None

## URI<a name="section063716154119"></a>

-   URI format

    PUT /v1/\{project\_id\}/protected-instances/\{protected\_instance\_id\}

-   Parameter description

    <a name="table6643196154115"></a>
    <table><thead align="left"><tr id="row1597836144112"><th class="cellrowborder" valign="top" width="21.65%" id="mcps1.1.5.1.1"><p id="p697818644112"><a name="p697818644112"></a><a name="p697818644112"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.1.5.1.2"><p id="p797815694112"><a name="p797815694112"></a><a name="p797815694112"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.4%" id="mcps1.1.5.1.3"><p id="p8978165418"><a name="p8978165418"></a><a name="p8978165418"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.519999999999996%" id="mcps1.1.5.1.4"><p id="p89781667413"><a name="p89781667413"></a><a name="p89781667413"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row397818620412"><td class="cellrowborder" valign="top" width="21.65%" headers="mcps1.1.5.1.1 "><p id="p2097819614412"><a name="p2097819614412"></a><a name="p2097819614412"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.1.5.1.2 "><p id="p1697820613414"><a name="p1697820613414"></a><a name="p1697820613414"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.4%" headers="mcps1.1.5.1.3 "><p id="p29785614117"><a name="p29785614117"></a><a name="p29785614117"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p397813654113"><a name="p397813654113"></a><a name="p397813654113"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row109781263417"><td class="cellrowborder" valign="top" width="21.65%" headers="mcps1.1.5.1.1 "><p id="p297817618419"><a name="p297817618419"></a><a name="p297817618419"></a>protected_instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.1.5.1.2 "><p id="p1797820616417"><a name="p1797820616417"></a><a name="p1797820616417"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.4%" headers="mcps1.1.5.1.3 "><p id="p13978166184111"><a name="p13978166184111"></a><a name="p13978166184111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p119787694116"><a name="p119787694116"></a><a name="p119787694116"></a>Specifies the ID of a protected instance.</p>
    <p id="p04812811294"><a name="p04812811294"></a><a name="p04812811294"></a>You can obtain this value by calling the API described in <a href="querying-protected-instances.md">Querying Protected Instances</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section1765717610416"></a>

-   Parameter description

    <a name="table36621563418"></a>
    <table><thead align="left"><tr id="row99786615414"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p797876124115"><a name="p797876124115"></a><a name="p797876124115"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.5.1.2"><p id="p14978266416"><a name="p14978266416"></a><a name="p14978266416"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.3"><p id="p1797819614117"><a name="p1797819614117"></a><a name="p1797819614117"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.1.5.1.4"><p id="p1197826144119"><a name="p1197826144119"></a><a name="p1197826144119"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1798010624116"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p798006114113"><a name="p798006114113"></a><a name="p798006114113"></a>protected_instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p098017615410"><a name="p098017615410"></a><a name="p098017615410"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p3980166184115"><a name="p3980166184115"></a><a name="p3980166184115"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p189809611416"><a name="p189809611416"></a><a name="p189809611416"></a>Specifies the information about a protected instance.</p>
    <p id="p292815511559"><a name="p292815511559"></a><a name="p292815511559"></a>For details, see <a href="#table920673314542">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **protected\_instance**  field description

    <a name="table920673314542"></a>
    <table><thead align="left"><tr id="row1320623313547"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p162061733155416"><a name="p162061733155416"></a><a name="p162061733155416"></a><strong id="b18805393321"><a name="b18805393321"></a><a name="b18805393321"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p1820613311541"><a name="p1820613311541"></a><a name="p1820613311541"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.91%" id="mcps1.2.5.1.3"><p id="p17206143375412"><a name="p17206143375412"></a><a name="p17206143375412"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.089999999999996%" id="mcps1.2.5.1.4"><p id="p14207193345412"><a name="p14207193345412"></a><a name="p14207193345412"></a><strong id="b18140134103215"><a name="b18140134103215"></a><a name="b18140134103215"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row122071033105418"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1120719339543"><a name="p1120719339543"></a><a name="p1120719339543"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p7207103355415"><a name="p7207103355415"></a><a name="p7207103355415"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.91%" headers="mcps1.2.5.1.3 "><p id="p112071633145415"><a name="p112071633145415"></a><a name="p112071633145415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.089999999999996%" headers="mcps1.2.5.1.4 "><p id="p17207193315415"><a name="p17207193315415"></a><a name="p17207193315415"></a>Specifies the name of a protected instance. The name can contain a maximum of 64 bytes. The value can contain only letters (a to z and A to Z), digits (0 to 9), decimal points (.), underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    PUT https://\{Endpoint\}/v1/\{project\_id\}/protected-instances/00000000632302f501632305f63c000e

    ```
    {  
          "protected_instance": {  
              "name": "test_protected_instance_name"  
          }  
      }
    ```


## Response<a name="section6674106144116"></a>

-   Parameter description

    <a name="table196814619413"></a>
    <table><thead align="left"><tr id="row59801618417"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p1298017624114"><a name="p1298017624114"></a><a name="p1298017624114"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p498014624119"><a name="p498014624119"></a><a name="p498014624119"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p198076154119"><a name="p198076154119"></a><a name="p198076154119"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row298018617416"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p1998010614118"><a name="p1998010614118"></a><a name="p1998010614118"></a>protected_instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p119800616417"><a name="p119800616417"></a><a name="p119800616417"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p1198019611416"><a name="p1198019611416"></a><a name="p1198019611416"></a>Specifies the details about a protected instance.</p>
    <p id="p1966085311438"><a name="p1966085311438"></a><a name="p1966085311438"></a>For details, see <a href="#table568913617418">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **protected\_instance**  field description

    <a name="table568913617418"></a>
    <table><thead align="left"><tr id="row098116184110"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p3981864413"><a name="p3981864413"></a><a name="p3981864413"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p6981126184117"><a name="p6981126184117"></a><a name="p6981126184117"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p698120618412"><a name="p698120618412"></a><a name="p698120618412"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row129811610416"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p49811669412"><a name="p49811669412"></a><a name="p49811669412"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p398126164114"><a name="p398126164114"></a><a name="p398126164114"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p998110618412"><a name="p998110618412"></a><a name="p998110618412"></a>Specifies the ID of a protected instance.</p>
    </td>
    </tr>
    <tr id="row49811761410"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1598110634119"><a name="p1598110634119"></a><a name="p1598110634119"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1898126194119"><a name="p1898126194119"></a><a name="p1898126194119"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1398146124116"><a name="p1398146124116"></a><a name="p1398146124116"></a>Specifies the name of a protected instance. Specifies the name of a protected instance. The name can contain a maximum of 64 bytes. The value can contain only letters (a to z and A to Z), digits (0 to 9), decimal points (.), underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row79814604116"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p09811867416"><a name="p09811867416"></a><a name="p09811867416"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1298106134118"><a name="p1298106134118"></a><a name="p1298106134118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p111181444212"><a name="p111181444212"></a><a name="p111181444212"></a>Specifies the description of a protected instance.</p>
    </td>
    </tr>
    <tr id="row949569266"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1982169411"><a name="p1982169411"></a><a name="p1982169411"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p189824694115"><a name="p189824694115"></a><a name="p189824694115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1498212619418"><a name="p1498212619418"></a><a name="p1498212619418"></a>Specifies the ID of a protection group.</p>
    </td>
    </tr>
    <tr id="row109812618417"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p129812614415"><a name="p129812614415"></a><a name="p129812614415"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p69813615417"><a name="p69813615417"></a><a name="p69813615417"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1798166144110"><a name="p1798166144110"></a><a name="p1798166144110"></a>Specifies the status of a protected instance. For details, see <a href="protected-instance-status.md">Protected Instance Status</a>.</p>
    </td>
    </tr>
    <tr id="row13362142710269"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p14745142282317"><a name="p14745142282317"></a><a name="p14745142282317"></a>progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p931104919418"><a name="p931104919418"></a><a name="p931104919418"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1330727191818"><a name="p1330727191818"></a><a name="p1330727191818"></a>Specifies the synchronization progress of a protected instance.</p>
    <p id="p12307127121818"><a name="p12307127121818"></a><a name="p12307127121818"></a>Unit: %</p>
    </td>
    </tr>
    <tr id="row1398113684118"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p89811961413"><a name="p89811961413"></a><a name="p89811961413"></a>source_server</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p149811761411"><a name="p149811761411"></a><a name="p149811761411"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p898115618413"><a name="p898115618413"></a><a name="p898115618413"></a>Specifies the production site server ID.</p>
    </td>
    </tr>
    <tr id="row398114654117"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p2981156174110"><a name="p2981156174110"></a><a name="p2981156174110"></a>target_server</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p798217674114"><a name="p798217674114"></a><a name="p798217674114"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p29820613412"><a name="p29820613412"></a><a name="p29820613412"></a>Specifies the DR site server ID.</p>
    </td>
    </tr>
    <tr id="row1698236124120"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p798220619412"><a name="p798220619412"></a><a name="p798220619412"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p179821064418"><a name="p179821064418"></a><a name="p179821064418"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p99821062416"><a name="p99821062416"></a><a name="p99821062416"></a>Specifies the time when a protected instance was created.</p>
    <p id="p161887311319"><a name="p161887311319"></a><a name="p161887311319"></a>The default format is as follows: "yyyy-MM-ddTHH:mm:ss.SSSZ", for example, <strong id="b6211442162612"><a name="b6211442162612"></a><a name="b6211442162612"></a>2019-04-01T12:00:00.000Z</strong>.</p>
    </td>
    </tr>
    <tr id="row998211694110"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p99821165411"><a name="p99821165411"></a><a name="p99821165411"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p149820694118"><a name="p149820694118"></a><a name="p149820694118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p698236134110"><a name="p698236134110"></a><a name="p698236134110"></a>Specifies the time when a protected instance was updated.</p>
    <p id="p0670511678"><a name="p0670511678"></a><a name="p0670511678"></a>The default format is as follows: "yyyy-MM-ddTHH:mm:ss.SSSZ", for example, <strong id="b5279164362617"><a name="b5279164362617"></a><a name="b5279164362617"></a>2019-04-01T12:00:00.000Z</strong>.</p>
    </td>
    </tr>
    <tr id="row1448212132711"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p10235944142418"><a name="p10235944142418"></a><a name="p10235944142418"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p10235154410245"><a name="p10235154410245"></a><a name="p10235154410245"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p382553192519"><a name="p382553192519"></a><a name="p382553192519"></a>Specifies the current production site AZ of the protection group containing the protected instance.</p>
    <a name="ul782135312518"></a><a name="ul782135312518"></a><ul id="ul782135312518"><li><strong id="b4933185132512"><a name="b4933185132512"></a><a name="b4933185132512"></a>source</strong>: indicates that the current production site AZ is the <strong id="b49341151122516"><a name="b49341151122516"></a><a name="b49341151122516"></a>source_availability_zone</strong> value.</li><li><strong id="b10418185762510"><a name="b10418185762510"></a><a name="b10418185762510"></a>target</strong>: indicates that the current production site AZ is the <strong id="b3419155717254"><a name="b3419155717254"></a><a name="b3419155717254"></a>target_availability_zone</strong> value.</li></ul>
    </td>
    </tr>
    <tr id="row208821610535"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1374517342565"><a name="p1374517342565"></a><a name="p1374517342565"></a>attachment</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p474543475616"><a name="p474543475616"></a><a name="p474543475616"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1674513345564"><a name="p1674513345564"></a><a name="p1674513345564"></a>Specifies the attached replication pairs.</p>
    <p id="p248022019511"><a name="p248022019511"></a><a name="p248022019511"></a>For details, see <a href="#table179273775819">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row11988241937"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p198281231145613"><a name="p198281231145613"></a><a name="p198281231145613"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p20771154912569"><a name="p20771154912569"></a><a name="p20771154912569"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p15241635617"><a name="p15241635617"></a><a name="p15241635617"></a>Specifies the tag list.</p>
    <p id="p94647391453"><a name="p94647391453"></a><a name="p94647391453"></a>For details, see <a href="#table537215313717">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row6217281633"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p6472615185719"><a name="p6472615185719"></a><a name="p6472615185719"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p457217441413"><a name="p457217441413"></a><a name="p457217441413"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p370974645720"><a name="p370974645720"></a><a name="p370974645720"></a>Specifies the metadata of a protected instance.</p>
    <p id="p370155313511"><a name="p370155313511"></a><a name="p370155313511"></a>For details, see <a href="#table18286124016331">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **attachment**  field description

    <a name="table179273775819"></a>
    <table><thead align="left"><tr id="row1492813755816"><th class="cellrowborder" valign="top" width="28.9028902890289%" id="mcps1.2.4.1.1"><p id="p292811711582"><a name="p292811711582"></a><a name="p292811711582"></a><strong id="b1555672414474"><a name="b1555672414474"></a><a name="b1555672414474"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.331733173317332%" id="mcps1.2.4.1.2"><p id="p11928107165814"><a name="p11928107165814"></a><a name="p11928107165814"></a><strong id="b122552614478"><a name="b122552614478"></a><a name="b122552614478"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.765376537653765%" id="mcps1.2.4.1.3"><p id="p129289712588"><a name="p129289712588"></a><a name="p129289712588"></a><strong id="b15145327144714"><a name="b15145327144714"></a><a name="b15145327144714"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row792810795814"><td class="cellrowborder" valign="top" width="28.9028902890289%" headers="mcps1.2.4.1.1 "><p id="p392816745818"><a name="p392816745818"></a><a name="p392816745818"></a>replication</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.331733173317332%" headers="mcps1.2.4.1.2 "><p id="p69286711582"><a name="p69286711582"></a><a name="p69286711582"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.765376537653765%" headers="mcps1.2.4.1.3 "><p id="p14719113310"><a name="p14719113310"></a><a name="p14719113310"></a>Specifies the ID of a replication pair.</p>
    </td>
    </tr>
    <tr id="row69284725813"><td class="cellrowborder" valign="top" width="28.9028902890289%" headers="mcps1.2.4.1.1 "><p id="p139281074588"><a name="p139281074588"></a><a name="p139281074588"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.331733173317332%" headers="mcps1.2.4.1.2 "><p id="p1192813705820"><a name="p1192813705820"></a><a name="p1192813705820"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.765376537653765%" headers="mcps1.2.4.1.3 "><p id="p99281876589"><a name="p99281876589"></a><a name="p99281876589"></a>Specifies the device name.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **tags**  field description

    <a name="table537215313717"></a>
    <table><thead align="left"><tr id="row133739314717"><th class="cellrowborder" valign="top" width="29.13291329132913%" id="mcps1.2.4.1.1"><p id="p23731337718"><a name="p23731337718"></a><a name="p23731337718"></a><strong id="b204511732124716"><a name="b204511732124716"></a><a name="b204511732124716"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.071707170717072%" id="mcps1.2.4.1.2"><p id="p53739312717"><a name="p53739312717"></a><a name="p53739312717"></a><strong id="b3740833124710"><a name="b3740833124710"></a><a name="b3740833124710"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.7953795379538%" id="mcps1.2.4.1.3"><p id="p193731731972"><a name="p193731731972"></a><a name="p193731731972"></a><strong id="b44281134194719"><a name="b44281134194719"></a><a name="b44281134194719"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12373831710"><td class="cellrowborder" valign="top" width="29.13291329132913%" headers="mcps1.2.4.1.1 "><p id="p1337323171"><a name="p1337323171"></a><a name="p1337323171"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.071707170717072%" headers="mcps1.2.4.1.2 "><p id="p5373831670"><a name="p5373831670"></a><a name="p5373831670"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7953795379538%" headers="mcps1.2.4.1.3 "><p id="p1688242248"><a name="p1688242248"></a><a name="p1688242248"></a>Specifies the tag key.</p>
    </td>
    </tr>
    <tr id="row163731831173"><td class="cellrowborder" valign="top" width="29.13291329132913%" headers="mcps1.2.4.1.1 "><p id="p1237315315710"><a name="p1237315315710"></a><a name="p1237315315710"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.071707170717072%" headers="mcps1.2.4.1.2 "><p id="p163731338716"><a name="p163731338716"></a><a name="p163731338716"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7953795379538%" headers="mcps1.2.4.1.3 "><p id="p1237320316714"><a name="p1237320316714"></a><a name="p1237320316714"></a>Specifies the tag value.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **metadata**  field description

    <a name="table18286124016331"></a>
    <table><thead align="left"><tr id="row1228734016335"><th class="cellrowborder" valign="top" width="29.14291429142914%" id="mcps1.2.4.1.1"><p id="p18958174419296"><a name="p18958174419296"></a><a name="p18958174419296"></a><strong id="b1412618117485"><a name="b1412618117485"></a><a name="b1412618117485"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.511751175117514%" id="mcps1.2.4.1.2"><p id="p12958154420296"><a name="p12958154420296"></a><a name="p12958154420296"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.34533453345335%" id="mcps1.2.4.1.3"><p id="p395816448297"><a name="p395816448297"></a><a name="p395816448297"></a><strong id="b14359821487"><a name="b14359821487"></a><a name="b14359821487"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row132895406331"><td class="cellrowborder" valign="top" width="29.14291429142914%" headers="mcps1.2.4.1.1 "><p id="p1558353082720"><a name="p1558353082720"></a><a name="p1558353082720"></a>__system__frozen</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.511751175117514%" headers="mcps1.2.4.1.2 "><p id="p11583730102710"><a name="p11583730102710"></a><a name="p11583730102710"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.34533453345335%" headers="mcps1.2.4.1.3 "><p id="p958313303271"><a name="p958313303271"></a><a name="p958313303271"></a>Specifies whether the resource is frozen.</p>
    <a name="ul529114370311"></a><a name="ul529114370311"></a><ul id="ul529114370311"><li><strong id="b386119204484"><a name="b386119204484"></a><a name="b386119204484"></a>true</strong>: indicates that the resource is frozen.</li><li>Empty: indicates that the resource is not frozen.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {  
          "protected_instance": {  
             "id": "00000000632302f501632305f63c000e",
             "name": "test_protected_instance_name",
             "description": "_sdrs_protected_instance",
             "server_group_id": "00000000632302f501632305ac75000a",
             "status": "available",
             "progress": 0,
             "source_server": "5597a320-7a36-4462-9f85-a0d01edfb416",
             "target_server": "e37ed7de-bd76-4189-8445-be747205322d",
             "created_at": "2018-05-02 22:43:03.0",
             "updated_at": "2018-05-02 22:47:27.0",
             "priority_station": "target",
             "attachment": [
                {
                    "replication": "6568f7c4-0510-4f39-929d-8ffccbd4fd47",
                    "device": "/dev/vda"
                }
            ],
            "tags": [
                {                   
                    "key": "aaaaaaa",                   
                    "value": "01234567889"               
                 },                
                 {                   
                    "key": "ffffff",                   
                    "value": "dddd"
                  }
                ],
             "metadata": {} 
      }  
      }
    ```

    Or

    ```
    { 
         "error": { 
             "message": "XXXX",  
             "code": "XXX" 
         } 
     }
    ```

    In this example,  **error**  represents a general error, including  **badrequest**  \(shown below\) and  **itemNotFound**.

    ```
    { 
         "badrequest": { 
             "message": "XXXX",  
             "code": "XXX" 
         } 
     }
    ```


## Returned Values<a name="section19734136174120"></a>

-   Normal

    <a name="sdrs_05_0101_table4315991194956"></a>
    <table><thead align="left"><tr id="sdrs_05_0101_row2336641294956"><th class="cellrowborder" valign="top" width="42.59%" id="mcps1.1.3.1.1"><p id="sdrs_05_0101_p1363125894956"><a name="sdrs_05_0101_p1363125894956"></a><a name="sdrs_05_0101_p1363125894956"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.410000000000004%" id="mcps1.1.3.1.2"><p id="sdrs_05_0101_p3039012494956"><a name="sdrs_05_0101_p3039012494956"></a><a name="sdrs_05_0101_p3039012494956"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="sdrs_05_0101_row507566794956"><td class="cellrowborder" valign="top" width="42.59%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p847584694956"><a name="sdrs_05_0101_p847584694956"></a><a name="sdrs_05_0101_p847584694956"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.410000000000004%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p1545496394956"><a name="sdrs_05_0101_p1545496394956"></a><a name="sdrs_05_0101_p1545496394956"></a>The server has accepted the request.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="sdrs_05_0101_table22458872203835"></a>
    <table><thead align="left"><tr id="sdrs_05_0101_row35704554203835"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="sdrs_05_0101_p6387753203835"><a name="sdrs_05_0101_p6387753203835"></a><a name="sdrs_05_0101_p6387753203835"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="sdrs_05_0101_p47646009203835"><a name="sdrs_05_0101_p47646009203835"></a><a name="sdrs_05_0101_p47646009203835"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="sdrs_05_0101_row34121538203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p12381163203835"><a name="sdrs_05_0101_p12381163203835"></a><a name="sdrs_05_0101_p12381163203835"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p63350108203835"><a name="sdrs_05_0101_p63350108203835"></a><a name="sdrs_05_0101_p63350108203835"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row33280063203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p11330608203835"><a name="sdrs_05_0101_p11330608203835"></a><a name="sdrs_05_0101_p11330608203835"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p45364094203835"><a name="sdrs_05_0101_p45364094203835"></a><a name="sdrs_05_0101_p45364094203835"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row5623667203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p52863895203835"><a name="sdrs_05_0101_p52863895203835"></a><a name="sdrs_05_0101_p52863895203835"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p54117066203835"><a name="sdrs_05_0101_p54117066203835"></a><a name="sdrs_05_0101_p54117066203835"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row17291554203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p58438642203835"><a name="sdrs_05_0101_p58438642203835"></a><a name="sdrs_05_0101_p58438642203835"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p35909542203835"><a name="sdrs_05_0101_p35909542203835"></a><a name="sdrs_05_0101_p35909542203835"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row54750425203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p5599455203835"><a name="sdrs_05_0101_p5599455203835"></a><a name="sdrs_05_0101_p5599455203835"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p50902717203835"><a name="sdrs_05_0101_p50902717203835"></a><a name="sdrs_05_0101_p50902717203835"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row55471277203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p63988484203835"><a name="sdrs_05_0101_p63988484203835"></a><a name="sdrs_05_0101_p63988484203835"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p15684678203835"><a name="sdrs_05_0101_p15684678203835"></a><a name="sdrs_05_0101_p15684678203835"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row6944380203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p25623884203835"><a name="sdrs_05_0101_p25623884203835"></a><a name="sdrs_05_0101_p25623884203835"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p62268733203835"><a name="sdrs_05_0101_p62268733203835"></a><a name="sdrs_05_0101_p62268733203835"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row23547689203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p28314670203835"><a name="sdrs_05_0101_p28314670203835"></a><a name="sdrs_05_0101_p28314670203835"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p11786919203835"><a name="sdrs_05_0101_p11786919203835"></a><a name="sdrs_05_0101_p11786919203835"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row38973411203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p2729702203835"><a name="sdrs_05_0101_p2729702203835"></a><a name="sdrs_05_0101_p2729702203835"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p19779281203835"><a name="sdrs_05_0101_p19779281203835"></a><a name="sdrs_05_0101_p19779281203835"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row43795805203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p57799353203835"><a name="sdrs_05_0101_p57799353203835"></a><a name="sdrs_05_0101_p57799353203835"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p51235984203835"><a name="sdrs_05_0101_p51235984203835"></a><a name="sdrs_05_0101_p51235984203835"></a>Failed to complete the request because of a service error.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row58470678203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p38504500203835"><a name="sdrs_05_0101_p38504500203835"></a><a name="sdrs_05_0101_p38504500203835"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p31856770203835"><a name="sdrs_05_0101_p31856770203835"></a><a name="sdrs_05_0101_p31856770203835"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row18275474203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p3918444203835"><a name="sdrs_05_0101_p3918444203835"></a><a name="sdrs_05_0101_p3918444203835"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p48958538203835"><a name="sdrs_05_0101_p48958538203835"></a><a name="sdrs_05_0101_p48958538203835"></a>Failed to complete the request because the server receives an invalid response from an upstream server.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row37973662203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p55967806203835"><a name="sdrs_05_0101_p55967806203835"></a><a name="sdrs_05_0101_p55967806203835"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p37098455203835"><a name="sdrs_05_0101_p37098455203835"></a><a name="sdrs_05_0101_p37098455203835"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row65450640203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p67010448203835"><a name="sdrs_05_0101_p67010448203835"></a><a name="sdrs_05_0101_p67010448203835"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p59137180203835"><a name="sdrs_05_0101_p59137180203835"></a><a name="sdrs_05_0101_p59137180203835"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


