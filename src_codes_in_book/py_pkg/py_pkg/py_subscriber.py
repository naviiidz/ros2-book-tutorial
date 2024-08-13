#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.publisher2= self.create_publisher(String, "OddOrEven", 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        msg2=String()
        text=msg.data
        text_split=text.split()
        if int(text_split[-1])%2==0:
            msg2.data="Even"
            self.publisher2.publish(msg2)
        else:
            msg2.data="Odd"
            self.publisher2.publish(msg2)           


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)


if __name__ == '__main__':
    main()