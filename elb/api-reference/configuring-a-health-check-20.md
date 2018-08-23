# Configuring a Health Check<a name="EN-US_TOPIC_0096561563"></a>

## Function<a name="en-us_topic_0049139665_section48637208"></a>

This API is used to configure a health check.

## API Format<a name="en-us_topic_0049139665_section35081689"></a>

<a name="en-us_topic_0049139665_table37609496125926"></a><table><thead align="left"><tr id="en-us_topic_0049139665_row13685301125926"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0049139665_p16717971125930"><a name="en-us_topic_0049139665_p16717971125930"></a><a name="en-us_topic_0049139665_p16717971125930"></a><strong id="b842352706172312"><a name="b842352706172312"></a><a name="b842352706172312"></a>Method</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0049139665_p11978410125930"><a name="en-us_topic_0049139665_p11978410125930"></a><a name="en-us_topic_0049139665_p11978410125930"></a>URI</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0049139665_p30727145125930"><a name="en-us_topic_0049139665_p30727145125930"></a><a name="en-us_topic_0049139665_p30727145125930"></a><strong id="b842352706192251"><a name="b842352706192251"></a><a name="b842352706192251"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139665_row32561654125926"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0049139665_p5776130125930"><a name="en-us_topic_0049139665_p5776130125930"></a><a name="en-us_topic_0049139665_p5776130125930"></a>POST</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0049139665_p65213355125930"><a name="en-us_topic_0049139665_p65213355125930"></a><a name="en-us_topic_0049139665_p65213355125930"></a>/v2.0/lbaas/healthmonitors</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0049139665_p47790364125930"><a name="en-us_topic_0049139665_p47790364125930"></a><a name="en-us_topic_0049139665_p47790364125930"></a>Configures a health check.</p>
</td>
</tr>
</tbody>
</table>

## Restrictions<a name="en-us_topic_0049139665_section47299748"></a>

-   The security groups must have rules that allow access by the 100.125.0.0/16 network segment.
-   The value of  **admin\_state\_up**  must be  **true**.

## Request<a name="en-us_topic_0049139665_section54669653"></a>

