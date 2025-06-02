// const express = require('express');

// mock the express app
const express = function() {
    return {
        use: function() {},
        get: function() {},
        listen: function() {}
    };
};
Object.defineProperty(express, 'static', {
    get: () => () => {}
});
