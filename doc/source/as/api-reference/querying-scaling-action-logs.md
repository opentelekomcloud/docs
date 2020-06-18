# Querying Scaling Action Logs<a name="EN-US_TOPIC_0043063071"></a>

## Function<a name="section37368030"></a>

This interface is used to query scaling action logs based on search criteria. The results are displayed by page.

-   Search criteria can be the start time, end time, start line number, and number of records.
-   If no search criteria are specified, a maximum of 20 scaling action logs can be queried by default.

## URI<a name="section767958"></a>

GET /autoscaling-api/v1/\{project\_id\}/scaling\_activity\_log/\{scaling\_group\_id\}

>![](/images/icon-note.gif) **NOTE:**   
>You can type the question mark \(?\) and ampersand \(&\) at the end of the URI to define multiple search criteria. Scaling action logs can be searched by all optional parameters in the following table. For details, see the example request.  

**Table  1**  Parameter description

<a name="table34134946"></a>
<table><thead align="left"><tr id="row52638042"><th class="cellrowborder" valign="top" width="22.772277227722775%" id="mcps1.2.5.1.1"><p id="p35823022"><a name="p35823022"></a><a name="p35823022"></a><strong id="b97392193218"><a name="b97392193218"></a><a name="b97392193218"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.2"><p id="p15983633"><a name="p15983633"></a><a name="p15983633"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.3"><p id="p19605934"><a name="p19605934"></a><a name="p19605934"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.504950495049506%" id="mcps1.2.5.1.4"><p id="p44576811"><a name="p44576811"></a><a name="p44576811"></a><strong id="b1199417202022"><a name="b1199417202022"></a><a name="b1199417202022"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row53951920"><td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.5.1.1 "><p id="p8029414"><a name="p8029414"></a><a name="p8029414"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p46402804"><a name="p46402804"></a><a name="p46402804"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p530819"><a name="p530819"></a><a name="p530819"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row51423381"><td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.5.1.1 "><p id="p4544348"><a name="p4544348"></a><a name="p4544348"></a>scaling_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p32547936"><a name="p32547936"></a><a name="p32547936"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p19137160"><a name="p19137160"></a><a name="p19137160"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="p6606141"><a name="p6606141"></a><a name="p6606141"></a>Specifies the AS group ID.</p>
</td>
</tr>
<tr id="row59455271"><td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.5.1.1 "><p id="p51147674"><a name="p51147674"></a><a name="p51147674"></a>start_time</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p49320909"><a name="p49320909"></a><a name="p49320909"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p35570664"><a name="p35570664"></a><a name="p35570664"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="p62651540"><a name="p62651540"></a><a name="p62651540"></a>Specifies the start time that complies with UTC for querying scaling action logs. The format of the start time is <strong id="b14044178162939"><a name="b14044178162939"></a><a name="b14044178162939"></a>yyyy-MM-ddThh:mm:ssZ</strong>.</p>
</td>
</tr>
<tr id="row26992952"><td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.5.1.1 "><p id="p38945471"><a name="p38945471"></a><a name="p38945471"></a>end_time</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p466603"><a name="p466603"></a><a name="p466603"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p37794916"><a name="p37794916"></a><a name="p37794916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="p41489361"><a name="p41489361"></a><a name="p41489361"></a>Specifies the end time that complies with UTC for querying scaling action logs. The format of the end time is <strong id="b11263138162939"><a name="b11263138162939"></a><a name="b11263138162939"></a>yyyy-MM-ddThh:mm:ssZ</strong>.</p>
</td>
</tr>
<tr id="row37859935"><td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.5.1.1 "><p id="p46755894"><a name="p46755894"></a><a name="p46755894"></a>start_number</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p29131061"><a name="p29131061"></a><a name="p29131061"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p10805765"><a name="p10805765"></a><a name="p10805765"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="p59373825"><a name="p59373825"></a><a name="p59373825"></a>Specifies the start line number. The default value is <strong id="b15998131202"><a name="b15998131202"></a><a name="b15998131202"></a>0</strong>. The minimum parameter value is <strong id="b18744142621611"><a name="b18744142621611"></a><a name="b18744142621611"></a>0</strong>.</p>
</td>
</tr>
<tr id="row25666111"><td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.5.1.1 "><p id="p65689071"><a name="p65689071"></a><a name="p65689071"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p19214507"><a name="p19214507"></a><a name="p19214507"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p12871260"><a name="p12871260"></a><a name="p12871260"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="p21968676"><a name="p21968676"></a><a name="p21968676"></a>Specifies the number of query records. The default value is <strong id="b168447885495335"><a name="b168447885495335"></a><a name="b168447885495335"></a>20</strong>. The value range is 0 to 100.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section6911623"></a>

