            // Only create a new Hls instance if one does not already exist
            if (!hlsRef.current) {
                const hls = new Hls();
                hlsRef.current = hls;  // Store the Hls instance in the ref
                hls.loadSource(streamUrl);
                hls.attachMedia(videoRef.current);
                hls.on(Hls.Events.MANIFEST_PARSED, () => {
                    videoRef.current.play();
                });
            } else {
                // If an Hls instance exists, just change the source
                hlsRef.current.loadSource(streamUrl);
                hlsRef.current.attachMedia(videoRef.current);
            }