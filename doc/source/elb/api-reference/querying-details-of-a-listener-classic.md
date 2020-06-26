# Querying Details of a Listener<a name="EN-US_TOPIC_0096561509"></a>

## Function<a name="en-us_topic_0020100161_section39312736"></a>

This API is used to query details about a listener.

## URI<a name="en-us_topic_0020100161_section18270305"></a>

GET /v1.0/\{project\_id\}/elbaas/listeners/\{listener\_id\}

**Table  1**  Parameter description

<a name="en-us_topic_0020100161_table24807479"></a>
<table><thead align="left"><tr id="en-us_topic_0020100161_row41130254"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020100161_p43216271"><a name="en-us_topic_0020100161_p43216271"></a><a name="en-us_topic_0020100161_p43216271"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100161_p10857028"><a name="en-us_topic_0020100161_p10857028"></a><a name="en-us_topic_0020100161_p10857028"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100161_p35310798115034"><a name="en-us_topic_0020100161_p35310798115034"></a><a name="en-us_topic_0020100161_p35310798115034"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020100161_p7004053"><a name="en-us_topic_0020100161_p7004053"></a><a name="en-us_topic_0020100161_p7004053"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020100161_row66239429113333"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100161_p59283951113333"><a name="en-us_topic_0020100161_p59283951113333"></a><a name="en-us_topic_0020100161_p59283951113333"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100161_p37270754113333"><a name="en-us_topic_0020100161_p37270754113333"></a><a name="en-us_topic_0020100161_p37270754113333"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100161_p46026982115034"><a name="en-us_topic_0020100161_p46026982115034"></a><a name="en-us_topic_0020100161_p46026982115034"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100161_p66141077113333"><a name="en-us_topic_0020100161_p66141077113333"></a><a name="en-us_topic_0020100161_p66141077113333"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
<tr id="en-us_topic_0020100161_row30457452"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100161_p51134510"><a name="en-us_topic_0020100161_p51134510"></a><a name="en-us_topic_0020100161_p51134510"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100161_p48254661"><a name="en-us_topic_0020100161_p48254661"></a><a name="en-us_topic_0020100161_p48254661"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100161_p45281603115034"><a name="en-us_topic_0020100161_p45281603115034"></a><a name="en-us_topic_0020100161_p45281603115034"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100161_p16313497"><a name="en-us_topic_0020100161_p16313497"></a><a name="en-us_topic_0020100161_p16313497"></a>Specifies the listener ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020100161_section30215023"></a>

-   Request parameters

    None


-   Example request

    None


