# Deleting a Private Zone<a name="EN-US_TOPIC_0057311030"></a>

## Function<a name="section2763065016101"></a>

Delete a private zone.

## URI<a name="section53701671161015"></a>

-   URI format

    DELETE /v2/zones/\{zone\_id\}

-   Parameter description

    **Table  1**  Parameter in the URI

    <a name="table56746773172616"></a><table><thead align="left"><tr id="row12848229172616"><th class="cellrowborder" valign="top" width="15.46%" id="mcps1.2.5.1.1"><p id="p44975878172616"><a name="p44975878172616"></a><a name="p44975878172616"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.530000000000005%" id="mcps1.2.5.1.2"><p id="p46443918172616"><a name="p46443918172616"></a><a name="p46443918172616"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.46%" id="mcps1.2.5.1.3"><p id="p1368350172616"><a name="p1368350172616"></a><a name="p1368350172616"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.550000000000004%" id="mcps1.2.5.1.4"><p id="p24157908172616"><a name="p24157908172616"></a><a name="p24157908172616"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39993297172616"><td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.5.1.1 "><p id="p43071797172616"><a name="p43071797172616"></a><a name="p43071797172616"></a>zone_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.2.5.1.2 "><p id="p26647585172616"><a name="p26647585172616"></a><a name="p26647585172616"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.5.1.3 "><p id="p21075379172616"><a name="p21075379172616"></a><a name="p21075379172616"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.550000000000004%" headers="mcps1.2.5.1.4 "><p id="p4976396172616"><a name="p4976396172616"></a><a name="p4976396172616"></a>Zone ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section44958995161021"></a>

None

## Response<a name="section40090803161031"></a>

