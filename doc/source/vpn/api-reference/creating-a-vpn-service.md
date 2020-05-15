# Creating a VPN Service<a name="en_topic_0093011498"></a>

## **Function**<a name="section34534866"></a>

This interface is used to create a VPN service.

>![](/images/icon-note.gif) **NOTE:**   
>Only one VPN service can be created for each VPC.  

## URI<a name="ole_link136"></a>

POST /v2.0/vpn/vpnservices

## Request Message<a name="section10093828"></a>

[Table 1](#table35351135)  describes the request parameters.

**Table  1**  Request parameters

<a name="table35351135"></a>
<table><thead align="left"><tr id="row50516929"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p65339469"><a name="p65339469"></a><a name="p65339469"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p58005670"><a name="p58005670"></a><a name="p58005670"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p838835"><a name="p838835"></a><a name="p838835"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p836829"><a name="p836829"></a><a name="p836829"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53242138"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p17645916"><a name="p17645916"></a><a name="p17645916"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p20033078"><a name="p20033078"></a><a name="p20033078"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p12066641"><a name="p12066641"></a><a name="p12066641"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p37873877"><a name="p37873877"></a><a name="p37873877"></a>Specifies the subnet ID.</p>
</td>
</tr>
<tr id="row5320573"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p28313264"><a name="p28313264"></a><a name="p28313264"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p11673056"><a name="p11673056"></a><a name="p11673056"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p5993460"><a name="p5993460"></a><a name="p5993460"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p15708245"><a name="p15708245"></a><a name="p15708245"></a>Specifies the router ID.</p>
</td>
</tr>
<tr id="row7156477"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p42803771"><a name="p42803771"></a><a name="p42803771"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p44553466"><a name="p44553466"></a><a name="p44553466"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p52061026"><a name="p52061026"></a><a name="p52061026"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p56193562"><a name="p56193562"></a><a name="p56193562"></a>Specifies the VPN service name.</p>
</td>
</tr>
<tr id="row35980011"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p28699807"><a name="p28699807"></a><a name="p28699807"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p42983031"><a name="p42983031"></a><a name="p42983031"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p59073500"><a name="p59073500"></a><a name="p59073500"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p20224181"><a name="p20224181"></a><a name="p20224181"></a>Specifies the administrative status. The value can be <strong id="b842352706221557"><a name="b842352706221557"></a><a name="b842352706221557"></a>true</strong> or <strong id="b84235270622160"><a name="b84235270622160"></a><a name="b84235270622160"></a>false</strong>.</p>
</td>
</tr>
<tr id="row47799905"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p46587076"><a name="p46587076"></a><a name="p46587076"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p15456783"><a name="p15456783"></a><a name="p15456783"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p44039915"><a name="p44039915"></a><a name="p44039915"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p10463359"><a name="p10463359"></a><a name="p10463359"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row27061374"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p44487706"><a name="p44487706"></a><a name="p44487706"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p46734467"><a name="p46734467"></a><a name="p46734467"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p27395488"><a name="p27395488"></a><a name="p27395488"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p4442074"><a name="p4442074"></a><a name="p4442074"></a>Provides supplementary information about the VPN service.</p>
</td>
</tr>
<tr id="row39978669"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p17046748"><a name="p17046748"></a><a name="p17046748"></a>vpnservice</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p38609372"><a name="p38609372"></a><a name="p38609372"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p40351445"><a name="p40351445"></a><a name="p40351445"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p47241582"><a name="p47241582"></a><a name="p47241582"></a>Specifies the VPN service object.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>1.  The  **project\_id**  parameter is not supported.  
>2.  The value of  **tenant\_id**  can contain a maximum of 255 characters.  
>3.  The value of  **name**  can contain 1 to 64 characters.  
>4.  The value of  **description**  can contain a maximum of 255 characters.  
>5.  The value of  **router\_id**  must be the VPC router ID.  
>6.  The value of  **admin\_state\_up**  can only be  **true**.  
>7.  This interface cannot be used to create a VPN service in the active-active VPN scenarios.  
>8.  Bandwidth limiting is used by default. The recommended bandwidth is 300 Mbit/s. This interface cannot be used to change the bandwidth size.  
>9.  In standalone mode, only one VPC service can be created for each VPN. In active-active mode, two VPC services can be created for each VPN.  

## Response Message<a name="section23735588"></a>

[Table 2](#table1362895)  describes the response parameters.

**Table  2**  Response parameters

<a name="table1362895"></a>
<table><thead align="left"><tr id="row67057771"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p62970394"><a name="p62970394"></a><a name="p62970394"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p328285"><a name="p328285"></a><a name="p328285"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p6398145"><a name="p6398145"></a><a name="p6398145"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row48487730"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="_Hlk477539510"><a name="_Hlk477539510"></a><a name="_Hlk477539510"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p31981592"><a name="p31981592"></a><a name="p31981592"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p48922001"><a name="p48922001"></a><a name="p48922001"></a>Specifies the router ID.</p>
</td>
</tr>
<tr id="row37644831"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p29332447"><a name="p29332447"></a><a name="p29332447"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p27118016"><a name="p27118016"></a><a name="p27118016"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p15707907"><a name="p15707907"></a><a name="p15707907"></a>Specifies whether the VPN service is currently operational. The value can be <strong id="b842352706212822"><a name="b842352706212822"></a><a name="b842352706212822"></a>ACTIVE</strong>, <strong id="b842352706212827"><a name="b842352706212827"></a><a name="b842352706212827"></a>DOWN</strong>, <strong id="b842352706212832"><a name="b842352706212832"></a><a name="b842352706212832"></a>BUILD</strong>, <strong id="b842352706212835"><a name="b842352706212835"></a><a name="b842352706212835"></a>ERROR</strong>, <strong id="b842352706212840"><a name="b842352706212840"></a><a name="b842352706212840"></a>PENDING_CREATE</strong>, <strong id="b842352706212845"><a name="b842352706212845"></a><a name="b842352706212845"></a>PENDING_UPDATE</strong>, or <strong id="b842352706212850"><a name="b842352706212850"></a><a name="b842352706212850"></a>PENDING_DELETE</strong>.</p>
</td>
</tr>
<tr id="row7153442"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p42557928"><a name="p42557928"></a><a name="p42557928"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p24640114"><a name="p24640114"></a><a name="p24640114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p65645300"><a name="p65645300"></a><a name="p65645300"></a>Specifies the VPN service name.</p>
</td>
</tr>
<tr id="row53936788"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p6803737"><a name="p6803737"></a><a name="p6803737"></a>external_v6_ip</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p14231847"><a name="p14231847"></a><a name="p14231847"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p26719483"><a name="p26719483"></a><a name="p26719483"></a>Specifies the IPv6 address of the VPN service external gateway.</p>
</td>
</tr>
<tr id="row39148759"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p16932901"><a name="p16932901"></a><a name="p16932901"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p29387744"><a name="p29387744"></a><a name="p29387744"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p9223355"><a name="p9223355"></a><a name="p9223355"></a>Specifies the administrative status. The value can be <strong id="b832554619"><a name="b832554619"></a><a name="b832554619"></a>true</strong> or <strong id="b288746640"><a name="b288746640"></a><a name="b288746640"></a>false</strong>.</p>
</td>
</tr>
<tr id="row15901331"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p12939396"><a name="p12939396"></a><a name="p12939396"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p41458150"><a name="p41458150"></a><a name="p41458150"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p14698523"><a name="p14698523"></a><a name="p14698523"></a>Specifies the subnet ID.</p>
</td>
</tr>
<tr id="row65177848"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p44914359"><a name="p44914359"></a><a name="p44914359"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p14184458"><a name="p14184458"></a><a name="p14184458"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p51347342"><a name="p51347342"></a><a name="p51347342"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row59472897"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p52575367"><a name="p52575367"></a><a name="p52575367"></a>external_v4_ip</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p30746341"><a name="p30746341"></a><a name="p30746341"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p64613452"><a name="p64613452"></a><a name="p64613452"></a>Specifies the IPv4 address of the VPN service external gateway.</p>
</td>
</tr>
<tr id="row44650158"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p59893061"><a name="p59893061"></a><a name="p59893061"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p19499801"><a name="p19499801"></a><a name="p19499801"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p28702870"><a name="p28702870"></a><a name="p28702870"></a>Specifies the VPN service ID.</p>
</td>
</tr>
<tr id="row56999240"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p53535755"><a name="p53535755"></a><a name="p53535755"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p41428878"><a name="p41428878"></a><a name="p41428878"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p23970293"><a name="p23970293"></a><a name="p23970293"></a>Provides supplementary information about the VPN service.</p>
</td>
</tr>
<tr id="row14406049"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p26039288"><a name="p26039288"></a><a name="p26039288"></a>vpnservice</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p28807604"><a name="p28807604"></a><a name="p28807604"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p28134778"><a name="p28134778"></a><a name="p28134778"></a>Specifies the VPN service object.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section12293700"></a>

-   Example Request

    ```
    POST /v2.0/vpn/vpnservices
    {
        "vpnservice": {
            "subnet_id": null,
            "router_id": "66e3b16c-8ce5-40fb-bb49-ab6d8dc3f2aa",
            "name": "myservice",
            "admin_state_up": true
        }
    }
    ```


-   Example Response

    ```
    {
      "vpnservice" : {
        "router_id" : "66e3b16c-8ce5-40fb-bb49-ab6d8dc3f2aa",
        "status" : "PENDING_CREATE",
        "name" : "myservice",
        "external_v6_ip" : "2001:db8::1",
        "admin_state_up" : true,
        "subnet_id" : null,
        "project_id" : "10039663455a446d8ba2cbb058b0f578",
        "tenant_id" : "10039663455a446d8ba2cbb058b0f578",
        "external_v4_ip" : "172.32.1.11",
        "id" : "5c561d9d-eaea-45f6-ae3e-08d1a7080828",
        "description" : ""
      }
    }
    ```


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

