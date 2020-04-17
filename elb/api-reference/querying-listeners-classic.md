# Querying Listeners<a name="EN-US_TOPIC_0096561510"></a>

## Function<a name="en-us_topic_0020100162_section37418306"></a>

This API is used to query listeners using search criteria and display them in a list.

## URI<a name="en-us_topic_0020100162_section1220438"></a>

GET /v1.0/\{project\_id\}/elbaas/listeners?loadbalancer\_id=\{loadbalancer\_id\}

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Enter a question mark \(?\) and an ampersand \(&\) at the end of the URI to define multiple search criteria. You can filter the listeners using the parameters in the response except  **update\_time**,  **create\_time**,  **admin\_state\_up**,  **session\_sticky**, and  **member\_number**.  

**Table  1**  Parameter description

<a name="en-us_topic_0020100162_table40156824113847"></a>
<table><thead align="left"><tr id="en-us_topic_0020100162_row28632303113847"><th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.1"><p id="p971216213460"><a name="p971216213460"></a><a name="p971216213460"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100162_p18833862113847"><a name="en-us_topic_0020100162_p18833862113847"></a><a name="en-us_topic_0020100162_p18833862113847"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100162_p18185448115120"><a name="en-us_topic_0020100162_p18185448115120"></a><a name="en-us_topic_0020100162_p18185448115120"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="59.4059405940594%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020100162_p49147891113847"><a name="en-us_topic_0020100162_p49147891113847"></a><a name="en-us_topic_0020100162_p49147891113847"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020100162_row21556224113847"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="p10688163320115"><a name="p10688163320115"></a><a name="p10688163320115"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100162_p32010971113847"><a name="en-us_topic_0020100162_p32010971113847"></a><a name="en-us_topic_0020100162_p32010971113847"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100162_p62274653115120"><a name="en-us_topic_0020100162_p62274653115120"></a><a name="en-us_topic_0020100162_p62274653115120"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.4059405940594%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100162_p42751865113847"><a name="en-us_topic_0020100162_p42751865113847"></a><a name="en-us_topic_0020100162_p42751865113847"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
<tr id="en-us_topic_0020100162_row2101084210316"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100162_p3840472210316"><a name="en-us_topic_0020100162_p3840472210316"></a><a name="en-us_topic_0020100162_p3840472210316"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100162_p6512056110322"><a name="en-us_topic_0020100162_p6512056110322"></a><a name="en-us_topic_0020100162_p6512056110322"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100162_p4249522510325"><a name="en-us_topic_0020100162_p4249522510325"></a><a name="en-us_topic_0020100162_p4249522510325"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.4059405940594%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100162_p1956118510325"><a name="en-us_topic_0020100162_p1956118510325"></a><a name="en-us_topic_0020100162_p1956118510325"></a>Specifies the load balancer ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020100162_section10983950"></a>

-   Request parameters

    None


-   Example request

    None


