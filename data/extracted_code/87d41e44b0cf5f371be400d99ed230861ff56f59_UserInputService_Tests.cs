using Business.Helpers;
using Business.Services;
using Busniess.Models;
using Moq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xunit;

namespace UppgiftSeeSharp.Tests.Services;

public class UserInputService_Tests
{

    /* With the help of ChatGPT 4 i made this test
     * Since i cant moq properly my inputhandler i decided to create a class that is based on the inputhandler here instead
     * then we test this logic with asserts to compare the result to the given input string */
    /* The TestInputHandler class implements the InputHandler requirements ConsoleWrapper and adds the string _ inputs and currentInputIndex logic*/
    public class TestInputHandler : InputHandler
    {
        private readonly string[] _inputs;
        private int _currentInputIndex = 0;

        public TestInputHandler(string[] inputs, ConsoleWrapper consoleWrapper) : base(consoleWrapper)
        {
            _inputs = inputs;
        }

        /* Returns the value of the string at the current index and increments it */
        public override string GetInput(string prompt)
        {
            if(_currentInputIndex < _inputs.Length)
            {
                return _inputs[_currentInputIndex++];
            }
            return string.Empty;
        }
    }

    /* ChatGpt4 
     * This test that checks the logic with asserts to compare the result to the given input string *
     * With the help of the TestInputHandler class */
    [Fact]
    public void CollectUserData_ShouldReturnMockedUserRegistrationFormData()
    {

        // arrange
        var inputs = new String[]
        {
            "Test",
            "Testsson",
            "Test.Testsson@Test.com",
            "0760321142",
            "TestVagen 24",
            "325 12",
            "TestStaden"
        };

        var consoleWrapper = new ConsoleWrapper();
        var testInputHandler = new TestInputHandler(inputs, consoleWrapper);
        var userInputService = new UserInputService(testInputHandler);

        // act
        var result = userInputService.CollectUserData();


        // assert
        Assert.Equal("Test", result.FirstName);
        Assert.Equal("Testsson", result.LastName);
        Assert.Equal("Test.Testsson@Test.com", result.Email);
        Assert.Equal("0760321142", result.PhoneNumber);
        Assert.Equal("TestVagen 24", result.Address);
        Assert.Equal("325 12", result.PostalNumber);
        Assert.Equal("TestStaden", result.City);
        Assert.NotNull(result);
    }
}