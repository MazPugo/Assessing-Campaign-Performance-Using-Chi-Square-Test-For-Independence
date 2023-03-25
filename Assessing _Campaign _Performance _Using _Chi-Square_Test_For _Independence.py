#Import required packages

import pandas as pd

from scipy.stats import chi2_contingency,chi2


#import data
campaign_data = pd.read_excel("grocery_database.xlsx", sheet_name= "campaign_data")

#filter our data

campaign_data = campaign_data.loc[campaign_data["mailer_type"] != "Control"]

# summarize to get our observed frequencies

observed_values = pd.crosstab(campaign_data["mailer_type"],campaign_data["signup_flag"]).values

mailer1_signup_rate = 123 / (252 + 123)
mailer2_signup_rate = 127 / (209 + 127)
print(mailer1_signup_rate, mailer2_signup_rate)

#state hypotheses & set acceptance criteria

null_hypothesis = "There is no relationship between mailer type and signup_rate. There are independent"
alternate_hypothesis = "There is a relationship between mailer type and signup_rate. There are not independent"
acceptance_citeria = 0.05

# calculte expected frequencies and chi square static
chi2_statistic, p_value, dof, expected_values = chi2_contingency(observed_values, correction = False)
print(chi2_statistic, p_value)

#Find the critical value for our test
critical_value = chi2.ppf(1 - acceptance_citeria, dof)
print(critical_value)


# ppf purcentage point function



if chi2_statistic >= critical_value:
    print(f"As our chi-square statistic of (chi_statistic) is higher than our critical value of {critical_value} - we reject the null hypothesis, and conclude that:{alternate_hypothesis}")
else:
    print(f"As our chi-square statistic of (chi_statistic) is lower than our critical value of {critical_value} - we retain the null hypothesis, and conclude that:{null_hypothesis}")



# print the results p-value


if p_value <= acceptance_citeria:
    print(f"As p.value of (p.value) is lower than our acceptance_citeria of {acceptance_citeria} - we reject the null hypothesis, and conclude that:{alternate_hypothesis}")
else:
    print(f"As p.value statistic of (p.value) is higher than our acceptance_citeria of {acceptance_citeria} - we retain the null hypothesis, and conclude that:{null_hypothesis}")












