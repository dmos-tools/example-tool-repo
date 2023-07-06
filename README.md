# Example tool

This is an example repository for onboarding a tool to [Ontologic](https://run.ontologic.ly). It contains a Python script (plotologic) with a simple function that plots a line and saves the resulting figure as an image.

## Setting dependencies
### Base environment
This is a Python-based tool, so the base environment should install Python 3.

### Tool code

The custom code used in this tool is contained in this repository, and can be added to the tool environment with the following link: https://github.com/ontologicly/example-tool-repo.git

Alternately, you can click on the green "Code" button on the Github page for this repository an copy the HTTPS link for cloning.

## Other dependencies

This tool uses the following Python libraries, which can be installed using Pip:
  - numpy
  - matplotlib

## Configuring the tool

### Tool script

To run the tool, use the following:

```
from plotologic import makeplot
import matplotlib.pyplot as plt

makeplot(slope, intercept, title)

plt.savefig('outputs/output.png')
```

### Parameters
The tool requires three parameters:
  - slope: a decimal that determines the steepness of the line.
  - intercept: a decimal that determines where the line crosses the y-axis.
  - title: a string that is placed at the top of the plot.

