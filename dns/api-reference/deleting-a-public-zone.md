# Deleting a Public Zone<a name="EN-US_TOPIC_0037134403"></a>

## Function<a name="section2763065016101"></a>

Delete a public zone.

## URI<a name="section53701671161015"></a>

-   URI format

    DELETE /v2/zones/\{zone\_id\}

-   Parameter description

    **Table  1**  Parameter in the URI

    <a name="table56746773172616"></a><table><thead align="left"><tr id="row12848229172616"><th class="cellrowborder" valign="top" width="15.459999999999999%" id="mcps1.2.5.1.1"><p id="p44975878172616"><a name="p44975878172616"></a><a name="p44975878172616"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.09%" id="mcps1.2.5.1.2"><p id="p46443918172616"><a name="p46443918172616"></a><a name="p46443918172616"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.899999999999999%" id="mcps1.2.5.1.3"><p id="p1368350172616"><a name="p1368350172616"></a><a name="p1368350172616"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.55%" id="mcps1.2.5.1.4"><p id="p24157908172616"><a name="p24157908172616"></a><a name="p24157908172616"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39993297172616"><td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.2.5.1.1 "><p id="p43071797172616"><a name="p43071797172616"></a><a name="p43071797172616"></a>zone_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.2.5.1.2 "><p id="p26647585172616"><a name="p26647585172616"></a><a name="p26647585172616"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.899999999999999%" headers="mcps1.2.5.1.3 "><p id="p21075379172616"><a name="p21075379172616"></a><a name="p21075379172616"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.55%" headers="mcps1.2.5.1.4 "><p id="p4976396172616"><a name="p4976396172616"></a><a name="p4976396172616"></a>Zone ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section44958995161021"></a>

None

## Response<a name="section40090803161031"></a>

