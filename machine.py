import numpy as np
import pandas as pd

# Sample GDP and Life Satisfaction Data
gdp = np.array([10000, 20000, 30000, 40000, 50000])
life_satisfaction = np.array([4.5, 5.0, 5.5, 6.0, 6.5])

# Convert to DataFrame
df = pd.DataFrame({'GDP': gdp, 'LifeSatisfaction': life_satisfaction})

# Calculate correlation
# correlation = df.corr().iloc[0,1]
# print(f"Correlation: {correlation:.3f}")
print(df)
