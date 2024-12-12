import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from collections import Counter

# function to clean the data and split it into open and closed access dataframes
def clean_data():

    df.drop(columns=["language"])
    
    df['open_access'] = df['open_access'].apply(
        
        lambda x: x.split(', ') if isinstance(x, str) else np.nan
        
    )
    
    open_access = df.loc[df["open_access"].notna()]
    closed_access = df.loc[df["open_access"].isna()]
    
    return open_access, closed_access

# creating lists of sample means
def sample_mean(sample_size, num_sample_means, citations):
    
    means = []
    
    for i in range(num_sample_means):
        
        sample_citations = citations.sample(n=sample_size)
        sample_mean = sample_citations.mean()
        means.append(sample_mean)
        
    return means

def visualize_oa_levels():
    
    open_access_levels = df['open_access'].dropna().explode()
    level_counts = Counter(open_access_levels)

    labels = list(level_counts.keys())
    counts = list(level_counts.values())

    plt.figure(figsize=(12, 6))
    plt.bar(labels, counts, color='skyblue', edgecolor='black', alpha=0.7)

    plt.title('Number of Papers Published by Open Access Level', fontsize=16)
    plt.xlabel('Open Access Level', fontsize=14)
    plt.ylabel('Number of Papers', fontsize=14)
    plt.xticks(rotation=45, fontsize=10, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig("figures/oa_levels.png")

df = pd.read_csv("data/wos.csv")

open_access, closed_access = clean_data()

open_access_citations = open_access['citations_all']
closed_access_citations = closed_access['citations_all']

#visualize_oa_levels()

# sample size = 100, 500 samples taken for both open and closed
open_sample_means = sample_mean(100, 500, open_access_citations)
closed_sample_means = sample_mean(100, 500, closed_access_citations)

t_stat, p_val = stats.ttest_ind(open_sample_means, closed_sample_means, equal_var=True)

print("t-statistic = " + str(t_stat))  
print("p-value = " + str(p_val))
#print(open_sample_means)
#print(closed_sample_means)