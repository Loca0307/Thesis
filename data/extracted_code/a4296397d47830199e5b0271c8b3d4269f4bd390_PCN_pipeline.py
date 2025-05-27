
def make_themisto_indices(themisto_ref_dir, themisto_index_dir):
    """Create Themisto indices for all genomes in the themisto reference directory."""
    asyncio.run(make_themisto_indices_in_parallel(themisto_ref_dir, themisto_index_dir))
    return
    
