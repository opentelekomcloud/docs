# URL Validation Overview<a name="en-us_topic_0045853689"></a>

To reduce costs, some websites steal links from other websites to enrich their own contents. Link stealing not only damages interests of the original websites but also increases workloads on the original websites' servers. Therefore URL is used to resolve this problem.

In HTTP, a website can detect the web page that accesses a target web page using the  **Referer**  field. As the  **Referer**  field can trace sources, specific techniques can be used to block or return to specific web pages if the pages are not from the website. URL validation checks whether the  **Referer**  field in requests matches the whitelist or blacklist by setting  **Referers**. If the field matches the whitelist, the requests are allowed. Otherwise, the requests are blocked or specific pages are displayed.

OBS supports URL validation based on the  **Referer**  header field in HTTP requests to prevent a user's data in OBS from being stolen by other users. OBS supports both whitelists and blacklists.

