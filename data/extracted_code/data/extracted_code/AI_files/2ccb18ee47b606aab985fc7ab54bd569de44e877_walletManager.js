            // Get current ETH price with safety check
            const ethPrice = window.walletBalances.ethusd || 0;
            if (ethPrice <= 0 && document.querySelector('[data-recommended-action="SELL"]')) {
                showNotification('Cannot test SELL notification: ETH price data not available', 'warning');
                return;
            }
            