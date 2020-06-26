# Saving Configurations<a name="EN-US_TOPIC_0220024731"></a>

## Function<a name="en-us_topic_0125376249_section143231817617"></a>

This API is used to save configurations of services, roles, and instances. This API allows you to perform the following operations:

-   Modify multiple configuration items at a time.

-   Modify multiple configuration items at service, role, and instance levels at a time.

## URI<a name="en-us_topic_0125376249_se06c5c6bada5412689ad527891487717"></a>

-   Format

POST /web/v1/config/cluster/\{cluster\_id\}/save

-   Parameter description

<a name="en-us_topic_0125376249_en-us_topic_0110839916_table7651470"></a>
<table><thead align="left"><tr id="en-us_topic_0125376249_en-us_topic_0110839916_row18935615"><th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.1"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p57389822"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p57389822"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p57389822"></a><strong id="en-us_topic_0125376249_b162774213314533_1"><a name="en-us_topic_0125376249_b162774213314533_1"></a><a name="en-us_topic_0125376249_b162774213314533_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.2"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p18063994"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p18063994"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p18063994"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="49.08%" id="mcps1.1.4.1.3"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p1179493"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p1179493"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p1179493"></a><strong id="en-us_topic_0125376249_b842352706134712"><a name="en-us_topic_0125376249_b842352706134712"></a><a name="en-us_topic_0125376249_b842352706134712"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376249_en-us_topic_0110839916_row28430119"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p21138326"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p21138326"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p21138326"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p34482841"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p34482841"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p34482841"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p16160787"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p16160787"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p16160787"></a>Cluster ID that is displayed on MRS Manager. The default cluster ID is <strong id="en-us_topic_0125376249_b842352706152828"><a name="en-us_topic_0125376249_b842352706152828"></a><a name="en-us_topic_0125376249_b842352706152828"></a>1</strong>, because MRS Manager supports management of only one cluster currently.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0125376249_s971d9bc6c27b4972a1817a7438721fe0"></a>

-   Example:

```
POST /web/v1/config/cluster/{cluster_id}/save HTTP/1.1  
Host: example.com  
Content-Type: application/json  
Accept:application/json  
{
  "id": 0,
  "user_password": "string",
  "configurations_summary": {
    "restart_affected_components": true,
    "components": [
      {
        "component_name": "string",
        "configurations": [
          {
            "name": "string",
            "value": "string",
            "default_value": "string",
            "description": "string",
            "type": "string",
            "config_group_type": "string",
            "config_group": "string",
            "item_type": "string",
            "item_conf": "string",
            "item_event": "string",
            "weak_reference": "string"
          }
        ],
        "children": [
          {
            "role_name": "string",
            "configurations": [],
            "children": [
              {
                "node": {
                  "id": 0,
                  "name": "string",
                  "description": "string",
                  "controller_id": "string",
                  "ip_address": "string",
                  "business_ip_address": "string",
                  "rack": "string",
                  "host_name": "string",
                  "total_memory": "string",
                  "available_memory": "string",
                  "total_hard_disk_space": "string",
                  "available_hard_disk_space": "string",
                  "no_of_CPUs": "string",
                  "available_swap_memory": "string",
                  "total_swap_memory": "string",
                  "cpu_usage": "string",
                  "disk_usage": "string",
                  "health_status": "GOOD",
                  "memory_usage": "string",
                  "swap_memory_usage": "string",
                  "files_info": [
                    {
                      "name": "string",
                      "description": "string"
                    }
                  ],
                  "operational_status": "STARTED",
                  "network_read": "string",
                  "network_write": "string",
                  "instances": [
                    {
                      "name": "string",
                      "id": "string",
                      "operational_status": "STARTED",
                      "health_status": "GOOD",
                      "ha_status": "ACTIVE",
                      "config_status": {
                        "level": "string",
                        "status": "UNKNOWN",
                        "description": "string"
                      },
                      "role_name": "string",
                      "service_name": "string",
                      "web_UI_address": "string",
                      "is_service_role": true,
                      "pair_name": "string",
                      "support_decom": true
                    }
                  ],
                  "is_OMS_node": true
                },
                "configurations": []
              }
            ],
            "classification": [
              {
                "name": "string",
                "description": "string"
              }
            ]
          }
        ],
        "classification": [
          {
            "name": "string",
            "description": "string"
          }
        ]
      }
    ]
  }
}
```

-   Parameter description

**Table  1**  Request parameter description

