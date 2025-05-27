              {loading ? 'Loading...' : 'Search'}
            </button>
          </div>

          {error && <p className="text-red-500">{error}</p>}

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 mt-6">
            {characters.map((char, idx) => (
              <div
                key={idx}
                className="bg-white dark:bg-gray-800 shadow-md rounded-lg overflow-hidden transition hover:shadow-xl"
              >
                <img
                  src={char.imageUrl}
                  alt={char.name}
                  className="w-full h-48 object-cover"
                />
                <div className="p-4">
                  <h2 className="text-xl font-bold mb-2">{char.name}</h2>
                  <h3 className="text-md font-semibold mb-1">Movies:</h3>
                  <ul className="list-disc list-inside">
                    {char.films.length > 0 ? (
                      char.films.map((film, i) => <li key={i}>{film}</li>)
                    ) : (
                      <li>No movies found</li>
                    )}
                  </ul>
                </div>