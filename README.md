# MandelbrotSet

This repository implements the algorithm of the Mandelbrot set to create both static and dynamic representations of the set on a complex plane.

## Significance of the Mandelbrot Set

The Mandelbrot set is a famous fractal named after the mathematician Benoît B. Mandelbrot. It is a set of complex numbers that produces a distinctive, infinitely complex boundary when plotted. The set is defined by iterating the function:

\[ f_c(z) = z^2 + c \]

where \( z \) starts at zero and \( c \) is a complex parameter. The Mandelbrot set includes all values of \( c \) for which the orbit of \( z \) does not escape to infinity.

### Key Properties

- **Self-Similarity**: The boundary of the Mandelbrot set exhibits self-similarity at different scales, meaning smaller portions of the boundary resemble the whole set.
- **Complexity from Simplicity**: Despite being generated from a simple iterative process, the Mandelbrot set produces highly intricate and beautiful patterns.
- **Connection to Julia Sets**: Each point in the Mandelbrot set corresponds to a specific Julia set, another type of fractal.

## Mathematical Calculation

To determine if a complex number \( c \) is in the Mandelbrot set, we iterate the function \( f_c(z) = z^2 + c \) starting with \( z = 0 \). The number \( c \) is part of the Mandelbrot set if the absolute value of \( z \) remains bounded (does not go to infinity) after many iterations. Typically, the following steps are used:

1. Initialize \( z = 0 \).
2. Iterate the function \( z = z^2 + c \).
3. Check if \( |z| > 2 \) (if so, \( c \) is not in the Mandelbrot set).
4. Repeat for a maximum number of iterations or until \( |z| \) exceeds 2.

The number of iterations before \( z \) exceeds 2 can be used to color the point \( c \), creating a visual representation of the set.

## Features

- **Static Representation**: Generates a static image of the Mandelbrot set.
- **Dynamic Representation**: Creates an animated visualization of the Mandelbrot set's iterative process.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries: `numpy`, `matplotlib`, `pyopengl`

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/sparsh-karna/MandelbrotSet.git
    cd MandelbrotSet
    ```
2. Install the required libraries:
    ```sh
    pip install numpy matplotlib pyopengl
    ```

### Usage

#### Static Representation

To generate a static image of the Mandelbrot set:
```sh
python static/mandelbrot_static.py
```

#### Dynamic Representation

To visualize the Mandelbrot set dynamically:
```sh
python dynamic/mandelbrot_dynamic.py
```

## Project Structure

- `static/`: Contains the script for generating static images of the Mandelbrot set.
- `dynamic/`: Contains the script for creating dynamic visualizations of the Mandelbrot set.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please contact [Sparsh Karna](mailto:sparsh.karna@example.com).
```

You can copy this content into a file named `README.md` in your repository.



