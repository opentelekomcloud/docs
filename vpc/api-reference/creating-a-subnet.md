# Creating a Subnet<a name="EN-US_TOPIC_0020090590"></a>

## Function<a name="section18389930"></a>

This interface is used to create a subnet.

## URI<a name="section31291646"></a>

-   POST /v1/\{tenant\_id\}/subnets
-   Parameter description

    <a name="table21421675"></a><table><thead align="left"><tr id="row9119245"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p461342"><a name="p461342"></a><a name="p461342"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p37368736"><a name="p37368736"></a><a name="p37368736"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p6968762"><a name="p6968762"></a><a name="p6968762"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row27598869"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p20915929"><a name="p20915929"></a><a name="p20915929"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p16468652"><a name="p16468652"></a><a name="p16468652"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p58892473"><a name="p58892473"></a><a name="p58892473"></a>Specifies the tenant ID of the operator.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section13189358"></a>

-   Parameter description

    <a name="table435429715639"></a><table><thead align="left"><tr id="row3955678815639"><th class="cellrowborder" valign="top" width="15.410000000000002%" id="mcps1.1.5.1.1"><p id="p4998329315639"><a name="p4998329315639"></a><a name="p4998329315639"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.12%" id="mcps1.1.5.1.2"><p id="p2211493815639"><a name="p2211493815639"></a><a name="p2211493815639"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.610000000000003%" id="mcps1.1.5.1.3"><p id="p4647957215639"><a name="p4647957215639"></a><a name="p4647957215639"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.86000000000001%" id="mcps1.1.5.1.4"><p id="p674897815639"><a name="p674897815639"></a><a name="p674897815639"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row979634915639"><td class="cellrowborder" valign="top" width="15.410000000000002%" headers="mcps1.1.5.1.1 "><p id="p5530678015639"><a name="p5530678015639"></a><a name="p5530678015639"></a>subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.12%" headers="mcps1.1.5.1.2 "><p id="p5066418415639"><a name="p5066418415639"></a><a name="p5066418415639"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.610000000000003%" headers="mcps1.1.5.1.3 "><p id="p1015820015639"><a name="p1015820015639"></a><a name="p1015820015639"></a><em id="i2431493715639"><a name="i2431493715639"></a><a name="i2431493715639"></a>Dictionary data structure</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="42.86000000000001%" headers="mcps1.1.5.1.4 "><p id="p2335287515639"><a name="p2335287515639"></a><a name="p2335287515639"></a>Specifies the subnet objects.</p>
    </td>
    </tr>
    </tbody>
    </table>

    Descriptions of  **subnet**  fields

    <a name="table45596481"></a><table><thead align="left"><tr id="row36936550"><th class="cellrowborder" valign="top" width="21.990000000000002%" id="mcps1.1.5.1.1"><p id="p39070558"><a name="p39070558"></a><a name="p39070558"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.1.5.1.2"><p id="p10598606"><a name="p10598606"></a><a name="p10598606"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.040000000000001%" id="mcps1.1.5.1.3"><p id="p795223417488"><a name="p795223417488"></a><a name="p795223417488"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.050000000000004%" id="mcps1.1.5.1.4"><p id="p53180767"><a name="p53180767"></a><a name="p53180767"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12674872"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p20031746"><a name="p20031746"></a><a name="p20031746"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.2 "><p id="p11958757"><a name="p11958757"></a><a name="p11958757"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.3 "><p id="p190787317482"><a name="p190787317482"></a><a name="p190787317482"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.1.5.1.4 "><p id="p29135240"><a name="p29135240"></a><a name="p29135240"></a>Specifies the subnet name.</p>
    <p id="p11144211"><a name="p11144211"></a><a name="p11144211"></a>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</p>
    </td>
    </tr>
    <tr id="row33189039"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p3957675"><a name="p3957675"></a><a name="p3957675"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.2 "><p id="p52136226"><a name="p52136226"></a><a name="p52136226"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.3 "><p id="p2032001117482"><a name="p2032001117482"></a><a name="p2032001117482"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.1.5.1.4 "><p id="p62284798"><a name="p62284798"></a><a name="p62284798"></a>Specifies the network segment on which the subnet resides.</p>
    <p id="p11903911"><a name="p11903911"></a><a name="p11903911"></a>The value must be in CIDR format.</p>
    <p id="p40026340"><a name="p40026340"></a><a name="p40026340"></a>The value must be within the CIDR block of the VPC. The subnet mask cannot be greater than 29.</p>
    </td>
    </tr>
    <tr id="row24692740"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p53954942"><a name="p53954942"></a><a name="p53954942"></a>gateway_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.2 "><p id="p8274172"><a name="p8274172"></a><a name="p8274172"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.3 "><p id="p3530821417482"><a name="p3530821417482"></a><a name="p3530821417482"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.1.5.1.4 "><p id="p66228199"><a name="p66228199"></a><a name="p66228199"></a>Specifies the gateway of the subnet.</p>
    <p id="p62883878"><a name="p62883878"></a><a name="p62883878"></a>The value must be a valid IP address.</p>
    <p id="p29083993"><a name="p29083993"></a><a name="p29083993"></a>The value must be an IP address in the subnet segment.</p>
    </td>
    </tr>
    <tr id="row60429346"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p62938818"><a name="p62938818"></a><a name="p62938818"></a>dhcp_enable</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.2 "><p id="p64879470"><a name="p64879470"></a><a name="p64879470"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.3 "><p id="p4139309817482"><a name="p4139309817482"></a><a name="p4139309817482"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.1.5.1.4 "><p id="p23779887174921"><a name="p23779887174921"></a><a name="p23779887174921"></a>Specifies whether the DHCP function is enabled for the subnet.</p>
    <p id="p29976079174925"><a name="p29976079174925"></a><a name="p29976079174925"></a>The value can be <strong>true</strong> or <strong>false</strong>.</p>
    <p id="p16049999"><a name="p16049999"></a><a name="p16049999"></a>If this parameter is left blank, it is set to <strong>true</strong> by default.</p>
    </td>
    </tr>
    <tr id="row10232270"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p23507505"><a name="p23507505"></a><a name="p23507505"></a>primary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.2 "><p id="p25059790"><a name="p25059790"></a><a name="p25059790"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.3 "><p id="p6450660517482"><a name="p6450660517482"></a><a name="p6450660517482"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.1.5.1.4 "><p id="p567760"><a name="p567760"></a><a name="p567760"></a>Specifies the IP address of DNS server 1 on the subnet.</p>
    <p id="p5109846"><a name="p5109846"></a><a name="p5109846"></a>The value must be a valid IP address.</p>
    </td>
    </tr>
    <tr id="row45988614"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p34090260"><a name="p34090260"></a><a name="p34090260"></a>secondary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.2 "><p id="p9847715"><a name="p9847715"></a><a name="p9847715"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.3 "><p id="p5765255417482"><a name="p5765255417482"></a><a name="p5765255417482"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.1.5.1.4 "><p id="p65445301"><a name="p65445301"></a><a name="p65445301"></a>Specifies the IP address of DNS server 2 on the subnet.</p>
    <p id="p52136803"><a name="p52136803"></a><a name="p52136803"></a>The value must be a valid IP address.</p>
    </td>
    </tr>
    <tr id="row1596910210505"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p1842890810505"><a name="p1842890810505"></a><a name="p1842890810505"></a>dnsList</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.2 "><p id="p1634655410505"><a name="p1634655410505"></a><a name="p1634655410505"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.3 "><p id="p4900246410505"><a name="p4900246410505"></a><a name="p4900246410505"></a>List</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.1.5.1.4 "><p id="p3461234111954"><a name="p3461234111954"></a><a name="p3461234111954"></a>Specifies the DNS server address list of a subnet. This field is required if you need to use more than two DNS servers.</p>
    <p id="p4307562111954"><a name="p4307562111954"></a><a name="p4307562111954"></a>This parameter value is the superset of both DNS server address 1 and DNS server address 2.</p>
    </td>
    </tr>
    <tr id="row66578044"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p24112512"><a name="p24112512"></a><a name="p24112512"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.2 "><p id="p6956456"><a name="p6956456"></a><a name="p6956456"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.3 "><p id="p3934528717482"><a name="p3934528717482"></a><a name="p3934528717482"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.1.5.1.4 "><p id="p1175390117504"><a name="p1175390117504"></a><a name="p1175390117504"></a>Identifies the availability zone (AZ) to which the subnet belongs.</p>
    <p id="p4402274117507"><a name="p4402274117507"></a><a name="p4402274117507"></a>The value must be an existing AZ in the system.</p>
    </td>
    </tr>
    <tr id="row53182860"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p12844374"><a name="p12844374"></a><a name="p12844374"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.2 "><p id="p33761356"><a name="p33761356"></a><a name="p33761356"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.3 "><p id="p3285166017482"><a name="p3285166017482"></a><a name="p3285166017482"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.1.5.1.4 "><p id="p50315352"><a name="p50315352"></a><a name="p50315352"></a>Specifies the ID of the VPC to which the subnet belongs.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example Request

    ```
    {
      "subnet":
             {
              "name": "subnet",
              "cidr": "192.168.20.0/24",
              "gateway_ip": "192.168.20.1",
              "dhcp_enable": "true",
              "primary_dns": "114.xx.xx.114",
              "secondary_dns": "114.xx.xx.115",
              "dnsList": [
                  "114.xx.xx.114",
                  "114.xx.xx.115"
              ],
              "availability_zone":"aa-bb-cc",//AZ aa-bb-cc is used as an example.
              "vpc_id":"3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85"
              }
    }
    ```


