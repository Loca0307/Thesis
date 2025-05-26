async def make_themisto_index_for_genome(genome_id, themisto_ref_dir, themisto_index_dir):
    """build a Themisto index for a single genome"""
    ref_fasta_dir = os.path.join(themisto_ref_dir, genome_id)
    if not os.path.isdir(ref_fasta_dir):
        return
    
    index_input_filelist = os.path.join(ref_fasta_dir, genome_id + ".txt")
    genome_index_dir = os.path.join(themisto_index_dir, genome_id)
    os.makedirs(genome_index_dir, exist_ok=True)
    
    index_prefix = os.path.join(genome_index_dir, genome_id)
    tempdir = os.path.join(genome_index_dir, "temp")
    os.makedirs(tempdir, exist_ok=True)
    
    themisto_build_args = [
        "themisto", "build", "-k", "31", "-i", index_input_filelist,
        "--index-prefix", index_prefix, "--temp-dir", tempdir,
        "--mem-gigas", "8", "--n-threads", "8", "--file-colors"
    ]
    themisto_build_string = " ".join(themisto_build_args)
    print(themisto_build_string)
    
    await run_command_with_retry(themisto_build_string, tempdir)


async def make_themisto_indices(themisto_ref_dir, themisto_index_dir):
    """Create Themisto indices for all genomes in the themisto reference directory."""
    os.makedirs(themisto_index_dir, exist_ok=True)
    
    tasks = [
        make_themisto_index_for_genome(genome_id, themisto_ref_dir, themisto_index_dir)
        for genome_id in os.listdir(themisto_ref_dir)
        if os.path.isdir(os.path.join(themisto_ref_dir, genome_id))
    ]
    
    await asyncio.gather(*tasks)