<a name="en-us_topic_0125376249_en-us_topic_0110839916_table29944381"></a>
<table><thead align="left"><tr id="en-us_topic_0125376249_en-us_topic_0110839916_row28997204"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p67072226"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p67072226"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p67072226"></a><strong id="en-us_topic_0125376249_b7617970162543"><a name="en-us_topic_0125376249_b7617970162543"></a><a name="en-us_topic_0125376249_b7617970162543"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p64141236"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p64141236"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p64141236"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p28057651"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p28057651"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p28057651"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p737610"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p737610"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p737610"></a><strong id="en-us_topic_0125376249_b842352706134712_1"><a name="en-us_topic_0125376249_b842352706134712_1"></a><a name="en-us_topic_0125376249_b842352706134712_1"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376249_en-us_topic_0110839916_row59746443"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p7623680"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p7623680"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p7623680"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p13538321"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p13538321"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p13538321"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p22862248"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p22862248"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p22862248"></a>LONG</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p10347541"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p10347541"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p10347541"></a>Asynchronous task ID (meaningless in other scenarios). The default value is <strong id="en-us_topic_0125376249_b842352706191850"><a name="en-us_topic_0125376249_b842352706191850"></a><a name="en-us_topic_0125376249_b842352706191850"></a>-1</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row26019009"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p27164986"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p27164986"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p27164986"></a>user_password</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p52880292"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p52880292"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p52880292"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p55445287"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p55445287"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p55445287"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p7324497"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p7324497"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p7324497"></a>User password</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row65920477"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p37958388"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p37958388"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p37958388"></a>configurations_summary</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p54730608"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p54730608"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p54730608"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p3994297"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p3994297"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p3994297"></a>REFERENCE</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p38728787"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p38728787"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p38728787"></a>Configures a description object.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **configurations\_summary**  parameter description

<a name="en-us_topic_0125376249_en-us_topic_0110839916_table50024034"></a>
<table><thead align="left"><tr id="en-us_topic_0125376249_en-us_topic_0110839916_row5189504"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p17696705"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p17696705"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p17696705"></a><strong id="en-us_topic_0125376249_b7617970162543_1"><a name="en-us_topic_0125376249_b7617970162543_1"></a><a name="en-us_topic_0125376249_b7617970162543_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p24147039"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p24147039"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p24147039"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p9753153"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p9753153"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p9753153"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p5579795"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p5579795"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p5579795"></a><strong id="en-us_topic_0125376249_b842352706134712_2"><a name="en-us_topic_0125376249_b842352706134712_2"></a><a name="en-us_topic_0125376249_b842352706134712_2"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376249_en-us_topic_0110839916_row49310231"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p34705768"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p34705768"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p34705768"></a>restart_affected_components</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p59703789"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p59703789"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p59703789"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p4168718"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p4168718"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p4168718"></a>BOOLEAN</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p30310318"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p30310318"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p30310318"></a>Whether to restart the affected components</p>
<p id="en-us_topic_0125376249_en-us_topic_0110839916_p4357413"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p4357413"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p4357413"></a><strong id="en-us_topic_0125376249_b84235270620459"><a name="en-us_topic_0125376249_b84235270620459"></a><a name="en-us_topic_0125376249_b84235270620459"></a>true</strong>: Restart</p>
<p id="en-us_topic_0125376249_en-us_topic_0110839916_p39216722"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p39216722"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p39216722"></a><strong id="en-us_topic_0125376249_b8423527062059"><a name="en-us_topic_0125376249_b8423527062059"></a><a name="en-us_topic_0125376249_b8423527062059"></a>false</strong>: Do not restart</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row17406182"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p614639"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p614639"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p614639"></a>components</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p49785833"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p49785833"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p49785833"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p6120700"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p6120700"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p6120700"></a>ARRAY_REFERENCE</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p39995614"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p39995614"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p39995614"></a>Service list</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **components**  parameter description

