LINK NUMBER 1
Error fetching diff

LINK NUMBER 2
Error fetching diff

LINK NUMBER 3

File path: openweatheraqi.py
"#!/usr/bin/python3

import urllib.request
import json
from datetime import datetime, timezone

# Constants
AQI_URL = 'http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={key}'
KEY_FILE = '/private/keys/openweather.txt'
OUT_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

# AQI Categories
AQI_GOOD = 1
AQI_FAIR = 2
AQI_MODERATE = 3
AQI_POOR = 4
AQI_VERY_POOR = 5

AQI_CATEGORY_MAP = {
    AQI_GOOD: ""Good"",
    AQI_FAIR: ""Fair"",
    AQI_MODERATE: ""Moderate"",
    AQI_POOR: ""Poor"",
    AQI_VERY_POOR: ""Very Poor""
}

class RemoteAQI:
    """"""
    A class to fetch and process AQI data from the OpenWeatherMap API.
    """"""

    def __init__(self, lat, lon, key):
        """"""
        Initialize the RemoteAQI class with latitude, longitude, and API key.
        """"""
        self.lat = lat
        self.lon = lon
        self.key = key
        self.forecast_url = AQI_URL.format(lat=self.lat, lon=self.lon, key=self.key)

    def get_raw_forecast_data(self):
        """"""
        Fetch raw AQI forecast data from the API.
        """"""
        response = urllib.request.urlopen(self.forecast_url)
        return json.loads(response.read().decode('utf8'))

    def get_forecast(self):
        """"""
        Get a detailed AQI forecast including local timestamps, AQI values, and categories.
        """"""
        raw_data = self.get_raw_forecast_data()
        forecast = []

        for entry in raw_data['list']:
            timestamp = entry['dt']
            # Convert UTC timestamp to local time
            date_time = convert_timestamp_to_local(timestamp)

            aqi = entry['main']['aqi']
            category = AQI_CATEGORY_MAP.get(aqi, ""Unknown"")
            components = entry['components']

            forecast.append({
                ""timestamp"": date_time,
                ""aqi"": aqi,
                ""category"": category,
                ""components"": components
            })

        return forecast

    def get_hourly_aqi_forecast(self):
        """"""
        Get the hourly AQI forecast for the next 24 hours.
        """"""
        forecast = self.get_forecast()
        hourly_aqi = []

        for entry in forecast[:24]:
            timestamp = entry[""timestamp""]
            aqi = entry[""aqi""]
            category = entry[""category""]
            components = entry[""components""]

            hourly_aqi.append({
                ""timestamp"": timestamp,
                ""aqi"": aqi,
                ""category"": category
            })
        return hourly_aqi
    
    def get_detailed_current_aqi(self):
        """"""
        Get the current AQI and its components.
        """"""
        forecast = self.get_forecast()
        current_aqi = forecast[0]
        timestamp = current_aqi[""timestamp""]
        aqi = current_aqi[""aqi""]
        category = current_aqi[""category""]
        components = current_aqi[""components""]
        # Convert components to a human-readable format
        components = {k: f""{v} μg/m³"" for k, v in components.items()}
        
        return {
            ""timestamp"": timestamp,
            ""aqi"": aqi,
            ""category"": category,
            ""components"": components
        }
    
    def get_daily_aqi_forecast(self):
        """"""
        Get the daily AQI forecast by calculating the maximum AQI for each day.
        """"""
        forecast = self.get_forecast()
        daily_aqi = {}

        for entry in forecast:
            date = entry[""timestamp""].split("" "")[0]  # Extract the date (YYYY-MM-DD)
            aqi = entry[""aqi""]
            category = entry[""category""]

            if date not in daily_aqi or aqi > daily_aqi[date][""aqi""]:
                daily_aqi[date] = {
                    ""date"": date,
                    ""aqi"": aqi,
                    ""category"": category
                }

        # Convert the dictionary to a sorted list of daily AQI forecasts
        return [daily_aqi[date] for date in sorted(daily_aqi.keys())]

def convert_timestamp_to_local(timestamp): 
    """"""
    Convert a UTC timestamp to local time.
    """"""
    utc_time = datetime.fromtimestamp(timestamp, timezone.utc)
    local_time = utc_time.astimezone()  # Converts to local time zone
    return local_time.strftime(OUT_TIME_FORMAT)

def main():
    """"""
    Main function to fetch and display AQI data.
    """"""
    with open(KEY_FILE, encoding=""utf-8"") as f:
        key = f.read().strip()

    # Example coordinates for testing
    lat, lon = 47.697, -122.3222
    ra = RemoteAQI(lat, lon, key)
    daily_aqi_forecast = ra.get_daily_aqi_forecast()

    # Print the current AQI
    current_aqi = ra.get_detailed_current_aqi()
    print(f""[Current AQI] {current_aqi['timestamp']}"")
    print(f""  AQI: {current_aqi['aqi']} ({current_aqi['category']})"")
    print(f""  Components: {current_aqi['components']}"")
    print()
    # Print the hourly AQI forecast
    hourly_aqi_forecast = ra.get_hourly_aqi_forecast()
    print(""[Hourly AQI Forecast]"")
    for hour in hourly_aqi_forecast:
        print(f""Timestamp: {hour['timestamp']}"")
        print(f""  AQI: {hour['aqi']} ({hour['category']})"")
        print()   
    print(""[7-Day AQI Forecast]"")
    for day in daily_aqi_forecast:
        print(f""Date: {day['date']}"")
        print(f""  AQI: {day['aqi']} ({day['category']})"")
        print()

if __name__ == '__main__':
    main()"

LINK NUMBER 4

File path: internal/model/sacct_fetchers.go
"package model

import (
	""bufio""
	""encoding/gob""
	""fmt""
	""os""
	""path""
	""runtime""
	""sync""
	""sync/atomic""
	""testing""
	""time""

	""github.com/antvirf/stui/internal/config""
	""github.com/stretchr/testify/assert""
	""github.com/stretchr/testify/require""
)

func init() {
	// Register types for gob
	gob.Register(&[]config.ColumnConfig{})
	gob.Register(TableData{})
}

