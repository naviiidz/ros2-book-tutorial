#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from my_interfaces.msg import TempSensor


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(TempSensor, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.send_temp)

    def send_temp(self):
        msg = TempSensor()
        msg.temperature = 22.5
        msg.unit = 'Centigrade'
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)


if __name__ == '__main__':
    main()