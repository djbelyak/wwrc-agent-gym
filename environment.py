"""Package to describe finite state machine environment."""


class Environment():
    """Class of a simple finite state machine."""

    def __init__(self):
        """Init of the object."""
        self.states = ['off', 'on']
        self.start_state = 'off'
        self.state = self.start_state
        self.finish_states = ['on']
        self.actions = ['switch off', 'switch on']
        self.transitions = {
            'off': {
                'switch on': 'on'
            },
            'on': {
                'switch off': 'off'
            }
        }

    def action(self, action):
        """Make an action.

        Args:
            action (str): name of action from self.actions list
        """
        if self.state in self.transitions:
            if action in self.transitions[self.state]:
                self.state = self.transitions[self.state][action]

    def is_finish(self):
        """Return true if state machine in finish state."""
        return self.state in self.finish_states

    def reset(self):
        """Reset state of FSM."""
        self.state = self.start_state
