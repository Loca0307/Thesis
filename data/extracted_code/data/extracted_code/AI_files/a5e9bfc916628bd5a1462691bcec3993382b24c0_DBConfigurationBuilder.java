        if (dataDir == null || tmpDir == null) {
            String p = SystemUtils.JAVA_IO_TMPDIR + path();

            this.baseDir = p + "/base";
            this.dataDir = p + DEFAULT_DATA_DIR;
            this.tmpDir = p + DEFAULT_TMP_DIR;
        }
