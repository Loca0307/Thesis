    void huntPrayCallback()
    {
        std::lock_guard<std::mutex> lock(mutex_);
        if (!pose_ || !target_){
            RCLCPP_ERROR(this->get_logger(), "Error: Pose or target is not available.");
            return;
        }
        geometry_msgs::msg::Twist msg;

        if (target_distance_ > 0.5)
        {
            msg.linear.x  = kp_linear_ * target_distance_;
            double diff = std::fmod(goal_theta_ - pose_->theta + M_PI, 2 * M_PI) - M_PI;
            msg.angular.z = kp_angular_ * diff;
        }
        else
        {
            msg.linear.x  = 0.0;
            msg.angular.z = 0.0;
            threads_.emplace_back(&HunterNode::sendKillRequest, this, target_->name);
        }

        cmd_vel_publisher_->publish(msg);