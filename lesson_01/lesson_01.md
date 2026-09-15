# Lesson 1 — What Is Manim?

Welcome to **Manim**. We will learn it step by step from absolute beginner level, with the eventual goal of creating mathematical animations for **vectors, vector operations, dot product, cross product, and functions of a single variable**.

By the end of this lesson, you will understand the basic Manim workflow and create your first animation.

---

## 1. What is Manim?

**Manim** stands for **Mathematical Animation Engine**.

It is a Python-based framework for creating **mathematical animations programmatically**.

Instead of manually drawing an animation frame by frame, you write Python code describing:

* what mathematical objects you want,
* where they should appear,
* how they should look,
* and how they should move or transform.

For example, you can create:

* points
* lines
* arrows
* vectors
* coordinate systems
* graphs
* equations
* matrices
* circles
* geometric shapes
* text
* 3D objects

and animate them.

For your eventual goal, Manim is particularly useful because you can create animations such as:

> A vector starts at the origin → its head moves → its components appear → the vector is decomposed into x and y components → its magnitude is displayed.

That is much easier to control programmatically than with ordinary video-editing software.

---

# 2. How Manim Works

The basic idea is:

```text
Python code
    ↓
Scene
    ↓
Mobjects
    ↓
Animations
    ↓
Manim renderer
    ↓
Video
```

Let's understand each part.

---

## 3. Scene

A **Scene** is the main container for an animation.

Think of a Scene as a **canvas/movie sequence**.

For example:

```python
from manim import *

class HelloManim(Scene):
    def construct(self):
        ...
```

Here:

```python
class HelloManim(Scene):
```

creates a Manim scene called `HelloManim`.

The important method is:

```python
def construct(self):
```

This is where we tell Manim what should happen in our animation.

You can think of it as:

> "Manim, build my animation here."

---

# 4. Objects: Mobjects

Manim calls its objects **Mobjects**.

The word means:

> **M**anipulatable **Object**

Examples include:

```python
Circle()
Square()
Line()
Arrow()
Dot()
Text()
MathTex()
```

For example:

```python
circle = Circle()
```

creates a circle.

Or:

```python
square = Square()
```

creates a square.

Or:

```python
text = Text("Hello Manim")
```

creates a text object.

Later, when we study vectors, you will frequently use objects such as:

```python
Arrow()
Line()
Dot()
NumberPlane()
Axes()
MathTex()
```

---

# 5. Animations

Creating an object isn't enough.

For example:

```python
circle = Circle()
```

creates a circle, but doesn't automatically make it appear as an animation.

Manim provides animation commands.

For example:

```python
self.play(Create(circle))
```

means approximately:

> Animate the creation of the circle.

Another example:

```python
self.play(FadeIn(circle))
```

means:

> Gradually make the circle appear.

And:

```python
self.play(FadeOut(circle))
```

means:

> Gradually make the circle disappear.

---

# 6. `self.play()`

You will use this command **constantly** in Manim:

```python
self.play(...)
```

For example:

```python
self.play(Create(circle))
```

The structure is:

```text
self.play(
    animation
)
```

For example:

```python
self.play(Create(square))
```

or:

```python
self.play(FadeIn(text))
```

or:

```python
self.play(Write(text))
```

You can think of `self.play()` as:

> "Play this animation in my scene."

---

# 7. `self.wait()`

Another extremely important command is:

```python
self.wait()
```

It tells Manim to pause the animation.

For example:

```python
self.play(Create(circle))
self.wait()
self.play(FadeOut(circle))
```

The sequence is:

```text
Create circle
      ↓
Pause
      ↓
Remove circle
```

You can also specify the duration:

```python
self.wait(2)
```

means approximately:

> Wait for 2 seconds.

---

# 8. The Complete Manim Workflow

Now let's put everything together.

Suppose we want to display a circle.

We write:

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.wait(2)
```

Manim processes this approximately as:

```text
                 Python file
                     │
                     ▼
              MyScene(Scene)
                     │
                     ▼
              construct()
                     │
                     ▼
                Circle()
                     │
                     ▼
              Create(circle)
                     │
                     ▼
              Render frames
                     │
                     ▼
                Video file
