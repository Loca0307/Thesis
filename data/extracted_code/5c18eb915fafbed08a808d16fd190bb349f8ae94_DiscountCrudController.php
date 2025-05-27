        for ($i = 0; $i < $instance->getNumberOfCodes(); ++$i) {
            do {
                $code = self::generateSingleCode($instance->getCodePrefix());
            } while ($em->getRepository(DiscountCode::class)->findOneBy(['code' => $code]));

            $codeObj = (new DiscountCode())
                ->setCode($code)
                ->setDiscount($instance)
            ;

            $em->persist($codeObj);
            $em->flush();
        }

        return $this->redirect($this->adminUrlGenerator->setAction(Action::INDEX)->generateUrl());
    }

    private static function generateSingleCode(string $prefix): string
    {
        $chars = array_flip(
            array_merge(range(0, 9), range('A', 'Z'))
        );

        $randomString = '';

        while (strlen($randomString) < 10) {
            $randomString .= array_rand($chars);
        }

        return (str_ends_with($prefix, '_') ? $prefix : ($prefix.'_')).$randomString;