// setupTestCache creates a temporary cache for testing
func setupTestCache(t *testing.T) (*SacctCache, string) {
	// Create a temporary directory for test
	tempDir, err := os.MkdirTemp("""", ""sacct_cache_test"")
	require.NoError(t, err)

	// Create cache file path
	filePath := path.Join(tempDir, ""sacct_cache.gob"")

	// Create a test cache
	file, err := os.OpenFile(filePath, os.O_RDWR|os.O_CREATE|os.O_APPEND, 0600)
	require.NoError(t, err)

	cache := &SacctCache{
		file:   file,
		writer: nil, // will be set after initialization
		reader: nil, // will be set after initialization
	}

	// Set up reader/writer
	cache.writer = bufio.NewWriter(file)
	cache.reader = bufio.NewReader(file)

	return cache, tempDir
}

// createTestTableData creates a TableData for testing
func createTestTableData(t *testing.T, rows int) *TableData {
	headers := []config.ColumnConfig{
		{Name: ""JobIDRaw""},
		{Name: ""JobID""},
		{Name: ""JobName""},
		{Name: ""Partition""},
		{Name: ""State""},
	}

	tableData := &TableData{
		Headers: &headers,
		Rows:    make([][]string, rows),
	}

	for i := 0; i < rows; i++ {
		tableData.Rows[i] = []string{
			fmt.Sprintf(""job_%d"", i),      // JobIDRaw
			fmt.Sprintf(""%d"", i),          // JobID
			fmt.Sprintf(""test_job_%d"", i), // JobName
			""test_partition"",              // Partition
			""RUNNING"",                     // State
		}
	}

	return tableData
}

// cleanupTestCache removes the temporary directory and files
func cleanupTestCache(t *testing.T, tempDir string) {
	err := os.RemoveAll(tempDir)
	require.NoError(t, err)
}

// TestBasicCacheOperations tests basic writing and reading operations
func TestBasicCacheOperations(t *testing.T) {
	cache, tempDir := setupTestCache(t)
	defer cleanupTestCache(t, tempDir)

	// Create test data
	testData := createTestTableData(t, 10)
	startTime := time.Now().Add(-24 * time.Hour)
	endTime := time.Now()

	// Test writing to cache
	err := cache.WriteToCache(testData, startTime, endTime, true)
	assert.NoError(t, err)

	// Test reading from cache
	readData, err := cache.GetFromCache()
	assert.NoError(t, err)
	assert.True(t, cache.IsUsable)

	// Verify data integrity
	assert.Equal(t, len(testData.Rows), len(readData.Rows))
	assert.Equal(t, (*testData.Headers)[0].Name, (*readData.Headers)[0].Name)

	// Check content field is updated
	assert.Equal(t, startTime.Unix(), cache.Content.StartTime.Unix()) // Compare unix timestamps to avoid precision issues
	assert.Equal(t, endTime.Unix(), cache.Content.EndTime.Unix())
}

// TestCorruptedCache tests recovery from corrupted cache file
func TestCorruptedCache(t *testing.T) {
	cache, tempDir := setupTestCache(t)
	defer cleanupTestCache(t, tempDir)

	// Write invalid data to the cache file
	_, err := cache.file.Write([]byte(""This is not valid gob data""))
	require.NoError(t, err)
	require.NoError(t, cache.file.Sync())

	// Try to read, should fail but not panic
	_, err = cache.GetFromCache()
	assert.Error(t, err)
	assert.False(t, cache.IsUsable)

	// Now write valid data, should work
	testData := createTestTableData(t, 5)
	err = cache.WriteToCache(testData, time.Now(), time.Now(), true)
	assert.NoError(t, err)

	// Try to read again, should succeed
	readData, err := cache.GetFromCache()
	assert.NoError(t, err)
	assert.True(t, cache.IsUsable)
	assert.Equal(t, len(testData.Rows), len(readData.Rows))
}

// TestEmptyCache tests handling of empty cache file
func TestEmptyCache(t *testing.T) {
	cache, tempDir := setupTestCache(t)
	defer cleanupTestCache(t, tempDir)

	// Try to read from empty cache
	data, err := cache.GetFromCache()
	assert.Error(t, err)
	assert.False(t, cache.IsUsable)
	assert.Nil(t, data)

	// Write empty data
	emptyData := createTestTableData(t, 0)
	err = cache.WriteToCache(emptyData, time.Now(), time.Now(), true)
	assert.NoError(t, err)

	// Read empty data
	readData, err := cache.GetFromCache()
	assert.NoError(t, err)
	assert.Equal(t, 0, len(readData.Rows))
}

// TestCacheMerging tests the merging functionality
func TestCacheMerging(t *testing.T) {
	cache, tempDir := setupTestCache(t)
	defer cleanupTestCache(t, tempDir)

	// Create initial data
	initialData := createTestTableData(t, 10)
	startTime := time.Now().Add(-48 * time.Hour)
	midTime := time.Now().Add(-24 * time.Hour)

	// Write initial data
	err := cache.WriteToCache(initialData, startTime, midTime, true)
	assert.NoError(t, err)

	// Create new data (with some overlap to test merging)
	newData := createTestTableData(t, 15) // More rows
	for i := 0; i < 5; i++ {
		// Modify first 5 rows to test replacement
		newData.Rows[i][4] = ""COMPLETED"" // Change state
	}
	endTime := time.Now()

	// Write new data with merge
	err = cache.WriteToCache(newData, midTime, endTime, false)
	assert.NoError(t, err)

	// Read merged data
	mergedData, err := cache.GetFromCache()
	assert.NoError(t, err)

	// Verify merged data
	assert.GreaterOrEqual(t, len(mergedData.Rows), 15) // Should have at least 15 rows

	// Check if state of first 5 jobs was updated
	foundCompleted := false
	for _, row := range mergedData.Rows {
		if row[0] == ""job_0"" && row[4] == ""COMPLETED"" {
			foundCompleted = true
			break
		}
	}
	assert.True(t, foundCompleted, ""Modified data should be present in merged result"")
}

// TestConcurrentAccess tests thread safety of the cache
func TestConcurrentAccess(t *testing.T) {
	cache, tempDir := setupTestCache(t)
	defer cleanupTestCache(t, tempDir)

	// Write initial data
	initialData := createTestTableData(t, 10)
	err := cache.WriteToCache(initialData, time.Now().Add(-24*time.Hour), time.Now(), true)
	assert.NoError(t, err)

	var wg sync.WaitGroup
	concurrentReaders := 10
	concurrentWriters := 2
	successfulReads := int32(0)
	successfulWrites := int32(0)

	// Start concurrent readers
	for i := 0; i < concurrentReaders; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			data, err := cache.GetFromCache()
			if err == nil && len(data.Rows) > 0 {
				atomic.AddInt32(&successfulReads, 1)
			}
		}(i)
	}

	// Start concurrent writers
	for i := 0; i < concurrentWriters; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			data := createTestTableData(t, 5+id)
			err := cache.WriteToCache(data, time.Now().Add(-12*time.Hour), time.Now(), false)
			if err == nil {
				atomic.AddInt32(&successfulWrites, 1)
			}
		}(i)
	}

	wg.Wait()

	// Verify that operations completed without deadlock
	assert.Greater(t, int(successfulReads), 0)
	assert.Greater(t, int(successfulWrites), 0)
}

// TestCacheFilePermissions tests handling of permission errors
func TestCacheFilePermissions(t *testing.T) {
	// Skip on Windows since permission testing works differently
	if runtime.GOOS == ""windows"" {
		t.Skip(""Skipping permission test on Windows"")
	}

	tempDir, err := os.MkdirTemp("""", ""sacct_cache_test"")
	require.NoError(t, err)
	defer os.RemoveAll(tempDir)

	filePath := path.Join(tempDir, ""readonly_cache.gob"")

	// Create file with read-only permissions
	file, err := os.OpenFile(filePath, os.O_RDWR|os.O_CREATE, 0400)
	require.NoError(t, err)
	file.Close()

	// Try to open the cache (should fail on write)
	file, err = os.OpenFile(filePath, os.O_RDWR, 0400)
	if err == nil {
		// Some platforms may allow opening but fail on write
		cache := &SacctCache{
			file:   file,
			writer: bufio.NewWriter(file),
			reader: bufio.NewReader(file),
		}

		testData := createTestTableData(t, 5)
		err = cache.WriteToCache(testData, time.Now(), time.Now(), true)
		assert.Error(t, err)
	}
}

// TestCacheReinitialization tests reinitialization from disk
func TestCacheReinitialization(t *testing.T) {
	cache1, tempDir := setupTestCache(t)
	defer cleanupTestCache(t, tempDir)

	// Write data with first instance
	testData := createTestTableData(t, 10)
	startTime := time.Now().Add(-24 * time.Hour)
	endTime := time.Now()

	err := cache1.WriteToCache(testData, startTime, endTime, true)
	assert.NoError(t, err)

	// Close first instance
	cache1.file.Close()

	// Create second instance pointing to same file
	filePath := cache1.file.Name()
	file2, err := os.OpenFile(filePath, os.O_RDWR, 0600)
	require.NoError(t, err)

	cache2 := &SacctCache{
		file:   file2,
		writer: bufio.NewWriter(file2),
		reader: bufio.NewReader(file2),
	}

	// Read with second instance
	readData, err := cache2.GetFromCache()
	assert.NoError(t, err)
	assert.True(t, cache2.IsUsable)
	assert.Equal(t, len(testData.Rows), len(readData.Rows))
}"

LINK NUMBER 5
Not enough lines

LINK NUMBER 6

File path: script.js
"const carouselNext = document.querySelector('.carousel-next');
const carouselPrev = document.querySelector('.carousel-prev');

if (carouselNext) {
  carouselNext.addEventListener('click', () => {
    currentTestimonial = (currentTestimonial + 1) % testimonials.length;
    showTestimonial(currentTestimonial);
  });
}

if (carouselPrev) {
  carouselPrev.addEventListener('click', () => {
    currentTestimonial = (currentTestimonial - 1 + testimonials.length) % testimonials.length;
    showTestimonial(currentTestimonial);
  });
if (loginForm) {
  loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    if (!email.includes('@')) {
      const emailError = document.getElementById('email-error');
      if (emailError) {
        emailError.textContent = 'Valid email required';
      }
      return;
    }
    // Proceed with login
  });
}"

LINK NUMBER 7
Error fetching diff

LINK NUMBER 8
Error fetching diff

LINK NUMBER 9
Error fetching diff

LINK NUMBER 10

File path: wich.c
"#include ""main.h""
/**
 * prompt - checks mode and prints prompt if in interactive mode
 * @fd: file stream
 */
void prompt(int fd)
{
    struct stat buf;
    
    if (fstat(fd, &buf) == -1)
    {
        return;
    }

    if (S_ISCHR(buf.st_mode))
        _puts(PROMPT);
}
/**
* _puts - prints a string without a \n
* @str: string to print
* Return: void
*/
void _puts(char *str)
{
	unsigned int length;

	length = _strlen(str);

	write(STDOUT_FILENO, str, length);
}"

LINK NUMBER 11
Not enough lines

LINK NUMBER 12
Not enough lines

LINK NUMBER 13
Not enough lines

LINK NUMBER 14
Error fetching diff

LINK NUMBER 15
Error fetching diff

LINK NUMBER 16
Error fetching diff

LINK NUMBER 17
Not enough lines

LINK NUMBER 18

File path: controllers/blogPosts.js
"# Project 8 Fullstack Travelblog Backend API

This backend API is designed to support the functionality of the Project 8 travel blog posts application. It provides endpoints for managing data, handling user authentication, and enabling seamless communication between the frontend and the database. Built with Node.js, it follows RESTful principles and ensures secure and efficient data handling.

## Features
- CRUD operations for managing resources
- Integration with a database for persistent storage
- Error handling and validation
- Scalable and modular architecture
- API endpoints for the posts resource:
  - **GET /posts**:  Retrieve all posts.
  - **GET /posts/:id**:  Retrieve a single post by ID.
  - **POST /posts**:  Create a new post.
  - **PUT /posts/:id**:  Update an existing post by ID.
  - **DELETE /posts/:id**:  Delete a post by ID.

## Technologies Used
- Node.js
- Express.js
- PostgreSQL database
- Middleware for request validation and error handling

"

LINK NUMBER 19
Not enough lines

LINK NUMBER 20

File path: tests/test_lunar.py
"import datetime
import zoneinfo
from pathlib import Path

from icalendar import Calendar, Event, vCalAddress

from lunar_birthday_ical.ical import (
    add_attendees_to_event,
    add_event_to_calendar,
    add_reminders_to_event,
    create_calendar,
    get_local_datetime,
    local_datetime_to_utc_datetime,
)
from tests.__init__ import config


def test_get_local_datetime():
    local_date = ""2023-10-01""
    local_time = ""12:00:00""
    timezone = zoneinfo.ZoneInfo(""UTC"")
    result = get_local_datetime(local_date, local_time, timezone)
    expected = datetime.datetime(2023, 10, 1, 12, 0, tzinfo=timezone)
    assert result == expected


def test_local_datetime_to_utc_datetime():
    local_datetime = datetime.datetime(
        2023, 10, 1, 12, 0, tzinfo=zoneinfo.ZoneInfo(""Asia/Shanghai"")
    )
    result = local_datetime_to_utc_datetime(local_datetime)
    expected = datetime.datetime(2023, 10, 1, 4, 0, tzinfo=zoneinfo.ZoneInfo(""UTC""))
    assert result == expected


def test_add_reminders_to_event():
    event = Event()
    reminders = [1, 2]
    summary = ""Test Event""
    add_reminders_to_event(event, reminders, summary)
    assert len(event.subcomponents) == 2


def test_add_attendees_to_event_one():
    event = Event()
    attendees = [""test@example.com""]
    add_attendees_to_event(event, attendees)
    assert (
        len(
            [event.get(""ATTENDEE"")]
            if isinstance(event.get(""ATTENDEE""), vCalAddress)
            else event.get(""ATTENDEE"")
        )
        == 1
    )


def test_add_attendees_to_event_multi():
    event = Event()
    attendees = [""test@example.com"", ""test@example.net""]
    add_attendees_to_event(event, attendees)
    assert (
        len(
            [event.get(""ATTENDEE"")]
            if isinstance(event.get(""ATTENDEE""), vCalAddress)
            else event.get(""ATTENDEE"")
        )
        == 2
    )


