# Querying AZ Information<a name="EN-US_TOPIC_0237964378"></a>

## Function<a name="section7882981"></a>

This API is used to query information about AZs.

## URI<a name="section3837973"></a>

-   URI format:

    GET /v1.0/availableZones

-   Parameter description:

    None.


## Request<a name="section34541762"></a>

None.

## Response<a name="section42440405"></a>

-   Status code:

    If status code "200 OK" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    [Table 1](#table7422478)  describes response parameters.


**Table  1**  Parameter description

<a name="table7422478"></a>
<table><thead align="left"><tr id="row34137448"><th class="cellrowborder" valign="top" width="24.489795918367346%" id="mcps1.2.4.1.1"><p id="p13669900"><a name="p13669900"></a><a name="p13669900"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="41.83673469387755%" id="mcps1.2.4.1.2"><p id="p33520145"><a name="p33520145"></a><a name="p33520145"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.6734693877551%" id="mcps1.2.4.1.3"><p id="p30777247"><a name="p30777247"></a><a name="p30777247"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9929053"><td class="cellrowborder" valign="top" width="24.489795918367346%" headers="mcps1.2.4.1.1 "><p id="p66055795"><a name="p66055795"></a><a name="p66055795"></a>regionId</p>
</td>
<td class="cellrowborder" valign="top" width="41.83673469387755%" headers="mcps1.2.4.1.2 "><p id="p48919178"><a name="p48919178"></a><a name="p48919178"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.6734693877551%" headers="mcps1.2.4.1.3 "><p id="p3030473"><a name="p3030473"></a><a name="p3030473"></a>Region ID.</p>
</td>
</tr>
<tr id="row27274264"><td class="cellrowborder" valign="top" width="24.489795918367346%" headers="mcps1.2.4.1.1 "><p id="p61731751"><a name="p61731751"></a><a name="p61731751"></a>available_zones</p>
</td>
<td class="cellrowborder" valign="top" width="41.83673469387755%" headers="mcps1.2.4.1.2 "><p id="p34215923"><a name="p34215923"></a><a name="p34215923"></a>Array</p>
<p id="p39507851"><a name="p39507851"></a><a name="p39507851"></a>For details, see <a href="#ref478638127">Table 2</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.6734693877551%" headers="mcps1.2.4.1.3 "><p id="p11520735"><a name="p11520735"></a><a name="p11520735"></a>Array of AZs.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Parameter description of the available\_zones array

<a name="ref478638127"></a>
<table><thead align="left"><tr id="row25871087"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="p15183298"><a name="p15183298"></a><a name="p15183298"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.2"><p id="p21887634"><a name="p21887634"></a><a name="p21887634"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.2.4.1.3"><p id="p28067910"><a name="p28067910"></a><a name="p28067910"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row58908231"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p6837372"><a name="p6837372"></a><a name="p6837372"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p16956237"><a name="p16956237"></a><a name="p16956237"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p31277988"><a name="p31277988"></a><a name="p31277988"></a>AZ ID.</p>
</td>
</tr>
<tr id="row13066436"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p51748380"><a name="p51748380"></a><a name="p51748380"></a>code</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p30869228"><a name="p30869228"></a><a name="p30869228"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p17379549"><a name="p17379549"></a><a name="p17379549"></a>AZ code.</p>
</td>
</tr>
<tr id="row22198217"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p53225166"><a name="p53225166"></a><a name="p53225166"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p16271175"><a name="p16271175"></a><a name="p16271175"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p42896797"><a name="p42896797"></a><a name="p42896797"></a>AZ name.</p>
</td>
</tr>
<tr id="row50526854"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p66143345"><a name="p66143345"></a><a name="p66143345"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p56010733"><a name="p56010733"></a><a name="p56010733"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p40575521"><a name="p40575521"></a><a name="p40575521"></a>Port of the AZ.</p>
</td>
</tr>
<tr id="row29635376"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p51655276"><a name="p51655276"></a><a name="p51655276"></a>resource_availability</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p23327861"><a name="p23327861"></a><a name="p23327861"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p10508594"><a name="p10508594"></a><a name="p10508594"></a>An indicator of whether there are available resources in the AZ.</p>
<a name="ul27468488"></a><a name="ul27468488"></a><ul id="ul27468488"><li><strong id="b10355055"><a name="b10355055"></a><a name="b10355055"></a>true</strong>: There are available resources in the AZ.</li><li><strong id="b33453118"><a name="b33453118"></a><a name="b33453118"></a>false</strong>: All resources have been used up in the AZ.</li></ul>
</td>
</tr>
</tbody>
</table>

-   Example response:

    ```
    { 
     "regionId": "XXXXXX", 
     "available_zones": [ 
            { 
                "id": "f84448fd537f46078dd8bd776747f573", 
                "code": "XXXXXX", 
                "name": "XXXXXX", 
                "port": "8003", 
                "resource_availability": "true" 
            }, 
            { 
                "id": "12c47a78666b4e438cd0c692b9860387", 
                "code": "XXXXXX", 
                "name": "XXXXXX", 
                "port": "8002", 
                "resource_availability": "true" 
            }, 
            { 
                "id": "0725858e0d26434f9aa3dc5fc40d5697", 
                "code": "XXXXXX", 
                "name": "XXXXXX", 
                "port": "8009", 
                "resource_availability": "true" 
            } 
     ] 
    }
    ```


