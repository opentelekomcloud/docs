# Web Application Firewall<a name="waf_01_0045"></a>

Web Application Firewall \(WAF\) keeps web services stable and secure. It examines all HTTP and HTTPS requests to detect and block the following attacks: Structured Query Language \(SQL\) injection, cross-site scripting \(XSS\), webshells, command and code injections, file inclusion, sensitive file access, third-party vulnerability exploits,  Challenge Collapsar \(CC\) attacks, malicious crawlers, and cross-site request forgery \(CSRF\).

## Functions<a name="section17475152012241"></a>

WAF helps you easily handle web security risks.

-   Basic web protection

    With preset powerful reputation databases, WAF defends against OWASP Top 10 threats, and detects and blocks malicious scanners, IP addresses, and webshells.

    -   Comprehensive protection

        WAF detects and blocks such threats as SQL injection, XSS, file inclusion, directory traversal attacks, sensitive file access, command and code injections, webshells, backdoors, malicious HTTP requests, and third-party vulnerability exploits.

    -   Precise identification
        -   Built-in semantic analysis and regex engines, and blacklist/whitelist configurations, reducing false positives
        -   Common code restoration with improved detection capabilities on distortion attacks

            Encoding types supported: url\_encode, Unicode, XML encoding, C-OCT encoding, hexadecimal encoding, HTML encoding, base64 encoding, obfuscation, JavaScript, shell, and php



-   CC attack protection

    By configuring protective actions and returned pages based on your needs, WAF mitigates the impact of CC attacks \(also known as HTTP flood attacks\).

    -   Fine-grained flexibility

        Allows you to flexibly set rate limiting policies by IP address, cookie, or Referer field.

    -   Returned page customization

        Meets diverse requirements for returned content and page type.


-   Security visualization

    Provides a user-friendly interface, allowing you to monitor attack information and event logs in real time.

    -   Centralized policy configuration

        On-console configuration, rapid delivery, and immediate implementation of policies

    -   Traffic and event statistics

        Real-time display of the number of requests, the number and types of security events, and log information


-   Non-standard ports \(169 in total\)

    In addition to standard ports 80 and 443, WAF also supports  169 non-standard ports. Select one of the following ports.

    -   146 non-standard HTTP ports:

        <a name="en-us_topic_0154713081_table101131190118"></a>
        <table><thead align="left"><tr id="en-us_topic_0154713081_row51145981117"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="en-us_topic_0154713081_p4114119101116"><a name="en-us_topic_0154713081_p4114119101116"></a><a name="en-us_topic_0154713081_p4114119101116"></a>Port Number Starting with 7 (33)</p>
        </th>
        <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="en-us_topic_0154713081_p01141292112"><a name="en-us_topic_0154713081_p01141292112"></a><a name="en-us_topic_0154713081_p01141292112"></a>Port Number Starting with 8 (57)</p>
        </th>
        <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="en-us_topic_0154713081_p311499171114"><a name="en-us_topic_0154713081_p311499171114"></a><a name="en-us_topic_0154713081_p311499171114"></a>Port Number Starting with 9 (33)</p>
        </th>
        <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="en-us_topic_0154713081_p12114179131118"><a name="en-us_topic_0154713081_p12114179131118"></a><a name="en-us_topic_0154713081_p12114179131118"></a>Other (23)</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="en-us_topic_0154713081_row171141894114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0154713081_p151141192117"><a name="en-us_topic_0154713081_p151141192117"></a><a name="en-us_topic_0154713081_p151141192117"></a>7000, 7001, 7002, 7003, 7004, 7005, 7006, 7009, 7010, 7011, 7012, 7013, 7014, 7015, 7016, 7018, 7019, 7020, 7021, 7022, 7023, 7024, 7025, 7026, 7070, 7081, 7082, 7083, 7088, 7097, 7510, 7777, and 7800</p>
        </td>
        <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0154713081_p101141094110"><a name="en-us_topic_0154713081_p101141094110"></a><a name="en-us_topic_0154713081_p101141094110"></a>81, 82, 83, 84, 86, 87, 88, 89, 800, 808, 8000, 8001, 8002, 8003, 8008, 8009, 8010, 8011, 8012, 8013, 8014, 8015, 8016, 8017, 8020, 8021, 8022, 8025, 8026, 8070, 8077, 8078, 8080, 8085, 8086, 8087, 8088, 8089, 8090, 8091, 8092, 8093, 8094, 8095, 8096, 8097, 8098, 8106, 8118, 8181, 8334, 8336, 8800, 8686, 8888, 8889, and 8999</p>
        </td>
        <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0154713081_p8775162641517"><a name="en-us_topic_0154713081_p8775162641517"></a><a name="en-us_topic_0154713081_p8775162641517"></a>97, 9000, 9001, 9002, 9003, 9080, 9200, 9802, 9999, 9021, 9023, 9027, 9037, 9081, 9082, 9201, 9205, 9207, 9208 9209, 9210, 9211, 9212, 9213, 9180, 9898, 9908, 9916, 9918, 9919, 9928, 9929, and 9939</p>
        </td>
        <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0154713081_p16115209171118"><a name="en-us_topic_0154713081_p16115209171118"></a><a name="en-us_topic_0154713081_p16115209171118"></a>1000, 1090, 10000, 10001, 10080, 12601, 28080, 33702, 3128, 3333, 3501, 3601, 4444, 48800, 5000, 5222, 5555, 5601, 6001, 6666, 6788 6789, and 6842</p>
        </td>
        </tr>
        </tbody>
        </table>

    -   23 non-standard HTTPS ports:

        4443, 5443, 6443, 7443, 8033, 8081, 8082, 8083, 8084, 8443, 8553, 8663, 8843, 9443, 9553, 9663, 18000, 18110, 18381, 18443, 18980, 28443, and 19000


-   Precise protection

    Supports precise logic- and parameter-based access control policies.

    -   A variety of parameter conditions

        Sets conditions with combinations of common HTTP parameters such as  **IP**,  **URL**,  **Referer**,  **User Agent**,  **Params**, and  **Header**.

    -   Rich set of logical relationships

        Blocks or allows traffic based on logical relationships such as "Include", "Exclude", "Equal to", "Not equal to", "Prefix is", and "Prefix is not."


-   Protection against scanners and crawlers

    Built-in scanner and crawler rules block unauthorized webpage crawling. The customized malicious crawler and scanner features improve protection accuracy.

-   Blacklist and whitelist

    This function allows you to blacklist or whitelist IP addresses to improve defense accuracy.

-   Web tamper protection

    Cache configuration is performed on static webpages. When a user accesses a webpage, the system returns a cached page to the user and randomly checks whether the page has been tampered with.

-   False alarm masking

    This function ignores certain attack detection rules for specific requests.

-   Data masking

    WAF masks sensitive information, such as usernames and passwords, in the event log.

-   Alarm notification

    Once this function is enabled, WAF sends attack logs to users by email or SMS.

-   Event management
    -   You can mask blocked or logged attack events misreported by WAF and view event details.
    -   You can download events data over the past five days.