def test_add_event_to_calendar():
    calendar = Calendar()
    dtstart = datetime.datetime(2023, 10, 1, 12, 0, tzinfo=zoneinfo.ZoneInfo(""UTC""))
    dtend = dtstart + datetime.timedelta(hours=1)
    summary = ""Test Event""
    reminders = [1]
    attendees = [""test@example.com""]
    add_event_to_calendar(calendar, dtstart, dtend, summary, reminders, attendees)
    assert len(calendar.subcomponents) == 1


def test_create_calendar(tmp_path: Path):
    output = tmp_path / ""test.ics""
    create_calendar(config, output)
    assert output.exists()
    with output.open(""rb"") as f:
        calendar_data = f.read()
    calendar = Calendar.from_ical(calendar_data)
    assert len(calendar.subcomponents) > 0
    assert calendar.get(""X-WR-CALNAME"") == ""Test Calendar"""

LINK NUMBER 21
Error fetching diff

LINK NUMBER 22
Error fetching diff

LINK NUMBER 23
Error fetching diff

LINK NUMBER 24
Not enough lines

LINK NUMBER 25
Not enough lines

LINK NUMBER 26

File path: plugin/src/main/java/github/benslabbert/txmanager/plugin/TransactionalAdvicePlugin.java
"        .intercept(Advice.withCustomMapping()
            .bind(Transactional.class, new AnnotationDescription.Loadable<Transactional>() {
                @Override
                public Class<? extends Annotation> getAnnotationType() {
                    return Transactional.class;
                }

                @Override
                public Transactional load() {
                    return annotationDescription.prepare(Transactional.class).load();
                }
            }).to(RequiresNewAdvice.class))"

LINK NUMBER 27

File path: ww/bufio/context_queue.c
"
/*
    @brief Destroys a buffer queue and releases its resources.
    @param self A pointer to the buffer queue to be destroyed.
*/
void bufferqueueDestory(buffer_queue_t *self);

/*
    @brief Pushes an sbuf_t pointer onto the back of the queue.
    @param self A pointer to the buffer queue.
    @param b A pointer to the sbuf_t to be added to the queue.
*/
void bufferqueuePush(buffer_queue_t *self, sbuf_t *b);

/*
    @brief Pops an sbuf_t pointer from the front of the queue.
    @param self A pointer to the buffer queue.
    @return A pointer to the sbuf_t at the front of the queue, or NULL if the queue is empty.
*/
sbuf_t *bufferqueuePop(buffer_queue_t *self);

/*
    @brief Gets the number of elements in the queue.
    @param self A pointer to the buffer queue.
    @return The number of sbuf_t pointers currently in the queue.
*/
size_t bufferqueueLen(buffer_queue_t *self);"

LINK NUMBER 28
Error fetching diff

LINK NUMBER 29
Error fetching diff

LINK NUMBER 30
Error fetching diff

LINK NUMBER 31
Not enough lines

LINK NUMBER 32
Not enough lines

LINK NUMBER 33

File path: 11.JS-Async-Exercises-2/01-Network-Request-Vizualization-Experiments/app.js
"async function fetchData() {
    try {
        const response = await fetch('https://swapi.dev/api/people/');
        const data = await response.json();
        createTable(data.results);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

function createTable(data) {
    const table = document.createElement('table');
    const headerRow = document.createElement('tr');

    // Create table headers
    const headers = ['Name', 'Height', 'Mass', 'Hair Color', 'Skin Color', 'Eye Color', 'Birth Year', 'Gender'];
    headers.forEach(headerText => {
        const header = document.createElement('th');
        header.textContent = headerText;
        headerRow.appendChild(header);
    });
    table.appendChild(headerRow);

    // Create table rows
    data.forEach(item => {
        const row = document.createElement('tr');
        Object.values(item).slice(0, 8).forEach(text => {
            const cell = document.createElement('td');
            cell.textContent = text;
            row.appendChild(cell);
        });
        table.appendChild(row);
    });

    // Append table to the div
    const dataTable = document.getElementById('data-table');
    dataTable.innerHTML = ''; // Clear any existing content
    dataTable.appendChild(table);
}"

LINK NUMBER 34

File path: js/script.js
"});

// Add dynamic background gradient for the photo wall
let fadeTimeout;
photoWall.addEventListener(""mousemove"", (event) => {
    const { clientX, clientY, currentTarget } = event;
    const { width, height, left, top } = currentTarget.getBoundingClientRect();
    const xPercent = ((clientX - left) / width) * 100;
    const yPercent = ((clientY - top) / height) * 100;

    // Update the background gradient based on the cursor's position
    photoWall.style.background = `radial-gradient(circle at ${xPercent}% ${yPercent}%, #ff7eb3, #ff758c, #ff6a6a)`;

    // Clear any existing fade timeout
    clearTimeout(fadeTimeout);

    // Set a timeout to fade the gradient when the cursor stops moving
    fadeTimeout = setTimeout(() => {
        photoWall.style.transition = ""background 0.8s ease""; // Smooth fade transition
        photoWall.style.background = `radial-gradient(circle at ${xPercent}% ${yPercent}%, white, #ff758c, #ff7eb3)`;
    }, 300); // 300ms delay before fading
});

// Function to randomly swap two images in the active set
function swapRandomImages() {
    // Select the active set
    const activeSet = document.querySelector("".photo-wall.set.active"");

    if (!activeSet) return; // Ensure there is an active set

    // Select all images within the active set
    const images = activeSet.querySelectorAll(""img"");

    if (images.length < 2) return; // Ensure there are at least two images to swap

    // Select two random images
    const firstIndex = Math.floor(Math.random() * images.length);
    let secondIndex;
    do {
        secondIndex = Math.floor(Math.random() * images.length);
    } while (secondIndex === firstIndex); // Ensure the two indices are different

    const firstImage = images[firstIndex];
    const secondImage = images[secondIndex];

    // Add fade-out effect
    firstImage.style.transition = ""opacity 0.5s ease"";
    secondImage.style.transition = ""opacity 0.5s ease"";
    firstImage.style.opacity = ""0"";
    secondImage.style.opacity = ""0"";

    // After fade-out, swap positions and fade back in
    setTimeout(() => {
        // Swap the actual DOM positions
        const parent = firstImage.parentNode;
        parent.insertBefore(secondImage, firstImage);

        // Fade back in
        firstImage.style.opacity = ""1"";
        secondImage.style.opacity = ""1"";
    }, 500); // Match the duration of the fade-out effect
}

// Set an interval to swap images every 3-5 seconds in the active set
setInterval(() => {
    swapRandomImages();
}, Math.random() * 2000 + 3000); // Random interval between 3-5 seconds

// Carousel Functionality
const sets = document.querySelectorAll("".photo-wall.set""); // Select all sets
const rightArrow = document.querySelector("".carousel-arrow.right-arrow""); // Select the right arrow button

let currentSetIndex = 0; // Track the current set index

// Function to show the current set
function showSet(index) {
    sets.forEach((set, i) => {
        set.classList.toggle(""active"", i === index); // Show the active set, hide others
    });
}

// Show the first set initially
showSet(currentSetIndex);

// Handle Right Arrow Click
rightArrow.addEventListener(""click"", () => {
    currentSetIndex = (currentSetIndex + 1) % sets.length; // Move to the next set, loop back to the start
    showSet(currentSetIndex); // Update the visible set"

LINK NUMBER 35
Error fetching diff

LINK NUMBER 36
Error fetching diff

LINK NUMBER 37
Error fetching diff

LINK NUMBER 38
Not enough lines

LINK NUMBER 39

File path: go/alphametics/alphametics.go
"	usedNumbers := make([]bool, 10)
	letterToNumber := make(map[string]int)

	if solveBacktrack(&equation, letters, letterToNumber, usedNumbers, 0) {
		return letterToNumber, nil
	}
	return nil, errors.New(""no solution found"")
}

func solveBacktrack(equation *equation, letters []string, letterToNumber map[string]int, usedNumbers []bool, index int) bool {
	fmt.Printf(""letters %v letterToNumber %v usedNumbers %v index %v\n"", letters, letterToNumber, usedNumbers, index) // Debug statement
	if index == len(letters) {
		return equation.evaluate(letterToNumber)
	}

	for num := 0; num <= 9; num++ {
		if !usedNumbers[num] {
			letterToNumber[letters[index]] = num
			usedNumbers[num] = true

			fmt.Printf(""Trying %s = %d\n"", letters[index], num) // Debug statement
			fmt.Printf(""Current map: %v\n"", letterToNumber)     // Debug statement

			if !equation.isLeadingZero(letterToNumber) && solveBacktrack(equation, letters, letterToNumber, usedNumbers, index+1) {
				return true
			}

			usedNumbers[num] = false
			delete(letterToNumber, letters[index])"

LINK NUMBER 40

File path: Day8/day8.ts
"import * as fs8 from ""fs"";

class Day8Execution {

    private readonly inputFilePath: string;
    private readonly data: string;
    private readonly inputMap: string[][];
    private posAntennas: Map<string, string>;

    constructor() {
        this.inputFilePath = ""real-input.txt"";
        this.data = fs8.readFileSync(this.inputFilePath, ""utf8"");
        this.inputMap = this.data.split(""\n"").map((line) => line.replace(""\r"", """").split("" ""));

        // parse the stringLine of every row to a string array 
        this.inputMap.forEach((stringLine, index) => {
            this.inputMap[index] = stringLine[0].split("""");
        });
        // console.log(this.inputMap);
    }

    // search for antennas in inputMap (could be letters or digits) and save the position in posAntennas 
    // (key: position (unique), value: antenna char)
    searchAntennas(): void {
        this.posAntennas = new Map<string, string>();
        for (let i = 0; i < this.inputMap.length; i++) {
            for (let j = 0; j < this.inputMap[i].length; j++) {
                if (RegExp(/[a-zA-Z0-9]/).exec(this.inputMap[i][j])) {
                    this.posAntennas.set(i + "","" + j, this.inputMap[i][j]);
                }
            }
        }

        // print the antennas and their positions 
        // this.posAntennas.forEach((value, key) => {
        //     console.log(key + "" -> "" + value);
        // });
    }

    // calculate antinode positions and return the total count
    calculateAnitnodePositions(): number {
        const antinodePositions = new Set<string>();
    
        const antennasByFreq = this.groupAntennasByFrequency();
        antennasByFreq.forEach((positions, freq) => {
            for (let i = 0; i < positions.length; i++) {
                for (let j = i + 1; j < positions.length; j++) {
                    const [x1, y1] = positions[i];
                    const [x2, y2] = positions[j];
    
                    // Skip if antennas are at the same position
                    if (x1 === x2 && y1 === y2) {
                        continue;
                    }
    
                    // Consider both ratios: 1:2 and 2:1
                    const ratios = [
                        { m: 1, n: 2 },
                        { m: 2, n: 1 },
                    ];
    
                    ratios.forEach(({ m, n }) => {
                        // Calculate internal and external division points
                        const internalPoint = this.dividePoints(x1, y1, x2, y2, m, n, true);
                        const externalPoint = this.dividePoints(x1, y1, x2, y2, m, n, false);
    
                        // Validate and add positions
                        [internalPoint, externalPoint].forEach(point => {
                            if (this.isValidPosition(point[0], point[1])) {
                                antinodePositions.add(`${point[0]},${point[1]}`);
                            }
                        });
                    });
                }
            }
        });
    
        // Return the total count of unique antinode positions
        return antinodePositions.size;
    }

    // group antennas by frequency, return new map with frequency as key and positions of antennas as value
    private groupAntennasByFrequency(): Map<string, Array<[number, number]>> {
        const antennasByFreq = new Map<string, Array<[number, number]>>();
        this.posAntennas.forEach((freq, pos) => {
            const [row, col] = pos.split(',').map(Number);
            if (!antennasByFreq.has(freq)) {
                antennasByFreq.set(freq, []);
            }
            antennasByFreq.get(freq)!.push([row, col]);
        });
        return antennasByFreq;
    }

    private dividePoints(
        x1: number,
        y1: number,
        x2: number,
        y2: number,
        m: number,
        n: number,
        isInternal: boolean
    ): [number, number] {
        let x: number;
        let y: number;
        if (isInternal) {
            x = (n * x1 + m * x2) / (m + n);
            y = (n * y1 + m * y2) / (m + n);
        } else {
            x = (n * x1 - m * x2) / (n - m);
            y = (n * y1 - m * y2) / (n - m);
        }
        return [x, y];
    }

    private isValidPosition(x: number, y: number): boolean {
        return (
            Number.isInteger(x) &&
            Number.isInteger(y) &&
            x >= 0 &&
            y >= 0 &&
            x < this.inputMap.length &&
            y < this.inputMap[x].length 
        );
    }

    getInputString(): string[][] {
        return this.inputMap;
    }
}

function main8() {
    let execution = new Day8Execution();
    execution.searchAntennas();
    let res = execution.calculateAnitnodePositions();
    console.log(`Number of unique antinode positions: ${res}`);
}

main8();"

LINK NUMBER 41

File path: study_ws/src/turtle_hunter_cpp/src/hunter_.cpp
"    void huntPrayCallback()
    {
        std::lock_guard<std::mutex> lock(mutex_);
        if (!pose_ || !target_){
            RCLCPP_ERROR(this->get_logger(), ""Error: Pose or target is not available."");
            return;
        }
        geometry_msgs::msg::Twist msg;

        if (target_distance_ > 0.5)
        {
            msg.linear.x  = kp_linear_ * target_distance_;
            double diff = std::fmod(goal_theta_ - pose_->theta + M_PI, 2 * M_PI) - M_PI;
            msg.angular.z = kp_angular_ * diff;
        }
        else
        {
            msg.linear.x  = 0.0;
            msg.angular.z = 0.0;
            threads_.emplace_back(&HunterNode::sendKillRequest, this, target_->name);
        }

        cmd_vel_publisher_->publish(msg);"

LINK NUMBER 42
Error fetching diff

LINK NUMBER 43
Error fetching diff

LINK NUMBER 44
Error fetching diff

LINK NUMBER 45

File path: UdderBot.js
"
//------------------ CONTROLLERS ------------------
let isBillionare = false;
let isWaiting = false;
let isBettingOff = false;
let isAutoGambaOn = false;
let isAutoGamba2On = false;
let isBroke = false;
let isWinstreak = false;
let rebirthed = true;
let riskUnder50 = 5; //if has less than 50m, risk 5m
let riskUnder100 = 10; //if has less than 100m, risk 10m
let riskUnder200 = 20; //if has less than 200m, risk 20m
let riskOver200 = 30; //if has more than 200m, risk 30m
let setAutoGamba2Risk=2; //set it to ""2k"" or ""200k"" or ""2""
let isAutoSpinOn = true;

//------------------ CONTROLLERS ------------------
"

LINK NUMBER 46

File path: __tests__/main.test.ts
"    expect(setOutputMock).toHaveBeenNthCalledWith(
      2,
      'release-status',
      'success'
    )
    expect(setOutputMock).toHaveBeenNthCalledWith(
      3,
      'target-url',
      'https://example.com'"

LINK NUMBER 47

File path: prepare_airport_data.py
"        if (
            _row[""gps_code""] in duplicate_icaos
            and _row[""ident""] != _row[""gps_code""]
        ):
            logger.info(
                f""ignoring duplicate entry {_row['ident']} for ""
                f""{_row['gps_code']} / {_row['iata_code']}.""
            )
            continue
        _longitude = float(_row[""longitude_deg""])
        _latitude = float(_row[""latitude_deg""])
        _timezone = tf.timezone_at(lng=_longitude, lat=_latitude)
        _country = countries[_row[""iso_country""]]
        if _timezone is None:
            logger.warning(""timezone info unknown: {}"".format(_row[""gps_code""]))
        _cursor.execute(
            ""REPLACE INTO airports(Name, City, Country, IATA, ICAO, Latitude, ""
            ""Longitude, Altitude, Timezone) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"",
            (
                _row[""name""],
                _row[""municipality""],
                _country,
                _row[""iata_code""],
                _row[""gps_code""],
                _latitude,
                _longitude,
                _row[""elevation_ft""],
                _timezone,
            ),"

LINK NUMBER 48
Not enough lines

LINK NUMBER 49
Error fetching diff

LINK NUMBER 50
Error fetching diff

LINK NUMBER 51
Error fetching diff

LINK NUMBER 52
Not enough lines

LINK NUMBER 53

File path: SpaceInvading/Resources/Pages/Game.xaml.cs
"
        private void SetupGame()
        {
            player = new Rectangle { Width = 50, Height = 20, Fill = Brushes.Blue };
            Canvas.SetLeft(player, (MainCanvas.Width - player.Width) / 2);
            Canvas.SetTop(player, MainCanvas.Height - player.Height - 10);
            MainCanvas.Children.Add(player);

            for (int i = 0; i < 5; i++)
            {
                Rectangle block = new() { Width = 60, Height = 30, Fill = Brushes.Red };
                Canvas.SetLeft(block, i * 70 + 20);
                Canvas.SetTop(block, 20);
                MainCanvas.Children.Add(block);
                blocks.Add(block);
            }
        }

        private void GameLoop(object sender, EventArgs e)
        {
            if (playerLeft && Canvas.GetLeft(player) > 0)
            {
                Canvas.SetLeft(player, Canvas.GetLeft(player) - playerSpeed);
            }
            if (playerRight && Canvas.GetLeft(player) < MainCanvas.Width - player.Width)
            {
                Canvas.SetLeft(player, Canvas.GetLeft(player) + playerSpeed);
            }
            if (playerAttack == KeyState.Pressed)
            {
                playerAttack = KeyState.Down;
                Shoot();
            }

            foreach (var bullet in bullets.ToArray())
            {
                Canvas.SetTop(bullet, Canvas.GetTop(bullet) - bulletSpeed);
                if (Canvas.GetTop(bullet) < 0)
                {
                    MainCanvas.Children.Remove(bullet);
                    bullets.Remove(bullet);
                }
            }

            foreach (var block in blocks.ToArray())
            {
                foreach (var bullet in bullets.ToArray())
                {
                    if (IsColliding(bullet, block))
                    {
                        MainCanvas.Children.Remove(bullet);
                        MainCanvas.Children.Remove(block);
                        bullets.Remove(bullet);
                        blocks.Remove(block);
                        break;
                    }
                }
            }
        }

        private bool IsColliding(Rectangle a, Rectangle b)
        {
            double aX = Canvas.GetLeft(a);
            double aY = Canvas.GetTop(a);
            double bX = Canvas.GetLeft(b);
            double bY = Canvas.GetTop(b);
            return aX < bX + b.Width && aX + a.Width > bX && aY < bY + b.Height && aY + a.Height > bY;
        }

        private void Window_KeyDown(object sender, KeyEventArgs e)
        {
            switch(e.Key)
            {
                case Key.A:
                    playerLeft = true;
                    break;
                case Key.D:
                    playerRight = true;
                    break;
                case Key.Space:
                    if (playerAttack == KeyState.Pressed || playerAttack == KeyState.Down)
                        playerAttack = KeyState.Down;
                    else
                        playerAttack = KeyState.Pressed;
                    break;
            }
        }

        private void Window_KeyUp(object sender, KeyEventArgs e)
        {
            switch(e.Key)
            {
                case Key.A:
                    playerLeft = false;
                    break;
                case Key.D:
                    playerRight = false;
                    break;
                case Key.Space:
                    playerAttack = KeyState.Released;
                    break;
            }
        }

        private void Shoot()
        {
            Rectangle bullet = new Rectangle { Width = 5, Height = 15, Fill = Brushes.Black };
            double x = Canvas.GetLeft(player) + player.Width / 2 - bullet.Width / 2;
            double y = Canvas.GetTop(player) - bullet.Height;
            Canvas.SetLeft(bullet, x);
            Canvas.SetTop(bullet, y);
            MainCanvas.Children.Add(bullet);
            bullets.Add(bullet);
        }
    }

    enum KeyState
    {
        Down,
        Pressed,
        Up,
        Released"

LINK NUMBER 54

File path: graph_1.cpp
"#include <bits/stdc++.h>
using namespace std;

// Graph using Adjacency Matrix

// Function to print the graph represented by an adjacency matrix
void PrintGraph(vector<vector<bool>> v, int vertex) {
    cout << ""Graph: "" << endl;
    // Loop through each vertex
    for (int i = 0; i < vertex; i++) {
        // Loop through each edge
        for (int j = 0; j < vertex; j++) {
            // Print the value of the adjacency matrix at position (i, j)
            cout << v[i][j] << "" "";
        }
        // Print a new line after each row of the matrix
        cout << endl;
    }
}

int main() {
    int vertex, edge;
    // Prompt the user to enter the number of vertices
    cout << ""Vertex: "";
    cin >> vertex;
    // Prompt the user to enter the number of edges
    cout << ""Edges: "";
    cin >> edge;
    // Undirected, unweighted graph
    vector<vector<bool>> AdjMat(vertex, vector<bool>(vertex, 0));
    int u, v;
    // Read the edges and update the adjacency matrix
    for (int i = 0; i < edge; i++) {
        cin >> u >> v;
        AdjMat[u][v] = 1;
        AdjMat[v][u] = 1;
    }
    // Print the graph
    PrintGraph(AdjMat, vertex);

    return 0;
}"

LINK NUMBER 55

File path: src/app/store/game/game.selectors.spec.ts
"  const initialState: GameState = {
    gameBoard: Array(9).fill({ gamePiece: '', isWinner: false }),
    player1: {
      name: 'Player 1',
      piece: 'X',
      wins: 0,
    },
    player2: {
      name: 'Player 2',
      piece: 'O',
      wins: 0,
    },
    currentPlayer: {
      name: 'Player 1',
      piece: 'X',
      wins: 0,
    },
    winner: null,
    isDraw: false,
    draws: 0,
  };

  it('should select the game board', () => {
    const result = selectGameBoard.projector(initialState);
    expect(result).toEqual(initialState.gameBoard);
  });

  it('should select the current player', () => {
    const result = selectCurrentPlayer.projector(initialState);
    expect(result).toEqual(initialState.currentPlayer);
  });

  it('should select the winner', () => {
    const result = selectWinner.projector(initialState);
    expect(result).toEqual(initialState.winner);
  });

  it('should select player 1', () => {
    const result = selectPlayer1.projector(initialState);
    expect(result).toEqual(initialState.player1);
  });

  it('should select player 2', () => {
    const result = selectPlayer2.projector(initialState);
    expect(result).toEqual(initialState.player2);
  });

  it('should select the number of draws', () => {
    const result = selectDraws.projector(initialState);
    expect(result).toEqual(initialState.draws);
  });

  it('should select if the game is a draw', () => {
    const result = selectIsDraw.projector(initialState);
    expect(result).toEqual(initialState.isDraw);"

LINK NUMBER 56
Error fetching diff

LINK NUMBER 57
Error fetching diff

LINK NUMBER 58
Error fetching diff

LINK NUMBER 59

File path: tailwind.config.ts
"  	extend: {
  		backgroundImage: {
  			'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
  			'gradient-conic': 'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))'
  		},
  		borderRadius: {
  			lg: 'var(--radius)',
  			md: 'calc(var(--radius) - 2px)',
  			sm: 'calc(var(--radius) - 4px)'
  		},
  		colors: {
  			background: 'hsl(var(--background))',
  			foreground: 'hsl(var(--foreground))',
  			card: {
  				DEFAULT: 'hsl(var(--card))',
  				foreground: 'hsl(var(--card-foreground))'
  			},
  			popover: {
  				DEFAULT: 'hsl(var(--popover))',
  				foreground: 'hsl(var(--popover-foreground))'
  			},
  			primary: {
  				DEFAULT: 'hsl(var(--primary))',
  				foreground: 'hsl(var(--primary-foreground))'
  			},
  			secondary: {
  				DEFAULT: 'hsl(var(--secondary))',
  				foreground: 'hsl(var(--secondary-foreground))'
  			},
  			muted: {
  				DEFAULT: 'hsl(var(--muted))',
  				foreground: 'hsl(var(--muted-foreground))'
  			},
  			accent: {
  				DEFAULT: 'hsl(var(--accent))',
  				foreground: 'hsl(var(--accent-foreground))'
  			},
  			destructive: {
  				DEFAULT: 'hsl(var(--destructive))',
  				foreground: 'hsl(var(--destructive-foreground))'
  			},
  			border: 'hsl(var(--border))',
  			input: 'hsl(var(--input))',
  			ring: 'hsl(var(--ring))',
  			chart: {
  				'1': 'hsl(var(--chart-1))',
  				'2': 'hsl(var(--chart-2))',
  				'3': 'hsl(var(--chart-3))',
  				'4': 'hsl(var(--chart-4))',
  				'5': 'hsl(var(--chart-5))'
  			}
  		}
  	}"

LINK NUMBER 60
Not enough lines

LINK NUMBER 61
Not enough lines

LINK NUMBER 62
Not enough lines

LINK NUMBER 63
Error fetching diff

LINK NUMBER 64
Error fetching diff

LINK NUMBER 65
Not enough lines

LINK NUMBER 66

File path: tests/phpunit/includes/classes/Fixes/FixesManagerTest.php
"<?php
/**
 * Test class for FixesManager.
 *
 * @package accessibility-checker
 */

use PHPUnit\Framework\TestCase;
use EqualizeDigital\AccessibilityChecker\Fixes\FixesManager;
use EqualizeDigital\AccessibilityChecker\Fixes\FixInterface;

/**
 * Unit tests for the FixesManager class.
 */
class FixesManagerTest extends TestCase {

	/**
	 * Setup the test environment by resetting the instance before each test.
	 *
	 * @return void
	 */
	public function setUp(): void {
		parent::setUp();
		// Reset the instance before each test.
		$reflection = new ReflectionClass( FixesManager::class );
		$instance   = $reflection->getProperty( 'instance' );
		$instance->setAccessible( true );
		$instance->setValue( null, null );
	}

	/**
	 * Test that the instance retuns an empty array when no fixes are registered.
	 *
	 * @return void
	 */
	public function test_get_fixes_settings_returns_empty_array_when_no_fixes() {
		$fixes_manager = FixesManager::get_instance();
		$this->assertEmpty( $fixes_manager->get_fixes_settings() );
	}

	/**
	 * Test that the instance returns the correct structure when fixes are registered.
	 *
	 * @return void
	 */
	public function test_get_fixes_settings_returns_correct_structure() {
		$fix_mock = $this->createMock( FixInterface::class );
		$fix_mock->method( 'get_fields_array' )->willReturn(
			[
				'field1' => [ 'default' => 'value1' ],
				'field2' => [ 'default' => 'value2' ],
			]
		);
		$fix_mock->method( 'get_slug' )->willReturn( 'mock_fix' );
		$fix_mock->is_pro = true;

		$fixes_manager  = FixesManager::get_instance();
		$reflection     = new ReflectionClass( $fixes_manager );
		$fixes_property = $reflection->getProperty( 'fixes' );
		$fixes_property->setAccessible( true );
		$fixes_property->setValue( $fixes_manager, [ 'mock_fix' => $fix_mock ] );

		$expected = [
			'mock_fix' => [
				'fields' => [
					'field1' => 'value1',
					'field2' => 'value2',
				],
				'is_pro' => true,
			],
		];

		$this->assertEquals( $expected, $fixes_manager->get_fixes_settings() );
	}

	/**
	 * Test that the instance returns the default values when options aren't set.
	 *
	 * @return void
	 */
	public function test_get_fixes_settings_uses_default_values() {
		$fix_mock = $this->createMock( FixInterface::class );
		$fix_mock->method( 'get_fields_array' )->willReturn(
			[
				'field1' => [ 'default' => 'default_value1' ],
				'field2' => [ 'default' => 'default_value2' ],
			]
		);
		$fix_mock->method( 'get_slug' )->willReturn( 'mock_fix' );

		$fixes_manager = FixesManager::get_instance();
		$reflection    = new ReflectionClass( $fixes_manager );
		$fixes_propert = $reflection->getProperty( 'fixes' );
		$fixes_propert->setAccessible( true );
		$fixes_propert->setValue( $fixes_manager, [ 'mock_fix' => $fix_mock ] );

		$expected = [
			'mock_fix' => [
				'fields' => [
					'field1' => 'default_value1',
					'field2' => 'default_value2',
				],
				'is_pro' => false,
			],
		];

		$this->assertEquals( $expected, $fixes_manager->get_fixes_settings() );
	}
}"

LINK NUMBER 67

File path: sql_db/src/app.py
"from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from crossref.restful import Works

app = Flask(__name__, template_folder=""../templates"")
DB_FILE = ""./mydata/refs.db""

# Helper function to connect to the database
def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

# Home route to display all references
@app.route(""/"")
def index():
    conn = get_db_connection()
    refs = conn.execute(""""""
        SELECT refs.ref_id, refs.type,
               (SELECT GROUP_CONCAT(author_name, ', ') 
                FROM authors 
                WHERE authors.ref_id = refs.ref_id) AS authors,
               MAX(CASE WHEN ref_dat.key = 'title' THEN ref_dat.value END) AS title,
               MAX(CASE WHEN ref_dat.key = 'journal' THEN ref_dat.value END) AS journal,
               MAX(CASE WHEN ref_dat.key = 'year' THEN ref_dat.value END) AS year,
               MAX(CASE WHEN ref_dat.key = 'doi' THEN ref_dat.value END) AS doi
        FROM refs
        LEFT JOIN ref_dat ON refs.ref_id = ref_dat.ref_id
        GROUP BY refs.ref_id
    """""").fetchall()
    conn.close()
    return render_template(""index.html"", refs=refs)

# Route to view details of a specific reference
@app.route(""/ref/<int:ref_id>"")
def view_ref(ref_id):
    conn = get_db_connection()
    ref = conn.execute(""SELECT * FROM refs WHERE ref_id = ?"", (ref_id,)).fetchone()
    authors = conn.execute(""SELECT author_name FROM authors WHERE ref_id = ?"", (ref_id,)).fetchall()
    ref_data = conn.execute(""SELECT key, value FROM ref_dat WHERE ref_id = ?"", (ref_id,)).fetchall()
    conn.close()
    return render_template(""view_ref.html"", ref=ref, authors=authors, ref_data=ref_data)

# Route to add a new reference
@app.route(""/add/<ref_type>"", methods=[""GET"", ""POST""])
def add_ref(ref_type):
    if request.method == ""POST"":
        authors = request.form.getlist(""authors"")
        ref_data = {key: value for key, value in request.form.items() if key not in [""authors"", ""submit""]}

        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert into refs table
        cursor.execute(""INSERT INTO refs (type) VALUES (?)"", (ref_type,))
        ref_id = cursor.lastrowid

        # Insert authors
        for author in authors:
            if author.strip():
                cursor.execute(""INSERT INTO authors (ref_id, author_name) VALUES (?, ?)"", (ref_id, author.strip()))

        # Insert ref details
        for key, value in ref_data.items():
            if value.strip():
                cursor.execute(""INSERT INTO ref_dat (ref_id, key, value) VALUES (?, ?, ?)"", (ref_id, key.strip(), value.strip()))

        conn.commit()
        conn.close()
        return redirect(url_for(""index""))

    return render_template(""add_ref.html"", ref_type=ref_type)

# Route to delete a reference
@app.route(""/delete/<int:ref_id>"", methods=[""POST""])
def delete_ref(ref_id):
    conn = get_db_connection()
    conn.execute(""DELETE FROM refs WHERE ref_id = ?"", (ref_id,))
    conn.execute(""DELETE FROM authors WHERE ref_id = ?"", (ref_id,))
    conn.execute(""DELETE FROM ref_dat WHERE ref_id = ?"", (ref_id,))
    conn.commit()
    conn.close()
    return redirect(url_for(""index""))

# Route to fetch DOI details
@app.route(""/fetch_doi"", methods=[""POST""])
def fetch_doi():
    doi = request.json.get(""doi"")
    if not doi:
        return jsonify({""error"": ""DOI is required""}), 400

    works = Works()
    try:
        ref = works.doi(doi)
        if not ref:
            return jsonify({""error"": ""DOI not found""}), 404

        # Extract relevant fields
        data = {
            ""title"": ref.get(""title"", [""""])[0],
            ""year"": ref.get(""published-print"", {}).get(""date-parts"", [[None]])[0][0] or ref.get(""published-online"", {}).get(""date-parts"", [[None]])[0][0],
            ""journal"": ref.get(""container-title"", [""""])[0],
            ""volume"": ref.get(""volume"", """"),
            ""issue"": ref.get(""issue"", """"),
            ""pages"": ref.get(""page"", """"),
            ""authors"": "", "".join([f""{author['family']} {author['given']}"" for author in ref.get(""author"", [])]),
        }
        return jsonify(data)
    except Exception as e:
        return jsonify({""error"": str(e)}), 500

if __name__ == ""__main__"":
    app.run(debug=True)"

LINK NUMBER 68

File path: webapp/main.py
"    return {'token': string}


class Text(BaseModel):
    text: str

# Create a FastAPI endpoint that accepts a POST request with a JSON body containing a single field called ""text"" and returns a checksum of the text.
# The checksum should be a SHA-256 hash of the text encoded in base64.
# The endpoint should return a JSON response with a single field called ""checksum"" containing the base64-encoded checksum.
@app.post('/checksum')
def checksum(text: Text):
    import hashlib
    checksum = hashlib.sha256(text.text.encode()).digest()
    return {'checksum': base64.b64encode(checksum).decode()}
"

LINK NUMBER 69
Error fetching diff

LINK NUMBER 70
Error fetching diff

LINK NUMBER 71
Error fetching diff

LINK NUMBER 72
Not enough lines

LINK NUMBER 73
Not enough lines

LINK NUMBER 74
Not enough lines

LINK NUMBER 75

File path: backend/controllers/email.controller.js
"        const fromUserId = req.id;
        const { to, subject, message } = req.body;

        if (!to || !subject || !message) return res.status(400).json({
            message: ""All the information is required"",
            success: false,
        });

        const toUser = await User.findOne({ email: to });
        if (!toUser) return res.status(404).json({
            message: ""Recipient user not found"",
            success: false,
        });

        const email = await Email.create({
            to: toUser.email,
            subject,
            message,
            userId: fromUserId
        });

        // Save the email for the recipient user as well
        await Email.create({
            to: toUser.email,
            subject,
            message,
            userId: toUser._id
        });

        return res.status(201).json({
            email,
            message: ""Message sent successfully"",
            success: true,
        });"

LINK NUMBER 76
Error fetching diff

LINK NUMBER 77
Error fetching diff

LINK NUMBER 78
Error fetching diff

LINK NUMBER 79

File path: LeetCodeProblems/1040MovingStonesUntilConsecutiveTwo.py
"class Solution:
    def numMovesStonesII(stones):
        stones.sort()
        i, n, low = 0, len(stones), len(stones)
        total = len(stones)
        sSum = stones[-1] - stones[0] + 1 - total
        high = sSum - min(stones[1] - stones[0] -1, stones[-1] - stones[-2] - 1)
        if (stones[total-2] - stones[0] + 1) == total - 1:
            low = min(stones[total-1] - stones[total-2] - 1, 2)
            return [high, low]
        if (stones[total-1] - stones[1] + 1) == total - 1:
            low = min(stones[1] - stones[0] - 1, 2)
            return [high, low]
        
        for j in range(n):
            while stones[j] - stones[i] > n:
                i += 1
            low = min(low, n - (j - i + 1))
        return [low, high]

stones = [7,4,9]
ans = Solution.numMovesStonesII(stones)
print(ans)  # Output: [1,2]
    
    "

LINK NUMBER 80

File path: main.py
"# ERROR:
# 'becoz of `post`'
# @app.put('/posts/update/{id}')
# def update_post(id: int, post: Post):
#     for index, post in enumerate(my_posts):
#         if post['id'] == id:
#             my_posts[index]['title'] = post.title
#             return {'all-post': my_posts}
#     return {'message': 'post not found'}

# Works!! (Copilot):
# solved it via changing `post` -> `updated_post`
"

LINK NUMBER 81

File path: controllers/api/rating-routes.js
"const router = require('express').Router();
const { Rating } = require('../../models');

// these aren't definite routes, just a starting point based off what I think we need.
// route to get all ratings
router.get(""/"", async (req, res) => {
  try {
    const ratingData = await Rating.findAll();
    res.status(200).json(ratingData);
  } catch (err) {
    res.status(500).json(err);
  }
});

// route to get one rating
router.get(""/:id"", async (req, res) => {
  try {
    const ratingData = await Rating.findByPk(req.params.id);
    if (!ratingData) {
      res.status(404).json({ message: ""No rating found with this id!"" });
      return;
    }
    res.status(200).json(ratingData);
  } catch (err) {
    res.status(500).json(err);
  }
});

// router to get all ratings by user
router.get(""/user/:user_id"", async (req, res) => {
  try {
    const ratingData = await Rating.findAll({ where: { user_id: req.params.user_id } });
    if (!ratingData) {
      res.status(404).json({ message: ""No ratings found with this user!"" });
      return;
    }
    res.status(200).json(ratingData);
  } catch (err) {
    res.status(500).json(err);
  }
});

// route to get one rating by user
router.get(""/user/:user_id/:id"", async (req, res) => {
  try {
    const ratingData = await Rating.findOne({ where: { user_id: req.params.user_id, id: req.params.id } });
    if (!ratingData) {
      res.status(404).json({ message: ""No rating found with this user!"" });
      return;
    }
    res.status(200).json(ratingData);
  } catch (err) {
    res.status(500).json(err);
  }
});


// copilot mumbo jumbo, don't know if we need, but can be used as a reference for the future
// route to get average rating for a song
router.get(""/average/:music_id"", async (req, res) => {
  try {
    const ratingData = await Rating.findAll({ where: { music_id: req.params.music_id } });
    if (!ratingData) {
      res.status(404).json({ message: ""No ratings found for this song!"" });
      return;
    }
    let total = 0;
    for (let i = 0; i < ratingData.length; i++) {
      total += ratingData[i].rating;
    }
    const average = total / ratingData.length;
    res.status(200).json(average);
  } catch (err) {
    res.status(500).json(err);
  }
});

module.exports = router;"

LINK NUMBER 82

File path: src/main/java/com/codedotorg/HonestHeadlines.java
"        for (String word : sensationalWords) {
            if (headline.toLowerCase().contains(word.toLowerCase())) {
                return ""Sensational"";
            }
        }
        return ""Not Sensational"";"

LINK NUMBER 83
Error fetching diff

LINK NUMBER 84
Error fetching diff

LINK NUMBER 85
Error fetching diff

LINK NUMBER 86
Not enough lines

LINK NUMBER 87
Not enough lines

LINK NUMBER 88
Not enough lines

LINK NUMBER 89

File path: music_services/utils.py
"import re

def extract_song_artist(string):
    string = re.sub(r'\[.*?\]', '', string)  # Remove anything in square brackets
    pattern = re.compile(r'^(.+) - (.+)')
    match = pattern.match(string)
    if match:
        return match.groups()
    else:
        return None
    
def url_sanitiser(url):
    tidal_link_pattern = re.compile(r'https?://(?:www\.)?tidal\.com/browse/track/\d+')
    spotify_link_pattern = re.compile(r'https://open\.spotify\.com/track/[a-zA-Z0-9]+')
    youtube_link_pattern = re.compile(r'(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+')

    tidal_link = re.search(tidal_link_pattern, url)
    spotify_link = re.search(spotify_link_pattern, url)
    youtube_link= re.search(youtube_link_pattern, url)

    if youtube_link:
      return { 'source_platform': 'youtube', 'id': url }
        
    if tidal_link:
      track_id = re.search(r'\d+', url)
      return { 'source_platform': 'tidal', 'id': track_id.group(0)}

    if spotify_link:
      track_id = re.search(r'https://open\.spotify\.com/track/([a-zA-Z0-9]+)', url)
      return { 'source_platform': 'spotify', 'id': track_id.group(1) }

    return None"

LINK NUMBER 90
Error fetching diff

LINK NUMBER 91
Error fetching diff

LINK NUMBER 92
Error fetching diff

LINK NUMBER 93

File path: webpack.config.js
"#homeTab {
    width: 80%;
    height:80%;
    background-color: aquamarine;

};

#descriptionContainer {
    width: 20%;
    height: 20%;
    background-color: rgb(9, 49, 36);
};

#hoursContainer {
    width: 20%;
    height: 20%;
    background-color: rgb(23, 77, 59);
}

#locationContainer {
    width: 20%;
    height: 20%;
    background-color: rgb(3, 129, 87);
}
"

