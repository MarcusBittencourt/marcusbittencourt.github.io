Title: R plots using plotly library
Category: Data Science
Date: 22/05/2019 09:22
Tags: r, view
Slug: r-plots
Authors: Marcus Bittencourt
Summary: R plots using plotly library

(underconstruction)
This article is plotly library showcase based on my skills like data scientist

    :::r
    read.csv('./iris.csv', header = TRUE, sep = ',')

Plot radar graph

    :::r
    library(plotly)

    p <- plot_ly(
        type = 'scatterpolar',
        r = c(39, 28, 8, 7, 28, 39),
        theta = c('A','B','C', 'D', 'E', 'A'),
        fill = 'toself'
    ) %>%
    layout(
        polar = list(
        radialaxis = list(
            visible = T,
            range = c(0,50)
        )
        ),
        showlegend = F
    )

1. [https://plot.ly/r/radar-chart/]