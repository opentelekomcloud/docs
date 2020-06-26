# Adding Share Access Rules<a name="sfs_02_0029"></a>

## Function<a name="sd0a393a25a894abdb12b4408b8535ae6"></a>

This API is used to add share access rules.

>![](/images/icon-note.gif) **NOTE:**   
>-   This API is an asynchronous API. If the returned status code is  **200**, the API request is successfully delivered and received. Later, you can refer to  [Querying Share Access Rules](querying-share-access-rules.md)  to check whether the share access rule is added successfully.  
>-   APIs whose microversions are from 2.28 to 2.42 can ignore error statuses of existing share access rules during rule adding. The microversions of APIs are specified by using the  **X-Openstack-Manila-Api-Version**  parameter in the request headers.  

## URI<a name="s9a383b99884f496a8c54f392b9cc85c1"></a>

-   POST  /v2/\{project\_id\}/shares/\{share\_id\}/action?vpc\_ip\_base\_acl=\{vpc\_ip\_base\_acl\}
-   Parameter description

    <a name="en-us_topic_0064390798_table42402339"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390798_row57367087"><th class="cellrowborder" valign="top" width="17.95179517951795%" id="mcps1.1.5.1.1"><p id="p17124101410431"><a name="p17124101410431"></a><a name="p17124101410431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.771477147714771%" id="mcps1.1.5.1.2"><p id="p1612415146430"><a name="p1612415146430"></a><a name="p1612415146430"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.931793179317932%" id="mcps1.1.5.1.3"><p id="p312416148432"><a name="p312416148432"></a><a name="p312416148432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.344934493449344%" id="mcps1.1.5.1.4"><p id="p3124181464318"><a name="p3124181464318"></a><a name="p3124181464318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390798_row24908514"><td class="cellrowborder" valign="top" width="17.95179517951795%" headers="mcps1.1.5.1.1 "><p id="a252f31af6a5941728f20b9ce4d913979"><a name="a252f31af6a5941728f20b9ce4d913979"></a><a name="a252f31af6a5941728f20b9ce4d913979"></a>share_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.771477147714771%" headers="mcps1.1.5.1.2 "><p id="ae7618cdcbab74270854c6a085c7fd459"><a name="ae7618cdcbab74270854c6a085c7fd459"></a><a name="ae7618cdcbab74270854c6a085c7fd459"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0064390798_p319635105113"><a name="en-us_topic_0064390798_p319635105113"></a><a name="en-us_topic_0064390798_p319635105113"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.344934493449344%" headers="mcps1.1.5.1.4 "><p id="a25e8c7cbf76742b3bb7c20ceab7cf039"><a name="a25e8c7cbf76742b3bb7c20ceab7cf039"></a><a name="a25e8c7cbf76742b3bb7c20ceab7cf039"></a>Specifies the UUID of the shared file system.</p>
    </td>
    </tr>
    <tr id="r7866797c60b8464cb268931e24b48673"><td class="cellrowborder" valign="top" width="17.95179517951795%" headers="mcps1.1.5.1.1 "><p id="ad6c63dbfe7fb42b8b9865d8c4c7449a0"><a name="ad6c63dbfe7fb42b8b9865d8c4c7449a0"></a><a name="ad6c63dbfe7fb42b8b9865d8c4c7449a0"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.771477147714771%" headers="mcps1.1.5.1.2 "><p id="a090b1d07c90c4afe8349081d7fe3ca56"><a name="a090b1d07c90c4afe8349081d7fe3ca56"></a><a name="a090b1d07c90c4afe8349081d7fe3ca56"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.1.5.1.3 "><p id="abf640452fc5e406bb823506eccfc3179"><a name="abf640452fc5e406bb823506eccfc3179"></a><a name="abf640452fc5e406bb823506eccfc3179"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.344934493449344%" headers="mcps1.1.5.1.4 "><p id="a6e5fab7f9bd34ef49b348c6248bad26a"><a name="a6e5fab7f9bd34ef49b348c6248bad26a"></a><a name="a6e5fab7f9bd34ef49b348c6248bad26a"></a>Specifies the project ID of the operator.</p>
    </td>
    </tr>
    <tr id="row1189816611118"><td class="cellrowborder" valign="top" width="17.95179517951795%" headers="mcps1.1.5.1.1 "><p id="p88981669112"><a name="p88981669112"></a><a name="p88981669112"></a>vpc_ip_base_acl</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.771477147714771%" headers="mcps1.1.5.1.2 "><p id="p198981363112"><a name="p198981363112"></a><a name="p198981363112"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.931793179317932%" headers="mcps1.1.5.1.3 "><p id="p108983610114"><a name="p108983610114"></a><a name="p108983610114"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.344934493449344%" headers="mcps1.1.5.1.4 "><p id="p2898166117"><a name="p2898166117"></a><a name="p2898166117"></a>Specifies the identifier of the IP address-based authorization scenario. Currently, only <strong id="b136621947101218"><a name="b136621947101218"></a><a name="b136621947101218"></a>enable</strong> is available. The value <strong id="b56105595121"><a name="b56105595121"></a><a name="b56105595121"></a>enable</strong> indicates creating a share access rule for the IP address-based authorization scenario.</p>
    <div class="notice" id="note14995413172620"><a name="note14995413172620"></a><a name="note14995413172620"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p699510137265"><a name="p699510137265"></a><a name="p699510137265"></a>To ensure compatibility, even though this parameter is left blank or set to another value other than <strong id="b104144441617"><a name="b104144441617"></a><a name="b104144441617"></a>enable</strong>, you can use the API to create a share access rule for the IP address-based authorization scenario. However, this method of creation has been discarded and will not be maintained in the future.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s1e8eb33120864ed0bca458fb8467230a"></a>