-   Parameter description

    **Table  2**  Parameters in the response

    <a name="table28510837181412"></a><table><thead align="left"><tr id="en-us_topic_0057311028_row29441359123415"><th class="cellrowborder" valign="top" width="18.38%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057311028_p35939865123415"><a name="en-us_topic_0057311028_p35939865123415"></a><a name="en-us_topic_0057311028_p35939865123415"></a><strong id="en-us_topic_0057311028_b162774213314533"><a name="en-us_topic_0057311028_b162774213314533"></a><a name="en-us_topic_0057311028_b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.64%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057311028_p25447972123415"><a name="en-us_topic_0057311028_p25447972123415"></a><a name="en-us_topic_0057311028_p25447972123415"></a><strong id="en-us_topic_0057311028_b84235270619112"><a name="en-us_topic_0057311028_b84235270619112"></a><a name="en-us_topic_0057311028_b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="63.980000000000004%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057311028_p48019864123415"><a name="en-us_topic_0057311028_p48019864123415"></a><a name="en-us_topic_0057311028_p48019864123415"></a><strong id="en-us_topic_0057311028_b842352706112423"><a name="en-us_topic_0057311028_b842352706112423"></a><a name="en-us_topic_0057311028_b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0057311028_row64403739123415"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311028_p49320408123415"><a name="en-us_topic_0057311028_p49320408123415"></a><a name="en-us_topic_0057311028_p49320408123415"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311028_p35530101123415"><a name="en-us_topic_0057311028_p35530101123415"></a><a name="en-us_topic_0057311028_p35530101123415"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.980000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311028_p59365914123415"><a name="en-us_topic_0057311028_p59365914123415"></a><a name="en-us_topic_0057311028_p59365914123415"></a>Zone ID, which is a UUID used to identify the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311028_row64531184123415"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311028_p59643381123415"><a name="en-us_topic_0057311028_p59643381123415"></a><a name="en-us_topic_0057311028_p59643381123415"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311028_p66384534123415"><a name="en-us_topic_0057311028_p66384534123415"></a><a name="en-us_topic_0057311028_p66384534123415"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.980000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311028_p8438205123415"><a name="en-us_topic_0057311028_p8438205123415"></a><a name="en-us_topic_0057311028_p8438205123415"></a>Zone name</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311028_row8834981123415"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311028_p44544845123415"><a name="en-us_topic_0057311028_p44544845123415"></a><a name="en-us_topic_0057311028_p44544845123415"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311028_p51362669123415"><a name="en-us_topic_0057311028_p51362669123415"></a><a name="en-us_topic_0057311028_p51362669123415"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.980000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311028_p66735534123415"><a name="en-us_topic_0057311028_p66735534123415"></a><a name="en-us_topic_0057311028_p66735534123415"></a>Zone description</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311028_row63748898123415"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311028_p63387127123415"><a name="en-us_topic_0057311028_p63387127123415"></a><a name="en-us_topic_0057311028_p63387127123415"></a>email</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311028_p34083648123415"><a name="en-us_topic_0057311028_p34083648123415"></a><a name="en-us_topic_0057311028_p34083648123415"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.980000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311028_p9312102123415"><a name="en-us_topic_0057311028_p9312102123415"></a><a name="en-us_topic_0057311028_p9312102123415"></a>Email address of the administrator managing the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311028_row16700055123415"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311028_p10527186123415"><a name="en-us_topic_0057311028_p10527186123415"></a><a name="en-us_topic_0057311028_p10527186123415"></a>zone_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311028_p47395742123415"><a name="en-us_topic_0057311028_p47395742123415"></a><a name="en-us_topic_0057311028_p47395742123415"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.980000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311028_p13849890123415"><a name="en-us_topic_0057311028_p13849890123415"></a><a name="en-us_topic_0057311028_p13849890123415"></a>Zone type, which can be <strong id="en-us_topic_0057311028_b842352706115152"><a name="en-us_topic_0057311028_b842352706115152"></a><a name="en-us_topic_0057311028_b842352706115152"></a>public</strong> or <strong id="en-us_topic_0057311028_b842352706115156"><a name="en-us_topic_0057311028_b842352706115156"></a><a name="en-us_topic_0057311028_b842352706115156"></a>private</strong></p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311028_row57540153123415"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311028_p30240837123415"><a name="en-us_topic_0057311028_p30240837123415"></a><a name="en-us_topic_0057311028_p30240837123415"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311028_p33588766123415"><a name="en-us_topic_0057311028_p33588766123415"></a><a name="en-us_topic_0057311028_p33588766123415"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.980000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311028_p36335531123415"><a name="en-us_topic_0057311028_p36335531123415"></a><a name="en-us_topic_0057311028_p36335531123415"></a>TTL value of the SOA record set in the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311028_row58584329123415"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311028_p47710208123415"><a name="en-us_topic_0057311028_p47710208123415"></a><a name="en-us_topic_0057311028_p47710208123415"></a>serial</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311028_p39321631123415"><a name="en-us_topic_0057311028_p39321631123415"></a><a name="en-us_topic_0057311028_p39321631123415"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.980000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311028_p30935567123415"><a name="en-us_topic_0057311028_p30935567123415"></a><a name="en-us_topic_0057311028_p30935567123415"></a>Serial number in the SOA record set in the zone, which identifies the change on the primary DNS server</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311028_row9984653123415"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311028_p3450553123415"><a name="en-us_topic_0057311028_p3450553123415"></a><a name="en-us_topic_0057311028_p3450553123415"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311028_p11059337123415"><a name="en-us_topic_0057311028_p11059337123415"></a><a name="en-us_topic_0057311028_p11059337123415"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.980000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311028_p23391077123415"><a name="en-us_topic_0057311028_p23391077123415"></a><a name="en-us_topic_0057311028_p23391077123415"></a>Resource status</p>
    <p id="en-us_topic_0057311028_p9193108123415"><a name="en-us_topic_0057311028_p9193108123415"></a><a name="en-us_topic_0057311028_p9193108123415"></a>The value can be <strong id="en-us_topic_0057311028_b84235270695628"><a name="en-us_topic_0057311028_b84235270695628"></a><a name="en-us_topic_0057311028_b84235270695628"></a>PENDING_CREATE</strong>,&nbsp;<strong id="en-us_topic_0057311028_b84235270695635"><a name="en-us_topic_0057311028_b84235270695635"></a><a name="en-us_topic_0057311028_b84235270695635"></a>ACTIVE</strong>,&nbsp;<strong id="en-us_topic_0057311028_b84235270695643"><a name="en-us_topic_0057311028_b84235270695643"></a><a name="en-us_topic_0057311028_b84235270695643"></a>PENDING_DELETE</strong>, or&nbsp;<strong id="en-us_topic_0057311028_b84235270695650"><a name="en-us_topic_0057311028_b84235270695650"></a><a name="en-us_topic_0057311028_b84235270695650"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311028_row15629110123415"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311028_p57998436123415"><a name="en-us_topic_0057311028_p57998436123415"></a><a name="en-us_topic_0057311028_p57998436123415"></a>record_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311028_p252886123415"><a name="en-us_topic_0057311028_p252886123415"></a><a name="en-us_topic_0057311028_p252886123415"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.980000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311028_p20483829123415"><a name="en-us_topic_0057311028_p20483829123415"></a><a name="en-us_topic_0057311028_p20483829123415"></a>Number of record sets in the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311028_row50136736123415"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311028_p34543853123415"><a name="en-us_topic_0057311028_p34543853123415"></a><a name="en-us_topic_0057311028_p34543853123415"></a>pool_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311028_p46588698123415"><a name="en-us_topic_0057311028_p46588698123415"></a><a name="en-us_topic_0057311028_p46588698123415"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.980000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311028_p15588175123415"><a name="en-us_topic_0057311028_p15588175123415"></a><a name="en-us_topic_0057311028_p15588175123415"></a>Pool ID of the zone, which is assigned by the system</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311028_row6075853123415"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311028_p22382050123415"><a name="en-us_topic_0057311028_p22382050123415"></a><a name="en-us_topic_0057311028_p22382050123415"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311028_p1006739123415"><a name="en-us_topic_0057311028_p1006739123415"></a><a name="en-us_topic_0057311028_p1006739123415"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.980000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311028_p14437066123415"><a name="en-us_topic_0057311028_p14437066123415"></a><a name="en-us_topic_0057311028_p14437066123415"></a>Project ID of the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311028_row62824730123415"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311028_p55638354123415"><a name="en-us_topic_0057311028_p55638354123415"></a><a name="en-us_topic_0057311028_p55638354123415"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311028_p10412802123415"><a name="en-us_topic_0057311028_p10412802123415"></a><a name="en-us_topic_0057311028_p10412802123415"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.980000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311028_p38130643123415"><a name="en-us_topic_0057311028_p38130643123415"></a><a name="en-us_topic_0057311028_p38130643123415"></a>Time when the zone was created</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311028_row7631471123415"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311028_p14169428123415"><a name="en-us_topic_0057311028_p14169428123415"></a><a name="en-us_topic_0057311028_p14169428123415"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311028_p6873005123415"><a name="en-us_topic_0057311028_p6873005123415"></a><a name="en-us_topic_0057311028_p6873005123415"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.980000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311028_p19842531123415"><a name="en-us_topic_0057311028_p19842531123415"></a><a name="en-us_topic_0057311028_p19842531123415"></a>Time when the zone was updated</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311028_row44365052123415"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311028_p36799431123415"><a name="en-us_topic_0057311028_p36799431123415"></a><a name="en-us_topic_0057311028_p36799431123415"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311028_p27963939123415"><a name="en-us_topic_0057311028_p27963939123415"></a><a name="en-us_topic_0057311028_p27963939123415"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.980000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311028_p5501274116741"><a name="en-us_topic_0057311028_p5501274116741"></a><a name="en-us_topic_0057311028_p5501274116741"></a>Link of the current resource or other related resources</p>
    <p id="en-us_topic_0057311028_p50486583123415"><a name="en-us_topic_0057311028_p50486583123415"></a><a name="en-us_topic_0057311028_p50486583123415"></a>When a response is broken into pages, a <strong id="en-us_topic_0057311028_b84235270695245"><a name="en-us_topic_0057311028_b84235270695245"></a><a name="en-us_topic_0057311028_b84235270695245"></a>next</strong> link is provided to retrieve all results.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311028_row51726070123415"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311028_p29062162123415"><a name="en-us_topic_0057311028_p29062162123415"></a><a name="en-us_topic_0057311028_p29062162123415"></a>masters</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311028_p5224955123415"><a name="en-us_topic_0057311028_p5224955123415"></a><a name="en-us_topic_0057311028_p5224955123415"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.980000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311028_p3720175814459"><a name="en-us_topic_0057311028_p3720175814459"></a><a name="en-us_topic_0057311028_p3720175814459"></a>Master DNS servers, from which the slave servers get DNS information</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311028_row50896222123415"><td class="cellrowborder" valign="top" width="18.38%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311028_p28953317123415"><a name="en-us_topic_0057311028_p28953317123415"></a><a name="en-us_topic_0057311028_p28953317123415"></a>routers</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311028_p63517332123415"><a name="en-us_topic_0057311028_p63517332123415"></a><a name="en-us_topic_0057311028_p63517332123415"></a>List&lt;Router&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.980000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311028_p44630292123415"><a name="en-us_topic_0057311028_p44630292123415"></a><a name="en-us_topic_0057311028_p44630292123415"></a>Routers (VPCs associated with the zone)</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "id": "ff8080825b8fc86c015b94bc6f8712c3",
        "name": "example.com.",
        "description": "This is an example zone.",
        "email": "xx@example.com",
        "ttl": 300,
        "serial": 1,
        "masters": [],
        "status": "PENDING_DELETE",
        "links": {
            "self": "https://Endpoint/v2/zones/ff8080825b8fc86c015b94bc6f8712c3"
        },
        "pool_id": "ff8080825ab738f4015ab7513298010e",
        "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c",
        "zone_type": "private",
        "created_at": "2017-04-22T10:05:23.110",
        "updated_at": "2017-04-22T10:05:23.959",
        "record_num": 0,
        "routers": [
            {
                "status": "PENDING_DELETE",
                "router_id": "19664294-0bf6-4271-ad3a-94b8c79c6558",
                "router_region": "xx"
            },
            {
                "status": "PENDING_DELETE",
                "router_id": "f0791650-db8c-4a20-8a44-a06c6e24b15b",
                "router_region": "xx"
            }
        ]
    }
    ```


## **Returned Value**<a name="section42637797161043"></a>

See  [General Request Return Code](general-request-return-code.md).

