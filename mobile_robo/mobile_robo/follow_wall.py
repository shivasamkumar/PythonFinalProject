import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import time

class follow_wall_bot(Node):
    def __init__(self):
        super().__init__('Go_to_position_node') ## name of the node
        # publisher
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        #subscriber
        self.subscription=self.create_subscription(LaserScan,'/scan',self.get_scan_values,40)
        #periodic publisher call
        timer_period = 0.2;self.timer = self.create_timer(timer_period, self.send_cmd_vel)
        ## Initializing Global values
        ## given a value for VELOCITY
        self.linear_vel = 0.2 
        self.region_1=0;self.region_2=0;self.region_3=0
        self.error=0
        self.case=""
        ## creating a message object to fit new velocities and publish them
        self.velocity=Twist()

    def get_scan_values(self,scan_data):
        self.region_1= min(min(scan_data.ranges[0:20])   , 100 )
        self.region_2= min(min(scan_data.ranges[20:40])  , 100 )
        self.region_3= min(min(scan_data.ranges[40:60])  , 100 )
        print(round(self.region_3,3) ,"/",round(self.region_2,3),"/",round(self.region_1,3),"/",self.velocity.angular.z,"/",self.case )
    
    ## helping function
    def proporitonal_control(self):
        ##Calculating error from the desired point
        self.error = 1.2 - self.region_1
        
        if(self.error < -1.57):
            self.error = 1.57
        self.velocity.linear.x= self.linear_vel
        self.velocity.angular.z=(self.error)

    ## Publihsing Velocity function call back
    def send_cmd_vel(self):
        if(self.region_1<4): 
            self.case="basic"
            self.proporitonal_control()## calling helper function
            if(self.region_3 > 4 and self.region_2 > 4):
                self.case="TURN"
                self.velocity.linear.x= 0.4 ## increasing speed
                self.velocity.angular.z=-1.57 ## sharp right turn
        ## Publishing Complete values
        self.publisher.publish(self.velocity)

def main(args=None):
    rclpy.init(args=args)
    oab=follow_wall_bot()
    rclpy.spin(oab)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