-   Parameter description

    <a name="en-us_topic_0064390798_table42069424"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390798_row20618333"><th class="cellrowborder" valign="top" width="18.3%" id="mcps1.1.5.1.1"><p id="p57416229519"><a name="p57416229519"></a><a name="p57416229519"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.280000000000001%" id="mcps1.1.5.1.2"><p id="p874118226518"><a name="p874118226518"></a><a name="p874118226518"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.21%" id="mcps1.1.5.1.3"><p id="p177560229518"><a name="p177560229518"></a><a name="p177560229518"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.21%" id="mcps1.1.5.1.4"><p id="p8756022155"><a name="p8756022155"></a><a name="p8756022155"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390798_row35228531"><td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0064390798_p34938791"><a name="en-us_topic_0064390798_p34938791"></a><a name="en-us_topic_0064390798_p34938791"></a>os-allow_access</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.280000000000001%" headers="mcps1.1.5.1.2 "><p id="a0ba098da87604be3a12c5273a1121964"><a name="a0ba098da87604be3a12c5273a1121964"></a><a name="a0ba098da87604be3a12c5273a1121964"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.21%" headers="mcps1.1.5.1.3 "><p id="a00590625860844f29165881530716e24"><a name="a00590625860844f29165881530716e24"></a><a name="a00590625860844f29165881530716e24"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.21%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0064390798_p18961705"><a name="en-us_topic_0064390798_p18961705"></a><a name="en-us_topic_0064390798_p18961705"></a>Specifies the <strong id="ac5180abeafc7432090f7875aff15b712"><a name="ac5180abeafc7432090f7875aff15b712"></a><a name="ac5180abeafc7432090f7875aff15b712"></a>os-allow_access</strong> object.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:**   
    >If the API version ranges from 1.0 to 2.6, the top-layer parameters of the request body in the JSON format use prefix  **os-**. If the API version is later than 2.6, prefix  **os-**  must be removed.   

