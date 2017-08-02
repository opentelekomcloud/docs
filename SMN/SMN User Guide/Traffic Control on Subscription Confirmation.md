## Traffic Control on Subscription Confirmation


To prevent a malicious user from harassing subscribers, we control the number of subscription confirmation messages a user can send to an individual subscriber within a specified time period. The traffic control policy is applicable to confirmation requests issued both from the SMN console and by API calling. The traffic control policies for different subscription protocols are as follows:

- Email: A user can send up to 20 confirmation messages within an hour and 40 within two days. If the user tries to send more confirmation messages than the threshold, SMN will not send any confirmation message to the email address within 7 days. After the subscriber confirms the subscription, SMN clears the count in the traffic control policy.

- SMS: A user can send up to 10 confirmation messages within an hour and 20 within two days. If the user tries to send more confirmation messages than the threshold, SMN will not send any confirmation message to the phone number within 7 days. After the subscriber confirms the subscription, SMN clears the count in the traffic control policy.

- HTTP/HTTPS: A user can send up to 200 confirmation messages within 10 minutes.