## Response<a name="en-us_topic_0020100161_section3499754"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="en-us_topic_0020100161_table21841875164110"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100161_row49453524164110"><th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100161_p46312512164110"><a name="en-us_topic_0020100161_p46312512164110"></a><a name="en-us_topic_0020100161_p46312512164110"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100161_p60325988164110"><a name="en-us_topic_0020100161_p60325988164110"></a><a name="en-us_topic_0020100161_p60325988164110"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="69.69696969696969%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100161_p54566889164110"><a name="en-us_topic_0020100161_p54566889164110"></a><a name="en-us_topic_0020100161_p54566889164110"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100161_row57841911164110"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p54683189164110"><a name="en-us_topic_0020100161_p54683189164110"></a><a name="en-us_topic_0020100161_p54683189164110"></a>update_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p153291164110"><a name="en-us_topic_0020100161_p153291164110"></a><a name="en-us_topic_0020100161_p153291164110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p12416610164110"><a name="en-us_topic_0020100161_p12416610164110"></a><a name="en-us_topic_0020100161_p12416610164110"></a>Specifies the time when the listener was updated.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row44640629164110"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p59121200164110"><a name="en-us_topic_0020100161_p59121200164110"></a><a name="en-us_topic_0020100161_p59121200164110"></a>backend_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p24087871164110"><a name="en-us_topic_0020100161_p24087871164110"></a><a name="en-us_topic_0020100161_p24087871164110"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p4960523164110"><a name="en-us_topic_0020100161_p4960523164110"></a><a name="en-us_topic_0020100161_p4960523164110"></a>Specifies the port used by backend ECSs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row44644707164110"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p59451476164110"><a name="en-us_topic_0020100161_p59451476164110"></a><a name="en-us_topic_0020100161_p59451476164110"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p50840246164110"><a name="en-us_topic_0020100161_p50840246164110"></a><a name="en-us_topic_0020100161_p50840246164110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p24419248164110"><a name="en-us_topic_0020100161_p24419248164110"></a><a name="en-us_topic_0020100161_p24419248164110"></a>Specifies the listener ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row18446646164110"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p17783368164110"><a name="en-us_topic_0020100161_p17783368164110"></a><a name="en-us_topic_0020100161_p17783368164110"></a>backend_protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p31166727164110"><a name="en-us_topic_0020100161_p31166727164110"></a><a name="en-us_topic_0020100161_p31166727164110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p41476954164110"><a name="en-us_topic_0020100161_p41476954164110"></a><a name="en-us_topic_0020100161_p41476954164110"></a>Specifies the protocol used by backend ECSs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row37748271164110"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p37711100164110"><a name="en-us_topic_0020100161_p37711100164110"></a><a name="en-us_topic_0020100161_p37711100164110"></a>sticky_session_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p34700241164110"><a name="en-us_topic_0020100161_p34700241164110"></a><a name="en-us_topic_0020100161_p34700241164110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="p1658610645719"><a name="p1658610645719"></a><a name="p1658610645719"></a>Specifies where the cookie is from. The only value is <strong id="b1758619617573"><a name="b1758619617573"></a><a name="b1758619617573"></a>insert</strong>, indicating that the cookie is inserted by the load balancer.</p>
    <a name="ul197928120572"></a><a name="ul197928120572"></a><ul id="ul197928120572"><li>This parameter is valid when <strong id="b179241235713"><a name="b179241235713"></a><a name="b179241235713"></a>protocol</strong> is set to <strong id="b47921124573"><a name="b47921124573"></a><a name="b47921124573"></a>HTTP</strong> and <strong id="b0792131215579"><a name="b0792131215579"></a><a name="b0792131215579"></a>session_sticky</strong> to <strong id="b16792161218571"><a name="b16792161218571"></a><a name="b16792161218571"></a>true</strong>. The default value is <strong id="b17792212145711"><a name="b17792212145711"></a><a name="b17792212145711"></a>insert</strong>.</li><li>This parameter is invalid when <strong id="b1889921410573"><a name="b1889921410573"></a><a name="b1889921410573"></a>protocol</strong> is set to <strong id="b4899171416576"><a name="b4899171416576"></a><a name="b4899171416576"></a>TCP</strong>, which means that the parameter is unavailable or its value is set to <strong id="b11899161412573"><a name="b11899161412573"></a><a name="b11899161412573"></a>null</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row63543316164110"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p46734949164110"><a name="en-us_topic_0020100161_p46734949164110"></a><a name="en-us_topic_0020100161_p46734949164110"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p27434556164110"><a name="en-us_topic_0020100161_p27434556164110"></a><a name="en-us_topic_0020100161_p27434556164110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p7606526164110"><a name="en-us_topic_0020100161_p7606526164110"></a><a name="en-us_topic_0020100161_p7606526164110"></a>Provides supplementary information about the listener.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row1349876164110"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p42231108164110"><a name="en-us_topic_0020100161_p42231108164110"></a><a name="en-us_topic_0020100161_p42231108164110"></a>loadbalancer_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p65276597164110"><a name="en-us_topic_0020100161_p65276597164110"></a><a name="en-us_topic_0020100161_p65276597164110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p52913006164110"><a name="en-us_topic_0020100161_p52913006164110"></a><a name="en-us_topic_0020100161_p52913006164110"></a>Specifies the load balancer ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row6455014164110"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p53094111164110"><a name="en-us_topic_0020100161_p53094111164110"></a><a name="en-us_topic_0020100161_p53094111164110"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p5655733164110"><a name="en-us_topic_0020100161_p5655733164110"></a><a name="en-us_topic_0020100161_p5655733164110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p55461199164110"><a name="en-us_topic_0020100161_p55461199164110"></a><a name="en-us_topic_0020100161_p55461199164110"></a>Specifies the time when the listener was created.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row29388745164110"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p31678149164110"><a name="en-us_topic_0020100161_p31678149164110"></a><a name="en-us_topic_0020100161_p31678149164110"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p15793273164110"><a name="en-us_topic_0020100161_p15793273164110"></a><a name="en-us_topic_0020100161_p15793273164110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p4186766164110"><a name="en-us_topic_0020100161_p4186766164110"></a><a name="en-us_topic_0020100161_p4186766164110"></a>Specifies the listener status. The value can be <strong id="b84235270693852"><a name="b84235270693852"></a><a name="b84235270693852"></a>ACTIVE</strong>, <strong id="b84235270693858"><a name="b84235270693858"></a><a name="b84235270693858"></a>PENDING_CREATE</strong>, or <strong id="b8423527069394"><a name="b8423527069394"></a><a name="b8423527069394"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row37680900164110"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p32254093164110"><a name="en-us_topic_0020100161_p32254093164110"></a><a name="en-us_topic_0020100161_p32254093164110"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p62444746164110"><a name="en-us_topic_0020100161_p62444746164110"></a><a name="en-us_topic_0020100161_p62444746164110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p24859684164110"><a name="en-us_topic_0020100161_p24859684164110"></a><a name="en-us_topic_0020100161_p24859684164110"></a>Specifies the protocol used for load balancing at Layer 4 or Layer 7.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row22410567164110"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p3316630164110"><a name="en-us_topic_0020100161_p3316630164110"></a><a name="en-us_topic_0020100161_p3316630164110"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p211638164110"><a name="en-us_topic_0020100161_p211638164110"></a><a name="en-us_topic_0020100161_p211638164110"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p17142735164110"><a name="en-us_topic_0020100161_p17142735164110"></a><a name="en-us_topic_0020100161_p17142735164110"></a>Specifies the port used by the load balancer.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row20066888164110"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p14805192164110"><a name="en-us_topic_0020100161_p14805192164110"></a><a name="en-us_topic_0020100161_p14805192164110"></a>cookie_timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p58369876164110"><a name="en-us_topic_0020100161_p58369876164110"></a><a name="en-us_topic_0020100161_p58369876164110"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100161_ul52834495115553"></a><a name="en-us_topic_0020100161_ul52834495115553"></a><ul id="en-us_topic_0020100161_ul52834495115553"><li>Specifies the cookie timeout duration. This parameter is valid when <strong>session_sticky</strong> is set to <strong>true</strong> and <strong>sticky_session_type</strong> to <strong>insert</strong>.</li><li>The value ranges from <strong id="b1583831004720"><a name="b1583831004720"></a><a name="b1583831004720"></a>1</strong> to <strong id="b758231416478"><a name="b758231416478"></a><a name="b758231416478"></a>1440</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row4620421164110"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p38709840164110"><a name="en-us_topic_0020100161_p38709840164110"></a><a name="en-us_topic_0020100161_p38709840164110"></a>admin_state_up</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p48489348164110"><a name="en-us_topic_0020100161_p48489348164110"></a><a name="en-us_topic_0020100161_p48489348164110"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100161_ul5987677212259"></a><a name="en-us_topic_0020100161_ul5987677212259"></a><ul id="en-us_topic_0020100161_ul5987677212259"><li>Specifies the administrative status of the load balancer.</li><li>Two options are available:<p id="en-us_topic_0020100161_p2940550812259"><a name="en-us_topic_0020100161_p2940550812259"></a><a name="en-us_topic_0020100161_p2940550812259"></a><strong id="b84235270615441"><a name="b84235270615441"></a><a name="b84235270615441"></a>false</strong>: The load balancer is disabled.</p>
    <p id="en-us_topic_0020100161_p10214835123026"><a name="en-us_topic_0020100161_p10214835123026"></a><a name="en-us_topic_0020100161_p10214835123026"></a><strong id="b842352706154416"><a name="b842352706154416"></a><a name="b842352706154416"></a>true</strong>: The load balancer is working properly.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row2090154119852"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p3777002619857"><a name="en-us_topic_0020100161_p3777002619857"></a><a name="en-us_topic_0020100161_p3777002619857"></a>member_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p3947326519857"><a name="en-us_topic_0020100161_p3947326519857"></a><a name="en-us_topic_0020100161_p3947326519857"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p4321788819857"><a name="en-us_topic_0020100161_p4321788819857"></a><a name="en-us_topic_0020100161_p4321788819857"></a>Specifies the quantity of backend ECSs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row64144780112559"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p4796951911264"><a name="en-us_topic_0020100161_p4796951911264"></a><a name="en-us_topic_0020100161_p4796951911264"></a>healthcheck_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p6032580011264"><a name="en-us_topic_0020100161_p6032580011264"></a><a name="en-us_topic_0020100161_p6032580011264"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p5455159311264"><a name="en-us_topic_0020100161_p5455159311264"></a><a name="en-us_topic_0020100161_p5455159311264"></a>Specifies the health check ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row49472263164110"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p47830375164110"><a name="en-us_topic_0020100161_p47830375164110"></a><a name="en-us_topic_0020100161_p47830375164110"></a>session_sticky</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p49055147164110"><a name="en-us_topic_0020100161_p49055147164110"></a><a name="en-us_topic_0020100161_p49055147164110"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p14043964164110"><a name="en-us_topic_0020100161_p14043964164110"></a><a name="en-us_topic_0020100161_p14043964164110"></a>Specifies whether to enable the sticky session feature. The feature is enabled when the value is <strong id="b3064351115846"><a name="b3064351115846"></a><a name="b3064351115846"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row59286812164110"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p37502474164110"><a name="en-us_topic_0020100161_p37502474164110"></a><a name="en-us_topic_0020100161_p37502474164110"></a>lb_algorithm</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p17801593164110"><a name="en-us_topic_0020100161_p17801593164110"></a><a name="en-us_topic_0020100161_p17801593164110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p32642961164110"><a name="en-us_topic_0020100161_p32642961164110"></a><a name="en-us_topic_0020100161_p32642961164110"></a>Specifies the load balancing algorithm.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row25351195164110"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p40180930164110"><a name="en-us_topic_0020100161_p40180930164110"></a><a name="en-us_topic_0020100161_p40180930164110"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p33429926164110"><a name="en-us_topic_0020100161_p33429926164110"></a><a name="en-us_topic_0020100161_p33429926164110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p23469486164110"><a name="en-us_topic_0020100161_p23469486164110"></a><a name="en-us_topic_0020100161_p23469486164110"></a>Specifies the listener name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row33327498192714"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p43443366192720"><a name="en-us_topic_0020100161_p43443366192720"></a><a name="en-us_topic_0020100161_p43443366192720"></a>certificate_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p29251771192720"><a name="en-us_topic_0020100161_p29251771192720"></a><a name="en-us_topic_0020100161_p29251771192720"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p2448247391051"><a name="en-us_topic_0020100161_p2448247391051"></a><a name="en-us_topic_0020100161_p2448247391051"></a>Specifies the ID of the SSL certificate for security authentication.</p>
    <p id="en-us_topic_0020100161_p20583236192720"><a name="en-us_topic_0020100161_p20583236192720"></a><a name="en-us_topic_0020100161_p20583236192720"></a>This parameter is mandatory when <strong id="b8423527061428"><a name="b8423527061428"></a><a name="b8423527061428"></a>protocol</strong> is set to <strong id="b84235270614212"><a name="b84235270614212"></a><a name="b84235270614212"></a>HTTPS</strong> or <strong id="b842352706182053"><a name="b842352706182053"></a><a name="b842352706182053"></a>SSL</strong>. Otherwise, the parameter value is <strong id="b4428435195955"><a name="b4428435195955"></a><a name="b4428435195955"></a>null</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row248033919946"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p2979576119949"><a name="en-us_topic_0020100161_p2979576119949"></a><a name="en-us_topic_0020100161_p2979576119949"></a>certificates</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="p8839294545"><a name="p8839294545"></a><a name="p8839294545"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p186894719949"><a name="en-us_topic_0020100161_p186894719949"></a><a name="en-us_topic_0020100161_p186894719949"></a>Lists the certificate IDs if <strong id="b842352706172631"><a name="b842352706172631"></a><a name="b842352706172631"></a>protocol</strong> is set to <strong id="b842352706172635"><a name="b842352706172635"></a><a name="b842352706172635"></a>HTTPS</strong>.</p>
    <p id="en-us_topic_0020100161_p1682052319949"><a name="en-us_topic_0020100161_p1682052319949"></a><a name="en-us_topic_0020100161_p1682052319949"></a>This parameter is mandatory in the SNI scenario.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row2857241511335"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p3501719911346"><a name="en-us_topic_0020100161_p3501719911346"></a><a name="en-us_topic_0020100161_p3501719911346"></a>tcp_timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p1782086711346"><a name="en-us_topic_0020100161_p1782086711346"></a><a name="en-us_topic_0020100161_p1782086711346"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p3420415211346"><a name="en-us_topic_0020100161_p3420415211346"></a><a name="en-us_topic_0020100161_p3420415211346"></a>Specifies the TCP session timeout duration.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row1020606011429"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p2252811211437"><a name="en-us_topic_0020100161_p2252811211437"></a><a name="en-us_topic_0020100161_p2252811211437"></a>udp_timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p1283775011437"><a name="en-us_topic_0020100161_p1283775011437"></a><a name="en-us_topic_0020100161_p1283775011437"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p3322482911437"><a name="en-us_topic_0020100161_p3322482911437"></a><a name="en-us_topic_0020100161_p3322482911437"></a>Specifies the UDP session timeout duration.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row843217395836"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p5418358395845"><a name="en-us_topic_0020100161_p5418358395845"></a><a name="en-us_topic_0020100161_p5418358395845"></a>ssl_protocols</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p2679406595845"><a name="en-us_topic_0020100161_p2679406595845"></a><a name="en-us_topic_0020100161_p2679406595845"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p2283567295845"><a name="en-us_topic_0020100161_p2283567295845"></a><a name="en-us_topic_0020100161_p2283567295845"></a>Specifies the supported SSL/TLS protocol version. This parameter is available only when <strong id="b842352706173219"><a name="b842352706173219"></a><a name="b842352706173219"></a>protocol</strong> is set to <strong id="b842352706173222"><a name="b842352706173222"></a><a name="b842352706173222"></a>HTTPS</strong> or <strong id="b842352706181923"><a name="b842352706181923"></a><a name="b842352706181923"></a>SSL</strong>.</p>
    <div class="note" id="en-us_topic_0020100161_note519440195935"><a name="en-us_topic_0020100161_note519440195935"></a><a name="en-us_topic_0020100161_note519440195935"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0020100161_p4674961395935"><a name="en-us_topic_0020100161_p4674961395935"></a><a name="en-us_topic_0020100161_p4674961395935"></a>For HTTPS listeners in versions earlier than 1.2.8, the parameter value is <strong id="b842352706105023"><a name="b842352706105023"></a><a name="b842352706105023"></a>TLSv1.2</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row6523375895841"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100161_p3786509295845"><a name="en-us_topic_0020100161_p3786509295845"></a><a name="en-us_topic_0020100161_p3786509295845"></a>ssl_ciphers</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100161_p4717362595845"><a name="en-us_topic_0020100161_p4717362595845"></a><a name="en-us_topic_0020100161_p4717362595845"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100161_p6296726695845"><a name="en-us_topic_0020100161_p6296726695845"></a><a name="en-us_topic_0020100161_p6296726695845"></a>Specifies the cipher suite of an encryption protocol. This parameter is available only when <strong id="b842352706173219_1"><a name="b842352706173219_1"></a><a name="b842352706173219_1"></a>protocol</strong> is set to <strong id="b842352706173222_1"><a name="b842352706173222_1"></a><a name="b842352706173222_1"></a>HTTPS</strong> or <strong id="b842352706181923_1"><a name="b842352706181923_1"></a><a name="b842352706181923_1"></a>SSL</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "update_time": "2015-09-15 07:41:17",
        "backend_port": 80,
        "id": "248425d7b97dc26920eb23720115e068",
        "backend_protocol": "TCP",
        "sticky_session_type": "insert",
        "description": "",
        "loadbalancer_id": "0b07acf06d243925bc24a0ac7445267a",
        "create_time": "2015-09-15 07:41:17",
        "status": "ACTIVE",
        "protocol": "TCP",
        "port": 88,
        "cookie_timeout": 100,
        "admin_state_up": true,
        "member_number": 0,
        "healthcheck_id": null,
        "session_sticky": true,
        "lb_algorithm": "roundrobin",
        "name": "listener1",
        "tcp_draining": true,
        "tcp_draining_timeout": 5
    }
    
    ```

    ```
    {
         "update_time": "2016-12-01 07:12:59",
         "backend_port": 9090,
         "id": "a824584fb3ba4d39ba0cf372c7cbbb67",
         "backend_protocol": "TCP",
         "sticky_session_type": null,
         "certificate_id": null,
         "description": "",
         "loadbalancer_id": "f54c65b1b5dd4a4f95b71b44796ac013",
         "lb_algorithm": "roundrobin",
         "create_time": "2016-12-01 07:12:43",
         "admin_state_up": false,
         "status": "ACTIVE",
         "protocol": "TCP",
         "cookie_timeout": 100,
         "port": 9092,
         "tcp_draining": 1,
         "tcp_timeout": 1,
         "member_number": 0,
         "healthcheck_id": null,
         "session_sticky": true,
         "tcp_draining_timeout": 5,
         "name": "lis"
    }
    ```


## Status Code<a name="en-us_topic_0020100161_section31497787"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0020100161_table498354015158"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100161_row73937115158"><th class="cellrowborder" valign="top" width="12.520000000000001%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020100161_p5988906115158"><a name="en-us_topic_0020100161_p5988906115158"></a><a name="en-us_topic_0020100161_p5988906115158"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.18%" id="mcps1.1.4.1.2"><p id="p01993423451"><a name="p01993423451"></a><a name="p01993423451"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.300000000000004%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020100161_p1917575515158"><a name="en-us_topic_0020100161_p1917575515158"></a><a name="en-us_topic_0020100161_p1917575515158"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100161_row973235915158"><td class="cellrowborder" valign="top" width="12.520000000000001%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100161_p5012358215158"><a name="en-us_topic_0020100161_p5012358215158"></a><a name="en-us_topic_0020100161_p5012358215158"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.18%" headers="mcps1.1.4.1.2 "><p id="p20293059164518"><a name="p20293059164518"></a><a name="p20293059164518"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.300000000000004%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100161_p3347836215158"><a name="en-us_topic_0020100161_p3347836215158"></a><a name="en-us_topic_0020100161_p3347836215158"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row3286981015158"><td class="cellrowborder" valign="top" width="12.520000000000001%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100161_p4520892815158"><a name="en-us_topic_0020100161_p4520892815158"></a><a name="en-us_topic_0020100161_p4520892815158"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.18%" headers="mcps1.1.4.1.2 "><p id="p429355944512"><a name="p429355944512"></a><a name="p429355944512"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.300000000000004%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100161_p3804451815158"><a name="en-us_topic_0020100161_p3804451815158"></a><a name="en-us_topic_0020100161_p3804451815158"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row685634615158"><td class="cellrowborder" valign="top" width="12.520000000000001%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100161_p1849314415158"><a name="en-us_topic_0020100161_p1849314415158"></a><a name="en-us_topic_0020100161_p1849314415158"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.18%" headers="mcps1.1.4.1.2 "><p id="p429395984516"><a name="p429395984516"></a><a name="p429395984516"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.300000000000004%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100161_p2154969915158"><a name="en-us_topic_0020100161_p2154969915158"></a><a name="en-us_topic_0020100161_p2154969915158"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row5972956415158"><td class="cellrowborder" valign="top" width="12.520000000000001%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100161_p625653315158"><a name="en-us_topic_0020100161_p625653315158"></a><a name="en-us_topic_0020100161_p625653315158"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.18%" headers="mcps1.1.4.1.2 "><p id="p1129345904518"><a name="p1129345904518"></a><a name="p1129345904518"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.300000000000004%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100161_p3701713415158"><a name="en-us_topic_0020100161_p3701713415158"></a><a name="en-us_topic_0020100161_p3701713415158"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row6471875015158"><td class="cellrowborder" valign="top" width="12.520000000000001%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100161_p772737015158"><a name="en-us_topic_0020100161_p772737015158"></a><a name="en-us_topic_0020100161_p772737015158"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.18%" headers="mcps1.1.4.1.2 "><p id="p10294105912458"><a name="p10294105912458"></a><a name="p10294105912458"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.300000000000004%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100161_p2193725915158"><a name="en-us_topic_0020100161_p2193725915158"></a><a name="en-us_topic_0020100161_p2193725915158"></a>System error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100161_row6321761115158"><td class="cellrowborder" valign="top" width="12.520000000000001%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100161_p2035288615158"><a name="en-us_topic_0020100161_p2035288615158"></a><a name="en-us_topic_0020100161_p2035288615158"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.18%" headers="mcps1.1.4.1.2 "><p id="p19294659144511"><a name="p19294659144511"></a><a name="p19294659144511"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.300000000000004%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100161_p3797108215158"><a name="en-us_topic_0020100161_p3797108215158"></a><a name="en-us_topic_0020100161_p3797108215158"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


