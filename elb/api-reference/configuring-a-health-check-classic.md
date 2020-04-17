# Configuring a Health Check<a name="EN-US_TOPIC_0096561512"></a>

## Function<a name="en-us_topic_0020100164_section54999878"></a>

This API is used to configure a health check for backend ECSs.

## URI<a name="en-us_topic_0020100164_section25236858"></a>

POST /v1.0/\{project\_id\}/elbaas/healthcheck

**Table  1**  Parameter description

<a name="en-us_topic_0020100164_table33323423"></a>
<table><thead align="left"><tr id="en-us_topic_0020100164_row8420641"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p75506301858"><a name="p75506301858"></a><a name="p75506301858"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100164_p17233719"><a name="en-us_topic_0020100164_p17233719"></a><a name="en-us_topic_0020100164_p17233719"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100164_p4164548117122"><a name="en-us_topic_0020100164_p4164548117122"></a><a name="en-us_topic_0020100164_p4164548117122"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020100164_p53754023"><a name="en-us_topic_0020100164_p53754023"></a><a name="en-us_topic_0020100164_p53754023"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020100164_row33431272113959"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100164_p1894114191435"><a name="en-us_topic_0020100164_p1894114191435"></a><a name="en-us_topic_0020100164_p1894114191435"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100164_p50996812114013"><a name="en-us_topic_0020100164_p50996812114013"></a><a name="en-us_topic_0020100164_p50996812114013"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100164_p54126260114016"><a name="en-us_topic_0020100164_p54126260114016"></a><a name="en-us_topic_0020100164_p54126260114016"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100164_p8340728114018"><a name="en-us_topic_0020100164_p8340728114018"></a><a name="en-us_topic_0020100164_p8340728114018"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
<tr id="en-us_topic_0020100164_row59108624"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100164_p23069209"><a name="en-us_topic_0020100164_p23069209"></a><a name="en-us_topic_0020100164_p23069209"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100164_p56666602"><a name="en-us_topic_0020100164_p56666602"></a><a name="en-us_topic_0020100164_p56666602"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100164_p1784078717122"><a name="en-us_topic_0020100164_p1784078717122"></a><a name="en-us_topic_0020100164_p1784078717122"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100164_p6471942"><a name="en-us_topic_0020100164_p6471942"></a><a name="en-us_topic_0020100164_p6471942"></a>Specifies the ID of the listener with which the health check is associated.</p>
</td>
</tr>
<tr id="en-us_topic_0020100164_row58247484"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100164_p20425774"><a name="en-us_topic_0020100164_p20425774"></a><a name="en-us_topic_0020100164_p20425774"></a>healthcheck_protocol</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100164_p43875021"><a name="en-us_topic_0020100164_p43875021"></a><a name="en-us_topic_0020100164_p43875021"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100164_p3581766217122"><a name="en-us_topic_0020100164_p3581766217122"></a><a name="en-us_topic_0020100164_p3581766217122"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100164_ul528706289201"></a><a name="en-us_topic_0020100164_ul528706289201"></a><ul id="en-us_topic_0020100164_ul528706289201"><li>Specifies the health check protocol. A listener using UDP is not allowed for a private network load balancer.</li><li>The value can be <strong>HTTP</strong>, <strong>TCP</strong>, or <strong id="en-us_topic_0020100164_b842352706155831"><a name="en-us_topic_0020100164_b842352706155831"></a><a name="en-us_topic_0020100164_b842352706155831"></a>UDP</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100164_row38446258"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100164_p27139175"><a name="en-us_topic_0020100164_p27139175"></a><a name="en-us_topic_0020100164_p27139175"></a>healthcheck_uri</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100164_p50789581"><a name="en-us_topic_0020100164_p50789581"></a><a name="en-us_topic_0020100164_p50789581"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100164_p1554952217122"><a name="en-us_topic_0020100164_p1554952217122"></a><a name="en-us_topic_0020100164_p1554952217122"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100164_ul6136760992020"></a><a name="en-us_topic_0020100164_ul6136760992020"></a><ul id="en-us_topic_0020100164_ul6136760992020"><li>Specifies the health check URI. This parameter is valid when <strong>healthcheck_protocol</strong> is <strong>HTTP</strong>.</li><li>The value is a string of 1 to 80 characters that must start with a slash (/) and can contain only letters, digits, and special characters such as -/.%?#&amp;_=</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100164_row45979426"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100164_p33345988"><a name="en-us_topic_0020100164_p33345988"></a><a name="en-us_topic_0020100164_p33345988"></a>healthcheck_connect_port</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100164_p16670523"><a name="en-us_topic_0020100164_p16670523"></a><a name="en-us_topic_0020100164_p16670523"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100164_p5155173317122"><a name="en-us_topic_0020100164_p5155173317122"></a><a name="en-us_topic_0020100164_p5155173317122"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100164_ul569317192032"></a><a name="en-us_topic_0020100164_ul569317192032"></a><ul id="en-us_topic_0020100164_ul569317192032"><li>Specifies the health check port.</li><li>The port number ranges from 1 to 65535.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100164_row24945412"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100164_p7312526"><a name="en-us_topic_0020100164_p7312526"></a><a name="en-us_topic_0020100164_p7312526"></a>healthy_threshold</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100164_p55443761"><a name="en-us_topic_0020100164_p55443761"></a><a name="en-us_topic_0020100164_p55443761"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100164_p1494088217122"><a name="en-us_topic_0020100164_p1494088217122"></a><a name="en-us_topic_0020100164_p1494088217122"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100164_ul2842639192044"></a><a name="en-us_topic_0020100164_ul2842639192044"></a><ul id="en-us_topic_0020100164_ul2842639192044"><li>Specifies the number of consecutive successful health checks when the health check result of a backend ECS changes from <strong id="en-us_topic_0020100164_b3116158110365"><a name="en-us_topic_0020100164_b3116158110365"></a><a name="en-us_topic_0020100164_b3116158110365"></a>fail</strong> to <strong id="en-us_topic_0020100164_b1201877310365"><a name="en-us_topic_0020100164_b1201877310365"></a><a name="en-us_topic_0020100164_b1201877310365"></a>success</strong>.</li><li>The value ranges from <strong id="b142091226151317"><a name="b142091226151317"></a><a name="b142091226151317"></a>1</strong> to <strong id="b73315292133"><a name="b73315292133"></a><a name="b73315292133"></a>10</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100164_row59835867"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100164_p14867095"><a name="en-us_topic_0020100164_p14867095"></a><a name="en-us_topic_0020100164_p14867095"></a>unhealthy_threshold</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100164_p63384014"><a name="en-us_topic_0020100164_p63384014"></a><a name="en-us_topic_0020100164_p63384014"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100164_p225191917122"><a name="en-us_topic_0020100164_p225191917122"></a><a name="en-us_topic_0020100164_p225191917122"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100164_ul583290992058"></a><a name="en-us_topic_0020100164_ul583290992058"></a><ul id="en-us_topic_0020100164_ul583290992058"><li>Specifies the threshold at which the health check result is <strong id="b202239429018"><a name="b202239429018"></a><a name="b202239429018"></a>fail</strong>, that is, the number of consecutive health checks when the health check result of backend ECSs changes from <strong id="en-us_topic_0020100164_b54755209181458"><a name="en-us_topic_0020100164_b54755209181458"></a><a name="en-us_topic_0020100164_b54755209181458"></a>success</strong> to <strong id="en-us_topic_0020100164_b5986964181458"><a name="en-us_topic_0020100164_b5986964181458"></a><a name="en-us_topic_0020100164_b5986964181458"></a>fail</strong>. </li><li>The value ranges from <strong id="b172615021415"><a name="b172615021415"></a><a name="b172615021415"></a>1</strong> to <strong id="b152622061412"><a name="b152622061412"></a><a name="b152622061412"></a>10</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100164_row34232944"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100164_p21405046"><a name="en-us_topic_0020100164_p21405046"></a><a name="en-us_topic_0020100164_p21405046"></a>healthcheck_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100164_p56087165"><a name="en-us_topic_0020100164_p56087165"></a><a name="en-us_topic_0020100164_p56087165"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100164_p4818773217122"><a name="en-us_topic_0020100164_p4818773217122"></a><a name="en-us_topic_0020100164_p4818773217122"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100164_ul562080659218"></a><a name="en-us_topic_0020100164_ul562080659218"></a><ul id="en-us_topic_0020100164_ul562080659218"><li>Specifies the maximum time required for waiting for a response from the health check in the unit of second.</li><li>The value ranges from <strong id="b77014279409"><a name="b77014279409"></a><a name="b77014279409"></a>1</strong> to <strong id="b13643529194019"><a name="b13643529194019"></a><a name="b13643529194019"></a>50</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100164_row1482002"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100164_p52933326"><a name="en-us_topic_0020100164_p52933326"></a><a name="en-us_topic_0020100164_p52933326"></a>healthcheck_interval</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100164_p59740974"><a name="en-us_topic_0020100164_p59740974"></a><a name="en-us_topic_0020100164_p59740974"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100164_p1089223417122"><a name="en-us_topic_0020100164_p1089223417122"></a><a name="en-us_topic_0020100164_p1089223417122"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100164_ul4166441692118"></a><a name="en-us_topic_0020100164_ul4166441692118"></a><ul id="en-us_topic_0020100164_ul4166441692118"><li>Specifies the interval between health checks in the unit of second.</li><li>The value ranges from <strong id="b1144311156417"><a name="b1144311156417"></a><a name="b1144311156417"></a>1</strong> to <strong id="b13407185416"><a name="b13407185416"></a><a name="b13407185416"></a>50</strong>.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020100164_section25805135"></a>