<a name="en-us_topic_0125376249_en-us_topic_0110839916_table18419338"></a>
<table><thead align="left"><tr id="en-us_topic_0125376249_en-us_topic_0110839916_row66916545"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p51531064"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p51531064"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p51531064"></a><strong id="en-us_topic_0125376249_b7617970162543_2"><a name="en-us_topic_0125376249_b7617970162543_2"></a><a name="en-us_topic_0125376249_b7617970162543_2"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p13266647"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p13266647"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p13266647"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p856647"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p856647"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p856647"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p58288522"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p58288522"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p58288522"></a><strong id="en-us_topic_0125376249_b842352706134712_3"><a name="en-us_topic_0125376249_b842352706134712_3"></a><a name="en-us_topic_0125376249_b842352706134712_3"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376249_en-us_topic_0110839916_row23749836"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p44688550"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p44688550"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p44688550"></a>component_name</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p63002817"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p63002817"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p63002817"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p2954565"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p2954565"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p2954565"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p30913106"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p30913106"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p30913106"></a>Service name</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row9782500"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p54185029"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p54185029"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p54185029"></a>configurations</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p26911194"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p26911194"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p26911194"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p32323083"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p32323083"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p32323083"></a>ARRAY_REFERENCE</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_p675119494481"><a name="en-us_topic_0125376249_p675119494481"></a><a name="en-us_topic_0125376249_p675119494481"></a>Description of the service, role, or instance level.</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row23209435"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p916111"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p916111"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p916111"></a>children</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p7096167"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p7096167"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p7096167"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p37918668"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p37918668"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p37918668"></a>ARRAY_REFERENCE</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p39306804"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p39306804"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p39306804"></a>Sublevel description array. The sublevel of the service level is role.</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row18216917"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p66284155"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p66284155"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p66284155"></a>classification</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p307511"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p307511"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p307511"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p24908398"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p24908398"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p24908398"></a>ARRAY_REFERENCE</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p58174480"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p58174480"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p58174480"></a>Configuration definition information</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **children**  parameter description

<a name="en-us_topic_0125376249_en-us_topic_0110839916_table32097378"></a>
<table><thead align="left"><tr id="en-us_topic_0125376249_en-us_topic_0110839916_row37351504"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p5572963"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p5572963"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p5572963"></a><strong id="en-us_topic_0125376249_b7617970162543_3"><a name="en-us_topic_0125376249_b7617970162543_3"></a><a name="en-us_topic_0125376249_b7617970162543_3"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p48756830"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p48756830"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p48756830"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p56989162"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p56989162"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p56989162"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p12943361"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p12943361"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p12943361"></a><strong id="en-us_topic_0125376249_b842352706134712_4"><a name="en-us_topic_0125376249_b842352706134712_4"></a><a name="en-us_topic_0125376249_b842352706134712_4"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376249_en-us_topic_0110839916_row41779295"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p28679701"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p28679701"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p28679701"></a>role_name</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p41354444"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p41354444"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p41354444"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p61375659"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p61375659"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p61375659"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p16869453"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p16869453"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p16869453"></a>Role name</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row17607349"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p16909137"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p16909137"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p16909137"></a>configurations</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p27462882"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p27462882"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p27462882"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p9901008"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p9901008"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p9901008"></a>ARRAY_REFERENCE</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p59344108"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p59344108"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p59344108"></a>Configuration item description array: Service level/role level/instance level</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row64334932"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p43747012"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p43747012"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p43747012"></a>children</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p53847064"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p53847064"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p53847064"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p66644921"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p66644921"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p66644921"></a>ARRAY_REFERENCE</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p52158974"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p52158974"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p52158974"></a>Sublevel description array. The sublevel of the role level is instance.</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row66777590"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p40275672"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p40275672"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p40275672"></a>classification</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p41104015"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p41104015"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p41104015"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p41090947"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p41090947"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p41090947"></a>ARRAY_REFERENCE</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p58381122"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p58381122"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p58381122"></a>Configuration definition information</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **configurations**  parameter description of services, roles, and instances

