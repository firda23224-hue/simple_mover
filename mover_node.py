import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MoverNode(Node):
    def __init__(self):
        super().__init__('mover_node')
        
        # Wajib diaktifkan agar waktu sesuai dengan simulator Gazebo
        self.set_parameters([rclpy.parameter.Parameter('use_sim_time', rclpy.Parameter.Type.BOOL, True)])
        
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.start_time = None

    def timer_callback(self):
        msg = Twist()
        
        # Ambil waktu simulasi Gazebo dalam satuan detik
        now = self.get_clock().now().nanoseconds / 1e9
        
        if self.start_time is None:
            self.start_time = now
            return

        elapsed_time = now - self.start_time

        # 1. Maju sisi panjang 1 (5.0 detik)
        if elapsed_time < 5.0:
            msg.linear.x = 0.5
            msg.angular.z = 0.0
            self.get_logger().info('Maju sisi panjang 1')
            
        # Jeda diam (0.5 detik)
        elif elapsed_time < 5.5:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        # 2. Rotasi 90 derajat pertama (4.0 detik)
        elif elapsed_time < 9.5:
            msg.linear.x = 0.0
            msg.angular.z = 0.5
            self.get_logger().info('Rotasi 90 derajat')

        # 3. Maju sisi pendek 1 (2.5 detik)
        elif elapsed_time < 12.0:
            msg.linear.x = 0.5
            msg.angular.z = 0.0
            self.get_logger().info('Maju sisi pendek 1')
            
        # Jeda diam (0.5 detik)
        elif elapsed_time < 12.5:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        # 4. Rotasi 90 derajat kedua (4.0 detik)
        elif elapsed_time < 16.5:
            msg.linear.x = 0.0
            msg.angular.z = 0.5
            self.get_logger().info('Rotasi 90 derajat')

        # 5. Maju sisi panjang 2 (5.0 detik)
        elif elapsed_time < 21.5:
            msg.linear.x = 0.5
            msg.angular.z = 0.0
            self.get_logger().info('Maju sisi panjang 2')
            
        # Jeda diam (0.5 detik)
        elif elapsed_time < 22.0:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        # 6. Rotasi 90 derajat ketiga (4.0 detik)
        elif elapsed_time < 26.0:
            msg.linear.x = 0.0
            msg.angular.z = 0.5
            self.get_logger().info('Rotasi 90 derajat')

        # 7. Maju sisi pendek 2 (2.5 detik)
        elif elapsed_time < 28.5:
            msg.linear.x = 0.5
            msg.angular.z = 0.0
            self.get_logger().info('Maju sisi pendek 2')
            
        # Jeda diam (0.5 detik)
        elif elapsed_time < 29.0:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        # 8. Rotasi 90 derajat terakhir (4.0 detik)
        elif elapsed_time < 33.0:
            msg.linear.x = 0.0
            msg.angular.z = 0.5
            self.get_logger().info('Rotasi 90 derajat terakhir')

        # Selesai
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.get_logger().info('Gerakan persegi panjang selesai.')
            self.publisher_.publish(msg)
            
            self.timer.cancel()
            rclpy.shutdown()
            return

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MoverNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()