-   Request parameters

    None


-   Example request 1: Configuring an HTTP health check

    ```
    {
        "healthcheck_connect_port": 80,
        "healthcheck_interval": 5,
        "healthcheck_protocol": "HTTP",
        "healthcheck_timeout": 10,
        "healthcheck_uri": "/",
        "healthy_threshold": 3,
        "listener_id": "3ce8c4429478a5eb6ef4930de2d75b28",
        "unhealthy_threshold": 3
    }
    ```

-   Example request 2: Configuring a TCP health check 

    ```
    {
        "healthcheck_connect_port": 80,
        "healthcheck_interval": 5,
        "healthcheck_protocol": "TCP",
        "healthcheck_timeout": 10,
        "healthcheck_uri": "",
        "healthy_threshold": 3,
        "listener_id": "3ce8c4429478a5eb6ef4930de2d75b28",
        "unhealthy_threshold": 3
    }
    ```


## Response<a name="en-us_topic_0020100164_section30919631"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="en-us_topic_0020100164_table58268660154720"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100164_row43546893154720"><th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100164_p37637446154720"><a name="en-us_topic_0020100164_p37637446154720"></a><a name="en-us_topic_0020100164_p37637446154720"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100164_p15158425193624"><a name="en-us_topic_0020100164_p15158425193624"></a><a name="en-us_topic_0020100164_p15158425193624"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.64646464646465%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100164_p45778611154720"><a name="en-us_topic_0020100164_p45778611154720"></a><a name="en-us_topic_0020100164_p45778611154720"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100164_row513410112435"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100164_p5065952912439"><a name="en-us_topic_0020100164_p5065952912439"></a><a name="en-us_topic_0020100164_p5065952912439"></a>healthcheck_interval</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100164_p978118112439"><a name="en-us_topic_0020100164_p978118112439"></a><a name="en-us_topic_0020100164_p978118112439"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.64646464646465%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100164_p5407822612439"><a name="en-us_topic_0020100164_p5407822612439"></a><a name="en-us_topic_0020100164_p5407822612439"></a>Specifies the interval between health checks in the unit of second.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100164_row3070025912523"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100164_p4562333112526"><a name="en-us_topic_0020100164_p4562333112526"></a><a name="en-us_topic_0020100164_p4562333112526"></a>listener_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100164_p450233212526"><a name="en-us_topic_0020100164_p450233212526"></a><a name="en-us_topic_0020100164_p450233212526"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.64646464646465%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100164_p2914464612526"><a name="en-us_topic_0020100164_p2914464612526"></a><a name="en-us_topic_0020100164_p2914464612526"></a>Specifies the ID of the listener with which the health check is associated.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100164_row17079990154720"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100164_p41301921154720"><a name="en-us_topic_0020100164_p41301921154720"></a><a name="en-us_topic_0020100164_p41301921154720"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100164_p66205107193624"><a name="en-us_topic_0020100164_p66205107193624"></a><a name="en-us_topic_0020100164_p66205107193624"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.64646464646465%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100164_p63423313154720"><a name="en-us_topic_0020100164_p63423313154720"></a><a name="en-us_topic_0020100164_p63423313154720"></a>Specifies the health check ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100164_row33938912154720"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100164_p2290315212554"><a name="en-us_topic_0020100164_p2290315212554"></a><a name="en-us_topic_0020100164_p2290315212554"></a>healthcheck_protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100164_p4321605112554"><a name="en-us_topic_0020100164_p4321605112554"></a><a name="en-us_topic_0020100164_p4321605112554"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.64646464646465%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100164_p1083922212554"><a name="en-us_topic_0020100164_p1083922212554"></a><a name="en-us_topic_0020100164_p1083922212554"></a>Specifies the health check protocol.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100164_row8871928154720"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100164_p1330045612610"><a name="en-us_topic_0020100164_p1330045612610"></a><a name="en-us_topic_0020100164_p1330045612610"></a>unhealthy_threshold</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100164_p359513812610"><a name="en-us_topic_0020100164_p359513812610"></a><a name="en-us_topic_0020100164_p359513812610"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.64646464646465%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100164_p2277078112610"><a name="en-us_topic_0020100164_p2277078112610"></a><a name="en-us_topic_0020100164_p2277078112610"></a>Specifies the number of consecutive health checks when the health check result of a backend ECS changes from <strong id="b2481928663"><a name="b2481928663"></a><a name="b2481928663"></a>success</strong> to <strong id="b4482152813617"><a name="b4482152813617"></a><a name="b4482152813617"></a>fail</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100164_row794063512618"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100164_p6094783912633"><a name="en-us_topic_0020100164_p6094783912633"></a><a name="en-us_topic_0020100164_p6094783912633"></a>update_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100164_p3782791312633"><a name="en-us_topic_0020100164_p3782791312633"></a><a name="en-us_topic_0020100164_p3782791312633"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.64646464646465%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100164_p4416213212633"><a name="en-us_topic_0020100164_p4416213212633"></a><a name="en-us_topic_0020100164_p4416213212633"></a>Specifies the time when the health check was updated.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100164_row16253572154720"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100164_p4904884012633"><a name="en-us_topic_0020100164_p4904884012633"></a><a name="en-us_topic_0020100164_p4904884012633"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100164_p1353309912633"><a name="en-us_topic_0020100164_p1353309912633"></a><a name="en-us_topic_0020100164_p1353309912633"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.64646464646465%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100164_p2243924312633"><a name="en-us_topic_0020100164_p2243924312633"></a><a name="en-us_topic_0020100164_p2243924312633"></a>Specifies the time when the health check was configured.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100164_row1392188154720"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100164_p45658399154720"><a name="en-us_topic_0020100164_p45658399154720"></a><a name="en-us_topic_0020100164_p45658399154720"></a>healthcheck_connect_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100164_p5661608193624"><a name="en-us_topic_0020100164_p5661608193624"></a><a name="en-us_topic_0020100164_p5661608193624"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.64646464646465%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100164_p57899715154720"><a name="en-us_topic_0020100164_p57899715154720"></a><a name="en-us_topic_0020100164_p57899715154720"></a>Specifies the health check port.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100164_row55133490154720"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100164_p36627707154720"><a name="en-us_topic_0020100164_p36627707154720"></a><a name="en-us_topic_0020100164_p36627707154720"></a>healthcheck_timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100164_p5905984019365"><a name="en-us_topic_0020100164_p5905984019365"></a><a name="en-us_topic_0020100164_p5905984019365"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.64646464646465%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100164_p64658568154720"><a name="en-us_topic_0020100164_p64658568154720"></a><a name="en-us_topic_0020100164_p64658568154720"></a>Specifies the maximum time required for waiting for a response from the health check in the unit of second.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100164_row45056202154720"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100164_p4309577612648"><a name="en-us_topic_0020100164_p4309577612648"></a><a name="en-us_topic_0020100164_p4309577612648"></a>healthcheck_uri</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100164_p109693812648"><a name="en-us_topic_0020100164_p109693812648"></a><a name="en-us_topic_0020100164_p109693812648"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.64646464646465%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100164_p2174313612648"><a name="en-us_topic_0020100164_p2174313612648"></a><a name="en-us_topic_0020100164_p2174313612648"></a>Specifies the health check URI. This parameter is valid when <strong>healthcheck_protocol</strong> is <strong>HTTP</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100164_row6017617712347"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100164_p504822112722"><a name="en-us_topic_0020100164_p504822112722"></a><a name="en-us_topic_0020100164_p504822112722"></a>healthy_threshold</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100164_p625278012722"><a name="en-us_topic_0020100164_p625278012722"></a><a name="en-us_topic_0020100164_p625278012722"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.64646464646465%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100164_p3671316712722"><a name="en-us_topic_0020100164_p3671316712722"></a><a name="en-us_topic_0020100164_p3671316712722"></a>Specifies the number of consecutive health checks when the health check result of backend ECSs changes from <strong id="en-us_topic_0020100164_b3772576810365"><a name="en-us_topic_0020100164_b3772576810365"></a><a name="en-us_topic_0020100164_b3772576810365"></a>fail</strong> to <strong id="en-us_topic_0020100164_b398759310365"><a name="en-us_topic_0020100164_b398759310365"></a><a name="en-us_topic_0020100164_b398759310365"></a>success</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response 1: Configuring an HTTP health check

    ```
    {
         "healthcheck_interval":5,
         "listener_id":"3ce8c4429478a5eb6ef4930de2d75b28",
         "id":"134e5ea962327c6a574b83e6e7f31f35",
         "healthcheck_protocol":"HTTP",
         "unhealthy_threshold":3,
         "update_time":"2015-12-25 03:57:23",
         "create_time":"2015-12-25 03:57:23",
         "healthcheck_connect_port":80,
         "healthcheck_timeout":10,
         "healthcheck_uri":"\/",
         "healthy_threshold":3
    }
    ```

