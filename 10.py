from sklearn.datasets import load_breast_cancer
cancer_data = load_breast_cancer()
X = cancer_data.data
Y = cancer_data.target
print('Input data size :', X.shape)
Input data size : (569, 30)
print('Output data size :', Y.shape)
Output data size : (569,)
print('Label names:', cancer_data.target_names)
Label names: ['malignant' 'benign']
n_pos = (Y == 1).sum()
n_neg = (Y == 0).sum()
print(f'{