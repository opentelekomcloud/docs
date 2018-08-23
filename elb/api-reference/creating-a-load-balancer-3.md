# Creating a Load Balancer<a name="EN-US_TOPIC_0096561535"></a>

## Function<a name="en-us_topic_0049139634_section19714419"></a>

This API is used to create a load balancer.

## API Format<a name="en-us_topic_0049139634_section43212049"></a>

<a name="en-us_topic_0049139634_table13630215111036"></a><table><thead align="left"><tr id="en-us_topic_0049139634_row60730435111036"><th class="cellrowborder" valign="top" width="23.75%" id="mcps1.1.4.1.1"><p id="en-us_topic_0049139634_p48951303111042"><a name="en-us_topic_0049139634_p48951303111042"></a><a name="en-us_topic_0049139634_p48951303111042"></a><strong id="en-us_topic_0049139634_b842352706111926"><a name="en-us_topic_0049139634_b842352706111926"></a><a name="en-us_topic_0049139634_b842352706111926"></a>Method</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.15%" id="mcps1.1.4.1.2"><p id="en-us_topic_0049139634_p5632573111042"><a name="en-us_topic_0049139634_p5632573111042"></a><a name="en-us_topic_0049139634_p5632573111042"></a>URI</p>
</th>
<th class="cellrowborder" valign="top" width="40.1%" id="mcps1.1.4.1.3"><p id="en-us_topic_0049139634_p53585268111042"><a name="en-us_topic_0049139634_p53585268111042"></a><a name="en-us_topic_0049139634_p53585268111042"></a><strong id="en-us_topic_0049139634_b84235270695939"><a name="en-us_topic_0049139634_b84235270695939"></a><a name="en-us_topic_0049139634_b84235270695939"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139634_row39175067111036"><td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0049139634_p56716291111042"><a name="en-us_topic_0049139634_p56716291111042"></a><a name="en-us_topic_0049139634_p56716291111042"></a>POST</p>
</td>
<td class="cellrowborder" valign="top" width="36.15%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0049139634_p30616876111042"><a name="en-us_topic_0049139634_p30616876111042"></a><a name="en-us_topic_0049139634_p30616876111042"></a>/v2.0/lbaas/loadbalancers</p>
</td>
<td class="cellrowborder" valign="top" width="40.1%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0049139634_p64047861111042"><a name="en-us_topic_0049139634_p64047861111042"></a><a name="en-us_topic_0049139634_p64047861111042"></a>Creates a load balancer.</p>
</td>
</tr>
</tbody>
</table>

## Restrictions<a name="en-us_topic_0049139634_section53364125"></a>

-   The backend ECS and VIP associated with the same load balancer must be in the same router.
-   Creating a load balancer using specified flavors is not supported.
-   The value of  **admin\_state\_up**  must be  **true**.
-   The value of  **provider**  must be  **vlb**.
-   The value of  **vip\_subnet\_id**  must be one of an internal network.

## Request<a name="section196085184393"></a>

-   Parameter description

    <a name="table55596238165"></a><table><thead align="left"><tr id="row1356016236168"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.1.5.1.1"><p id="p185600235163"><a name="p185600235163"></a><a name="p185600235163"></a><strong id="b842352706181819"><a name="b842352706181819"></a><a name="b842352706181819"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.1.5.1.2"><p id="p15560192331614"><a name="p15560192331614"></a><a name="p15560192331614"></a><strong id="b84235270610580"><a name="b84235270610580"></a><a name="b84235270610580"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.1.5.1.3"><p id="p1756052313165"><a name="p1756052313165"></a><a name="p1756052313165"></a><strong id="b8423527061798"><a name="b8423527061798"></a><a name="b8423527061798"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.1.5.1.4"><p id="p1856019234166"><a name="p1856019234166"></a><a name="p1856019234166"></a><strong id="b842352706192251"><a name="b842352706192251"></a><a name="b842352706192251"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row155611323101620"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.1 "><p id="p1556182321620"><a name="p1556182321620"></a><a name="p1556182321620"></a>loadbalancer</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.1.5.1.2 "><p id="p656218233167"><a name="p656218233167"></a><a name="p656218233167"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="p165629237162"><a name="p165629237162"></a><a name="p165629237162"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.1.5.1.4 "><p id="p17562023141619"><a name="p17562023141619"></a><a name="p17562023141619"></a>Specifies the load balancer. For details, see <a href="overview.html#en-us_topic_0049139630_table5521863511010">Table 1</a>.</p>
    <p id="p656262341614"><a name="p656262341614"></a><a name="p656262341614"></a>The <strong id="b1888000238145516"><a name="b1888000238145516"></a><a name="b1888000238145516"></a>vip_subnet_id</strong> field is mandatory.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST /v2.0/lbaas/loadbalancers
    {
        "loadbalancer": {
            "name": "loadbalancer1",
            "description": "simple lb",
            "tenant_id": "1867112d054b427e808cc6096d8193a1",
            "vip_subnet_id": "58077bdb-d470-424b-8c45-2e3c65060a5b",
            "vip_address": "10.0.0.4",
            "admin_state_up": true
        }
    }
    ```


## Response<a name="section14610958143910"></a>

-   Parameter description

    <a name="table10636133131611"></a><table><thead align="left"><tr id="row6637113381614"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.1.5.1.1"><p id="p763763315165"><a name="p763763315165"></a><a name="p763763315165"></a><strong id="b842352706181819_1"><a name="b842352706181819_1"></a><a name="b842352706181819_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.1.5.1.2"><p id="p363733310161"><a name="p363733310161"></a><a name="p363733310161"></a><strong id="b84235270610580_1"><a name="b84235270610580_1"></a><a name="b84235270610580_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.1.5.1.3"><p id="p1463716332169"><a name="p1463716332169"></a><a name="p1463716332169"></a><strong id="b8423527061798_1"><a name="b8423527061798_1"></a><a name="b8423527061798_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.1.5.1.4"><p id="p1637733201614"><a name="p1637733201614"></a><a name="p1637733201614"></a><strong id="b842352706192251_1"><a name="b842352706192251_1"></a><a name="b842352706192251_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row26373338166"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.1 "><p id="p166371933191614"><a name="p166371933191614"></a><a name="p166371933191614"></a>loadbalancer</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.1.5.1.2 "><p id="p563833361611"><a name="p563833361611"></a><a name="p563833361611"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="p3638113315164"><a name="p3638113315164"></a><a name="p3638113315164"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.1.5.1.4 "><p id="p3638153321619"><a name="p3638153321619"></a><a name="p3638153321619"></a>Specifies the load balancer. For details, see <a href="overview.html#en-us_topic_0049139630_table5521863511010">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "loadbalancer": {
            "description": "",
            "admin_state_up": true,
            "tenant_id": "1867112d054b427e808cc6096d8193a1",
            "provisioning_status": "ACTIVE",
            "vip_subnet_id": "58077bdb-d470-424b-8c45-2e3c65060a5b",
            "listeners": [],
            "vip_address": "10.0.0.4",
            "vip_port_id": "519f6af5-74aa-4347-9dba-84c440192877",
            "provider": "vlb",
            "pools": [],
            "id": "b0657373-0c68-41d1-980f-1a44d9e3ff01",
            "operating_status": "ONLINE",
            "name": "loadbalancer1"
        }
    }
    ```


## Error Codes<a name="en-us_topic_0049139632_section15511864"></a>

For details, see section  [Error Codes for Enhanced Load Balancers](error-codes-for-enhanced-load-balancers.md).