-   Parameter description

    **Table  2**  Parameters in the response

    <a name="table3873760215524"></a><table><thead align="left"><tr id="en-us_topic_0057310891_row54125868171039"><th class="cellrowborder" valign="top" width="17.990000000000002%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057310891_p46128019171039"><a name="en-us_topic_0057310891_p46128019171039"></a><a name="en-us_topic_0057310891_p46128019171039"></a><strong id="en-us_topic_0057310891_b162774213314533"><a name="en-us_topic_0057310891_b162774213314533"></a><a name="en-us_topic_0057310891_b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.77%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057310891_p61288737171039"><a name="en-us_topic_0057310891_p61288737171039"></a><a name="en-us_topic_0057310891_p61288737171039"></a><strong id="en-us_topic_0057310891_b84235270619112"><a name="en-us_topic_0057310891_b84235270619112"></a><a name="en-us_topic_0057310891_b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.239999999999995%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057310891_p39427830171039"><a name="en-us_topic_0057310891_p39427830171039"></a><a name="en-us_topic_0057310891_p39427830171039"></a><strong id="en-us_topic_0057310891_b842352706112423"><a name="en-us_topic_0057310891_b842352706112423"></a><a name="en-us_topic_0057310891_b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0057310891_row3275315171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057310891_p13677558171039"><a name="en-us_topic_0057310891_p13677558171039"></a><a name="en-us_topic_0057310891_p13677558171039"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057310891_p31480160171039"><a name="en-us_topic_0057310891_p31480160171039"></a><a name="en-us_topic_0057310891_p31480160171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057310891_p55186322171039"><a name="en-us_topic_0057310891_p55186322171039"></a><a name="en-us_topic_0057310891_p55186322171039"></a>Zone ID, which is a UUID used to identify the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057310891_row62038903171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057310891_p21725743171039"><a name="en-us_topic_0057310891_p21725743171039"></a><a name="en-us_topic_0057310891_p21725743171039"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057310891_p55078653171039"><a name="en-us_topic_0057310891_p55078653171039"></a><a name="en-us_topic_0057310891_p55078653171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057310891_p65545475171039"><a name="en-us_topic_0057310891_p65545475171039"></a><a name="en-us_topic_0057310891_p65545475171039"></a>Zone name</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057310891_row24663709171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057310891_p56112529171039"><a name="en-us_topic_0057310891_p56112529171039"></a><a name="en-us_topic_0057310891_p56112529171039"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057310891_p46656524171039"><a name="en-us_topic_0057310891_p46656524171039"></a><a name="en-us_topic_0057310891_p46656524171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057310891_p31778607171039"><a name="en-us_topic_0057310891_p31778607171039"></a><a name="en-us_topic_0057310891_p31778607171039"></a>Zone description</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057310891_row34212800171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057310891_p51657401171039"><a name="en-us_topic_0057310891_p51657401171039"></a><a name="en-us_topic_0057310891_p51657401171039"></a>email</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057310891_p336297171039"><a name="en-us_topic_0057310891_p336297171039"></a><a name="en-us_topic_0057310891_p336297171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057310891_p66322352171039"><a name="en-us_topic_0057310891_p66322352171039"></a><a name="en-us_topic_0057310891_p66322352171039"></a>Email address of the administrator managing the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057310891_row45341886171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057310891_p22374403171039"><a name="en-us_topic_0057310891_p22374403171039"></a><a name="en-us_topic_0057310891_p22374403171039"></a>zone_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057310891_p16323247171039"><a name="en-us_topic_0057310891_p16323247171039"></a><a name="en-us_topic_0057310891_p16323247171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057310891_p58527202171039"><a name="en-us_topic_0057310891_p58527202171039"></a><a name="en-us_topic_0057310891_p58527202171039"></a>Zone type, which can be <strong id="en-us_topic_0057310891_b842352706115152"><a name="en-us_topic_0057310891_b842352706115152"></a><a name="en-us_topic_0057310891_b842352706115152"></a>public</strong> or <strong id="en-us_topic_0057310891_b842352706115156"><a name="en-us_topic_0057310891_b842352706115156"></a><a name="en-us_topic_0057310891_b842352706115156"></a>private</strong></p>
    </td>
    </tr>
    <tr id="en-us_topic_0057310891_row36905265171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057310891_p4888971171039"><a name="en-us_topic_0057310891_p4888971171039"></a><a name="en-us_topic_0057310891_p4888971171039"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057310891_p16027579171039"><a name="en-us_topic_0057310891_p16027579171039"></a><a name="en-us_topic_0057310891_p16027579171039"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057310891_p41240291171039"><a name="en-us_topic_0057310891_p41240291171039"></a><a name="en-us_topic_0057310891_p41240291171039"></a>TTL value of the SOA record set in the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057310891_row29641334171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057310891_p63311148171039"><a name="en-us_topic_0057310891_p63311148171039"></a><a name="en-us_topic_0057310891_p63311148171039"></a>serial</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057310891_p26678057171039"><a name="en-us_topic_0057310891_p26678057171039"></a><a name="en-us_topic_0057310891_p26678057171039"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057310891_p7524749171039"><a name="en-us_topic_0057310891_p7524749171039"></a><a name="en-us_topic_0057310891_p7524749171039"></a>Serial number in the SOA record set in the zone, which identifies the change on the primary DNS server</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057310891_row44990376171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057310891_p30244483171039"><a name="en-us_topic_0057310891_p30244483171039"></a><a name="en-us_topic_0057310891_p30244483171039"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057310891_p47406357171039"><a name="en-us_topic_0057310891_p47406357171039"></a><a name="en-us_topic_0057310891_p47406357171039"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057310891_p9822846171039"><a name="en-us_topic_0057310891_p9822846171039"></a><a name="en-us_topic_0057310891_p9822846171039"></a>Resource status</p>
    <p id="en-us_topic_0057310891_p36239781171039"><a name="en-us_topic_0057310891_p36239781171039"></a><a name="en-us_topic_0057310891_p36239781171039"></a>The value can be <strong id="en-us_topic_0057310891_b84235270695628"><a name="en-us_topic_0057310891_b84235270695628"></a><a name="en-us_topic_0057310891_b84235270695628"></a>PENDING_CREATE</strong>, <strong id="en-us_topic_0057310891_b84235270695635"><a name="en-us_topic_0057310891_b84235270695635"></a><a name="en-us_topic_0057310891_b84235270695635"></a>ACTIVE</strong>, <strong id="en-us_topic_0057310891_b84235270695643"><a name="en-us_topic_0057310891_b84235270695643"></a><a name="en-us_topic_0057310891_b84235270695643"></a>PENDING_DELETE</strong>, or <strong id="en-us_topic_0057310891_b84235270695650"><a name="en-us_topic_0057310891_b84235270695650"></a><a name="en-us_topic_0057310891_b84235270695650"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057310891_row1454557171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057310891_p51202644171039"><a name="en-us_topic_0057310891_p51202644171039"></a><a name="en-us_topic_0057310891_p51202644171039"></a>record_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057310891_p32016130171039"><a name="en-us_topic_0057310891_p32016130171039"></a><a name="en-us_topic_0057310891_p32016130171039"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057310891_p53878535171039"><a name="en-us_topic_0057310891_p53878535171039"></a><a name="en-us_topic_0057310891_p53878535171039"></a>Number of record sets in the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057310891_row48476716171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057310891_p54136527171039"><a name="en-us_topic_0057310891_p54136527171039"></a><a name="en-us_topic_0057310891_p54136527171039"></a>pool_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057310891_p48020249171039"><a name="en-us_topic_0057310891_p48020249171039"></a><a name="en-us_topic_0057310891_p48020249171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057310891_p63987755171039"><a name="en-us_topic_0057310891_p63987755171039"></a><a name="en-us_topic_0057310891_p63987755171039"></a>Pool ID of the zone, which is assigned by the system</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057310891_row49967872171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057310891_p35791512171039"><a name="en-us_topic_0057310891_p35791512171039"></a><a name="en-us_topic_0057310891_p35791512171039"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057310891_p10454086171039"><a name="en-us_topic_0057310891_p10454086171039"></a><a name="en-us_topic_0057310891_p10454086171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057310891_p8704812171039"><a name="en-us_topic_0057310891_p8704812171039"></a><a name="en-us_topic_0057310891_p8704812171039"></a>Project ID of the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057310891_row27690345171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057310891_p48529730171039"><a name="en-us_topic_0057310891_p48529730171039"></a><a name="en-us_topic_0057310891_p48529730171039"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057310891_p59988242171039"><a name="en-us_topic_0057310891_p59988242171039"></a><a name="en-us_topic_0057310891_p59988242171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057310891_p9292793171039"><a name="en-us_topic_0057310891_p9292793171039"></a><a name="en-us_topic_0057310891_p9292793171039"></a>Time when the zone was created</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057310891_row4377608115654"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057310891_p5844041115654"><a name="en-us_topic_0057310891_p5844041115654"></a><a name="en-us_topic_0057310891_p5844041115654"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057310891_p3605288915654"><a name="en-us_topic_0057310891_p3605288915654"></a><a name="en-us_topic_0057310891_p3605288915654"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057310891_p3460290715654"><a name="en-us_topic_0057310891_p3460290715654"></a><a name="en-us_topic_0057310891_p3460290715654"></a>Time when the zone was updated</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057310891_row384676871572"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057310891_p288749251572"><a name="en-us_topic_0057310891_p288749251572"></a><a name="en-us_topic_0057310891_p288749251572"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057310891_p571676251572"><a name="en-us_topic_0057310891_p571676251572"></a><a name="en-us_topic_0057310891_p571676251572"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057310891_p59736855103137"><a name="en-us_topic_0057310891_p59736855103137"></a><a name="en-us_topic_0057310891_p59736855103137"></a>Link of the current resource or other related resources</p>
    <p id="en-us_topic_0057310891_p5462345019130"><a name="en-us_topic_0057310891_p5462345019130"></a><a name="en-us_topic_0057310891_p5462345019130"></a>When a response is broken into pages, a <strong id="en-us_topic_0057310891_b84235270695245"><a name="en-us_topic_0057310891_b84235270695245"></a><a name="en-us_topic_0057310891_b84235270695245"></a>next</strong> link is provided to retrieve all results.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057310891_row177328815945"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057310891_p1595959815945"><a name="en-us_topic_0057310891_p1595959815945"></a><a name="en-us_topic_0057310891_p1595959815945"></a>masters</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057310891_p1765902715945"><a name="en-us_topic_0057310891_p1765902715945"></a><a name="en-us_topic_0057310891_p1765902715945"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057310891_p2109506015945"><a name="en-us_topic_0057310891_p2109506015945"></a><a name="en-us_topic_0057310891_p2109506015945"></a>Master DNS servers, from which the slave servers get DNS information</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Response example

    ```
    {
        "id": "2c9eb155587194ec01587224c9f90149",
        "name": "example.com.",
        "description": "This is an example zone.",
        "email": "xx@example.com",
        "ttl": 300,
        "serial": 1,
        "masters": [],
        "status": "PENDING_DELETE",
        "links": {
            "self": "https://Endpoint/v2/zones/2c9eb155587194ec01587224c9f90149"
        },
        "pool_id": "00000000570e54ee01570e9939b20019",
        "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c",
        "zone_type": "public",
        "created_at": "2016-11-17T11:56:03.439",
        "updated_at": "2016-11-17T11:56:05.057",
        "record_num": 0
    }
    ```


## Returned Value<a name="section42637797161043"></a>

See  [General Request Return Code](general-request-return-code.md).