LINK NUMBER 94

File path: src/helper.ts
"		""Cut selection. Cut line on empty selection"": { key: ""⌘X"", wkey: ""Ctrl+X"", id: ""editor.action.clipboardCutAction"" },
		""Copy Selection"": { key: ""⌘C"", wkey: ""Ctrl+C"", id: ""editor.action.clipboardCopyAction"" },
		""Copy line (empty selection"": { key: ""⌘C"", wkey: ""Ctrl+C"", id: ""editor.action.clipboardCopyAction"" },
		""Move line down"": { key: ""⌥↓"", wkey: ""Alt+Down"", id: ""editor.action.moveLinesDownAction"" },
		""Move line up"": { key: ""⌥↑"", wkey: ""Alt+Up"", id: ""editor.action.moveLinesUpAction"" },
		""Copy line down"": { key: ""⇧⌥↓"", wkey: ""Shift+Alt+Down"", id: ""editor.action.copyLinesDownAction"" },
		""Copy line up"": { key: ""⇧⌥↑"", wkey: ""Shift+Alt+Up"", id: ""editor.action.copyLinesUpAction"" },
		""Delete line"": { key: ""⇧⌘K"", wkey: ""Shift+Ctrl+K"", id: ""editor.action.deleteLines"" },
		""Insert line below"": { key: ""⌘Enter"", wkey: ""Ctrl+Enter"", id: ""editor.action.insertLineAfter"" },
		""Insert line above"": { key: ""⇧⌘Enter"", wkey: ""Shift+Ctrl+Enter"", id: ""editor.action.insertLineBefore"" },
		""Jump to matching bracket"": { key: ""⇧⌘\\"", wkey: ""Shift+Ctrl+\\"", id: ""editor.action.jumpToBracket"" },
		""Indent line"": { key: ""⌘]"", wkey: ""Ctrl+]"", id: ""editor.action.indentLines"" },
		""outdent line"": { key: ""⌘["", wkey: ""Ctrl+["", id: ""editor.action.outdentLines"" },
		""Go to beginning of line"": { key: ""Home"", wkey: ""Home"", id: ""cursorHome"" },
		""Go end of line"": { key: ""End"", wkey: ""End"", id: ""cursorEnd"" },
		""Go to beginning of file"": { key: ""⌘↑"", wkey: ""Ctrl+Up"", id: ""cursorTop"" },
		""Go to end of file"": { key: ""⌘↓"", wkey: ""Ctrl+Down"", id: ""cursorBottom"" },
		""Scroll line up"": { key: ""⌃PgUp"", wkey: ""Ctrl+PgUp"", id: ""scrollLineUp"" },
		""Scroll page down"": { key: ""⌘PgDown"", wkey: ""Ctrl+PgDown"", id: ""scrollPageDown"" },
		""Fold region"": { key: ""⌥⌘["", wkey: ""Alt+Ctrl+["", id: ""editor.fold"" },
		""Unfold region"": { key: ""⌥⌘]"", wkey: ""Alt+Ctrl+]"", id: ""editor.unfold"" },
		""Fold all subregions"": { key: ""⌘K ⌘["", wkey: ""Ctrl+K Ctrl+["", id: ""editor.foldRecursively"" },
		""Unfold all subregions"": { key: ""⌘K ⌘]"", wkey: ""Ctrl+K Ctrl+]"", id: ""editor.unfoldRecursively"" },
		""Fold all regions"": { key: ""⌘K ⌘0"", wkey: ""Ctrl+K Ctrl+0"", id: ""editor.foldAll"" },
		""Unfold all regions"": { key: ""⌘K ⌘J"", wkey: ""Ctrl+K Ctrl+J"", id: ""editor.unfoldAll"" },
		""Add line comment"": { key: ""⌘/"", wkey: ""Ctrl+/"", id: ""editor.action.addCommentLine"" },
		""Remove line comment"": { key: ""⌘K ⌘U"", wkey: ""Ctrl+K Ctrl+U"", id: ""editor.action.removeCommentLine"" },
		""Toggle line comment"": { key: ""⌘/"", wkey: ""Ctrl+/"", id: ""editor.action.commentLine"" },
		""Toggle block comment"": { key: ""⇧⌥A"", wkey: ""Shift+Alt+A"", id: ""editor.action.blockComment"" },
		""Toggle word wrap"": { key: ""⌥Z"", wkey: ""Alt+Z"", id: ""editor.action.toggleWordWrap"" },		"

LINK NUMBER 95
Not enough lines

LINK NUMBER 96
Not enough lines

LINK NUMBER 97
Error fetching diff

LINK NUMBER 98
Error fetching diff

LINK NUMBER 99
Error fetching diff

LINK NUMBER 100

File path: listen.py
"    print(hotkeys)
    return hotkeys



# hhh = loadHotkeys()
# hhh[""<ctrl>+<alt>+p""]()
# print(hhh)
def addHotkeys(hotkeyDict):

    with keyboard.GlobalHotKeys(
    #     {
    #     ""<ctrl>+<alt>+p"": lambda: callUserHotkey(""python3 /Users/sh/DEV/password-generator/generate-password.py""),
        
    #     ""<ctrl>+<alt>+<cmd>+o"": lambda: callUserHotkey(""python3 /Users/sh/DEV/macroni/scripts/reload.py"")
    # }
    hotkeyDict
    ) as h:
        h.join()

addHotkeys(loadHotkeys())
# Attempting to initialise multiple global hotkeys with small dict to fix lamda dict issue
# does not work, only the first executes
def initHotkeys():
    f = open(""/Users/sh/DEV/macroni/hotkeys.json"", ""rt"")
    hotkey_string_commands = json.loads(f.read())
    # hotkeys = {}
    for key, value in hotkey_string_commands.items():

        addHotkeys({key: lambda: callUserHotkey(hotkey_string_commands[key])})
    # print(hotkeys)
    f.close()
    # print(hotkeys)
    # return hotkeys
# initHotkeys()"

LINK NUMBER 101
Not enough lines

LINK NUMBER 102
Not enough lines

LINK NUMBER 103
Not enough lines

LINK NUMBER 104
Error fetching diff

LINK NUMBER 105
Error fetching diff

LINK NUMBER 106
Error fetching diff

LINK NUMBER 107

File path: Highscore.py
"class Highscore:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lessthan__(self, other):
        return self.score < other.score

    def __greaterthan__(self, other):
        return self.score > other.score

    def __equal__(self, other):
        return self.score == other.score

    def __lessthanorequal__(self, other):
        return self.score <= other.score

    def __greaterthanorequal__(self, other):
        return self.score >= other.score

    def __notqual__(self, other):
        return self.score != other.score

    def __str__(self):
        return self.name + "" "" + str(self.score)

    def __repr__(self):
        return self.name + "" "" + str(self.score)
"

LINK NUMBER 108

File path: app/src/main/java/com/example/amanid/signup_page.java
"    }
        hint_answer_edit_text = findViewById(R.id.hint_answer_edit_text);
        button9 = findViewById(R.id.button9);
        button9.setOnClickListener( new View.OnClickListener(){
            public void onClick(View v) {
                database = FirebaseDatabase.getInstance();
                reference = database.getReference(""users"");
                String idnum = editTextid_signup.getText().toString();
                String pass = editTextpass.getText().toString();
                String pass2 = editTextpass2.getText().toString();
                String qhint = editTextid_qhint.getText().toString();
                HelperClass helperClass = new HelperClass(idnum , pass , pass2 ,qhint);
                reference.child(idnum).setValue(helperClass);
                Toast.makeText(signup_page.this, ""you have signup successfully!"",Toast.LENGTH_LONG).show();
                Intent intent = new Intent(signup_page.this,done_page9.class);

            }
        });

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(signup_page.this,know_more_about_qhint.class));
            }
        });
