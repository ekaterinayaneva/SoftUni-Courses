value = float(input())
input_metric = input()
output_metric = input()


if input_metric == 'mm':
   value = value / 1000
elif input_metric == 'cm':
    value = value / 100

if output_metric == 'mm':
    value = value * 1000
elif output_metric == 'cm':
    value = value * 100

print(f'{value:.3f}')

