#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from my_interfaces.msg import TempSensor


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(TempSensor, 'topic', self.listener_callback, 10)

    def listener_callback(self, msg):
        unit_received=msg.unit
        temp_received=msg.temperature
        print('Temperature is %f %s' %(temp_received, unit_received))         


def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)


if __name__ == '__main__':
    main()