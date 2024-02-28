#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 23:35:32 2022

@author: jordanlubbers
"""

import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler
from matplotlib.text import Annotation
from matplotlib.transforms import Affine2D

# rebuild fonts list...for if you recently
# added a new ttf file.
# matplotlib.font_manager._rebuild()

# removes the matplotlib cache so fonts always work
# this is usually in the form of a json file with
# "fontlist" somewhere in the filename.
cache_dir = matplotlib.get_cachedir()

# for windows paths
for file in os.listdir(cache_dir):
    if "fontlist" in file:
        os.remove(cache_dir + "\\" + file)


# setting matplotlib defaults
p = plt.rcParams

p["pdf.fonttype"] = 42

# figure-wide aesthetics
p["figure.figsize"] = [4, 4]
p["figure.edgecolor"] = "#000000"
p["figure.facecolor"] = "#ffffff"
# p["figure.dpi"] = 300
p["savefig.dpi"] = 300
p["figure.titlesize"] = 24
p["figure.constrained_layout.use"] = True
p["savefig.bbox"] = "tight"

# axes-level aesthetics
p["axes.linewidth"] = 2
p["axes.facecolor"] = "whitesmoke"
p["axes.labelsize"] = 18
p["axes.prop_cycle"] = cycler(
    "color",
    [
        "#009ADE",
        "#FF1F5B",
        "#00CD6C",
        "#AF58BA",
        "#FFC61E",
        "#089099",
        "#F28522",
        "#A0B1BA",
        "#045275",
    ],
)
p["axes.titlesize"] = 20
p["axes.titlelocation"] = "left"

p["errorbar.capsize"] = 0

# grid
p["grid.color"] = "gray"
p["grid.linewidth"] = 0.5


# font stuff
p["font.family"] = "sans-serif"
# on my computer good options for sans serif are
# Arial, Univers Condensed, CMU Sans Serif, Fira Sans Condensed
p["font.sans-serif"] = ["CMU Sans Serif"]
# computer modern for serif fonts
p["font.serif"] = ["CMU Serif"]
p["mathtext.fontset"] = "stixsans"


# x-tick customization
p["xtick.bottom"] = True
p["xtick.top"] = True
p["xtick.direction"] = "out"
p["xtick.major.size"] = 5
p["xtick.major.width"] = 1
p["xtick.minor.size"] = 3
p["xtick.minor.width"] = 0.5
p["xtick.minor.visible"] = False
p["xtick.labelsize"] = 10


# y-tick customization
p["ytick.left"] = True
p["ytick.right"] = True
p["ytick.direction"] = "out"
p["ytick.major.size"] = 5
p["ytick.major.width"] = 1
p["ytick.minor.size"] = 3
p["ytick.minor.width"] = 0.5
p["ytick.minor.visible"] = False
p["ytick.labelsize"] = 10


# marker customization
p["lines.linewidth"] = 1.5
p["lines.marker"] = ""
p["lines.markeredgewidth"] = 0.5
p["lines.markeredgecolor"] = "k"
p["lines.markerfacecolor"] = "auto"
p["lines.markersize"] = 6


def create_colorblind_palette(n=9):
    if n <= 9:
        if n == 1:
            colors = ["#FF1F5B"]
        elif n == 2:
            colors = [
                "#009ADE",
                "#FF1F5B",
            ]

        elif n == 3:
            colors = ["#009ADE", "#FF1F5B", "#FFC61E"]
        elif n == 4:
            colors = ["#009ADE", "#FF1F5B", "#AF58BA", "#FFC61E"]
        elif n == 5:
            colors = ["#009ADE", "#FF1F5B", "#AF58BA", "#FFC61E", "#F28522"]
        elif n == 6:
            colors = [
                "#009ADE",
                "#FF1F5B",
                "#00CD6C",
                "#AF58BA",
                "#FFC61E",
                "#089099",
            ]
        elif n == 7:
            colors = [
                "#009ADE",
                "#FF1F5B",
                "#00CD6C",
                "#AF58BA",
                "#FFC61E",
                "#089099",
                "#F28522",
            ]
        elif n == 8:
            colors = [
                "#009ADE",
                "#FF1F5B",
                "#00CD6C",
                "#AF58BA",
                "#FFC61E",
                "#089099",
                "#F28522",
                "#A0B1BA",
            ]

        else:
            colors = [
                "#009ADE",
                "#FF1F5B",
                "#00CD6C",
                "#AF58BA",
                "#FFC61E",
                "#089099",
                "#F28522",
                "#A0B1BA",
                "#045275",
            ]
    else:
        raise Exception("Please choose 9 colors or less")

    return colors


# helper function for removing the top
# and right spines for a simple looking plot
def left_bottom_axes(ax):
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.set_facecolor("white")


# helper function for removing the top
# and right spines for a simple looking plot
def bottom_only_axes(ax):
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.set_yticks([])
    ax.get_xaxis().tick_bottom()
    ax.set_facecolor("white")


import string

# helper for labeling subplots
from matplotlib.offsetbox import AnchoredText


def label_subplots(axes, location, fontsize=14, alpha=0.5, **kwargs):
    if len(axes.shape) > 1:
        axes = axes.ravel()
    letters = list(string.ascii_uppercase)

    for a, letter in zip(axes, letters):
        at = AnchoredText(
            "{}".format(letter),
            prop=dict(size=fontsize),
            frameon=True,
            loc=location,
            **kwargs,
        )
        at_noletters = AnchoredText(
            "{}".format(letter),
            prop=dict(size=fontsize, color="white"),
            frameon=True,
            loc=location,
            **kwargs,
        )

        at_noletters.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
        at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
        at.patch.set_linewidth(2)

        at_noletters.patch.set_facecolor("white")
        at.patch.set_facecolor("none")

        at_noletters.patch.set_alpha(alpha)
        a.add_artist(at_noletters)
        a.add_artist(at)


def make_dark_bkgd_compatible(
    ax=None,
    color="w",
    bkgd_color="k",
    spines=False,
    has_colorbar=False,
    cbar=None,
    **tick_kwargs,
):
    """Make your figures dark background compatible by changing
        the spines, tickmarks/labels, axis labels, and title to a color of
        your choosing

        Will NOT do suplabels for the figure. Just manually do these
            fig.supxlabel(label, color = 'w')

    Args:
        ax (_matplotlib axis object_): da figure to make dark background
        compatible. Defaults to None.

        color (str, optional): The color to change everything to. Defaults to "w".
        Will accept any matplotlib color value (e.g., names, hex codes, rgb values)

        bkgd_color (str, optional): background color for the figure. Defaults to "k".
        Will accept any matplotlib color value (e.g., names, hex codes, rgb values)

        spines (bool, optional): Whether or not to change the color of the spines.
        Defaults to False.

        has_colorbar (bool, optional): Whether or not the figure has a colorbar.
        Defaults to False.

        cbar (matplotlib colorbar, optional): The colorbar object to change the colors of
        similar to the actual figure. Only applies if has_colorbar = True.
        Defaults to None.

        **tick_kwargs : other customizations found here
        https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html
    """

    if ax is None:
        ax = plt.gca()
    if spines is True:
        for spine in ["top", "bottom", "left", "right"]:
            ax.spines[spine].set_color(color)

    ax.tick_params(
        axis="both",
        which="both",
        color=color,
    )
    ax.set_xticks(ax.get_xticks())
    ax.set_xticklabels(ax.get_xticklabels(), color=color)

    ax.set_yticks(ax.get_yticks())
    ax.set_yticklabels(ax.get_yticklabels(), color=color)

    ax.tick_params(axis="both", which="both", color="w", **tick_kwargs)

    xlabel = ax.xaxis.get_label()
    ax.set_xlabel(xlabel.get_text(), color=color)

    ylabel = ax.yaxis.get_label()
    ax.set_ylabel(ylabel.get_text(), color=color)

    title = ax.get_title()
    ax.set_title(title, color=color)

    if has_colorbar is True:
        cbar_ticks = cbar.get_ticks()
        cbar.set_ticks(cbar_ticks)
        cbar.set_ticklabels(np.round(cbar_ticks, 1), color=color)
        cbar.ax.tick_params(axis="both", which="both", color="w", **tick_kwargs)

    fig = plt.gcf()
    fig.set_facecolor(bkgd_color)


class LineAnnotation(Annotation):
    """A sloped annotation to *line* at position *x* with *text*
    Optionally an arrow pointing from the text to the graph at *x* can be drawn.
    Usage
    -----
    fig, ax = subplots()
    x = linspace(0, 2*pi)
    line, = ax.plot(x, sin(x))
    ax.add_artist(LineAnnotation("text", line, 1.5))
    """

    def __init__(
        self, text, line, x, xytext=(0, 5), textcoords="offset pixels", **kwargs
    ):
        """Annotate the point at *x* of the graph *line* with text *text*.

        By default, the text is displayed with the same rotation as the slope of the
        graph at a relative position *xytext* above it (perpendicularly above).

        An arrow pointing from the text to the annotated point *xy* can
        be added by defining *arrowprops*.

        Parameters
        ----------
        text : str
            The text of the annotation.
        line : Line2D
            Matplotlib line object to annotate
        x : float
            The point *x* to annotate. y is calculated from the points on the line.
        xytext : (float, float), default: (0, 5)
            The position *(x, y)* relative to the point *x* on the *line* to place the
            text at. The coordinate system is determined by *textcoords*.
        **kwargs
            Additional keyword arguments are passed on to `Annotation`.

        See also
        --------
        `Annotation`
        `line_annotate`
        """
        assert textcoords.startswith(
            "offset "
        ), "*textcoords* must be 'offset points' or 'offset pixels'"

        self.line = line
        self.xytext = xytext

        # Determine points of line immediately to the left and right of x
        xs, ys = line.get_data()

        def neighbours(x, xs, ys, try_invert=True):
            (inds,) = np.where((xs <= x)[:-1] & (xs > x)[1:])
            if len(inds) == 0:
                assert try_invert, "line must cross x"
                return neighbours(x, xs[::-1], ys[::-1], try_invert=False)

            i = inds[0]
            return np.asarray([(xs[i], ys[i]), (xs[i + 1], ys[i + 1])])

        self.neighbours = n1, n2 = neighbours(x, xs, ys)

        # Calculate y by interpolating neighbouring points
        y = n1[1] + ((x - n1[0]) * (n2[1] - n1[1]) / (n2[0] - n1[0]))

        kwargs = {
            "horizontalalignment": "center",
            "rotation_mode": "anchor",
            **kwargs,
        }
        super().__init__(text, (x, y), xytext=xytext, textcoords=textcoords, **kwargs)

    def get_rotation(self):
        """Determines angle of the slope of the neighbours in display coordinate system"""
        transData = self.line.get_transform()
        dx, dy = np.diff(transData.transform(self.neighbours), axis=0).squeeze()
        return np.rad2deg(np.arctan2(dy, dx))

    def update_positions(self, renderer):
        """Updates relative position of annotation text
        Note
        ----
        Called during annotation `draw` call
        """
        xytext = Affine2D().rotate_deg(self.get_rotation()).transform(self.xytext)
        self.set_position(xytext)
        super().update_positions(renderer)


def line_annotate(text, line, x, *args, **kwargs):
    """Add a sloped annotation to *line* at position *x* with *text*

    Optionally an arrow pointing from the text to the graph at *x* can be drawn.

    Usage
    -----
    x = linspace(0, 2*pi)
    line, = ax.plot(x, sin(x))
    line_annotate("sin(x)", line, 1.5)

    See also
    --------
    `LineAnnotation`
    `plt.annotate`
    """
    ax = line.axes
    a = LineAnnotation(text, line, x, *args, **kwargs)
    if "clip_on" in kwargs:
        a.set_clip_path(ax.patch)
    ax.add_artist(a)
    return a