## Response<a name="section51595365"></a>

-   Parameter description

    <a name="table3201287115737"></a><table><thead align="left"><tr id="row4941460315737"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.1.4.1.1"><p id="p4315992415737"><a name="p4315992415737"></a><a name="p4315992415737"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.1.4.1.2"><p id="p3996487815737"><a name="p3996487815737"></a><a name="p3996487815737"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.1.4.1.3"><p id="p1592968015737"><a name="p1592968015737"></a><a name="p1592968015737"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1523569015737"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.1.4.1.1 "><p id="p2613139715737"><a name="p2613139715737"></a><a name="p2613139715737"></a>subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p5206127615737"><a name="p5206127615737"></a><a name="p5206127615737"></a><em id="i2431493715639_1"><a name="i2431493715639_1"></a><a name="i2431493715639_1"></a>Dictionary data structure</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.1.4.1.3 "><p id="p3616274015737"><a name="p3616274015737"></a><a name="p3616274015737"></a>Specifies the subnet objects.</p>
    </td>
    </tr>
    </tbody>
    </table>

    Descriptions of  **subnet**  fields

    <a name="table54041329"></a><table><thead align="left"><tr id="row3088388"><th class="cellrowborder" valign="top" width="28.860000000000003%" id="mcps1.1.4.1.1"><p id="p48832851"><a name="p48832851"></a><a name="p48832851"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.25%" id="mcps1.1.4.1.2"><p id="p31305988175034"><a name="p31305988175034"></a><a name="p31305988175034"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.89%" id="mcps1.1.4.1.3"><p id="p14620943"><a name="p14620943"></a><a name="p14620943"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row43445707"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.1.4.1.1 "><p id="p29441404"><a name="p29441404"></a><a name="p29441404"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.1.4.1.2 "><p id="p52757101175034"><a name="p52757101175034"></a><a name="p52757101175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.1.4.1.3 "><p id="p25747420"><a name="p25747420"></a><a name="p25747420"></a>Specifies a resource ID in UUID format.</p>
    </td>
    </tr>
    <tr id="row30400195"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.1.4.1.1 "><p id="p46496694"><a name="p46496694"></a><a name="p46496694"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.1.4.1.2 "><p id="p45466823175034"><a name="p45466823175034"></a><a name="p45466823175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.1.4.1.3 "><p id="p55028720"><a name="p55028720"></a><a name="p55028720"></a>Specifies the subnet name.</p>
    </td>
    </tr>
    <tr id="row51945267"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.1.4.1.1 "><p id="p46817064"><a name="p46817064"></a><a name="p46817064"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.1.4.1.2 "><p id="p58934074175034"><a name="p58934074175034"></a><a name="p58934074175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.1.4.1.3 "><p id="p9487824"><a name="p9487824"></a><a name="p9487824"></a>Specifies the subnet network segment.</p>
    </td>
    </tr>
    <tr id="row39696553"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.1.4.1.1 "><p id="p61304253"><a name="p61304253"></a><a name="p61304253"></a>gateway_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.1.4.1.2 "><p id="p8930669175034"><a name="p8930669175034"></a><a name="p8930669175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.1.4.1.3 "><p id="p52252659"><a name="p52252659"></a><a name="p52252659"></a>Specifies the subnet gateway address.</p>
    </td>
    </tr>
    <tr id="row4606985"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.1.4.1.1 "><p id="p37621475"><a name="p37621475"></a><a name="p37621475"></a>dhcp_enable</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.1.4.1.2 "><p id="p52295560175034"><a name="p52295560175034"></a><a name="p52295560175034"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.1.4.1.3 "><p id="p29849008175159"><a name="p29849008175159"></a><a name="p29849008175159"></a>Specifies whether the DHCP function is enabled for the subnet.</p>
    </td>
    </tr>
    <tr id="row1048160"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.1.4.1.1 "><p id="p17792110"><a name="p17792110"></a><a name="p17792110"></a>primary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.1.4.1.2 "><p id="p8081972175034"><a name="p8081972175034"></a><a name="p8081972175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.1.4.1.3 "><p id="p19162058"><a name="p19162058"></a><a name="p19162058"></a>Specifies the IP address of DNS server 1 on the subnet.</p>
    </td>
    </tr>
    <tr id="row8622890"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.1.4.1.1 "><p id="p27365507"><a name="p27365507"></a><a name="p27365507"></a>secondary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.1.4.1.2 "><p id="p50659992175034"><a name="p50659992175034"></a><a name="p50659992175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.1.4.1.3 "><p id="p58602024"><a name="p58602024"></a><a name="p58602024"></a>Specifies the IP address of DNS server 2 on the subnet.</p>
    </td>
    </tr>
    <tr id="row29925916105649"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.1.4.1.1 "><p id="p8080156105649"><a name="p8080156105649"></a><a name="p8080156105649"></a>dnsList</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.1.4.1.2 "><p id="p65014446105649"><a name="p65014446105649"></a><a name="p65014446105649"></a>List</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.1.4.1.3 "><p id="p31678735105649"><a name="p31678735105649"></a><a name="p31678735105649"></a>Specifies the IP address list of DNS servers on the subnet.</p>
    </td>
    </tr>
    <tr id="row49143529"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.1.4.1.1 "><p id="p21202951"><a name="p21202951"></a><a name="p21202951"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.1.4.1.2 "><p id="p9818717175034"><a name="p9818717175034"></a><a name="p9818717175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.1.4.1.3 "><p id="p44463652175257"><a name="p44463652175257"></a><a name="p44463652175257"></a>Identifies the AZ to which the subnet belongs.</p>
    </td>
    </tr>
    <tr id="row15677883"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.1.4.1.1 "><p id="p61948991"><a name="p61948991"></a><a name="p61948991"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.1.4.1.2 "><p id="p57118635175034"><a name="p57118635175034"></a><a name="p57118635175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.1.4.1.3 "><p id="p36052245"><a name="p36052245"></a><a name="p36052245"></a>Specifies the ID of the VPC to which the subnet belongs.</p>
    </td>
    </tr>
    <tr id="row34550710"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.1.4.1.1 "><p id="p47144157"><a name="p47144157"></a><a name="p47144157"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.1.4.1.2 "><p id="p63206697175034"><a name="p63206697175034"></a><a name="p63206697175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.1.4.1.3 "><p id="p5432205"><a name="p5432205"></a><a name="p5432205"></a>The value can be <strong>ACTIVE</strong>, <strong>DOWN</strong>, <strong>UNKNOWN</strong>, or <strong>ERROR</strong>.</p>
    <a name="ul756817571315"></a><a name="ul756817571315"></a><ul id="ul756817571315"><li id="li175681357183117"><a name="li175681357183117"></a><a name="li175681357183117"></a><strong>ACTIVE</strong>: indicates that the subnet has been attached to the router.</li><li id="li5568157103111"><a name="li5568157103111"></a><a name="li5568157103111"></a><strong id="b842352706151633"><a name="b842352706151633"></a><a name="b842352706151633"></a>UNKNOWN</strong>: indicates that the subnet has not been attached to the router.</li><li id="li85681932326"><a name="li85681932326"></a><a name="li85681932326"></a><strong id="b842352706151734"><a name="b842352706151734"></a><a name="b842352706151734"></a>ERROR</strong>: indicates that the subnet is abnormal.</li></ul>
    <p id="p48889850"><a name="p48889850"></a><a name="p48889850"></a>Specifies the status of the subnet.</p>
    <p id="p1826011115242"><a name="p1826011115242"></a><a name="p1826011115242"></a>The system creates a subnet and then attaches the subnet to the router in the threads.</p>
    <p id="p897825072010"><a name="p897825072010"></a><a name="p897825072010"></a>In the concurrent scenario, if the CIDR of the created subnet is the same as that of an existing subnet, the created subnet fails to attach to the router after underlying system verification. As a result, the subnet creation fails.</p>
    <p id="p13289132102011"><a name="p13289132102011"></a><a name="p13289132102011"></a>In this scenario, the returned value of <strong id="b842352706172823"><a name="b842352706172823"></a><a name="b842352706172823"></a>status</strong> is <strong id="b842352706172828"><a name="b842352706172828"></a><a name="b842352706172828"></a>UNKNOWN</strong>.</p>
    </td>
    </tr>
    <tr id="row3884489103221"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.1.4.1.1 "><p id="p34960403103221"><a name="p34960403103221"></a><a name="p34960403103221"></a>neutron_network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.1.4.1.2 "><p id="p64221241103221"><a name="p64221241103221"></a><a name="p64221241103221"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.1.4.1.3 "><p id="p34538004103221"><a name="p34538004103221"></a><a name="p34538004103221"></a>Specifies the network (Native OpenStack API) ID.</p>
    </td>
    </tr>
    <tr id="row5205001104010"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.1.4.1.1 "><p id="p18951959104010"><a name="p18951959104010"></a><a name="p18951959104010"></a>neutron_subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.1.4.1.2 "><p id="p58188011104010"><a name="p58188011104010"></a><a name="p58188011104010"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.1.4.1.3 "><p id="p15608450104010"><a name="p15608450104010"></a><a name="p15608450104010"></a>Specifies the subnet (Native OpenStack API) ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example Response

    ```
    {
        "subnet": {
            "id": "4779ab1c-7c1a-44b1-a02e-93dfc361b32d",
            "name": "subnet",
            "cidr": "192.168.20.0/24",
            "dnsList": [
                "114.xx.xx.114",
                "1114.xx.xx.115"
            ],
            "status": "UNKNOWN",
            "vpc_id": "3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85",
            "gateway_ip": "192.168.20.1",
            "dhcp_enable": true,
            "primary_dns": "114.xx.xx.114",
            "secondary_dns": "114.xx.xx.115",
              "availability_zone":"aa-bb-cc",//AZ aa-bb-cc is used as an example.
            "neutron_network_id": "4779ab1c-7c1a-44b1-a02e-93dfc361b32d",
            "neutron_subnet_id": "213cb9d-3122-2ac1-1a29-91ffc1231a12"
        }
    }
    ```


