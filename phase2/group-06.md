# Group 06

## Practical details

Students:

- Rebekka Reimund
- Sonja Wüst

### Wednesday (July 03)

Summary of feedback after first week

Below, you'll find a summary of our discussion.

**Activity:**

- Existing useful code for tasks (a) and (b).
- Some nice plots already there. Good!

**Other feedback:**

- The $j$ in $\{\tau^j : j \in \mathbb{N}\}$ represents the exponential power of $\tau$.

### Wednesday (July 10)

Summary of feedback after second week

Below, you'll find a summary of our discussion.

**Activity:**

- Existing useful code for all basic requirements and some of extensions.
- Some nice plots already there with some issues to be fixed.

**Other feedback:**

- I made a mistake when I wrote `function2` where I wrote `x[0] ** 2 + x[1] ** 2`, so it doesn't work. But these two methods are equivalent.

    ```python
    import numpy as np

    x = np.arange(10)
    X, Y = np.meshgrid(x, x)


    def function(X, Y):
        Z = X**2 + Y**5
        return Z


    def function2(x):
        return x[0] ** 2 + x[1] ** 5


    Z1 = function(X, Y)
    print(f"Z1 from {function.__name__}")
    print(Z1)

    Z2 = function2([X, Y])
    print(f"Z2 from {function.__name__}")
    print(Z2)
    assert (Z1 == Z2).all()
    ```
