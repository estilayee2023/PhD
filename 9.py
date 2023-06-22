for train_indices, test_indices in k_fold.split(X, Y):
X_train, X_test = X[train_indices], X[test_indices]
Y_train, Y_test = Y[train_indices], Y[test_indices]
for alpha in smoothing_factor_option:
if alpha not in auc_record:
auc_record[alpha] = {}
for fit_prior in fit_prior_option:
clf = MultinomialNB(alpha=alpha,
fit_prior=fit_prior)
clf.fit(X_train, Y_train)
     prediction_prob = clf.predict_proba(X_test)
     pos_prob = prediction_prob[:, 1]
     auc = roc_auc_score(Y_test, pos_prob)
     auc_record[alpha][fit_prior] = auc +
         auc_record[alpha].get(fit_prior, 0.0)