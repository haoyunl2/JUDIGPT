# JUDIGPT Prompt Suggestions

This document provides a curated list of prompts you can use to test and interact with JUDIGPT. The prompts are organized by complexity and JUDI.jl functionality.

## Basic Modeling Prompts

### 2D Acoustic Modeling
1. **Minimal 2D simulation:**
   ```
   Write a minimal working example that builds a 2D acoustic wave simulation in JUDI.jl, including Model, Geometry, and a forward modeling operator.
   ```

2. **2D with specific parameters:**
   ```
   Create a 2D acoustic modeling example in JUDI.jl with a 200x150 grid, 10m spacing, constant velocity of 2.0 km/s, and a single source at the center.
   ```

3. **2D with multiple sources:**
   ```
   Write JUDI.jl code for a 2D acoustic simulation with 5 sources evenly spaced along the surface and receivers covering the entire model.
   ```

### 3D Acoustic Modeling
4. **Basic 3D:**
   ```
   Create a minimal 3D acoustic wave simulation in JUDI.jl with Model, Geometry, and forward modeling.
   ```

5. **3D with layered velocity:**
   ```
   Write JUDI.jl code for a 3D acoustic model with a two-layer velocity structure (1.5 km/s in upper layer, 3.0 km/s in lower layer).
   ```

## Advanced Modeling Prompts

### Extended Source
6. **Extended source modeling:**
   ```
   Create a JUDI.jl example using extended source modeling for 2D acoustic wave propagation.
   ```

7. **Extended source with LSQR:**
   ```
   Write JUDI.jl code that uses extended source modeling with LSQR solver for solving the inverse problem.
   ```

### Elastic Modeling
8. **Elastic wave propagation:**
   ```
   Create a 2D elastic wave modeling example in JUDI.jl that propagates both P and S waves.
   ```

### Wavefield Extraction
9. **Wavefield snapshots:**
   ```
   Write JUDI.jl code to extract and visualize wavefield snapshots at different time steps for a 2D acoustic simulation.
   ```

## Imaging & Inversion Prompts

### Reverse Time Migration (RTM)
10. **Basic RTM:**
    ```
    Create a JUDI.jl example that performs reverse time migration (RTM) on synthetic 2D seismic data.
    ```

11. **LSRTM:**
    ```
    Write JUDI.jl code for least-squares reverse time migration (LSRTM) with iterative optimization.
    ```

### Imaging Conditions
12. **Imaging condition comparison:**
    ```
    Create a JUDI.jl example that compares different imaging conditions (cross-correlation, deconvolution) for RTM.
    ```

### Full Waveform Inversion (FWI)
13. **Basic FWI setup:**
    ```
    Write JUDI.jl code to set up a 2D full waveform inversion (FWI) problem with a starting model and observed data.
    ```

14. **FWI with constraints:**
    ```
    Create a JUDI.jl FWI example with bound constraints on the velocity model (e.g., 1.5-5.0 km/s).
    ```

15. **FWI gradient computation:**
    ```
    Write JUDI.jl code to compute the FWI gradient for a 2D acoustic model using the adjoint-state method.
    ```

## Acquisition Geometry Prompts

16. **Custom geometry:**
    ```
    Create a JUDI.jl example with a custom acquisition geometry: sources at depth 50m, receivers at surface, recording for 2 seconds.
    ```

17. **Marine acquisition:**
    ```
    Write JUDI.jl code for a marine seismic acquisition setup with sources and receivers in the water column.
    ```

18. **Land acquisition:**
    ```
    Create a JUDI.jl example for land seismic acquisition with sources and receivers at the surface.
    ```

## Source Wavelet Prompts

19. **Ricker wavelet:**
    ```
    Write JUDI.jl code to create a Ricker wavelet source with 10 Hz peak frequency and use it in a forward modeling simulation.
    ```

20. **Custom source:**
    ```
    Create a JUDI.jl example with a custom source wavelet (e.g., a band-limited pulse) for 2D acoustic modeling.
    ```

## Model Setup Prompts

21. **Layered model:**
    ```
    Write JUDI.jl code to create a 2D layered velocity model with 3 layers of different velocities.
    ```

22. **Marmousi-like model:**
    ```
    Create a JUDI.jl example with a complex 2D velocity model similar to the Marmousi model (smooth variations).
    ```

23. **Model with anomaly:**
    ```
    Write JUDI.jl code for a 2D model with a high-velocity anomaly embedded in a constant background.
    ```

## Operator & Linear Algebra Prompts

24. **JudiModeling operator:**
    ```
    Create a JUDI.jl example that builds and applies a judiModeling operator for forward wave propagation.
    ```

25. **JudiJacobian operator:**
    ```
    Write JUDI.jl code to create and use a judiJacobian operator for linearized modeling (Born approximation).
    ```

26. **Adjoint test:**
    ```
    Create a JUDI.jl example that performs an adjoint test to verify the adjoint of the forward modeling operator.
    ```

27. **Projection operators:**
    ```
    Write JUDI.jl code using judiProjection operators to inject sources and extract data at receiver locations.
    ```

## Utility & Analysis Prompts

28. **Illumination analysis:**
    ```
    Create a JUDI.jl example that computes wavefield illumination for a given source-receiver geometry.
    ```

29. **Data visualization:**
    ```
    Write JUDI.jl code to visualize synthetic seismic shot records using PythonPlot or SlimPlotting.
    ```

30. **Model visualization:**
    ```
    Create a JUDI.jl example that plots the velocity model and overlays source/receiver positions.
    ```

## Complex Workflow Prompts

31. **Complete FWI workflow:**
    ```
    Write a complete JUDI.jl workflow for 2D FWI: generate synthetic data, set up inversion, compute gradient, and run a few optimization iterations.
    ```

32. **RTM to LSRTM pipeline:**
    ```
    Create a JUDI.jl example that starts with RTM imaging and then refines it using LSRTM with iterative updates.
    ```

33. **Multi-scale FWI:**
    ```
    Write JUDI.jl code for a multi-scale FWI approach, starting with low frequencies and progressively adding higher frequencies.
    ```

## Tips for Using Prompts

- **Start simple:** Begin with basic modeling prompts (#1-5) to verify the agent understands JUDI.jl syntax
- **Add complexity gradually:** Move to advanced prompts (#6-12) once basic examples work
- **Be specific:** Include details like grid size, velocity values, or time parameters for more accurate code generation
- **Request visualization:** Add "and plot the results" to prompts that should generate figures
- **Test error handling:** Try prompts with intentionally ambiguous requirements to see how the agent handles edge cases

## Current Working Prompt

Your current prompt works well:
```
Write a minimal working example that builds a 2D acoustic wave simulation in JUDI.jl, including Model, Geometry, and a forward modeling operator.
```

This is a good baseline. You can extend it by:
- Adding specific parameters: "with 100x80 grid and 10m spacing"
- Requesting visualization: "and plot the synthetic data"
- Adding complexity: "with multiple sources and receivers"
- Including inversion: "and compute the FWI gradient"

