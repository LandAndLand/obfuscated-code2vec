import os
import pandas as pd
import sys

results_loc = sys.argv[1]
if len(sys.argv) > 2:
    output_file = sys.argv[2]
else:
    output_file = results_loc.split('.csv')[0] + '_processed.csv'

weka_df = pd.read_csv(results_loc)
new_df = pd.DataFrame(columns=['model', 'selection_method', 'agg_method', 'reduction_method', 'accuracy', 'stddev'])

for i, row in weka_df.iterrows():
    split = row['dataset'].split('_')
    model = split[0]
    selection_method = split[1]
    agg_method = split[2]
    reduction_method = split[3]

    new_df = new_df.append({
        'model': model,
        'selection_method': selection_method,
        'agg_method': agg_method,
        'reduction_method': reduction_method,
        'accuracy': row['accuracy'],
        'stddev': row['stddev']
    }, ignore_index=True)

with open(output_file, newline='', mode='w') as out_file:
    new_df.to_csv(out_file, index=False)
