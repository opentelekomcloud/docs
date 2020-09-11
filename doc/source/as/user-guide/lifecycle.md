# Lifecycle<a name="EN-US_TOPIC_0192950172"></a>

The lifecycle of an instance in an AS group starts when it is created and ends when it is removed from the AS group.

If you have not added a lifecycle hook to the AS group, the instance lifecycle changes as shown in  [Figure 1](#en-us_topic_0190954031_fig9892349365).

**Figure  1**  Instance lifecycle<a name="en-us_topic_0190954031_fig9892349365"></a>  
![](figures/instance-lifecycle.png "instance-lifecycle")

In trigger conditions 2 and 4, a scaling action is automatically triggered to change the instance status.

**Table  1**  Instance status

<a name="en-us_topic_0190954031_table58314838122115"></a>
<table><thead align="left"><tr id="en-us_topic_0190954031_row2761988122115"><th class="cellrowborder" valign="top" width="14.888511148885112%" id="mcps1.2.5.1.1"><p id="en-us_topic_0190954031_p223663122115"><a name="en-us_topic_0190954031_p223663122115"></a><a name="en-us_topic_0190954031_p223663122115"></a><strong id="b4449180193214"><a name="b4449180193214"></a><a name="b4449180193214"></a>Status</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.328267173282672%" id="mcps1.2.5.1.2"><p id="en-us_topic_0190954031_p18116763122115"><a name="en-us_topic_0190954031_p18116763122115"></a><a name="en-us_topic_0190954031_p18116763122115"></a><strong id="b191102081324"><a name="b191102081324"></a><a name="b191102081324"></a>Sub-item</strong></p>
</th>
<th class="cellrowborder" valign="top" width="32.03679632036797%" id="mcps1.2.5.1.3"><p id="en-us_topic_0190954031_p48878785162735"><a name="en-us_topic_0190954031_p48878785162735"></a><a name="en-us_topic_0190954031_p48878785162735"></a><strong id="b17720540123219"><a name="b17720540123219"></a><a name="b17720540123219"></a>Status Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="35.746425357464254%" id="mcps1.2.5.1.4"><p id="en-us_topic_0190954031_p41345704155647"><a name="en-us_topic_0190954031_p41345704155647"></a><a name="en-us_topic_0190954031_p41345704155647"></a><strong id="b12838104683211"><a name="b12838104683211"></a><a name="b12838104683211"></a>Trigger Condition</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0190954031_row3086574154529"><td class="cellrowborder" valign="top" width="14.888511148885112%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954031_p48685961154529"><a name="en-us_topic_0190954031_p48685961154529"></a><a name="en-us_topic_0190954031_p48685961154529"></a>Initial</p>
</td>
<td class="cellrowborder" valign="top" width="17.328267173282672%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954031_p51248781154529"><a name="en-us_topic_0190954031_p51248781154529"></a><a name="en-us_topic_0190954031_p51248781154529"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="32.03679632036797%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954031_p49739838162820"><a name="en-us_topic_0190954031_p49739838162820"></a><a name="en-us_topic_0190954031_p49739838162820"></a>The instance has not been added to an AS group.</p>
</td>
<td class="cellrowborder" rowspan="3" valign="top" width="35.746425357464254%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0190954031_p6433059915580"><a name="en-us_topic_0190954031_p6433059915580"></a><a name="en-us_topic_0190954031_p6433059915580"></a>The status of an instance is changed to <strong id="en-us_topic_0190954031_b84235270614229"><a name="en-us_topic_0190954031_b84235270614229"></a><a name="en-us_topic_0190954031_b84235270614229"></a>Adding to AS group</strong> when either of the following operations is performed:<a name="en-us_topic_0190954031_ul4210447915580"></a><a name="en-us_topic_0190954031_ul4210447915580"></a><ul id="en-us_topic_0190954031_ul4210447915580"><li>When you manually change the expected number of instances or a scaling condition is met, a scaling action is triggered to expand resources.</li><li>You manually add instances to the AS group.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0190954031_row43008980122115"><td class="cellrowborder" rowspan="2" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954031_p61175331122115"><a name="en-us_topic_0190954031_p61175331122115"></a><a name="en-us_topic_0190954031_p61175331122115"></a>Adding to AS group</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954031_p56254767122115"><a name="en-us_topic_0190954031_p56254767122115"></a><a name="en-us_topic_0190954031_p56254767122115"></a>Add an instance.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954031_p21556004162820"><a name="en-us_topic_0190954031_p21556004162820"></a><a name="en-us_topic_0190954031_p21556004162820"></a>When trigger condition 1 is met, AS adds the instance to expand the AS group capacity.</p>
</td>
</tr>
<tr id="en-us_topic_0190954031_row6209240122115"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954031_p3745972122115"><a name="en-us_topic_0190954031_p3745972122115"></a><a name="en-us_topic_0190954031_p3745972122115"></a>(Optional) Associate the instance with a load balancing listener.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954031_p10852798162820"><a name="en-us_topic_0190954031_p10852798162820"></a><a name="en-us_topic_0190954031_p10852798162820"></a>When trigger condition 1 is met, AS associates the created instance with the load balancing listener.</p>
</td>
</tr>
<tr id="en-us_topic_0190954031_row46459564122115"><td class="cellrowborder" valign="top" width="14.888511148885112%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954031_p5128363122115"><a name="en-us_topic_0190954031_p5128363122115"></a><a name="en-us_topic_0190954031_p5128363122115"></a>Enabled</p>
</td>
<td class="cellrowborder" valign="top" width="17.328267173282672%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954031_p12744254122115"><a name="en-us_topic_0190954031_p12744254122115"></a><a name="en-us_topic_0190954031_p12744254122115"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="32.03679632036797%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954031_p59952928162820"><a name="en-us_topic_0190954031_p59952928162820"></a><a name="en-us_topic_0190954031_p59952928162820"></a>The instance is added to the AS group and starts to process service traffic.</p>
</td>
<td class="cellrowborder" rowspan="3" valign="top" width="35.746425357464254%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0190954031_p35518063161151"><a name="en-us_topic_0190954031_p35518063161151"></a><a name="en-us_topic_0190954031_p35518063161151"></a>The instance status is changed from <strong id="en-us_topic_0190954031_b8423527061438"><a name="en-us_topic_0190954031_b8423527061438"></a><a name="en-us_topic_0190954031_b8423527061438"></a>Enabled</strong> to <strong id="en-us_topic_0190954031_b84235270614312"><a name="en-us_topic_0190954031_b84235270614312"></a><a name="en-us_topic_0190954031_b84235270614312"></a>Removing from AS group</strong> when any of the following operations are performed:<a name="en-us_topic_0190954031_ul51227112161151"></a><a name="en-us_topic_0190954031_ul51227112161151"></a><ul id="en-us_topic_0190954031_ul51227112161151"><li>When you manually change the expected number of instances or a scaling condition is met, a scaling action is triggered to reduce resources.</li><li>When a health check shows that an enabled instance is unhealthy, the instance is removed from the AS group.</li><li>You manually remove an instance from an AS group.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0190954031_row29538368122115"><td class="cellrowborder" rowspan="2" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954031_p43797589122115"><a name="en-us_topic_0190954031_p43797589122115"></a><a name="en-us_topic_0190954031_p43797589122115"></a>Removing from AS group</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954031_p57943835122115"><a name="en-us_topic_0190954031_p57943835122115"></a><a name="en-us_topic_0190954031_p57943835122115"></a>(Optional) Disassociate the instance from the load balancing listener.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954031_p17814630162820"><a name="en-us_topic_0190954031_p17814630162820"></a><a name="en-us_topic_0190954031_p17814630162820"></a>When trigger condition 3 is met, the AS group starts to reduce resources and disassociate the instance from the load balancing listener.</p>
</td>
</tr>
<tr id="en-us_topic_0190954031_row63808889123150"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954031_p25032235123150"><a name="en-us_topic_0190954031_p25032235123150"></a><a name="en-us_topic_0190954031_p25032235123150"></a>Remove the instance.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954031_p34854770162820"><a name="en-us_topic_0190954031_p34854770162820"></a><a name="en-us_topic_0190954031_p34854770162820"></a>After the instance is unbound from the load balancing listener, it is removed from the AS group.</p>
</td>
</tr>
<tr id="en-us_topic_0190954031_row44493857154932"><td class="cellrowborder" valign="top" width="14.888511148885112%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954031_p47232674154932"><a name="en-us_topic_0190954031_p47232674154932"></a><a name="en-us_topic_0190954031_p47232674154932"></a>Removed</p>
</td>
<td class="cellrowborder" valign="top" width="17.328267173282672%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954031_p641387154932"><a name="en-us_topic_0190954031_p641387154932"></a><a name="en-us_topic_0190954031_p641387154932"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="32.03679632036797%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954031_p41976750162820"><a name="en-us_topic_0190954031_p41976750162820"></a><a name="en-us_topic_0190954031_p41976750162820"></a>The instance lifecycle in the AS group ends.</p>
</td>
<td class="cellrowborder" valign="top" width="35.746425357464254%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0190954031_p8509637155647"><a name="en-us_topic_0190954031_p8509637155647"></a><a name="en-us_topic_0190954031_p8509637155647"></a>N/A</p>
</td>
</tr>
</tbody>
</table>

Instances are added to an AS group manually or through a scaling action. Then, they go through the  **Adding to AS group**,  **Enabled**, and  **Removing from AS group**  statuses, and are finally removed from the AS group.

If you have not added a lifecycle hook to the AS group, the instance lifecycle changes as shown in  [Figure 2](#en-us_topic_0190954031_fig32791162165412). When the AS group is performing a scaling action, instances are suspended by the lifecycle hook and remain in the waiting state until the timeout period ends or the user manually calls back the instances. You can perform desired operations during the waiting. For example, you can install or configure software on a newly added instance or download log files from an instance before it is removed. 

**Figure  2**  Instance lifecycle<a name="en-us_topic_0190954031_fig32791162165412"></a>  
![](figures/instance-lifecycle-0.png "instance-lifecycle-0")

In trigger conditions 2, 4, 6, and 8, a scaling action is automatically triggered to change the instance status.

**Table  2**  Instance status

<a name="en-us_topic_0190954031_table44806733123523"></a>
<table><thead align="left"><tr id="en-us_topic_0190954031_row12488715123523"><th class="cellrowborder" valign="top" width="17.32%" id="mcps1.2.5.1.1"><p id="en-us_topic_0190954031_p4953027123523"><a name="en-us_topic_0190954031_p4953027123523"></a><a name="en-us_topic_0190954031_p4953027123523"></a><strong id="b1111728175919"><a name="b1111728175919"></a><a name="b1111728175919"></a>Status</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.7%" id="mcps1.2.5.1.2"><p id="en-us_topic_0190954031_p65650891123523"><a name="en-us_topic_0190954031_p65650891123523"></a><a name="en-us_topic_0190954031_p65650891123523"></a><strong id="b4595103615919"><a name="b4595103615919"></a><a name="b4595103615919"></a>Sub-status</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.549999999999997%" id="mcps1.2.5.1.3"><p id="en-us_topic_0190954031_p16121931123523"><a name="en-us_topic_0190954031_p16121931123523"></a><a name="en-us_topic_0190954031_p16121931123523"></a><strong id="b177271242185913"><a name="b177271242185913"></a><a name="b177271242185913"></a>Status Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="35.43%" id="mcps1.2.5.1.4"><p id="en-us_topic_0190954031_p61546087163046"><a name="en-us_topic_0190954031_p61546087163046"></a><a name="en-us_topic_0190954031_p61546087163046"></a><strong id="b2212352175918"><a name="b2212352175918"></a><a name="b2212352175918"></a>Trigger Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0190954031_row44048139155326"><td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954031_p55335857155343"><a name="en-us_topic_0190954031_p55335857155343"></a><a name="en-us_topic_0190954031_p55335857155343"></a>Initial</p>
</td>
<td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954031_p53019407155343"><a name="en-us_topic_0190954031_p53019407155343"></a><a name="en-us_topic_0190954031_p53019407155343"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="29.549999999999997%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954031_p66713541155343"><a name="en-us_topic_0190954031_p66713541155343"></a><a name="en-us_topic_0190954031_p66713541155343"></a>The instance has not been added to an AS group.</p>
</td>
<td class="cellrowborder" rowspan="2" valign="top" width="35.43%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0190954031_p6275314916349"><a name="en-us_topic_0190954031_p6275314916349"></a><a name="en-us_topic_0190954031_p6275314916349"></a>The status of an instance is changed to <strong id="b564662505"><a name="b564662505"></a><a name="b564662505"></a>Adding to AS group</strong> when either of the following operations is performed:<a name="en-us_topic_0190954031_ul2790743316349"></a><a name="en-us_topic_0190954031_ul2790743316349"></a><ul id="en-us_topic_0190954031_ul2790743316349"><li>When you manually change the expected number of instances or a scaling condition is met, a scaling action is triggered to expand resources.</li><li>You manually add instances to the AS group.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0190954031_row36403380123523"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954031_p62992638123523"><a name="en-us_topic_0190954031_p62992638123523"></a><a name="en-us_topic_0190954031_p62992638123523"></a>Adding to AS group</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954031_p2130036123523"><a name="en-us_topic_0190954031_p2130036123523"></a><a name="en-us_topic_0190954031_p2130036123523"></a>Add the instance.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954031_p10186492154034"><a name="en-us_topic_0190954031_p10186492154034"></a><a name="en-us_topic_0190954031_p10186492154034"></a>When trigger condition 1 is met, AS adds the instance to expand the AS group capacity.</p>
</td>
</tr>
<tr id="en-us_topic_0190954031_row63642540123523"><td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954031_p54772121123523"><a name="en-us_topic_0190954031_p54772121123523"></a><a name="en-us_topic_0190954031_p54772121123523"></a>Wait (Adding to AS group)</p>
</td>
<td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954031_p7356835123523"><a name="en-us_topic_0190954031_p7356835123523"></a><a name="en-us_topic_0190954031_p7356835123523"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="29.549999999999997%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954031_p59032753123523"><a name="en-us_topic_0190954031_p59032753123523"></a><a name="en-us_topic_0190954031_p59032753123523"></a>The lifecycle hook suspends the instance that is being added to the AS group and sets the instance to be in waiting state.</p>
</td>
<td class="cellrowborder" rowspan="2" valign="top" width="35.43%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0190954031_p1010873018757"><a name="en-us_topic_0190954031_p1010873018757"></a><a name="en-us_topic_0190954031_p1010873018757"></a>The instance status is changed from <strong id="b1807733970"><a name="b1807733970"></a><a name="b1807733970"></a>Wait (Adding to AS group)</strong> to <strong id="b715365286"><a name="b715365286"></a><a name="b715365286"></a>Adding to AS group</strong> when either of the following operations is performed:<a name="en-us_topic_0190954031_ul5016346818818"></a><a name="en-us_topic_0190954031_ul5016346818818"></a><ul id="en-us_topic_0190954031_ul5016346818818"><li>The default callback action is performed.</li><li>You manually perform the callback action.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0190954031_row61532733123523"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954031_p18095501123523"><a name="en-us_topic_0190954031_p18095501123523"></a><a name="en-us_topic_0190954031_p18095501123523"></a>Adding to AS group</p>
<p id="en-us_topic_0190954031_p28641787123523"><a name="en-us_topic_0190954031_p28641787123523"></a><a name="en-us_topic_0190954031_p28641787123523"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954031_p38283399123523"><a name="en-us_topic_0190954031_p38283399123523"></a><a name="en-us_topic_0190954031_p38283399123523"></a>(Optional) Associate the instance with a load balancing listener.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954031_p2636777316478"><a name="en-us_topic_0190954031_p2636777316478"></a><a name="en-us_topic_0190954031_p2636777316478"></a>When trigger condition 3 is met, AS associates the instance with the load balancing listener.</p>
</td>
</tr>
<tr id="en-us_topic_0190954031_row5043122123523"><td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954031_p5839748123523"><a name="en-us_topic_0190954031_p5839748123523"></a><a name="en-us_topic_0190954031_p5839748123523"></a>Enabled</p>
</td>
<td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954031_p3257603123523"><a name="en-us_topic_0190954031_p3257603123523"></a><a name="en-us_topic_0190954031_p3257603123523"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="29.549999999999997%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954031_p62539286123523"><a name="en-us_topic_0190954031_p62539286123523"></a><a name="en-us_topic_0190954031_p62539286123523"></a>The instance is added to the AS group and starts to process service traffic.</p>
</td>
<td class="cellrowborder" rowspan="2" valign="top" width="35.43%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0190954031_p34805667163440"><a name="en-us_topic_0190954031_p34805667163440"></a><a name="en-us_topic_0190954031_p34805667163440"></a>The instance status is changed from <strong id="b1625953503"><a name="b1625953503"></a><a name="b1625953503"></a>Enabled</strong> to <strong id="b27763235"><a name="b27763235"></a><a name="b27763235"></a>Removing from AS group</strong> when any of the following operations are performed:<a name="en-us_topic_0190954031_ul44815551163440"></a><a name="en-us_topic_0190954031_ul44815551163440"></a><ul id="en-us_topic_0190954031_ul44815551163440"><li>When you manually change the expected number of instances or a scaling condition is met, a scaling action is triggered to reduce resources.</li><li>When a health check shows that an enabled instance is unhealthy, the instance is removed from the AS group.</li><li>You manually remove an instance from an AS group.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0190954031_row4457222412386"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954031_p5358038112386"><a name="en-us_topic_0190954031_p5358038112386"></a><a name="en-us_topic_0190954031_p5358038112386"></a>Removing from AS group</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954031_p4504358612386"><a name="en-us_topic_0190954031_p4504358612386"></a><a name="en-us_topic_0190954031_p4504358612386"></a>(Optional) Disassociate the instance from the load balancing listener.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954031_p133616815419"><a name="en-us_topic_0190954031_p133616815419"></a><a name="en-us_topic_0190954031_p133616815419"></a>When trigger condition 5 is met, the AS group starts to reduce resources and disassociate the instance from the load balancing listener.</p>
</td>
</tr>
<tr id="en-us_topic_0190954031_row13234780123848"><td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954031_p65384237123848"><a name="en-us_topic_0190954031_p65384237123848"></a><a name="en-us_topic_0190954031_p65384237123848"></a>Wait (Removing from AS group)</p>
</td>
<td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954031_p61631876123848"><a name="en-us_topic_0190954031_p61631876123848"></a><a name="en-us_topic_0190954031_p61631876123848"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="29.549999999999997%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954031_p26126022123848"><a name="en-us_topic_0190954031_p26126022123848"></a><a name="en-us_topic_0190954031_p26126022123848"></a>The lifecycle hook suspends the instance that is being removed from the AS group and sets the instance to be in waiting state.</p>
</td>
<td class="cellrowborder" rowspan="2" valign="top" width="35.43%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0190954031_p45158251181620"><a name="en-us_topic_0190954031_p45158251181620"></a><a name="en-us_topic_0190954031_p45158251181620"></a>The instance status is changed from <strong id="b1942795081"><a name="b1942795081"></a><a name="b1942795081"></a>Wait (Removing from AS group)</strong> to <strong id="b948639311"><a name="b948639311"></a><a name="b948639311"></a>Removing from AS group</strong> when either of the following operations is performed:<a name="en-us_topic_0190954031_ul4346242181746"></a><a name="en-us_topic_0190954031_ul4346242181746"></a><ul id="en-us_topic_0190954031_ul4346242181746"><li>The default callback action is performed.</li><li>You manually perform the callback action.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0190954031_row17111799123913"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954031_p43878479123913"><a name="en-us_topic_0190954031_p43878479123913"></a><a name="en-us_topic_0190954031_p43878479123913"></a>Removing from AS group</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954031_p64495924123913"><a name="en-us_topic_0190954031_p64495924123913"></a><a name="en-us_topic_0190954031_p64495924123913"></a>Remove the instance.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954031_p56787341123913"><a name="en-us_topic_0190954031_p56787341123913"></a><a name="en-us_topic_0190954031_p56787341123913"></a>When trigger condition 7 is met, AS removes the instance from the AS group.</p>
</td>
</tr>
<tr id="en-us_topic_0190954031_row8482253155454"><td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954031_p16400190155511"><a name="en-us_topic_0190954031_p16400190155511"></a><a name="en-us_topic_0190954031_p16400190155511"></a>Removed</p>
</td>
<td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954031_p53347033155511"><a name="en-us_topic_0190954031_p53347033155511"></a><a name="en-us_topic_0190954031_p53347033155511"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="29.549999999999997%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954031_p26142429155511"><a name="en-us_topic_0190954031_p26142429155511"></a><a name="en-us_topic_0190954031_p26142429155511"></a>The instance lifecycle in the AS group ends.</p>
</td>
<td class="cellrowborder" valign="top" width="35.43%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0190954031_p13332350163046"><a name="en-us_topic_0190954031_p13332350163046"></a><a name="en-us_topic_0190954031_p13332350163046"></a>N/A</p>
</td>
</tr>
</tbody>
</table>

Instances are added to an AS group manually or through a scaling action. Then, they go through the  **Adding to AS group**,  **Wait \(Adding to AS group\)**,  **Adding to AS group**,  **Enabled**,  **Removing from AS group**,  **Wait \(Removing from the AS group\)**, and  **Removing from AS group**  and are finally removed from the AS group.

