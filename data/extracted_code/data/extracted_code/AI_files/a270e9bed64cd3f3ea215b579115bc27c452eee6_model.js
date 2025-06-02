    searchCourses(query) {
        const searchResults = this.courses.filter(course =>
            course.code.toLowerCase() === query.toLowerCase() ||
            course.name.toLowerCase().includes(query.toLowerCase()) ||
            course.description.toLowerCase().includes(query.toLowerCase())
        );
        this.setCurrentSearch(searchResults);
    }
};