-   Description of field  **os-allow\_access**

    <a name="en-us_topic_0064390798_table59503116"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390798_row48337798"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.5.1.1"><p id="p524019261656"><a name="p524019261656"></a><a name="p524019261656"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.2"><p id="p6240142617519"><a name="p6240142617519"></a><a name="p6240142617519"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.1.5.1.3"><p id="p1324013261958"><a name="p1324013261958"></a><a name="p1324013261958"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49%" id="mcps1.1.5.1.4"><p id="p1525613267514"><a name="p1525613267514"></a><a name="p1525613267514"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390798_row26390432"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="a3437c56c5227456fb764438beec6f25b"><a name="a3437c56c5227456fb764438beec6f25b"></a><a name="a3437c56c5227456fb764438beec6f25b"></a>access_level</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.2 "><p id="acf8d302961324bb1a12ccb3bac4f5485"><a name="acf8d302961324bb1a12ccb3bac4f5485"></a><a name="acf8d302961324bb1a12ccb3bac4f5485"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.3 "><p id="aaebea89349d540b1a923dd3f87944ea6"><a name="aaebea89349d540b1a923dd3f87944ea6"></a><a name="aaebea89349d540b1a923dd3f87944ea6"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="a0234596b7285480fb1486ced3829ac07"><a name="a0234596b7285480fb1486ced3829ac07"></a><a name="a0234596b7285480fb1486ced3829ac07"></a>Specifies the access level of the shared file system. Possible values are <strong id="b327976527114855"><a name="b327976527114855"></a><a name="b327976527114855"></a>ro</strong> (read-only) and <strong id="b360052986114855"><a name="b360052986114855"></a><a name="b360052986114855"></a>rw</strong> (read-write). The default value is <strong id="b45449543119"><a name="b45449543119"></a><a name="b45449543119"></a>rw</strong> (read/write).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row65794642"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="aa71a35f7d99544738468f17e9dd6687b"><a name="aa71a35f7d99544738468f17e9dd6687b"></a><a name="aa71a35f7d99544738468f17e9dd6687b"></a>access_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.2 "><p id="a7ad4ca3d82cb454dbf394967a67c9c46"><a name="a7ad4ca3d82cb454dbf394967a67c9c46"></a><a name="a7ad4ca3d82cb454dbf394967a67c9c46"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.3 "><p id="aaef3c98e802e444e825e62948c21143b"><a name="aaef3c98e802e444e825e62948c21143b"></a><a name="aaef3c98e802e444e825e62948c21143b"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="aa796fa0f9ddf4509a2a886e2bd83aa4e"><a name="aa796fa0f9ddf4509a2a886e2bd83aa4e"></a><a name="aa796fa0f9ddf4509a2a886e2bd83aa4e"></a>Specifies the type of the share access rule. The value can be <strong id="b455041345316"><a name="b455041345316"></a><a name="b455041345316"></a>NFS</strong> or <strong id="b14891135733115"><a name="b14891135733115"></a><a name="b14891135733115"></a>CIFS</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row22568466"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="ae33d6534cb064d12aa561d65ca431000"><a name="ae33d6534cb064d12aa561d65ca431000"></a><a name="ae33d6534cb064d12aa561d65ca431000"></a>access_to</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.2 "><p id="a85f81f9c83664dcb9f943be437e2d3cd"><a name="a85f81f9c83664dcb9f943be437e2d3cd"></a><a name="a85f81f9c83664dcb9f943be437e2d3cd"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.3 "><p id="adb9e962619a24fefa9f963178e240c1c"><a name="adb9e962619a24fefa9f963178e240c1c"></a><a name="adb9e962619a24fefa9f963178e240c1c"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="p815612772610"><a name="p815612772610"></a><a name="p815612772610"></a>Specifies the value that defines the access rule. The value contains 1 to 255 characters. The value varies according to the scenario: </p>
    <a name="ul8741726143110"></a><a name="ul8741726143110"></a><ul id="ul8741726143110"><li>Enter the VPC ID in VPC authorization scenarios. </li></ul>
    <a name="ul181581909274"></a><a name="ul181581909274"></a><ul id="ul181581909274"><li>Set this parameter in IP address authorization scenario.<a name="ul115546141057"></a><a name="ul115546141057"></a><ul id="ul115546141057"><li>Enter the value in the format of <em id="i9447112173212"><a name="i9447112173212"></a><a name="i9447112173212"></a>VPC ID</em>#<em id="i1044811215324"><a name="i1044811215324"></a><a name="i1044811215324"></a>IP address</em>#<em id="i1244992153216"><a name="i1244992153216"></a><a name="i1244992153216"></a>priority</em>#<em id="i17449621193210"><a name="i17449621193210"></a><a name="i17449621193210"></a>user permission</em> for an NFS shared file system, for example, <strong id="b34505210328"><a name="b34505210328"></a><a name="b34505210328"></a>0157b53f-4974-4e80-91c9-098532bcaf00#2.2.2.2/16#100#all_squash,root_squash</strong>.</li><li>For a CIFS shared file system, enter the value in the format of <em id="i172341153213"><a name="i172341153213"></a><a name="i172341153213"></a>VPC ID</em>#<em id="i1872511115328"><a name="i1872511115328"></a><a name="i1872511115328"></a>IP address</em>#<em id="i87255118325"><a name="i87255118325"></a><a name="i87255118325"></a>priority</em>. For example, <strong id="b29616491475"><a name="b29616491475"></a><a name="b29616491475"></a>0157b53f-4974-4e80-91c9-098532bcaf00#2.2.2.2/16#0</strong>.</li></ul>
    </li></ul>
    <div class="note" id="note64711718143510"><a name="note64711718143510"></a><a name="note64711718143510"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1247291883517"><a name="p1247291883517"></a><a name="p1247291883517"></a>Description of and restrictions on the VPC ID, IP address, priority, and user permission: </p>
    <a name="ul14824125361"></a><a name="ul14824125361"></a><ul id="ul14824125361"><li>VPC ID: ID of the VPC. </li><li>IP address: Tenant IPv4 address or address segment of the ECS's active network port. Each rule only supports one IPv4 address or address segment. The mask format is used to represent an address segment. For example, 192.168.1.0/24 represents the IP address segment of 192.168.1.0 to 192.168.1.255. Other address segment formats, such as 192.168.1.0-255, are not supported. The entered IPv4 address or address segment must be valid and cannot be an IP address or address segment starting with 0 except 0.0.0.0/0. The value <strong id="b2078014555475"><a name="b2078014555475"></a><a name="b2078014555475"></a>0.0.0.0/0</strong> indicates any IP address in the VPC. In addition, the IP address or address segment cannot start with 127 or 224 to 255, for example, 127.0.0.1, 224.0.0.1, or 255.255.255.255. This is because IP addresses or address segments starting with 224 to 239 are class D addresses and they are used for multicast. IP addresses or address segments starting with 240 to 255 are class E addresses and they are used for research. If an invalid IP address or address segment is used, the access rule may fail to be added or the added access rule cannot take effect.</li><li>Priority: Priority of a share access rule. It must be an integer ranging from 0 to 100. 0 indicates the highest priority, and 100 indicates the lowest priority. In the same VPC, the permission of the IP address or address segment with the highest priority is preferentially used. For example, if your IP address for mounting is 10.1.1.32, and the authorized 10.1.1.32 (read/write) and 10.1.1.0/24 (read-only) both meet the requirements, the permission of the IP address or segment with the higher priority is used first. If some IP addresses or address segments are of the same priority, one permission of them is randomly chosen. </li><li>User permission: Set the user permission in the format of <strong id="b842352706112054"><a name="b842352706112054"></a><a name="b842352706112054"></a>allSquash,rootSquash</strong>. That is, <strong id="b842352706112145"><a name="b842352706112145"></a><a name="b842352706112145"></a>allSquash</strong> is separated from <strong id="b842352706112149"><a name="b842352706112149"></a><a name="b842352706112149"></a>rootSquash</strong> using a comma (,). The value of <strong id="b1653573209112159"><a name="b1653573209112159"></a><a name="b1653573209112159"></a>allSquash</strong> can be <strong id="b842352706112215"><a name="b842352706112215"></a><a name="b842352706112215"></a>all_squash</strong> or <strong id="b842352706112221"><a name="b842352706112221"></a><a name="b842352706112221"></a>no_all_squash</strong>. The value of <strong id="b522459052112237"><a name="b522459052112237"></a><a name="b522459052112237"></a>rootSquash</strong> can be <strong id="b842352706112258"><a name="b842352706112258"></a><a name="b842352706112258"></a>root_squash</strong> or <strong id="b84235270611232"><a name="b84235270611232"></a><a name="b84235270611232"></a>no_root_squash</strong>. </li></ul>
    </div></div>
    <div class="notice" id="note3174139185520"><a name="note3174139185520"></a><a name="note3174139185520"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><a name="ul1782913302201"></a><a name="ul1782913302201"></a><ul id="ul1782913302201"><li>When creating a shared access rule for the IP address-based authorization scenario, the microversions of the APIs must be 2.28 or later and the <strong id="b1668184712512"><a name="b1668184712512"></a><a name="b1668184712512"></a>vpc_ip_base_acl</strong> parameter must be added to the request URL. For details, see the following request example (which varies with the IP address-based authorization scenario).</li><li>For an ECS in VPC A, its IP addresses can be successfully added to the authorized IP addresses of VPC B, but the file system of VPC B cannot be mounted to this ECS. The VPC used by the ECS and the file system must be the same one.</li></ul>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response \(VPC-based authorization\)

    When the specified API version ranges from 1.0 to 2.6, the request example is as follows:

    ```
    { 
        "os-allow_access": { 
            "access_to": "59cd070d-9c4c-462e-9dcc-b6bb716225bc", 
            "access_type": "cert", 
            "access_level": "rw" 
        } 
    }
    ```

    When the specified API version is later than 2.6, the request example is as follows: 

    ```
    { 
        "allow_access": { 
            "access_to": "59cd070d-9c4c-462e-9dcc-b6bb716225bc", 
            "access_type": "cert", 
            "access_level": "rw" 
        } 
    }
    ```


