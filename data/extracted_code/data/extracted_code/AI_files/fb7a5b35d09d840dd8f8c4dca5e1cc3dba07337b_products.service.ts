            // Calculate the difference in totalStock
            const stockDifference = sizeDto.totalStock - existingSize.totalStock;

            // If the `totalStock`increases, update stockRemaining accordingly
            const updatedSize = this.productSizeRepository.merge(existingSize, {
              ...sizeDto,
              stockRemaining: stockDifference > 0 ? existingSize.stockRemaining + stockDifference : existingSize.stockRemaining, // Don't decrease stockRemaining if totalStock decreases
            });

            return updatedSize;