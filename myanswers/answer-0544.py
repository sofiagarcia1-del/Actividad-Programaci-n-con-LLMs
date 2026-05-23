def varianza_explicada_pca(X):
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    pca.fit(X)
    return float(pca.explained_variance_ratio_.sum())
