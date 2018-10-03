"""Test for finite state machine package."""
import unittest

from environment import Environment


class EnvironmentTest(unittest.TestCase):
    """TestCase for a simple FSM."""

    def test_init(self):
        """Test __init__() method."""
        env = Environment()
        self.assertEqual(env.states, ['off', 'on'])
        self.assertEqual(env.state, 'off')
        self.assertEqual(env.finish_states, ['on'])
        self.assertEqual(env.actions, ['switch off', 'switch on'])

    def test_actions(self):
        """Test of action method."""
        env = Environment()
        self.assertEqual(env.state, 'off')

        env.action('switch on')
        self.assertEqual(env.state, 'on')

        env.action('switch off')
        self.assertEqual(env.state, 'off')

    def test_is_finish(self):
        """Test of is_finish method."""
        env = Environment()
        self.assertFalse(env.is_finish())

        env.action('switch on')
        self.assertEqual(env.state, 'on')
        self.assertTrue(env.is_finish())

    def test_reset(self):
        """Test of reset method."""
        env = Environment()
        self.assertFalse(env.is_finish())

        env.action('switch on')
        self.assertEqual(env.state, 'on')
        self.assertTrue(env.is_finish())

        env.reset()
        self.assertEqual(env.state, 'off')
        self.assertFalse(env.is_finish())
