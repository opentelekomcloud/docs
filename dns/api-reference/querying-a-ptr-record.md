# Querying a PTR Record<a name="EN-US_TOPIC_0042318614"></a>

## Function<a name="section18389930"></a>

Query the PTR record of an EIP.

## URI<a name="section31291646"></a>

-   URI format

    GET /v2/reverse/floatingips/\{region\}:\{floatingip\_id\}

-   Parameter description

    **Table  1**  Parameters in the URI

    <a name="table21421675"></a><table><thead align="left"><tr id="en-us_topic_0042318613_row3442661918149"><th class="cellrowborder" valign="top" width="20.380000000000003%" id="mcps1.2.5.1.1"><p id="en-us_topic_0042318613_p3709279118149"><a name="en-us_topic_0042318613_p3709279118149"></a><a name="en-us_topic_0042318613_p3709279118149"></a><strong id="en-us_topic_0042318613_b162774213314533"><a name="en-us_topic_0042318613_b162774213314533"></a><a name="en-us_topic_0042318613_b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.439999999999998%" id="mcps1.2.5.1.2"><p id="en-us_topic_0042318613_p5172606218149"><a name="en-us_topic_0042318613_p5172606218149"></a><a name="en-us_topic_0042318613_p5172606218149"></a><strong id="en-us_topic_0042318613_b593421527191713"><a name="en-us_topic_0042318613_b593421527191713"></a><a name="en-us_topic_0042318613_b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.59%" id="mcps1.2.5.1.3"><p id="en-us_topic_0042318613_p2906151418149"><a name="en-us_topic_0042318613_p2906151418149"></a><a name="en-us_topic_0042318613_p2906151418149"></a><strong id="en-us_topic_0042318613_b84235270619112"><a name="en-us_topic_0042318613_b84235270619112"></a><a name="en-us_topic_0042318613_b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.589999999999996%" id="mcps1.2.5.1.4"><p id="en-us_topic_0042318613_p517246718149"><a name="en-us_topic_0042318613_p517246718149"></a><a name="en-us_topic_0042318613_p517246718149"></a><strong id="en-us_topic_0042318613_b842352706112423"><a name="en-us_topic_0042318613_b842352706112423"></a><a name="en-us_topic_0042318613_b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0042318613_row1631668818149"><td class="cellrowborder" valign="top" width="20.380000000000003%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0042318613_p4658337018149"><a name="en-us_topic_0042318613_p4658337018149"></a><a name="en-us_topic_0042318613_p4658337018149"></a>region</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0042318613_p1515661618149"><a name="en-us_topic_0042318613_p1515661618149"></a><a name="en-us_topic_0042318613_p1515661618149"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.59%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0042318613_p1972638718149"><a name="en-us_topic_0042318613_p1972638718149"></a><a name="en-us_topic_0042318613_p1972638718149"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.589999999999996%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0042318613_p5433349018149"><a name="en-us_topic_0042318613_p5433349018149"></a><a name="en-us_topic_0042318613_p5433349018149"></a>Region of the tenant</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042318613_row1923936518149"><td class="cellrowborder" valign="top" width="20.380000000000003%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0042318613_p1488470218149"><a name="en-us_topic_0042318613_p1488470218149"></a><a name="en-us_topic_0042318613_p1488470218149"></a>floatingip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0042318613_p6481017518149"><a name="en-us_topic_0042318613_p6481017518149"></a><a name="en-us_topic_0042318613_p6481017518149"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.59%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0042318613_p1513281718149"><a name="en-us_topic_0042318613_p1513281718149"></a><a name="en-us_topic_0042318613_p1513281718149"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.589999999999996%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0042318613_p1779865118149"><a name="en-us_topic_0042318613_p1779865118149"></a><a name="en-us_topic_0042318613_p1779865118149"></a>EIP ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section13189358"></a>

None

## Response<a name="section51595365"></a>

