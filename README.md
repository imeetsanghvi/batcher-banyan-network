# Project 2 Batcher-Banyan-Network

IFT 510 Principles of Computer Information and Technology Architecture - Project Assignment 2 Submission

## Question
Create a computer program in the language of your choice that emulates a Banyan-Batcher-Network with 8x8 Inputs & Outputs. Then scale the output to 16x16 Delta Network. Use a random generator with 8 or 16 options to emulate the input table routing list with the assigned input port. Show that your simulation works for all inputs and outputs. Explain how your routing fabric changes when you have 16 inputs and outputs.

Make a video presentation that demonstrates how your network works. Submission - a youtube video link or MP4 file

## Deliverables
- Develop the expected values of any tests conducted that demonstrate how your program functions
    * 
- Provide a copy of your source code
- Provide a sequence of screenshots in the video to demonstrate the simulation and how the network works for all inputs and outputs (0-7). Ensure to separate the batcher sorter from the banyan network and how they work in conjunction
- Provide a detailed discussion of results, and the concepts you used in developing the program. Discussions should include analysis and a comparison of the results with the expected value from the theory. - Explained thoroughly in video
- Present the results in the video file and submit

### Explanation
A Banyan network could essentially route any input to any out but in case of conflicts at any particular intermediate state would result in the loss of packets which are being passed through. To avoid this packet loss in the delta network we sort the input first before passing it to the banyan(delta) network which then correctly finds the path for each packet and routes them. 

The main logic is to 
1. take the user input (a list of numbers)
2. This input goes through the batcher network first which basically sorts the input according to the desired locations for the banyan network.
3. Get the binary values of each data
4. At each column state A|B|C|D implement a switching pattern to find out the route that each packet will take
    1. for example - if the packet is 4 ==> 0100
    2. then 4 will first go to A5 as seen in the image below
    from A5 if the first value of binary is 0 goto B1 else B5
   3. Similarly, from B1 we check the binary value (0100 - 2nd column) if value is 0 go to c1 else c3
    in this way once we traverse through the switches we will be able to reach the destination output port correctly
      
![img.png](img.png)

### How to run this Code
1. The main logic is implemented inside bbn.py inside the main function
2. to run the flask project
    * Requirements 
        * pip install flask
3. just run ==> python app.py while inside the directory
    
## Output 
Image 1 - Input Options (default state load)

![img_1.png](img_1.png)

Image 2 - Correct Output

![img_2.png](img_2.png)

Image 3 - Output if there is an error in input

![img_3.png](img_3.png)