## Response<a name="en-us_topic_0020100162_section31746690"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="en-us_topic_0020100162_table731543415476"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100162_row3827659115476"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100162_p1339613215476"><a name="en-us_topic_0020100162_p1339613215476"></a><a name="en-us_topic_0020100162_p1339613215476"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100162_p10520793193014"><a name="en-us_topic_0020100162_p10520793193014"></a><a name="en-us_topic_0020100162_p10520793193014"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="72%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100162_p4652052415476"><a name="en-us_topic_0020100162_p4652052415476"></a><a name="en-us_topic_0020100162_p4652052415476"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100162_row1006606215476"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p25265545114026"><a name="en-us_topic_0020100162_p25265545114026"></a><a name="en-us_topic_0020100162_p25265545114026"></a>update_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p33243230114026"><a name="en-us_topic_0020100162_p33243230114026"></a><a name="en-us_topic_0020100162_p33243230114026"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p8347087114026"><a name="en-us_topic_0020100162_p8347087114026"></a><a name="en-us_topic_0020100162_p8347087114026"></a>Specifies the time when the listener was updated.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row2193164615476"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p45229302114026"><a name="en-us_topic_0020100162_p45229302114026"></a><a name="en-us_topic_0020100162_p45229302114026"></a>backend_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p39694830114026"><a name="en-us_topic_0020100162_p39694830114026"></a><a name="en-us_topic_0020100162_p39694830114026"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p61164638114026"><a name="en-us_topic_0020100162_p61164638114026"></a><a name="en-us_topic_0020100162_p61164638114026"></a>Specifies the port used by backend ECSs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row5227516715476"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p28735851114026"><a name="en-us_topic_0020100162_p28735851114026"></a><a name="en-us_topic_0020100162_p28735851114026"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p45902608114026"><a name="en-us_topic_0020100162_p45902608114026"></a><a name="en-us_topic_0020100162_p45902608114026"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p27123753114026"><a name="en-us_topic_0020100162_p27123753114026"></a><a name="en-us_topic_0020100162_p27123753114026"></a>Specifies the listener ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row5719055815476"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p43210264114026"><a name="en-us_topic_0020100162_p43210264114026"></a><a name="en-us_topic_0020100162_p43210264114026"></a>backend_protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p10370467114026"><a name="en-us_topic_0020100162_p10370467114026"></a><a name="en-us_topic_0020100162_p10370467114026"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p34701503114026"><a name="en-us_topic_0020100162_p34701503114026"></a><a name="en-us_topic_0020100162_p34701503114026"></a>Specifies the protocol used by backend ECSs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row4106693215476"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p64463154114026"><a name="en-us_topic_0020100162_p64463154114026"></a><a name="en-us_topic_0020100162_p64463154114026"></a>sticky_session_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p54133006114026"><a name="en-us_topic_0020100162_p54133006114026"></a><a name="en-us_topic_0020100162_p54133006114026"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="p5421817203913"><a name="p5421817203913"></a><a name="p5421817203913"></a>Specifies where the cookie is from. The only value is <strong id="b142181753919"><a name="b142181753919"></a><a name="b142181753919"></a>insert</strong>, indicating that the cookie is inserted by the load balancer.</p>
    <a name="ul3229192416394"></a><a name="ul3229192416394"></a><ul id="ul3229192416394"><li>This parameter is valid when <strong id="b18229624163915"><a name="b18229624163915"></a><a name="b18229624163915"></a>protocol</strong> is set to <strong id="b322920241396"><a name="b322920241396"></a><a name="b322920241396"></a>HTTP</strong> and <strong id="b1522952417391"><a name="b1522952417391"></a><a name="b1522952417391"></a>session_sticky</strong> to <strong id="b42292024143915"><a name="b42292024143915"></a><a name="b42292024143915"></a>true</strong>. The default value is <strong id="b322952423919"><a name="b322952423919"></a><a name="b322952423919"></a>insert</strong>.</li><li>This parameter is invalid when <strong id="b5327526163911"><a name="b5327526163911"></a><a name="b5327526163911"></a>protocol</strong> is set to <strong id="b163285267393"><a name="b163285267393"></a><a name="b163285267393"></a>TCP</strong>, which means that the parameter is unavailable or its value is set to <strong id="b4328142614392"><a name="b4328142614392"></a><a name="b4328142614392"></a>null</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row5802723115476"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p37623738114026"><a name="en-us_topic_0020100162_p37623738114026"></a><a name="en-us_topic_0020100162_p37623738114026"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p27623937114026"><a name="en-us_topic_0020100162_p27623937114026"></a><a name="en-us_topic_0020100162_p27623937114026"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p22946416114026"><a name="en-us_topic_0020100162_p22946416114026"></a><a name="en-us_topic_0020100162_p22946416114026"></a>Provides supplementary information about the listener.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row5028106115476"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p17830710114026"><a name="en-us_topic_0020100162_p17830710114026"></a><a name="en-us_topic_0020100162_p17830710114026"></a>loadbalancer_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p35001394114026"><a name="en-us_topic_0020100162_p35001394114026"></a><a name="en-us_topic_0020100162_p35001394114026"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p16540626114026"><a name="en-us_topic_0020100162_p16540626114026"></a><a name="en-us_topic_0020100162_p16540626114026"></a>Specifies the load balancer ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row2637640715476"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p45629813114026"><a name="en-us_topic_0020100162_p45629813114026"></a><a name="en-us_topic_0020100162_p45629813114026"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p5027359114026"><a name="en-us_topic_0020100162_p5027359114026"></a><a name="en-us_topic_0020100162_p5027359114026"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p4562954114026"><a name="en-us_topic_0020100162_p4562954114026"></a><a name="en-us_topic_0020100162_p4562954114026"></a>Specifies the time when the listener was created.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row5790894015476"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p38059598114026"><a name="en-us_topic_0020100162_p38059598114026"></a><a name="en-us_topic_0020100162_p38059598114026"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p62928593114026"><a name="en-us_topic_0020100162_p62928593114026"></a><a name="en-us_topic_0020100162_p62928593114026"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p64051281114026"><a name="en-us_topic_0020100162_p64051281114026"></a><a name="en-us_topic_0020100162_p64051281114026"></a>Specifies the listener status. The value can be <strong id="b84235270693852"><a name="b84235270693852"></a><a name="b84235270693852"></a>ACTIVE</strong>, <strong id="b84235270693858"><a name="b84235270693858"></a><a name="b84235270693858"></a>PENDING_CREATE</strong>, or <strong id="b8423527069394"><a name="b8423527069394"></a><a name="b8423527069394"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row573753415476"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p52723552114026"><a name="en-us_topic_0020100162_p52723552114026"></a><a name="en-us_topic_0020100162_p52723552114026"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p42749334114026"><a name="en-us_topic_0020100162_p42749334114026"></a><a name="en-us_topic_0020100162_p42749334114026"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p40144036114026"><a name="en-us_topic_0020100162_p40144036114026"></a><a name="en-us_topic_0020100162_p40144036114026"></a>Specifies the protocol used for load balancing at Layer 4 or Layer 7.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row2530427515476"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p44601764114144"><a name="en-us_topic_0020100162_p44601764114144"></a><a name="en-us_topic_0020100162_p44601764114144"></a>lb_algorithm</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p55973152114144"><a name="en-us_topic_0020100162_p55973152114144"></a><a name="en-us_topic_0020100162_p55973152114144"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p37531497114144"><a name="en-us_topic_0020100162_p37531497114144"></a><a name="en-us_topic_0020100162_p37531497114144"></a>Specifies the load balancing algorithm.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row241883715476"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p1986814811428"><a name="en-us_topic_0020100162_p1986814811428"></a><a name="en-us_topic_0020100162_p1986814811428"></a>admin_state_up</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p6581611911428"><a name="en-us_topic_0020100162_p6581611911428"></a><a name="en-us_topic_0020100162_p6581611911428"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100162_ul4756691122651"></a><a name="en-us_topic_0020100162_ul4756691122651"></a><ul id="en-us_topic_0020100162_ul4756691122651"><li>Specifies the administrative status of the load balancer.</li><li>Two options are available:<p id="en-us_topic_0020100162_p45076268122651"><a name="en-us_topic_0020100162_p45076268122651"></a><a name="en-us_topic_0020100162_p45076268122651"></a><strong id="b84235270615441"><a name="b84235270615441"></a><a name="b84235270615441"></a>false</strong>: The load balancer is disabled.</p>
    <p id="en-us_topic_0020100162_p36918481123054"><a name="en-us_topic_0020100162_p36918481123054"></a><a name="en-us_topic_0020100162_p36918481123054"></a><strong id="b842352706154416"><a name="b842352706154416"></a><a name="b842352706154416"></a>true</strong>: The load balancer is working properly.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row6048320515476"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p6092365114222"><a name="en-us_topic_0020100162_p6092365114222"></a><a name="en-us_topic_0020100162_p6092365114222"></a>cookie_timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p23719591114222"><a name="en-us_topic_0020100162_p23719591114222"></a><a name="en-us_topic_0020100162_p23719591114222"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100162_ul33350349115710"></a><a name="en-us_topic_0020100162_ul33350349115710"></a><ul id="en-us_topic_0020100162_ul33350349115710"><li>Specifies the cookie timeout duration. This parameter is valid when <strong>session_sticky</strong> is set to <strong>true</strong> and <strong>sticky_session_type</strong> to <strong>insert</strong>.</li><li>The value ranges from <strong id="b78535253472"><a name="b78535253472"></a><a name="b78535253472"></a>1</strong> to <strong id="b191431029154712"><a name="b191431029154712"></a><a name="b191431029154712"></a>1440</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row2980919315476"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p15469043114239"><a name="en-us_topic_0020100162_p15469043114239"></a><a name="en-us_topic_0020100162_p15469043114239"></a>member_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p360955114239"><a name="en-us_topic_0020100162_p360955114239"></a><a name="en-us_topic_0020100162_p360955114239"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p42841405114239"><a name="en-us_topic_0020100162_p42841405114239"></a><a name="en-us_topic_0020100162_p42841405114239"></a>Specifies the quantity of backend ECSs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row4411394316142"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p678340616142"><a name="en-us_topic_0020100162_p678340616142"></a><a name="en-us_topic_0020100162_p678340616142"></a>healthcheck_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p27864571193014"><a name="en-us_topic_0020100162_p27864571193014"></a><a name="en-us_topic_0020100162_p27864571193014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p1275507216142"><a name="en-us_topic_0020100162_p1275507216142"></a><a name="en-us_topic_0020100162_p1275507216142"></a>Specifies the health check ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row39654186114120"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p62134065114242"><a name="en-us_topic_0020100162_p62134065114242"></a><a name="en-us_topic_0020100162_p62134065114242"></a>session_sticky</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p66803340114242"><a name="en-us_topic_0020100162_p66803340114242"></a><a name="en-us_topic_0020100162_p66803340114242"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p42361464114242"><a name="en-us_topic_0020100162_p42361464114242"></a><a name="en-us_topic_0020100162_p42361464114242"></a>Specifies whether to enable the sticky session feature. The feature is enabled when the value is <strong id="b3064351115846"><a name="b3064351115846"></a><a name="b3064351115846"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row5115575114559"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p59558165114559"><a name="en-us_topic_0020100162_p59558165114559"></a><a name="en-us_topic_0020100162_p59558165114559"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p59482097114559"><a name="en-us_topic_0020100162_p59482097114559"></a><a name="en-us_topic_0020100162_p59482097114559"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p53320520114559"><a name="en-us_topic_0020100162_p53320520114559"></a><a name="en-us_topic_0020100162_p53320520114559"></a>Specifies the port used by the load balancer.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row30394559114559"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p14627372114559"><a name="en-us_topic_0020100162_p14627372114559"></a><a name="en-us_topic_0020100162_p14627372114559"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p43966458114559"><a name="en-us_topic_0020100162_p43966458114559"></a><a name="en-us_topic_0020100162_p43966458114559"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p4513312114559"><a name="en-us_topic_0020100162_p4513312114559"></a><a name="en-us_topic_0020100162_p4513312114559"></a>Specifies the listener name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row47738131192526"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p45068101192530"><a name="en-us_topic_0020100162_p45068101192530"></a><a name="en-us_topic_0020100162_p45068101192530"></a>certificate_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p26637577192530"><a name="en-us_topic_0020100162_p26637577192530"></a><a name="en-us_topic_0020100162_p26637577192530"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p10160092192530"><a name="en-us_topic_0020100162_p10160092192530"></a><a name="en-us_topic_0020100162_p10160092192530"></a>Specifies the ID of the SSL certificate for security authentication. This parameter is mandatory when <strong id="b8423527061428"><a name="b8423527061428"></a><a name="b8423527061428"></a>protocol</strong> is set to <strong id="b84235270614212"><a name="b84235270614212"></a><a name="b84235270614212"></a>HTTPS</strong> or <strong id="b842352706182053"><a name="b842352706182053"></a><a name="b842352706182053"></a>SSL</strong>. Otherwise, the parameter value is <strong id="b4428435195955"><a name="b4428435195955"></a><a name="b4428435195955"></a>null</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row58796638191150"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p14955541191153"><a name="en-us_topic_0020100162_p14955541191153"></a><a name="en-us_topic_0020100162_p14955541191153"></a>certificates</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p159761928125416"><a name="p159761928125416"></a><a name="p159761928125416"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p10150984191153"><a name="en-us_topic_0020100162_p10150984191153"></a><a name="en-us_topic_0020100162_p10150984191153"></a>Lists the certificate IDs if <strong id="b842352706172631"><a name="b842352706172631"></a><a name="b842352706172631"></a>protocol</strong> is set to <strong id="b842352706172635"><a name="b842352706172635"></a><a name="b842352706172635"></a>HTTPS</strong>.</p>
    <p id="en-us_topic_0020100162_p24249993191153"><a name="en-us_topic_0020100162_p24249993191153"></a><a name="en-us_topic_0020100162_p24249993191153"></a>This parameter is mandatory in the SNI scenario.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row2375380811549"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p1504952911549"><a name="en-us_topic_0020100162_p1504952911549"></a><a name="en-us_topic_0020100162_p1504952911549"></a>tcp_timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p409416311549"><a name="en-us_topic_0020100162_p409416311549"></a><a name="en-us_topic_0020100162_p409416311549"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p3012604011549"><a name="en-us_topic_0020100162_p3012604011549"></a><a name="en-us_topic_0020100162_p3012604011549"></a>Specifies the TCP session timeout duration.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row2500893311549"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p5132288011549"><a name="en-us_topic_0020100162_p5132288011549"></a><a name="en-us_topic_0020100162_p5132288011549"></a>udp_timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p6270870011549"><a name="en-us_topic_0020100162_p6270870011549"></a><a name="en-us_topic_0020100162_p6270870011549"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p2027531511549"><a name="en-us_topic_0020100162_p2027531511549"></a><a name="en-us_topic_0020100162_p2027531511549"></a>Specifies the UDP session timeout duration.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row4641899895910"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p3542825295918"><a name="en-us_topic_0020100162_p3542825295918"></a><a name="en-us_topic_0020100162_p3542825295918"></a>ssl_protocols</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p5111613495918"><a name="en-us_topic_0020100162_p5111613495918"></a><a name="en-us_topic_0020100162_p5111613495918"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p4676617295918"><a name="en-us_topic_0020100162_p4676617295918"></a><a name="en-us_topic_0020100162_p4676617295918"></a>Specifies the supported SSL/TLS protocol version. This parameter is available only when <strong id="b842352706173219"><a name="b842352706173219"></a><a name="b842352706173219"></a>protocol</strong> is set to <strong id="b842352706173222"><a name="b842352706173222"></a><a name="b842352706173222"></a>HTTPS</strong> or <strong id="b842352706181923"><a name="b842352706181923"></a><a name="b842352706181923"></a>SSL</strong>.</p>
    <div class="note" id="en-us_topic_0020100162_note519440195935"><a name="en-us_topic_0020100162_note519440195935"></a><a name="en-us_topic_0020100162_note519440195935"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0020100162_p4674961395935"><a name="en-us_topic_0020100162_p4674961395935"></a><a name="en-us_topic_0020100162_p4674961395935"></a>For HTTPS listeners in versions earlier than 1.2.8, the parameter value is <strong id="b842352706105023"><a name="b842352706105023"></a><a name="b842352706105023"></a>TLSv1.2</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row2109321595915"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100162_p1113444795918"><a name="en-us_topic_0020100162_p1113444795918"></a><a name="en-us_topic_0020100162_p1113444795918"></a>ssl_ciphers</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100162_p2947503595918"><a name="en-us_topic_0020100162_p2947503595918"></a><a name="en-us_topic_0020100162_p2947503595918"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100162_p3866766895918"><a name="en-us_topic_0020100162_p3866766895918"></a><a name="en-us_topic_0020100162_p3866766895918"></a>Specifies the cipher suite of an encryption protocol. This parameter is available only when <strong id="b842352706173219_1"><a name="b842352706173219_1"></a><a name="b842352706173219_1"></a>protocol</strong> is set to <strong id="b842352706173222_1"><a name="b842352706173222_1"></a><a name="b842352706173222_1"></a>HTTPS</strong> or <strong id="b842352706181923_1"><a name="b842352706181923_1"></a><a name="b842352706181923_1"></a>SSL</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    [
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
         "tcp_draining": true,
         "tcp_timeout": 1,
         "member_number": 0,
         "healthcheck_id": null,
         "session_sticky": true,
         "tcp_draining_timeout": 5,
         "name": "lis"
    },
    
    {
         "update_time": "2016-12-01 07:11:49",
         "backend_port": 9090,
         "id": "4818300858fc43e0a4d843ce74ee83a4",
         "backend_protocol": "HTTP",
         "sticky_session_type": "insert",
         "certificate_id": null,
         "description": "",
         "loadbalancer_id": "f54c65b1b5dd4a4f95b71b44796ac013",
         "lb_algorithm": "roundrobin",
         "create_time": "2016-12-01 07:11:30",
         "admin_state_up": false,
         "status": "ACTIVE",
         "protocol": "HTTP",
         "cookie_timeout": 100,
         "port": 9091,
         "tcp_draining": true,
         "tcp_timeout": null,
         "member_number": 0,
         "healthcheck_id": null,
         "session_sticky": true,
         "tcp_draining_timeout": 5,
         "name": "lis"
     }
    ]
    ```


## Status Code<a name="en-us_topic_0020100162_section17284754"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0020100162_table17012524151517"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100162_row19952879151517"><th class="cellrowborder" valign="top" width="13.04%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020100162_p5570470151517"><a name="en-us_topic_0020100162_p5570470151517"></a><a name="en-us_topic_0020100162_p5570470151517"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.72%" id="mcps1.1.4.1.2"><p id="p131756574460"><a name="p131756574460"></a><a name="p131756574460"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020100162_p48554946151517"><a name="en-us_topic_0020100162_p48554946151517"></a><a name="en-us_topic_0020100162_p48554946151517"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100162_row40636587151517"><td class="cellrowborder" valign="top" width="13.04%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100162_p3229256151517"><a name="en-us_topic_0020100162_p3229256151517"></a><a name="en-us_topic_0020100162_p3229256151517"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.72%" headers="mcps1.1.4.1.2 "><p id="p5767151014718"><a name="p5767151014718"></a><a name="p5767151014718"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100162_p60243202151517"><a name="en-us_topic_0020100162_p60243202151517"></a><a name="en-us_topic_0020100162_p60243202151517"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row5317909151517"><td class="cellrowborder" valign="top" width="13.04%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100162_p28097476151517"><a name="en-us_topic_0020100162_p28097476151517"></a><a name="en-us_topic_0020100162_p28097476151517"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.72%" headers="mcps1.1.4.1.2 "><p id="p47676107477"><a name="p47676107477"></a><a name="p47676107477"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100162_p61303108151517"><a name="en-us_topic_0020100162_p61303108151517"></a><a name="en-us_topic_0020100162_p61303108151517"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row14857066151517"><td class="cellrowborder" valign="top" width="13.04%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100162_p62571686151517"><a name="en-us_topic_0020100162_p62571686151517"></a><a name="en-us_topic_0020100162_p62571686151517"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.72%" headers="mcps1.1.4.1.2 "><p id="p14767191094714"><a name="p14767191094714"></a><a name="p14767191094714"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100162_p35141766151517"><a name="en-us_topic_0020100162_p35141766151517"></a><a name="en-us_topic_0020100162_p35141766151517"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row47840439151517"><td class="cellrowborder" valign="top" width="13.04%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100162_p49870345151517"><a name="en-us_topic_0020100162_p49870345151517"></a><a name="en-us_topic_0020100162_p49870345151517"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.72%" headers="mcps1.1.4.1.2 "><p id="p276781014479"><a name="p276781014479"></a><a name="p276781014479"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100162_p12966131151517"><a name="en-us_topic_0020100162_p12966131151517"></a><a name="en-us_topic_0020100162_p12966131151517"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row49586321151517"><td class="cellrowborder" valign="top" width="13.04%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100162_p57069075151517"><a name="en-us_topic_0020100162_p57069075151517"></a><a name="en-us_topic_0020100162_p57069075151517"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.72%" headers="mcps1.1.4.1.2 "><p id="p27681510194711"><a name="p27681510194711"></a><a name="p27681510194711"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100162_p59192386151517"><a name="en-us_topic_0020100162_p59192386151517"></a><a name="en-us_topic_0020100162_p59192386151517"></a>System error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100162_row62969429151517"><td class="cellrowborder" valign="top" width="13.04%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100162_p250162151517"><a name="en-us_topic_0020100162_p250162151517"></a><a name="en-us_topic_0020100162_p250162151517"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.72%" headers="mcps1.1.4.1.2 "><p id="p376811016475"><a name="p376811016475"></a><a name="p376811016475"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100162_p20263151151517"><a name="en-us_topic_0020100162_p20263151151517"></a><a name="en-us_topic_0020100162_p20263151151517"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