<a name="en-us_topic_0125376249_en-us_topic_0110839916_table31250469"></a>
<table><thead align="left"><tr id="en-us_topic_0125376249_en-us_topic_0110839916_row36612450"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p12818494"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p12818494"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p12818494"></a><strong id="en-us_topic_0125376249_b7617970162543_4"><a name="en-us_topic_0125376249_b7617970162543_4"></a><a name="en-us_topic_0125376249_b7617970162543_4"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p31665127"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p31665127"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p31665127"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p14738500"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p14738500"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p14738500"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p32499751"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p32499751"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p32499751"></a><strong id="en-us_topic_0125376249_b842352706134712_5"><a name="en-us_topic_0125376249_b842352706134712_5"></a><a name="en-us_topic_0125376249_b842352706134712_5"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376249_en-us_topic_0110839916_row15234150"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p26006626"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p26006626"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p26006626"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p26161922"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p26161922"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p26161922"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p38740910"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p38740910"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p38740910"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p45779855"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p45779855"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p45779855"></a>Name of the configuration item to be saved</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row9365518"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p20409457"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p20409457"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p20409457"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p42553358"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p42553358"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p42553358"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p24269963"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p24269963"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p24269963"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p65432404"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p65432404"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p65432404"></a>Value to be saved</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row52020732"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p52929795"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p52929795"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p52929795"></a>default_value</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p59454965"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p59454965"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p59454965"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p51122876"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p51122876"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p51122876"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p37638813"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p37638813"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p37638813"></a>Default value</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row3204999"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p58278394"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p58278394"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p58278394"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p22929453"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p22929453"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p22929453"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p45346376"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p45346376"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p45346376"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p63528221"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p63528221"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p63528221"></a>Configuration item description</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row34883083"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p6957508"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p6957508"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p6957508"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p26687281"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p26687281"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p26687281"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p14186171"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p14186171"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p14186171"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p36212115"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p36212115"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p36212115"></a>Configuration item type</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row57473582"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p24848535"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p24848535"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p24848535"></a>config_group_type</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p66574280"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p66574280"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p66574280"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p23807594"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p23807594"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p23807594"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p29172995"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p29172995"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p29172995"></a>Configuration group type</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row61230363"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p60712366"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p60712366"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p60712366"></a>config_group</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p18754622"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p18754622"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p18754622"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p42729394"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p42729394"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p42729394"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p56019961"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p56019961"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p56019961"></a>Configuration group</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row34417608"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p36362896"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p36362896"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p36362896"></a>item_type</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p59713448"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p59713448"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p59713448"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p4951096"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p4951096"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p4951096"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p11394508"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p11394508"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p11394508"></a>Type of the configuration item value to be saved</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row35441715"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p52206665"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p52206665"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p52206665"></a>item_conf</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p881443"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p881443"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p881443"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p4288041"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p4288041"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p4288041"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p25601496"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p25601496"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p25601496"></a>Configuration item value validity check</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row29086880"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p7227054"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p7227054"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p7227054"></a>item_event</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p48520468"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p48520468"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p48520468"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p37843835"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p37843835"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p37843835"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p44490435"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p44490435"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p44490435"></a>Event type of a configuration item. Currently, only <strong id="en-us_topic_0125376249_b842352706202144"><a name="en-us_topic_0125376249_b842352706202144"></a><a name="en-us_topic_0125376249_b842352706202144"></a>hide-show</strong> is supported.</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row64869596"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p19945884"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p19945884"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p19945884"></a>weak_reference</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p5003880"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p5003880"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p5003880"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p2661161"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p2661161"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p2661161"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p65487800"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p65487800"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p65487800"></a>Whether a configuration item is a weak reference. If the configuration item is a weak reference, the configuration parsing is passed even though the configuration item name or role name does not exist, and the value will be set to an empty string.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **classification**  parameter description

<a name="en-us_topic_0125376249_en-us_topic_0110839916_table2911579"></a>
<table><thead align="left"><tr id="en-us_topic_0125376249_en-us_topic_0110839916_row9061374"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p62882733"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p62882733"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p62882733"></a><strong id="en-us_topic_0125376249_b7617970162543_5"><a name="en-us_topic_0125376249_b7617970162543_5"></a><a name="en-us_topic_0125376249_b7617970162543_5"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p60336645"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p60336645"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p60336645"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p55430061"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p55430061"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p55430061"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p35759767"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p35759767"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p35759767"></a><strong id="en-us_topic_0125376249_b842352706134712_6"><a name="en-us_topic_0125376249_b842352706134712_6"></a><a name="en-us_topic_0125376249_b842352706134712_6"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376249_en-us_topic_0110839916_row10860049"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p7248804"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p7248804"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p7248804"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p50282231"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p50282231"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p50282231"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p46328882"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p46328882"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p46328882"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p33428583"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p33428583"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p33428583"></a>Name</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row32421797"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p8919934"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p8919934"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p8919934"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p51426059"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p51426059"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p51426059"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p4761269"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p4761269"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p4761269"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p61150701"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p61150701"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p61150701"></a>Description</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0125376249_sb039594d40ea435589069822075fc5f6"></a>

-   Example:

    ```
    HTTP/1.1 200 OK
    Data:Wed,02 May 2018 10:10:01 GMT
    Server: example-server
    Content-Type: application/json
    {
      "id": 0,
      "state": "COMPLETE",
      "error_code": 0,
      "error_description": "string",
      "total_progress": 0
    }
    ```

