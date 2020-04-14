# Querying Details About extra\_specs Parameters of a BMS Flavor \(Native OpenStack API\)<a name="EN-US_TOPIC_0114885743"></a>

## Function<a name="section62221755111516"></a>

**extra\_specs**  parameters specify the key-value pair of a BMS flavor. For example,  **baremetal:extBootType**  specifies the boot device of the BMS. Its value can be  **LocalDisk**  \(local disk\) or  **Volume**  \(EVS disk\). If you want to check whether a flavor supports quick provisioning, you can call this API.

## URI<a name="section116617920169"></a>

GET /v2.1/\{project\_id\}/flavors/\{flavors\_id\}/os-extra\_specs

[Table 1](#table955744812451)  lists the parameters.

**Table  1**  Parameter description

<a name="table955744812451"></a>
<table><thead align="left"><tr id="row1155794814454"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057973064_p26298136"><a name="en-us_topic_0057973064_p26298136"></a><a name="en-us_topic_0057973064_p26298136"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057973064_p49774232"><a name="en-us_topic_0057973064_p49774232"></a><a name="en-us_topic_0057973064_p49774232"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057973064_p5180964"><a name="en-us_topic_0057973064_p5180964"></a><a name="en-us_topic_0057973064_p5180964"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13559114874517"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973064_p35224963"><a name="en-us_topic_0057973064_p35224963"></a><a name="en-us_topic_0057973064_p35224963"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973064_p34649765"><a name="en-us_topic_0057973064_p34649765"></a><a name="en-us_topic_0057973064_p34649765"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973064_p55167604"><a name="en-us_topic_0057973064_p55167604"></a><a name="en-us_topic_0057973064_p55167604"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row255944854514"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973064_p18974100"><a name="en-us_topic_0057973064_p18974100"></a><a name="en-us_topic_0057973064_p18974100"></a>flavors_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973064_p60507121"><a name="en-us_topic_0057973064_p60507121"></a><a name="en-us_topic_0057973064_p60507121"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973064_p2129750"><a name="en-us_topic_0057973064_p2129750"></a><a name="en-us_topic_0057973064_p2129750"></a>Specifies the flavor ID.</p>
<p id="p1461914516495"><a name="p1461914516495"></a><a name="p1461914516495"></a>You can obtain the flavor ID from the <span id="en-us_topic_0053158674_text374914110111"><a name="en-us_topic_0053158674_text374914110111"></a><a name="en-us_topic_0053158674_text374914110111"></a>BMS</span><span id="en-us_topic_0053158674_text1749131818"><a name="en-us_topic_0053158674_text1749131818"></a><a name="en-us_topic_0053158674_text1749131818"></a></span> console or using the <a href="querying-bms-flavors-(native-openstack-api).md">Querying BMS Flavors (Native OpenStack API)</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section1517812126172"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/flavors/physical.s2.medium/os-extra_specs
    ```


## Response Message<a name="section3899184185"></a>

-   Response parameters

    <a name="en-us_topic_0057973064_table28168569"></a>
    <table><thead align="left"><tr id="en-us_topic_0057973064_row26406300"><th class="cellrowborder" valign="top" width="21.95%" id="mcps1.1.4.1.1"><p id="p59978491115233"><a name="p59978491115233"></a><a name="p59978491115233"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.95%" id="mcps1.1.4.1.2"><p id="p26419641115233"><a name="p26419641115233"></a><a name="p26419641115233"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.10000000000001%" id="mcps1.1.4.1.3"><p id="p64181866115233"><a name="p64181866115233"></a><a name="p64181866115233"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0057973064_row46433444"><td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0057973064_p3012613"><a name="en-us_topic_0057973064_p3012613"></a><a name="en-us_topic_0057973064_p3012613"></a>extra_specs</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0057973064_p42695066"><a name="en-us_topic_0057973064_p42695066"></a><a name="en-us_topic_0057973064_p42695066"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0057973064_p9931138"><a name="en-us_topic_0057973064_p9931138"></a><a name="en-us_topic_0057973064_p9931138"></a>Specifies the key-value pair of a <span id="text6300153138"><a name="text6300153138"></a><a name="text6300153138"></a>BMS</span><span id="text13005314316"><a name="text13005314316"></a><a name="text13005314316"></a></span> flavor.</p>
    <a name="ul6746628171115"></a><a name="ul6746628171115"></a><ul id="ul6746628171115"><li><strong id="b1834750114010"><a name="b1834750114010"></a><a name="b1834750114010"></a>capabilities:cpu_arch</strong>: specifies the CPU architecture of the <span id="text46223511313"><a name="text46223511313"></a><a name="text46223511313"></a>BMS</span><span id="text3622651316"><a name="text3622651316"></a><a name="text3622651316"></a></span>. The value can be <strong id="b13963733154212"><a name="b13963733154212"></a><a name="b13963733154212"></a>x86_64</strong> (for x86 servers) or <strong id="b1622965574218"><a name="b1622965574218"></a><a name="b1622965574218"></a>aarch64</strong> (for ARM servers).</li><li><strong id="b15196639576"><a name="b15196639576"></a><a name="b15196639576"></a>baremetal:disk_detail</strong>: specifies the disk description.</li><li><strong id="b11843105618712"><a name="b11843105618712"></a><a name="b11843105618712"></a>capabilities:hypervisor_type</strong>: specifies the hypervisor type. The value is fixed at <strong id="b191615141280"><a name="b191615141280"></a><a name="b191615141280"></a>ironic</strong>.</li><li><strong id="b123992302081"><a name="b123992302081"></a><a name="b123992302081"></a>baremetal:__support_evs</strong>: specifies whether to support EVS disks. The value can be <strong id="b208618517912"><a name="b208618517912"></a><a name="b208618517912"></a>true</strong> or <strong id="b494067494"><a name="b494067494"></a><a name="b494067494"></a>false</strong>.</li><li><strong id="b1826411507919"><a name="b1826411507919"></a><a name="b1826411507919"></a>baremetal:extBootType</strong>: specifies the boot device of the <span id="text193781491131"><a name="text193781491131"></a><a name="text193781491131"></a>BMS</span><span id="text1037816914313"><a name="text1037816914313"></a><a name="text1037816914313"></a></span>. The value can be <strong id="b964584291014"><a name="b964584291014"></a><a name="b964584291014"></a>LocalDisk</strong> (local disk) or <strong id="b381702512106"><a name="b381702512106"></a><a name="b381702512106"></a>Volume</strong> (EVS disk).</li><li><strong id="b20941920111018"><a name="b20941920111018"></a><a name="b20941920111018"></a>baremetal:net_num</strong>: specifies the number of NICs that can be attached to a <span id="text105681112318"><a name="text105681112318"></a><a name="text105681112318"></a>BMS</span><span id="text9568811236"><a name="text9568811236"></a><a name="text9568811236"></a></span>.</li><li><strong id="b553105913112"><a name="b553105913112"></a><a name="b553105913112"></a>baremetal:netcard_detail</strong>: specifies description of the NIC.</li><li><strong id="b65187165126"><a name="b65187165126"></a><a name="b65187165126"></a>baremetal:cpu_detail</strong>: specifies description of the CPU.</li><li><strong id="b4232103119127"><a name="b4232103119127"></a><a name="b4232103119127"></a>resource_type</strong>: specifies the resource type. The value is fixed at <strong id="b137541842141220"><a name="b137541842141220"></a><a name="b137541842141220"></a>ironic</strong>.</li><li><strong id="b8760174821217"><a name="b8760174821217"></a><a name="b8760174821217"></a>baremetal:memory_detail</strong>: specifies description of the memory.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "extra_specs": {
            "capabilities:cpu_arch": "x86_64",
            "baremetal:disk_detail": "SAS 8T",
            "capabilities:hypervisor_type": "ironic",
            "baremetal:__support_evs": "true",
            "baremetal:extBootType": "LocalDisk",
            "capabilities:board_type": "s2m",
            "baremetal:net_num": "2",
            "baremetal:netcard_detail": "2*10GE",
            "baremetal:cpu_detail": "2*8coreIntel Xeon E5-2667 V43.2GHz",
            "resource_type": "ironic",
            "baremetal:memory_detail": "256GB DDR4 RAM(GB)"
        }
    }
    ```


## Returned Values<a name="section7610951"></a>

Normal values

<a name="en-us_topic_0106040941_table753804619176"></a>
<table><thead align="left"><tr id="en-us_topic_0106040941_row10735134615172"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="en-us_topic_0106040941_p19735204616177"><a name="en-us_topic_0106040941_p19735204616177"></a><a name="en-us_topic_0106040941_p19735204616177"></a>Returned Values</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="en-us_topic_0106040941_p207355465176"><a name="en-us_topic_0106040941_p207355465176"></a><a name="en-us_topic_0106040941_p207355465176"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0106040941_row1473514621713"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0106040941_p13735144611178"><a name="en-us_topic_0106040941_p13735144611178"></a><a name="en-us_topic_0106040941_p13735144611178"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0106040941_p207351246161711"><a name="en-us_topic_0106040941_p207351246161711"></a><a name="en-us_topic_0106040941_p207351246161711"></a>The server has successfully processed the request.</p>
</td>
</tr>
</tbody>
</table>

For details about other returned values, see  [Status Codes](status-codes.md).

## Error Codes<a name="section14752650154917"></a>

See  [Error Codes](error-codes.md).