-   Example response \(IP address-based authorization\)

    POST  /v2/\{project\_id\}/shares/\{share\_id\}/action?vpc\_ip\_base\_acl=enable

    NFS share:

    ```
    { 
        "allow_access": { 
            "access_to": "0560a527-0e77-40a6-aa3b-110beecad368#0.0.0.0/0#1#all_squash,root_squash", 
            "access_type": "cert", 
            "access_level": "rw" 
        } 
    }
    ```

    CIFS share:

    ```
    { 
        "allow_access": { 
            "access_to": "0560a527-0e77-40a6-aa3b-110beecad368#0.0.0.0/0#0", 
            "access_type": "cert", 
            "access_level": "rw" 
        } 
    }
    ```

    >![](/images/icon-notice.gif) **NOTICE:**   
    >When creating the share access rule for an IP address-based authorization scenario.  
    >1. The  **X-Openstack-Manila-Api-Version**  parameter must be specified for the request header, and the value of  **X-Openstack-Manila-Api-Version**  must be from 2.28 to 2.42.  
    >2. The  **vpc\_ip\_base\_acl**  parameter must be added in the request URL and the value of  **vpc\_ip\_base\_acl**  must be set to  **enable**. To ensure compatibility, even though this parameter is left blank or set to another value other than  **enable**, you can use the API to create a share access rule for the IP address-based authorization scenario. However, this method of creation has been discarded and will not be maintained in the future.  


