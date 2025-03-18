# ROS2 Package: talker_listener & add_integers

## Overview
This repository contains implementations demonstrating different communication methodologies in ROS2. Each package follows a specific methodology and serves as an independent lesson for understanding ROS2 communication patterns.

## Lesson 1: talker_listener (Publisher/Subscriber - Message Methodology)
### Objective
The goal of this package is to understand how publishing and subscribing work in ROS2 using the message-passing methodology.

### Explanation
- The **talker** node continuously publishes messages at a fixed interval.
- The **listener** node subscribes to these messages and prints them when received.
- This demonstrates one-way communication where a publisher broadcasts messages, and multiple subscribers can receive and process them.

### Implementation Details
- Uses ROS2 **std_msgs/String** for message transmission.
- Demonstrates real-time communication between nodes.
- Implemented using `rclpy` for Python-based nodes.
- A simple example of decoupled communication between ROS2 nodes.

### Running `talker_listener`
```bash
ros2 run talker_listener talker &
ros2 run talker_listener listener
```

---

## Lesson 2: add_integers & custom_integers (Service/Client - Service Methodology)
### Objective
The goal of these packages is to understand how services and clients work in ROS2 using request-response communication.

### Explanation
- The **add_integers** package (Python) implements a service that adds two numbers.
- A **client** node sends a request with two integers.
- The **server** node processes the request, computes the sum, and returns the result to the client.
- The **custom_integers** package (C++) acts as an interface defining a structured format for passing and processing data.

### Implementation Details
- Uses ROS2 **srv** services to handle request-response communication.
- The **add_integers** package provides a Python-based service-server and client interaction.
- The **custom_integers** package provides a CMake-based package defining the type of data being passed for structured communication.

### Running `add_integers` (Python Service/Client)
```bash
ros2 run add_integers add_server &  # Start service
ros2 run add_integers add_client 4 7  # Request sum of 4 and 7
```

### Running `custom_integers` (C++ Service/Client)
```bash
ros2 run custom_integers custom_server &
ros2 run custom_integers custom_client 10 20
```

---

## Getting Started

### Prerequisites
Ensure you have ROS2 installed and sourced:
```bash
source /opt/ros/<your_ros_version>/setup.bash
```

### Installation & Build
Clone the repository and build it using `colcon`:
```bash
cd ~/ros2_ws/src
git clone <repository-url>
cd ~/ros2_ws
colcon build
source install/setup.bash
```

## Customization
- Modify `srv/AddTwoInts.srv` for custom service definitions.
- Extend `talker_listener` with additional topics as needed.
- Expand `custom_integers` to define additional structured data types.

## License
This project is licensed under the MIT License.

## Contact
For questions, feel free to reach out.
