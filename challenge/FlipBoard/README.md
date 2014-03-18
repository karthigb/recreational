A challenge from FlipBoard described as so:

"Hello!

This is a challenge that requires you to construct a program that will complete a maze. Each step of the maze is done by accessing a URL that returns the next set of moves. If the response body contains end:true then your program is complete and it should print out the steps it used to get there. Bonus points if your program can also display a human-understandable representation of the maze you just completed.

You may use any language to write the program, the only caveat is that it must be buildable and runnable on common, modern operating systems (definition of which is intentionally loose). We won’t accept pseudo-code :)

Access this link (https://challenge.flipboard.com/m) to begin. You can start a new maze at any time by returning to the same link (https://challenge.flipboard.com/m).
What you should submit

    The output of your program for one maze. This should be a list of the points along the path that takes you from the initial URL to the final URL which returns a response containing end:true.
    The code you used to generate the output.
    (Optional) Have your code also output a representation of the maze it just completed."

The output may be so:

end:true/(n, n)*

or

end:false/(n, n)*

Where * represents the coordinate term can occur one or more times.

My graphical representation of the maze is the moment I completed the maze (any unexplored area is a mystery).