## Response<a name="s49caf4f5f50849fe92552867d4f15f34"></a>

-   Parameter description

    <a name="en-us_topic_0064390798_table52956621"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390798_row22822288"><th class="cellrowborder" valign="top" width="21.02%" id="mcps1.1.4.1.1"><p id="p10369123410146"><a name="p10369123410146"></a><a name="p10369123410146"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.25%" id="mcps1.1.4.1.2"><p id="p203841234131418"><a name="p203841234131418"></a><a name="p203841234131418"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.730000000000004%" id="mcps1.1.4.1.3"><p id="p12384203491414"><a name="p12384203491414"></a><a name="p12384203491414"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390798_row58761073"><td class="cellrowborder" valign="top" width="21.02%" headers="mcps1.1.4.1.1 "><p id="a243d2967d303468aa760d00127725c32"><a name="a243d2967d303468aa760d00127725c32"></a><a name="a243d2967d303468aa760d00127725c32"></a>access</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390798_p757259172256"><a name="en-us_topic_0064390798_p757259172256"></a><a name="en-us_topic_0064390798_p757259172256"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.730000000000004%" headers="mcps1.1.4.1.3 "><p id="a209c01902c264cb680c35677d47054b0"><a name="a209c01902c264cb680c35677d47054b0"></a><a name="a209c01902c264cb680c35677d47054b0"></a>Specifies the access object. If the share access rule is not updated, this value is <strong id="b196612352556"><a name="b196612352556"></a><a name="b196612352556"></a>null</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of the  **access**  field

    <a name="en-us_topic_0064390798_table38586810"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390798_row9150720"><th class="cellrowborder" valign="top" width="21.029999999999998%" id="mcps1.1.4.1.1"><p id="p047935141510"><a name="p047935141510"></a><a name="p047935141510"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.990000000000002%" id="mcps1.1.4.1.2"><p id="p114791957158"><a name="p114791957158"></a><a name="p114791957158"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.98%" id="mcps1.1.4.1.3"><p id="p194961753156"><a name="p194961753156"></a><a name="p194961753156"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390798_row12086140"><td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.4.1.1 "><p id="ade7f5aa946bd4b38a14586a7a5ea4f07"><a name="ade7f5aa946bd4b38a14586a7a5ea4f07"></a><a name="ade7f5aa946bd4b38a14586a7a5ea4f07"></a>share_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.4.1.2 "><p id="acc24d18212ff4e79baf8eea70448d011"><a name="acc24d18212ff4e79baf8eea70448d011"></a><a name="acc24d18212ff4e79baf8eea70448d011"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.98%" headers="mcps1.1.4.1.3 "><p id="a5ea83195b0da49d3b8ad87dd908c9cd3"><a name="a5ea83195b0da49d3b8ad87dd908c9cd3"></a><a name="a5ea83195b0da49d3b8ad87dd908c9cd3"></a>Specifies the UUID of the shared file system to which the access rule is added.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row748676"><td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.4.1.1 "><p id="a75c7a2d33fec479aaebad4087567c47d"><a name="a75c7a2d33fec479aaebad4087567c47d"></a><a name="a75c7a2d33fec479aaebad4087567c47d"></a>access_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.4.1.2 "><p id="a7461bbdfe85f4cc1803c4ff8ab4b8ca2"><a name="a7461bbdfe85f4cc1803c4ff8ab4b8ca2"></a><a name="a7461bbdfe85f4cc1803c4ff8ab4b8ca2"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.98%" headers="mcps1.1.4.1.3 "><p id="ac120a52789af482582a0fb9bb405d7b5"><a name="ac120a52789af482582a0fb9bb405d7b5"></a><a name="ac120a52789af482582a0fb9bb405d7b5"></a>Specifies the type of the share access rule.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row41110918"><td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.4.1.1 "><p id="a7c172a1393c047f0ac76bf357cc0fd46"><a name="a7c172a1393c047f0ac76bf357cc0fd46"></a><a name="a7c172a1393c047f0ac76bf357cc0fd46"></a>access_to</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.4.1.2 "><p id="a00e1e049a0064fec8a556a09aa21d120"><a name="a00e1e049a0064fec8a556a09aa21d120"></a><a name="a00e1e049a0064fec8a556a09aa21d120"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.98%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390798_p851710117391"><a name="en-us_topic_0064390798_p851710117391"></a><a name="en-us_topic_0064390798_p851710117391"></a>Specifies the access that the back end grants or denies.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row3472933"><td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.4.1.1 "><p id="a158519a5a3c548d79e117474ab1da360"><a name="a158519a5a3c548d79e117474ab1da360"></a><a name="a158519a5a3c548d79e117474ab1da360"></a>access_level</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.4.1.2 "><p id="a54b5565d34dd4ccd9cc3ae3f8de1d04e"><a name="a54b5565d34dd4ccd9cc3ae3f8de1d04e"></a><a name="a54b5565d34dd4ccd9cc3ae3f8de1d04e"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.98%" headers="mcps1.1.4.1.3 "><p id="a7b6040b79fc04b78808a70ff8d142ec5"><a name="a7b6040b79fc04b78808a70ff8d142ec5"></a><a name="a7b6040b79fc04b78808a70ff8d142ec5"></a>Specifies the access level of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row63592346"><td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.4.1.1 "><p id="a8dc3a9af17c442a88d667e71ee206114"><a name="a8dc3a9af17c442a88d667e71ee206114"></a><a name="a8dc3a9af17c442a88d667e71ee206114"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.4.1.2 "><p id="a511925acc242408896e80fa37a47043b"><a name="a511925acc242408896e80fa37a47043b"></a><a name="a511925acc242408896e80fa37a47043b"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.98%" headers="mcps1.1.4.1.3 "><p id="a0d9b3408e587442a90e53eb5ce5f98ec"><a name="a0d9b3408e587442a90e53eb5ce5f98ec"></a><a name="a0d9b3408e587442a90e53eb5ce5f98ec"></a>Specifies the UUID of the share access rule.</p>
    </td>
    </tr>
    <tr id="r3028d814ba7f4035b4a1a07f2336149f"><td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.4.1.1 "><p id="a7ad61dc3d43f403a937eafe1f080c091"><a name="a7ad61dc3d43f403a937eafe1f080c091"></a><a name="a7ad61dc3d43f403a937eafe1f080c091"></a>state</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.4.1.2 "><p id="a9ff0d54e2ce8460bbeedff326b3abeac"><a name="a9ff0d54e2ce8460bbeedff326b3abeac"></a><a name="a9ff0d54e2ce8460bbeedff326b3abeac"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.98%" headers="mcps1.1.4.1.3 "><p id="p121105177474"><a name="p121105177474"></a><a name="p121105177474"></a>Specifies the status of the share access rule. If the API version is earlier than 2.28, the status of the share access rule is <strong id="b842352706205652"><a name="b842352706205652"></a><a name="b842352706205652"></a>new</strong>, <strong id="b84235270620570"><a name="b84235270620570"></a><a name="b84235270620570"></a>active</strong>, or <strong id="b84235270620573"><a name="b84235270620573"></a><a name="b84235270620573"></a>error</strong>. In versions from 2.28 to 2.42, the status of the share access rule is <strong id="b842352706205734"><a name="b842352706205734"></a><a name="b842352706205734"></a>queued_to_apply</strong>, <strong id="b842352706205741"><a name="b842352706205741"></a><a name="b842352706205741"></a>applying</strong>, <strong id="b842352706205747"><a name="b842352706205747"></a><a name="b842352706205747"></a>active</strong>, <strong id="b842352706205753"><a name="b842352706205753"></a><a name="b842352706205753"></a>error</strong>, <strong id="b84235270620581"><a name="b84235270620581"></a><a name="b84235270620581"></a>queued_to_deny</strong>, or <strong id="b84235270620586"><a name="b84235270620586"></a><a name="b84235270620586"></a>denying</strong>.</p>
    </td>
    </tr>
    <tr id="row4201917114910"><td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.4.1.1 "><p id="p1348615521813"><a name="p1348615521813"></a><a name="p1348615521813"></a>access_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.4.1.2 "><p id="p14486352683"><a name="p14486352683"></a><a name="p14486352683"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.98%" headers="mcps1.1.4.1.3 "><p id="p84875524818"><a name="p84875524818"></a><a name="p84875524818"></a>Specifies the access credential of the access rule. This parameter exists only when the value of <strong id="b1486015285517"><a name="b1486015285517"></a><a name="b1486015285517"></a>X-Openstack-Manila-Api-Version</strong> in the request header is from 2.21 to 2.42.</p>
    </td>
    </tr>
    <tr id="row394295013488"><td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.4.1.1 "><p id="p10201155134810"><a name="p10201155134810"></a><a name="p10201155134810"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.4.1.2 "><p id="p5201165514816"><a name="p5201165514816"></a><a name="p5201165514816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.98%" headers="mcps1.1.4.1.3 "><p id="p72011155134814"><a name="p72011155134814"></a><a name="p72011155134814"></a>Specifies the time when a shared access rule is created. This parameter exists only when the value of <strong id="b515965654"><a name="b515965654"></a><a name="b515965654"></a>X-Openstack-Manila-Api-Version</strong> in the request header is greater than or equal to 2.33.</p>
    </td>
    </tr>
    <tr id="row147971753154819"><td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.4.1.1 "><p id="p1463583132213"><a name="p1463583132213"></a><a name="p1463583132213"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.4.1.2 "><p id="p1520115553482"><a name="p1520115553482"></a><a name="p1520115553482"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.98%" headers="mcps1.1.4.1.3 "><p id="p1720135512481"><a name="p1720135512481"></a><a name="p1720135512481"></a>Specifies the time when a shared access rule is updated. This parameter exists only when the value of <strong id="b1051713214"><a name="b1051713214"></a><a name="b1051713214"></a>X-Openstack-Manila-Api-Version</strong> in the request header is greater than or equal to 2.33.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "access": {
        "share_id": "15940c49-789f-476a-b099-a3be7d311854",
        "access_type": "cert",
        "access_to": "59cd070d-9c4c-462e-9dcc-b6bb716225bc",
        "access_level": "rw",
        "state": "new",
        "id": "418e3cf4-08c3-4ed2-a29a-ceffa346b3b8",
        "access_key":null,
        "created_at": "2017-07-07T03:15:06.858662",
        "updated_at": "2018-07-07T03:15:06.858662"
      }
    }
    ```


-   Example response \(IP address-based authorization\)

    NFS share:

    ```
    {
        "access":{
            "access_key":null,
            "share_id":"7ec1115f-518b-40ff-a998-5599ce2da332",
            "access_type":"cert",
            "access_to":"0560a527-0e77-40a6-aa3b-110beecad368#0.0.0.0/0#1#all_squash,root_squash",
            "access_level":"rw",
            "state":"queued_to_apply",
            "id":"24615391-d58d-4a74-ac5a-520233c9c396",
            "created_at": "2017-07-07T03:15:06.858662",
            "updated_at": "2018-07-07T03:15:06.858662"
        }
    }
    ```

    CIFS share:

    ```
    {
        "access":{
            "access_key":null,
            "share_id":"7ec1115f-518b-40ff-a998-5599ce2da332",
            "access_type":"cert",
            "access_to":"0560a527-0e77-40a6-aa3b-110beecad368#0.0.0.0/0#0",
            "access_level":"rw",
            "state":"queued_to_apply",
            "id":"24615391-d58d-4a74-ac5a-520233c9c396",
            "created_at": "2017-07-07T03:15:06.858662",
            "updated_at": "2018-07-07T03:15:06.858662"
        }
    }
    ```


## Status Codes<a name="s0bd8d946290c43d3a54ae9d1cfed754c"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0064390798_table35008393"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390798_row56283646"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="en-us_topic_0064390798_p62681466"><a name="en-us_topic_0064390798_p62681466"></a><a name="en-us_topic_0064390798_p62681466"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="en-us_topic_0064390798_p44033946"><a name="en-us_topic_0064390798_p44033946"></a><a name="en-us_topic_0064390798_p44033946"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390798_row9979846"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390798_p3061223"><a name="en-us_topic_0064390798_p3061223"></a><a name="en-us_topic_0064390798_p3061223"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390798_p46632549"><a name="en-us_topic_0064390798_p46632549"></a><a name="en-us_topic_0064390798_p46632549"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row17039762"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390798_p38043494"><a name="en-us_topic_0064390798_p38043494"></a><a name="en-us_topic_0064390798_p38043494"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390798_p61624137"><a name="en-us_topic_0064390798_p61624137"></a><a name="en-us_topic_0064390798_p61624137"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row17746329"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390798_p28166553"><a name="en-us_topic_0064390798_p28166553"></a><a name="en-us_topic_0064390798_p28166553"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390798_p66898301"><a name="en-us_topic_0064390798_p66898301"></a><a name="en-us_topic_0064390798_p66898301"></a>Access to the requested page is forbidden.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row65213800"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390798_p47826462"><a name="en-us_topic_0064390798_p47826462"></a><a name="en-us_topic_0064390798_p47826462"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390798_p48738220"><a name="en-us_topic_0064390798_p48738220"></a><a name="en-us_topic_0064390798_p48738220"></a>The requested page was not found.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row35990804"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390798_p29574043"><a name="en-us_topic_0064390798_p29574043"></a><a name="en-us_topic_0064390798_p29574043"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390798_p46687245"><a name="en-us_topic_0064390798_p46687245"></a><a name="en-us_topic_0064390798_p46687245"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row17532027"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390798_p10808059"><a name="en-us_topic_0064390798_p10808059"></a><a name="en-us_topic_0064390798_p10808059"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390798_p3037596"><a name="en-us_topic_0064390798_p3037596"></a><a name="en-us_topic_0064390798_p3037596"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row27338368"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390798_p66924213"><a name="en-us_topic_0064390798_p66924213"></a><a name="en-us_topic_0064390798_p66924213"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390798_p52152158"><a name="en-us_topic_0064390798_p52152158"></a><a name="en-us_topic_0064390798_p52152158"></a>You must use the proxy server for authentication. Then the request can be processed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row66716242"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390798_p35306501"><a name="en-us_topic_0064390798_p35306501"></a><a name="en-us_topic_0064390798_p35306501"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390798_p41254304"><a name="en-us_topic_0064390798_p41254304"></a><a name="en-us_topic_0064390798_p41254304"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row35744420"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390798_p9616944"><a name="en-us_topic_0064390798_p9616944"></a><a name="en-us_topic_0064390798_p9616944"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390798_p40774967"><a name="en-us_topic_0064390798_p40774967"></a><a name="en-us_topic_0064390798_p40774967"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row31430389"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390798_p62833603"><a name="en-us_topic_0064390798_p62833603"></a><a name="en-us_topic_0064390798_p62833603"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390798_p56357057"><a name="en-us_topic_0064390798_p56357057"></a><a name="en-us_topic_0064390798_p56357057"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row37451465"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390798_p13669843"><a name="en-us_topic_0064390798_p13669843"></a><a name="en-us_topic_0064390798_p13669843"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390798_p33515489"><a name="en-us_topic_0064390798_p33515489"></a><a name="en-us_topic_0064390798_p33515489"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row33203949"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390798_p5165373"><a name="en-us_topic_0064390798_p5165373"></a><a name="en-us_topic_0064390798_p5165373"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390798_p15742086"><a name="en-us_topic_0064390798_p15742086"></a><a name="en-us_topic_0064390798_p15742086"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row7461047"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390798_p365031"><a name="en-us_topic_0064390798_p365031"></a><a name="en-us_topic_0064390798_p365031"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390798_p29567523"><a name="en-us_topic_0064390798_p29567523"></a><a name="en-us_topic_0064390798_p29567523"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390798_row64781122"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390798_p12779516"><a name="en-us_topic_0064390798_p12779516"></a><a name="en-us_topic_0064390798_p12779516"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390798_p28507895"><a name="en-us_topic_0064390798_p28507895"></a><a name="en-us_topic_0064390798_p28507895"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