-   Response parameter description

<a name="en-us_topic_0125376249_en-us_topic_0110839916_table45442885"></a>
<table><thead align="left"><tr id="en-us_topic_0125376249_en-us_topic_0110839916_row8144950"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.1.5.1.1"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p55761186"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p55761186"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p55761186"></a><strong id="en-us_topic_0125376249_b7617970162543_6"><a name="en-us_topic_0125376249_b7617970162543_6"></a><a name="en-us_topic_0125376249_b7617970162543_6"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.1.5.1.2"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p20362243"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p20362243"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p20362243"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.1.5.1.3"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p38729025"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p38729025"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p38729025"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.1.5.1.4"><p id="en-us_topic_0125376249_en-us_topic_0110839916_p37737141"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p37737141"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p37737141"></a><strong id="en-us_topic_0125376249_b842352706134712_7"><a name="en-us_topic_0125376249_b842352706134712_7"></a><a name="en-us_topic_0125376249_b842352706134712_7"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376249_en-us_topic_0110839916_row36809589"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p28786713"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p28786713"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p28786713"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p50022410"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p50022410"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p50022410"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p25283375"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p25283375"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p25283375"></a>LONG</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p18351721"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p18351721"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p18351721"></a>Asynchronous task ID (meaningless in other scenarios). The default value is <strong id="en-us_topic_0125376249_b842352706191850_1"><a name="en-us_topic_0125376249_b842352706191850_1"></a><a name="en-us_topic_0125376249_b842352706191850_1"></a>-1</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row30947767"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p23741175"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p23741175"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p23741175"></a>state</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p43987032"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p43987032"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p43987032"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p6179841"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p6179841"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p6179841"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p46486449"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p46486449"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p46486449"></a>Cluster status. The value <strong id="en-us_topic_0125376249_b842352706191926"><a name="en-us_topic_0125376249_b842352706191926"></a><a name="en-us_topic_0125376249_b842352706191926"></a>FAILED</strong>&nbsp;indicates that the command fails to be executed. The value&nbsp;<strong id="en-us_topic_0125376249_b842352706191940"><a name="en-us_topic_0125376249_b842352706191940"></a><a name="en-us_topic_0125376249_b842352706191940"></a>COMPLETE</strong> indicates that the command is successfully executed.</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row15724863"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p65754424"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p65754424"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p65754424"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p24508133"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p24508133"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p24508133"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p39001775"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p39001775"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p39001775"></a>INTEGER</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p32990791"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p32990791"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p32990791"></a>Error code returned</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row28481666"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p25313579"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p25313579"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p25313579"></a>error_description</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p37133980"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p37133980"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p37133980"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p55062398"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p55062398"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p55062398"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p65645783"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p65645783"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p65645783"></a>Error code description</p>
</td>
</tr>
<tr id="en-us_topic_0125376249_en-us_topic_0110839916_row53941135"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p7155810"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p7155810"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p7155810"></a>total_progress</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p42749746"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p42749746"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p42749746"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p40177382"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p40177382"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p40177382"></a>FLOAT</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376249_en-us_topic_0110839916_p15243245"><a name="en-us_topic_0125376249_en-us_topic_0110839916_p15243245"></a><a name="en-us_topic_0125376249_en-us_topic_0110839916_p15243245"></a>Total progress</p>
</td>
</tr>
</tbody>
</table>

## Status Code<a name="en-us_topic_0125376249_section2092982712508"></a>

<a name="en-us_topic_0125376249_table2979011121511"></a>
<table><thead align="left"><tr id="en-us_topic_0125376249_row3981161161515"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.3.1.1"><p id="en-us_topic_0125376249_p398115116158"><a name="en-us_topic_0125376249_p398115116158"></a><a name="en-us_topic_0125376249_p398115116158"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83%" id="mcps1.1.3.1.2"><p id="en-us_topic_0125376249_p1798121191515"><a name="en-us_topic_0125376249_p1798121191515"></a><a name="en-us_topic_0125376249_p1798121191515"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376249_row69813112155"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0125376249_p15667142018546"><a name="en-us_topic_0125376249_p15667142018546"></a><a name="en-us_topic_0125376249_p15667142018546"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0125376249_p23378286542"><a name="en-us_topic_0125376249_p23378286542"></a><a name="en-us_topic_0125376249_p23378286542"></a>The operation is successful.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

