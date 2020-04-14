# Step 1: Creating a DIS Stream<a name="dis_01_0601"></a>

You can create a DIS stream on the DIS management console.

## Procedure<a name="section39878449"></a>

1.  Use the account to log in to the DIS console.  

    **Figure  1**  DIS management console<a name="fig12690164612212"></a>  
    ![](figures/dis-management-console.jpg "dis-management-console")

2.  Click  ![](figures/wwx437827-中软基础平台部-datasight-image-bbfbe22f-2a2d-4e1b-8f10-a7782fd1d3ed.png)  in the upper left corner of the page and select a region and project.
3.  On the homepage, click  **Create Stream**  and configure stream parameters.

    **Table  1**  Stream parameters

    <a name="table328403631418"></a>
    <table><thead align="left"><tr id="row357610691418"><th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.1"><p id="p315806171418"><a name="p315806171418"></a><a name="p315806171418"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="60.209999999999994%" id="mcps1.2.4.1.2"><p id="p78931591418"><a name="p78931591418"></a><a name="p78931591418"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.62%" id="mcps1.2.4.1.3"><p id="p353661091418"><a name="p353661091418"></a><a name="p353661091418"></a>Example</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6491641418"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p525822931418"><a name="p525822931418"></a><a name="p525822931418"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.2 "><p id="p313073021418"><a name="p313073021418"></a><a name="p313073021418"></a>Physical location of the cloud service. You can select a different region from the drop-down list.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.2.4.1.3 "><p id="p6323188132310"><a name="p6323188132310"></a><a name="p6323188132310"></a>-</p>
    </td>
    </tr>
    <tr id="row60097061418"><td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.4.1.1 mcps1.2.4.1.2 mcps1.2.4.1.3 "><p id="p42690617141219"><a name="p42690617141219"></a><a name="p42690617141219"></a><strong id="b11481420315"><a name="b11481420315"></a><a name="b11481420315"></a>Basic Information</strong></p>
    </td>
    </tr>
    <tr id="row392937481418"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p286770571418"><a name="p286770571418"></a><a name="p286770571418"></a>Stream Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.2 "><p id="p411402701418"><a name="p411402701418"></a><a name="p411402701418"></a>Name of the DIS stream to be created. A stream name is 1 to 64 characters long. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.2.4.1.3 "><p id="p440275551418"><a name="p440275551418"></a><a name="p440275551418"></a>dis-Tido</p>
    </td>
    </tr>
    <tr id="row607036811418"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p180510941418"><a name="p180510941418"></a><a name="p180510941418"></a>Stream Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.2 "><a name="ul2481239414181"></a><a name="ul2481239414181"></a><ul id="ul2481239414181"><li><strong id="b270313478366"><a name="b270313478366"></a><a name="b270313478366"></a>Common</strong>: Each partition supports a maximum read speed of 2 MB/s and a maximum write speed of 1 MB/s.</li><li><strong id="b362495163612"><a name="b362495163612"></a><a name="b362495163612"></a>Advanced</strong>: Each partition supports a maximum read speed of 10 MB/s and a maximum write speed of 5 MB/s.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.2.4.1.3 "><p id="p531930861418"><a name="p531930861418"></a><a name="p531930861418"></a>-</p>
    </td>
    </tr>
    <tr id="row89757261418"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p559451901418"><a name="p559451901418"></a><a name="p559451901418"></a>Partitions</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.2 "><div class="p" id="p50847566142947"><a name="p50847566142947"></a><a name="p50847566142947"></a>Partitions are the base throughput unit of a DIS stream. <a name="ul64669032142927"></a><a name="ul64669032142927"></a><ul id="ul64669032142927"><li>For a common DIS stream, the value of <strong id="b5668832395556"><a name="b5668832395556"></a><a name="b5668832395556"></a>Partitions</strong> is an integer from 1 to 50. A tenant can create a maximum of 50 partitions.</li><li>For an advanced DIS stream, the value of <strong id="b405423599567"><a name="b405423599567"></a><a name="b405423599567"></a>Partitions</strong> is an integer from 1 to 10. A tenant can create a maximum of 10 partitions.</li></ul>
    </div>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.2.4.1.3 "><p id="p380157191418"><a name="p380157191418"></a><a name="p380157191418"></a>5</p>
    </td>
    </tr>
    <tr id="row65971551418"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p646075601418"><a name="p646075601418"></a><a name="p646075601418"></a>Partition Calculator</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.2 "><div class="p" id="p203587582019"><a name="p203587582019"></a><a name="p203587582019"></a>Calculator used to calculate the estimated number of partitions based on the information you entered.<a name="ol03889271924"></a><a name="ol03889271924"></a><ol id="ol03889271924"><li>Click <strong id="b193881414191212"><a name="b193881414191212"></a><a name="b193881414191212"></a>Partition Calculator</strong>.</li><li>In the <strong id="b363025828104226"><a name="b363025828104226"></a><a name="b363025828104226"></a>Partition Calculator</strong> dialog box, configure the <strong id="b110349419104226"><a name="b110349419104226"></a><a name="b110349419104226"></a>Average Record Size (KB)</strong>, <strong id="b625601961104226"><a name="b625601961104226"></a><a name="b625601961104226"></a>Max. Records Written</strong>, and <strong id="b2057444388104226"><a name="b2057444388104226"></a><a name="b2057444388104226"></a>Consumer Applications</strong> parameters. The <strong id="b04809481248"><a name="b04809481248"></a><a name="b04809481248"></a>Estimated Partitions</strong> field then displays the recommended number of partitions. The value of this field cannot be modified.<div class="note" id="note0380722563"><a name="note0380722563"></a><a name="note0380722563"></a><span class="notetitle"> NOTE: </span><div class="notebody"><div class="p" id="p43809221865"><a name="p43809221865"></a><a name="p43809221865"></a>Partition calculation formulas:<a name="ul13223349162"></a><a name="ul13223349162"></a><ul id="ul13223349162"><li>Based on the traffic (the final value must be rounded up):<p id="p1292793683715"><a name="p1292793683715"></a><a name="p1292793683715"></a>Common stream: Average record size x (1 + 20%) x Maximum records written/ (1 x 1024 KB) (20% is the reserved partition percentage.)</p>
    <p id="p1611153718285"><a name="p1611153718285"></a><a name="p1611153718285"></a>Advanced stream: Average record size x (1 + 20%) x Maximum records written/ (5 x 1024 KB) (20% is the reserved partition percentage.)</p>
    </li><li>Based on the consumer program quantity (the final value must be rounded up): <p id="p2361623371"><a name="p2361623371"></a><a name="p2361623371"></a>(Number of consumer programs/2) x Number of partitions calculated based on the traffic (The result of the number of consumer programs/2 must reserve two decimals.)</p>
    <p id="p183221412162615"><a name="p183221412162615"></a><a name="p183221412162615"></a>The largest value among the values calculated based on the previous three formulas is considered as the estimated partition value.</p>
    </li></ul>
    </div>
    </div></div>
    </li><li>Click <strong id="b1445267158104413"><a name="b1445267158104413"></a><a name="b1445267158104413"></a>Use Estimated Value</strong>. The estimated value is automatically used as the value of <strong id="b209344337517"><a name="b209344337517"></a><a name="b209344337517"></a>Partitions</strong>.</li></ol>
    </div>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.2.4.1.3 "><p id="p306181991418"><a name="p306181991418"></a><a name="p306181991418"></a>-</p>
    </td>
    </tr>
    <tr id="row2057950714455"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p5497124314454"><a name="p5497124314454"></a><a name="p5497124314454"></a>Data Retention (hours)</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.2 "><p id="p25880564143452"><a name="p25880564143452"></a><a name="p25880564143452"></a>The maximum number of hours for which data can be preserved in DIS. Data will be deleted when the retention period expires.</p>
    <p id="p1238010993414"><a name="p1238010993414"></a><a name="p1238010993414"></a>Value range: an integer ranging from 24 to 72.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.2.4.1.3 "><p id="p2329645314454"><a name="p2329645314454"></a><a name="p2329645314454"></a>24</p>
    </td>
    </tr>
    <tr id="row12874732141417"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p1516161015226"><a name="p1516161015226"></a><a name="p1516161015226"></a>Configure</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.2 "><p id="p142241002214"><a name="p142241002214"></a><a name="p142241002214"></a>Click <span class="uicontrol" id="uicontrol17421434215"><a name="uicontrol17421434215"></a><a name="uicontrol17421434215"></a><b>Configure now</b></span>. The <strong id="b17768149424"><a name="b17768149424"></a><a name="b17768149424"></a>Tag</strong> parameter is displayed.</p>
    <p id="p85681029161817"><a name="p85681029161817"></a><a name="p85681029161817"></a>For details about how to add a tag, see <a href="managing-stream-tags.md">Managing Stream Tags</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.2.4.1.3 "><p id="p087463201415"><a name="p087463201415"></a><a name="p087463201415"></a>-</p>
    </td>
    </tr>
    <tr id="row119185814171"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p16331210132219"><a name="p16331210132219"></a><a name="p16331210132219"></a>Skip</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.2 "><p id="p1738121014228"><a name="p1738121014228"></a><a name="p1738121014228"></a>No advanced settings need to be configured.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.2.4.1.3 "><p id="p219158141716"><a name="p219158141716"></a><a name="p219158141716"></a>-</p>
    </td>
    </tr>
    <tr id="row421718362145"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p2795837192013"><a name="p2795837192013"></a><a name="p2795837192013"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0110219762_p4117414171914"><a name="en-us_topic_0110219762_p4117414171914"></a><a name="en-us_topic_0110219762_p4117414171914"></a>Identifier of the stream. Adding tags to streams can help you identify and manage your stream resources.</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.2.4.1.3 "><p id="p157951937162012"><a name="p157951937162012"></a><a name="p157951937162012"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **Buy Now**. The  **Details**  page is displayed.
5.  Click  **Submit**.

