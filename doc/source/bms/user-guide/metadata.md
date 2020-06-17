# Metadata<a name="EN-US_TOPIC_0096279463"></a>

## Introduction<a name="section39791057141010"></a>

The BMS metadata includes BMS basic information on the cloud platform, such as the BMS ID, hostname, and network information. The BMS metadata can be obtained using compatible OpenStack and EC2 APIs listed in  [Table 1](#en-us_topic_0042400609_table273552371680).

**Table  1**  BMS metadata types

<a name="en-us_topic_0042400609_table273552371680"></a>
<table><thead align="left"><tr id="en-us_topic_0042400609_row459785021680"><th class="cellrowborder" valign="top" width="19.05%" id="mcps1.2.4.1.1"><p id="en-us_topic_0042400609_p1611763716833"><a name="en-us_topic_0042400609_p1611763716833"></a><a name="en-us_topic_0042400609_p1611763716833"></a>Metadata Type</p>
</th>
<th class="cellrowborder" valign="top" width="26.6%" id="mcps1.2.4.1.2"><p id="en-us_topic_0042400609_p304933271680"><a name="en-us_topic_0042400609_p304933271680"></a><a name="en-us_topic_0042400609_p304933271680"></a>Metadata Item</p>
</th>
<th class="cellrowborder" valign="top" width="54.35%" id="mcps1.2.4.1.3"><p id="en-us_topic_0042400609_p213207321680"><a name="en-us_topic_0042400609_p213207321680"></a><a name="en-us_topic_0042400609_p213207321680"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0042400609_row378821081680"><td class="cellrowborder" rowspan="5" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042400609_p809695916822"><a name="en-us_topic_0042400609_p809695916822"></a><a name="en-us_topic_0042400609_p809695916822"></a>OpenStack type</p>
</td>
<td class="cellrowborder" valign="top" width="26.6%" headers="mcps1.2.4.1.2 "><p id="p175787921680"><a name="p175787921680"></a><a name="p175787921680"></a>/meta_data.json</p>
</td>
<td class="cellrowborder" valign="top" width="54.35%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042400609_p426193551680"><a name="en-us_topic_0042400609_p426193551680"></a><a name="en-us_topic_0042400609_p426193551680"></a>This interface is used to query BMS metadata.</p>
<p id="p1530225016365"><a name="p1530225016365"></a><a name="p1530225016365"></a>For the key fields in the BMS metadata, see <a href="#table2373623012315">Table 2</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0042400609_row292374981680"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p163874991680"><a name="p163874991680"></a><a name="p163874991680"></a>/password</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042400609_p409248351680"><a name="en-us_topic_0042400609_p409248351680"></a><a name="en-us_topic_0042400609_p409248351680"></a>This interface is used to query the BMS password.</p>
<p id="p9343133813384"><a name="p9343133813384"></a><a name="p9343133813384"></a>If a key pair is selected during the creation of a Windows BMS, Cloudbase-Init is used to save the ciphertext password when the BMS is initialized.</p>
</td>
</tr>
<tr id="en-us_topic_0042400609_row104562411680"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p11850321680"><a name="p11850321680"></a><a name="p11850321680"></a>/user_data</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042400609_p98983401680"><a name="en-us_topic_0042400609_p98983401680"></a><a name="en-us_topic_0042400609_p98983401680"></a>This interface is used to query BMS user data.</p>
<p id="p3818124617428"><a name="p3818124617428"></a><a name="p3818124617428"></a>This metadata allows you to specify scripts and configuration files for initializing BMSs. For details, see <a href="injecting-user-data-into-bmss.md">Injecting User Data into BMSs</a>.</p>
<p id="p212122444313"><a name="p212122444313"></a><a name="p212122444313"></a>For password-authenticated Linux BMSs, save the password injection script.</p>
</td>
</tr>
<tr id="en-us_topic_0042400609_row216681141680"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p21457114512"><a name="p21457114512"></a><a name="p21457114512"></a>/network_data.json</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042400609_p532334241680"><a name="en-us_topic_0042400609_p532334241680"></a><a name="en-us_topic_0042400609_p532334241680"></a>This interface is used to query network information of BMSs.</p>
</td>
</tr>
<tr id="en-us_topic_0042400609_row19335028144551"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p714571205111"><a name="p714571205111"></a><a name="p714571205111"></a>/securitykey</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042400609_p58093494144551"><a name="en-us_topic_0042400609_p58093494144551"></a><a name="en-us_topic_0042400609_p58093494144551"></a>This interface is used to obtain temporary AKs and SKs.</p>
<p id="p579241610263"><a name="p579241610263"></a><a name="p579241610263"></a>Before obtaining a temporary AK and SK on a BMS, ensure that the <strong id="b84235270615356"><a name="b84235270615356"></a><a name="b84235270615356"></a>op_svc_ecs</strong> account has been authorized on IAM and that the desired BMS resources have been authorized for management.</p>
</td>
</tr>
<tr id="en-us_topic_0042400609_row16772135161746"><td class="cellrowborder" rowspan="8" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042400609_p4373564516822"><a name="en-us_topic_0042400609_p4373564516822"></a><a name="en-us_topic_0042400609_p4373564516822"></a>EC2 type</p>
</td>
<td class="cellrowborder" valign="top" width="26.6%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042400609_p10396761161746"><a name="en-us_topic_0042400609_p10396761161746"></a><a name="en-us_topic_0042400609_p10396761161746"></a>/meta-data/hostname</p>
</td>
<td class="cellrowborder" valign="top" width="54.35%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042400609_p45518664161746"><a name="en-us_topic_0042400609_p45518664161746"></a><a name="en-us_topic_0042400609_p45518664161746"></a>This interface is used to query the host name of a BMS.</p>
<p id="p1687574395116"><a name="p1687574395116"></a><a name="p1687574395116"></a>To remove the suffix <strong id="b842352706145759"><a name="b842352706145759"></a><a name="b842352706145759"></a>.novalocal</strong> from a BMS, see:</p>
<p id="p1146185614517"><a name="p1146185614517"></a><a name="p1146185614517"></a><a href="is-the-bms-host-name-with-suffix-novalocal-normal.md">Is the BMS Host Name with Suffix novalocal Normal?</a></p>
</td>
</tr>
<tr id="en-us_topic_0042400609_row35033331161746"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042400609_p24758917161746"><a name="en-us_topic_0042400609_p24758917161746"></a><a name="en-us_topic_0042400609_p24758917161746"></a>/meta-data/instance-type</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042400609_p21785021161746"><a name="en-us_topic_0042400609_p21785021161746"></a><a name="en-us_topic_0042400609_p21785021161746"></a>This interface is used to query the flavor name of a BMS.</p>
</td>
</tr>
<tr id="en-us_topic_0042400609_row25345840161746"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042400609_p38423929161746"><a name="en-us_topic_0042400609_p38423929161746"></a><a name="en-us_topic_0042400609_p38423929161746"></a>/meta-data/local-ipv4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042400609_p15298182161746"><a name="en-us_topic_0042400609_p15298182161746"></a><a name="en-us_topic_0042400609_p15298182161746"></a>This interface is used to query the fixed IP address of a BMS.</p>
<p id="p20873155615618"><a name="p20873155615618"></a><a name="p20873155615618"></a>If there are multiple NICs, only the IP address of the primary NIC is displayed.</p>
</td>
</tr>
<tr id="en-us_topic_0042400609_row898531716190"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042400609_p2079227616190"><a name="en-us_topic_0042400609_p2079227616190"></a><a name="en-us_topic_0042400609_p2079227616190"></a>/meta-data/placement/availability-zone</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042400609_p1219338216190"><a name="en-us_topic_0042400609_p1219338216190"></a><a name="en-us_topic_0042400609_p1219338216190"></a>This interface is used to query AZ information about a BMS.</p>
</td>
</tr>
<tr id="en-us_topic_0042400609_row1017501716190"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042400609_p631251216190"><a name="en-us_topic_0042400609_p631251216190"></a><a name="en-us_topic_0042400609_p631251216190"></a>/meta-data/public-ipv4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042400609_p308179816190"><a name="en-us_topic_0042400609_p308179816190"></a><a name="en-us_topic_0042400609_p308179816190"></a>This interface is used to query the EIP of a BMS.</p>
<p id="p116419213584"><a name="p116419213584"></a><a name="p116419213584"></a>If there are multiple NICs, only the EIP of the primary NIC is displayed.</p>
</td>
</tr>
<tr id="en-us_topic_0042400609_row6185333416190"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042400609_p2656422816190"><a name="en-us_topic_0042400609_p2656422816190"></a><a name="en-us_topic_0042400609_p2656422816190"></a>/meta-data/public-keys/0/openssh-key</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042400609_p2942083216190"><a name="en-us_topic_0042400609_p2942083216190"></a><a name="en-us_topic_0042400609_p2942083216190"></a>This interface is used to query the public key of a BMS.</p>
</td>
</tr>
<tr id="en-us_topic_0042400609_row2268075016190"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042400609_p4362812316190"><a name="en-us_topic_0042400609_p4362812316190"></a><a name="en-us_topic_0042400609_p4362812316190"></a>/user-data</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042400609_p5919884816190"><a name="en-us_topic_0042400609_p5919884816190"></a><a name="en-us_topic_0042400609_p5919884816190"></a>This interface is used to query the BMS user data.</p>
</td>
</tr>
<tr id="row206310763810"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p26229140161746"><a name="p26229140161746"></a><a name="p26229140161746"></a>/meta-data/security-groups</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p30692537161746"><a name="p30692537161746"></a><a name="p30692537161746"></a>This interface is used to query the name of the security group of the BMS.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Metadata key fields

<a name="table2373623012315"></a>
<table><thead align="left"><tr id="row4787810512315"><th class="cellrowborder" valign="top" width="19.1%" id="mcps1.2.4.1.1"><p id="p135337462439"><a name="p135337462439"></a><a name="p135337462439"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="26.21%" id="mcps1.2.4.1.2"><p id="p2054974617431"><a name="p2054974617431"></a><a name="p2054974617431"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.690000000000005%" id="mcps1.2.4.1.3"><p id="p75495461436"><a name="p75495461436"></a><a name="p75495461436"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1717815342412"><td class="cellrowborder" valign="top" width="19.1%" headers="mcps1.2.4.1.1 "><p id="p91796345418"><a name="p91796345418"></a><a name="p91796345418"></a>uuid</p>
</td>
<td class="cellrowborder" valign="top" width="26.21%" headers="mcps1.2.4.1.2 "><p id="p1438181511138"><a name="p1438181511138"></a><a name="p1438181511138"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.690000000000005%" headers="mcps1.2.4.1.3 "><p id="p138151561316"><a name="p138151561316"></a><a name="p138151561316"></a>Specifies the BMS ID.</p>
</td>
</tr>
<tr id="row7197172751211"><td class="cellrowborder" valign="top" width="19.1%" headers="mcps1.2.4.1.1 "><p id="p171982279122"><a name="p171982279122"></a><a name="p171982279122"></a>availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="26.21%" headers="mcps1.2.4.1.2 "><p id="p131981527161214"><a name="p131981527161214"></a><a name="p131981527161214"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.690000000000005%" headers="mcps1.2.4.1.3 "><p id="p819818276124"><a name="p819818276124"></a><a name="p819818276124"></a>Specifies the AZ where the BMS is located.</p>
</td>
</tr>
<tr id="row1961315241786"><td class="cellrowborder" valign="top" width="19.1%" headers="mcps1.2.4.1.1 "><p id="p156131424089"><a name="p156131424089"></a><a name="p156131424089"></a>meta</p>
</td>
<td class="cellrowborder" valign="top" width="26.21%" headers="mcps1.2.4.1.2 "><p id="p66147241387"><a name="p66147241387"></a><a name="p66147241387"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="54.690000000000005%" headers="mcps1.2.4.1.3 "><p id="p11614124384"><a name="p11614124384"></a><a name="p11614124384"></a>Specifies the metadata information, including the image name, image ID, and VPC ID.</p>
</td>
</tr>
<tr id="row4117204012123"><td class="cellrowborder" valign="top" width="19.1%" headers="mcps1.2.4.1.1 "><p id="p8117040181218"><a name="p8117040181218"></a><a name="p8117040181218"></a>hostname</p>
</td>
<td class="cellrowborder" valign="top" width="26.21%" headers="mcps1.2.4.1.2 "><p id="p51174405125"><a name="p51174405125"></a><a name="p51174405125"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.690000000000005%" headers="mcps1.2.4.1.3 "><p id="p1555373117469"><a name="p1555373117469"></a><a name="p1555373117469"></a>Specifies the hostname of the BMS.</p>
<p id="p144362417139"><a name="p144362417139"></a><a name="p144362417139"></a>To remove the suffix <strong id="b779421105114"><a name="b779421105114"></a><a name="b779421105114"></a>.novalocal</strong> from a BMS, see:</p>
<p id="p18161134820255"><a name="p18161134820255"></a><a name="p18161134820255"></a><a href="is-the-bms-host-name-with-suffix-novalocal-normal.md">Is the BMS Host Name with Suffix novalocal Normal?</a></p>
</td>
</tr>
<tr id="row162411232141311"><td class="cellrowborder" valign="top" width="19.1%" headers="mcps1.2.4.1.1 "><p id="p924253261317"><a name="p924253261317"></a><a name="p924253261317"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.21%" headers="mcps1.2.4.1.2 "><p id="p152427325137"><a name="p152427325137"></a><a name="p152427325137"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.690000000000005%" headers="mcps1.2.4.1.3 "><p id="p6242103211134"><a name="p6242103211134"></a><a name="p6242103211134"></a>Specifies the ID of the VPC where the BMS is located.</p>
</td>
</tr>
</tbody>
</table>

The following describes the URI and methods of using the supported BMS metadata.

## Prerequisites<a name="en-us_topic_0042400609_section36703712181817"></a>

-   You have logged in to the BMS.
-   Security group rules in the outbound direction meet the following requirements:

    -   Protocol: TCP
    -   Port Range: 80
    -   Remote End: 169.254.0.0/16

    >![](/images/icon-note.gif) **NOTE:**   
    >If you use the default security group rules in the outbound direction, the preceding requirements are met, and the metadata can be accessed. The default outbound security group rule is as follows:  
    >-   Protocol: Any  
    >-   Port Range: Any  
    >-   Remote End: 0.0.0.0/16  


## Metadata \(OpenStack Metadata API\)<a name="en-us_topic_0042400609_section29573104171554"></a>

This interface is used to query BMS metadata.

-   URI

    /169.254.169.254/openstack/latest/meta\_data.json

-   Method

    Supports GET requests.

-   Example

    The following describes how to use the cURL tool to query the BMS metadata:

    **curl** **http://169.254.169.254/openstack/latest/meta\_data.json**

    ```
    {
        "random_seed": "rEocCViRS+dNwlYdGIxJHUp+00poeUsAdBFkbPbYQTmpNwpoEb43k9z+96TyrekNKS+iLYDdRNy4kKGoNPEVBCc05Hg1TcDblAPfJwgJS1okqEtlcofUhKmL3K0fto+5KXEDU3GNuGwyZXjdVb9HQWU+E1jztAJjjqsahnU+g/tawABTVySLBKlAT8fMGax1mTGgArucn/WzDcy19DGioKPE7F8ILtSQ4Ww3VClK5VYB/h0x+4r7IVHrPmYX/bi1Yhm3Dc4rRYNaTjdOV5gUOsbO3oAeQkmKwQ/NO0N8qw5Ya4l8ZUW4tMav4mOsRySOOB35v0bvaJc6p+50DTbWNeX5A2MLiEhTP3vsPrmvk4LRF7CLz2J2TGIM14OoVBw7LARwmv9cz532zHki/c8tlhRzLmOTXh/wL36zFW10DeuReUGmxth7IGNmRMQKV6+miI78jm/KMPpgAdK3vwYF/GcelOFJD2HghMUUCeMbwYnvijLTejuBpwhJMNiHA/NvlEsxJDxqBCoss/Jfe+yCmUFyxovJ+L8oNkTzkmtCNzw3Ra0hiKchGhqK3BIeToV/kVx5DdF081xrEA+qyoM6CVyfJtEoz1zlRRyoo9bJ65Eg6JJd8dj1UCVsDqRY1pIjgzE/Mzsw6AaaCVhaMJL7u7YMVdyKzA6z65Xtvujz0Vo=",
        "uuid": "ca9e8b7c-f2be-4b6d-a639-f10b4d994d04",
        "availability_zone": "lt-test-1c",
        "hostname": "bms-ddd4-l00349281.novalocal",
        "launch_index": 0,
        "meta": {
            "metering.image_id": "3a64bd37-955e-40cd-ab9e-129db56bc05d",
            "metering.imagetype": "gold",
            "metering.resourcespeccode": "physical.s3.small",
            "metering.cloudServiceType": "service.type.ec2",
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


## User Data \(OpenStack Metadata API\)<a name="en-us_topic_0042400609_section51339028173755"></a>

This interface is used to query BMS user data. The value is configured when you create a BMS. It cannot be changed after the configuration.

-   URI

    /169.254.169.254/openstack/latest/user\_data

-   Method

    Supports GET requests.

-   Example

    **curl** **http://169.254.169.254/openstack/latest/user\_data**

    ```
    ICAgICAgDQoiQSBjbG91ZCBkb2VzIG5vdCBrbm93IHdoeSBpdCBtb3ZlcyBpbiBqdXN0IHN1Y2ggYSBkaXJlY3Rpb24gYW5kIGF0IHN1Y2ggYSBzcGVlZC4uLkl0IGZlZWxzIGFuIGltcHVsc2lvbi4uLnRoaXMgaXMgdGhlIHBsYWNlIHRvIGdvIG5vdy4gQnV0IHRoZSBza3kga25vd3MgdGhlIHJlYXNvbnMgYW5kIHRoZSBwYXR0ZXJucyBiZWhpbmQgYWxsIGNsb3VkcywgYW5kIHlvdSB3aWxsIGtub3csIHRvbywgd2hlbiB5b3UgbGlmdCB5b3Vyc2VsZiBoaWdoIGVub3VnaCB0byBzZWUgYmV5b25kIGhvcml6b25zLiINCg0KLVJpY2hhcmQgQmFjaA==
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >If user data is not injected during BMS creation, the query result is 404.  
    >**Figure  1**  404 Not Found<a name="fig748134111137"></a>    
    >![](figures/404-not-found.png "404-not-found")  


## Network Data \(OpenStack Metadata API\)<a name="section374011381441"></a>

This interface is used to query network information of a BMS.

-   URI

    /openstack/latest/network\_data.json

-   Method

    Supports GET requests.

-   Example

    **curl** **http://169.254.169.254/openstack/**latest**/network\_data.json**

    ```
    {
        "services": [{
            "type": "dns",
            "address": "100.125.1.250"
        },
        {
            "type": "dns",
            "address": "100.125.21.250"
        }],
        "networks": [{
            "network_id": "67dc10ce-441f-4592-9a80-cc709f6436e7",
            "type": "ipv4_dhcp",
            "link": "tap68a9272d-71",
            "id": "network0"
        }],
        "links": [{
            "type": "cascading",
            "vif_id": "68a9272d-7152-4ae7-a138-3ef53af669e7",
            "ethernet_mac_address": "fa:16:3e:f7:c1:47",
            "id": "tap68a9272d-71",
            "mtu": null
        }]
    }
    ```


## Security Key \(OpenStack Metadata API\)<a name="en-us_topic_0042400609_section921029416614"></a>

This interface is used to obtain temporary AKs and SKs.

>![](/images/icon-note.gif) **NOTE:**   
>-   To obtain a temporary AK and SK on a BMS, ensure that the  **op\_svc\_ecs**  account has been authorized on IAM and that the desired BMS resources have been authorized for management.  
>-   Temporary AKs and SKs expire an hour later.  
>-   When using temporary AKs and SKs, add  **'X-Security-Token':securitytoken**  in the message header.  **securitytoken**  is the value returned when a call is made to the API.  

-   URI

    /openstack/latest/securitykey

-   Method

    Supports GET requests.

-   Example

    **curl** **http://169.254.169.254/openstack/latest/securitykey**


## User Data \(EC2 Compatible API\)<a name="en-us_topic_0042400609_section1526795182322"></a>

This interface is used to query BMS user data. The value is configured when you create a BMS. It cannot be changed after the configuration.

-   URI

    /169.254.169.254/latest/user-data

-   Method

    Supports GET requests.

-   Example

    **curl** **http://169.254.169.254/latest/user-data**

    ```
    ICAgICAgDQoiQSBjbG91ZCBkb2VzIG5vdCBrbm93IHdoeSBpdCBtb3ZlcyBpbiBqdXN0IHN1Y2ggYSBkaXJlY3Rpb24gYW5kIGF0IHN1Y2ggYSBzcGVlZC4uLkl0IGZlZWxzIGFuIGltcHVsc2lvbi4uLnRoaXMgaXMgdGhlIHBsYWNlIHRvIGdvIG5vdy4gQnV0IHRoZSBza3kga25vd3MgdGhlIHJlYXNvbnMgYW5kIHRoZSBwYXR0ZXJucyBiZWhpbmQgYWxsIGNsb3VkcywgYW5kIHlvdSB3aWxsIGtub3csIHRvbywgd2hlbiB5b3UgbGlmdCB5b3Vyc2VsZiBoaWdoIGVub3VnaCB0byBzZWUgYmV5b25kIGhvcml6b25zLiINCg0KLVJpY2hhcmQgQmFjaA==
    ```


## Hostname \(EC2 Compatible API\)<a name="en-us_topic_0042400609_section370431618033"></a>

This interface is used to query the name of the host accommodating a BMS. The  **.novalocal**  suffix will be added later.

-   URI

    /169.254.169.254/latest/meta-data/hostname

-   Method

    Supports GET requests.

-   Example

    **curl** **http://169.254.169.254/latest/meta-data/hostname**

    ```
    bms-test.novalocal
    ```


## Instance Type \(EC2 Compatible API\)<a name="en-us_topic_0042400609_section5678065318623"></a>

This interface is used to query the flavor name of a BMS.

-   URI

    /169.254.169.254/latest/meta-data/instance-type

-   Method

    Supports GET requests.

-   Example

    **curl** **http://169.254.169.254/latest/meta-data/instance-type**

    ```
    physical.o2.medium
    ```


## Local IPv4 \(EC2 Compatible API\)<a name="en-us_topic_0042400609_section3229992918750"></a>

This interface is used to query the fixed IP address of a BMS. If there are multiple NICs, only the IP address of the primary NIC is displayed.

-   URI

    /169.254.169.254/latest/meta-data/local-ipv4

-   Method

    Supports GET requests.

-   Example

    **curl** **http://169.254.169.254/latest/meta-data/local-ipv4**

    ```
    192.1.1.2
    ```


## Availability Zone \(EC2 Compatible API\)<a name="en-us_topic_0042400609_section4087782618925"></a>

This interface is used to query AZ information about a BMS.

-   URI

    /169.254.169.254/latest/meta-data/placement/availability-zone

-   Method

    Supports GET requests.

-   Example

    **curl** **http://169.254.169.254/latest/meta-data/placement/availability-zone**

    ```
    az1.dc1
    ```


## Public IPv4 \(EC2 Compatible API\)<a name="en-us_topic_0042400609_section5999198518129"></a>

This interface is used to query the EIP of a BMS. If there are multiple NICs, only the EIP of the primary NIC is displayed.

-   URI

    /169.254.169.254/latest/meta-data/public-ipv4

-   Method

    Supports GET requests.

-   Example

    **curl** **http://169.254.169.254/latest/meta-data/public-ipv4**

    ```
    46.1.1.2
    ```


## Public Keys \(EC2 Compatible API\)<a name="en-us_topic_0042400609_section51581190181532"></a>

This interface is used to query the public key of a BMS.

-   URI

    /169.254.169.254/latest/meta-data/public-keys/0/openssh-key

-   Method

    Supports GET requests.

-   Example

    **curl** **http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key**

    ```
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDI5Fw5k8Fgzajn1zJwLoV3+wMP+6CyvsSiIc/hioggSnYu/AD0Yqm8vVO0kWlun1rFbdO+QUZKyVr/OPUjQSw4SRh4qsTKf/+eFoWTjplFvd1WCBZzS/WRenxIwR00KkczHSJro763+wYcwKieb4eKRxaQoQvoFgVjLBULXAjH4eKoKTVNtMXAvPP9aMy2SLgsJNtMb9ArfziAiblQynq7UIfLnN3VclzPeiWrqtzjyOp6CPUXnL0lVPTvbLe8sUteBsJZwlL6K4i+Y0lf3ryqnmQgC21yW4Dzu+kwk8FVT2MgWkCwiZd8gQ/+uJzrJFyMfUOBIklOBfuUENIJUhAB Generated-by-Nova
    ```