```

---

# 9. How a `.py` File Becomes a Video

This is one of the most important concepts to understand.

Suppose you create:

```text
hello.py
```

Inside it:

```python
from manim import *

class HelloManim(Scene):
    def construct(self):
        text = Text("Hello Manim")
        self.play(Write(text))
        self.wait(2)
```

The `.py` file itself is **not the video**.

It is the **instructions for producing the video**.

When you run Manim, it:

1. Reads your Python code.
2. Finds the Scene.
3. Creates the mathematical objects.
4. Executes the animations.
5. Calculates/render frames.
6. Combines those frames into a video.
7. Saves the resulting video.

Conceptually:

```text
hello.py
   │
   │ Manim
   ▼
Scene
   │
   ▼
Mobjects
   │
   ▼
Animations
   │
   ▼
Rendered frames
   │
   ▼
MP4 video
```

This is why Manim is different from simply drawing something in Python.

---

# 10. Community Edition vs Other Manim Versions

You will encounter the word **Manim** in different contexts.

The most important distinction for you is:

### Manim Community Edition

Usually called:

```text
Manim Community Edition
```

or simply:

```text
Manim
```

It is the modern community-maintained version and is the version we should use for your learning.

Its Python package is generally imported with:

```python
from manim import *
```

There was also an earlier version associated with the original project by **3Blue1Brown**, often referred to as **ManimGL**.

You may encounter tutorials using:

```text
ManimGL
```

or older Manim syntax.

### Important for our course

We will use **Manim Community Edition**, not older ManimGL tutorials/syntax.

So when you find an online tutorial, be careful about its Manim version. Code written for older versions may not work exactly the same way.

---

# 11. Your First Manim Program

Let's now create our first real program.

Create a file called:

```text
hello_manim.py
```

Put this inside:

```python
from manim import *

class HelloManim(Scene):
    def construct(self):
        text = Text("Hello Manim")

        self.play(Write(text))
        self.wait(2)
```

Let's understand it line by line.

---

## Line 1

```python
from manim import *
```

This imports Manim.

It gives our Python program access to Manim's classes and functions.

For example:

```python
Scene
Text
Circle
Square
Create
Write
FadeIn
```

and many others.

---

## Line 2

```python
class HelloManim(Scene):
```

We create a Scene named:

```text
HelloManim
```

It inherits from:

```python
Scene
```

So:

```python
HelloManim(Scene)
```

means that `HelloManim` is a Manim Scene.

---

## Line 3

```python
def construct(self):
```

This defines the `construct()` method.

Your animation instructions go inside this method.

---

## Line 4

```python
text = Text("Hello Manim")
```

This creates a text Mobject.

Conceptually:

```text
Text
 │
 └── "Hello Manim"
```

We store it in:

```python
text
```

---

## Line 5

```python
self.play(Write(text))
```

This tells Manim to animate writing the text onto the screen.

---

## Line 6

```python
self.wait(2)
```

This keeps the text visible for about two seconds.

---

# 12. Rendering Your First Animation

From your terminal, go to the directory containing:

```text
hello_manim.py
```

Then run:

```bash
manim -pql hello_manim.py HelloManim
```

Let's break that command down.

### `manim`

Runs Manim.

### `hello_manim.py`

The Python file containing our Scene.

### `HelloManim`

The Scene we want to render.

### `-p`

Preview the resulting video after rendering.

### `-ql`

Render at **low quality**, which is useful while learning because rendering is faster.

So:

```bash
manim -pql hello_manim.py HelloManim
```

basically means:

> Render the `HelloManim` Scene from `hello_manim.py` at low quality and preview the result.

---

# 13. What Will You See?

The resulting animation should show:

```text
        Hello Manim
```

with the text being written onto the screen.

Then it remains visible for two seconds.

Conceptually:

```text
Time →

[             ]
[ Hello       ]
[             ]

        ↓

[             ]
[ Hello Manim ]
[             ]

        ↓

       wait
