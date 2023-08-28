from hypothesis import strategies as st

import ivy_tests.test_ivy.helpers as helpers
from ivy_tests.test_ivy.helpers import handle_frontend_test


@handle_frontend_test(
    fn_tree="sklearn.metrics.accuracy_score",
    arrays_and_dtypes=helpers.dtype_and_values(
        num_arrays=2,
        min_value=-2,
        max_value=2,
        shared_dtype=True,
        shape=helpers.lists(
            x=helpers.ints(min_value=2, max_value=5),
            min_size=2,
            max_size=3,
        )),
    normalize=st.booleans(),
)
def test_sklearn_accuracy_score(
    arrays_and_dtypes,
    on_device,
    fn_tree,
    frontend,
    test_flags,
    backend_fw,
    normalize,
):
    dtypes, values = arrays_and_dtypes
    helpers.test_frontend_function(
        input_dtypes=dtypes,
        backend_to_test=backend_fw,
        test_flags=test_flags,
        fn_tree=fn_tree,
        frontend=frontend,
        on_device=on_device,
        y_true=values[0],
        y_pred=values[1],
        normalize=normalize,
        sample_weight=None,
    )