-   Request parameters

    None

-   Example request

    This example shows how to query the scaling action logs of the AS group with ID  **e5d27f5c-dd76-4a61-b4bc-a67c5686719a**.

    ```
    GET https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_activity_log/e5d27f5c-dd76-4a61-b4bc-a67c5686719a
    ```


## Response Message<a name="section62204612"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table23410136"></a>
    <table><thead align="left"><tr id="row62549356"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.1"><p id="p33333103"><a name="p33333103"></a><a name="p33333103"></a><strong id="b184112619216"><a name="b184112619216"></a><a name="b184112619216"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="11%" id="mcps1.2.4.1.2"><p id="p15626802"><a name="p15626802"></a><a name="p15626802"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p57811421"><a name="p57811421"></a><a name="p57811421"></a><strong id="b1487216303215"><a name="b1487216303215"></a><a name="b1487216303215"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52213529"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p1437453"><a name="p1437453"></a><a name="p1437453"></a>total_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p49324898"><a name="p49324898"></a><a name="p49324898"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p35893824"><a name="p35893824"></a><a name="p35893824"></a>Specifies the total number of query records.</p>
    </td>
    </tr>
    <tr id="row54608961"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p61249726"><a name="p61249726"></a><a name="p61249726"></a>start_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p62280792"><a name="p62280792"></a><a name="p62280792"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p11579382"><a name="p11579382"></a><a name="p11579382"></a>Specifies the start line number.</p>
    </td>
    </tr>
    <tr id="row37105578"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p52761866"><a name="p52761866"></a><a name="p52761866"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p45852771"><a name="p45852771"></a><a name="p45852771"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p23086940"><a name="p23086940"></a><a name="p23086940"></a>Specifies the maximum number of resources to be queried.</p>
    </td>
    </tr>
    <tr id="row6455868"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p53163272"><a name="p53163272"></a><a name="p53163272"></a>scaling_activity_log</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p11257801"><a name="p11257801"></a><a name="p11257801"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p39466727"><a name="p39466727"></a><a name="p39466727"></a>Specifies scaling action logs. For details, see <a href="#table5100505111129">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **scaling\_activity\_log**  field description

    <a name="table5100505111129"></a>
    <table><thead align="left"><tr id="r2f50795d76cf453c9dc60f658a624810"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.1"><p id="a69f0ad0844e544b9a8cd7c6c96155fdf"><a name="a69f0ad0844e544b9a8cd7c6c96155fdf"></a><a name="a69f0ad0844e544b9a8cd7c6c96155fdf"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="11%" id="mcps1.2.4.1.2"><p id="a3dfdc81a6cc0409db1eedc7cf822ed37"><a name="a3dfdc81a6cc0409db1eedc7cf822ed37"></a><a name="a3dfdc81a6cc0409db1eedc7cf822ed37"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="a8238ba808fdb4829b4f15ea7e48befa2"><a name="a8238ba808fdb4829b4f15ea7e48befa2"></a><a name="a8238ba808fdb4829b4f15ea7e48befa2"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r74ce6d1664164a38b25d42101210a7c0"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="a47bbfe35b287448db539f535eff78327"><a name="a47bbfe35b287448db539f535eff78327"></a><a name="a47bbfe35b287448db539f535eff78327"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="a3e1edba5712c431cabcd001866b1b410"><a name="a3e1edba5712c431cabcd001866b1b410"></a><a name="a3e1edba5712c431cabcd001866b1b410"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="a0346256b63b14f3a956d7d5f32b83134"><a name="a0346256b63b14f3a956d7d5f32b83134"></a><a name="a0346256b63b14f3a956d7d5f32b83134"></a>Specifies the status of the scaling action.</p>
    <a name="ul1567913975911"></a><a name="ul1567913975911"></a><ul id="ul1567913975911"><li><strong id="b12358105314353"><a name="b12358105314353"></a><a name="b12358105314353"></a>SUCCESS</strong>: The scaling action has been performed.</li><li><strong id="b16165155917358"><a name="b16165155917358"></a><a name="b16165155917358"></a>FAIL</strong>: Performing the scaling action failed.</li><li><strong id="b129777275369"><a name="b129777275369"></a><a name="b129777275369"></a>DOING</strong>: The scaling action is being performed.</li></ul>
    </td>
    </tr>
    <tr id="rbbfd1b372fcb4b0baddc196b7d09df49"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="a008e65853fde473b8450d208c18d69e0"><a name="a008e65853fde473b8450d208c18d69e0"></a><a name="a008e65853fde473b8450d208c18d69e0"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="a11a097f6ba114149932d358048dbc3ce"><a name="a11a097f6ba114149932d358048dbc3ce"></a><a name="a11a097f6ba114149932d358048dbc3ce"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="a0c1c1d336fc64fc586107d994ca5baa8"><a name="a0c1c1d336fc64fc586107d994ca5baa8"></a><a name="a0c1c1d336fc64fc586107d994ca5baa8"></a>Specifies the start time of the scaling action. The time format must comply with UTC.</p>
    </td>
    </tr>
    <tr id="r3ce78f22df7540a6b8ca010f03ee8764"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="ad1345bea1ad4473a90bf1ac673b1e722"><a name="ad1345bea1ad4473a90bf1ac673b1e722"></a><a name="ad1345bea1ad4473a90bf1ac673b1e722"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="adebff9ceb0c94e8da3278ab781c33a0e"><a name="adebff9ceb0c94e8da3278ab781c33a0e"></a><a name="adebff9ceb0c94e8da3278ab781c33a0e"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="a59970e70708b45fd876375d5a8b039ce"><a name="a59970e70708b45fd876375d5a8b039ce"></a><a name="a59970e70708b45fd876375d5a8b039ce"></a>Specifies the end time of the scaling action. The time format must comply with UTC.</p>
    </td>
    </tr>
    <tr id="r353afd89b086409b87683d796011ea0d"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="a2b1b93d204c9427b962d16643bb54bd0"><a name="a2b1b93d204c9427b962d16643bb54bd0"></a><a name="a2b1b93d204c9427b962d16643bb54bd0"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="a96c0e7acbc3345bfa0b96f2f2730af76"><a name="a96c0e7acbc3345bfa0b96f2f2730af76"></a><a name="a96c0e7acbc3345bfa0b96f2f2730af76"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="a53a786e08fb340138998e54070a09a16"><a name="a53a786e08fb340138998e54070a09a16"></a><a name="a53a786e08fb340138998e54070a09a16"></a>Specifies the scaling action log ID.</p>
    </td>
    </tr>
    <tr id="r2a965ee79b664b7dbb172f7c13211adc"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="ac587d719a7494651835024bc76830e6d"><a name="ac587d719a7494651835024bc76830e6d"></a><a name="ac587d719a7494651835024bc76830e6d"></a>instance_removed_list</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="ab41902ac9f224f77b5694422279e4a27"><a name="ab41902ac9f224f77b5694422279e4a27"></a><a name="ab41902ac9f224f77b5694422279e4a27"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0021400639_p672823715567"><a name="en-us_topic_0021400639_p672823715567"></a><a name="en-us_topic_0021400639_p672823715567"></a>Specifies the names of the instances removed from the AS group after the scaling action is complete. The instance names are separated using a comma (,).</p>
    </td>
    </tr>
    <tr id="rae14399a79384a1fa32f64132c5063e7"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0021400639_p593774715567"><a name="en-us_topic_0021400639_p593774715567"></a><a name="en-us_topic_0021400639_p593774715567"></a>instance_deleted_list</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="adf76f011c5004c0ab0734c7581eb0616"><a name="adf76f011c5004c0ab0734c7581eb0616"></a><a name="adf76f011c5004c0ab0734c7581eb0616"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="af42ad1a314304e9eb473095b14730ef3"><a name="af42ad1a314304e9eb473095b14730ef3"></a><a name="af42ad1a314304e9eb473095b14730ef3"></a>Specifies the names of the instances removed and deleted from the AS group after the scaling action is complete. The instance names are separated using a comma (,).</p>
    </td>
    </tr>
    <tr id="r2b10b36488f14a8abe004656288f6ee3"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="af9614300bbba4ca29bf63f4c25a4cbf6"><a name="af9614300bbba4ca29bf63f4c25a4cbf6"></a><a name="af9614300bbba4ca29bf63f4c25a4cbf6"></a>instance_added_list</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0021400639_p804543115567"><a name="en-us_topic_0021400639_p804543115567"></a><a name="en-us_topic_0021400639_p804543115567"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="aa7a68694a8d7497cbaf64c6d128195a0"><a name="aa7a68694a8d7497cbaf64c6d128195a0"></a><a name="aa7a68694a8d7497cbaf64c6d128195a0"></a>Specifies the names of the instances added to the AS group after the scaling action is complete. The instance names are separated using a comma (,).</p>
    </td>
    </tr>
    <tr id="rd2b0cba3f6ac4f85a61bd72efff96a76"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="adf005843b6f04767a113662ad46f2a46"><a name="adf005843b6f04767a113662ad46f2a46"></a><a name="adf005843b6f04767a113662ad46f2a46"></a>scaling_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="abba7c061addb4776ae0612c65f4d8d5c"><a name="abba7c061addb4776ae0612c65f4d8d5c"></a><a name="abba7c061addb4776ae0612c65f4d8d5c"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0021400639_p3081215567"><a name="en-us_topic_0021400639_p3081215567"></a><a name="en-us_topic_0021400639_p3081215567"></a>Specifies the number of increased or decreased instances in the scaling action.</p>
    </td>
    </tr>
    <tr id="rfa29ea8a914e452a84f738e1c56efdc1"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="a97f9d365379e45eba520166fa1ba0d8d"><a name="a97f9d365379e45eba520166fa1ba0d8d"></a><a name="a97f9d365379e45eba520166fa1ba0d8d"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0021400639_p748687915567"><a name="en-us_topic_0021400639_p748687915567"></a><a name="en-us_topic_0021400639_p748687915567"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0021400639_p245743015567"><a name="en-us_topic_0021400639_p245743015567"></a><a name="en-us_topic_0021400639_p245743015567"></a>Specifies the description of the scaling action.</p>
    </td>
    </tr>
    <tr id="re7f4724989884b4488b2af0f7f8feaa2"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="a933a6e84e9c14f5cadfe840317e33c32"><a name="a933a6e84e9c14f5cadfe840317e33c32"></a><a name="a933a6e84e9c14f5cadfe840317e33c32"></a>instance_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="ae46063a5a6d84619bcc7dde0e0dd7a76"><a name="ae46063a5a6d84619bcc7dde0e0dd7a76"></a><a name="ae46063a5a6d84619bcc7dde0e0dd7a76"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="a137ae1c7eb2b4cd0a938c0d9509e462f"><a name="a137ae1c7eb2b4cd0a938c0d9509e462f"></a><a name="a137ae1c7eb2b4cd0a938c0d9509e462f"></a>Specifies the number of instances in the AS group.</p>
    </td>
    </tr>
    <tr id="rab90ab2baf6e48eb801e81e791e8b45c"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="a3abee0c2188d4a83862789649dc4462a"><a name="a3abee0c2188d4a83862789649dc4462a"></a><a name="a3abee0c2188d4a83862789649dc4462a"></a>desire_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0021400639_p585410715567"><a name="en-us_topic_0021400639_p585410715567"></a><a name="en-us_topic_0021400639_p585410715567"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0021400639_p442063415567"><a name="en-us_topic_0021400639_p442063415567"></a><a name="en-us_topic_0021400639_p442063415567"></a>Specifies the expected number of instances for the scaling action.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "limit": 20,
      "scaling_activity_log": [
        {
          "id": "66e0f775-c4ac-4b52-9d5c-f93ba217aa5f",
          "instance_value": 1,
          "desire_value": 0,
          "scaling_value": 1,
          "start_time": "2019-03-18T16:00:11Z",
          "end_time": "2019-03-18T16:00:32Z",
          "instance_added_list": null,
          "instance_deleted_list": "as-config-bblh-ONQE551S",
          "instance_removed_list": null,
          "status": "SUCCESS",
          "description": "{\"reason\":[{\"change_reason\":\"RECURRENCE\",\"old_value\":1,\"scaling_policy_name\":\"as-policy-bvfk\",\"change_time\":\"2019-03-18T16:00:00Z\",\"new_value\":0,\"scaling_policy_id\":\"05545d3d-ccf9-4bca-ae4f-1e5e73ca0bf6\"}]}"
        },
        {
          "id": "c3a1fff6-84a3-4cbc-8ac0-e3b0f645ecd8",
          "instance_value": 0,
          "desire_value": 1,
          "scaling_value": 1,
          "start_time": "2019-03-16T10:21:11Z",
          "end_time": "2019-03-16T10:25:12Z",
          "instance_added_list": "as-config-bblh-ONQE551S",
          "instance_deleted_list": null,
          "instance_removed_list": null,
          "status": "SUCCESS",
          "description": "{\"reason\":[{\"change_reason\":\"DIFF\",\"old_value\":0,\"change_time\":\"2019-03-16T10:21:11Z\",\"new_value\":1}]}"
        },
        "total_number": 2,
        "start_number": 0
    }
    ```


## Returned Values<a name="section22970596"></a>

-   Normal

    200

-   Abnormal

    <a name="table15568903"></a>
    <table><thead align="left"><tr id="row3870635"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p45086037"><a name="p45086037"></a><a name="p45086037"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p28090371"><a name="p28090371"></a><a name="p28090371"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60727582"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p19987085"><a name="p19987085"></a><a name="p19987085"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p8341177"><a name="p8341177"></a><a name="p8341177"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row7961729"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p40920274"><a name="p40920274"></a><a name="p40920274"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p26207892"><a name="p26207892"></a><a name="p26207892"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row34544438"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p46636132"><a name="p46636132"></a><a name="p46636132"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p19430358"><a name="p19430358"></a><a name="p19430358"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row40655501"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p4761248"><a name="p4761248"></a><a name="p4761248"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p50116845"><a name="p50116845"></a><a name="p50116845"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row48398424"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p27958252"><a name="p27958252"></a><a name="p27958252"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p50025933"><a name="p50025933"></a><a name="p50025933"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row47580213"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p28792051"><a name="p28792051"></a><a name="p28792051"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p50454834"><a name="p50454834"></a><a name="p50454834"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row51440330"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5917164"><a name="p5917164"></a><a name="p5917164"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p9528291"><a name="p9528291"></a><a name="p9528291"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row18645762"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p33911763"><a name="p33911763"></a><a name="p33911763"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p62498284"><a name="p62498284"></a><a name="p62498284"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row25613652"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p61439917"><a name="p61439917"></a><a name="p61439917"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p10577379"><a name="p10577379"></a><a name="p10577379"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row28087548"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p60498887"><a name="p60498887"></a><a name="p60498887"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1462819"><a name="p1462819"></a><a name="p1462819"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row13165375"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p59762422"><a name="p59762422"></a><a name="p59762422"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p8918034"><a name="p8918034"></a><a name="p8918034"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row13153450"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p58796504"><a name="p58796504"></a><a name="p58796504"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p64896350"><a name="p64896350"></a><a name="p64896350"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row47196242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p64799248"><a name="p64799248"></a><a name="p64799248"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p14247739"><a name="p14247739"></a><a name="p14247739"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row61120788"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p51836813"><a name="p51836813"></a><a name="p51836813"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38032294"><a name="p38032294"></a><a name="p38032294"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

