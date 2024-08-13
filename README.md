# ROS 2 Python Package - `your_package_name`

## Overview
This repo presents sample codes of ROS2 explained in the book. The book is written in Farsi language and published by Dibagaran publication in August 2024.

## Packages
Packages created in the book are included in _src_codes_in_book_. There are 3 main packages:
- **py_package**: This is the main package. Almost all nodes are in _py_package_ (Chapters 3, 4, 5, 7, 8).
- **launch_all**: This package includes a launch file to launch all nodes created in _py_pkg_ (Chapter 9).
- **my_interfaces**: This package includes the custom interface explained (Chapter 6).

## Requirements
Packages have been developed and tested with the following dependencies:
- **ROS 2**: This is the main package. Almost all nodes are in _py_package_ (Chapters 3, 4, 5, 7, 8).
- **Python**: 3.10.12
- Other dependencies: rclpy, std_msgs, example_interfaces, sys, action_tutorials_interfaces, 

### Cloning the Repository
Clone the repository into your ROS 2 workspace (e.g., `~/ros2_ws/src`)

```bash
cd ~/ros2_ws/src
git clone https://github.com/naviiidz/ros2-book-tutorial.git
