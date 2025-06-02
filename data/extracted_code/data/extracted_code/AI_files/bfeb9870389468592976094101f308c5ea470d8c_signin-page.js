class SignInPage {
    // const for selectors in Home Page
    selectors = { 
        // define selector for new transaction input[name="username"] input[name="password"] form
        // to store username, password and submit locators
        // input[name="username"] input[name="password"] form
        username : () => cy.get('input[name="username"]'),
        password : () => cy.get('input[name="password"]'),
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

module.exports = new SignInPage();