## Returned Value<a name="section61705107"></a>

-   Normal

    200

-   Abnormal

    <a name="table1697655195242"></a><table><thead align="left"><tr id="row4329637495242"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p1734541495242"><a name="p1734541495242"></a><a name="p1734541495242"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p6280127495242"><a name="p6280127495242"></a><a name="p6280127495242"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5373842795242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5784529695242"><a name="p5784529695242"></a><a name="p5784529695242"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5495737795242"><a name="p5495737795242"></a><a name="p5495737795242"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row2485435295242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p6704552895242"><a name="p6704552895242"></a><a name="p6704552895242"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p6197867295242"><a name="p6197867295242"></a><a name="p6197867295242"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row2093713795242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1818656595242"><a name="p1818656595242"></a><a name="p1818656595242"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p6382566195242"><a name="p6382566195242"></a><a name="p6382566195242"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row3756004295242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2246459695242"><a name="p2246459695242"></a><a name="p2246459695242"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p769301595242"><a name="p769301595242"></a><a name="p769301595242"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row212827395242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3817239595242"><a name="p3817239595242"></a><a name="p3817239595242"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p495627395242"><a name="p495627395242"></a><a name="p495627395242"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row4460646595242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5635390995242"><a name="p5635390995242"></a><a name="p5635390995242"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p126394695242"><a name="p126394695242"></a><a name="p126394695242"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row1137552095242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p4900196195242"><a name="p4900196195242"></a><a name="p4900196195242"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p973591095242"><a name="p973591095242"></a><a name="p973591095242"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row2051433295242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5104819595242"><a name="p5104819595242"></a><a name="p5104819595242"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p4126312295242"><a name="p4126312295242"></a><a name="p4126312295242"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row3582378595242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1604544895242"><a name="p1604544895242"></a><a name="p1604544895242"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2461290095242"><a name="p2461290095242"></a><a name="p2461290095242"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row2018950895242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2473741395242"><a name="p2473741395242"></a><a name="p2473741395242"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5757343195242"><a name="p5757343195242"></a><a name="p5757343195242"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row4839883395242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2799143995242"><a name="p2799143995242"></a><a name="p2799143995242"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5271409795242"><a name="p5271409795242"></a><a name="p5271409795242"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row466483295242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p4230707595242"><a name="p4230707595242"></a><a name="p4230707595242"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p432108895242"><a name="p432108895242"></a><a name="p432108895242"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row3888979595242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p6306567195242"><a name="p6306567195242"></a><a name="p6306567195242"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p804572095242"><a name="p804572095242"></a><a name="p804572095242"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row530261695242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2685875895242"><a name="p2685875895242"></a><a name="p2685875895242"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2807582995242"><a name="p2807582995242"></a><a name="p2807582995242"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section85821649202813"></a>

For details, see section  [Error Codes](error-codes-27.md).

