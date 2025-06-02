
            //TODO: add a silly little coment
            int w = this.image.getWidth();
            int h = this.image.getHeight();
            double proportion = ((double) w) / (double) h;
            this.image = toBufferedImage(image.getScaledInstance((int) (HEIGHT * proportion), HEIGHT, java.awt.Image.SCALE_SMOOTH));
