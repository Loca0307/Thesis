        .intercept(Advice.withCustomMapping()
            .bind(Transactional.class, new AnnotationDescription.Loadable<Transactional>() {
                @Override
                public Class<? extends Annotation> getAnnotationType() {
                    return Transactional.class;
                }

                @Override
                public Transactional load() {
                    return annotationDescription.prepare(Transactional.class).load();
                }
            }).to(RequiresNewAdvice.class))