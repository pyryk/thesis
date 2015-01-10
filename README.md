# Tools for Visualizing Geographical Data on the Web
## Reducing the Work Needed by Eliminating Boilerplate

[Download PDF](http://pyryk.github.io/thesis/thesis.pdf)

### Abstract

This thesis studies the effect of a reusable software tool on geographical visualizations on the web. In particular, the thesis studies the efficiency of development and the effectiveness of the resulting visualizations. During this thesis, I implemented and evaluated a reusable software tool for geovisualization on the web.

Geographical data is data with a geospatial dimension. Typically, geographical data is visualized on a map using a process called thematic mapping. In the past, thematic mapping was predominantly done by cartographers. However, with the advent of the web, the situation has changed. Currently, a majority of geographical visualizations is done by ordinary web users.

Before this work, no sufficient geovisualization tools for the web exist. General-purpose mapping libraries such as Google Maps API provide a low-level support for visualizations. However, generally, those tools are on too low abstraction level to support efficient building of complex visualizations.

During this work, I implemented Thematic.js, a reusable tool for thematic mapping on the web, and evaluated it using a sister project case study. I implemented several geographical visualizations with and without the tool and evaluated the effort needed for the implementations. I also examined the effect of the tool on visualization effectiveness by using visualization heuristics and objectives.