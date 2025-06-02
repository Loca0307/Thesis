
    //-------------------------------------------------------------------------------------------------
    //-------------------------------------------------------------------------------------------------
    //-------------------------------------------------------------------------------------------------

    public class DateValidationAttribute : ValidationAttribute //27/04/25 from chstGPT
    {
        private readonly int _minimumDate;
        private readonly int _maximumDate; //mine
        private readonly string _prefix; //mine
        private readonly string _suffix;

        public DateValidationAttribute(int minimumDate, int maximumDate, string prefix = "Employee", string suffix = " years old")
        {
            //note: prefix & suffix jic i need to expand this in the future. 27/04/25
            _minimumDate = minimumDate;
            _maximumDate = maximumDate; //mine
            _prefix = prefix; //mine
            this._suffix = suffix;
            ErrorMessage = $"{_prefix} must be between {_minimumDate} and {_maximumDate}{_suffix}."; //mine
        }

        protected override ValidationResult IsValid(object value, ValidationContext validationContext)
        {
            if ((value is DateOnly) || (value is DateTime))
            {
                DateOnly dob = value is DateTime ? DateOnly.FromDateTime((DateTime)value) : (DateOnly)value;

                var today = DateTime.Today;
                var age = today.Year - dob.Year;
                if (dob > DateOnly.FromDateTime(today.AddYears(-age))) age--;

                if ((age < _minimumDate) || (age > _maximumDate)) //mine
                {
                    return new ValidationResult(ErrorMessage);
                }

                return ValidationResult.Success!;
            }

            return new ValidationResult("Invalid date format.");
        }
    }
