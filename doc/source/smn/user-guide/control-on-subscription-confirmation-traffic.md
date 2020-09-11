# Control on Subscription Confirmation Traffic<a name="smn_ug_a4000"></a>

To prevent malicious users from harassing subscribers, there is a limit on the number of subscription confirmation messages a user can send to an individual subscriber within a specified period of time. Traffic control policies apply to confirmation requests issued both from the SMN console and by API calling. Traffic control policies for different subscription protocols are as follows:

-   Email: A user can send up to 20 confirmation messages within one hour or 40 within two days. If the user exceeds this threshold, SMN will not send any more confirmation messages to that email address in the next seven days. After the subscriber confirms the subscription, SMN clears the count in the traffic control policy.
-   SMS: A user can send up to 10 confirmation messages within one hour or 20 within two days. If the user exceeds this threshold, SMN will not send any more confirmation messages to that phone number in the next seven days. After the subscriber confirms the subscription, SMN clears the count in the traffic control policy.
-   HTTP/HTTPS: A user can send up to 200 confirmation messages within 10 minutes.

