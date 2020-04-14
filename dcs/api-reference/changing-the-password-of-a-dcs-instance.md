# Changing the Password of a DCS Instance<a name="EN-US_TOPIC_0237964366"></a>

## Function<a name="section10930096"></a>

This API is used to change the password of a DCS instance.

## URI<a name="section31262001"></a>

-   URI format:

    PUT /v1.0/\{project\_id\}/instances/\{instance\_id\}/password

-   Parameter description:

    [Table 1](#table657479)  describes the parameters of this API.


**Table  1**  Parameter description

<a name="table657479"></a>
<table><thead align="left"><tr id="row25084465"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p18575747"><a name="p18575747"></a><a name="p18575747"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p28240554"><a name="p28240554"></a><a name="p28240554"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p5783566"><a name="p5783566"></a><a name="p5783566"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p65815702"><a name="p65815702"></a><a name="p65815702"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row29471659"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p38394164"><a name="p38394164"></a><a name="p38394164"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p22919578"><a name="p22919578"></a><a name="p22919578"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p44546500"><a name="p44546500"></a><a name="p44546500"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p51496730"><a name="p51496730"></a><a name="p51496730"></a>Project ID.</p>
</td>
</tr>
<tr id="row60817394"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p27261878"><a name="p27261878"></a><a name="p27261878"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p60728539"><a name="p60728539"></a><a name="p60728539"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p20064649"><a name="p20064649"></a><a name="p20064649"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p14623847"><a name="p14623847"></a><a name="p14623847"></a>DCS instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section12922556"></a>

-   Request parameter:

    [Table 2](#table5917317)  describes request parameters.


**Table  2**  Parameter description

<a name="table5917317"></a>
<table><thead align="left"><tr id="row53632486"><th class="cellrowborder" valign="top" width="20.2020202020202%" id="mcps1.2.5.1.1"><p id="p49264104"><a name="p49264104"></a><a name="p49264104"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.2"><p id="p30969474"><a name="p30969474"></a><a name="p30969474"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.3"><p id="p25499485"><a name="p25499485"></a><a name="p25499485"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="45.45454545454545%" id="mcps1.2.5.1.4"><p id="p52192417"><a name="p52192417"></a><a name="p52192417"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row66836212"><td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.2.5.1.1 "><p id="p45024129"><a name="p45024129"></a><a name="p45024129"></a>old_password</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p23075822"><a name="p23075822"></a><a name="p23075822"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="p57202275"><a name="p57202275"></a><a name="p57202275"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454545%" headers="mcps1.2.5.1.4 "><p id="p2872713"><a name="p2872713"></a><a name="p2872713"></a>Old password.</p>
</td>
</tr>
<tr id="row25854422"><td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.2.5.1.1 "><p id="p13833415"><a name="p13833415"></a><a name="p13833415"></a>new_password</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p46764862"><a name="p46764862"></a><a name="p46764862"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="p29857440"><a name="p29857440"></a><a name="p29857440"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454545%" headers="mcps1.2.5.1.4 "><p id="p2533591"><a name="p2533591"></a><a name="p2533591"></a>New password.</p>
<p id="p22802326"><a name="p22802326"></a><a name="p22802326"></a>Password complexity requirements:</p>
<a name="ul3894347"></a><a name="ul3894347"></a><ul id="ul3894347"><li>A string of 8–32 characters.</li><li>Must be different from the old password.</li><li>Contains at least three of the following character types:<a name="ul49445640"></a><a name="ul49445640"></a><ul id="ul49445640"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters (`~!@#$%^&amp;*()-_=+\|[{}]:'",&lt;.&gt;/?)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

-   Example request:

    ```
    { 
     "old_password": "XXXXXX", 
     "new_password": "XXXXXX" 
    }
    ```


## Response<a name="section49194147"></a>

-   Status code:

    If status code "200 OK" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    [Table 3](#table53255854)  describes response parameters.


**Table  3**  Parameter description

<a name="table53255854"></a>
<table><thead align="left"><tr id="row23298728"><th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.4.1.1"><p id="p8148840"><a name="p8148840"></a><a name="p8148840"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.4.1.2"><p id="p56076321"><a name="p56076321"></a><a name="p56076321"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.57575757575758%" id="mcps1.2.4.1.3"><p id="p45888122"><a name="p45888122"></a><a name="p45888122"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row25950363"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="p21604653"><a name="p21604653"></a><a name="p21604653"></a>result</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.2 "><p id="p5146455"><a name="p5146455"></a><a name="p5146455"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.57575757575758%" headers="mcps1.2.4.1.3 "><p id="p14209730"><a name="p14209730"></a><a name="p14209730"></a>An indicator of whether the password is successfully changed:</p>
<p id="p60778711"><a name="p60778711"></a><a name="p60778711"></a>Options:</p>
<a name="ul10137494"></a><a name="ul10137494"></a><ul id="ul10137494"><li><strong id="b15830649"><a name="b15830649"></a><a name="b15830649"></a>Success</strong>: The password is successfully changed.</li><li><strong id="b7214230"><a name="b7214230"></a><a name="b7214230"></a>passwordFailed</strong>: The old password is incorrect.</li><li><strong id="b47481747"><a name="b47481747"></a><a name="b47481747"></a>Locked</strong>: This account has been locked.</li><li><strong id="b20816280"><a name="b20816280"></a><a name="b20816280"></a>Failed</strong>: Failed to change the password.</li></ul>
</td>
</tr>
<tr id="row53128798"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="p8465347"><a name="p8465347"></a><a name="p8465347"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.2 "><p id="p14604484"><a name="p14604484"></a><a name="p14604484"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.57575757575758%" headers="mcps1.2.4.1.3 "><p id="p42112587"><a name="p42112587"></a><a name="p42112587"></a>Error message.</p>
</td>
</tr>
<tr id="row43468963"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="p31325099"><a name="p31325099"></a><a name="p31325099"></a>retry_times_left</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.2 "><p id="p54305067"><a name="p54305067"></a><a name="p54305067"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.57575757575758%" headers="mcps1.2.4.1.3 "><p id="p36634316"><a name="p36634316"></a><a name="p36634316"></a>Number of remaining password attempts.</p>
</td>
</tr>
<tr id="row61273392"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="p64197733"><a name="p64197733"></a><a name="p64197733"></a>lock_time</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.2 "><p id="p32633870"><a name="p32633870"></a><a name="p32633870"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.57575757575758%" headers="mcps1.2.4.1.3 "><p id="p26097812"><a name="p26097812"></a><a name="p26097812"></a>Account lockout duration.</p>
</td>
</tr>
<tr id="row33553717"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="p33496528"><a name="p33496528"></a><a name="p33496528"></a>lock_time_left</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.2 "><p id="p28864252"><a name="p28864252"></a><a name="p28864252"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.57575757575758%" headers="mcps1.2.4.1.3 "><p id="p56303072"><a name="p56303072"></a><a name="p56303072"></a>Remaining time before the account is unlocked.</p>
</td>
</tr>
</tbody>
</table>

-   Example response:

    ```
    //Change password successful. 
    { 
     "result" : "success", 
     "message" : "Modify DCSInstance password success.", 
     "retry_times_left" : "5", 
     "lock_time" : "0", 
     "lock_time_left" : "0" 
    } 
    //Change password failed. 
    { 
     "result" : "passwordFailed", 
     "message" : "verify password failed.", 
     "retry_times_left" : "4", 
     "lock_time" : "5", 
     "lock_time_left" : "5" 
    }
    ```


