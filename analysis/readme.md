## ***Exploratory Data Analysis***
This analysis included the following information from the dataset:
* Age - Age of patient
* Sex - Sex of patient
* Children - Number of children patient has
* Smoker - If patient is a smoker
* Charges - Amount patient is charged

All of the previous values were used to determine the average hospital charge relative to each data type. The results were similar to what one would expect. 
* As age increases, cost goes up linearly
* Males are charges slightly more than females
* More children generally means higher charges
* Smoking drastically increases hospital charges

## ***Research Analysis***

## ***Introduction***
In this dataset I will be exploring all of the factors that affect the average amount a patient is charged in a hospital visit. All of my research questions have to do with what variable affects the average hospital charge for patients, such as wether older patients were charged more and if children had any effect on the price. I found that bar plots would be the best type of chart to use for these questions, given how the graphs make comparing the differences of groups very clear. These questions are important because healthcare is a very important topic in this political climate, and knowing who is most affected by it will be extremely valuable information to determine needed changes regarding hospital charges

## ***Research Questions***
My research questions when starting this project were as follows:
* What is the correlation of age to hospital charges?
* Which gender is charged more?
* What effect does the amount of children have on hospital charges?
* How much does smoking increase the average hospital charge?

I found that for all of my research questions a bar plot would be the most efficient and clear visualization of my data. Since all of my questions focused on the average charge depending on different columns, all of the graphs are straightforward and easy to understand.
## ***Research Question 1***
My hypothesis for Question 1 was: "Due to older patients needing to go to the hospital more often than younger ones, they would be charged more on average". The graph shows that this is true in most cases, with the result being a nigh linear upward graph as age increases. The only result that contradicts this is 48 - 53 year olds being charged around 100$ less than 42-47 year olds. With the ages being so close to one another, as well as the average cost being almost the same, I beleive this statistical anomaly would be solved if there was more patient data in this specific age range.

![Age Graph](https://github.com/data301-2020-winter1/course-project-solo_300/blob/main/images/age.png)

## ***Research Question 2***
My hypothesis for Question 2 was: "The difference in average charges for men and women will be negligible". My thoughts were that men and women can have exclusive health problems to their gender, but they would eventually balance eachother out and average charges would be very similar. The graph shows that men on average are charged around 1500$ more on average than women. When looking at my dataset, I found that this is due to men being smoking ciggarettes more often than women do. I beleive that while my hypothesis itself was mostly accurate, I neglected to consider which gender smoked more, which led to the resulting graph being slightly skewed towards men.

![Gender Graph](https://github.com/data301-2020-winter1/course-project-solo_300/blob/main/images/gender.png)

## ***Research Question 3***
My hypothesis for Question 3 was: "Patients will be charged more on average if they have more children". This hypothesis was incorrect, given how the graph shows a bell curve with the dataset. Parents with 3 kids are charged the most on average, while parents with 5 children are charged the least. There are a lot of possible factors for this result and it cannot be narrowed down to just one. Some factors could include estimations such as parents with 5 children may not have enough finances to pay hospital bills for all of their kids, or another theory could be parents who have 2 - 3 children are likely the wealthiest of all patients in the dataset. One final factor that could skew the results mentioned is that there were only 18 patients with 5 children, so more data could balance the chart towards a more logarithmic graph.

![Count of Children Graph](https://github.com/data301-2020-winter1/course-project-solo_300/blob/main/images/children.png)

## ***Research Question 4***
My hypothesis for Question 4 was: "Smokers will be charges significantly more than non-smokers". This hypothesis was indeed correct, as smokers were charged around 4.25x the amount non-smokers were charged. It is fairly obvious why this is, given the countless amounts of evidence pointing towards smoking causing health problems such as cancer and heart disease. What I was mainly looking for in this part of the dataset was how much more they will be charged, since there was no question wether or not the smoking patients would be charged more than non-smokers.

![Smoker Graph](https://github.com/data301-2020-winter1/course-project-solo_300/blob/main/images/smoker.png)

## ***Conclusion***
In conclusion, the charts used for this dataset proved to be valuable. All of my research questions were able to be answered by the graphs, and given how important hospital charges are the information this data gives would be useful in the real world.

## ***References***
All data was gathered by Miri Choi and can be found here: https://www.kaggle.com/mirichoi0218/insurance