-   Parameter description

    <a name="en-us_topic_0049139665_table470163"></a><table><thead align="left"><tr id="en-us_topic_0049139665_row24812117"><th class="cellrowborder" valign="top" width="19.59%" id="mcps1.1.5.1.1"><p id="en-us_topic_0049139665_p63624481"><a name="en-us_topic_0049139665_p63624481"></a><a name="en-us_topic_0049139665_p63624481"></a><strong id="b842352706181819"><a name="b842352706181819"></a><a name="b842352706181819"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.53%" id="mcps1.1.5.1.2"><p id="en-us_topic_0049139665_p53309370"><a name="en-us_topic_0049139665_p53309370"></a><a name="en-us_topic_0049139665_p53309370"></a><strong id="b84235270610580"><a name="b84235270610580"></a><a name="b84235270610580"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="8.25%" id="mcps1.1.5.1.3"><p id="en-us_topic_0049139665_p23091719"><a name="en-us_topic_0049139665_p23091719"></a><a name="en-us_topic_0049139665_p23091719"></a><strong id="b8423527061798"><a name="b8423527061798"></a><a name="b8423527061798"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.63%" id="mcps1.1.5.1.4"><p id="en-us_topic_0049139665_p58489969"><a name="en-us_topic_0049139665_p58489969"></a><a name="en-us_topic_0049139665_p58489969"></a><strong id="b842352706192251_1"><a name="b842352706192251_1"></a><a name="b842352706192251_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0049139665_row40067039"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0049139665_p24204730"><a name="en-us_topic_0049139665_p24204730"></a><a name="en-us_topic_0049139665_p24204730"></a>healthmonitor</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0049139665_p14426089"><a name="en-us_topic_0049139665_p14426089"></a><a name="en-us_topic_0049139665_p14426089"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.25%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0049139665_p27662549"><a name="en-us_topic_0049139665_p27662549"></a><a name="en-us_topic_0049139665_p27662549"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0049139665_p26073957"><a name="en-us_topic_0049139665_p26073957"></a><a name="en-us_topic_0049139665_p26073957"></a>Specifies the health check. For details, see <a href="overview-18.html#en-us_topic_0049139662_table43819641125220">Table 1</a>.</p>
    <p id="en-us_topic_0049139665_p33339022"><a name="en-us_topic_0049139665_p33339022"></a><a name="en-us_topic_0049139665_p33339022"></a>Fields <strong id="b842352706115514"><a name="b842352706115514"></a><a name="b842352706115514"></a>type</strong>, <strong id="b842352706115525"><a name="b842352706115525"></a><a name="b842352706115525"></a>delay</strong>, <strong id="b842352706115529"><a name="b842352706115529"></a><a name="b842352706115529"></a>timeout</strong>, <strong id="b842352706115532"><a name="b842352706115532"></a><a name="b842352706115532"></a>max_retries</strong>, and <strong id="b842352706115537"><a name="b842352706115537"></a><a name="b842352706115537"></a>pool_id</strong> are mandatory.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST /v2.0/lbaas/healthmonitors
    {
      "healthmonitor": {
        "admin_state_up": true,
        "pool_id": "bb44bffb-05d9-412c-9d9c-b189d9e14193",
        "domain_name": "www.test.com",
        "delay": "10",
        "max_retries": "10",
        "timeout": "10",
        "type": "HTTP"
      }
    }
    ```


## Response<a name="en-us_topic_0049139665_section22264835"></a>

-   Parameter description

    <a name="en-us_topic_0049139665_table16106256"></a><table><thead align="left"><tr id="en-us_topic_0049139665_row50461073"><th class="cellrowborder" valign="top" width="19.59%" id="mcps1.1.5.1.1"><p id="en-us_topic_0049139665_p60815108"><a name="en-us_topic_0049139665_p60815108"></a><a name="en-us_topic_0049139665_p60815108"></a><strong id="b842352706181819_1"><a name="b842352706181819_1"></a><a name="b842352706181819_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.53%" id="mcps1.1.5.1.2"><p id="en-us_topic_0049139665_p27076724"><a name="en-us_topic_0049139665_p27076724"></a><a name="en-us_topic_0049139665_p27076724"></a><strong id="b84235270610580_1"><a name="b84235270610580_1"></a><a name="b84235270610580_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="8.25%" id="mcps1.1.5.1.3"><p id="en-us_topic_0049139665_p45731016"><a name="en-us_topic_0049139665_p45731016"></a><a name="en-us_topic_0049139665_p45731016"></a><strong id="b8423527061798_1"><a name="b8423527061798_1"></a><a name="b8423527061798_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.63%" id="mcps1.1.5.1.4"><p id="en-us_topic_0049139665_p13224809"><a name="en-us_topic_0049139665_p13224809"></a><a name="en-us_topic_0049139665_p13224809"></a><strong id="b842352706192251_2"><a name="b842352706192251_2"></a><a name="b842352706192251_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0049139665_row64576574"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0049139665_p63319983"><a name="en-us_topic_0049139665_p63319983"></a><a name="en-us_topic_0049139665_p63319983"></a>healthmonitor</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0049139665_p28645030"><a name="en-us_topic_0049139665_p28645030"></a><a name="en-us_topic_0049139665_p28645030"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.25%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0049139665_p38546056"><a name="en-us_topic_0049139665_p38546056"></a><a name="en-us_topic_0049139665_p38546056"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0049139665_p35222847"><a name="en-us_topic_0049139665_p35222847"></a><a name="en-us_topic_0049139665_p35222847"></a>Specifies the health check. For details, see <a href="overview-18.html#en-us_topic_0049139662_table43819641125220">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "healthmonitor": {
        "name": "",
        "admin_state_up": true,
        "tenant_id": "145483a5107745e9b3d80f956713e6a3",
        "domain_name": "www.test.com",
        "delay": 10,
        "expected_codes": "200",
        "max_retries": 10,
        "http_method": "GET",
        "timeout": 10,
        "pools": [
          {
            "id": "bb44bffb-05d9-412c-9d9c-b189d9e14193"
          }
        ],
        "url_path": "/",
        "type": "HTTP",
        "id": "2dca3867-98c5-4cde-8f2c-b89ae6bd7e36",
        "monitor_port": 112
      }
    }
    ```


## Error Codes<a name="en-us_topic_0049139655_section64643717"></a>

For details, see section  [Error Codes for Enhanced Load Balancers](error-codes-for-enhanced-load-balancers.md).

