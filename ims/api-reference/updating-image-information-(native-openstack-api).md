# Updating Image Information \(Native OpenStack API\)<a name="EN-US_TOPIC_0060804960"></a>

## Function<a name="section16095919"></a>

This API is used to modify image information.

## Constraints<a name="section4659381317371"></a>

Only customized attributes, image name, and image description can be modified.

## URI<a name="section10645546"></a>

PATCH /v2/images/\{image\_id\}

[Table 1](#table30282311)  lists the parameters.

**Table  1**  Parameter description

<a name="table30282311"></a>
<table><thead align="left"><tr id="row19672999"><th class="cellrowborder" valign="top" width="23.31%" id="mcps1.2.5.1.1"><p id="p50009058"><a name="p50009058"></a><a name="p50009058"></a><strong id="b24725868162658"><a name="b24725868162658"></a><a name="b24725868162658"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.31%" id="mcps1.2.5.1.2"><p id="p24201902"><a name="p24201902"></a><a name="p24201902"></a><strong id="b84235270616551"><a name="b84235270616551"></a><a name="b84235270616551"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.22%" id="mcps1.2.5.1.3"><p id="p265296612135"><a name="p265296612135"></a><a name="p265296612135"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="38.16%" id="mcps1.2.5.1.4"><p id="p14197042"><a name="p14197042"></a><a name="p14197042"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row41227749"><td class="cellrowborder" valign="top" width="23.31%" headers="mcps1.2.5.1.1 "><p id="p51113363"><a name="p51113363"></a><a name="p51113363"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.31%" headers="mcps1.2.5.1.2 "><p id="p46541742"><a name="p46541742"></a><a name="p46541742"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.22%" headers="mcps1.2.5.1.3 "><p id="p14189122135"><a name="p14189122135"></a><a name="p14189122135"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38.16%" headers="mcps1.2.5.1.4 "><p id="p11784733"><a name="p11784733"></a><a name="p11784733"></a>Specifies the image ID.</p>
<p id="p158631336410"><a name="p158631336410"></a><a name="p158631336410"></a>For details about how to obtain the image ID, see <a href="querying-images.md">Querying Images</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section28701056"></a>

-   Request parameters

    Glance has two methods of updating image information. The method is specified by  **Content-Type**  in the HTTP header.  **application/openstack-images-v2.0-json-patch**  and  **application/openstack-images-v2.1-json-patch**  are supported. Content types differ only in the format of the request message body.

    **Table  2**  v2.0 request message body

    <a name="table16631401173819"></a>
    <table><thead align="left"><tr id="row52304254173819"><th class="cellrowborder" valign="top" width="18.8%" id="mcps1.2.5.1.1"><p id="p8786159173819"><a name="p8786159173819"></a><a name="p8786159173819"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.280000000000001%" id="mcps1.2.5.1.2"><p id="p40590310173819"><a name="p40590310173819"></a><a name="p40590310173819"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.25%" id="mcps1.2.5.1.3"><p id="p66589640173819"><a name="p66589640173819"></a><a name="p66589640173819"></a><strong id="b1473727747"><a name="b1473727747"></a><a name="b1473727747"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.67%" id="mcps1.2.5.1.4"><p id="p25051775173819"><a name="p25051775173819"></a><a name="p25051775173819"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15927923173819"><td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.1 "><p id="p15093387173819"><a name="p15093387173819"></a><a name="p15093387173819"></a>replace</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.280000000000001%" headers="mcps1.2.5.1.2 "><p id="p14604848173819"><a name="p14604848173819"></a><a name="p14604848173819"></a>String</p>
    </td>
    <td class="cellrowborder" rowspan="3" valign="top" width="24.25%" headers="mcps1.2.5.1.3 "><p id="p42142025173819"><a name="p42142025173819"></a><a name="p42142025173819"></a>Mandatory for any of the three values</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.67%" headers="mcps1.2.5.1.4 "><p id="p58060863173819"><a name="p58060863173819"></a><a name="p58060863173819"></a>Indicates that an image attribute will be replaced. The value is the attribute to be replaced and a slash (/) must be added in front of the attribute name.</p>
    </td>
    </tr>
    <tr id="row52785720173819"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p47784899173819"><a name="p47784899173819"></a><a name="p47784899173819"></a>add</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p45371615173819"><a name="p45371615173819"></a><a name="p45371615173819"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p51222195173819"><a name="p51222195173819"></a><a name="p51222195173819"></a>Indicates that an image attribute will be added. The value is the attribute to be added and a slash (/) must be added in front of the attribute name. </p>
    </td>
    </tr>
    <tr id="row58346578173819"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p28452398173819"><a name="p28452398173819"></a><a name="p28452398173819"></a>remove</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p22942935173819"><a name="p22942935173819"></a><a name="p22942935173819"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p46438452173819"><a name="p46438452173819"></a><a name="p46438452173819"></a>Indicates that an image attribute will be deleted. The value is the attribute to be deleted and a slash (/) must be added in front of the attribute name. </p>
    </td>
    </tr>
    <tr id="row15292890173819"><td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.1 "><p id="p30764577173819"><a name="p30764577173819"></a><a name="p30764577173819"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.280000000000001%" headers="mcps1.2.5.1.2 "><p id="p8902800173819"><a name="p8902800173819"></a><a name="p8902800173819"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.25%" headers="mcps1.2.5.1.3 "><p id="p50038224173819"><a name="p50038224173819"></a><a name="p50038224173819"></a>Mandatory for <strong id="b84235270619277"><a name="b84235270619277"></a><a name="b84235270619277"></a>replace</strong> and <strong id="b842352706192711"><a name="b842352706192711"></a><a name="b842352706192711"></a>add</strong>, and not for <strong id="b842352706192721"><a name="b842352706192721"></a><a name="b842352706192721"></a>remove</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="42.67%" headers="mcps1.2.5.1.4 "><p id="p26564361173819"><a name="p26564361173819"></a><a name="p26564361173819"></a>Indicates the value of the attribute to be updated or added. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  v2.1 request message body

    <a name="table64660774173946"></a>
    <table><thead align="left"><tr id="row19981747173946"><th class="cellrowborder" valign="top" width="19.54%" id="mcps1.2.5.1.1"><p id="p7908847173946"><a name="p7908847173946"></a><a name="p7908847173946"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.48%" id="mcps1.2.5.1.2"><p id="p36636838173946"><a name="p36636838173946"></a><a name="p36636838173946"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.44%" id="mcps1.2.5.1.3"><p id="p14793922173946"><a name="p14793922173946"></a><a name="p14793922173946"></a><strong id="b1259275125"><a name="b1259275125"></a><a name="b1259275125"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.54%" id="mcps1.2.5.1.4"><p id="p57457067173946"><a name="p57457067173946"></a><a name="p57457067173946"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23510856173946"><td class="cellrowborder" valign="top" width="19.54%" headers="mcps1.2.5.1.1 "><p id="p25331202173946"><a name="p25331202173946"></a><a name="p25331202173946"></a>op</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.48%" headers="mcps1.2.5.1.2 "><p id="p38561472173946"><a name="p38561472173946"></a><a name="p38561472173946"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.44%" headers="mcps1.2.5.1.3 "><p id="p36471531173946"><a name="p36471531173946"></a><a name="p36471531173946"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.54%" headers="mcps1.2.5.1.4 "><p id="p5834164717521"><a name="p5834164717521"></a><a name="p5834164717521"></a>Indicates the type of the update operation, including replacing, adding, and deleting an attribute.</p>
    <p id="p1404010173946"><a name="p1404010173946"></a><a name="p1404010173946"></a>The value can be <strong id="b842352706192856"><a name="b842352706192856"></a><a name="b842352706192856"></a>replace</strong>, <strong id="b84235270619291"><a name="b84235270619291"></a><a name="b84235270619291"></a>add</strong>, or <strong id="b84235270619295"><a name="b84235270619295"></a><a name="b84235270619295"></a>remove</strong>.</p>
    </td>
    </tr>
    <tr id="row12636093173946"><td class="cellrowborder" valign="top" width="19.54%" headers="mcps1.2.5.1.1 "><p id="p16890582173946"><a name="p16890582173946"></a><a name="p16890582173946"></a>path</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.48%" headers="mcps1.2.5.1.2 "><p id="p25959863173946"><a name="p25959863173946"></a><a name="p25959863173946"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.44%" headers="mcps1.2.5.1.3 "><p id="p22374153173946"><a name="p22374153173946"></a><a name="p22374153173946"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.54%" headers="mcps1.2.5.1.4 "><p id="p15711105815213"><a name="p15711105815213"></a><a name="p15711105815213"></a>Indicates the name of the target attribute.</p>
    <p id="p367091173946"><a name="p367091173946"></a><a name="p367091173946"></a>For <strong id="b19331162102120"><a name="b19331162102120"></a><a name="b19331162102120"></a>replace</strong> and <strong id="b6331162122114"><a name="b6331162122114"></a><a name="b6331162122114"></a>add</strong>, the value can only be an existing attribute of the image. For <strong id="b14472282218"><a name="b14472282218"></a><a name="b14472282218"></a>add</strong>, the value can be an existing or a new attribute. If the value is an existing attribute, <strong id="b1581017366226"><a name="b1581017366226"></a><a name="b1581017366226"></a>add</strong> takes the same effect as <strong id="b1643294882219"><a name="b1643294882219"></a><a name="b1643294882219"></a>replace</strong>. If the value is a new attribute, the <strong id="b364823118236"><a name="b364823118236"></a><a name="b364823118236"></a>add</strong> operation is performed. Add a slash (/) before the attribute name.</p>
    </td>
    </tr>
    <tr id="row3303825173946"><td class="cellrowborder" valign="top" width="19.54%" headers="mcps1.2.5.1.1 "><p id="p66283283173946"><a name="p66283283173946"></a><a name="p66283283173946"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.48%" headers="mcps1.2.5.1.2 "><p id="p236866173946"><a name="p236866173946"></a><a name="p236866173946"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.44%" headers="mcps1.2.5.1.3 "><p id="p19186181173946"><a name="p19186181173946"></a><a name="p19186181173946"></a>Mandatory for <strong id="b1408980225"><a name="b1408980225"></a><a name="b1408980225"></a>replace</strong> and <strong id="b530415176"><a name="b530415176"></a><a name="b530415176"></a>add</strong>, and not for <strong id="b1272544794"><a name="b1272544794"></a><a name="b1272544794"></a>remove</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="41.54%" headers="mcps1.2.5.1.4 "><p id="p10576837173946"><a name="p10576837173946"></a><a name="p10576837173946"></a>Indicates the value of the attribute to be updated or added.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    PATCH https://{Endpoint}/v2/images/33ad552d-1149-471c-8190-ff6776174a00
    ```

    -   v2.0 request body

        ```
        "Content-Type:application/openstack-images-v2.0-json-patch"
        [
             {
                 "replace": "/name",
                 "value": "test01"       
             }
        ]     
        ```

    -   v2.1 request body

        ```
        "Content-Type:application/openstack-images-v2.1-json-patch"   
        [
             {
                 "op": "replace",
                 "path": "/name",
                 "value": "test01"
             }
        ]
        ```



## Response<a name="section56982912"></a>

-   Response parameters

    <a name="table2226228174345"></a>
    <table><thead align="left"><tr id="en-us_topic_0020091567_row23919935194835"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020091567_p58466603194835"><a name="en-us_topic_0020091567_p58466603194835"></a><a name="en-us_topic_0020091567_p58466603194835"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.29%" id="mcps1.1.4.1.2"><p id="en-us_topic_0020091567_p38174436194835"><a name="en-us_topic_0020091567_p38174436194835"></a><a name="en-us_topic_0020091567_p38174436194835"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020091567_p5121617194835"><a name="en-us_topic_0020091567_p5121617194835"></a><a name="en-us_topic_0020091567_p5121617194835"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020091567_row12197851194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p48501865194835"><a name="en-us_topic_0020091567_p48501865194835"></a><a name="en-us_topic_0020091567_p48501865194835"></a>file</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p36336996194835"><a name="en-us_topic_0020091567_p36336996194835"></a><a name="en-us_topic_0020091567_p36336996194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p57615539194835"><a name="en-us_topic_0020091567_p57615539194835"></a><a name="en-us_topic_0020091567_p57615539194835"></a>Specifies the URL for uploading and downloading the image file.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row48777806194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p58688183194835"><a name="en-us_topic_0020091567_p58688183194835"></a><a name="en-us_topic_0020091567_p58688183194835"></a>owner</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p56122344194835"><a name="en-us_topic_0020091567_p56122344194835"></a><a name="en-us_topic_0020091567_p56122344194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p49616010194835"><a name="en-us_topic_0020091567_p49616010194835"></a><a name="en-us_topic_0020091567_p49616010194835"></a>Specifies the image owner.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row43890908194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p65502698194835"><a name="en-us_topic_0020091567_p65502698194835"></a><a name="en-us_topic_0020091567_p65502698194835"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p4118332194835"><a name="en-us_topic_0020091567_p4118332194835"></a><a name="en-us_topic_0020091567_p4118332194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p65149499194835"><a name="en-us_topic_0020091567_p65149499194835"></a><a name="en-us_topic_0020091567_p65149499194835"></a>Specifies the image ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row49474582194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p48018243194835"><a name="en-us_topic_0020091567_p48018243194835"></a><a name="en-us_topic_0020091567_p48018243194835"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p64272464194835"><a name="en-us_topic_0020091567_p64272464194835"></a><a name="en-us_topic_0020091567_p64272464194835"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p38687077194835"><a name="en-us_topic_0020091567_p38687077194835"></a><a name="en-us_topic_0020091567_p38687077194835"></a>This parameter is unavailable currently.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row12639379194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p17156744194835"><a name="en-us_topic_0020091567_p17156744194835"></a><a name="en-us_topic_0020091567_p17156744194835"></a>self</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p47519001194835"><a name="en-us_topic_0020091567_p47519001194835"></a><a name="en-us_topic_0020091567_p47519001194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p23833904194835"><a name="en-us_topic_0020091567_p23833904194835"></a><a name="en-us_topic_0020091567_p23833904194835"></a>Specifies the image URL.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row13178544194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p60829128194835"><a name="en-us_topic_0020091567_p60829128194835"></a><a name="en-us_topic_0020091567_p60829128194835"></a>schema</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p28212312194835"><a name="en-us_topic_0020091567_p28212312194835"></a><a name="en-us_topic_0020091567_p28212312194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p3495945194835"><a name="en-us_topic_0020091567_p3495945194835"></a><a name="en-us_topic_0020091567_p3495945194835"></a>Specifies the image schema.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row31463509194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p65516314194835"><a name="en-us_topic_0020091567_p65516314194835"></a><a name="en-us_topic_0020091567_p65516314194835"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p5221203194835"><a name="en-us_topic_0020091567_p5221203194835"></a><a name="en-us_topic_0020091567_p5221203194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p29539523155411"><a name="en-us_topic_0020091567_p29539523155411"></a><a name="en-us_topic_0020091567_p29539523155411"></a>Specifies the image status. The value can be one of the following:</p>
    <a name="en-us_topic_0020091567_ul64671162155411"></a><a name="en-us_topic_0020091567_ul64671162155411"></a><ul id="en-us_topic_0020091567_ul64671162155411"><li><strong id="en-us_topic_0020091567_b842352706103333"><a name="en-us_topic_0020091567_b842352706103333"></a><a name="en-us_topic_0020091567_b842352706103333"></a>queued</strong>: indicates that the image metadata has already been created, and it is ready for the image file to upload. </li><li><strong id="en-us_topic_0020091567_b842352706104325"><a name="en-us_topic_0020091567_b842352706104325"></a><a name="en-us_topic_0020091567_b842352706104325"></a>saving</strong>: indicates that the image file is being uploaded to the backend storage. </li><li><strong id="en-us_topic_0020091567_b842352706104450"><a name="en-us_topic_0020091567_b842352706104450"></a><a name="en-us_topic_0020091567_b842352706104450"></a>deleted</strong>: indicates that the image has been deleted. </li><li><strong id="en-us_topic_0020091567_b842352706104518"><a name="en-us_topic_0020091567_b842352706104518"></a><a name="en-us_topic_0020091567_b842352706104518"></a>killed</strong>: indicates that an error occurs on the image uploading. </li><li><strong id="en-us_topic_0020091567_b842352706104558"><a name="en-us_topic_0020091567_b842352706104558"></a><a name="en-us_topic_0020091567_b842352706104558"></a>active</strong>: indicates that the image is available for use. </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row48160946194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p8722525194835"><a name="en-us_topic_0020091567_p8722525194835"></a><a name="en-us_topic_0020091567_p8722525194835"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p35435929194835"><a name="en-us_topic_0020091567_p35435929194835"></a><a name="en-us_topic_0020091567_p35435929194835"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p51737997194835"><a name="en-us_topic_0020091567_p51737997194835"></a><a name="en-us_topic_0020091567_p51737997194835"></a>Lists the image tags, through which you can manage private images in your own way. You can use the image tag API to add different tags to each image and filter images by tag.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row62988796194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p1818872194835"><a name="en-us_topic_0020091567_p1818872194835"></a><a name="en-us_topic_0020091567_p1818872194835"></a>visibility</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p13110977194835"><a name="en-us_topic_0020091567_p13110977194835"></a><a name="en-us_topic_0020091567_p13110977194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p13296112271017"><a name="en-us_topic_0020091567_p13296112271017"></a><a name="en-us_topic_0020091567_p13296112271017"></a>Specifies whether the image is available to other tenants. The value can be one of the following:</p>
    <a name="en-us_topic_0020091567_ul5644164418103"></a><a name="en-us_topic_0020091567_ul5644164418103"></a><ul id="en-us_topic_0020091567_ul5644164418103"><li><strong id="en-us_topic_0020091567_b183535353418"><a name="en-us_topic_0020091567_b183535353418"></a><a name="en-us_topic_0020091567_b183535353418"></a>private</strong>: private image</li><li><strong id="en-us_topic_0020091567_b96231055203419"><a name="en-us_topic_0020091567_b96231055203419"></a><a name="en-us_topic_0020091567_b96231055203419"></a>public</strong>: public image</li><li><strong id="en-us_topic_0020091567_b1527335713413"><a name="en-us_topic_0020091567_b1527335713413"></a><a name="en-us_topic_0020091567_b1527335713413"></a>shared</strong>: shared image</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row28443956194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p22259099194835"><a name="en-us_topic_0020091567_p22259099194835"></a><a name="en-us_topic_0020091567_p22259099194835"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p58156586194835"><a name="en-us_topic_0020091567_p58156586194835"></a><a name="en-us_topic_0020091567_p58156586194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p13063050194835"><a name="en-us_topic_0020091567_p13063050194835"></a><a name="en-us_topic_0020091567_p13063050194835"></a>Specifies the image name. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row50458592194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p60614140194835"><a name="en-us_topic_0020091567_p60614140194835"></a><a name="en-us_topic_0020091567_p60614140194835"></a>checksum</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p10798268194835"><a name="en-us_topic_0020091567_p10798268194835"></a><a name="en-us_topic_0020091567_p10798268194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p2244488194835"><a name="en-us_topic_0020091567_p2244488194835"></a><a name="en-us_topic_0020091567_p2244488194835"></a>This parameter is unavailable currently.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row20200399194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p25619609194835"><a name="en-us_topic_0020091567_p25619609194835"></a><a name="en-us_topic_0020091567_p25619609194835"></a>deleted</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p61922468194835"><a name="en-us_topic_0020091567_p61922468194835"></a><a name="en-us_topic_0020091567_p61922468194835"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p49664024194835"><a name="en-us_topic_0020091567_p49664024194835"></a><a name="en-us_topic_0020091567_p49664024194835"></a>Specifies whether the image has been deleted. The value can be <strong id="en-us_topic_0020091567_b178851538203618"><a name="en-us_topic_0020091567_b178851538203618"></a><a name="en-us_topic_0020091567_b178851538203618"></a>true</strong> or <strong id="en-us_topic_0020091567_b1289711387361"><a name="en-us_topic_0020091567_b1289711387361"></a><a name="en-us_topic_0020091567_b1289711387361"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row44323032194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p33395835194835"><a name="en-us_topic_0020091567_p33395835194835"></a><a name="en-us_topic_0020091567_p33395835194835"></a>protected</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p20708123194835"><a name="en-us_topic_0020091567_p20708123194835"></a><a name="en-us_topic_0020091567_p20708123194835"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p66745247194835"><a name="en-us_topic_0020091567_p66745247194835"></a><a name="en-us_topic_0020091567_p66745247194835"></a>Specifies whether the image is protected. A protected image cannot be deleted. The value can be <strong id="en-us_topic_0020091567_b149531447103618"><a name="en-us_topic_0020091567_b149531447103618"></a><a name="en-us_topic_0020091567_b149531447103618"></a>true</strong> or <strong id="en-us_topic_0020091567_b169534478363"><a name="en-us_topic_0020091567_b169534478363"></a><a name="en-us_topic_0020091567_b169534478363"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row63836314194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p3358960194835"><a name="en-us_topic_0020091567_p3358960194835"></a><a name="en-us_topic_0020091567_p3358960194835"></a>container_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p3640350194835"><a name="en-us_topic_0020091567_p3640350194835"></a><a name="en-us_topic_0020091567_p3640350194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p26432973194835"><a name="en-us_topic_0020091567_p26432973194835"></a><a name="en-us_topic_0020091567_p26432973194835"></a>Specifies the container type.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row36570173194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p9393999194835"><a name="en-us_topic_0020091567_p9393999194835"></a><a name="en-us_topic_0020091567_p9393999194835"></a>min_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p22716470194835"><a name="en-us_topic_0020091567_p22716470194835"></a><a name="en-us_topic_0020091567_p22716470194835"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p28094810194835"><a name="en-us_topic_0020091567_p28094810194835"></a><a name="en-us_topic_0020091567_p28094810194835"></a>Specifies the minimum memory size (MB) required for running the image. The parameter value depends on the <span id="en-us_topic_0020091567_text134961814105612"><a name="en-us_topic_0020091567_text134961814105612"></a><a name="en-us_topic_0020091567_text134961814105612"></a></span><span id="en-us_topic_0020091567_text5497131475612"><a name="en-us_topic_0020091567_text5497131475612"></a><a name="en-us_topic_0020091567_text5497131475612"></a>ECS</span> specifications. The default value is <strong id="en-us_topic_0020091567_b174975148566"><a name="en-us_topic_0020091567_b174975148566"></a><a name="en-us_topic_0020091567_b174975148566"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row51176839416"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p118791549416"><a name="en-us_topic_0020091567_p118791549416"></a><a name="en-us_topic_0020091567_p118791549416"></a>max_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p257405589416"><a name="en-us_topic_0020091567_p257405589416"></a><a name="en-us_topic_0020091567_p257405589416"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p46104269416"><a name="en-us_topic_0020091567_p46104269416"></a><a name="en-us_topic_0020091567_p46104269416"></a>Specifies the maximum memory of the image in the unit of MB. The parameter value depends on the ECS flavor and is not configured by default.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row51526702194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p12913335194835"><a name="en-us_topic_0020091567_p12913335194835"></a><a name="en-us_topic_0020091567_p12913335194835"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p39347249194835"><a name="en-us_topic_0020091567_p39347249194835"></a><a name="en-us_topic_0020091567_p39347249194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p33010628194835"><a name="en-us_topic_0020091567_p33010628194835"></a><a name="en-us_topic_0020091567_p33010628194835"></a>Specifies the time when the image was updated. The value is in UTC format. </p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row28660198194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p39774672194835"><a name="en-us_topic_0020091567_p39774672194835"></a><a name="en-us_topic_0020091567_p39774672194835"></a>__os_bit</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p522982194835"><a name="en-us_topic_0020091567_p522982194835"></a><a name="en-us_topic_0020091567_p522982194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p42361618194835"><a name="en-us_topic_0020091567_p42361618194835"></a><a name="en-us_topic_0020091567_p42361618194835"></a>Specifies the OS architecture, 32 bit or 64 bit.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row45710242194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p11542151194835"><a name="en-us_topic_0020091567_p11542151194835"></a><a name="en-us_topic_0020091567_p11542151194835"></a>__os_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p62499061194835"><a name="en-us_topic_0020091567_p62499061194835"></a><a name="en-us_topic_0020091567_p62499061194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p29259155194835"><a name="en-us_topic_0020091567_p29259155194835"></a><a name="en-us_topic_0020091567_p29259155194835"></a>Specifies the OS version.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row62005803194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p56414165194835"><a name="en-us_topic_0020091567_p56414165194835"></a><a name="en-us_topic_0020091567_p56414165194835"></a>__description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p6144643194835"><a name="en-us_topic_0020091567_p6144643194835"></a><a name="en-us_topic_0020091567_p6144643194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p27954078194835"><a name="en-us_topic_0020091567_p27954078194835"></a><a name="en-us_topic_0020091567_p27954078194835"></a>Provides supplementary information about the image. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row50260111194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p44537208194835"><a name="en-us_topic_0020091567_p44537208194835"></a><a name="en-us_topic_0020091567_p44537208194835"></a>disk_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p50744065194835"><a name="en-us_topic_0020091567_p50744065194835"></a><a name="en-us_topic_0020091567_p50744065194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p16628562194835"><a name="en-us_topic_0020091567_p16628562194835"></a><a name="en-us_topic_0020091567_p16628562194835"></a>Specifies the image format. The value can be <strong id="en-us_topic_0020091567_b667911865611"><a name="en-us_topic_0020091567_b667911865611"></a><a name="en-us_topic_0020091567_b667911865611"></a>vhd</strong>, <strong id="en-us_topic_0020091567_b867919181567"><a name="en-us_topic_0020091567_b867919181567"></a><a name="en-us_topic_0020091567_b867919181567"></a>raw</strong>, <strong id="en-us_topic_0020091567_b17680121815617"><a name="en-us_topic_0020091567_b17680121815617"></a><a name="en-us_topic_0020091567_b17680121815617"></a>zvhd</strong>, or <strong id="en-us_topic_0020091567_b136811818105613"><a name="en-us_topic_0020091567_b136811818105613"></a><a name="en-us_topic_0020091567_b136811818105613"></a>qcow2</strong>. The default value is <strong id="en-us_topic_0020091567_b842352706165234"><a name="en-us_topic_0020091567_b842352706165234"></a><a name="en-us_topic_0020091567_b842352706165234"></a>vhd</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row15439333194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p42626486194835"><a name="en-us_topic_0020091567_p42626486194835"></a><a name="en-us_topic_0020091567_p42626486194835"></a>__isregistered</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p30193380194835"><a name="en-us_topic_0020091567_p30193380194835"></a><a name="en-us_topic_0020091567_p30193380194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p29744726194835"><a name="en-us_topic_0020091567_p29744726194835"></a><a name="en-us_topic_0020091567_p29744726194835"></a>Specifies whether the image has been registered. The value can be <strong id="en-us_topic_0020091567_b1378193283816"><a name="en-us_topic_0020091567_b1378193283816"></a><a name="en-us_topic_0020091567_b1378193283816"></a>true</strong> or <strong id="en-us_topic_0020091567_b178243211384"><a name="en-us_topic_0020091567_b178243211384"></a><a name="en-us_topic_0020091567_b178243211384"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row66375949194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p7742752194835"><a name="en-us_topic_0020091567_p7742752194835"></a><a name="en-us_topic_0020091567_p7742752194835"></a>__platform</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p23183213194835"><a name="en-us_topic_0020091567_p23183213194835"></a><a name="en-us_topic_0020091567_p23183213194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p16267923202620"><a name="en-us_topic_0020091567_p16267923202620"></a><a name="en-us_topic_0020091567_p16267923202620"></a>Specifies the image platform type. The value can be <strong id="en-us_topic_0020091567_b128190224020"><a name="en-us_topic_0020091567_b128190224020"></a><a name="en-us_topic_0020091567_b128190224020"></a>Windows</strong>, <strong id="en-us_topic_0020091567_b682015218401"><a name="en-us_topic_0020091567_b682015218401"></a><a name="en-us_topic_0020091567_b682015218401"></a>Ubuntu</strong>, <strong id="en-us_topic_0020091567_b582011210401"><a name="en-us_topic_0020091567_b582011210401"></a><a name="en-us_topic_0020091567_b582011210401"></a>RedHat</strong>, <strong id="en-us_topic_0020091567_b198217210406"><a name="en-us_topic_0020091567_b198217210406"></a><a name="en-us_topic_0020091567_b198217210406"></a>SUSE</strong>, <strong id="en-us_topic_0020091567_b118211725408"><a name="en-us_topic_0020091567_b118211725408"></a><a name="en-us_topic_0020091567_b118211725408"></a>CentOS</strong>, <strong id="en-us_topic_0020091567_b1382219244016"><a name="en-us_topic_0020091567_b1382219244016"></a><a name="en-us_topic_0020091567_b1382219244016"></a>Debian</strong>, <strong id="en-us_topic_0020091567_b38228215405"><a name="en-us_topic_0020091567_b38228215405"></a><a name="en-us_topic_0020091567_b38228215405"></a>OpenSUSE</strong>, <strong id="en-us_topic_0020091567_b1682318234014"><a name="en-us_topic_0020091567_b1682318234014"></a><a name="en-us_topic_0020091567_b1682318234014"></a>Oracle Linux</strong>, <strong id="en-us_topic_0020091567_b982313213407"><a name="en-us_topic_0020091567_b982313213407"></a><a name="en-us_topic_0020091567_b982313213407"></a>Fedora</strong>, <strong id="en-us_topic_0020091567_b1982315212402"><a name="en-us_topic_0020091567_b1982315212402"></a><a name="en-us_topic_0020091567_b1982315212402"></a>Other</strong>, <strong id="en-us_topic_0020091567_b128241625407"><a name="en-us_topic_0020091567_b128241625407"></a><a name="en-us_topic_0020091567_b128241625407"></a>CoreOS</strong>, or <strong id="en-us_topic_0020091567_b38246217405"><a name="en-us_topic_0020091567_b38246217405"></a><a name="en-us_topic_0020091567_b38246217405"></a>EulerOS</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row56237676194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p58957901194835"><a name="en-us_topic_0020091567_p58957901194835"></a><a name="en-us_topic_0020091567_p58957901194835"></a>__os_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p10860642194835"><a name="en-us_topic_0020091567_p10860642194835"></a><a name="en-us_topic_0020091567_p10860642194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p7296787194835"><a name="en-us_topic_0020091567_p7296787194835"></a><a name="en-us_topic_0020091567_p7296787194835"></a>Specifies the OS type. The value can be <strong id="en-us_topic_0020091567_b111902564014"><a name="en-us_topic_0020091567_b111902564014"></a><a name="en-us_topic_0020091567_b111902564014"></a>Linux</strong>, <strong id="en-us_topic_0020091567_b2191258406"><a name="en-us_topic_0020091567_b2191258406"></a><a name="en-us_topic_0020091567_b2191258406"></a>Windows</strong>, or <strong id="en-us_topic_0020091567_b1219115564017"><a name="en-us_topic_0020091567_b1219115564017"></a><a name="en-us_topic_0020091567_b1219115564017"></a>Other</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row65671090194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p17758106194835"><a name="en-us_topic_0020091567_p17758106194835"></a><a name="en-us_topic_0020091567_p17758106194835"></a>min_disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p29120466194835"><a name="en-us_topic_0020091567_p29120466194835"></a><a name="en-us_topic_0020091567_p29120466194835"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p9947522194835"><a name="en-us_topic_0020091567_p9947522194835"></a><a name="en-us_topic_0020091567_p9947522194835"></a>Specifies the minimum disk space (GB) required for running the image. The value ranges from 1 GB to 1024 GB.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row22418839194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p3986671194835"><a name="en-us_topic_0020091567_p3986671194835"></a><a name="en-us_topic_0020091567_p3986671194835"></a>virtual_env_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p54484948194835"><a name="en-us_topic_0020091567_p54484948194835"></a><a name="en-us_topic_0020091567_p54484948194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p125611053153413"><a name="en-us_topic_0020091567_p125611053153413"></a><a name="en-us_topic_0020091567_p125611053153413"></a>Specifies the environment where the image is used. The value can be <strong id="en-us_topic_0020091567_b1331907114015"><a name="en-us_topic_0020091567_b1331907114015"></a><a name="en-us_topic_0020091567_b1331907114015"></a>FusionCompute</strong>, <strong id="en-us_topic_0020091567_b4320573403"><a name="en-us_topic_0020091567_b4320573403"></a><a name="en-us_topic_0020091567_b4320573403"></a>Ironic</strong>, or <strong id="en-us_topic_0020091567_b63201371402"><a name="en-us_topic_0020091567_b63201371402"></a><a name="en-us_topic_0020091567_b63201371402"></a>DataImage</strong>.</p>
    <a name="en-us_topic_0020091567_ul20526189153516"></a><a name="en-us_topic_0020091567_ul20526189153516"></a><ul id="en-us_topic_0020091567_ul20526189153516"><li>For an <span id="en-us_topic_0020091567_text1175125161018"><a name="en-us_topic_0020091567_text1175125161018"></a><a name="en-us_topic_0020091567_text1175125161018"></a></span><span id="en-us_topic_0020091567_text576145111017"><a name="en-us_topic_0020091567_text576145111017"></a><a name="en-us_topic_0020091567_text576145111017"></a>ECS</span> image (system disk image), the value is <strong id="en-us_topic_0020091567_b376175112109"><a name="en-us_topic_0020091567_b376175112109"></a><a name="en-us_topic_0020091567_b376175112109"></a>FusionCompute</strong>.</li><li>For a data disk image, set the value to <strong id="en-us_topic_0020091567_b166310339511"><a name="en-us_topic_0020091567_b166310339511"></a><a name="en-us_topic_0020091567_b166310339511"></a>DataImage</strong>.</li><li>For a <span id="en-us_topic_0020091567_text1839145751012"><a name="en-us_topic_0020091567_text1839145751012"></a><a name="en-us_topic_0020091567_text1839145751012"></a></span><span id="en-us_topic_0020091567_text539117577103"><a name="en-us_topic_0020091567_text539117577103"></a><a name="en-us_topic_0020091567_text539117577103"></a>BMS</span> image, the value is <strong id="en-us_topic_0020091567_b2392115721014"><a name="en-us_topic_0020091567_b2392115721014"></a><a name="en-us_topic_0020091567_b2392115721014"></a>Ironic</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row58188697194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p15663996194835"><a name="en-us_topic_0020091567_p15663996194835"></a><a name="en-us_topic_0020091567_p15663996194835"></a>__image_source_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p60824135194835"><a name="en-us_topic_0020091567_p60824135194835"></a><a name="en-us_topic_0020091567_p60824135194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p27807907194835"><a name="en-us_topic_0020091567_p27807907194835"></a><a name="en-us_topic_0020091567_p27807907194835"></a>Specifies the image backend storage type. Only UDS is supported currently. </p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row48944575194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p5087606194835"><a name="en-us_topic_0020091567_p5087606194835"></a><a name="en-us_topic_0020091567_p5087606194835"></a>__imagetype</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p9442962194835"><a name="en-us_topic_0020091567_p9442962194835"></a><a name="en-us_topic_0020091567_p9442962194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p2572734285718"><a name="en-us_topic_0020091567_p2572734285718"></a><a name="en-us_topic_0020091567_p2572734285718"></a>Specifies the image type. The following types are supported:</p>
    <a name="en-us_topic_0020091567_ul6291210685828"></a><a name="en-us_topic_0020091567_ul6291210685828"></a><ul id="en-us_topic_0020091567_ul6291210685828"><li>Public image: The value is <strong id="en-us_topic_0020091567_b842352706163515"><a name="en-us_topic_0020091567_b842352706163515"></a><a name="en-us_topic_0020091567_b842352706163515"></a>gold</strong>.</li><li>Private image: The value is <strong id="en-us_topic_0020091567_b1762610292163524"><a name="en-us_topic_0020091567_b1762610292163524"></a><a name="en-us_topic_0020091567_b1762610292163524"></a>private</strong>.</li><li>Shared image: The value is <strong id="en-us_topic_0020091567_b298092137163545"><a name="en-us_topic_0020091567_b298092137163545"></a><a name="en-us_topic_0020091567_b298092137163545"></a>shared</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row38815832194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p57074654194835"><a name="en-us_topic_0020091567_p57074654194835"></a><a name="en-us_topic_0020091567_p57074654194835"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p59644261194835"><a name="en-us_topic_0020091567_p59644261194835"></a><a name="en-us_topic_0020091567_p59644261194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p66455828194835"><a name="en-us_topic_0020091567_p66455828194835"></a><a name="en-us_topic_0020091567_p66455828194835"></a>Specifies the time when the image was created. The value is in UTC format. </p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row61231547194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p60808250194835"><a name="en-us_topic_0020091567_p60808250194835"></a><a name="en-us_topic_0020091567_p60808250194835"></a>virtual_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p26521206194835"><a name="en-us_topic_0020091567_p26521206194835"></a><a name="en-us_topic_0020091567_p26521206194835"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p734038194835"><a name="en-us_topic_0020091567_p734038194835"></a><a name="en-us_topic_0020091567_p734038194835"></a>This parameter is unavailable currently.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row6606343194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p65351769194835"><a name="en-us_topic_0020091567_p65351769194835"></a><a name="en-us_topic_0020091567_p65351769194835"></a>deleted_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p59001923194835"><a name="en-us_topic_0020091567_p59001923194835"></a><a name="en-us_topic_0020091567_p59001923194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p14426478194835"><a name="en-us_topic_0020091567_p14426478194835"></a><a name="en-us_topic_0020091567_p14426478194835"></a>Specifies the time when the image was deleted. The value is in UTC format. </p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row62729443194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p47920146194835"><a name="en-us_topic_0020091567_p47920146194835"></a><a name="en-us_topic_0020091567_p47920146194835"></a>__originalimagename</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p56326613194835"><a name="en-us_topic_0020091567_p56326613194835"></a><a name="en-us_topic_0020091567_p56326613194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p66161813194835"><a name="en-us_topic_0020091567_p66161813194835"></a><a name="en-us_topic_0020091567_p66161813194835"></a>Specifies the parent image ID.</p>
    <p id="en-us_topic_0020091567_p58585407194835"><a name="en-us_topic_0020091567_p58585407194835"></a><a name="en-us_topic_0020091567_p58585407194835"></a>If the image is a public image or created from an image file, this value is left empty.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row57506617194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p27524394194835"><a name="en-us_topic_0020091567_p27524394194835"></a><a name="en-us_topic_0020091567_p27524394194835"></a>__backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p14883407194835"><a name="en-us_topic_0020091567_p14883407194835"></a><a name="en-us_topic_0020091567_p14883407194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p64705296194835"><a name="en-us_topic_0020091567_p64705296194835"></a><a name="en-us_topic_0020091567_p64705296194835"></a>Specifies the backup ID. To create an image using a backup, set the value to the backup ID. Otherwise, this value is left empty.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row45476759194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p59738895194835"><a name="en-us_topic_0020091567_p59738895194835"></a><a name="en-us_topic_0020091567_p59738895194835"></a>__productcode</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p7012311194835"><a name="en-us_topic_0020091567_p7012311194835"></a><a name="en-us_topic_0020091567_p7012311194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p31126295194835"><a name="en-us_topic_0020091567_p31126295194835"></a><a name="en-us_topic_0020091567_p31126295194835"></a>Specifies the ID of the market image product.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row54629742194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p62932961194835"><a name="en-us_topic_0020091567_p62932961194835"></a><a name="en-us_topic_0020091567_p62932961194835"></a>__image_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p64405052194835"><a name="en-us_topic_0020091567_p64405052194835"></a><a name="en-us_topic_0020091567_p64405052194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p49426728194835"><a name="en-us_topic_0020091567_p49426728194835"></a><a name="en-us_topic_0020091567_p49426728194835"></a>Specifies the size (bytes) of the image file. Value: an integer greater than 0</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row42187372194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p61733939194835"><a name="en-us_topic_0020091567_p61733939194835"></a><a name="en-us_topic_0020091567_p61733939194835"></a>__data_origin</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p34393183194835"><a name="en-us_topic_0020091567_p34393183194835"></a><a name="en-us_topic_0020091567_p34393183194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p34384472194835"><a name="en-us_topic_0020091567_p34384472194835"></a><a name="en-us_topic_0020091567_p34384472194835"></a>Specifies the image resource.</p>
    <p id="en-us_topic_0020091567_p41024797194835"><a name="en-us_topic_0020091567_p41024797194835"></a><a name="en-us_topic_0020091567_p41024797194835"></a>If the image is a public image, this parameter is left empty.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row241695482710"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p3417155412277"><a name="en-us_topic_0020091567_p3417155412277"></a><a name="en-us_topic_0020091567_p3417155412277"></a>hw_firmware_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p94173546271"><a name="en-us_topic_0020091567_p94173546271"></a><a name="en-us_topic_0020091567_p94173546271"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p1841725410273"><a name="en-us_topic_0020091567_p1841725410273"></a><a name="en-us_topic_0020091567_p1841725410273"></a>Specifies the <span id="en-us_topic_0020091567_text517213819114"><a name="en-us_topic_0020091567_text517213819114"></a><a name="en-us_topic_0020091567_text517213819114"></a></span><span id="en-us_topic_0020091567_text617310871112"><a name="en-us_topic_0020091567_text617310871112"></a><a name="en-us_topic_0020091567_text617310871112"></a>ECS</span> boot mode. The following values are supported:</p>
    <a name="en-us_topic_0020091567_ul149852572301"></a><a name="en-us_topic_0020091567_ul149852572301"></a><ul id="en-us_topic_0020091567_ul149852572301"><li><strong id="en-us_topic_0020091567_b21976546489"><a name="en-us_topic_0020091567_b21976546489"></a><a name="en-us_topic_0020091567_b21976546489"></a>bios</strong> indicates the BIOS boot mode.</li><li><strong id="en-us_topic_0020091567_b131713934914"><a name="en-us_topic_0020091567_b131713934914"></a><a name="en-us_topic_0020091567_b131713934914"></a>uefi</strong> indicates the UEFI boot mode.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row1922712020747"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p1688848719937"><a name="en-us_topic_0020091567_p1688848719937"></a><a name="en-us_topic_0020091567_p1688848719937"></a>__support_kvm</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p1314210319937"><a name="en-us_topic_0020091567_p1314210319937"></a><a name="en-us_topic_0020091567_p1314210319937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p6435151319937"><a name="en-us_topic_0020091567_p6435151319937"></a><a name="en-us_topic_0020091567_p6435151319937"></a>Specifies whether the image supports KVM. If yes, the value is <strong id="en-us_topic_0020091567_b842352706174145"><a name="en-us_topic_0020091567_b842352706174145"></a><a name="en-us_topic_0020091567_b842352706174145"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row2176677820925"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p4682508419937"><a name="en-us_topic_0020091567_p4682508419937"></a><a name="en-us_topic_0020091567_p4682508419937"></a>__support_xen</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p2922074219937"><a name="en-us_topic_0020091567_p2922074219937"></a><a name="en-us_topic_0020091567_p2922074219937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p5999426419937"><a name="en-us_topic_0020091567_p5999426419937"></a><a name="en-us_topic_0020091567_p5999426419937"></a>Specifies whether the image supports Xen. If yes, the value is <strong id="en-us_topic_0020091567_b40128715692258"><a name="en-us_topic_0020091567_b40128715692258"></a><a name="en-us_topic_0020091567_b40128715692258"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row40128591201933"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p5564125819937"><a name="en-us_topic_0020091567_p5564125819937"></a><a name="en-us_topic_0020091567_p5564125819937"></a>__support_largememory</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p3285048619937"><a name="en-us_topic_0020091567_p3285048619937"></a><a name="en-us_topic_0020091567_p3285048619937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p14775155391313"><a name="en-us_topic_0020091567_p14775155391313"></a><a name="en-us_topic_0020091567_p14775155391313"></a>Specifies whether the image can be used to create large-memory ECSs. If the image supports large-memory ECSs, the value is <strong id="en-us_topic_0020091567_b4112171915415"><a name="en-us_topic_0020091567_b4112171915415"></a><a name="en-us_topic_0020091567_b4112171915415"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="en-us_topic_0020091567_p3197171053216"><a name="en-us_topic_0020091567_p3197171053216"></a><a name="en-us_topic_0020091567_p3197171053216"></a>For the supported OSs, see <a href="values-of-related-parameters.md#table48545918250">Table 3</a>.</p>
    <p id="en-us_topic_0020091567_p86725554217"><a name="en-us_topic_0020091567_p86725554217"></a><a name="en-us_topic_0020091567_p86725554217"></a></p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row27314678185940"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p5257634319937"><a name="en-us_topic_0020091567_p5257634319937"></a><a name="en-us_topic_0020091567_p5257634319937"></a>__support_diskintensive</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p4365124719937"><a name="en-us_topic_0020091567_p4365124719937"></a><a name="en-us_topic_0020091567_p4365124719937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p3727279719937"><a name="en-us_topic_0020091567_p3727279719937"></a><a name="en-us_topic_0020091567_p3727279719937"></a>Specifies whether the image can be used to create disk-intensive ECSs. If the image supports disk-intensive ECSs, the value is <strong id="en-us_topic_0020091567_b2025511543"><a name="en-us_topic_0020091567_b2025511543"></a><a name="en-us_topic_0020091567_b2025511543"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row55915043185940"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p6005168719937"><a name="en-us_topic_0020091567_p6005168719937"></a><a name="en-us_topic_0020091567_p6005168719937"></a>__support_highperformance</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p6702872519937"><a name="en-us_topic_0020091567_p6702872519937"></a><a name="en-us_topic_0020091567_p6702872519937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p3306819319937"><a name="en-us_topic_0020091567_p3306819319937"></a><a name="en-us_topic_0020091567_p3306819319937"></a>Specifies whether the image can be used to create high-performance ECSs. If the image supports high-performance ECSs, the value is <strong id="en-us_topic_0020091567_b1321410424"><a name="en-us_topic_0020091567_b1321410424"></a><a name="en-us_topic_0020091567_b1321410424"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row32822185940"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p1241378919937"><a name="en-us_topic_0020091567_p1241378919937"></a><a name="en-us_topic_0020091567_p1241378919937"></a>__support_xen_gpu_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p3786179019937"><a name="en-us_topic_0020091567_p3786179019937"></a><a name="en-us_topic_0020091567_p3786179019937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p5825807419937"><a name="en-us_topic_0020091567_p5825807419937"></a><a name="en-us_topic_0020091567_p5825807419937"></a>Specifies whether the image can be used to create GPU-optimized ECSs on the Xen platform. See <a href="values-of-related-parameters.md#table65768383152758">Table 2</a> for its value. If the image does not support GPU-optimized ECSs on the Xen platform, this attribute is not required. This attribute cannot co-exist with <strong id="en-us_topic_0020091567_b842352706175423"><a name="en-us_topic_0020091567_b842352706175423"></a><a name="en-us_topic_0020091567_b842352706175423"></a>__support_xen</strong> and <strong id="en-us_topic_0020091567_b842352706175430"><a name="en-us_topic_0020091567_b842352706175430"></a><a name="en-us_topic_0020091567_b842352706175430"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row11388758185940"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p4869692419937"><a name="en-us_topic_0020091567_p4869692419937"></a><a name="en-us_topic_0020091567_p4869692419937"></a>__support_kvm_gpu_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p2602039619937"><a name="en-us_topic_0020091567_p2602039619937"></a><a name="en-us_topic_0020091567_p2602039619937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p1297699219937"><a name="en-us_topic_0020091567_p1297699219937"></a><a name="en-us_topic_0020091567_p1297699219937"></a>Specifies whether the image supports GPU-optimized ECSs on the KVM platform. See <a href="values-of-related-parameters.md#table65768383152758">Table 2</a> for its value.</p>
    <p id="en-us_topic_0020091567_p1103263019937"><a name="en-us_topic_0020091567_p1103263019937"></a><a name="en-us_topic_0020091567_p1103263019937"></a>If the image does not support GPU-optimized ECSs on the KVM platform, this attribute is not required. This attribute cannot co-exist with <strong id="en-us_topic_0020091567_b2090041441"><a name="en-us_topic_0020091567_b2090041441"></a><a name="en-us_topic_0020091567_b2090041441"></a>__support_xen</strong> and <strong id="en-us_topic_0020091567_b147119975"><a name="en-us_topic_0020091567_b147119975"></a><a name="en-us_topic_0020091567_b147119975"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row1461958185940"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p6196955419937"><a name="en-us_topic_0020091567_p6196955419937"></a><a name="en-us_topic_0020091567_p6196955419937"></a>__support_xen_hana</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p2663872719937"><a name="en-us_topic_0020091567_p2663872719937"></a><a name="en-us_topic_0020091567_p2663872719937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p2469264919937"><a name="en-us_topic_0020091567_p2469264919937"></a><a name="en-us_topic_0020091567_p2469264919937"></a>Specifies whether the image supports HANA ECSs on the Xen platform. If yes, the value is <strong id="en-us_topic_0020091567_b1066553282174316"><a name="en-us_topic_0020091567_b1066553282174316"></a><a name="en-us_topic_0020091567_b1066553282174316"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="en-us_topic_0020091567_p1546130419937"><a name="en-us_topic_0020091567_p1546130419937"></a><a name="en-us_topic_0020091567_p1546130419937"></a>This attribute cannot co-exist with <strong id="en-us_topic_0020091567_b839921310"><a name="en-us_topic_0020091567_b839921310"></a><a name="en-us_topic_0020091567_b839921310"></a>__support_xen</strong> and <strong id="en-us_topic_0020091567_b345297505"><a name="en-us_topic_0020091567_b345297505"></a><a name="en-us_topic_0020091567_b345297505"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091567_row1957610919416"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020091567_p3308936119937"><a name="en-us_topic_0020091567_p3308936119937"></a><a name="en-us_topic_0020091567_p3308936119937"></a>__support_kvm_infiniband</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0020091567_p1490599719937"><a name="en-us_topic_0020091567_p1490599719937"></a><a name="en-us_topic_0020091567_p1490599719937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020091567_p3836423719937"><a name="en-us_topic_0020091567_p3836423719937"></a><a name="en-us_topic_0020091567_p3836423719937"></a>Specifies whether the image supports ECSs with the InfiniBand NIC on the KVM platform. If yes, the value is <strong id="en-us_topic_0020091567_b2040161919154726"><a name="en-us_topic_0020091567_b2040161919154726"></a><a name="en-us_topic_0020091567_b2040161919154726"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="en-us_topic_0020091567_p2430059519937"><a name="en-us_topic_0020091567_p2430059519937"></a><a name="en-us_topic_0020091567_p2430059519937"></a>This attribute cannot co-exist with <strong id="en-us_topic_0020091567_b1655636019"><a name="en-us_topic_0020091567_b1655636019"></a><a name="en-us_topic_0020091567_b1655636019"></a>__support_xen</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    STATUS CODE 200
    ```

    ```
    {  
        "file": "/v2/images/33ad552d-1149-471c-8190-ff6776174a00/file",  
        "owner": "0b1e494e2660441a957313163095fe5c",  
        "id": "33ad552d-1149-471c-8190-ff6776174a00",  
        "size": 2,  
        "self": "/v2/images/33ad552d-1149-471c-8190-ff6776174a00",  
        "schema": "/v2/schemas/image",  
        "status": "active",  
        "tags": [],  
        "visibility": "private",  
        "name": "ims_test",  
        "checksum": "99914b932bd37a50b983c5e7c90ae93b",  
        "deleted": false,  
        "protected": false,  
        "container_format": "bare",  
        "min_ram": 0,  
        "updated_at": "2015-12-08T02:30:49Z",  
        "__os_bit": "64",  
        "__os_version": "Ubuntu 14.04 server 64bit",  
        "__description": "ims test",  
        "disk_format": "vhd",  
        "__isregistered": "true",  
        "__platform": "Ubuntu",  
        "__os_type": "Linux",  
        "min_disk": 40,  
        "virtual_env_type": "FusionCompute",  
        "__image_source_type": "uds",  
        "__imagetype": "private",  
        "created_at": "2015-12-04T09:45:33Z",  
        "virtual_size": 0,  
        "deleted_at": null,  
        "__originalimagename": "33ad552d-1149-471c-8190-ff6776174a00",  
        "__backup_id": "",  
        "__productcode": "",  
        "__image_size": "449261568",  
        "__data_origin": null,
        "hw_firmware_type":"bios"
    }
    ```


## Returned Values<a name="section43084165"></a>

-   Normal

    200

-   Abnormal

    <a name="table2933833017254"></a>
    <table><thead align="left"><tr id="row5083298917254"><th class="cellrowborder" valign="top" width="38.080000000000005%" id="mcps1.1.3.1.1"><p id="p2383143117254"><a name="p2383143117254"></a><a name="p2383143117254"></a><strong id="b84235270611188"><a name="b84235270611188"></a><a name="b84235270611188"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.919999999999995%" id="mcps1.1.3.1.2"><p id="p5129777817254"><a name="p5129777817254"></a><a name="p5129777817254"></a><strong id="b84235270616929"><a name="b84235270616929"></a><a name="b84235270616929"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6147936617254"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p1377271317254"><a name="p1377271317254"></a><a name="p1377271317254"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p4184800617254"><a name="p4184800617254"></a><a name="p4184800617254"></a>Request error. For details, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    <tr id="row3424531517254"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p2240711217254"><a name="p2240711217254"></a><a name="p2240711217254"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p303679817254"><a name="p303679817254"></a><a name="p303679817254"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row2733118717254"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p6634251617254"><a name="p6634251617254"></a><a name="p6634251617254"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p503474717254"><a name="p503474717254"></a><a name="p503474717254"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row48054866192311"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p47142447192313"><a name="p47142447192313"></a><a name="p47142447192313"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p60441878192313"><a name="p60441878192313"></a><a name="p60441878192313"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row4531272317254"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p4645193117254"><a name="p4645193117254"></a><a name="p4645193117254"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p451004317254"><a name="p451004317254"></a><a name="p451004317254"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row4059039217254"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p6659632017254"><a name="p6659632017254"></a><a name="p6659632017254"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p2559285317254"><a name="p2559285317254"></a><a name="p2559285317254"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


