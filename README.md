First steps:
determine what needs to be objects and what doesn't
- pipe
- bird
- ground

Neat functionality
- evolves a neural network
- say we have three input neurons and one output
    - changes the value of the weights
    - maybe add another node --> removes and adds connections
    - why?
- tries to find the best topology for the problem we're solving
    - if it doesn't need to be more complex, it won't be
    - if it finds a simple architecture, it'll use that so long as it performs better than a more complex one
- starts simple --> adds connections and nodes as the algorithm sees fit

What i need to give the NEAT module
- inputs
    - bird y posn (doesn't move along the x axis)
    - dist between the bird and the next top pipe, next bottom pipe
        - technically we could give it one of the pipes, but then we'd need to figure out the gap distance too
- outputs
    - jump? tis a leap of faith
- activation function
    - TanH (it's a hyperbolic tangent function uk what it looks like)
- pop size
    - arbitrary (it's just the number of birds we want to sacrifice for the greater good)
- FITNESS FUNCTION
    - however far the bird gets aka dist
- max generations
    - what we give up at (maybe 40)