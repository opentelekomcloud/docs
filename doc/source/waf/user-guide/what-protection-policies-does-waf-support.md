# What Protection Policies Does WAF Support?<a name="waf_01_0028"></a>

The protection policies supported by WAF are described below.

-   Basic Web Protection

    WAF can defend against common web attacks, such as SQL injection, XSS, webshells, and Trojans in HTTP upload channels. Once these functions are enabled, protection takes effect immediately.

-   CC Attack Protection

    Flexible rate limiting policies can be set based on the IP addresses, cookies, or Referer field, mitigating CC attacks.

-   Precise Protection

    Common HTTP fields can be combined to customize protection policies, such as CSRF protection. With user-defined rules, WAF can accurately detect malicious requests and protect sensitive information in websites.

-   Blacklist and Whitelist

    Blacklist or whitelist rules allow you to block or allow specific IP addresses or address ranges, improving defense accuracy.

-   Web Tamper Protection

    Cache configuration is performed on static webpages. When a user accesses a webpage, the system returns a cached page to the user and randomly checks whether the page has been tampered with.

-   False Alarm Masking

    This function ignores certain attack detection rules for specific requests.

-   Data Masking

    Data masking prevents such data as passwords from being displayed in event logs.


