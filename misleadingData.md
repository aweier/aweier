Misleading Data - DatasuRus Dozen
================

![Anscombe’s Quartet Image From
Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Anscombe%27s_quartet_3.svg/1280px-Anscombe%27s_quartet_3.svg.png)
By Anscombe.svg: Schutz(label using subscripts): Avenue - Anscombe.svg,
CC BY-SA 3.0, <https://commons.wikimedia.org/w/index.php?curid=9838454>

## What is Anscombe’s quartet?

Anscombe’s quartet is a classic example in statistics that shows
different datasets with nearly identical statistical properties (like
mean, variance, and regression line) but different distributions and
patterns.

See Anscombe’s Quartet dataset anscombe. It is important to understand
for EDA, especially applicable for ML.

\##Getting Data and Comparing Means and Variances of ‘x_shape’ and
‘dino’ Data Let’s compare the means and variances of the `x_shape` and
`dino` datasets to understand their similarities and differences in
terms of basic statistical properties.

    ##   Dataset   Mean_X   Mean_Y Variance_X Variance_Y
    ## 1 x_shape 54.26015 47.83972   281.2315    725.225
    ## 2    dino 54.26327 47.83225   281.0700    725.516

\##Plot of x_Shape with summary statistics of regression model

    ## 
    ## Call:
    ## lm(formula = y ~ x, data = x_dino)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -45.381 -24.631  -8.142  26.292  50.807 
    ## 
    ## Coefficients:
    ##             Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)  53.5542     7.6889   6.965 1.17e-10 ***
    ## x            -0.1053     0.1354  -0.778    0.438    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 26.97 on 140 degrees of freedom
    ## Multiple R-squared:  0.004301,   Adjusted R-squared:  -0.002811 
    ## F-statistic: 0.6048 on 1 and 140 DF,  p-value: 0.4381

![](misleadingData_files/figure-gfm/unnamed-chunk-2-1.png)<!-- -->

\##Plot Dino_data with summary statistics of regression model

    ## 
    ## Call:
    ## lm(formula = y ~ x, data = dino_data)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -43.439 -23.213  -1.296  21.368  52.050 
    ## 
    ## Coefficients:
    ##             Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)  53.4530     7.6934   6.948 1.29e-10 ***
    ## x            -0.1036     0.1355  -0.764    0.446    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 26.98 on 140 degrees of freedom
    ## Multiple R-squared:  0.004157,   Adjusted R-squared:  -0.002957 
    ## F-statistic: 0.5844 on 1 and 140 DF,  p-value: 0.4459

![](misleadingData_files/figure-gfm/unnamed-chunk-3-1.png)<!-- -->

Summary of Comparison

1.  **Visual Differences**: The `x_shape` dataset and the `dino` dataset
    have distinct shapes when plotted. The `x_shape` dataset forms a
    specific pattern resembling the letter “X”, while the `dino` dataset
    forms the shape of a dinosaur. These visual differences highlight
    the importance of visually inspecting data before applying
    statistical models.

2.  **Different Regression Lines**: Despite potentially having similar
    statistical summaries (e.g., means, variances), the regression lines
    for `x_shape` and `dino` differ significantly. The `x_shape`
    regression line reflects the intersecting pattern of the data, while
    the `dino` regression line reflects the general trend of the data
    points shaped like a dinosaur. The pink regression line from the
    `x_shape` dataset plotted alongside the blue regression line from
    the `dino` dataset emphasizes these differences.

3.  **Importance of Context**: This comparison underscores that
    statistical models, such as linear regression, are
    context-sensitive. The linear regression lines show different trends
    depending on the underlying data patterns, which affects how the
    model would be interpreted and used in analysis.

4.  **Illustrating a Broader Point**: By comparing these two plots, you
    demonstrate a broader point about data analysis: datasets with
    similar statistical properties can have very different underlying
    structures and relationships. This is why it’s crucial to both
    visualize and statistically analyze data before drawing conclusions.

Overall, the comparison helps to visually communicate that understanding
the data’s distribution and shape is as important as knowing its summary
statistics, especially when applying linear regression models,
conducting EDA, or applying Machine Learning applications.
