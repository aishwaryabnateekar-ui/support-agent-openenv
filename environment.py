class SupportAgentEnv:

    def reset(self):
        self.ticket = "Payment failed but money deducted"
        self.step_count = 0
        self.resolved = False
        return self.ticket

    def step(self, action):
        reward = 0.0
        done = False
        error = None

        self.step_count += 1

        if action["action_type"] == "classify":
            reward = 0.3

        elif action["action_type"] == "set_priority":
            reward = 0.2

        elif action["action_type"] == "respond":
            reward = 0.4

        elif action["action_type"] == "resolve":
            reward = 0.5
            done = True

        else:
            reward = -0.2
            error = "Invalid action"

        return self.ticket, reward, done, {"error": error}

    def state(self):
        return {
            "ticket": self.ticket,
            "steps": self.step_count,
            "resolved": self.resolved
        }
