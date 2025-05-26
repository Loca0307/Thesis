

def test_scaler():
    # Test a ultraplot scaler and a matplotlib native scaler; should not race errors
    fig, ax = uplt.subplots(ncols=2, share=0)
    ax[0].set_yscale("mercator")
    ax[1].set_yscale("asinh")
    return fig