"

LINK NUMBER 109
Not enough lines

LINK NUMBER 110

File path: eligibility/utils.py
"

class UtilityTests(TestCase):
    def test_get_age_edge_cases(self):
        ""Ensure that get_age() handles edge cases correctly.""
        player = PlayerFactory.create(date_of_birth=date(2014, 2, 8))
        for census_date, expected_age in [
            (date(2022, 2, 7), 7),
            (date(2022, 2, 8), 8),
            (date(2022, 2, 9), 8),
        ]:
            with self.subTest(census_date=census_date):
                self.assertEqual(get_age(player, census_date), expected_age)"

LINK NUMBER 111
Error fetching diff

LINK NUMBER 112
Error fetching diff

LINK NUMBER 113
Error fetching diff

LINK NUMBER 114
Not enough lines

LINK NUMBER 115

File path: server/aarogyam-server/src/dao/user.dao.ts
"import { PrismaClient, Token, TokenType } from ""@prisma/client"";

const tokenClient = new PrismaClient().token;

/**
 * Creates a new token (either verification or reset password) for a user.
 *
 * @param userId - The ID of the user.
 * @param token - The token string.
 * @param type - The type of the token (VERIFICATION or RESET_PASSWORD).
 * @returns A promise that resolves to the created token.
 */
