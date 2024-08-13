#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.declare_parameter("frequency_of_publishing", 2)
        self.declare_parameter("increment", 1)
        timer_period = 1/self.get_parameter("frequency_of_publishing").value  # seconds
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.i += self.get_parameter("increment").value


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)


if __name__ == '__main__':
    main()