```

Congratulations — you've created your first Manim animation. 🎉

---

# 14. Your First Modification

Now change:

```python
text = Text("Hello Manim")
```

to:

```python
text = Text("Hello Aamir")
```

Run:

```bash
manim -pql hello_manim.py HelloManim
```

You should get:

```text
Hello Aamir
```

This demonstrates an important Manim principle:

> **The Python code is the source of your animation.**

Change the code → render again → get a new video.

---

# 15. Mini-Project — "Hello Manim"

Now let's make the mini-project slightly more interesting.

Create:

```python
from manim import *

class HelloManim(Scene):
    def construct(self):
        text = Text("Hello Manim")

        self.play(Write(text))
        self.wait(2)

        self.play(FadeOut(text))
        self.wait(1)
```

The animation is now:

```text
                 Hello Manim
                     │
                     │ Write
                     ▼
              "Hello Manim"
                     │
                     │ wait 2 sec
                     ▼
              "Hello Manim"
                     │
                     │ FadeOut
                     ▼
                   empty
```

Render it:

```bash
manim -pql hello_manim.py HelloManim
```

---

# 16. Mini-Project Challenge

Before moving to Lesson 2, modify the project yourself.

Try to make this sequence:

```text
Hello
  ↓
Hello Manim
  ↓
Hello Manim!
  ↓
disappear
```

**Do not worry if you cannot do it yet.** The purpose is to start thinking in terms of:

```text
Object → Animation → Wait → Animation
```

A possible tool you will eventually learn for this is `Transform`, but **don't look it up yet**. We'll learn it properly.

---

# 17. The Most Important Mental Model

For now, remember this:

### Manim = Objects + Animations

For example:

```python
circle = Circle()
```

means:

> Create an object.

Then:

```python
self.play(Create(circle))
```

means:

> Animate that object.

Then:

```python
self.wait(2)
```

means:

> Keep the current scene visible.

So a Manim program often looks conceptually like:

```python
create object

animate object

wait

animate object

wait

remove object
```

This pattern will become the foundation for everything we do later.

---

# 18. Connection to Your Final Goal

Eventually, we'll build animations like this:

### Vector

```text
                 ●
                ↗
               /
              /
             /
            O
```

### Vector addition

```text
      b
      ↗
     /
    ●────→ a

       ↓

      a + b
```

### Dot product

```text
a · b = |a||b|cosθ
```

with the angle and projections animated.

### Cross product

```text
        a
       ↗
      /
     O ───→ b

        ↓

      a × b
```

### Single-variable function

```text
       y
       ↑
       │       ●
       │     ●
       │   ●
       │ ●
       └──────────→ x
```

But we won't jump directly into those. We'll build the skills systematically.

---

# Lesson 1 — What You Should Know Now

You should now be able to explain:

| Concept       | Meaning                                                        |
| ------------- | -------------------------------------------------------------- |
| **Manim**     | Python framework for mathematical animations                   |
| **Scene**     | Container for an animation                                     |
| **Mobject**   | Object that can be displayed/manipulated                       |
| **Animation** | Action applied to a Mobject                                    |
| `construct()` | Where the Scene's animation instructions are written           |
| `self.play()` | Plays an animation                                             |
| `self.wait()` | Pauses/holds the scene                                         |
| `Text()`      | Creates a text Mobject                                         |
| `Write()`     | Animates writing an object                                     |
| `FadeOut()`   | Animates removing/fading an object                             |
| `.py` file    | Python instructions for generating the animation               |
| Renderer      | Converts the animation instructions into rendered frames/video |

The core workflow to memorize is:

```text
                 MANIM WORKFLOW

                  Python .py
                       │
                       ▼
                    Scene
                       │
                       ▼
                   Mobjects
                       │
                       ▼
                  Animations
                       │
                       ▼
                   Rendering
                       │
                       ▼
                  Video (.mp4)
```

## Your Lesson 1 task

Create and successfully render:

```text
Hello Manim
```

using:

```bash
manim -pql hello_manim.py HelloManim
```

Then try the mini-project sequence:

```text
Hello
  ↓
Hello Manim
  ↓
Hello Manim!
  ↓
disappear
```

**Don't move to Lesson 2 until you can create and render the basic `Hello Manim` animation yourself.** In Lesson 2, we'll learn the **Manim coordinate system, points, positions, directions, and placing objects on the screen**—the foundation we need before drawing vectors.
