        # Penalize for high speeds when landing
        if didAgentLand(self) and self.y_speed > 2.0:
            score -= 2000
        # Reward for successful landing
        if didAgentLand(self) and self.y_speed <= 2.0:
            score += 1000