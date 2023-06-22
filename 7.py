pos_prob = prediction_prob[:, 1]
thresholds = np.arange(0.0, 1.1, 0.05)
true_pos, false_pos = [0]*len(thresholds), [0]*len(thresholds)
for pred, y in zip(pos_prob, Y_test):
... for i, threshold in enumerate(thresholds):
... if pred >= threshold:
... # if truth and prediction are both 1
... if y == 1:
... true_pos[i] += 1
... # if truth is 0 while prediction is 1
... else:
... false_pos[i] += 1
... else:
... break