export const createToken = async (
  userId: number,
  token: string,
  type: TokenType
): Promise<Token> => {
  return tokenClient.create({
    data: {
      userId,
      token,
      type,
    },
  });
};

/**
 * Deletes tokens by user ID and token type.
 *
 * @param userId - The ID of the user whose tokens are to be deleted.
 * @param type - The type of the token (VERIFICATION or RESET_PASSWORD).
 * @returns A promise that resolves to the result of the delete operation.
 */
export const deleteTokensByUserId = async (userId: number, type: TokenType) => {
  return tokenClient.deleteMany({
    where: {
      userId,
      type,
    },
  });
};

/**
 * Retrieves a token by its token string and type.
 *
 * @param token - The token string.
 * @param type - The type of the token (VERIFICATION or RESET_PASSWORD).
 * @returns A promise that resolves to the found token, including the associated user.
 */
export const getTokenByTokenString = async (
  token: string,
  type: TokenType
): Promise<Token | null> => {
  return tokenClient.findFirst({
    where: {
      token,
      type,
    },
    include: {
      user: true,
    },
  });
};"

LINK NUMBER 116
Not enough lines

LINK NUMBER 117
Not enough lines

LINK NUMBER 118
Error fetching diff

LINK NUMBER 119
Error fetching diff

