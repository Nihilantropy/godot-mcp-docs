allow_comments
:   False

# Performance {#doc_performance}

## Introduction

Godot follows a balanced performance philosophy. In the performance
world, there are always tradeoffs, which consist of trading speed for
usability and flexibility. Some practical examples of this are:

- Rendering large amounts of objects efficiently is easy, but when a
  large scene must be rendered, it can become inefficient. To solve
  this, visibility computation must be added to the rendering. This
  makes rendering less efficient, but at the same time, fewer objects
  are rendered. Therefore, the overall rendering efficiency is improved.
- Configuring the properties of every material for every object that
  needs to be rendered is also slow. To solve this, objects are sorted
  by material to reduce the costs. At the same time, sorting has a cost.
- In 3D physics, a similar situation happens. The best algorithms to
  handle large amounts of physics objects (such as SAP) are slow at
  insertion/removal of objects and raycasting. Algorithms that allow
  faster insertion and removal, as well as raycasting, will not be able
  to handle as many active objects.

And there are many more examples of this! Game engines strive to be
general-purpose in nature. Balanced algorithms are always favored over
algorithms that might be fast in some situations and slow in others, or
algorithms that are fast but are more difficult to use.

Godot is not an exception to this. While it is designed to have backends
swappable for different algorithms, the default backends prioritize
balance and flexibility over performance.

With this clear, the aim of this tutorial section is to explain how to
get the maximum performance out of Godot. While the tutorials can be
read in any order, it is a good idea to start from
`doc_general_optimization`{.interpreted-text role="ref"}.

## Common

::: {#toc-learn-features-general-optimization .toctree maxdepth="1"}
general_optimization using_servers
:::

## CPU

::: {#toc-learn-features-cpu-optimization .toctree maxdepth="1"}
cpu_optimization
:::

## GPU

::: {#toc-learn-features-gpu-optimization .toctree maxdepth="1"}
gpu_optimization using_multimesh pipeline_compilations
:::

## 3D

::: {#toc-learn-features-3d-optimization .toctree maxdepth="1"}
optimizing_3d_performance vertex_animation/index
:::

## Threads

::: {#toc-learn-features-threads .toctree maxdepth="1"}
using_multiple_threads thread_safe_apis
:::
