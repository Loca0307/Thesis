						<div>
							<TableContainer component={Paper}>
								<Table aria-label="simple table" size="small">
									<TableHead>
										<TableRow>
											{columns.map((column) => (<TableCell>{column.title}</TableCell>))}
										</TableRow>
									</TableHead>
									<TableBody>

										{outputDictValue.filter(
											(key) => {
												return key.value !== "";
											}).map((row) => (<TableRow key={row.pattern}>
												<CustomTableCell color={row.color} align="right">{row.pattern}</CustomTableCell>
												<CustomTableCell color={row.color} align="right">{row.value}</CustomTableCell>
											</TableRow>))}
									</TableBody>
								</Table>
							</TableContainer>
						</div>