-   Example response 2: Configuring a TCP health check 

    ```
    {
         "healthcheck_interval":5,
         "listener_id":"3ce8c4429478a5eb6ef4930de2d75b28",
         "id":"134e5ea962327c6a574b83e6e7f31f35",
         "healthcheck_protocol":"TCP",
         "unhealthy_threshold":3,
         "update_time":"2015-12-25 03:57:23",
         "create_time":"2015-12-25 03:57:23",
         "healthcheck_connect_port":80,
         "healthcheck_timeout":10,
         "healthcheck_uri":"",
         "healthy_threshold":3
    }
    ```


## Status Code<a name="en-us_topic_0020100164_section9841225"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0020100164_table11098151151527"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100164_row16678161151527"><th class="cellrowborder" valign="top" width="10.299999999999999%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020100164_p8753830151527"><a name="en-us_topic_0020100164_p8753830151527"></a><a name="en-us_topic_0020100164_p8753830151527"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.46%" id="mcps1.1.4.1.2"><p id="p074410397618"><a name="p074410397618"></a><a name="p074410397618"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020100164_p37971652151527"><a name="en-us_topic_0020100164_p37971652151527"></a><a name="en-us_topic_0020100164_p37971652151527"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100164_row55804946151527"><td class="cellrowborder" valign="top" width="10.299999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100164_p23906744151527"><a name="en-us_topic_0020100164_p23906744151527"></a><a name="en-us_topic_0020100164_p23906744151527"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.4.1.2 "><p id="p171381521668"><a name="p171381521668"></a><a name="p171381521668"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100164_p57398111151527"><a name="en-us_topic_0020100164_p57398111151527"></a><a name="en-us_topic_0020100164_p57398111151527"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100164_row46820954151527"><td class="cellrowborder" valign="top" width="10.299999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100164_p34400933151527"><a name="en-us_topic_0020100164_p34400933151527"></a><a name="en-us_topic_0020100164_p34400933151527"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.4.1.2 "><p id="p91382052765"><a name="p91382052765"></a><a name="p91382052765"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100164_p35012164151527"><a name="en-us_topic_0020100164_p35012164151527"></a><a name="en-us_topic_0020100164_p35012164151527"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100164_row46674023151527"><td class="cellrowborder" valign="top" width="10.299999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100164_p22499488151527"><a name="en-us_topic_0020100164_p22499488151527"></a><a name="en-us_topic_0020100164_p22499488151527"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.4.1.2 "><p id="p13139105218617"><a name="p13139105218617"></a><a name="p13139105218617"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100164_p10519201151527"><a name="en-us_topic_0020100164_p10519201151527"></a><a name="en-us_topic_0020100164_p10519201151527"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100164_row27563948151527"><td class="cellrowborder" valign="top" width="10.299999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100164_p18087341151527"><a name="en-us_topic_0020100164_p18087341151527"></a><a name="en-us_topic_0020100164_p18087341151527"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.4.1.2 "><p id="p10139115213615"><a name="p10139115213615"></a><a name="p10139115213615"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100164_p55788555151527"><a name="en-us_topic_0020100164_p55788555151527"></a><a name="en-us_topic_0020100164_p55788555151527"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100164_row32334952151527"><td class="cellrowborder" valign="top" width="10.299999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100164_p1885468151527"><a name="en-us_topic_0020100164_p1885468151527"></a><a name="en-us_topic_0020100164_p1885468151527"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.4.1.2 "><p id="p213919521619"><a name="p213919521619"></a><a name="p213919521619"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100164_p18505183151527"><a name="en-us_topic_0020100164_p18505183151527"></a><a name="en-us_topic_0020100164_p18505183151527"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100164_row32328927151527"><td class="cellrowborder" valign="top" width="10.299999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100164_p1397439151527"><a name="en-us_topic_0020100164_p1397439151527"></a><a name="en-us_topic_0020100164_p1397439151527"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.4.1.2 "><p id="p0139752267"><a name="p0139752267"></a><a name="p0139752267"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100164_p46083715151527"><a name="en-us_topic_0020100164_p46083715151527"></a><a name="en-us_topic_0020100164_p46083715151527"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


