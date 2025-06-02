
    public function insertInBatch(int $discountId, array $codes): void
    {
        $values = implode(
            separator: ',',
            array: array_map(
                callback: static fn (string $code) => sprintf(
                    "(nextval('discount_code_id_seq'), '%s', '%s', false)",
                    $discountId,
                    $code
                ),
                array: $codes
            )
        );

        $this->getEntityManager()->getConnection()->executeQuery(
            "INSERT INTO discount_code (id, discount_id, code, used) VALUES {$values} ON CONFLICT DO NOTHING"
        );
    }

    public function countByDiscount(Discount $discount): int
    {
        return $this->createQueryBuilder('dc')
            ->select('COUNT(dc.id)')
            ->andWhere('dc.discount = :discount')
            ->setParameter('discount', $discount)
            ->getQuery()
            ->getSingleScalarResult()
        ;
    }