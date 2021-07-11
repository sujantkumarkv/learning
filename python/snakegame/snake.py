import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# Since each turtle is 20px long & we are taking 3 to make our initial snake.
STEP_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():

    def __init__(self):

        # super().__init__()
        self.bauaas_list = []
        self.create_snake()  # eachtime we call Snake() class creating on OBJECT; it calls a
        # function specially for our 3 turtle long snake
        self.first_turtle = self.bauaas_list[0]

        # I can't create this first_turtle ATTRIBUTE to snake object before the above line bcz here I'm calling
        # bauaas_list[0] and before self.create_initial_snake() ; bauaas_list is empty 7 we can't call its 1st element;
        # and that would give an error..

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_bauaa(position)

    def add_bauaa(self, position):
        new_bauaa = turtle.Turtle(shape="square")
        new_bauaa.color("white")
        new_bauaa.penup()
        new_bauaa.goto(position)
        self.bauaas_list.append(new_bauaa)

    def extend(self):
        self.add_bauaa(self.bauaas_list[-1].pos())

    def snake_head_pos(self):
        return self.first_turtle.position()

    def move(self):

        # for turtle_segment in bauaas_list: ##PROBLEM WITH THIS LOOP CODE IS IF WE TURN A TURTLE, OTHER 2 WILL KEEP
        #     turtle_segment.forward(20)    ## ON MOOVING FORWARDS BCZ THAT'S WHAT SAID; INSTEAD BETTER APPROCH IS TO MAKE
        ## FOLLOW EACH TURTLE THE PATH OF THE TURTLE IN-FRONT OF IT.

        # for bauaa_no in range(len(bauaas_list)-1):
        #     # x_cor= bauaas_list[bauaa_no].xcor()
        #     # y_cor= bauaas_list[bauaa_no].ycor()
        #     bauaas_list[bauaa_no+1].goto(bauaas_list[bauaa_no].pos())

        # The -above Loop works but one issue ; we update position of a turtle object w.r.t one before it ; we go from top to
        # bottom in list of objectlist, so say when 3 wants to goto pos() of 2, 2 has already moved to pos() of 1;So, what we
        # actually want is to move 3 to 2's older pos() but its now changed to 1's pos(). So, overall appears asif length of snake
        # decreases & then it moves in that way.
        # Therefore this doesn't work; We have to change the pos() of later turtle to its forwards turtle pos() before moving
        # forward one 1st; Therefore going in reverse is the way !!

        for bauaa_no in range(len(self.bauaas_list) - 1, 0, -1):
            # start=first term, stop=0(EXCLUDES), step=-1
            # (x_cor, y_cor)= bauaas_list[bauaa_no - 1].pos()
            # pos_tuple= bauaas_list[bauaa_no - 1].pos()
            self.bauaas_list[bauaa_no].goto(self.bauaas_list[bauaa_no - 1].pos())

        self.first_turtle.forward(STEP_DISTANCE)
        # first_turtle.left(90)

    # In the code below, I did mistake by calling "self.setheading" BUT, self is snake object created by me & surely
    # it doesn't have the setheading feature,a turtle OBJECT has it; so call it from bauaas_list BCZ its a list of
    # turtle objects after-all & then can use "setheading" functionality.
    def up(self):
        if self.first_turtle.heading() != DOWN:
            self.first_turtle.setheading(UP)
            self.move()

    def down(self):
        if self.first_turtle.heading() != UP:
            self.first_turtle.setheading(DOWN)
            self.move()

    def right(self):
        if self.first_turtle.heading() != LEFT:  # I did a typo BLUNDER; wrote condn as *==* LEFT; so left keystrokes
            # didn't respond ..
            self.first_turtle.setheading(RIGHT)
            self.move()

    def left(self):
        if self.first_turtle.heading() != RIGHT:  # I did a typo BLUNDER; wrote condn as *==* RIGHT; so left keystrokes
            # didn't respond ..
            self.first_turtle.setheading(LEFT)
            self.move()
