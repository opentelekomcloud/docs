# Introduction to the Alarm Function<a name="EN-US_TOPIC_0084572153"></a>

The alarm function is based on collected metrics. You can set alarm rules for key metrics of cloud services. When the metric data triggers the conditions set in the alarm rule, Cloud Eye sends emails, or text messages, to you, or sends HTTP/HTTPS requests to the servers. In this way, you are immediately informed of cloud service exceptions and can quickly handle the faults to avoid service losses.

Cloud Eye uses the SMN service to notify users. This requires you to create a topic and add subscriptions to this topic on the SMN console first. Then when you create alarm rules, you can enable the  **Alarm Notification**  function and select the created topic. When an error occurs, Cloud Eye can broadcast alarm information to those subscriptions in real time.

