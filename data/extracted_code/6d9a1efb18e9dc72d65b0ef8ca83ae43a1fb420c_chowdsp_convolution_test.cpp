    if (mono_ir)
    {
        chowdsp::convolution::create_ir (&conv_config,
                                         &conv_ir,
                                         ir.data(),
                                         ir_length_samples,
                                         fft_scratch);
    }
    else
    {
        chowdsp::convolution::create_multichannel_ir (&conv_config,
                                                      &conv_ir,
                                                      multi_channel_ir.data(),
                                                      ir_length_samples,
                                                      num_channels,
                                                      fft_scratch);
    }