LINK NUMBER 120
Error fetching diff

LINK NUMBER 121

File path: assets/layout.js
"  layout.innerHTML = ` <div class=""container bg-gray-300 rounded-2xl mx-auto flex flex-col justify-between m-3"">
  <div class=""flex flex-col justify-between mx-auto m-3 items-center"">
      <h1 class=""font-josefin text-2xl"">Player?</h1>

      <div class="""">
          <button
              class=""player bg-transparent w-20 border-2 border-black rounded-xl m-3 hover:bg-gray-200 ease-in duration-300 shadow-btn"">X</button>
          <button
              class=""player bg-transparent w-20 border-2 border-black rounded-xl m-3 hover:bg-gray-200 ease-in duration-300 shadow-btn"">O</button>
      </div>

  </div>

  <div class=""container mx-auto w-2/4 p-3 mt-10 h-3/4 flex items-center justify-center"">
      <div class=""grid grid-cols-3 place-items-center font-cursive"">
          <button
              class=""gameCard relative border-4 border-l-0 border-t-0 text-5xl md:text-9xl min-h-16 md:min-h-36 min-w-16 md:min-w-32 after:absolute after:-translate-x-2/4 after:-translate-y-2/4 after:left-2/4 after:top-2/4 after:text-5xl after:md:text-9xl after:text-gray-400 ""></button>
          <button
              class=""gameCard relative border-4 border-l-0 border-r-0 border-t-0 text-5xl md:text-9xl min-h-16 md:min-h-36 min-w-16 md:min-w-32 after:absolute after:-translate-x-2/4 after:-translate-y-2/4 after:left-2/4 after:top-2/4 after:text-5xl after:md:text-9xl after:text-gray-400 ""></button>
          <button
              class=""gameCard relative border-4 border-r-0 border-t-0 text-5xl md:text-9xl min-h-16 md:min-h-36 min-w-16 md:min-w-32 after:absolute after:-translate-x-2/4 after:-translate-y-2/4 after:left-2/4 after:top-2/4 after:text-5xl after:md:text-9xl after:text-gray-400 ""></button>
          <button
              class=""gameCard relative border-4 border-l-0 text-5xl md:text-9xl min-h-16 md:min-h-36 min-w-16 md:min-w-32 after:absolute after:-translate-x-2/4 after:-translate-y-2/4 after:left-2/4 after:top-2/4 after:text-5xl after:md:text-9xl after:text-gray-400 ""></button>
          <button
              class=""gameCard relative border-4 border-l-0 border-r-0 text-5xl md:text-9xl min-h-16 md:min-h-36 min-w-16 md:min-w-32 after:absolute after:-translate-x-2/4 after:-translate-y-2/4 after:left-2/4 after:top-2/4 after:text-5xl after:md:text-9xl after:text-gray-400 ""></button>
          <button
              class=""gameCard relative border-4 border-r-0 text-5xl md:text-9xl min-h-16 md:min-h-36 min-w-16 md:min-w-32 after:absolute after:-translate-x-2/4 after:-translate-y-2/4 after:left-2/4 after:top-2/4 after:text-5xl after:md:text-9xl after:text-gray-400 ""></button>
          <button
              class=""gameCard relative border-4 border-l-0 border-b-0 text-5xl md:text-9xl min-h-16 md:min-h-36 min-w-16 md:min-w-32 after:absolute after:-translate-x-2/4 after:-translate-y-2/4 after:left-2/4 after:top-2/4 after:text-5xl after:md:text-9xl after:text-gray-400 ""></button>
          <button
              class=""gameCard relative border-4 border-l-0 border-r-0 border-b-0 text-5xl md:text-9xl min-h-16 md:min-h-36 min-w-16 md:min-w-32 after:absolute after:-translate-x-2/4 after:-translate-y-2/4 after:left-2/4 after:top-2/4 after:text-5xl after:md:text-9xl after:text-gray-400 ""></button>
          <button
              class=""gameCard relative border-4 border-r-0 border-b-0 text-5xl md:text-9xl min-h-16 md:min-h-36 min-w-16 md:min-w-32 after:absolute after:-translate-x-2/4 after:-translate-y-2/4 after:left-2/4 after:top-2/4 after:text-5xl after:md:text-9xl after:text-gray-400 ""></button>
      </div>
  </div>
</div>`;"

LINK NUMBER 122
Not enough lines

LINK NUMBER 123

File path: components/SmoothGrid.js
"/** Creates A Div Element With A ease-in-out Transition Of
 * grid-template-columns
 * grid-template-rows
 * gap
 * on an automatic div element with grid mutations
*/

import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Transition } from 'react-transition-group';

export default class SmoothGrid extends Component { // eslint-disable-line react/prefer-stateless-function
  static propTypes = {
    children: PropTypes.node,
    style: PropTypes.object,
    className: PropTypes.string,
    gridTemplateColumns: PropTypes.string,
    gridTemplateRows: PropTypes.string,
    gap: PropTypes.string,
    duration: PropTypes.number,
    onEnter: PropTypes.func,
    onEntered: PropTypes.func,
    onEntering: PropTypes.func,
    onExit: PropTypes.func,
    onExited: PropTypes.func,
    onExiting: PropTypes.func,
  };

  static defaultProps = {
    duration: 300,
  };

  render() {
    const {
      children,
      style,
      className,
      gridTemplateColumns,
      gridTemplateRows,
      gap,
      duration,
      onEnter,
      onEntered,
      onEntering,
      onExit,
      onExited,
      onExiting,
      ...props
    } = this.props;

    return (
      <Transition
        {...props}
        timeout={{
          enter: duration,
          exit: duration,
        }}
        onEnter={onEnter}
        onEntered={onEntered}
        onEntering={onEntering}
        onExit={onExit}
        onExited={onExited}
        onExiting={onExiting}
      >
        {state => (
          <div
            style={{
              ...style,
              gridTemplateColumns,
              gridTemplateRows,
              gap,
              transition: `all ${duration}ms ease-in-out`,
              ...(state === 'entered' && {
                gridTemplateColumns: 'auto',
                gridTemplateRows: 'auto',
                gap: '0',
              }),
            }}
            className={`smooth-grid ${className}`}
          >
            {children}
          </div>
        )}
        </Transition>
    );
  }
}"

LINK NUMBER 124

File path: target.c
"#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifndef _HAVE_ARGV_FUZZ_INL
#define _HAVE_ARGV_FUZZ_INL

// Function prototypes
void add(double num1, double num2);
void sub(double num1, double num2);
void mul(double num1, double num2);
void divi(double num1, double num2);
void parse_args(int argc, char **argv);

// Main function
int main(int argc, char **argv) {
    if (argc < 4) {
        fprintf(stderr, ""Usage: %s <operation> <num1> <num2>\n"", argv[0]);
        return 1;
    }
    // Intentional bug: potential null pointer dereference
    if (argv == NULL) {
        fprintf(stderr, ""Error: argv is NULL\n"");
        return 1;
    }
    parse_args(argc, argv);
    return 0;
}

// Function to parse arguments and call appropriate operation
void parse_args(int argc, char **argv) {
    char operation[10]; // Ensure this array is declared
    double num1 = atof(argv[2]);
    double num2 = atof(argv[3]);

    // Intentional bug: potential buffer overflow
    strcpy(operation, argv[1]);

    // Intentional bug: uninitialized variable
    int uninitialized_var;
    if (uninitialized_var == 0) {
        printf(""Uninitialized variable is zero\n"");
    }

    // Intentional bug: off-by-one error
    if (argv[4] != NULL) {
        printf(""Accessing out-of-bounds index\n"");
    }

    // Intentional bug: memory leak
    char *leak = (char *)malloc(100);
    strcpy(leak, ""This memory is not freed"");

    if (strcmp(operation, ""add"") == 0) {
        add(num1, num2);
    } else if (strcmp(operation, ""sub"") == 0) {
        sub(num1, num2);
    } else if (strcmp(operation, ""mul"") == 0) {
        mul(num1, num2);
    } else if (strcmp(operation, ""div"") == 0) {
        divi(num1, num2);
    } else {
        fprintf(stderr, ""Unknown operation: %s\n"", operation);
    }
}

// Addition function
void add(double num1, double num2) {
    printf(""Result: %f\n"", num1 + num2);
}

// Subtraction function
void sub(double num1, double num2) {
    printf(""Result: %f\n"", num1 - num2);
}

// Multiplication function
void mul(double num1, double num2) {
    printf(""Result: %f\n"", num1 * num2);
}

// Division function
void divi(double num1, double num2) {
    // Intentional bug: no check for division by zero
    printf(""Result: %f\n"", num1 / num2);
}

#endif /* !_HAVE_ARGV_FUZZ_INL */"

LINK NUMBER 125
Error fetching diff

LINK NUMBER 126
Error fetching diff

LINK NUMBER 127
Error fetching diff

LINK NUMBER 128
Not enough lines

LINK NUMBER 129

File path: cypress/pages/signin-page.js
"class SignInPage {
    // const for selectors in Home Page
    selectors = { 
        // define selector for new transaction input[name=""username""] input[name=""password""] form
        // to store username, password and submit locators
        // input[name=""username""] input[name=""password""] form
        username : () => cy.get('input[name=""username""]'),
        password : () => cy.get('input[name=""password""]'),
        submit : () => cy.get('form')
    }

    // define function for signin 
    login(username, password) {
            const urlSignin = 'http://localhost:3000/signin';
            cy.visit(urlSignin)
            this.selectors.username().click()
            this.selectors.username().type(username)
            this.selectors.password().click()
            this.selectors.password().type(password)
            this.selectors.submit()
    }
}

module.exports = new SignInPage();"

LINK NUMBER 130
Not enough lines

LINK NUMBER 131

File path: 214242Q_ASSN/__init__.py
"def countingSort(packageList):
    count = [0] * (max(packageList) + 1)
 
    for i in packageList:
        count[i] += 1
 
    i = 0
    for j in range(len(count)):
        for k in range(count[j]):
            packageList[i] = j
            i += 1
 
    return packageList

def radixSort(packageList):
    bucket = [[] for i in range(10)]
    maxLength = 0
    for i in packageList:
        if len(str(i[""Cost""])) > maxLength:
            maxLength = len(str(i[""Cost""]))
    for i in range(maxLength):
        for j in packageList:
            bucket[int(j[""Cost""]/(10**i)) % 10].append(j)
        packageList = []
        for z in bucket:
            packageList.extend(z)
    return packageList

def shellSort(packageList):
    n = len(packageList)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            temp = packageList[i]
            j = i
            while j >= gap and packageList[j-gap][""Customer Name""] > temp[""Customer Name""]:
                packageList[j] = packageList[j-gap]
                j -= gap
            packageList[j] = temp
        gap //= 2
"