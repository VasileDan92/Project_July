# Creating a Paddle Pong Game in Python

# Create Graphics using turtle
import turtle
import pong_game_elements
import pong_paddle
import pong_ball
import pong_scoreboard

# Creating Score
score_player_a = 0
score_player_b = 0


# Ball comes back to center after a goal
def back_to_center(scoreboard, ball, paddle_1, paddle_2):
    ball.goto(0, 0)
    ball.dx *= -1
    scoreboard.clear( )
    paddle_1.goto(-350, 0)
    paddle_2.goto(+350, 0)


# The game was finished
def game_over(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element):
    ball.goto(0, 0)
    ball.dx = 0
    ball.dy = 0
    scoreboard.goto(0, 230)
    scoreboard.write("Wanna play again? Y for Yes, N for No!", align="center", font=("Verdana", 18, "normal"))
    scoreboard.goto(0, 260)
    scoreboard.color("yellow")
    # Choose to continue or finish the game
    game_screen.onkeypress(game_element.reset, "y")
    game_screen.onkeypress(game_element.return_to_main, "n")
    paddle_1.goto(-350, 0)
    paddle_2.goto(+350, 0)


# Reset the scoreboard after the games has finished
def reset_scoreboard(scoreboard):
    scoreboard.clear( )
    scoreboard.goto(0, 260)


# Start Game
def start_pong_game(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element):
    global score_player_a
    global score_player_b

    # Move the ball which starts from 0.
    ball.setx(ball.xcor( ) + ball.dx)
    ball.sety(ball.ycor( ) + ball.dy)

    # Border Checking - Top and Down Border - Compare Coordinate. When it hits a certain point, it needs to bound
    if ball.ycor( ) > 290:
        ball.sety(290)
        # Reversing the direction
        ball.dy *= -1

    if ball.ycor( ) < -290:
        ball.sety(-290)
        # Reversing the direction
        ball.dy *= -1

    # Border Checking - Left and Right
    if ball.xcor( ) > 390:
        # Coming back to center
        back_to_center(scoreboard, ball, paddle_1, paddle_2)
        score_player_a += 1
        scoreboard.write("Home (Blue): {} Away (Red): {}".format(score_player_a, score_player_b), align="center",
                         font=("Verdana", 18, "normal"))
        if score_player_a == 2:
            reset_scoreboard(scoreboard)
            scoreboard.color("blue")
            scoreboard.write("Game Over! Home won", align="center", font=("Verdana", 18, "normal"))
            game_over(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
            score_player_a = 0
            score_player_b = 0

    if ball.xcor( ) < -390:
        # Coming back to center
        back_to_center(scoreboard, ball, paddle_1, paddle_2)
        score_player_b += 1
        scoreboard.clear( )
        scoreboard.write("Home (Blue): {} Away (Red): {}".format(score_player_a, score_player_b), align="center",
                         font=("Verdana", 18, "normal"))
        if score_player_b == 2:
            reset_scoreboard(scoreboard)
            scoreboard.color("red")
            scoreboard.write("Game Over! Away won", align="center", font=("Verdana", 18, "normal"))
            game_over(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
            score_player_a = 0
            score_player_b = 0

    # Paddle and Ball Collisions - avoid ball going after the paddle
    if (-340 > ball.xcor( ) > -350) and (paddle_1.ycor( ) + 50 > ball.ycor( ) > paddle_1.ycor( ) - 50):
        ball.setx(-340)
        ball.dx *= -1

    if (340 < ball.xcor( ) < 350) and (paddle_2.ycor( ) + 50 > ball.ycor( ) > paddle_2.ycor( ) - 50):
        ball.setx(340)
        ball.dx *= -1


# Run the Game after P was pressed on the main menu or the game was restarted
def run_game():

    # Creating Game Screen
    game_screen = turtle.Screen( )
    game_screen.bgpic("black.gif")
    game_screen.update( )
    game_screen.title("Welcome to Pong Game")
    game_screen.bgcolor("black")
    game_screen.setup(width=800, height=600)
    # Stop window from updating
    # Game speed is increased
    game_screen.tracer(0)
    # Paddle 1
    paddle_1 = pong_paddle.Paddle( )
    # Set shape and color of Paddle 1
    paddle_1.shape("square")
    paddle_1.color("blue")
    # Set position of the Paddle 1
    paddle_1.goto(-350, 0)

    # Paddle 2
    paddle_2 = pong_paddle.Paddle( )
    # Set shape and color of Paddle 2
    paddle_2.shape("square")
    paddle_2.color("red")
    # Set position of the Paddle 2
    paddle_2.goto(+350, 0)

    # Ball
    ball = pong_ball.Ball( )
    # Set shape and color of ball
    ball.shape("circle")
    ball.color("white")
    # Set position on the middle
    ball.goto(0, 0)

    # Scoreboard
    scoreboard = pong_scoreboard.ScoreBoard( )
    scoreboard.goto(0, 260)
    scoreboard.write("Home (Blue): 0 Away (Red): 0", align="center", font=("Verdana", 18, "normal"))

    # Generate Game Elements
    game_element = pong_game_elements.GameElements(scoreboard, ball, paddle_1, paddle_2, game_screen)
    game_element.running = True
    while game_element.running:
        # Keyboard binding
        game_screen.listen( )
        # Paddle 1 Moving
        game_screen.onkeypress(paddle_1.paddle_moving_up, "w")
        game_screen.onkeypress(paddle_1.paddle_moving_down, "s")
        # Paddle 2 Moving
        game_screen.onkeypress(paddle_2.paddle_moving_up, "i")
        game_screen.onkeypress(paddle_2.paddle_moving_down, "k")
        # Start game
        start_pong_game(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
        # Update screen
        game_screen.update( )
