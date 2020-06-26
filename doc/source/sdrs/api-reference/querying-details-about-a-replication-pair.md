# Querying Details About a Replication Pair<a name="sdrs_05_0604"></a>

## Function<a name="en-us_topic_0079693002_section34649765"></a>

This API is used to query the details about a replication pair.

## Constraints and Limitations<a name="section14394105720412"></a>

None

## URI<a name="en-us_topic_0079693002_section39390935"></a>

-   URI format

    GET /v1/\{project\_id\}/replications/\{replication\_id\}

-   Parameter description

    <a name="en-us_topic_0079693002_table63321005"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row37593218"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.1.4.1.1"><p id="en-us_topic_0079693002_p25151854"><a name="en-us_topic_0079693002_p25151854"></a><a name="en-us_topic_0079693002_p25151854"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.1.4.1.2"><p id="en-us_topic_0079693002_p1556805116115"><a name="en-us_topic_0079693002_p1556805116115"></a><a name="en-us_topic_0079693002_p1556805116115"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.1.4.1.3"><p id="en-us_topic_0079693002_p2565159161120"><a name="en-us_topic_0079693002_p2565159161120"></a><a name="en-us_topic_0079693002_p2565159161120"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row29123463"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.1.4.1.1 "><p id="p1955525154517"><a name="p1955525154517"></a><a name="p1955525154517"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.1.4.1.2 "><p id="p1555195114518"><a name="p1555195114518"></a><a name="p1555195114518"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.1.4.1.3 "><p id="p655525119457"><a name="p655525119457"></a><a name="p655525119457"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row209064399310"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.1.4.1.1 "><p id="p14555451204519"><a name="p14555451204519"></a><a name="p14555451204519"></a>replication_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.1.4.1.2 "><p id="p1555545124511"><a name="p1555545124511"></a><a name="p1555545124511"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.1.4.1.3 "><p id="p555555110456"><a name="p555555110456"></a><a name="p555555110456"></a>Specifies the ID of a replication pair.</p>
    <p id="p1427173615218"><a name="p1427173615218"></a><a name="p1427173615218"></a>You can obtain this value by calling the API described in <a href="querying-replication-pairs.md">Querying Replication Pairs</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079693002_section18974100"></a>

-   Request parameters

    None

-   Example request

    GET https://\{Endpoint\}/v1/\{project\_id\}/replications/b93bc1c4-67ee-45a1-bc8a-d022fdd28811


## Response<a name="en-us_topic_0079693002_section36549175"></a>

