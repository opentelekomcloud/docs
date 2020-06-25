# Simple Message Notification<a name="en-us_topic_0043394877"></a>

Simple Message Notification \(SMN\) is a reliable and flexible large-scale message notification service. It enables you to efficiently send messages to phone numbers, email addresses and HTTP/HTTPS servers and connect cloud services through notifications, reducing system complexity.

SMN offers a publish/subscribe model to achieve one-to-multiple message subscriptions and notifications in a variety of message types. SMN involves two roles: publisher and subscriber. A publisher publishes messages to a topic, and SMN then delivers the messages to subscribers in the topic. The subscribers can be email addresses, phone numbers, message queues, and URLs.

A topic is a collection of messages and a logical access point, through which the publisher and the subscriber can interact with each other. Each topic has a unique topic name. The topic creator can configure topic policies to grant other users or cloud services permissions to perform certain operations to a topic, for example, querying subscriptions or publishing messages.

