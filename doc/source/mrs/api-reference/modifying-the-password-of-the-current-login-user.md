# Modifying the Password of the Current Login User<a name="EN-US_TOPIC_0220024727"></a>

## Function<a name="en-us_topic_0125376205_section1656417305558"></a>

This API is used to change the password of the current login user. This API can be used only by security clusters that support Kerberos authentication.

## URI<a name="en-us_topic_0125376205_sc9d330ebf874400aaecc23abdde57478"></a>

-   Format

POST /web/v1/access/modify\_self\_password

-   Parameter description

<a name="en-us_topic_0125376205_en-us_topic_0110839912_table47282592"></a>
<table><thead align="left"><tr id="en-us_topic_0125376205_en-us_topic_0110839912_row45150877"><th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.1"><p id="en-us_topic_0125376205_en-us_topic_0110839912_p33342387"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p33342387"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p33342387"></a><strong id="en-us_topic_0125376205_b162774213314533_1"><a name="en-us_topic_0125376205_b162774213314533_1"></a><a name="en-us_topic_0125376205_b162774213314533_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.2"><p id="en-us_topic_0125376205_en-us_topic_0110839912_p16378826"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p16378826"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p16378826"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="49.08%" id="mcps1.1.4.1.3"><p id="en-us_topic_0125376205_en-us_topic_0110839912_p52256971"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p52256971"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p52256971"></a><strong id="en-us_topic_0125376205_b842352706134712"><a name="en-us_topic_0125376205_b842352706134712"></a><a name="en-us_topic_0125376205_b842352706134712"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376205_en-us_topic_0110839912_row4956220"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376205_en-us_topic_0110839912_p65909534"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p65909534"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p65909534"></a>old_password</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376205_en-us_topic_0110839912_p37072024"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p37072024"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p37072024"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376205_en-us_topic_0110839912_p49815831"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p49815831"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p49815831"></a>Old password</p>
</td>
</tr>
<tr id="en-us_topic_0125376205_en-us_topic_0110839912_row45689298"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376205_en-us_topic_0110839912_p9845638"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p9845638"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p9845638"></a>new_password</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376205_en-us_topic_0110839912_p59299207"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p59299207"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p59299207"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376205_en-us_topic_0110839912_p53276198"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p53276198"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p53276198"></a>New password</p>
</td>
</tr>
<tr id="en-us_topic_0125376205_en-us_topic_0110839912_row9723740"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376205_en-us_topic_0110839912_p49425452"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p49425452"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p49425452"></a>confirm_password</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376205_en-us_topic_0110839912_p44038685"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p44038685"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p44038685"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376205_en-us_topic_0110839912_p22074310"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p22074310"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p22074310"></a>Confirm password</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0125376205_section72641738175810"></a>

-   Example:

    ```
    POST /web/v1/access/modify_self_password?old_password=null&new_password=null& confirm_password=null HTTP/1.1
    Host: example.com
    Content-Type: application/json
    Accept:application/json
    ```


-   Parameter description

    None


## Response<a name="en-us_topic_0125376205_s73422f750f424cfa8968c03323c498d5"></a>

-   Example:

    ```
    HTTP/1.1 200 OK
    Data:Wed,02 May 2018 10:10:01 GMT
    Server: example-server
    Content-Type: application/json
    {
      "int_result_code": 0,
      "result_desc": "string"
    }
    ```

-   Parameter description

<a name="en-us_topic_0125376205_en-us_topic_0110839912_table41167797"></a>
<table><thead align="left"><tr id="en-us_topic_0125376205_en-us_topic_0110839912_row19777822"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.1.5.1.1"><p id="en-us_topic_0125376205_en-us_topic_0110839912_p58499767"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p58499767"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p58499767"></a><strong id="en-us_topic_0125376205_b7617970162543"><a name="en-us_topic_0125376205_b7617970162543"></a><a name="en-us_topic_0125376205_b7617970162543"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.1.5.1.2"><p id="en-us_topic_0125376205_en-us_topic_0110839912_p40860656"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p40860656"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p40860656"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.1.5.1.3"><p id="en-us_topic_0125376205_en-us_topic_0110839912_p21378801"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p21378801"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p21378801"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.1.5.1.4"><p id="en-us_topic_0125376205_en-us_topic_0110839912_p40932280"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p40932280"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p40932280"></a><strong id="en-us_topic_0125376205_b842352706134712_1"><a name="en-us_topic_0125376205_b842352706134712_1"></a><a name="en-us_topic_0125376205_b842352706134712_1"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376205_en-us_topic_0110839912_row27180396"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376205_en-us_topic_0110839912_p54128431"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p54128431"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p54128431"></a>int_result_code</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376205_en-us_topic_0110839912_p22326828"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p22326828"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p22326828"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376205_en-us_topic_0110839912_p63642633"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p63642633"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p63642633"></a>INTEGER</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376205_en-us_topic_0110839912_p41190130"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p41190130"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p41190130"></a>Code of the return result</p>
</td>
</tr>
<tr id="en-us_topic_0125376205_en-us_topic_0110839912_row35166858"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376205_en-us_topic_0110839912_p29943281"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p29943281"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p29943281"></a>result_desc</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376205_en-us_topic_0110839912_p9486659"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p9486659"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p9486659"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376205_en-us_topic_0110839912_p30221930"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p30221930"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p30221930"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376205_en-us_topic_0110839912_p8729451"><a name="en-us_topic_0125376205_en-us_topic_0110839912_p8729451"></a><a name="en-us_topic_0125376205_en-us_topic_0110839912_p8729451"></a>Description of the return result</p>
</td>
</tr>
</tbody>
</table>

## Status Code<a name="en-us_topic_0125376205_section2092982712508"></a>

<a name="en-us_topic_0125376205_table2979011121511"></a>
<table><thead align="left"><tr id="en-us_topic_0125376205_row3981161161515"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.3.1.1"><p id="en-us_topic_0125376205_p398115116158"><a name="en-us_topic_0125376205_p398115116158"></a><a name="en-us_topic_0125376205_p398115116158"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83%" id="mcps1.1.3.1.2"><p id="en-us_topic_0125376205_p1798121191515"><a name="en-us_topic_0125376205_p1798121191515"></a><a name="en-us_topic_0125376205_p1798121191515"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376205_row69813112155"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0125376205_p15667142018546"><a name="en-us_topic_0125376205_p15667142018546"></a><a name="en-us_topic_0125376205_p15667142018546"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0125376205_p69861225163419"><a name="en-us_topic_0125376205_p69861225163419"></a><a name="en-us_topic_0125376205_p69861225163419"></a>The operation is successful.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