-   Parameter description

    <a name="table155991608555"></a>
    <table><thead align="left"><tr id="row460510055518"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p19409173684810"><a name="p19409173684810"></a><a name="p19409173684810"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p941053617485"><a name="p941053617485"></a><a name="p941053617485"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p74105367482"><a name="p74105367482"></a><a name="p74105367482"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row86164025512"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p6840181219244"><a name="p6840181219244"></a><a name="p6840181219244"></a>replication</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p18840181222411"><a name="p18840181222411"></a><a name="p18840181222411"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p5840712122416"><a name="p5840712122416"></a><a name="p5840712122416"></a>Specifies the information about a replication pair.</p>
    <p id="p239671215525"><a name="p239671215525"></a><a name="p239671215525"></a>For details, see <a href="#table84048224492">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **replication**  field description

    <a name="table84048224492"></a>
    <table><thead align="left"><tr id="row258022264919"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p7580222114911"><a name="p7580222114911"></a><a name="p7580222114911"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p658017226491"><a name="p658017226491"></a><a name="p658017226491"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p858162214494"><a name="p858162214494"></a><a name="p858162214494"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row558172244916"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p12581722154920"><a name="p12581722154920"></a><a name="p12581722154920"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p155812022124920"><a name="p155812022124920"></a><a name="p155812022124920"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p19581322154910"><a name="p19581322154910"></a><a name="p19581322154910"></a>Specifies the ID of a replication pair.</p>
    </td>
    </tr>
    <tr id="row6581922124910"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p6581132214919"><a name="p6581132214919"></a><a name="p6581132214919"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p958162284920"><a name="p958162284920"></a><a name="p958162284920"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1758172217497"><a name="p1758172217497"></a><a name="p1758172217497"></a>Specifies the name of a replication pair.</p>
    </td>
    </tr>
    <tr id="row10581132294910"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1458182224913"><a name="p1458182224913"></a><a name="p1458182224913"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1658162274918"><a name="p1658162274918"></a><a name="p1658162274918"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p6581142234917"><a name="p6581142234917"></a><a name="p6581142234917"></a>Specifies the description of a replication pair.</p>
    </td>
    </tr>
    <tr id="row24151831192816"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p958352219493"><a name="p958352219493"></a><a name="p958352219493"></a>replication_model</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1958302220497"><a name="p1958302220497"></a><a name="p1958302220497"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p758322214914"><a name="p758322214914"></a><a name="p758322214914"></a>Specifies the replication mode of a replication pair. The default value is <strong id="b01721019506"><a name="b01721019506"></a><a name="b01721019506"></a>hypermetro</strong>, indicating synchronous replication.</p>
    </td>
    </tr>
    <tr id="row185811122114912"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p558192224911"><a name="p558192224911"></a><a name="p558192224911"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p13581152213492"><a name="p13581152213492"></a><a name="p13581152213492"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p758115222495"><a name="p758115222495"></a><a name="p758115222495"></a>Specifies the status of a replication pair. For details, see <a href="replication-pair-status.md">Replication Pair Status</a>.</p>
    </td>
    </tr>
    <tr id="row18952102202911"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1058415222498"><a name="p1058415222498"></a><a name="p1058415222498"></a>progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1358492224911"><a name="p1358492224911"></a><a name="p1358492224911"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p13584142264910"><a name="p13584142264910"></a><a name="p13584142264910"></a>Specifies the synchronization progress of a replication pair.</p>
    <p id="p125841322144911"><a name="p125841322144911"></a><a name="p125841322144911"></a>Unit: %</p>
    </td>
    </tr>
    <tr id="row752590155911"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1931012731819"><a name="p1931012731819"></a><a name="p1931012731819"></a>replication_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p19589849375"><a name="p19589849375"></a><a name="p19589849375"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p17310171185"><a name="p17310171185"></a><a name="p17310171185"></a>Specifies the data synchronization status.</p>
    <a name="ul1231014717183"></a><a name="ul1231014717183"></a><ul id="ul1231014717183"><li><strong id="b169761184917"><a name="b169761184917"></a><a name="b169761184917"></a>active</strong>: Data has been synchronized.</li><li><strong id="b8316151014910"><a name="b8316151014910"></a><a name="b8316151014910"></a>inactive</strong>: Data is not synchronized.</li><li><strong id="b91417111395"><a name="b91417111395"></a><a name="b91417111395"></a>copying</strong>: Data is being synchronized.</li><li><strong id="b1778019121892"><a name="b1778019121892"></a><a name="b1778019121892"></a>active-stopped</strong>: Data synchronization is stopped.</li></ul>
    </td>
    </tr>
    <tr id="row221493292917"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p75811922164919"><a name="p75811922164919"></a><a name="p75811922164919"></a>attachment</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p201191223013"><a name="p201191223013"></a><a name="p201191223013"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p2583122144910"><a name="p2583122144910"></a><a name="p2583122144910"></a>Specifies the device name.</p>
    <p id="p159014171534"><a name="p159014171534"></a><a name="p159014171534"></a>For details, see <a href="#table03591028145217">Table 2</a>.</p>
    </td>
    </tr>
    <tr id="row155036470297"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1310134114816"><a name="p1310134114816"></a><a name="p1310134114816"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p171011454814"><a name="p171011454814"></a><a name="p171011454814"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p181074144815"><a name="p181074144815"></a><a name="p181074144815"></a>Specifies the ID of a protection group.</p>
    </td>
    </tr>
    <tr id="row55811622124919"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p65811822104915"><a name="p65811822104915"></a><a name="p65811822104915"></a>volume_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1858118221496"><a name="p1858118221496"></a><a name="p1858118221496"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p558142274912"><a name="p558142274912"></a><a name="p558142274912"></a>Specifies the ID of the disk used to create a replication pair.</p>
    </td>
    </tr>
    <tr id="row13581922194914"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p210940487"><a name="p210940487"></a><a name="p210940487"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p910134174818"><a name="p910134174818"></a><a name="p910134174818"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p14104484816"><a name="p14104484816"></a><a name="p14104484816"></a>Specifies the current production site AZ of the protection group containing the replication pair.</p>
    <a name="ul3102418482"></a><a name="ul3102418482"></a><ul id="ul3102418482"><li><strong id="b6129886568"><a name="b6129886568"></a><a name="b6129886568"></a>source</strong>: indicates that the current production site AZ is the <strong id="b11130188195610"><a name="b11130188195610"></a><a name="b11130188195610"></a>source_availability_zone</strong> value.</li><li><strong id="b10871143125611"><a name="b10871143125611"></a><a name="b10871143125611"></a>target</strong>: indicates that the current production site AZ is the <strong id="b38884315566"><a name="b38884315566"></a><a name="b38884315566"></a>target_availability_zone</strong> value.</li></ul>
    </td>
    </tr>
    <tr id="row18606162620306"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p2584122213498"><a name="p2584122213498"></a><a name="p2584122213498"></a>fault_level</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p15584172274917"><a name="p15584172274917"></a><a name="p15584172274917"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p155848220495"><a name="p155848220495"></a><a name="p155848220495"></a>Specifies the fault level of a replication pair.</p>
    <a name="ul2584112215491"></a><a name="ul2584112215491"></a><ul id="ul2584112215491"><li><strong id="b1237212459139"><a name="b1237212459139"></a><a name="b1237212459139"></a>0</strong>: No fault occurs.</li><li><strong id="b1677475415514"><a name="b1677475415514"></a><a name="b1677475415514"></a>2</strong>: The disk of the current production site does not have read/write permissions. In this case, you are advised to perform a failover.</li><li><strong id="b206395182253"><a name="b206395182253"></a><a name="b206395182253"></a>5</strong>: The replication link is disconnected. In this case, a failover is not allowed. Contact the <span id="text146401818182513"><a name="text146401818182513"></a><a name="text146401818182513"></a>customer service</span> to obtain service support.</li></ul>
    </td>
    </tr>
    <tr id="row6583162264917"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p195833226491"><a name="p195833226491"></a><a name="p195833226491"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p85831022194913"><a name="p85831022194913"></a><a name="p85831022194913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p558352217495"><a name="p558352217495"></a><a name="p558352217495"></a>Specifies the time when a replication pair was created.</p>
    <p id="p852335742213"><a name="p852335742213"></a><a name="p852335742213"></a>The default format is as follows: "yyyy-MM-ddTHH:mm:ss.SSSZ", for example, <strong id="b5556156171419"><a name="b5556156171419"></a><a name="b5556156171419"></a>2019-04-01T12:00:00.000Z</strong>.</p>
    </td>
    </tr>
    <tr id="row25831822194911"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p11583152211495"><a name="p11583152211495"></a><a name="p11583152211495"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p258312210493"><a name="p258312210493"></a><a name="p258312210493"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p185831822184915"><a name="p185831822184915"></a><a name="p185831822184915"></a>Specifies the time when a replication pair was updated.</p>
    <p id="p942310122313"><a name="p942310122313"></a><a name="p942310122313"></a>The default format is as follows: "yyyy-MM-ddTHH:mm:ss.SSSZ", for example, <strong id="b352943115153"><a name="b352943115153"></a><a name="b352943115153"></a>2019-04-01T12:00:00.000Z</strong>.</p>
    </td>
    </tr>
    <tr id="row185831822184918"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p65841722164911"><a name="p65841722164911"></a><a name="p65841722164911"></a>record_metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p6584132211492"><a name="p6584132211492"></a><a name="p6584132211492"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p4584722164919"><a name="p4584722164919"></a><a name="p4584722164919"></a>Specifies the SDR data of a replication pair.</p>
    <p id="p2310353125317"><a name="p2310353125317"></a><a name="p2310353125317"></a>For details, see <a href="#table1636242815523">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row95841322154913"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p15848228493"><a name="p15848228493"></a><a name="p15848228493"></a>failure_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p058462216499"><a name="p058462216499"></a><a name="p058462216499"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1258419228499"><a name="p1258419228499"></a><a name="p1258419228499"></a>Specifies the error code returned only when <strong id="b136121118251"><a name="b136121118251"></a><a name="b136121118251"></a>status</strong> of a replication pair is <strong id="b1561917119254"><a name="b1561917119254"></a><a name="b1561917119254"></a>error</strong>.</p>
    <p id="p355010444262"><a name="p355010444262"></a><a name="p355010444262"></a>For details, see the returned value in <a href="error-code-description.md">Error Code Description</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **attachment**  field description

    <a name="table03591028145217"></a>
    <table><thead align="left"><tr id="row635882865210"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p173585289526"><a name="p173585289526"></a><a name="p173585289526"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p14358192811524"><a name="p14358192811524"></a><a name="p14358192811524"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p16358132815220"><a name="p16358132815220"></a><a name="p16358132815220"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row267413352"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p435982835213"><a name="p435982835213"></a><a name="p435982835213"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p6359192810529"><a name="p6359192810529"></a><a name="p6359192810529"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p2359528105212"><a name="p2359528105212"></a><a name="p2359528105212"></a>Specifies the device name.</p>
    </td>
    </tr>
    <tr id="row63591128105213"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p4359102819529"><a name="p4359102819529"></a><a name="p4359102819529"></a>protected_instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p13359172811521"><a name="p13359172811521"></a><a name="p13359172811521"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p53593287528"><a name="p53593287528"></a><a name="p53593287528"></a>Specifies the ID of the protected instance to which the replication pair is attached.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **record\_metadata**  field description

    <a name="table1636242815523"></a>
    <table><thead align="left"><tr id="row13360172815217"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p93605283527"><a name="p93605283527"></a><a name="p93605283527"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p0360162845212"><a name="p0360162845212"></a><a name="p0360162845212"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p1836062855220"><a name="p1836062855220"></a><a name="p1836062855220"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row336015282524"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p03601628125218"><a name="p03601628125218"></a><a name="p03601628125218"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p19360628165219"><a name="p19360628165219"></a><a name="p19360628165219"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p636022895213"><a name="p636022895213"></a><a name="p636022895213"></a>Specifies whether the disk in a replication pair is a shared disk.</p>
    </td>
    </tr>
    <tr id="row736222820524"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p536272814529"><a name="p536272814529"></a><a name="p536272814529"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p15362162815218"><a name="p15362162815218"></a><a name="p15362162815218"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p14362142817528"><a name="p14362142817528"></a><a name="p14362142817528"></a>Specifies whether the disk in a replication pair is a system disk.</p>
    </td>
    </tr>
    <tr id="row436215284528"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p83621528105212"><a name="p83621528105212"></a><a name="p83621528105212"></a>volume_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p4362102815217"><a name="p4362102815217"></a><a name="p4362102815217"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p143621528205213"><a name="p143621528205213"></a><a name="p143621528205213"></a>Specifies the size of the disk in a replication pair. Unit: GB</p>
    </td>
    </tr>
    <tr id="row53621284522"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1736212815211"><a name="p1736212815211"></a><a name="p1736212815211"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p536213287526"><a name="p536213287526"></a><a name="p536213287526"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p736211286523"><a name="p736211286523"></a><a name="p736211286523"></a>Specifies the type of the disk in a replication pair.</p>
    <a name="ul188853197144"></a><a name="ul188853197144"></a><ul id="ul188853197144"><li><strong id="b14973103141615"><a name="b14973103141615"></a><a name="b14973103141615"></a>SATA</strong>: common I/O</li><li><strong id="b294965169"><a name="b294965169"></a><a name="b294965169"></a>SAS</strong>: high I/O</li><li><strong id="b132649717165"><a name="b132649717165"></a><a name="b132649717165"></a>SSD</strong>: ultra-high I/O</li><li><strong id="b20464482161"><a name="b20464482161"></a><a name="b20464482161"></a>co-p1</strong>: high I/O (performance-optimized I)</li><li><strong id="b8553790169"><a name="b8553790169"></a><a name="b8553790169"></a>uh-l1</strong>: ultra-high I/O (latency-optimized)<p id="p159027562599"><a name="p159027562599"></a><a name="p159027562599"></a>Disks of the co-p1 and uh-l1 types can be used on servers of the HANA, HL1, and HL2 types only.</p>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "replication": 
            {
                "id": "b93bc1c4-67ee-45a1-bc8a-d022fdd28811",
                "name": "test_sdrs_replication",
                "description": "test_description",
                "replication_model": "hypermetro",
                "status": "available",
                "progress": 0,
                "replication_status": "active",
                "attachment": [               
                    {     
                        "device": "/dev/vda",                   
                        "protected_instance": "8a7a6339-679b-452b-948c-144e0ef85d9c"               
                    }           
                ],
                "server_group_id": "c2aee29a-2959-4d01-9755-01cc76a4d17d",
                "volume_ids": "48dda0c0-c800-46f2-9728-a519ff783d35,388b324a-a9d1-44a4-a00d-42085f22a9bc",
                "priority_station": "source",
                "fault_level": "0",
                "created_at": "2018-05-04T03:43:24.108526",
                "updated_at": "2018-05-04T03:44:28.322873",
                "record_metadata": {
                    "multiattach": false,
                    "bootable": false,
                    "volume_size": 10,
                    "volume_type": "SATA"
                }
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


## Returned Values<a name="en-us_topic_0079693002_section60507121"></a>

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


