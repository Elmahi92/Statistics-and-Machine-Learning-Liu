
def WeakClassifier(T, P, X):
    """ WEAKCLASSIFIER
    Classify images using a decision stump.
    Takes a vector X of scalars obtained by applying one Haar feature to all
    training images. Classifies the examples using a decision stump with
    cut-off T and polarity P. Returns a vector C of classifications for all
    examples in X.

    You are not allowed to use a loop in this function.
    This is for your own benefit, since a loop will be too slow to use
    with a reasonable amount of Haar features and training images.
    """

    #C = (P*X < P*T).astype(int)
    #C = (X < T).astype(int)
    #C[C == 0] = -1
    
    #C = [1]*len(X)
    
    C = (P*X >= P*T).astype(int)
    C[C == 0] = -1
    
    return C


def WeakClassifierError(C, D, Y):
    """ WEAKCLASSIFIERERROR
    Calculate the error of a single decision stump.
    Takes a vector C of classifications from a weak classifier, a vector D
    with weights for each example, and a vector Y with desired
    classifications. Calculates the weighted error of C, using the 0-1 cost
    function.

    You are not allowed to use a loop in this function.
    This is for your own benefit, since a loop will be too slow to use
    with a reasonable amount of Haar features and training images.
    """

    #E = sum(D[Y != C])
    E = sum(D[Y != C])

    return E