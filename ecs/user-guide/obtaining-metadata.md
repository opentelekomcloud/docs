# Obtaining Metadata<a name="EN-US_TOPIC_0042400609"></a>

ECS metadata includes basic information of an ECS on the cloud platform, such as the ECS ID, hostname, and network information. ECS metadata can be obtained using either OpenStack APIs or EC2 APIs, as shown in  [Table 1](#table273552371680).

**Table  1**  ECS metadata types

<a name="table273552371680"></a>
<table><thead align="left"><tr id="row459785021680"><th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.4.1.1"><p id="p1611763716833"><a name="p1611763716833"></a><a name="p1611763716833"></a>Metadata Type</p>
</th>
<th class="cellrowborder" valign="top" width="23.05%" id="mcps1.2.4.1.2"><p id="p304933271680"><a name="p304933271680"></a><a name="p304933271680"></a>Metadata Item</p>
</th>
<th class="cellrowborder" valign="top" width="52.459999999999994%" id="mcps1.2.4.1.3"><p id="p213207321680"><a name="p213207321680"></a><a name="p213207321680"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row378821081680"><td class="cellrowborder" rowspan="5" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p809695916822"><a name="p809695916822"></a><a name="p809695916822"></a>OpenStack type</p>
</td>
<td class="cellrowborder" valign="top" width="23.05%" headers="mcps1.2.4.1.2 "><p id="p175787921680"><a name="p175787921680"></a><a name="p175787921680"></a>/meta_data.json</p>
</td>
<td class="cellrowborder" valign="top" width="52.459999999999994%" headers="mcps1.2.4.1.3 "><p id="p426193551680"><a name="p426193551680"></a><a name="p426193551680"></a>Displays ECS metadata.</p>
<p id="p63391215141014"><a name="p63391215141014"></a><a name="p63391215141014"></a>For the key fields in the ECS metadata, see <a href="#table2373623012315">Table 2</a>.</p>
</td>
</tr>
<tr id="row292374981680"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p163874991680"><a name="p163874991680"></a><a name="p163874991680"></a>/password</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p409248351680"><a name="p409248351680"></a><a name="p409248351680"></a>Displays the password for logging in to an ECS.</p>
<p id="p661917247101"><a name="p661917247101"></a><a name="p661917247101"></a>This metadata is used by Cloudbase-Init to store ciphertext passwords during initialization of key-pair-authenticated Windows ECSs.</p>
</td>
</tr>
<tr id="row104562411680"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p11850321680"><a name="p11850321680"></a><a name="p11850321680"></a>/user_data</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p98983401680"><a name="p98983401680"></a><a name="p98983401680"></a>Displays ECS user data.</p>
<p id="p465163616106"><a name="p465163616106"></a><a name="p465163616106"></a>This metadata allows you to specify scripts and configuration files for initializing ECSs. For details, see <a href="injecting-user-data-into-ecss.md">Injecting User Data into ECSs</a>.</p>
<p id="p865193611107"><a name="p865193611107"></a><a name="p865193611107"></a>For password-authenticated Linux ECSs, this metadata is used to save password injection scripts.</p>
</td>
</tr>
<tr id="row216681141680"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p21457114512"><a name="p21457114512"></a><a name="p21457114512"></a>/network_data.json</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p31455115119"><a name="p31455115119"></a><a name="p31455115119"></a>Displays ECS network information.</p>
</td>
</tr>
<tr id="row19335028144551"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p714571205111"><a name="p714571205111"></a><a name="p714571205111"></a>/securitykey</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p17145915518"><a name="p17145915518"></a><a name="p17145915518"></a>Obtains temporary AKs and SKs.</p>
<p id="p11608355141017"><a name="p11608355141017"></a><a name="p11608355141017"></a>Before enabling an ECS to obtain a temporary AK and SK, make sure that the <strong id="b84235270615356"><a name="b84235270615356"></a><a name="b84235270615356"></a>op_svc_ecs</strong> account has been authorized on IAM and that the desired ECS resources have been authorized for management.</p>
</td>
</tr>
<tr id="row16772135161746"><td class="cellrowborder" rowspan="8" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p4373564516822"><a name="p4373564516822"></a><a name="p4373564516822"></a>EC2 type</p>
</td>
<td class="cellrowborder" valign="top" width="23.05%" headers="mcps1.2.4.1.2 "><p id="p10396761161746"><a name="p10396761161746"></a><a name="p10396761161746"></a>/meta-data/hostname</p>
</td>
<td class="cellrowborder" valign="top" width="52.459999999999994%" headers="mcps1.2.4.1.3 "><p id="p45518664161746"><a name="p45518664161746"></a><a name="p45518664161746"></a>Displays the name of the host accommodating an ECS.</p>
<p id="p138091329218"><a name="p138091329218"></a><a name="p138091329218"></a>To remove the suffix <strong id="b842352706145759"><a name="b842352706145759"></a><a name="b842352706145759"></a>.novalocal</strong> from an ECS, see:</p>
<p id="p1117557174416"><a name="p1117557174416"></a><a name="p1117557174416"></a><a href="is-an-ecs-hostname-with-suffix-novalocal-normal.md">Is an ECS Hostname with Suffix .novalocal Normal?</a></p>
</td>
</tr>
<tr id="row35033331161746"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p24758917161746"><a name="p24758917161746"></a><a name="p24758917161746"></a>/meta-data/instance-type</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p21785021161746"><a name="p21785021161746"></a><a name="p21785021161746"></a>Displays an ECS flavor.</p>
</td>
</tr>
<tr id="row25345840161746"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p177222426305"><a name="p177222426305"></a><a name="p177222426305"></a>/meta-data/local-ipv4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p39741144528"><a name="p39741144528"></a><a name="p39741144528"></a>Displays the fixed IP address of an ECS.</p>
<p id="p15298182161746"><a name="p15298182161746"></a><a name="p15298182161746"></a>If there are multiple NICs, only the IP address of the primary NIC is displayed.</p>
</td>
</tr>
<tr id="row898531716190"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p2079227616190"><a name="p2079227616190"></a><a name="p2079227616190"></a>/meta-data/placement/availability-zone</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1219338216190"><a name="p1219338216190"></a><a name="p1219338216190"></a>Displays the AZ accommodating an ECS.</p>
</td>
</tr>
<tr id="row1017501716190"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p631251216190"><a name="p631251216190"></a><a name="p631251216190"></a>/meta-data/public-ipv4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1836582505313"><a name="p1836582505313"></a><a name="p1836582505313"></a>Displays the EIP bound to an ECS.</p>
<p id="p308179816190"><a name="p308179816190"></a><a name="p308179816190"></a>If there are multiple NICs, only the EIP of the primary NIC is displayed.</p>
</td>
</tr>
<tr id="row6185333416190"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p158411821163117"><a name="p158411821163117"></a><a name="p158411821163117"></a>/meta-data/public-keys/0/openssh-key</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p2942083216190"><a name="p2942083216190"></a><a name="p2942083216190"></a>Displays the public key of an ECS.</p>
</td>
</tr>
<tr id="row2268075016190"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p4362812316190"><a name="p4362812316190"></a><a name="p4362812316190"></a>/user-data</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p5919884816190"><a name="p5919884816190"></a><a name="p5919884816190"></a>Displays ECS user data.</p>
</td>
</tr>
<tr id="row3380124162159"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p21312452162159"><a name="p21312452162159"></a><a name="p21312452162159"></a>/meta-data/security-groups</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p7578912162159"><a name="p7578912162159"></a><a name="p7578912162159"></a>Displays the security group to which an ECS belongs.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Metadata key fields

<a name="table2373623012315"></a>
<table><thead align="left"><tr id="row4787810512315"><th class="cellrowborder" valign="top" width="24.959999999999997%" id="mcps1.2.4.1.1"><p id="p135337462439"><a name="p135337462439"></a><a name="p135337462439"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.349999999999998%" id="mcps1.2.4.1.2"><p id="p2054974617431"><a name="p2054974617431"></a><a name="p2054974617431"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.690000000000005%" id="mcps1.2.4.1.3"><p id="p75495461436"><a name="p75495461436"></a><a name="p75495461436"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1717815342412"><td class="cellrowborder" valign="top" width="24.959999999999997%" headers="mcps1.2.4.1.1 "><p id="p91796345418"><a name="p91796345418"></a><a name="p91796345418"></a>uuid</p>
</td>
<td class="cellrowborder" valign="top" width="20.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p1438181511138"><a name="p1438181511138"></a><a name="p1438181511138"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.690000000000005%" headers="mcps1.2.4.1.3 "><p id="p138151561316"><a name="p138151561316"></a><a name="p138151561316"></a>Specifies an ECS ID.</p>
</td>
</tr>
<tr id="row7197172751211"><td class="cellrowborder" valign="top" width="24.959999999999997%" headers="mcps1.2.4.1.1 "><p id="p171982279122"><a name="p171982279122"></a><a name="p171982279122"></a>availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="20.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p131981527161214"><a name="p131981527161214"></a><a name="p131981527161214"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.690000000000005%" headers="mcps1.2.4.1.3 "><p id="p819818276124"><a name="p819818276124"></a><a name="p819818276124"></a>Specifies the AZ where an ECS locates.</p>
</td>
</tr>
<tr id="row1961315241786"><td class="cellrowborder" valign="top" width="24.959999999999997%" headers="mcps1.2.4.1.1 "><p id="p156131424089"><a name="p156131424089"></a><a name="p156131424089"></a>meta</p>
</td>
<td class="cellrowborder" valign="top" width="20.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p66147241387"><a name="p66147241387"></a><a name="p66147241387"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="54.690000000000005%" headers="mcps1.2.4.1.3 "><p id="p11614124384"><a name="p11614124384"></a><a name="p11614124384"></a>Specifies the metadata information, including the image name, image ID, and VPC ID.</p>
</td>
</tr>
<tr id="row4117204012123"><td class="cellrowborder" valign="top" width="24.959999999999997%" headers="mcps1.2.4.1.1 "><p id="p8117040181218"><a name="p8117040181218"></a><a name="p8117040181218"></a>hostname</p>
</td>
<td class="cellrowborder" valign="top" width="20.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p51174405125"><a name="p51174405125"></a><a name="p51174405125"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.690000000000005%" headers="mcps1.2.4.1.3 "><p id="p1555373117469"><a name="p1555373117469"></a><a name="p1555373117469"></a>Specifies the name of the host accommodating an ECS.</p>
<p id="p144362417139"><a name="p144362417139"></a><a name="p144362417139"></a>To remove the suffix <strong id="b202427275"><a name="b202427275"></a><a name="b202427275"></a>.novalocal</strong> from an ECS, see:</p>
<p id="p139015188431"><a name="p139015188431"></a><a name="p139015188431"></a><a href="is-an-ecs-hostname-with-suffix-novalocal-normal.md">Is an ECS Hostname with Suffix .novalocal Normal?</a></p>
</td>
</tr>
<tr id="row162411232141311"><td class="cellrowborder" valign="top" width="24.959999999999997%" headers="mcps1.2.4.1.1 "><p id="p924253261317"><a name="p924253261317"></a><a name="p924253261317"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p152427325137"><a name="p152427325137"></a><a name="p152427325137"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.690000000000005%" headers="mcps1.2.4.1.3 "><p id="p6242103211134"><a name="p6242103211134"></a><a name="p6242103211134"></a>Specifies the ID of the VPC for an ECS.</p>
</td>
</tr>
</tbody>
</table>

The following describes the URI and methods of using the supported ECS metadata.

## Prerequisites<a name="section36703712181817"></a>

-   The target ECS has been logged in.
-   Security group rules in the outbound direction meet the following requirements:

    -   **Protocol**:  **TCP**
    -   **Port Range**:  **80**
    -   **Remote End**:  **169.254.0.0/16**

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If you use the default security group rules in the outbound direction, the preceding requirements are met, and the metadata can be accessed. Default security group rules in the outbound direction are as follows:  
    >-   **Protocol**:  **ANY**  
    >-   **Port Range**:  **ANY**  
    >-   **Remote End**:  **0.0.0.0/0**  


## Metadata \(OpenStack Metadata API\)<a name="section29573104171554"></a>

Displays ECS metadata.

-   URI

    /169.254.169.254/openstack/latest/meta\_data.json

-   Usage method

    Supports GET requests.

-   Example

    The following section describes how to use the tool cURL to view ECS metadata.

    **curl http://169.254.169.254/openstack/latest/meta\_data.json**

    ```
    {
        "random_seed": "rEocCViRS+dNwlYdGIxJHUp+00poeUsAdBFkbPbYQTmpNwpoEb43k9z+96TyrekNKS+iLYDdRNy4kKGoNPEVBCc05Hg1TcDblAPfJwgJS1okqEtlcofUhKmL3K0fto+5KXEDU3GNuGwyZXjdVb9HQWU+E1jztAJjjqsahnU+g/tawABTVySLBKlAT8fMGax1mTGgArucn/WzDcy19DGioKPE7F8ILtSQ4Ww3VClK5VYB/h0x+4r7IVHrPmYX/bi1Yhm3Dc4rRYNaTjdOV5gUOsbO3oAeQkmKwQ/NO0N8qw5Ya4l8ZUW4tMav4mOsRySOOB35v0bvaJc6p+50DTbWNeX5A2MLiEhTP3vsPrmvk4LRF7CLz2J2TGIM14OoVBw7LARwmv9cz532zHki/c8tlhRzLmOTXh/wL36zFW10DeuReUGmxth7IGNmRMQKV6+miI78jm/KMPpgAdK3vwYF/GcelOFJD2HghMUUCeMbwYnvijLTejuBpwhJMNiHA/NvlEsxJDxqBCoss/Jfe+yCmUFyxovJ+L8oNkTzkmtCNzw3Ra0hiKchGhqK3BIeToV/kVx5DdF081xrEA+qyoM6CVyfJtEoz1zlRRyoo9bJ65Eg6JJd8dj1UCVsDqRY1pIjgzE/Mzsw6AaaCVhaMJL7u7YMVdyKzA6z65Xtvujz0Vo=",
        "uuid": "ca9e8b7c-f2be-4b6d-a639-f10b4d994d04",
        "availability_zone": "lt-test-1c",
        "hostname": "ecs-ddd4-l00349281.novalocal",
        "launch_index": 0,
        "meta": {
            "metering.image_id": "3a64bd37-955e-40cd-ab9e-129db56bc05d",
            "metering.imagetype": "gold",
            "metering.resourcespeccode": "s3.medium.1.linux",
            "image_name": "CentOS 7.6 64bit",
            "os_bit": "64",
            "vpc_id": "3b6c201f-aeb3-4bce-b841-64756e66cb49",
            "metering.resourcetype": "1",
            "cascaded.instance_extrainfo": "pcibridge:2",
            "os_type": "Linux",
            "charging_mode": "0"
        },
        "project_id": "6e8b0c94265645f39c5abbe63c4113c6",
        "name": "ecs-ddd4-l00349281"
    }
    ```


## User Data \(OpenStack Metadata API\)<a name="section51339028173755"></a>

Displays ECS user data. The value is configured only when you create an ECS. It cannot be changed after the configuration.

-   URI

    /169.254.169.254/openstack/latest/user\_data

-   Usage method

    Supports GET requests.

-   Example

    **curl http://169.254.169.254/openstack/latest/user\_data**

    ```
    ICAgICAgDQoiQSBjbG91ZCBkb2VzIG5vdCBrbm93IHdoeSBpdCBtb3ZlcyBpbiBqdXN0IHN1Y2ggYSBkaXJlY3Rpb24gYW5kIGF0IHN1Y2ggYSBzcGVlZC4uLkl0IGZlZWxzIGFuIGltcHVsc2lvbi4uLnRoaXMgaXMgdGhlIHBsYWNlIHRvIGdvIG5vdy4gQnV0IHRoZSBza3kga25vd3MgdGhlIHJlYXNvbnMgYW5kIHRoZSBwYXR0ZXJucyBiZWhpbmQgYWxsIGNsb3VkcywgYW5kIHlvdSB3aWxsIGtub3csIHRvbywgd2hlbiB5b3UgbGlmdCB5b3Vyc2VsZiBoaWdoIGVub3VnaCB0byBzZWUgYmV5b25kIGhvcml6b25zLiINCg0KLVJpY2hhcmQgQmFjaA==
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If user data was not injected during ECS creation, the query result is 404.  
    >**Figure  1**  404 Not Found<a name="fig4761957537"></a>    
    >![](figures/404-not-found.png "404-not-found")  


## Network Data \(OpenStack Metadata API\)<a name="section374011381441"></a>

Displays ECS network information.

-   URI

    /openstack/latest/network\_data.json

-   Usage method

    Supports GET requests.

-   Example

    **curl http://169.254.169.254/openstack/**latest**/network\_data.json**

    ```
    {
        "services": [{
            "type": "dns",
            "address": "xxx.xx.x.x"
        },
        {
            "type": "dns",
            "address": "100.1
    25.21.250"
        }],
        "networks": [{
            "network_id": "67dc10ce-441f-4592-9a80-cc709f6436e7",
            "type": "i
    pv4_dhcp",
            "link": "tap68a9272d-71",
            "id": "network0"
        }],
        "links": [{
            "type": "cascading",
            "vi
    f_id": "68a9272d-7152-4ae7-a138-3ef53af669e7",
            "ethernet_mac_address": "fa:16:3e:f7:c1:47",
            "id": "tap68a9272d-71",
            "mtu": null
        }]
    }
    ```


## Security Key \(OpenStack Metadata API\)<a name="section921029416614"></a>

Obtains temporary AKs and SKs.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   Before enabling an ECS to obtain a temporary AK and SK, make sure that the  **op\_svc\_ecs**  account has been authorized on IAM and that the desired ECS resources have been authorized for management.  
>-   The validity period of a temporary AK and SK is one hour. The temporary AK and SK are updated 10 minutes ahead of the expiration time. During the 10 minutes, both the new and old temporary AKs and SKs can be used.  
>-   When using temporary AKs and SKs, add  **'X-Security-Token':\{securitytoken\}**  in the message header.  **securitytoken**  is the value returned when a call is made to the API.  

-   URI

    /openstack/latest/securitykey

-   Usage method

    Supports GET requests.

-   Examples

    **curl http://169.254.169.254/openstack/**latest**/securitykey**


## User Data \(EC2 Compatible API\)<a name="section1526795182322"></a>

Displays ECS user data. The value is configured only when you create an ECS. It cannot be changed after the configuration.

-   URI

    /169.254.169.254/latest/user-data

-   Usage method

    Supports GET requests.

-   Example

    **curl http://169.254.169.254/latest/user-data**

    ```
    ICAgICAgDQoiQSBjbG91ZCBkb2VzIG5vdCBrbm93IHdoeSBpdCBtb3ZlcyBpbiBqdXN0IHN1Y2ggYSBkaXJlY3Rpb24gYW5kIGF0IHN1Y2ggYSBzcGVlZC4uLkl0IGZlZWxzIGFuIGltcHVsc2lvbi4uLnRoaXMgaXMgdGhlIHBsYWNlIHRvIGdvIG5vdy4gQnV0IHRoZSBza3kga25vd3MgdGhlIHJlYXNvbnMgYW5kIHRoZSBwYXR0ZXJucyBiZWhpbmQgYWxsIGNsb3VkcywgYW5kIHlvdSB3aWxsIGtub3csIHRvbywgd2hlbiB5b3UgbGlmdCB5b3Vyc2VsZiBoaWdoIGVub3VnaCB0byBzZWUgYmV5b25kIGhvcml6b25zLiINCg0KLVJpY2hhcmQgQmFjaA==
    ```


## Hostname \(EC2 Compatible API\)<a name="section370431618033"></a>

Displays the name of the host accommodating an ECS. The .novalocal suffix will be added later.

-   URI

    /169.254.169.254/latest/meta-data/hostname

-   Usage method

    Supports GET requests.

-   Example

    **curl http://169.254.169.254/latest/meta-data/hostname**

    ```
    vm-test.novalocal
    ```


## Instance Type \(EC2 Compatible API\)<a name="section5678065318623"></a>

Displays an ECS flavor.

-   URI

    /169.254.169.254/latest/meta-data/instance-type

-   Usage method

    Supports GET requests.

-   Example

    **curl http://169.254.169.254/latest/meta-data/instance-type**

    ```
    s3.medium.1
    ```


## Local IPv4 \(EC2 Compatible API\)<a name="section3229992918750"></a>

Displays the fixed IP address of an ECS. If there are multiple NICs, only the IP address of the primary NIC is displayed.

-   URI

    /169.254.169.254/latest/meta-data/local-ipv4

-   Usage method

    Supports GET requests.

-   Example

    **curl http://169.254.169.254/latest/meta-data/local-ipv4**

    ```
    192.1.1.2
    ```


## Availability Zone \(EC2 Compatible API\)<a name="section4087782618925"></a>

Displays the AZ accommodating an ECS.

-   URI

    /169.254.169.254/latest/meta-data/placement/availability-zone

-   Usage method

    Supports GET requests.

-   Example

    **curl http://169.254.169.254/latest/meta-data/placement/availability-zone**

    ```
    az1.dc1
    ```


## Public IPv4 \(EC2 Compatible API\)<a name="section5999198518129"></a>

Displays the floating IP address of an ECS. If there are multiple NICs, only the EIP of the primary NIC is displayed.

-   URI

    /169.254.169.254/latest/meta-data/public-ipv4

-   Usage method

    Supports GET requests.

-   Example

    **curl http://169.254.169.254/latest/meta-data/public-ipv4**

    ```
    46.1.1.2
    ```


## Public Keys \(EC2 Compatible API\)<a name="section51581190181532"></a>

Displays the public key of an ECS.

-   URI

    /169.254.169.254/latest/meta-data/public-keys/0/openssh-key

-   Usage method

    Supports GET requests.

-   Example

    **curl http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key**

    ```
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDI5Fw5k8Fgzajn1zJwLoV3+wMP+6CyvsSiIc/hioggSnYu/AD0Yqm8vVO0kWlun1rFbdO+QUZKyVr/OPUjQSw4SRh4qsTKf/+eFoWTjplFvd1WCBZzS/WRenxIwR00KkczHSJro763+wYcwKieb4eKRxaQoQvoFgVjLBULXAjH4eKoKTVNtMXAvPP9aMy2SLgsJNtMb9ArfziAiblQynq7UIfLnN3VclzPeiWrqtzjyOp6CPUXnL0lVPTvbLe8sUteBsJZwlL6K4i+Y0lf3ryqnmQgC21yW4Dzu+kwk8FVT2MgWkCwiZd8gQ/+uJzrJFyMfUOBIklOBfuUENIJUhAB Generated-by-Nova
    ```


