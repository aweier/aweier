nycAirQualitySimpleLinearRegression
================
ACW

### Use R to answer Simple Linear Regression Questions about NYC air quality dataset

First step we will load the data and make a scatter plot

    ## `geom_smooth()` using formula = 'y ~ x'

![](nycIAQSimpleLinearRegression_files/figure-gfm/unnamed-chunk-1-1.png)<!-- -->

``` r
model <- lm(Temp ~ Wind, data = airq)
#Forumula gives you the intercept and the slope
#= 90.13-1.23*x
```

Use this equation to predict the temperature, on a day when the observed
wind speed is 8mph

``` r
obs_wind_spped_8 <- 90.13 - 1.23*8
print(obs_wind_spped_8)
```

    ## [1] 80.29

\##Determine the Residual at a Given Observation We want to determine
the residual at wind of 8mph and temp of 72°Fahrenheit

``` r
summary(model)
```

    ## 
    ## Call:
    ## lm(formula = Temp ~ Wind, data = airq)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -23.291  -5.723   1.709   6.016  19.199 
    ## 
    ## Coefficients:
    ##             Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)  90.1349     2.0522  43.921  < 2e-16 ***
    ## Wind         -1.2305     0.1944  -6.331 2.64e-09 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 8.442 on 151 degrees of freedom
    ## Multiple R-squared:  0.2098, Adjusted R-squared:  0.2045 
    ## F-statistic: 40.08 on 1 and 151 DF,  p-value: 2.642e-09

### Result

The model provides an extremely small p-value for the slope of Wind,
which is much smaller than the typical significance level (e.g., 0.05).
This indicates that we can reject the null hypothesis that there is no
relationship between Wind and Temp. Therefore, our data suggests that
there is a statistically significant relationship between Wind and Temp.

![](nycIAQSimpleLinearRegression_files/figure-gfm/unnamed-chunk-5-1.png)<!-- -->

### Residuals Explained

Residuals are the difference between the observed value and the
predicted value, visualized using various diagnostic plots. These
include the Residuals vs. Fitted plot, the Q-Q plot for normality
assessment, the Scale-Location plot to check homoscedasticity, and the
Residuals vs. Leverage plot to identify influential data points.