-   Parameter description

    **Table  2**  Parameters in the response

    <a name="table28278595"></a><table><thead align="left"><tr id="en-us_topic_0042318613_row5725206118456"><th class="cellrowborder" valign="top" width="18.37%" id="mcps1.2.4.1.1"><p id="en-us_topic_0042318613_p690539418456"><a name="en-us_topic_0042318613_p690539418456"></a><a name="en-us_topic_0042318613_p690539418456"></a><strong id="en-us_topic_0042318613_b162774213314533_1"><a name="en-us_topic_0042318613_b162774213314533_1"></a><a name="en-us_topic_0042318613_b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.87%" id="mcps1.2.4.1.2"><p id="en-us_topic_0042318613_p2246606418456"><a name="en-us_topic_0042318613_p2246606418456"></a><a name="en-us_topic_0042318613_p2246606418456"></a><strong id="en-us_topic_0042318613_b84235270619112_1"><a name="en-us_topic_0042318613_b84235270619112_1"></a><a name="en-us_topic_0042318613_b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="66.75999999999999%" id="mcps1.2.4.1.3"><p id="en-us_topic_0042318613_p781187018456"><a name="en-us_topic_0042318613_p781187018456"></a><a name="en-us_topic_0042318613_p781187018456"></a><strong id="en-us_topic_0042318613_b842352706112423_1"><a name="en-us_topic_0042318613_b842352706112423_1"></a><a name="en-us_topic_0042318613_b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0042318613_row2878170018456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042318613_p4961636318456"><a name="en-us_topic_0042318613_p4961636318456"></a><a name="en-us_topic_0042318613_p4961636318456"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042318613_p5950245818456"><a name="en-us_topic_0042318613_p5950245818456"></a><a name="en-us_topic_0042318613_p5950245818456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042318613_p5496981818456"><a name="en-us_topic_0042318613_p5496981818456"></a><a name="en-us_topic_0042318613_p5496981818456"></a>PTR record ID, which is in <strong id="en-us_topic_0042318613_b842352706151833"><a name="en-us_topic_0042318613_b842352706151833"></a><a name="en-us_topic_0042318613_b842352706151833"></a>{region}:{floatingip_id}</strong> format</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042318613_row3274940018456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042318613_p3545576918456"><a name="en-us_topic_0042318613_p3545576918456"></a><a name="en-us_topic_0042318613_p3545576918456"></a>ptrdname</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042318613_p5334507918456"><a name="en-us_topic_0042318613_p5334507918456"></a><a name="en-us_topic_0042318613_p5334507918456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042318613_p2598415318456"><a name="en-us_topic_0042318613_p2598415318456"></a><a name="en-us_topic_0042318613_p2598415318456"></a>Domain name of the PTR record</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042318613_row3253079218456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042318613_p1774845918456"><a name="en-us_topic_0042318613_p1774845918456"></a><a name="en-us_topic_0042318613_p1774845918456"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042318613_p2833911218456"><a name="en-us_topic_0042318613_p2833911218456"></a><a name="en-us_topic_0042318613_p2833911218456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042318613_p1376672518456"><a name="en-us_topic_0042318613_p1376672518456"></a><a name="en-us_topic_0042318613_p1376672518456"></a>PTR record description</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042318613_row5679166318456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042318613_p3672198418456"><a name="en-us_topic_0042318613_p3672198418456"></a><a name="en-us_topic_0042318613_p3672198418456"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042318613_p2169069318456"><a name="en-us_topic_0042318613_p2169069318456"></a><a name="en-us_topic_0042318613_p2169069318456"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042318613_p65120323151724"><a name="en-us_topic_0042318613_p65120323151724"></a><a name="en-us_topic_0042318613_p65120323151724"></a>Caching period of a PTR record (in seconds)</p>
    <p id="en-us_topic_0042318613_p1211568618456"><a name="en-us_topic_0042318613_p1211568618456"></a><a name="en-us_topic_0042318613_p1211568618456"></a>The default value is <strong id="en-us_topic_0042318613_b766716615417"><a name="en-us_topic_0042318613_b766716615417"></a><a name="en-us_topic_0042318613_b766716615417"></a>300s</strong>.</p>
    <p id="en-us_topic_0042318613_p4184654118456"><a name="en-us_topic_0042318613_p4184654118456"></a><a name="en-us_topic_0042318613_p4184654118456"></a>The value range is 300–2147483647.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042318613_row3412662318456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042318613_p1279309418456"><a name="en-us_topic_0042318613_p1279309418456"></a><a name="en-us_topic_0042318613_p1279309418456"></a>address</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042318613_p2960772218456"><a name="en-us_topic_0042318613_p2960772218456"></a><a name="en-us_topic_0042318613_p2960772218456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042318613_p4941528218456"><a name="en-us_topic_0042318613_p4941528218456"></a><a name="en-us_topic_0042318613_p4941528218456"></a>EIP</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042318613_row4208435918456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042318613_p5338995318456"><a name="en-us_topic_0042318613_p5338995318456"></a><a name="en-us_topic_0042318613_p5338995318456"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042318613_p2961896418456"><a name="en-us_topic_0042318613_p2961896418456"></a><a name="en-us_topic_0042318613_p2961896418456"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042318613_p5032586318456"><a name="en-us_topic_0042318613_p5032586318456"></a><a name="en-us_topic_0042318613_p5032586318456"></a>Resource status</p>
    <p id="en-us_topic_0042318613_p55721846144628"><a name="en-us_topic_0042318613_p55721846144628"></a><a name="en-us_topic_0042318613_p55721846144628"></a>The value can be <strong id="en-us_topic_0042318613_b84235270695628"><a name="en-us_topic_0042318613_b84235270695628"></a><a name="en-us_topic_0042318613_b84235270695628"></a>PENDING_CREATE</strong>, <strong id="en-us_topic_0042318613_b84235270695635"><a name="en-us_topic_0042318613_b84235270695635"></a><a name="en-us_topic_0042318613_b84235270695635"></a>ACTIVE</strong>, <strong id="en-us_topic_0042318613_b84235270695643"><a name="en-us_topic_0042318613_b84235270695643"></a><a name="en-us_topic_0042318613_b84235270695643"></a>PENDING_DELETE</strong>, <strong id="en-us_topic_0042318613_b842352706141041"><a name="en-us_topic_0042318613_b842352706141041"></a><a name="en-us_topic_0042318613_b842352706141041"></a>PENDING_UPDATE</strong>, or <strong id="en-us_topic_0042318613_b84235270695650"><a name="en-us_topic_0042318613_b84235270695650"></a><a name="en-us_topic_0042318613_b84235270695650"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042318613_row4986307418456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042318613_p1237719818456"><a name="en-us_topic_0042318613_p1237719818456"></a><a name="en-us_topic_0042318613_p1237719818456"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042318613_p6302897818456"><a name="en-us_topic_0042318613_p6302897818456"></a><a name="en-us_topic_0042318613_p6302897818456"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042318613_p507362318456"><a name="en-us_topic_0042318613_p507362318456"></a><a name="en-us_topic_0042318613_p507362318456"></a>Requested operation on the resource</p>
    <p id="en-us_topic_0042318613_p9217462145017"><a name="en-us_topic_0042318613_p9217462145017"></a><a name="en-us_topic_0042318613_p9217462145017"></a>The value can be <strong id="en-us_topic_0042318613_b842352706141356"><a name="en-us_topic_0042318613_b842352706141356"></a><a name="en-us_topic_0042318613_b842352706141356"></a>CREATE</strong>, <strong id="en-us_topic_0042318613_b84235270614144"><a name="en-us_topic_0042318613_b84235270614144"></a><a name="en-us_topic_0042318613_b84235270614144"></a>UPDATE</strong>, or <strong id="en-us_topic_0042318613_b84235270614146"><a name="en-us_topic_0042318613_b84235270614146"></a><a name="en-us_topic_0042318613_b84235270614146"></a>DELETE</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042318613_row831034118456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042318613_p204899518456"><a name="en-us_topic_0042318613_p204899518456"></a><a name="en-us_topic_0042318613_p204899518456"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042318613_p3175087318456"><a name="en-us_topic_0042318613_p3175087318456"></a><a name="en-us_topic_0042318613_p3175087318456"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042318613_p2168392018456"><a name="en-us_topic_0042318613_p2168392018456"></a><a name="en-us_topic_0042318613_p2168392018456"></a>Link of the current resource or other related resources</p>
    <p id="en-us_topic_0042318613_p6093755518456"><a name="en-us_topic_0042318613_p6093755518456"></a><a name="en-us_topic_0042318613_p6093755518456"></a>When a response is broken into pages, a <strong id="en-us_topic_0042318613_b84235270695245"><a name="en-us_topic_0042318613_b84235270695245"></a><a name="en-us_topic_0042318613_b84235270695245"></a>next</strong> link is provided to retrieve all results.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
        "id": "region\_id:c5504932-bf23-4171-b655-b87a6bc59334",
        "ptrdname": "www.example.com.",
        "description": "Description for this PTR record",
        "address": "10.154.52.138",
        "action": "CREATE",
        "ttl": 300,
        "status": "ACTIVE",
        "links": {
            "self": "https://Endpoint/v2/reverse/floatingips/region\_id:c5504932-bf23-4171-b655-b87a6bc59334"
        }
    }
    ```


## **Returned Value**<a name="section61705107"></a>

See  [General Request Return Code](general-request-return-code.md).

