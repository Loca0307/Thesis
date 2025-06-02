		plugins: [
			new WebpackBar(
				{
					name: 'Plugin Entry Points',
					color: '#B6CD58',
				}
			),
			new ESLintPlugin({
				failOnError: true,
				extensions: ['js', 'jsx'],
			}),
		],
		performance: {
			hints: 'warning',
		},
		optimization: {
			minimize: true,
		},
		target: ['web', 'es5'],