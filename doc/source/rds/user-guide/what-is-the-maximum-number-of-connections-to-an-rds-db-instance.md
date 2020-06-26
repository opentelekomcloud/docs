# What Is the Maximum Number of Connections to an RDS DB Instance?<a name="rds_faq_0055"></a>

RDS does not have constraints on the number of connections. This number is determined by the default value and value range of the DB engine. For example, you can set  **max\_connections**  and  **max\_user\_connections**  in a parameter template to configure the maximum number of connections for an RDS MySQL DB instance.

## About max\_connections<a name="section164061146172516"></a>

The max\_connections is closely related to storage space \(unit: GB\) of the DB instance.

Estimated max\_connections = Available node memory/Estimated memory occupied by a single connection

>![](/images/icon-note.gif) **NOTE:**   
>-   Available node memory = Total memory – Memory occupied by the buffer pool – 1 GB \(mysqld process/OS/monitoring program\)  
>-   Estimated memory usage of a single connection \(single\_thread\_memory\) = thread\_stack \(256K\) + binlog\_cache\_size \(32K\) + join\_buffer\_size \(256K\) + sort\_buffer\_size \(256K\) + read\_buffer\_size \(128K\) + read\_rnd\_buffer\_size \(256K\) = 1 MB  

The following table lists the default values of  **max\_connections**  for different memory specifications.

**Table  1**  Max\_connection values for different memory specifications

<a name="table167335205291"></a>
<table><thead align="left"><tr id="row273372012295"><th class="cellrowborder" valign="top" width="46.78%" id="mcps1.2.3.1.1"><p id="p51186704165712"><a name="p51186704165712"></a><a name="p51186704165712"></a><strong id="b16913205614139"><a name="b16913205614139"></a><a name="b16913205614139"></a>Memory (GB)</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.22%" id="mcps1.2.3.1.2"><p id="p52482393165712"><a name="p52482393165712"></a><a name="p52482393165712"></a><strong id="b3382126101420"><a name="b3382126101420"></a><a name="b3382126101420"></a>Connections</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row8205956376"><td class="cellrowborder" valign="top" width="46.78%" headers="mcps1.2.3.1.1 "><p id="p16552181015310"><a name="p16552181015310"></a><a name="p16552181015310"></a>512</p>
</td>
<td class="cellrowborder" valign="top" width="53.22%" headers="mcps1.2.3.1.2 "><p id="p14345145216293"><a name="p14345145216293"></a><a name="p14345145216293"></a>100000</p>
</td>
</tr>
<tr id="row167551215173717"><td class="cellrowborder" valign="top" width="46.78%" headers="mcps1.2.3.1.1 "><p id="p873462012910"><a name="p873462012910"></a><a name="p873462012910"></a>384</p>
</td>
<td class="cellrowborder" valign="top" width="53.22%" headers="mcps1.2.3.1.2 "><p id="p11345195222919"><a name="p11345195222919"></a><a name="p11345195222919"></a>80000</p>
</td>
</tr>
<tr id="row1392813153815"><td class="cellrowborder" valign="top" width="46.78%" headers="mcps1.2.3.1.1 "><p id="p173462017290"><a name="p173462017290"></a><a name="p173462017290"></a>256</p>
</td>
<td class="cellrowborder" valign="top" width="53.22%" headers="mcps1.2.3.1.2 "><p id="p934525212918"><a name="p934525212918"></a><a name="p934525212918"></a>60000</p>
</td>
</tr>
<tr id="row722119406210"><td class="cellrowborder" valign="top" width="46.78%" headers="mcps1.2.3.1.1 "><p id="p178589411923"><a name="p178589411923"></a><a name="p178589411923"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="53.22%" headers="mcps1.2.3.1.2 "><p id="p88582411126"><a name="p88582411126"></a><a name="p88582411126"></a>30000</p>
</td>
</tr>
<tr id="row14593122933812"><td class="cellrowborder" valign="top" width="46.78%" headers="mcps1.2.3.1.1 "><p id="p917217512331"><a name="p917217512331"></a><a name="p917217512331"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="53.22%" headers="mcps1.2.3.1.2 "><p id="p53459527299"><a name="p53459527299"></a><a name="p53459527299"></a>18000</p>
</td>
</tr>
<tr id="row3419121033810"><td class="cellrowborder" valign="top" width="46.78%" headers="mcps1.2.3.1.1 "><p id="p273419206296"><a name="p273419206296"></a><a name="p273419206296"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="53.22%" headers="mcps1.2.3.1.2 "><p id="p834575215297"><a name="p834575215297"></a><a name="p834575215297"></a>10000</p>
</td>
</tr>
<tr id="row17733122042916"><td class="cellrowborder" valign="top" width="46.78%" headers="mcps1.2.3.1.1 "><p id="p187331420152920"><a name="p187331420152920"></a><a name="p187331420152920"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="53.22%" headers="mcps1.2.3.1.2 "><p id="p5345135219291"><a name="p5345135219291"></a><a name="p5345135219291"></a>5000</p>
</td>
</tr>
<tr id="row14109145020389"><td class="cellrowborder" valign="top" width="46.78%" headers="mcps1.2.3.1.1 "><p id="p16578142103315"><a name="p16578142103315"></a><a name="p16578142103315"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="53.22%" headers="mcps1.2.3.1.2 "><p id="p195786273311"><a name="p195786273311"></a><a name="p195786273311"></a>2500</p>
</td>
</tr>
<tr id="row20583182273815"><td class="cellrowborder" valign="top" width="46.78%" headers="mcps1.2.3.1.1 "><p id="p20734102072911"><a name="p20734102072911"></a><a name="p20734102072911"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="53.22%" headers="mcps1.2.3.1.2 "><p id="p16345852132918"><a name="p16345852132918"></a><a name="p16345852132918"></a>1500</p>
</td>
</tr>
<tr id="row19733132010292"><td class="cellrowborder" valign="top" width="46.78%" headers="mcps1.2.3.1.1 "><p id="p1973312017299"><a name="p1973312017299"></a><a name="p1973312017299"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="53.22%" headers="mcps1.2.3.1.2 "><p id="p11345252102912"><a name="p11345252102912"></a><a name="p11345252102912"></a>800</p>
</td>
</tr>
</tbody>
</table>

