# Enabling Sample Efficient Design Space Exploration through Machine Learning Methods

## Project Overview

Engineering is driven by effective design space exploration and optimisation. Computational tools, such as computational fluid dynamics (CFD), are widely used to replace expensive physical testing by solving physical equations to provide flow field information, including surface pressure fields and velocity profiles. While these simulations provide accurate insights, they are computationally intensive and unsuitable for rapid, iterative design exploration.

One key bottleneck in accelerating design optimisation lies in the complexity of input geometries. Unstructured mesh files, point clouds, and other geometric representations lack simple parameterisation, making it difficult to capture and interpret the defining features of complex geometries. This high-dimensional landscape imposes significant computational burdens and exacerbates the curse of dimensionality, limiting efficient design optimisation.

By developing low-dimensional representations of complex shapes, it becomes feasible to apply optimisation methods such as grid search, Monte Carlo methods, and gradient-based algorithms more efficiently. This project investigates how various AI models can encode complex geometries into compact, interpretable representations to enhance design space exploration and optimisation.

## Project Objectives

1. **Research and Compare AI Models**: Explore and evaluate different AI approaches for encoding geometries into low-dimensional spaces, including:

   - Autoencoders (AEs)
   - Encoder-Decoders
   - Generative Adversarial Networks (GANs)

2. **Facilitate Design Space Exploration**: Assess how these learned representations can enable more efficient exploration of geometric quantities of interest for optimisation tasks.

3. **Analyse Geometry Representations**: Evaluate the structure, smoothness, and interpretability of the learned geometry representations and their suitability for:

   - Gradient-based optimisation
   - Genetic algorithms
   - Bayesian optimisation

4. **Optimisation Task**: Implement the learned representations on a 2D optimisation problem—specifically, minimising the area-to-perimeter ratio. While this serves as a simplified analogy to real-world engineering challenges (e.g., optimising lift-to-drag ratios in aerospace), the methodologies can be extended to other domains.

## Why Focus on 2D Geometries?

While industry applications typically focus on 3D geometries, the computational overhead and data availability present unnecessary challenges that obscure the core research aims. By focusing on 2D shapes, this project can systematically explore and compare AI-based encoding methods without being constrained by the computational demands of 3D simulations.

## Significance of the Research

Generative models have become pivotal in engineering due to their ability to compress high-complexity processes into a manageable, low-dimensional search space. This research aims to:

- Identify which generative models best capture and represent complex geometries.
- Demonstrate how low-dimensional representations facilitate efficient design optimisation.
- Provide insights into interpretable and controllable geometric representations that support targeted design modification.

The outcomes of this project aim to advance the use of AI-driven geometry encoding for engineering design, offering scalable solutions for rapid and efficient design exploration.

## Repository Structure

```
├── data/                  # Datasets and preprocessed geometry files
├── models/                # Implementation of AE, GAN, and other models
├── notebooks/             # Jupyter notebooks for exploration and visualization
├── results/               # Outputs, figures, and analysis
└── README.md              # Project documentation
```



