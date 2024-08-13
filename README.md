# ROS 2 Python Package - `ros2-book-tutorials`

## Overview
This repository contains sample codes for ROS 2 as explained in the book, written in Farsi and published by Dibagaran Publications in August 2024. You can find more information about the book [here](https://www.dibagaranpakhsh.ir/index.php?route=product/product&product_id=2122).


## Packages
The repository includes the following three main packages created in the book:

- **py_package**: This is the main package where most of the nodes are implemented (Chapters 3, 4, 5, 7, 8).
- **launch_all**: This package contains a launch file to start all nodes created in `py_package` (Chapter 9).
- **my_interfaces**: This package includes the custom interfaces discussed in Chapter 6.

## Requirements
The packages have been developed and tested with the following dependencies:
- **ROS 2**: Iron Irwini
- **Python**: 3.10.12
- Other dependencies: `rclpy`, `std_msgs`, `example_interfaces`, `sys`, `action_tutorials_interfaces`

## Cloning the Repository
Clone the repository into your ROS 2 workspace (e.g., `~/ros2_ws/src`):

```bash
cd ~/ros2_ws/src
git clone https://github.com/naviiidz/ros2-book-tutorial.git
```

## Future Updates
More useful information, including cheatsheets and additional resources, will be added to this repository over time. Stay tuned for updates!
