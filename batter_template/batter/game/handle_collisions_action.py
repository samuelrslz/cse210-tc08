import random
import sys
from game import constants
from game.action import Action
from game.point import Point


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]
        # ball.set_text("")
        for i in range(len(bricks)-1):
            if ball.get_position().equals(bricks[i].get_position()):
                del bricks[i]
                ball.set_velocity(Point(ball.get_velocity().get_x(), ball.get_velocity().get_y() * -1))
        paddleEnd = Point(paddle.get_position().get_x() + 11,paddle.get_position().get_y())
        pX = paddle.get_position().get_x()
        pY = paddle.get_position().get_y() - 1
        pW = paddle.get_position().get_x() + 11

        bX = ball.get_position().get_x()
        bY = ball.get_position().get_y()
        if (bX >= pX and bX <= pW) and bY == pY or bY == 1:
            ball.set_velocity(Point(ball.get_velocity().get_x(), ball.get_velocity().get_y() * -1))

        if bX == 1 or bX == constants.MAX_X -1: 
            ball.set_velocity(Point(ball.get_velocity().get_x() * -1, ball.get_velocity().get_y()))
        
        if bY == constants.MAX_Y-1:
            sys.exit()

