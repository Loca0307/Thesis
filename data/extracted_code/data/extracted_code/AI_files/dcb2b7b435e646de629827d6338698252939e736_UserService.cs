using Business.Helpers;
using Busniess.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Business.Services;

/* By the suggestion of ChatGPT 4o im making a service for userinputs,
 * This will be used in the menu in order to keep SRP
 * Im moving the userRegistration code here and using the inputhandler aswell for SRP */
public class UserInputService(InputHandler inputHandler)
{
    private readonly InputHandler _inputHandler = inputHandler;

    public UserRegistrationForm CollectUserData()
    {
        return new UserRegistrationForm
        {
            // Get First Name
            FirstName = _inputHandler.GetInput("Enter your first name: "),

            // Get Last Name
            LastName = _inputHandler.GetInput("Enter your last name: "),

            // Get Email
            Email = _inputHandler.GetInput("Enter your email: "),

            // Get Phone Number
            PhoneNumber = _inputHandler.GetInput("Enter your phonenumber: "),

            // Get Street Address
            Address = _inputHandler.GetInput("Enter your street address: "),

            // Get Postal Number
            PostalNumber = _inputHandler.GetInput("Enter your postal number: "),

            // Get City
            City = _inputHandler.GetInput("Enter your city: ")
        };
    }
}