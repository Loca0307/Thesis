  // Add preview
  addPreview: (files: File[]) => {
    const newPreviews = files.map((file) => ({
      id: crypto.randomUUID(),
      file,
      previewUrl: URL.createObjectURL(file),
      isUploaded: false,
    }));

    set((state) => ({
      previewMedia: [...state.previewMedia, ...newPreviews],
    }));
  },

  // Delete preview
  removePreview: (previewId: string) => {
    set((state) => {
      // delete preview url
      const previewToRemove = state.previewMedia.find(
        (p) => p.id === previewId
      );
      if (previewToRemove) {
        URL.revokeObjectURL(previewToRemove.previewUrl);
      }

      return {
        previewMedia: state.previewMedia.filter((p) => p.id !== previewId),
      };
    });
  },

  // Delete all previews
  clearPreviews: () => {
    const { previewMedia } = get();

    // delete all preview urls
    previewMedia.forEach((preview) => {
      URL.revokeObjectURL(preview.previewUrl);
    });

    set({ previewMedia: [] });
  },

  // Upload all previews to server
  uploadAllPreviews: async (options: MediaUploadOptions) => {
    const { previewMedia } = get();
    set({ isUploading: true, uploadProgress: 0 });

    const uploadedItems: Media[] = [];
    const totalFiles = previewMedia.length;
    let processedCount = 0;

    try {
      for (const preview of previewMedia) {
        if (!preview.isUploaded) {
          const media = await get().uploadMedia(preview.file, options);
          if (media) {
            uploadedItems.push(media);

            // change states to uploaded
            set((state) => ({
              previewMedia: state.previewMedia.map((p) =>
                p.id === preview.id ? { ...p, isUploaded: true } : p
              ),
            }));
          }
        }

        processedCount++;
        const percentCompleted = Math.round(
          (processedCount * 100) / totalFiles
        );
        set({ uploadProgress: percentCompleted });
      }

      // Clear preview after uploaded
      get().clearPreviews();

      set({ isUploading: false, uploadProgress: 100 });
      return uploadedItems;
    } catch (error) {
      console.error("Failed to upload previews:", error);
      set({
        isUploading: false,
        error: error instanceof Error ? error.message : "Upload failed",
      });
      return [];
    }
  },
